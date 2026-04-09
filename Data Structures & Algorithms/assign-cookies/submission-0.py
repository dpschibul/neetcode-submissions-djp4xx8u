class Solution:
    def findContentChildren(self, g: List[int], s: List[int]) -> int:
        g.sort()
        s.sort()

        greed = 0
        cookie = 0

        while greed < len(g) and cookie < len(s):
            if s[cookie] >= g[greed]:
                cookie+=1
                greed+=1
            else:
                cookie+=1
        
        return greed
        