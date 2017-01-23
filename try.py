import random

movieName =''
orignalMovieNameList = []
gameMovieNameList = []
gameMovieNameString =''
noOfChances = 9
randomNoList = []
escapeTupple = ('\'',':',' ')

def Welcome(): #this function is to continously welcome users and play the game.
    while True:
        print ('\nWelcome to HollyWood Game! \n \n Enter 1 to start the game. \n Enter 2 for Rules. \n Enter 3 to Exit.')
        userSelection = int(input())
        if userSelection == 1:
            StartGame()
        elif userSelection==2:
            ShowRules()
            print('\nEnter your selection again.')
            userSelection = int(input())
        else:
            print("\nThanks You!")
            break

        
def setEnvironment(): #this functions initialises the variables, takes the movie and prepares movie name for the game.
    global movieName
    global orignalMovieNameList
    global gameMovieNameList
    global gameMovieNameString
    global randomNoList
    global noOfChances
    global escapeTupple
    
    noOfChances= 9
    movieName = getMovieName()
    orignalMovieNameList= list(movieName)
    gameMovieNameList= list(movieName)
    
    movieName_length = len((movieName).strip())
    noOfSpaces = movieName.count(' ')
    noOfCharacterToBeEliminated = int((movieName_length-noOfSpaces)/2) -1  
    noOfCharacterToBeEliminated_backup = noOfCharacterToBeEliminated
    """ logic to replace the random character to _ """
    
    while noOfCharacterToBeEliminated !=0:
        number =random.randint(0,movieName_length-1)
        if number in randomNoList:
            continue
        else :
            if gameMovieNameList[number] not in  escapeTupple :
                randomNoList = randomNoList + [number]
                gameMovieNameList[number] = '_'
                noOfCharacterToBeEliminated = noOfCharacterToBeEliminated -1
            else:
                continue
            
    gameMovieNameString = ''.join(gameMovieNameList)

    
def StartGame(): # this function has the logic to take input and inform user if input was correct or not.
    global noOfChances
    global movieName
    global orignalMovieNameList
    global gameMovieNameList
    global gameMovieNameString
    global randomNoList
    
    setEnvironment()
    #print(noOfChances)
    #print(movieName + ' ' + gameMovieNameString)
    print('\nYour Movie Name is ->\t\t' + gameMovieNameString + '\n')
    print('Lets start Guessing the characters (including Numbers) and \'')
    while noOfChances != 0:  
        print('\n' + str(noOfChances) + ' chance left. ' + gameMovieNameString + '\nEnter your Guess ->')
        charGuess = input()
        count =0
        if charGuess in orignalMovieNameList:
            #indexOfnumberGuess = orignalMovieNameList.index(charGuess)
            indexListOfCharGuess = find(movieName, charGuess)
            for i in indexListOfCharGuess:
                if i in randomNoList:
                   # print('Wrong Guess, try again')
                    #noOfChances = noOfChances -1
                    gameMovieNameList[i]= orignalMovieNameList[i]
                    gameMovieNameString = ''.join(gameMovieNameList)
                    print('')
                    randomNoList.remove(i)
                    count =1
                    
        else :
            count = 0
            
        if count ==0:
            noOfChances = noOfChances -1
            print('Wrong Guess')
        else:
            print('Correct Guess')
       # print(movieName + ' and ' + gameMovieNameString)
        
        if gameMovieNameString == movieName:
            print('\nCongrats!!\nYou guessed the movie name correct.\nThe movie Name was ->' + movieName)
            noOfChances = -1
            break

    if noOfChances != -1:
        print("Game Over!")
        print("Correct Movie Name was ->" + movieName)
            
def getMovieName(): # this function just returns the movie name randomnly
    return movies_list[random.randint(0,len(movies_list)-1)]

def find(s, ch): # this function return a list with all the indexes at which ch is present in string s.
    return [i for i, ltr in enumerate(s) if ltr == ch]


def ShowRules(): #just to display the rules
    print('\nRules: ')
    print('Movies name will be displayed with come characters missing.')
    print('Guess the characters within 9 chances (Hollywood) and you win game')
    
movies_list = ('The Godfather','The Shawshank Redemption',
               'Schindler\'s List','Raging Bull','Casablanca',
               'Citizen Kane','Gone with the Wind','The Wizard of Oz',
               'One Flew Over the Cuckoo\'s Nest','Lawrence of Arabia',
               'Vertigo','Psycho','On the Waterfront','Sunset Blvd',
               'Forrest Gump','The Sound of Music','12 Angry Men',
               'West Side Story','The Dark Knight','Pulp Fiction','The Lord of the Rings: The Return of the King','The Good',
               'the Bad and the Ugly','Fight Club','Inception','One Flew Over the Cuckoo\'s Nest',
               'Seven Samurai','Se7en','The Silence of the Lambs', 'It\'s a Wonderful Life',
               'The Usual Suspects','Life Is Beautiful' ,'Spirited Away','Saving Private Ryan',
               'Once Upon a Time in the West','American History X','Interstellar' ,'Raiders of the Lost Ark',
               'The Intouchables','Modern Times','Rear Window','The Pianist','Back to the Future',
               'Apocalypse Now','Sunset Boulevard','The Great Dictator','The Lives of Others',
               'Cinema Paradiso')


Welcome() # starts the program execution.
