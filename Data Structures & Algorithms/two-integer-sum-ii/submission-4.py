class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        look = {}

        for i in range(len(numbers)):
            if numbers[i] in look:
                return [look[numbers[i]]+1, i+1]
            look[target - numbers[i]] = i
        return [-1, -1]
            
        