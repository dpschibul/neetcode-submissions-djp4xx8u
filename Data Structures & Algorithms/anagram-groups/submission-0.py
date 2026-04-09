class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        solutionDict = {}
        for s in strs:
            sortedString = "".join(sorted(s))
            if sortedString in solutionDict:
                solutionDict[sortedString].append(s) 
            else:
                solutionDict[sortedString] = [s]

        return list(solutionDict.values())
        