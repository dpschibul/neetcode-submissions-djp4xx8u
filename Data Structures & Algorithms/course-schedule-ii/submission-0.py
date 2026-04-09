class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        course_map = defaultdict(list)
        res = []

        for pre in prerequisites:
            course_map[pre[0]].append(pre[1])
        
        visited, cycle = set(), set()

        def dfs(course) -> bool :
            if course in cycle:
                return False
            if course in visited:
                return True

            cycle.add(course)

            for crs in course_map[course]:
                if not dfs(crs):
                    return False

            cycle.remove(course)
            visited.add(course)
            res.append(course)
            return True

        for n in range(numCourses):
            if not dfs(n):
                return []
        
        for n in range(numCourses):
            if n not in visited:
                res.append(n)

        return res
        

        

#  numcourses = 3 -> 0, 1, 2 , 3 
# [[0,1],[1,2],[2,3]]
# course_map = {1:0, 2: 1, 3: 2} 1->0 2->1 3->2

