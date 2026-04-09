class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        most_freq = {}
        res = []

        for n in nums:
            if n in most_freq or len(most_freq) < 2:
                most_freq[n] = most_freq.get(n, 0) + 1
            else:
                to_delete = []
                for elem, freq in most_freq.items():
                    most_freq[elem]-=1
                    if most_freq[elem] == 0:
                        to_delete.append(elem)
                for elem in to_delete:
                    del most_freq[elem]
        
        for elem in most_freq.keys():
            if nums.count(elem) > len(nums) // 3:
                res.append(elem)
        return res
                
                    

        




        

        