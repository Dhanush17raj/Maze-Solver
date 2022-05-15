import turtle                    # import turtle library
import time
import sys
from collections import deque
from imgtomaze import grid

wn = turtle.Screen()               # define the turtle window
wn.bgcolor("black")
wn.title("A BFS Maze Solving Program")
wn.setup(1300,700)

class box(turtle.Turtle):               # defining a generalsed box class
    def __init__(self, c):
        turtle.Turtle.__init__(self)
        self.c = c
        self.shape("square")
        self.color(self.c)
        self.penup()                    # lift up the pen so it do not leave a trail
        self.speed(0)

path = "maze.jpg"
g = grid(path)

def setup_maze(grid):                          # define a function called setup_maze
    global start_x, start_y, end_x, end_y      # set up global variables for start and end locations
    global dim
    dim = 24
    for y in range(len(grid)):                 # read in the grid line by line
        for x in range(len(grid[y])):          # read each cell in the line
            character = grid[y][x]             # assign the varaible "character" the the x and y location od the grid
            screen_x = -600 + (x * (dim))         # move to the x location on the screen staring at -588
            screen_y = 310 - (y * (dim))          # move to the y location of the screen starting at 288

            if character == "+":
                maze.goto(screen_x, screen_y)         # move pen to the x and y locaion and
                maze.stamp()                          # stamp a copy of the turtle on the screen
                walls.append((screen_x, screen_y))    # add coordinate to walls list

            if character == " " or character == "e":
                path.append((screen_x, screen_y))     # add " " and e to path list

            if character == "e":
                green.color("blue")
                green.goto(screen_x, screen_y)       # send green sprite to screen location
                end_x, end_y = screen_x,screen_y     # assign end locations variables to end_x and end_y
                green.stamp()
                green.color("green")

            if character == "s":
                start_x, start_y = screen_x, screen_y  # assign start locations variables to start_x and start_y
                red.goto(screen_x, screen_y)


def endProgram():
    wn.exitonclick()
    sys.exit()

def search(x,y):
    frontier.append((x, y))
    solution[x,y] = x,y

    while len(frontier) > 0:          # exit while loop when frontier queue equals zero
        time.sleep(0)
        x, y = frontier.popleft()     # pop next entry in the frontier queue an assign to x and y location

        if(x - dim, y) in path and (x - dim, y) not in visited:  # check the cell on the left
            cell = (x - dim, y)
            solution[cell] = x, y    # backtracking routine [cell] is the previous cell. x, y is the current cell
            blue.goto(cell)          # identify frontier cells
            blue.stamp()
            frontier.append(cell)   # add cell to frontier list
            visited.add((x-dim, y))  # add cell to visited list

        if (x, y - dim) in path and (x, y - dim) not in visited:  # check the cell down
            cell = (x, y - dim)
            solution[cell] = x, y
            blue.goto(cell)
            blue.stamp()
            frontier.append(cell)
            visited.add((x, y - dim))

        if(x + dim, y) in path and (x + dim, y) not in visited:   # check the cell on the  right
            cell = (x + dim, y)
            solution[cell] = x, y
            blue.goto(cell)
            blue.stamp()
            frontier.append(cell)
            visited.add((x + dim, y))

        if(x, y + dim) in path and (x, y + dim) not in visited:  # check the cell up
            cell = (x, y + dim)
            solution[cell] = x, y
            blue.goto(cell)
            blue.stamp()
            frontier.append(cell)
            visited.add((x, y + dim))
        green.goto(x,y)
        green.stamp()

def backRoute(x, y):
    yellow.goto(x, y)
    # yellow.stamp()
    while (x, y) != (start_x, start_y):    # stop loop when current cells == start cell
        yellow.goto(solution[x, y])        # move the yellow sprite to the key value of solution ()
        yellow.stamp()
        x, y = solution[x, y]              # "key value" now becomes the new key

# set up classes
maze = box("white")
red = box("red")
blue = box("blue")
green = box("green")
yellow = box("yellow")

# setup lists
walls = []
path = []
visited = set()
frontier = deque()
solution = {}                           # solution dictionary

# main program starts here ####
setup_maze(g)
search(start_x,start_y)
backRoute(end_x, end_y)
endProgram()
