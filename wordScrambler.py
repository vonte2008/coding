def wordScrambler():
    wordpool = ["latitude" , 'arithmetic' , 'sophisticated' , 'pyscosis']

    for attemps in range(3):
        print("latitude" + str(attemps))
        if attemps are more then 3



    random = random.randint(0,3)
    print(randomselect)

    if randomselect == 0:

        print("welcome to scrambled! ")
        randomselect= random.randint(0,3)

    if randomselect == 0:
        correctword = wordpool[0]
    elif randomselect == 1:
        correctword = wordpool[1]
    elif randomselect == 2:
        correctword = wordpool [2]
    elif randomselect == 3:
        correctword = wordpool[3]

    convertedstring = list(correctword)

    random.suffle(convertedstring)
    scrambled = "".join(convertedstring)
    print("please guess the correct word: " + scrambled)
    userguess = input()

    if userguess == correctword:
        print("you win")
    else:
        print("sorry you lose.")

wordScrambler() 
           



