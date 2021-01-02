class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        
        ones = len([student for student in students if student])
        zeros = len(students) - ones
        for i in range(len(sandwiches)):
            if sandwiches[i] and ones > 0:
                ones -= 1
            elif not sandwiches[i] and zeros > 0:
                zeros -= 1
            else:
                break
        return ones + zeros
            
