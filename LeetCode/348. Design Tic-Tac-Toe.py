class TicTacToe(object):
    def __init__(self, n):
        import collections
        self.count = collections.Counter()
        self.n = n

    def move(self, row, col, player):
        for i, x in enumerate((row, col, row + col, row - col)):
            print(i, x, player)
            self.count[i, x, player] += 1
            if self.count[i, x, player] == self.n:
                return player
        return 0