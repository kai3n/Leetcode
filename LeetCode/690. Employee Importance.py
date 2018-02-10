"""
# Employee info
class Employee:
    def __init__(self, id, importance, subordinates):
        # It's the unique id of each node.
        # unique id of this employee
        self.id = id
        # the importance value of this employee
        self.importance = importance
        # the id of direct subordinates
        self.subordinates = subordinates
"""


class Solution:
    def getImportance(self, employees, id):
        """
        :type employees: Employee
        :type id: int
        :rtype: int
        """
        if not employees:
            return 0

        d = {i.id: [i.importance, i.subordinates] for i in employees}

        self.value = d[id][0]

        def helper(employee, visited):
            for e in d[employee][1]:
                if e not in visited:
                    visited.add(e)
                    self.value += d[e][0]
                    helper(e, visited, self.value)

        visited = set()
        visited.add(id)
        helper(id, visited)
        return self.value

