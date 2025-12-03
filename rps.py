"player should be able to pick from 3 options; rock, paper, and scissors"
"player can play aganist the computer or another player."
"program needs to be able to understand which options win lose or tie agaist another option"
"if two player sleect the same option draw they have to play again keep count of points"






def rpsGame(_):
    ptint("welcome to RPS: the game!")
    print('****************************')
    print ("please select from the following options:" )
    print('1, start Game')
    print("3. Quit")
    selection = input()
    if int (selection) == 1:
        print('the game is starting')
        print("please select a game mode")
        print('the game is starting...')
    elif selection == 2:
        print('game rules...')
    elif selection == 3:
        print("good bye...")
    else:
        print()            
