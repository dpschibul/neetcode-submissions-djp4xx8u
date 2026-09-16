class Solution:
    def relativeSortArray(self, arr1: List[int], arr2: List[int]) -> List[int]:
        arr1_count = Counter(arr1)

        idx = 0

        for i in range(len(arr1)):
            if idx == len(arr2):
                break
            arr1_count[arr2[idx]] -= 1

            arr1[i] = arr2[idx]

            if arr1_count[arr2[idx]] == 0:
                idx += 1
        
        left_over = []
        for key, val in arr1_count.items():
            count = val
            while count > 0:
                left_over.append(key)
                count -= 1
        left_over.sort()
        print(left_over)
        for i in range(len(left_over)):
            arr1[len(arr1) - len(left_over) + i] = left_over[i]
        return arr1
            



        