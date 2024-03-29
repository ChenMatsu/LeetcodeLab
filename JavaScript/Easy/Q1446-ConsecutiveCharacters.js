/**
 * @param {string} s
 * @return {number}
 */
var maxPower = function (s) {
    let max = 1,
        count = 1;

    for (let i = 1; i < s.length; i++) {
        if (s[i - 1] === s[i]) {
            count++;
            max = Math.max(max, count);
        } else count = 1;
    }

    return max;
};
