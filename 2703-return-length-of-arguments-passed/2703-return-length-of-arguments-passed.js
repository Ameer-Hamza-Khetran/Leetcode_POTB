/**
 * @param {...(null|boolean|number|string|Array|Object)} args
 * @return {number}
 */
var argumentsLength = function(...args) {
    arguments = [...args]
    count = 0
    for(i=0; i < arguments.length; i++) {
        count += 1
    }
    return count
};

/**
 * argumentsLength(1, 2, 3); // 3
 */