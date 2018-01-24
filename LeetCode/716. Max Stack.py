class MaxStack(object):

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stk=[]
        self.maxstk=[]

    def push(self, x):
        """
        :type x: int
        :rtype: void
        """
        self.stk.append(x)
        if not self.maxstk:
            self.maxstk.append(x)
        else:
            self.maxstk.append(max(x,self.maxstk[-1]))

    def pop(self):
        """
        :rtype: int
        """
        self.maxstk.pop()
        return self.stk.pop()
    def top(self):
        """
        :rtype: int
        """
        return self.stk[-1]

    def peekMax(self):
        """
        :rtype: int
        """
        return self.maxstk[-1]

    def popMax(self):
        """
        :rtype: int
        """
        n=self.maxstk.pop()
        i=len(self.stk)-1
        tmp=[]
        while n!=self.stk[-1]:
            tmp.append(self.pop())
        ret=self.stk.pop()
        for i in xrange(len(tmp)-1,-1,-1):
            self.push(tmp[i])
        return ret