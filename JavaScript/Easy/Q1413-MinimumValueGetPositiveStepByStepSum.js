/**
 * @param {number[]} nums
 * @return {number}
 */
var minStartValue = function (nums) {
    let min = 0,
        total = 0;

    for (let i = 0; i < nums.length; i++) {
        total += nums[i];
        min = Math.min(min, total);
    }

    return -min + 1;
};
