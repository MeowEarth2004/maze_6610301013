import os
import time
import keyboard  # Import the keyboard module

class Maze:
    def __init__(self) -> None:
        self.maze = [
            ["X", "X", "X", "X", "X", "X", "X"],
            ["X", " ", " ", " ", "X", " ", "X"],
            ["X", " ", "X", " ", "X", " ", " "],
            ["X", " ", "X", " ", "X", " ", "X"],
            ["X", " ", "X", " ", " ", " ", "X"],
            ["X", " ", "X", "X", "X", "X", "X"],
        ]
        self.ply = pos(5, 1)
        self.end = pos(2, 6)
        self.maze[self.ply.y][self.ply.x] = "P"
        self.maze[self.end.y][self.end.x] = "E"

    def is_in_bound(self, y, x):
        return 0 <= y < len(self.maze) and 0 <= x < len(self.maze[0])

    def print_board(self):
        os.system("cls")
        print("\n\n\n")
        for row in self.maze:
            for col in row:
                print(col, " ", end="")
            print("")
        print("\n\n\n")

    def print_end(self):
        os.system("cls")
        print("\n\n\n")
        print(">>>>> Congratulations!!! <<<<<")
        print("\n\n\n")
        time.sleep(1)

    def move(self, direction):
        directions = {"up": (-1, 0), "down": (1, 0), "left": (0, -1), "right": (0, 1)}
        dy, dx = directions.get(direction, (0, 0))
        next_move = Pos(self.ply.y + dy, self.ply.x + dx)

        if self.is_in_bound(next_move.y, next_move.x) and self.maze[next_move.y][next_move.x] in [" ", "E"]:
            self.maze[self.ply.y][self.ply.x] = " "
            self.maze[next_move.y][next_move.x] = "P"
            self.ply = next_move
            time.sleep(0.25)

            if self.maze[next_move.y][next_move.x] == "E":
                self.print_end()
                return False

        return True

    def solve_maze_dfs(self, y, x):
        if not self.is_in_bound(y, x) or self.maze[y][x] in ["X", "P", "."]:
            return False

        if self.maze[y][x] == "E":
            return True

        self.maze[y][x] = "."
        self.print_board()
        time.sleep(0.25)

        if self.solve_maze_dfs(y - 1, x) or self.solve_maze_dfs(y + 1, x) or \
           self.solve_maze_dfs(y, x - 1) or self.solve_maze_dfs(y, x + 1):
            return True

        self.maze[y][x] = " "
        self.print_board()
        time.sleep(0.25)
        return False

    def auto_solve_maze(self):
        self.solve_maze_dfs(self.ply.y, self.ply.x)

class pos:
    def __init__(self, y, x):
        self.y = y
        self.x = x




 
import os
import time

class maze:
    def __init__(self) -> None:
        self.maze = [
                    ["X", "X", "X", "X", "X", "X", "X"],
                    ["X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", "X", " ", "X", " ", " "],
                    ["X", " ", "X", " ", "X", " ", "X"],
                    ["X", " ", " ", " ", " ", " ", "X"],
                    ["X", " ", "X", "X", "X", "X", "X"],
                    ]
        self.ply = pos(5, 1)
        self.end = pos(2, 6)
        self.maze[self.ply.y][self.ply.x] = "P"
        self.maze[self.end.y][self.end.x] = "E"
    
    def isInBound(self, y, x):
        if y>=0 and x>=0 and y<len(self.maze) and x<len(self.maze[0]):
            return True
        else:
            return False
    
    def print(self):
        os.system("cls")
        print("\n\n\n")
        for row in self.maze:
            for col in row:
                print(col," ", end="")
            print("")
        print("\n\n\n")
    
    def printEND(self):
        os.system("cls")
        print("\n\n\n")
        print(">>>>> Congraturation!!! <<<<<")
        print("\n\n\n")

    def move_up(self):
        next_move = pos(self.ply.y-1, self.ply.x)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True
    
    def move_down(self):
        next_move = pos(self.ply.y+1, self.ply.x)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def move_left(self):
        next_move = pos(self.ply.y, self.ply.x-1)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

    def move_right(self):
        next_move = pos(self.ply.y, self.ply.x+1)
        if self.isInBound(next_move.y,next_move.x):
            if self.maze[next_move.y][next_move.x] == " ":
                self.maze[self.ply.y][self.ply.x] = " "
                self.maze[next_move.y][next_move.x] = "P"
                self.ply = next_move
                time.sleep(0.25)
            if self.maze[next_move.y][next_move.x] == "E":
                self.printEND()
                return False
        return True

class pos:
    def __init__(self) -> None:
        self.y = None
        self.x = None
    
    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x


if __name__ == '__main__':

    m = maze()
    m.print()

    u,r,d = 1,1,1

while u <= 4 :
    if m.move_up():
        m.print()
        u += 1
u = 1
while r <= 2 :
    if m.move_right():
        m.print()
        r += 1
r = 1
while d <= 3 :
    if m.move_down():
        m.print()
        d += 1
d = 1
while r <= 2 :
    if m.move_right():
        m.print()
        r += 1
r = 1
while u <= 2 :
    if m.move_up():
        m.print()
        u += 1 
u = 1
while r <= 1 :
    if m.move_right():
        m.print()
        r +=1       
        r = 1