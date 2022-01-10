import itertools

def win(current_game): #Winner

    def all_same(l):
        if l.count(l[0]) == len(l) and l[0] != 0: #Winner Logic
            return True
        else: 
            return False

    for row in game: #Horizontal Winner
        print(row)
        if all_same(row): #Horizontal Winner Logic
            print(f'Player {row[0]} is the winner, Horizontally (-).')
            return True

    for col in range(len(game)): #Vertical Winner
        check = []
        for row in game:
            check.append(row[col])
        if all_same(check): #Vertical Winner Logic
            print(f'Player {check[0]} is the winner, Vertically (|).')
            return True

    diags = [] #Diagonal Left bottom to Right top Winner
    for col, row in enumerate(reversed(range(len(game)))):
        diags.append(game[row][col])
    if all_same(diags): #Diagonal Left bottom to Right top Winner Logic
        print(f'Player {diags[0]} is the winner, Diagonally (/).')
        return True

    diags = [] #Diagonal Left top to Right bottom Winner
    for ix in range(len(game)):
        diags.append(game[ix][ix])
    if all_same(diags): #Diagonal Left top to Right bottom Winner Logic
        print(f'Player {diags[0]} is the winner, Diagonally (\\).')
        return True
    
    return False

#win(game)

def game_board(game_map, player=0, row=0, column=0, just_display=False): #Game Logic
    
    try:
        if game_map[row][column] != 0:
            print("This postition is occupied, Try Again.")
            return game_map, False

        print("   "+"  ".join([str(i) for i in range(len(game_map))])) #Column Denotation
        if not just_display:
            game_map[row][column] = player #Position of player
        
        for count,row in enumerate(game_map) :
            print(count,row) #Row Denotation
        
        return game_map, True
    
    except IndexError as e:
        print("Error, Make sure you enter row/column as 0,1 or 2 :  ", e) #When Row/Column is a value more than 2 or less than 0
        return game_map, False

    except Exception as e:
        print("Error: Something went really wrong. Check your code. ",e) #Any other Error
        return game_map, False

play = True
players = [1,2]
while play: #Resetting the Game

    game_size = int(input("What size of Tic Tac Toe would you like to play? :  ")) #Dynamic Game size
    game = [[0 for i in range(game_size)] for i in range(game_size)]

    game_won=False
    game, _ = game_board(game, just_display=True) #Displaying the Game Board
    player_choice = itertools.cycle([1, 2]) #Cycles between players 1 and 2

    while not game_won:
        current_player = next(player_choice) #Iterable vs Iterator
        print(f"Current Player is {current_player}") #Prints the player that is supposed to play
        played = False

        while not played:
            column_choice  = int(input("Which COLUMN Do you want to play? (0, 1 or 2) :  ")) #Prompting the user for Column number
            row_choice  = int(input("Which ROW Do you want to play? (0, 1 or 2) :  ")) #Prompting the user for Row number
            game, played = game_board(game, current_player, row_choice, column_choice) #Passing Arguments for player to play

        if win(game):
            game_won = True
            again = input("Game Over. Play again? (Y/N) :  ") #Contuinuation to Next Round of Game
            if again.lower() == "y":
                print("Restarting...") #Players want to play again
            elif again.lower() == "n":
                print("Bye, Have a Good day!") #Players don't want to play again
                play = False
            else:
                print("Entered character is Invalid.") #Invalid input fed by players
                play = False