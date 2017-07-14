# Jeremiah Cote
# User Id - 1
# Assignment/Lab 5
# Part C - Game of Life
# 13 July 2017

import sys
import turtle
import random

CELL_SIZE = 10
class LifeBoard:
#This is to create the game of life board and class for it

    def __init__(self, xsize, ysize):
        #Create a new life game board
        self.state = set()
        #This sets the state of the life board
        self.xsize, self.ysize = xsize, ysize
    #this is to determine the board size

    def is_legal(self, x, y):
        #If the board is within legitimate sizes then this will yield a return true
        return (0 <= x < self.xsize) and (0 <= y < self.ysize)
        #As long as the board is not less than 0 then the board will be created to that particular size

    def set(self, x, y):
        #This allows a certain area to be a live area
        if not self.is_legal(x, y):
            #IF this is not a legitmate move this loop is called
            raise ValueError("Coordinates {}, {} out of range 0..{}, 0..{}".format(
                #This is to indicated that the coordinates are out of range and that the format is incorrect
                x, y, self.xsize, self.ysize))
                #This is to have the format called to reenter the value

        key = (x, y)
        #This is to indicate the key variable that will be called later to be used
        self.state.add(key)
        #This is to incorpate the key into the game

    def makeRandom(self):
        #This is to randomize the board for the game
        self.erase()
        #This is erase and always have a fresh randomized board
        for i in range(0, self.xsize):
            #This is to have the rows within a particluar call and size
            for j in range(0, self.ysize):
                #This is the loop for specific columns
                if random.random() > 0.5:#This is to ranomized each row and colum greater than .5
                    self.set(i, j)
                #This set the randomized board

    def toggle(self, x, y):
        #This is to determine if the certain aera is considered dead or alive
        if not self.is_legal(x, y):
            #This loop is called if this area is not within a certain range
            raise ValueError("Coordinates {}, {} out of range 0..{}, 0..{}".format(
                # This is to indicated that the coordinates are out of range and that the format is incorrect
                x, y, self.xsize, self.ysize))
        # This is to have the format called to reenter the value
        key = (x, y)
        #This is to indicate the key variable that will be called later to be used
        if key in self.state:
            #If the key is called then this area is removed or added
            self.state.remove(key)
            #This is remove the specific area
        else:
            #This is to call the other condition of the loop
            self.state.add(key)
        #This is to add a specific area

    def erase(self):
        #This will erase the entire game
        self.state.clear()
        #This is to call to clear the enter state of the game

    def step(self):
        #This is for updating the generation
        d = set()
        for i in range(self.xsize):
            x_range = range(max(0, i - 1), min(self.xsize, i + 2))
            for j in range(self.ysize):
                s = 0
                live = ((i, j) in self.state)
                for yp in range(max(0, j - 1), min(self.ysize, j + 2)):
                    for xp in x_range:
                        if (xp, yp) in self.state:
                            s += 1
                s -= live
                if s == 3:
                    #Thi is for birth
                    d.add((i, j))
                elif s == 2 and live:
                    #This is for survival
                    d.add((i, j))
                elif live:
                    #This is for the death
                    pass

        self.state = d
    def draw(self, x, y):
        turtle.penup()
        key = (x, y)
        if key in self.state:
            turtle.setpos(x * CELL_SIZE, y * CELL_SIZE)
            turtle.color('black')
            turtle.pendown()
            turtle.setheading(0)
            turtle.begin_fill()
            for i in range(4):
                turtle.forward(CELL_SIZE - 1)
                turtle.left(90)
            turtle.end_fill()

    def display(self):
        turtle.clear()
        for i in range(self.xsize):
            for j in range(self.ysize):
                self.draw(i, j)
        turtle.update()


def display_help_window():
    from turtle import TK
    root = TK.Tk()
    frame = TK.Frame()
    canvas = TK.Canvas(root, width=300, height=200, bg="white")
    canvas.pack()
    help_screen = turtle.TurtleScreen(canvas)
    help_t = turtle.RawTurtle(help_screen)
    help_t.penup()
    help_t.hideturtle()
    help_t.speed('fastest')

    width, height = help_screen.screensize()
    line_height = 20
    y = height // 2 - 30
    for s in ("Click on cells to make them alive or dead.",
              "Keyboard commands:",
              " E)rase the board",
              " R)andom fill",
              " S)tep once or",
              " C)ontinuously -- use 'S' to resume stepping",
              " Q)uit"):
        help_t.setpos(-(width / 2), y)
        help_t.write(s, font=('sans-serif', 14, 'normal'))
        y -= line_height


def main():
    display_help_window()

    scr = turtle.Screen()
    turtle.mode('standard')
    xsize, ysize = scr.screensize()
    turtle.setworldcoordinates(0, 0, xsize, ysize)

    turtle.hideturtle()
    turtle.speed('fastest')
    turtle.tracer(0, 0)
    turtle.penup()

    board = LifeBoard(xsize // CELL_SIZE, 1 + ysize // CELL_SIZE)

    # Set up mouse bindings
    def toggle(x, y):
        cell_x = x // CELL_SIZE
        cell_y = y // CELL_SIZE
        if board.is_legal(cell_x, cell_y):
            board.toggle(cell_x, cell_y)
            board.display()

    turtle.onscreenclick(turtle.listen)
    turtle.onscreenclick(toggle)

    board.makeRandom()
    board.display()

    def erase():
        board.erase()
        board.display()
    turtle.onkey(erase, 'e')
    def makeRandom():
        board.makeRandom()
        board.display()

    turtle.onkey(makeRandom, 'r')
    turtle.onkey(sys.exit, 'q')

    continuous = False

    def step_once():
        nonlocal continuous
        continuous = False
        perform_step()

    def step_continuous():
        nonlocal continuous
        continuous = True
        perform_step()

    def perform_step():
        board.step()
        board.display()
        if continuous:
            turtle.ontimer(perform_step, 25)

    turtle.onkey(step_once, 's')
    turtle.onkey(step_continuous, 'c')

    turtle.listen()
    turtle.mainloop()

if __name__ == '__main__':
    main()