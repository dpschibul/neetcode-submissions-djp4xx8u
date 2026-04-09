class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        if numCourses == 0:
            return True

        course_map = defaultdict(list)

        def dfs(cur, visit) -> bool:
            if cur == numCourses or cur not in course_map:
                return True
            if cur in visit:
                return False
            
            visit.add(cur)
            
            for course in course_map[cur]:
                if not dfs(course, visit):
                    return False
            return True

        for pre in prerequisites:
            course_map[pre[1]].append(pre[0])

        for num in range(numCourses):
            visited = set()
            if not dfs(num, visited):
                return False
        return True



        


# prerequisists = [[a, b] [b, c]] do a -> to be allowed to do b
# [[0,1],[1,0]].  a->b  b<-a
# visited = set -> {0 1 2}
# cur = 0->1->2
# [[0,1], [1,2], [2,0]] {0:1, 1:2, 1:5, 5:0} num courses 3 [0, 1, 2, 5]