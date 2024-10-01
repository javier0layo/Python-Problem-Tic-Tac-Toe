
#This is a grid list that displays each space of the grid. 
grid = [[' ', ' ', ' '],
        [' ', ' ', ' '],
        [' ', ' ', ' ']]


#Displays the grid with the lines around the boarders of the spaces. 
def display_grid():
    print()
    print("+---+---+---+")
    for row in grid:
        print("|", end = " ")
        for column in row:
            print(f" {column}|", end = " ")
        print()
        print("+---+---+---+")
    print()
     

#Function will start game.
def start_game():
    game_over = False
    while not game_over: #infinite loop controllled with game_over
        game_over = take_turn() #While the game is not over, the take_turn() function
        #will allows the user(s) to continue playing.
    print()
    print("Game Over!") #If game is over, will display message, and end. 
              

#Function will display the turn of each player and results of the game.
def take_turn():
    turn = 1 #identify who is playing X and who is O.
    while True:
        if not turn % 2 == 0:
            mark = "X" #X will go first.
        else:
            mark = "O"
        print(f"{mark}'s turn") #Will display message stating who's turn it is. 

        row = int(input("Pick a row(1, 2, 3): ")) #User will select row.
        column = int(input("Pick a column(1, 2, 3): ")) #User will select column.
        if row < 1 or row > 3:
            print("Invalid row number. Try again.") #If the input is out of bound of the row it will display error message.
            continue
        if column < 1 or column > 3:
            print("Invalid column number. Try again.") #If the input is out of bound of the column it will display error message.
            continue
        if not grid[row - 1][column - 1]== " ":
            print("The square is already taken. Try again.") #Display error message if column/row is already taken.
            continue
        grid[row -1][column - 1] = mark
        display_grid() #Will display the mark(X or O) on the grid that the user selected. 

        winner = check_for_winner() #Calls in the check_for_winner function to see who won the game. 
        if winner == "X" or winner == "O":
            print(f"{winner} wins!")
            return True
            
        if turn == 9: #If the users have played 9 times and their is no winner, than it is a tie. 
            print("It's a tie!")
            return True
     

        turn += 1
        
#Function will check for who won the game.
def check_for_winner():
    #rows
    for x in range(3):
        if grid[x][0] == grid[x][1] and grid[x][1] == grid[x][2]:
            return grid[x][0]
        
    #columns
    for y in range(3):
        if grid[0][y] == grid[1][y] and grid[1][y] == grid[2][y]:
            return grid[0][y]
    #diagnoal 1:
    if grid[0][0] == grid[1][1] and grid[1][1] == grid[2][2]:
        return grid[0][0]
    
    #diagnoal 2:
    if grid[0][2] == grid[1][1] and frid[1][1] == grid[2][0]:
        return grid[0][2]
    
    #no winner yet
        return " "
            

def main():
    print("Welcome to Tic Tac Toe") #display title
    display_grid() #function
    start_game() #function
    
#Checks the main method
if __name__ == "__main__":
    main()
    


    
