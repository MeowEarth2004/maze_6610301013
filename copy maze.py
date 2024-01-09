import os
import keyboard
import time

class maze:
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
        keyboard.wait("")

    def move_auto(self , direction):
        next_move = pos(self.ply.y, self.ply.x)

        if direction == "up":
            next_move.y -= 1
        elif direction == "down":
            next_move.y += 1
        elif direction == "left":
            next_move.x -= 1
        elif direction == "right":
            next_move.x += 1

        if self.isinbound(next_move.y , next_move.x) and self.maze[next_move.y][next_move.x] in [" " , "E"]:
            self.maze[self.ply.y][self.ply.x] = " "
            self.maze[next_move.y][next_move.x] = "P"
            self.ply = next_move
            time.sleep(0.1)
            if self.maze[next_move.y][next_move.x] == "E":
                self.print_end()
                return False

            return True

        return False

class pos:

    def __init__(self) -> None:
        self.y = None
        self.x = None

    def __init__(self, y, x) -> None:
        self.y = y
        self.x = x

# ------------------------ #
# ===== MAIN PROGRAM ===== #
# ------------------------ #

m = maze()
m.print()

while True:

    if keyboard.is_pressed("q"):
        print("Quit Program")
        break
    if keyboard.is_pressed("A"):
        if m.move_auto(" "):
            m.print()
        else:
            break