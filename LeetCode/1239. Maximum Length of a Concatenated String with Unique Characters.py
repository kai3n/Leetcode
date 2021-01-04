class Solution:
    def maxLength(self, arr: List[str]) -> int:
        self.m = 0
        self.s = set()
        def helper(arr, s, l):
            if not arr:
                return
            for i in range(len(arr)):
                if any(c in s for c in arr[i]): continue
                if len(set(arr[i])) != len(arr[i]): continue
                self.m = max(self.m, l + len(arr[i]))
                for c in arr[i]:
                    s.add(c)
                helper(arr[i+1:], s, l + len(arr[i]))
                for c in arr[i]:
                    if c in s:
                        s.remove(c)
        helper(arr, self.s, 0)
        return self.m
                
