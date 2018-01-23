class Solution:
    def findItinerary(self, tickets):
        """
        :type tickets: List[List[str]]
        :rtype: List[str]
        """
        from collections import defaultdict

        g = defaultdict(list)
        res = ['JFK']
        for ticket in tickets:
            g[ticket[0]].append(ticket[1])

        def helper(airport):
            if len(res) == len(tickets) + 1:
                return res
            for n in sorted(g[airport]):
                g[airport].remove(n)
                res.append(n)
                worked = helper(n)
                if worked:
                    return worked
                res.pop()
                g[airport].append(n)
            return []

        return helper('JFK')