const fs = require('fs');

// Read the input text file
const inputText = fs.readFileSync('./day_02/day2a_input.txt', 'utf-8');

// Initialize the arrays for red, blue, and green

const max_cubes = [12, 14, 13]; // RBG
let sum = 0;

// Split the input text into rows
const rows = inputText.split('\n');

// Iterate over each row
rows.forEach((row, index) => {
    const red = [];
    const blue = [];
    const green = [];
  // Extract the color and numbers from the row
  const matches = row.match(/(\d+)\s+(\w+)/g);
  
  // Iterate over each match
  matches.forEach(match => {
    // Extract the number and color from the match
    const [number, color] = match.split(' ');
    
    // Store the number in the corresponding color array
    if (color === 'red') {
      red.push(Number(number));
    } else if (color === 'blue') {
      blue.push(Number(number));
    } else if (color === 'green') {
      green.push(Number(number));
    }
    
  });
// Find the maximum value in red, blue, and green arrays
const maxRed = Math.max(...red);
const maxBlue = Math.max(...blue);
const maxGreen = Math.max(...green);

cube_power = maxRed * maxBlue * maxGreen
// if (maxRed <= max_cubes[0] && maxBlue <= max_cubes[1] && maxGreen <= max_cubes[2]) {sum += (index + 1); console.log("index",index)}
sum += cube_power
});
console.log('sum:', sum);
