# TicTacToe Game
# Defining Global Variables
HEIGHT = 3
WIDTH = 3


def Empty_State():  #defining empty game state
    state = list()
    for _ in range(HEIGHT): 
        row_list = list()
        for _ in range(WIDTH):
            row_list.append(" ")
        state.append(row_list)

    return state

def main():
    print("Hello World")
    
    print (GameState)

if __name__ == "__main__":
    main()  