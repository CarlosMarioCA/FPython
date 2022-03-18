import PySimpleGUI as sg


button_size = (20, 10)
PLAYER_ONE = "X"
PLAYER_TWO = "O"
current_player = PLAYER_ONE
game_over = True
sg.theme("DarkAmber")

deck = [0, 0, 0,
        0, 0, 0,
        0, 0, 0]

win = [[0, 1, 2],[0, 3, 6],[0, 4, 8],[1, 4, 7],[2, 5, 8],[3, 4, 5],[6, 7, 8],[2, 4, 6]]

layout = [[sg.Button("", key="-0-", size=button_size), sg.Button("", key="-1-", size=button_size), sg.Button("", key="-2-", size=button_size)],
        [sg.Button("",  key="-3-", size=button_size), sg.Button("",  key="-4-", size=button_size), sg.Button("", key="-5-", size=button_size)],
        [sg.Button("",  key="-6-",size=button_size), sg.Button("",  key="-7-",size=button_size), sg.Button("",  key="-8-",size=button_size)],
        [sg.Button('-GAME OVER-', 'center')]]

window = sg.Window("Demo", layout, margins=(10, 10), element_justification='c')

while game_over:
    event, value = window.read()
    if event == sg.WINDOW_CLOSED or event == "-GAME OVER-":
        break

    if window.Element(event).ButtonText == "":
        index = int(event.replace("-", ""))
        deck[index] = current_player
        window.Element(event).Update(text=current_player)
        if current_player == PLAYER_ONE:
            current_player = PLAYER_TWO
        else:
            current_player = PLAYER_ONE

    for win_play in win:
        if deck[win_play[0]] == deck[win_play[1]] == deck[win_play[2]] != 0:
            print("GAME OVER.")
            if deck[win_play[0]] == PLAYER_ONE:
                print("Player 1 win!")
                game_over = False
            elif deck[win_play[0]] == PLAYER_TWO:
                print("Player 2 win!")
                game_over = False

    if 0 not in deck:
        print("GAME OVER.")

window.Close()
