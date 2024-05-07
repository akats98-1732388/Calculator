# TicTacToe Game
# Defining Global Variables
HEIGHT = 3
WIDTH = 3


def empty_state():  #defining empty game state
    state = list()
    for _ in range(HEIGHT): 
        row_list = list()
        for _ in range(WIDTH):
            row_list.append(" ")
        state.append(row_list)

    return state

def draw_line():
    line = ""
    for i in range(WIDTH*2+1): 
        line += "-"
    print(line)
        
def draw_row(GameState:list[str]):
    row = "|"
    for i in GameState:
        row += (i + "|")
    print(row)
           
def draw_board(GameState:list[list[str]]):
    for i in GameState:
        draw_line()
        draw_row(i)
    draw_line()
    

def main():
    GameState = empty_state()
    draw_board(GameState)

if __name__ == "__main__":
    main()  