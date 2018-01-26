class Vector2D(object):
    # Initialize your data structure here.
    def __init__(self, vec2d):
        self.col = 0
        self.row = 0
        self.vec = vec2d

    def next(self):
        result = self.vec[self.row][self.col]
        self.col += 1
        return result

    def hasNext(self):
        while self.row < len(self.vec):
            if self.col < len(self.vec[self.row]):
                return True

            self.col = 0
            self.row += 1
        return False