const fs = require('fs');

fs.readFile('./day_01/day1a_input.txt', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }

    const rows = data.split('\n');

    let result = [];

    rows.forEach(row => {
        const leftChar = row.match(/\d/)[0];
        const rightChar = row.match(/\d(?=\D*$)/)[0];

        const number = parseInt(leftChar + rightChar);

        result.push(number);
    });

    const sum = result.reduce((acc, curr) => acc + curr, 0);

    console.log(sum);
});