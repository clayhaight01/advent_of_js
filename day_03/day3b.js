const fs = require('fs');

fs.readFile('day_03/day3_input.txt', 'utf8', function(err, data) {
    if (err) {
        console.error("Error reading file:", err);
        return;
    }
    let charactersArray = data.split('\n').map(line => line.trim());

    let rows = charactersArray.length;
    let cols = rows ? charactersArray[0].length : 0;
    let visited = charactersArray.map(row => Array(row.length).fill(false));
    let sum = 0;

    for (let i = 0; i < rows; i++) {
        for (let j = 0; j < charactersArray[i].length; j++) {
            if (charactersArray[i][j] === '*') {
                let ratio = 0;
                for (let x = Math.max(0, i - 1); x < Math.min(i + 2, rows); x++) {
                    for (let y = Math.max(0, j - 1); y < Math.min(j + 2, cols); y++) {
                        if (!isNaN(parseInt(charactersArray[x][y])) && !visited[x][y]) {
                            let jTemp = y;
                            while (jTemp > 0 && !isNaN(parseInt(charactersArray[x][jTemp - 1]))) {
                                jTemp -= 1;
                            }
                            let pnum = parseInt(charactersArray[x][jTemp]);
                            visited[x][jTemp] = true;
                            while (jTemp + 1 < cols && !isNaN(parseInt(charactersArray[x][jTemp + 1]))) {
                                jTemp += 1;
                                pnum = pnum * 10 + parseInt(charactersArray[x][jTemp]);
                                visited[x][jTemp] = true;
                            }
                            if (ratio > 0) {
                                sum += pnum * ratio;
                            }
                            ratio = pnum;
                        }
                    }
                }
            }
        }
    }
    console.log(sum);
});
