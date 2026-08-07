class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:

        stud = Counter(students)
        
        for i in range(len(sandwiches)):
            s = sandwiches[i]
            
            if (s in stud and stud[s] == 0) or s not in stud:
                return stud.get(0, 0) + stud.get(1, 0)

            stud[s] -= 1
        
        return 0


        