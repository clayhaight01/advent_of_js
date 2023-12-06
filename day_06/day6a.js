const fs = require('fs');

// Read file and split into lines
const f = "day_06/day6_input.txt";
const lines = fs.readFileSync(f, 'utf8').split('\n');

// Extract and convert time and distance data
const timeData = lines[0].split(' ').slice(1).map(Number);
const distanceData = lines[1].split(' ').slice(1).map(Number);
const tds = timeData.map((t, i) => [t, distanceData[i]]);

let numWays = tds.map(td => {
    let ways = 0;
    for (let v = 0; v <= td[0]; v++) {
        let d = v * (td[0] - v);
        if (d > td[1]) ways++;
    }
    return ways;
});

console.log(numWays);

// Calculate the final result
let result = numWays.reduce((acc, val) => acc * val, 1);
console.log(result);