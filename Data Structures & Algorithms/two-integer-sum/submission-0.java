class Solution {
    public int[] twoSum(int[] nums, int target) {
    HashMap<Integer, Integer> map = new HashMap<>();

    for (int i = 0; i < nums.length; i++) {
        if (map.containsKey(nums[i])) {
            return new int[]{map.get(nums[i]), i};  // Corrected syntax for returning the array
        }
        map.put(target - nums[i], i);
    }

    return new int[]{};  // Corrected syntax for returning an empty array
}
}
