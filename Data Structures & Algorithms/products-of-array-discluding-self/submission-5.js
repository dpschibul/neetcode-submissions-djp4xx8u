class Solution {
    /**
     * @param {number[]} nums
     * @return {number[]}
     */
    
    productExceptSelf(arr) {
    const prefix = new Array(arr.length).fill(1);
    const suffix = new Array(arr.length).fill(1);

    for (let i = 1; i < arr.length; i++) {
        prefix[i] = arr[i-1] * prefix[i-1];
    }

    for (let j = arr.length-2; j >= 0; j--) {
        suffix[j] = arr[j+1] * suffix[j+1]
    }

    const res = []

    for (let i = 0; i < arr.length; i++) {
        res.push(prefix[i] * suffix[i])
    }

    return res

    }
}
