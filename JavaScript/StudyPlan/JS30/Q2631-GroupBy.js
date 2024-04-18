/**
 * @param {Function} fn
 * @return {Object}
 */
Array.prototype.groupBy = function(fn) {
    const map = {};

    for(let i = 0; i < this.length; i++) {
        if(fn(this[i]) in map) {
            map[fn(this[i])].push(this[i]);
        } else {
            map[fn(this[i])] = [this[i]];
        }
    }

    return map;
};

Array.prototype.groupBy = function(fn) {
    return this.reduce((grouped, item) => {
        const key = fn(item);
        if(!grouped[key]) grouped[key] = [];
        grouped[key].push(item);
        return grouped;
    }, {});
}

/**
 * [1,2,3].groupBy(String) // {"1":[1],"2":[2],"3":[3]}
 */