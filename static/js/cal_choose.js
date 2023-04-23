function clearFormFields() {
  const quiz = document.getElementById('quiz-inputs');
  const oppe = document.getElementById('oppe-inputs');
  const gaa = document.getElementById('gaa');
  const oppe1 = document.getElementById('oppe1');
  const oppe2 = document.getElementById('oppe2');
  const qz1 = document.getElementById('quiz1');
  const qz2 = document.getElementById('quiz2');

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
        oppe.style.display = 'None'
        console.log('done dn')
      }
});


function submitClicked() {
  const categorySelect = document.getElementById('category-select');
  const optionSelect = document.getElementById('option-select');
  // const gaa = document.getElementById('gaa');
  

  // const end = document.getElementById('quiz1');


  if (categorySelect.value === '' || optionSelect.value === '') {
    return;
  }
    if (qz2.value !== '') {
      const url = `/cal/${categorySelect.value}/${optionSelect.value}/${gaa.value}/${qz1.value}/${qz2.value}`;
      window.location.href = url;
    } else if (oppe1.value !== '' & oppe2.value != '') {
      const url = `/cal/${categorySelect.value}/${optionSelect.value}/${gaa.value}/${qz1.value}/${oppe1.value}_${oppe2.value}`;
      window.location.href = url;
    }

}

const categorySelect = document.getElementById('category-select');
categorySelect.addEventListener('change', categoryChanged);

const submitBtn = document.getElementById('submit-btn');
submitBtn.addEventListener('click', submitClicked);
