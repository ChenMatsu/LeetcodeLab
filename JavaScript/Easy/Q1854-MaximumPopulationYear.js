/**
 * @param {number[][]} logs
 * @return {number}
 */
var maximumPopulation = function (logs) {
    logs.sort((a, b) => a[0] - b[0]);

    let fYear = Infinity, max = -Infinity;
    const set = new Set();

    for (const log of logs) {
        const [birth, _] = log;
        if (!set.has(birth)) set.add(birth);
    }

    for (const year of [...set]) {
        let count = 0;
        for (const log of logs) {
            const [birth, death] = log;
            if (year >= birth && year < death) count++;
        }
        if (max < count) {
            max = count;
            fYear = year;
        }
    }
    return fYear;
};