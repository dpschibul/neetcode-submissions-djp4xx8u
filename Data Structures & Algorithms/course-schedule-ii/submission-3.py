class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:

        pre_req = defaultdict(list)
        indegree = [0] * numCourses

        for courses in prerequisites:
            pre_req[courses[0]].append(courses[1])
            indegree[courses[1]] += 1
        
        q = deque()
        for course in range(numCourses):
            if indegree[course] == 0:
                q.append(course)
        
        course_order = []

        while q:
            course = q.pop()
            course_order.append(course)

            for nei in pre_req[course]:
                indegree[nei] -= 1
                if indegree[nei] == 0:
                    q.append(nei)
        print(course_order)
        if len(course_order) != numCourses:
            return []
        return course_order[::-1]






        