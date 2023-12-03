const fs = require('fs');

fs.readFile('./day_01/day1a_input.txt', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }

    const rows = data.split('\n');

    let result = [];

    const digitWords = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine'];
    const reversedDigitWords = digitWords.map(word => word.split('').reverse().join(''));


    rows.forEach(row => {
        const leftMatch = row.match(new RegExp('^.*?(' + digitWords.join('|') + ')', 'i'))?.[1];
        const rightMatch = row.match(new RegExp('(' + digitWords.join('|') + ').*$', 'i'))?.[1];
        console.log(rightMatch);
        const leftNumber = leftMatch ? digitWords.indexOf(leftMatch.toLowerCase()) + 1 : '';
        const rightNumber = rightMatch ? digitWords.indexOf(rightMatch.split('').reverse().join('').toLowerCase()) + 1 : '';
        const number = parseInt(leftNumber + rightNumber) || null;
        result.push(number);
        console.log(leftMatch, rightMatch);
    });

    const sum = result.reduce((acc, curr) => acc + curr, 0);

    console.log('Sum:', sum);
});