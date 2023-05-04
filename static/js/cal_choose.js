function clearFormFields() {
  const quiz = document.getElementById('quiz-inputs');
  const oppe = document.getElementById('oppe-inputs');
  const gaa = document.getElementById('gaa');
  const oppe1 = document.getElementById('oppe1');
  const oppe2 = document.getElementById('oppe2');
  const qz1 = document.getElementById('quiz1');
  const qz2 = document.getElementById('quiz2');
  const end = document.getElementById('end');
  const bonus = document.getElementById('bonus');

  quiz.value = '';
  oppe.value = '';
  gaa.value = '';
  oppe1.value = '';
  oppe2.value = '';
  qz1.value = '';
  qz2.value = '';
}

window.addEventListener('load', clearFormFields);


const quiz = document.getElementById('quiz-inputs');
const oppe = document.getElementById('oppe-inputs');
const gaa = document.getElementById('gaa');
const oppe1 = document.getElementById('oppe1');
const oppe2 = document.getElementById('oppe2');
const qz1 = document.getElementById('quiz1');
const qz2 = document.getElementById('quiz2');
const end = document.getElementById('end');
const bonus = document.getElementById('bonus');

function categoryChanged() {
  const categorySelect = document.getElementById('category-select');
  const optionSelect = document.getElementById('option-select');
  
  // Clear the options in the option select box
  optionSelect.innerHTML = '<option value="">Select an option</option>';
  
  if (categorySelect.value === '') {
    return;
  }
  
  // Make a request to your Flask app to get the options for the selected category
  fetch(`/get_options/${categorySelect.value}`)
    .then(response => response.json())
    .then(options => {
      // Add the options to the option select box
      options.forEach(option => {
        const optionElement = document.createElement('option');
        optionElement.value = option.value;
        optionElement.textContent = option.label;
        optionSelect.appendChild(optionElement);
      });
    });
}

const optionSelected = document.getElementById('option-select');
let selectedOption = '';

optionSelected.addEventListener('change', (event) => {
  selectedOption = event.target.value;
  console.log(selectedOption);
      if (selectedOption.startsWith('cs') & selectedOption != 'cs1001') {
        console.log(selectedOption.startsWith('cs'));
        oppe.style.display = 'block';
        quiz.style.display = 'None'
        console.log(oppe.innerHTML);
      } else {
        quiz.style.display = 'block';
        oppe.style.display = 'None';
        console.log('done dn');
      }
});

function calculate(GAA, F, Qz1, PE1, PE2, bonus ) {
  const term1 = 0.1 * GAA;
  const term2 = 0.1 * Qz1;
  const term3a = 0.5 * F;
  const term3b = 0.2 * Math.max(PE1, PE2);
  const term4a = 0.4 * F;
  const term4b = 0.3 * Math.max(PE1, PE2);
  const term4c = 0.1 * Math.min(PE1, PE2);

  const term3 = term3a + term3b;
  const term4 = term4a + term4b + term4c;

  const T = term1 + term2 + Math.max(term3, term4) + bonus;
  let grade;
  if (PE1 > 40 | PE2> 40) { 
       if (T >= 90) {
          grade = '10, S';
        } else if (T >= 80) {
          grade = '9,  A ';
        } else if (T >= 70) {
          grade = '8, B';
        } else if (T >= 60) {
          grade = '7, C';
        } else if (T >= 50) {
          grade = '6, D';
        } else if (T >= 40) {
          grade = '4, E';
        } else {
          grade = 'U  Fail';
        }
    } else{
      grade = 'U || Fail oppe > 40'
    }

  return { T, grade };

}


function calculateT(GAA, F, Qz1, Qz2, bonus) {
  const term1 = 0.1 * GAA;
  const term2a = 0.6 * F;
  const term2b = 0.2 * Math.max(Qz1, Qz2);
  const term3a = 0.4 * F;
  const term3b = 0.2 * Qz1;
  const term3c = 0.3 * Qz2;

  const term2 = term2a + term2b;
  const term3 = term3a + term3b + term3c;

  const T = term1 + Math.max(term2, term3) + bonus;
  let grade;
  if (T >= 90) {
    grade = '10, S';
  } else if (T >= 80) {
    grade = '9,  A ';
  } else if (T >= 70) {
    grade = '8, B';
  } else if (T >= 60) {
    grade = '7, C';
  } else if (T >= 50) {
    grade = '6, D';
  } else if (T >= 40) {
    grade = '4, E';
  } else {
    grade = 'U  Fail';
  }

  return { T, grade };

}

const modal = document.getElementById("modal");

// Get the <span> element that closes the modal
const span = document.getElementsByClassName("close")[0];

// Get the <p> element where the result will be displayed
const resultElem = document.getElementById("result");
const resultScore = document.getElementById("score")


function submitClicked() {
  const categorySelect = document.getElementById('category-select');
  const optionSelect = document.getElementById('option-select');
  

  // const end = document.getElementById('quiz1');


  if (categorySelect.value === '' || optionSelect.value === '') {
    return;
  }
    if (qz2.value !== '' & end.value === '') {
      const url = `/cal/${categorySelect.value}/${optionSelect.value}/${gaa.value}/${qz1.value}/${qz2.value}_${end.value}`;
      window.location.href = url;
    } else if (oppe1.value !== '' & oppe2.value != '' & end.value === '') {
      const url = `/cal/${categorySelect.value}/${optionSelect.value}/${gaa.value}/${qz1.value}/${oppe1.value}_${oppe2.value}_${end.value}`;
      window.location.href = url;
    } else   if (qz2.value !== '' & end.value !== '') {  
    const result = calculateT(gaa.value, end.value, qz1.value, qz2.value, parseFloat(bonus.value));
    const grade = result.grade; // get the letter grade
    const tWithGrade = `Final Score : ${result.T.toFixed(2)}`; // concatenate T and the letter grade
    const tScore = `Grade : ${grade}`;
    resultElem.textContent = tWithGrade;
    resultScore.textContent = tScore;
    modal.style.display = "block";


// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

  } else if (oppe1.value !== '' & oppe2.value != '' & end.value !== '') {
  const result = calculate(gaa.value, end.value, qz1.value, oppe1.value, oppe2.value, parseFloat(bonus.value));
    const grade = result.grade; // get the letter grade
    const tWithGrade = `Final Score: ${result.T.toFixed(2)}`; // concatenate T and the letter grade
    const tScore = `Grade : ${grade}`;
    resultElem.textContent = tWithGrade;
    resultScore.textContent = tScore;
    modal.style.display = "block";

// When the user clicks on <span> (x), close the modal
span.onclick = function() {
  modal.style.display = "none";
}

// When the user clicks anywhere outside of the modal, close it
window.onclick = function(event) {
  if (event.target == modal) {
    modal.style.display = "none";
  }
}

  }

} 

const categorySelect = document.getElementById('category-select');
categorySelect.addEventListener('change', categoryChanged);

const submitBtn = document.getElementById('submit-btn');
submitBtn.addEventListener('click', submitClicked);