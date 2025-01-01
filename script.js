// Replace with your actual birth year
const birthYear = 1996;

function calculateAge() {
  const currentYear = new Date().getFullYear(); // Get the current year
  const age = currentYear - birthYear; // Calculate the age
  return age;
}

// Update the HTML element with the calculated age
document.getElementById("age").textContent = calculateAge();
