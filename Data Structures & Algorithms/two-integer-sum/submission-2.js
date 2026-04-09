class Solution {
    /**
     * @param {number[]} nums
     * @param {number} target
     * @return {number[]}
     */
    twoSum(nums, target) {
        const targetMap = new Map();

        for (const i in nums) {
            const cur = target - nums[i];
            if (targetMap.has(cur)) {
                return [Number(i), targetMap.get(cur)];
            } else {
                targetMap.set(Number(nums[i]), Number(i));
            }
        }
        return [-1, -1];

    }
}
