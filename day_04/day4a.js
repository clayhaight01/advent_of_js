const fs = require('fs');

const inputText = fs.readFileSync('./day_04/day4_input.txt', 'utf-8');
const rows = inputText.split('\n');

var sum = 0
rows.forEach((row, index) => {
    cutCard = row.slice(8);
    const parts = cutCard.split('|');

    const convertToArray = (str) => {
        return str.trim().split(/\s+/).map(num => parseInt(num, 10));
    };
    const winning = convertToArray(parts[0]);
    const ours = convertToArray(parts[1]);
    var num_wins = 0
    ours.forEach(num => {
        if (winning.includes(num)) {
            num_wins += 1;
        };
    });
    sum += Math.floor(2**(num_wins-1))
})
console.log(sum)

