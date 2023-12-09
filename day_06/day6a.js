const fs = require('fs');

const f = "day_06/day6_input.txt";
const lines = fs.readFileSync(f, 'utf8').trim().split('\n');

function processLine(line) {
    return line.split(' ')
               .map(Number)
               .filter(num => num !== 0);
}

const timeData = processLine(lines[0]);
const distanceData = processLine(lines[1]);

if (timeData.length !== distanceData.length) {
    throw new Error('Mismatched lengths of time and distance data');
}

const tds = timeData.map((time, index) => [time, distanceData[index]]);

let numWays = tds.map(([time, distance]) => {
    let ways = 0;
    for (let v = 0; v <= time; v++) {
        let d = v * (time - v);
        if (d > distance) ways++;
    }
    return ways;
});

console.log(numWays);

let result = numWays.reduce((acc, val) => acc * val, 1);
console.log(result);
