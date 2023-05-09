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
  const emailEndsWith = document.querySelector('#email-endswith').value;

  if (categorySelect.value === '' || optionSelect.value === '') {
    // Move this console.log statement before the return statement
    console.log('You need to select a category and an option');
    return;
  }

if (emailEndsWith == 'false') {
  console.log('You need to login with student email id to access this content \n retry after login');
  if (optionSelect.value !== 'cs1001' && optionSelect.value !== 'ma1001' && optionSelect.value !== 'hs1001' && optionSelect.value !== 'ma1002') {
    alert('Retry after login\n\n login with student email id to access this content ');
  }
} 
  

  const url = `/pyq/${optionSelect.value}/${subjectselect.value}`;
  window.location.replace(url);
}

const categorySelect = document.getElementById('category-select');
categorySelect.addEventListener('change', categoryChanged);

const submitBtn = document.getElementById('submit-btn');
submitBtn.addEventListener('click', submitClicked);


