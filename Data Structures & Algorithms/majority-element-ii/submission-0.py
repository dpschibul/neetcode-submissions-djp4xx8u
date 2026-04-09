class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        res = []

        for key, count in counter.items():
            if count > (len(nums)//3):
                res.append(key)
        return res




        

        