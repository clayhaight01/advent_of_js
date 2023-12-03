const fs = require('fs');

fs.readFile('./day_03/day3a_input.txt', 'utf8', (err, data) => {
    if (err) {
        console.error(err);
        return;
    }

    const rows = data.split('\n');
    const expandedArrays = []; // 2D array to store expanded arrays

    rows.forEach(row => {
        const booleanArray = Array.from(row).map(char => {
            return (char === '.' || !isNaN(char)) ? false : true;
        });
        const expandedArray = Array.from(booleanArray, () => false);
        booleanArray.map((value, index) => {
            if (value) {
                expandedArray[index] = true;
                if (index > 0) expandedArray[index - 1] = true; // left
                if (index < expandedArray.length - 1) expandedArray[index + 1] = true; // right
            }
            return value;
        });

        expandedArrays.push(expandedArray); // append expandedArray to expandedArrays
    });
    const upArray = expandedArrays.slice(1);
    upArray.push(Array.from(expandedArrays[0], () => false));
    const downArray = expandedArrays.slice(0, -1);
    downArray.unshift(Array.from(expandedArrays[0], () => false));
    
    expandedArrays.forEach(row => {
        row.forEach((value, index) => {
            if (value || upArray[expandedArrays.indexOf(row)][index] || downArray[expandedArrays.indexOf(row)][index]) {
                row[index] = true;
            }
        });
    });
    const nums2sum = Array.from(expandedArrays, () => Array(expandedArrays[0].length).fill(" "));

    rows.forEach(row => {
        rowArray = row.split("");
        rowArray.forEach((value, index) => {
            if (!isNaN(value) && expandedArrays[rows.indexOf(row)][index]) {
                nums2sum[rows.indexOf(row)][index] = value.toString();
            }
        });
    });
    nums2sum.forEach(row => {
        const rowString = row.join("");
    });
});
