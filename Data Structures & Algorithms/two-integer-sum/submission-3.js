class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const targetMap = new Map();

        for (let i = 0; i < nums.length; i++) {
            const cur = target - nums[i];
            if (targetMap.has(cur)) {
                return [i, targetMap.get(cur)];
            } 
            targetMap.set(nums[i], i);

        }
        return [];

    }
}
