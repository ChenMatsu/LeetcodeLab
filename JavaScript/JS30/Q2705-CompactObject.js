/**
 * @param {Object|Array} obj
 * @return {Object|Array}
 */
var compactObject = function(obj) {
    if(!obj) return null;
    if(Array.isArray(obj)) return obj.filter(Boolean).map(compactObject);
    if(typeof obj !== "object") return obj;

    const compact = {};
    for(const key in obj) {
        let value = compactObject(obj[key]);
        if(Boolean(value)) compact[key] = value;
    }
    return compact;
}