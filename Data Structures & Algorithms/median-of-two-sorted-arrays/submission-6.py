class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        A, B = nums1, nums2
        total = len(nums1) + len(nums2)
        half = total // 2

        if len(A) > len(B):
            A, B = B, A
        
        l, r = 0, len(A) - 1

        while True:
            aP = (l+r)//2
            bP = half - aP - 2

            print(r)
            Aleft = A[aP] if aP >= 0 else float("-infinity")
            Aright = A[aP + 1] if aP + 1 < len(A) else float("infinity")
            Bleft = B[bP] if bP >= 0 else float("-infinity")
            Bright = B[bP + 1] if bP + 1 < len(B) else float("infinity")

            if Aleft <= Bright and Bleft <= Aright:
                if total % 2 == 1:
                    return min(Aright, Bright)
                else:
                    return (max(Aleft, Bleft) + min(Aright, Bright)) / 2
            elif Aleft > Bright:
                r = aP - 1
            else:
                l = aP + 1 


