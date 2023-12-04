const fs = require('fs');

const inputText = fs.readFileSync('./day_04/day4_input.txt', 'utf-8');
const rows = inputText.split('\n');

const multiplier = Array.from({ length: rows.length }, () => 1);
rows.forEach((row, r) => {
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
    for (let i = 0; i < num_wins; i++) {
        multiplier[r+i+1] += multiplier[r]
    }
})
var sum = multiplier.reduce((acc, curr) => acc + curr, 0);
console.log(sum)

