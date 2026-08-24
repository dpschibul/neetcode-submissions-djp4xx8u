class Solution:
    def replaceElements(self, arr: List[int]) -> List[int]:
        res = [0] * len(arr)

        for i in range(len(arr)-1, -1, -1):
            if i == len(arr) - 1:
                res[i] = -1
            else:
                res[i] = max(res[i + 1], arr[i + 1])
        return res
        