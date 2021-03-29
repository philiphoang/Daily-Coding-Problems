/**
 * Calculate the product of all numbers at index i except for i itself
 * 
 * @param {*} arr List of numbers
 * 
 * @return {List} List containing the product of all numbers except the number at i
 */
function productOfAllNumbers(arr) {
    result_list = []

    for (i in arr) {
        sum = 1
        for (j in arr) {
            if (arr[i] !== arr[j]) {
                sum = sum * arr[j]
            }
        }
        result_list.push(sum)
    }

    return result_list
}

console.log(productOfAllNumbers([1, 2, 3, 4, 5]))

console.log(productOfAllNumbers([3, 2, 1]))

