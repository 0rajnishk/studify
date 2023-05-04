const form = document.querySelector('#marks-form');
const resultTable = document.querySelector('#result table tbody');
form.addEventListener('submit', function (event) {
  event.preventDefault(); // prevent the form from submitting and refreshing the page
  if (secondDropdown.value === 'cs1001') {
    const subject = secondDropdown.value;
    const ga = parseInt(form.elements.ga.value);
    const qz1 = parseInt(form.elements.qz1.value);
    const pe1 = parseInt(form.elements.pe1.value);
    const pe2 = parseInt(form.elements.pe2.value);

    let arr = [0, 0, 0, 0, 0, 0]
    for (let i = 0, j = 40; i < arr.length; i++, j += 10) {
      const num1 = (j - ((0.1 * ga) + (0.1 * qz1) + (0.3 * (Math.max(pe1, pe2))) + (0.1 * (Math.min(pe1, pe2))))) / 0.4;
      const num2 = (j - ((0.1 * ga) + (0.1 * qz1) + (0.2 * (Math.max(pe1, pe2))))) / 0.5;
      if (num1 < num2) {
        if (num1 <= 100) {
          arr[i] = num1 <= 0 ? "Already Passed" : num1.toFixed(2);;
        }
        else {
          arr[i] = "not possible"
        }
      }
      else {
        if (num2 <= 100) {
          arr[i] = num2 <= 0 ? "Already Passed" : num2.toFixed(2);;
        }
        else {
          arr[i] = "not possible"
        }
      }
    }
  }

  else {
    const subject = secondDropdown.value;
    const ga = parseInt(form.elements.ga.value);
    const qz1 = parseInt(form.elements.qz1.value);
    const qz2 = parseInt(form.elements.qz2.value);

    let arr = [0, 0, 0, 0, 0, 0]
    for (let i = 0, j = 40; i < arr.length; i++, j += 10) {
      const num1 = (j - ((0.1 * ga) + (0.2 * qz1) + (0.3 * qz2))) / 0.4;
      const num2 = (j - ((0.1 * ga) + (0.2 * (Math.max(qz1, qz2))))) / 0.6;
      if (num1 < num2) {
        if (num1 <= 100) {
          arr[i] = num1 <= 0 ? "Already Passed" : num1.toFixed(2);;
        }
        else {
          arr[i] = "not possible"
        }
      }
      else {
        if (num2 <= 100) {
          arr[i] = num2 <= 0 ? "Already Passed" : num2.toFixed(2);;
        }
        else {
          arr[i] = "not possible"
        }
      }
    }

  }
  calc.classList.add('hidden');
});


























