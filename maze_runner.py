import turtle                    # import turtle library
import time
import sys
from collections import deque


# class Maze(turtle.Turtle) -> class maze is inherited from class turtle
class Maze(turtle.Turtle):               # Maze class -> defines walls of the maze
    def __init__(self):
        turtle.Turtle.__init__(self)    # initializes the Turtle module in turtle library
        self.shape("square")            # the turtle shape
        self.color("white")             # colour of the turtle
        self.penup()                    # lift up the pen so it do not leave a trail
        self.speed(0)


class Green(turtle.Turtle):             # Green class -> defines turtle while searching the maze
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(0)

class Blue(turtle.Turtle):              # Blue class -> defines exit point in maze
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("blue")
        self.penup()
        self.speed(0)



class Red(turtle.Turtle):               # Red class -> defines starting point in maze
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("red")
        self.penup()
        self.speed(0)

class Yellow(turtle.Turtle):            # Yellow class -> defines the backtracking path
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(0)

class Runner:
    def __init__(self):
        self.sc = turtle.Screen()               # define the turtle screen
        self.sc.bgcolor("black")                # set the background colour
        self.sc.title("A BFS Maze Solving Program")
        self.sc.setup(1300,700)

        self.walls = []
        self.path = []
        self.visited = set()                            # stores visited coordinates
        self.frontier = deque()                         # Queue for BFS Algorithm
        self.solution = {}                           # solution dictionary to store backtracking path

        self.grid = [
            "+++++++++++++++++++++++++++++++++++++++++++++++++++",
            "+               +                                 +",
            "+  ++++++++++  +++++++++++++  +++++++  ++++++++++++",
            "s           +                 +               ++  +",
            "+  +++++++  +++++++++++++  +++++++++++++++++++++  +",
            "+  +     +  +           +  +                 +++  +",
            "+  +  +  +  +  +  ++++  +  +  +++++++++++++  +++  +",
            "+  +  +  +  +  +  +        +  +  +        +       +",
            "+  +  ++++  +  ++++++++++  +  +  ++++  +  +  ++   +",
            "+  +     +  +          +   +           +  +  ++  ++",
            "+  ++++  +  +++++++ ++++++++  +++++++++++++  ++  ++",
            "+     +  +     +              +              ++   +",
            "++++  +  ++++++++++ +++++++++++  ++++++++++  +++  +",
            "+  +  +                    +     +     +  +  +++  +",
            "+  +  ++++  +++++++++++++  +  ++++  +  +  +  ++   +",
            "+  +  +     +     +     +  +  +     +     +  ++  ++",
            "+  +  +  +++++++  ++++  +  +  +  ++++++++++  ++  ++",
            "+                       +  +  +              ++  ++",
            "+ ++++++             +  +  +  +  +++        +++  ++",
            "+ ++++++ ++++++ +++++++++    ++ ++   ++++++++++  ++",
            "+ +    +    +++ +     +++++++++ ++  +++++++    + ++",
            "+ ++++ ++++ +++ + +++ +++    ++    ++    ++ ++ + ++",
            "+ ++++    +     + +++ +++ ++ ++++++++ ++ ++ ++   ++",
            "+      ++ +++++++++++     ++          ++    +++++++",
            "++++++++++++++++++++++e++++++++++++++++++++++++++++",
            ]


    def setup_maze(self, grid):                          # define a function called setup_maze
        global start_x, start_y, end_x, end_y      # set up global variables for start and end locations
        for y in range(len(grid)):                 # read in the grid line by line
            for x in range(len(grid[y])):          # read each cell in the line
                character = grid[y][x]             # assign the varaible "character" the the x and y location od the grid
                screen_x = -588 + (x * 24)         # move to the x location on the screen staring at -588
                screen_y = 288 - (y * 24)          # move to the y location of the screen starting at 288

                if character == "+":
                    maze.goto(screen_x, screen_y)         # move pen to the x and y locaion and
                    maze.stamp()                          # stamp a copy of the turtle on the screen
                    self.walls.append((screen_x, screen_y))    # add coordinate to walls list

                if character == " " or character == "e":
                    self.path.append((screen_x, screen_y))     # add " " and e to path list

                if character == "e":
                    green.color("blue")
                    green.goto(screen_x, screen_y)       # send green sprite to screen location
                    end_x, end_y = screen_x,screen_y     # assign end locations variables to end_x and end_y
                    green.stamp()
                    green.color("green")

                if character == "s":
                    start_x, start_y = screen_x, screen_y  # assign start locations variables to start_x and start_y
                    red.goto(screen_x, screen_y)



    def endProgram(self):
        self.sc.exitonclick()
        sys.exit()

    def search(self, x, y):
        self.frontier.append((x, y))
        self.solution[x, y] = x,y

        while len(self.frontier) > 0:          # exit while loop when frontier queue equals zero
            time.sleep(0)
            x, y = self.frontier.popleft()     # pop next entry in the frontier queue an assign to x and y location

            if(x - 24, y) in self.path and (x - 24, y) not in self.visited:  # check the cell on the left
                cell = (x - 24, y)
                self.solution[cell] = x, y
                self.frontier.append(cell)      # add cell to frontier list
                self.visited.add((x-24, y))     # add cell to visited list

            if (x, y - 24) in self.path and (x, y - 24) not in self.visited:  # check the cell below
                cell = (x, y - 24)
                self.solution[cell] = x, y
                self.frontier.append(cell)
                self.visited.add((x, y - 24))
                print(self.solution)

            if(x + 24, y) in self.path and (x + 24, y) not in self.visited:   # check the cell on the right
                cell = (x + 24, y)
                self.solution[cell] = x, y
                self.frontier.append(cell)
                self.visited.add((x + 24, y))

            if(x, y + 24) in self.path and (x, y + 24) not in self.visited:  # check the cell above 
                cell = (x, y + 24)
                self.solution[cell] = x, y
                self.frontier.append(cell)
                self.visited.add((x, y + 24))
                
            green.goto(x,y)
            green.stamp()


    def backTrack(self, x, y):
        yellow.goto(x, y)
        yellow.stamp()
        while (x, y) != (start_x, start_y):    # stop loop when current cells == start cell
            yellow.goto(self.solution[x, y])        # move the yellow sprite to the key value of solution ()
            yellow.stamp()
            x, y = self.solution[x, y]               # "key value" now becomes the new key



if __name__ == '__main__':

    # set up classes
    maze = Maze()
    red = Red()
    blue = Blue()
    green = Green()
    yellow = Yellow()
    run = Runner()

# main program starts here 
    run.setup_maze(run.grid)
    run.search(start_x,start_y)
    run.backTrack(end_x, end_y)
    run.sc.exitonclick()    
