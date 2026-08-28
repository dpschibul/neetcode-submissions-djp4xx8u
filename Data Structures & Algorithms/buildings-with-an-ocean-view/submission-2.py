class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        largest_at = [h for h in heights]
        res = [len(heights) - 1]
        for i in range(len(heights)-2, -1, -1):
            if largest_at[i] > largest_at[i + 1]:
                res.append(i)

            largest_at[i] = max(largest_at[i], largest_at[i + 1])
        
        
        return sorted(res)




        