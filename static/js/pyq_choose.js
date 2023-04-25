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

function submitClicked() {
  const categorySelect = document.getElementById('category-select');
  const optionSelect = document.getElementById('option-select');
  const subjectselect = document.getElementById('subject-select');


  if (categorySelect.value === '' || optionSelect.value === '') {
    return;
  }

  const url = `/pyq/${optionSelect.value}/${subjectselect.value}`;
  window.location.href = url;
}

const categorySelect = document.getElementById('category-select');
categorySelect.addEventListener('change', categoryChanged);

const submitBtn = document.getElementById('submit-btn');
submitBtn.addEventListener('click', submitClicked);



// function categoryChanged() {
//   const categorySelect = document.getElementById('category-select');
//   const optionSelect = document.getElementById('option-select');
  
//   // Clear the options in the option select box
//   optionSelect.innerHTML = '<option value="">Select an option</option>';
  
//   if (categorySelect.value === '') {
//     return;
//   }
  
//   // Make a request to your Flask app to get the options for the selected category
//   fetch(`/get_options/${categorySelect.value}`)
//     .then(response => response.json())
//     .then(options => {
//       // Add the options to the option select box
//       options.forEach(option => {
//         const optionElement = document.createElement('option');
//         optionElement.value = option.value;
//         optionElement.textContent = option.label;
//         optionSelect.appendChild(optionElement);
//       });
//     });
// }

// const categorySelect = document.getElementById('category-select');
// categorySelect.addEventListener('change', categoryChanged);