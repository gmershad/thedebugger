class Solution(object):
    def countStudents(self, students, sandwiches):
        """
        :type students: List[int]
        :type sandwiches: List[int]
        :rtype: int
        """
        count = 0
        
        while students:
            student = students.pop(0)
            if student == sandwiches[0]:
                count = 0
                sandwiches.pop(0)
            else:
                count += 1
                students.append(student)
            
            if count == len(students):
                break
        
        return len(students)
        
