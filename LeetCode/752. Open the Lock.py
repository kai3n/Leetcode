class Solution:
    def openLock(self, deadends, target):
        """
        :type deadends: List[str]
        :type target: str
        :rtype: int
        """

        if target in deadends or '0000' in deadends:
            return -1

        if target == '0000':
            return 0

        min_step = 0
        deadends = set(deadends)
        deadends.add('0000')
        queue = collections.deque(['0000'])
        while queue:
            size = len(queue)
            for i in range(size):
                cur = queue.popleft()
                if cur == target:
                    return min_step
                trans = self.transform(cur)
                for tran in trans:
                    if tran not in deadends:
                        queue.append(tran)
                        deadends.add(tran)
            min_step += 1
        return -1

    def transform(self, target):
        transforms = []
        for i in range(len(target)):
            op1 = str((int(target[i]) + 1) % 10)  # 0 becomes 1, 9 becomes 0
            op2 = str((int(target[i]) + 9) % 10)  # 0 becomes 9, 9 becomes 8
            transforms.append(target[:i] + op1 + target[i + 1:])
            transforms.append(target[:i] + op2 + target[i + 1:])
        return transforms