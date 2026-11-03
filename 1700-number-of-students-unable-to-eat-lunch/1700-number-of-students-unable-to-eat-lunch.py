class Solution:
    def countStudents(self, students: list[int], sandwiches: list[int]) -> int:
        count = [students.count(0), students.count(1)]
        for i in sandwiches:
            if count[i] == 0:
                return sum(count)
            count[i] -= 1
        return 0