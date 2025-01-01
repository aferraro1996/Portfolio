// Set your exact Date of Birth (DOB)
const birthDate = new Date('1996-10-25'); // Example: YYYY-MM-DD

// Function to calculate the age based on DOB
function calculateAge() {
  const currentDate = new Date(); // Get the current date
  let age = currentDate.getFullYear() - birthDate.getFullYear(); // Initial age calculation

  // Adjust age if birthday hasn't occurred yet this year
  const monthDifference = currentDate.getMonth() - birthDate.getMonth();
  const dayDifference = currentDate.getDate() - birthDate.getDate();

  if (monthDifference < 0 || (monthDifference === 0 && dayDifference < 0)) {
    age--; // Decrease age if birthday hasn't happened yet this year
  }

  return age;
}

// Update the element with the id "age" with the calculated age
document.getElementById("age").textContent = calculateAge();
