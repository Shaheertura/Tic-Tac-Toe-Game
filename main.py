board = [' ' for _ in range(9)]

def display_board(current_player):
    print("Player Turn:",current_player)
    print("-------------")
    print("|",board[0],"|",board[1],"|",board[2],"|")
    print("-------------")
    print("|",board[3],"|",board[4],"|",board[5],"|")
    print("-------------")
    print("|",board[6],"|",board[7],"|",board[8],"|")
    print("-------------")

def get_player_move():

    position = input("Enter Your Move From (1-9)")
    position = int(position)
    position -= 1
    return position


def make_move(position, player):
    if board[position] == ' ':
        board[position] = player
        return True
    else:
        return False

def check_winner(player):
    
    winning_combinations = [
        (0,1,2),(3,4,5),(6,7,8), #Rows
        (0,3,6),(1,4,7),(2,5,8), #Columns
        (0,4,8),(2,4,6) # Diaganols

    ]
    for combination in winning_combinations:
        if board[combination[0]] == board[combination[1]] == board[combination[2]] == player:
            return True
    return False

def check_draw():
    return ' ' not in board

def switch_player(player):
    if player == "X":
        return "O"
    else:
        return "X"

def play_game():
    current_player = "X"
    display_board(current_player)
    while True:
        postion = get_player_move()
        if make_move(postion,current_player):
            display_board(current_player)
            if check_winner(current_player):
                print("Player:",current_player,"Wins!")
                break
            elif check_draw():
                print("It's A Draw!")
                break
            current_player = switch_player(current_player)

        else:
            print("Invalid Move. Try Again")
play_game()
