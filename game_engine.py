class Game:

    def __init__(self, width, height):
        self.width = width
        self.height = height
        self.board = [[" "] * height] * width
        self.turn = 0
        self.game_state = False

    def check_length(self, row, col, x, y):
        count = 0
        for i in range (1, 4):
            check_y = row + y * i
            check_x = col + x * i
            if check_y >= 0 and check_y < self.height and check_x >= 0 and check_x < self.width and self.board[col][row] == self.board[check_x][check_y]:
                count += 1
            else:
                return count
        return count

    def move(self, col):
        if self.game_state == False and col < len(self.board) and self.board[col][0] == " ":
            row = self.board.index(" ", -1)
            self.board[col][row] = self.turn
            self.turn ^= 1

            self.game_state =  self.check_length(row, col, 1, 0) + self.check_length(row, col, -1, 0) >= 3 or
                               self.check_length(row, col, 0, 1) + self.check_length(row, col, 0, -1) >= 3 or
                               self.check_length(row, col, 1, 1) + self.check_length(row, col, -1, -1) >= 3 or
                               self.check_length(row, col, -1, 1) + self.check_length(row, col, 1, -1) >= 3
        else:
            print("Move to column %i failed. Out of bounds or game already over." % col)
            return False