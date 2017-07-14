# Jeremiah Cote
# User Id - 1
# Assignment/Lab 5
# Part B - Tic Tac Toe with classes
# 13 July 2017

import os
#This is to import some os functions

class Board():
    #This is to make the board the object of this code by calling it a class of board
    def __init__(self):
        #This is to call to itself what the board will generally consist of
        self.cells = [" ", " "," "," ", " ", " ", " ", " ", " ", " "]
        #This is to create the board using spaces so that later we can fill in the spaces with either X's or O's

    def display(self):
        #This is to identify the function to display the object we created and then to have the components dispalyed as we please
        print("%s | %s | %s " %(self.cells[1], self.cells[2], self.cells[3]))
        #This is to have the first row broken up into cells
        print("----------")
        #This is to have a border seperating the first and second row
        print("%s | %s | %s " %(self.cells[4], self.cells[5], self.cells[6]))
        #This is to have the second row broken up into cells
        print("----------")
        #This is to have a border seperating the second and third row
        print("%s | %s | %s " %(self.cells[7], self.cells[8], self.cells[9]))
        #This is to have the third row broken up into cells


    def update_cell(self, cell_no, player):
        #This is a funciton used to call to self and to idenfty the player, so this way the board will continouse update on what the player inputs
       if self.cells[cell_no] == " ":
           #This is to populate only cells that are blanks and prevent replacing another's symbol with their own
           self.cells[cell_no] = player
            #This is to identify what and when this cell will be filled

    def is_winner(self, player):
        #This is to defince the function within the class that determines who wins the game
        if self.cells[1]==player and self.cells[2]==player and self.cells[3]==player:
            #This is to indicate if these cells are filled with a specific symobl then a winning condiditon exists
           return True
        #If this is correct then the return will be true indicatinga  winner condition
        if self.cells[4]==player and self.cells[5]==player and self.cells[6]==player:
            # This is to indicate if these cells are filled with a specific symobl then a winning condiditon exists
            return True
        #If this is correct then the return will be true indicatinga  winner condition
        if self.cells[7]==player and self.cells[8]==player and self.cells[9]==player:
            # This is to indicate if these cells are filled with a specific symobl then a winning condiditon exists
            return True
        #If this is correct then the return will be true indicatinga  winner condition
        if self.cells[1]==player and self.cells[4]==player and self.cells[7]==player:
            # This is to indicate if these cells are filled with a specific symobl then a winning condiditon exists
            return True
        #If this is correct then the return will be true indicatinga  winner condition
        if self.cells[3]==player and self.cells[6]==player and self.cells[9]==player:
            # This is to indicate if these cells are filled with a specific symobl then a winning condiditon exists
            return True
        #If this is correct then the return will be true indicatinga  winner condition
        if self.cells[1]==player and self.cells[5]==player and self.cells[9]==player:
            # This is to indicate if these cells are filled with a specific symobl then a winning condiditon exists
            return True
        #If this is correct then the return will be true indicatinga  winner condition
        if self.cells[7]==player and self.cells[5]==player and self.cells[3]==player:
            # This is to indicate if these cells are filled with a specific symobl then a winning condiditon exists
            return True
        #If this is correct then the return will be true indicatinga  winner condition

    def reset(self):
        #This is to reset the board if the game ends with a winner
        self.cells = [" ", " ", " ", " ", " ", " ", " ", " ", " ", " "]
        #This is to call back the inital design of the board

board = Board()
#This is to call the board so that it can be reset and displayed

def print_header():
    #This is to input a header within the class to indicate a message to the user
    print("Welcome to Tic-Tac-Toe\n")
    #This is the output display on the screen to the user

def refresh_screen():
    #This is to refresh the board so that after every turn and input the board updates
    print_header()
    #This is to print the header
    board.display()
    #This is to display the new board

while True:
    #This is to indicate that while there is no winning condition the game continues
    refresh_screen()
    #This is to refresh the board
    x_choice = int(input("\nPlayer 1). you are X's, to input your symbol please choose 1-9. > "))
    #This is to have the input entered from player 1 or X's onto the baord
    board.update_cell(x_choice, "X")
    #This is to update the board with the player's choice
    refresh_screen()
    #This is to refresh the board
    if board.is_winner("X"):
        #This is a loop message that will dispaly if Player 1 wins
        print("\nPlayer 1 wins!!!!")
        #This is to display the winning message if player 1 wins
        play_again = input("Would you like to play again?) (Y/N) > ").upper()
        #This is to indicate if the users would like to play again apened with upper incase they enter an uppercase character
        if play_again=="Y":
            #This is a loop that if the users selecte yes the board is reset and game is played again
            board.reset()
            #This is to reset the borad
            continue
            #This is to continue with the loop until a break is determined
        else:
            #This is if the users chooses No instead of Yes
            break
            #This is the break in the loop to prevent the computer from continouing

    o_choice = int(input("\nPLayer 2.) You are O's, to input your symbol PLease Choose 1-9. > "))
    #This is to have the input entered from player 2 or O's onto the board
    board.update_cell(o_choice, "O")
    #This is to update the board with the player's choice
    if board.is_winner("O"):
        #This is a loop message that will dispaly if Player 2 wins
        print("\nPLayer 2 wins!!!")
        #This is to display the winning message if player 1 wins
        play_again = input("Would you like to play again?) (Y/N) > ").upper()
        #This is to indicate if the users would like to play again apened with upper incase they enter an uppercase character
        if play_again == "Y":
        #This is a loop that if the users selecte yes the board is reset and game is played again
            board.reset()
        #This is to reset the borad
            continue
        # This is to continue with the loop until a break is determined
        else:
            #This is if the users chooses No instead of Yes
            break
            #This is the break in the loop to prevent the computer from continouing


b = Board()
#This is to create an instance of the board with preselected moves
b.printBoard()
#This is to create an instance of the board with preselected moves
b.update(1, 'X')
#This is to create an instance of the board with preselected moves
b.printBoard()
#This is to create an instance of the board with preselected moves
b.update(2, 'X')
#This is to create an instance of the board with preselected moves
b.printBoard()
#This is to create an instance of the board with preselected moves
b.update(3, 'X')
#This is to create an instance of the board with preselected moves
b.printBoard()
#This is to create an instance of the board with preselected moves
b.update(4, 'O')
#This is to create an instance of the board with preselected moves
b.printBoard()
#This is to create an instance of the board with preselected moves
b.update(5, 'O')
#This is to create an instance of the board with preselected moves
b.printBoard()
#This is to create an instance of the board with preselected moves
b.update(6, ' ')
#This is to create an instance of the board with preselected moves
b.printBoard()
#This is to create an instance of the board with preselected moves
b.update(7, ' ')
#This is to create an instance of the board with preselected moves
b.printBoard()
#This is to create an instance of the board with preselected moves
b.update(8, ' ')
#This is to create an instance of the board with preselected moves
b.printBoard()
#This is to create an instance of the board with preselected moves
b.update(9, ' ')
#This is to create an instance of the board with preselected moves
b.printBoard()
#This is to create an instance of the board with preselected moves
