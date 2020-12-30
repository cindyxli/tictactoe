def print_board(board):
    for i in range(len(board)):
        current_row = board[i]
        for j in range(len(current_row)):
            print(board[i][j], end='')
        print("")


def make_board():
    board = []
    space_row = ["   ", "|", "   ", "|", "   "]
    board.append(space_row)
    for _ in range(2):
        line_row = []
        for _ in range(11):
            line_row.append("-")
        board.append(line_row)
        board.append(space_row[:])

    return board

def check_letter(str):
    for char in str:
        if ord(char) != 45 or ord(char) != 124:
            return False 
    return True

def get_symbol(str):
    #meant for strings that have a symbol in it
    return str[1]

def raw_board(board):
    #returns a list with only the x's and o's, in 3 rows
    raw = []
    for i in range(len(board)):
        raw_row = []
        if i%2 == 0:
            raw_row = [get_symbol(str) for str in board[i] if check_letter(str) or str == "   "]
            raw.append(raw_row)
    return raw

#def play(board = [], turns = 0):
 #   over = False
  #  while not over:
        

#def npc_turn(raw_board, turn):
 #   if turn == 0: 
  #      raw_board[1][1] = "x"
   #     return raw_board


board = make_board()
print_board(board)
print(raw_board(board))
#[_ _ _ _ _ _ _ _ _]
#make an option where a user can select what their x or o looks like hehe
