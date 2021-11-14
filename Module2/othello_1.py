''' Assignment: othello_1
    Created on 14-11-2021
    @author Alejo Cain '''

# size of playing field, constant
TOTAL_SQUARES = 64.00
# input white pieces
white_pieces = int(input("Enter the number of white pieces on the board: "))
# input black pieces
black_pieces = int(input("Enter the number of black pieces on the board: "))
# calculation of percentage black pieces owning the board
percentage_black_pieces_on_board = (black_pieces / TOTAL_SQUARES) * 100
# calculation of percentage of all black pieces on the board
total_percentage_black_pieces = black_pieces / \
    (white_pieces + black_pieces) * 100
# output showing the black pieces on the board and the percentage of the board covered in black pieces
print("The percentage of black pieces on the board is: %.2f%% " %
      (percentage_black_pieces_on_board))
print("The percentage of black pieces of all the pieces on the board is: %.2f%% " %
      (total_percentage_black_pieces))
