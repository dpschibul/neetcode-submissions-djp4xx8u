class Solution:
    def minWindow(self, s: str, t: str) -> str:
        if len(t) > len(s):
            return ""
        tmap = [0] * 26 * 2
        
        for c in t: 
            tmap[self.getIndexForChar(c)] += 1
        
        scan = len(t)
        l = 0 
        while True:
            if scan > len(s):
                break
            while l + scan <= len(s):
                r = l+scan
                if self.compareWithMap(s[l:r], tmap):
                    return s[l:r]
                l+=1

            l = 0
            scan += 1
        return ""




    def compareWithMap(self, s, tMap) -> bool:
        sMap = [0] * 26 * 2
        for c in s:
            sMap[self.getIndexForChar(c)] += 1

        for i in range(26 * 2):
            if sMap[i] < tMap[i]:
                return False
        return True

        
    def getIndexForChar(self, c) -> int:
        if (ord(c) >= ord('a') and ord(c) <= ord('z')):
            return ord(c) - ord('a')
        elif (ord(c) >= ord('A') and ord(c) <= ord('Z')):
            return ord(c) - ord('A') + 26
        return -1


        