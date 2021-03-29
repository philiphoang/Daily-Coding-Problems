/**
 * See if two numbers in the list add up to the value k
 * 
 * @param {List} arr List of numbers
 * @param {Number} k The value we are looking for
 * 
 * @return {Boolean} True if k exists in the list, false otherwise
 */
function doesArrayAddUpToK(arr, k) {
    var current_val = 0
    for (i in arr) {
        for (j in arr) {
            if (arr[i] !== arr[j]) {
                current_val = arr[i] + arr[j]
                // console.log(current_val)
                //Triple equals for matching on value and type
                if (current_val === k) { 
                    return true
                }
            }    
        }
    }
    return false
}

var example_array =  [10, 15, 3, 7]
var k = 17

console.log(doesArrayAddUpToK(example_array, k))
