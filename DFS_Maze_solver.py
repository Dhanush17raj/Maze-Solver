import turtle
import time
import sys

wn = turtle.Screen()
wn.bgcolor("black")
wn.title("Maze Solver")
wn.setup(1300, 700)

class box(turtle.Turtle):                  # turtle.Turtle basically passes on the Turtle object as a parameter into the class
    def __init__(self, c):
        turtle.Turtle.__init__(self)        # this function gives the turtle class access to the self variable
        self.c = c
        self.shape("square")
        self.color(self.c)
        self.penup()
        self.speed(0)

# grid = [
# "+++++++++",
# "+   s++++",
# "+ ++   ++",
# "+ ++++  +",
# "+    ++ +",
# "++ ++++ +",
# "+  + ++ +",
# "+      e+",
# "+       +",
# "+++++++++",
# ]

grid = [
"++++++++++++++++++++++++++++++++++++++++++++++++++",
"+s              +                                +",
"+ +++++++++++  +++++++++++++  +++++++  +++++++++++",
"+          ++                 +               ++ +",
"++ +++++++  +++++++++++++  +++++++++++++++++++++ +",
"++ ++  + ++ +           +  +                ++++ +",
"++ ++ ++ ++ +  +  ++++  +  +  +++++++++++++ ++++ +",
"++ ++    ++ +  +  +        +  +  +        +      +",
"+  ++ +++++ +  ++++++++++  +  +  ++++  +  + +++  +",
"+ +++    ++ +          +   +           +  + +++  +",
"+ +++++  ++ +++++++ ++++++++  +++++++++++++ +++  +",
"+     ++ +     +              +              ++  +",
"++++  ++ ++++++++++ +++++++++++  +++++++++++ +++ +",
"+ ++  ++                   ++    ++    ++ ++ +++ +",
"+ ++  ++++  +++++++++++++  ++ +++++ ++ ++ ++ ++  +",
"+  +  ++    +     +    ++ +++ +     ++    ++ ++ ++",
"++ +  ++ +++++++  ++++ ++ +++ +  +++++++++++ ++ ++",
"+                      ++ ++  +              ++ ++",
"+ ++++++             + ++ ++ ++  +++        +++ ++",
"+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  +",
"+ +    +    +++ +     +++++++++ ++  +++++++    + +",
"+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + +",
"+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   +",
"+      ++ +++++++e+++     ++          ++    ++++++",
"++++++++++++++++++++++++++++++++++++++++++++++++++",
 ]

def setup(grid):
    global start_x, start_y, end_x, end_y
    for y in range(len(grid)):
        for x in range(len(grid[y])):
            char = grid[y][x]
            screen_x = -588 + (x * 24)
            screen_y = 288 - (y * 24)

            if(char == "+"):
                maze.goto(screen_x, screen_y)
                maze.stamp()
                walls.append((screen_x, screen_y))

            elif(char == " "):
                path.append((screen_x, screen_y))

            elif(char == "e"):
                green.color("blue")
                green.goto(screen_x, screen_y)
                end_x, end_y = screen_x, screen_y
                green.stamp()
                green.color("green")
                path.append((end_x, end_y))

            elif(char == "s"):
                start_x, start_y = screen_x, screen_y
                red.goto(screen_x, screen_y)

def endProgram():
    wn.exitonclick()
    sys.exit()

def search(x, y, frontier, visited, solution):
    frontier.append((x, y))
    solution[(x, y)] = (x, y)
    time.sleep(0)
    while(len(frontier) != 0):
        time.sleep(0)
        current = (x, y)
        if((x - 24, y) in path and (x - 24, y) not in visited):
            cellleft = (x - 24, y)
            solution[cellleft] = (x, y)
            blue.goto(cellleft)
            blue.stamp()
            frontier.append(cellleft)

        if((x + 24, y) in path and (x + 24, y) not in visited):
            cellright = (x + 24, y)
            solution[cellright] = (x, y)
            blue.goto(cellright)
            blue.stamp()
            frontier.append(cellright)

        if((x, y - 24) in path and (x, y - 24) not in visited):
            celldown = (x, y - 24)
            solution[celldown] = (x, y)
            blue.goto(celldown)
            blue.stamp()
            frontier.append(celldown)

        if((x, y + 24) in path and (x, y + 24) not in visited):
            cellup = (x, y + 24)
            solution[cellup] = (x, y)
            blue.goto(cellup)
            blue.stamp()
            frontier.append(cellup)

        (x, y) = frontier.pop()
        visited.add(current)
        green.goto((x,y))
        green.stamp()
        if((x, y) == (end_x, end_y)):
            red.stamp()
        elif((x, y) == (start_x, start_y)):
            red.stamp()

def trackBack(x, y):
    yellow.goto(x, y)
    yellow.stamp()
    while((x, y) != (start_x, start_y)):
        yellow.goto(solution[(x, y)])
        yellow.stamp()
        (x, y) = solution[(x, y)]

maze = box("white")
red = box("red")
blue = box("blue")
green = box("green")
yellow = box("yellow")

walls = list()
path = list()
solution = dict()
visited = set()
frontier = list()

setup(grid)
search(start_x, start_y, frontier, visited, solution)
trackBack(end_x, end_y)
endProgram()
