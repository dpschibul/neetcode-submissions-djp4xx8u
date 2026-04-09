class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        visited = {}

        for i, n in enumerate(nums):
            if n in visited:
                return [visited[n], i]
            visited[target-n] = i
        return [-1,-1]
        