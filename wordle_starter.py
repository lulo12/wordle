'''
Wordle Rules:
 Guess a five-letter word in six attempts.
 Each time you guess, you're told which of your chosen letters are in the target word, and whether they are in the right place
 Every time you make a guess you get feedback:
    Green - Correct letter in the correct spot
    Yellow - Correct letter in the incorrect spot
    Black - Incorrect letter

 There are no five-letter words that use the same letter four times. They can only be sets of two or three.

 If you try a word that shares duplicate letters with the answer, every instance of that letter will change color.
 For example, if you guess ”lever” and the answer is “eaten,” the first E in “lever” will turn yellow and the second one will turn green.
 The first one is in the word but in the wrong spot, and the second one is in the correct spot. The other letters will turn gray.

 Wordle tells you when a letter is not duplicated, too. If you use two of the same letter in a word, and only one of them turns yellow
   or green, then there is only one copy of that letter in the correct Wordle answer.

 AI mode
    -Rate AI's by average number of guesses for 1000 random games

 Extensions:
     -Keep track of wordle streaks
     -Wordle bot: https://www.tomsguide.com/news/wordlebot-is-a-new-tool-to-help-you-beat-wordle-and-its-brilliant

  Wordle Design Questions
    1) What are the rules for playing Wordle?
        -see above
    2) What functions will you use to break the big problem into smaller pieces?
        -see below
    3) How will you provide feedback without the use of color?
        -Incorrect letters
        -Correct letters, wrong spots
        -Correct letters, correct spots
    4) List some good test cases for Wordle
      -words with lengths that aren't 5 letters
      -winning outcome after n guesses
      -winning on 6th guess
      -duplicate guesses
      -guess with no correct letters
      -guess with correct letters, correct spot
      -guess with some correct letters in the correct spot, some correct letters in wrong spot
      -hidden word with duplicate letters ("MOTTO")
    5) What information is needed to compare AI approaches?
        -hidden word, list of guessed words
    6) What information is needed for an AI to make their next guess?
        -same feedback as for humans
'''

from  wordlist_helper import getWordList
import random

def pickHiddenWord():
    '''
    Returns a single word from the list of allowable words
    '''

    words = getWordList() 
    
    hiddenWord = random.choice(words)

    hiddenWord = "amama"

    hiddenWord = hiddenWord.upper()

    return hiddenWord


def getPlayerGuess():
    '''
    Prompts for and returns a player guess.
    Returns a string guess that is exactly 5 uppercase letters.
    '''
    
    bool = False

    words = getWordList()

    while not bool:
        guess = str(input("Enter a valid five letter word: "))
        if len(guess)!= 5 or guess not in words:
            continue
        else:
            bool = True

    guess = guess.upper()

    return guess


def generateFeedback(guess, hiddenWord, feedback):
    '''
    Returns a list of feeback based on comparing guess with the hidden word
    '''
    hiddenList = list(hiddenWord)
    guessList = list(guess)
    currentFeedback = []
    count = 0 
    bool = False

    for x in range(len(hiddenList)):
        bool = False
        count = 0 
        if guessList[x] in hiddenList:
            for y in range(0, x):
                if guessList[x] == guessList[y]:
                    count += 1
            if (count >= hiddenList.count(guessList[x])):
                bool = True
            if guessList[x] == hiddenList[x]:
                currentFeedback.append(guessList[x].upper())
                if bool:
                    for z in range(len(currentFeedback)):
                        if currentFeedback[len(currentFeedback) - z - 1] == guessList[x].lower():
                            currentFeedback[len(currentFeedback) - z - 1] = "-"
                            break
            elif guessList[x] and not bool:
                    currentFeedback.append(guessList[x].lower())
            else:
                currentFeedback.append("-")
        else:
            currentFeedback.append("-")

    tempList = [currentFeedback[:], guess]
    feedback.append(tuple(tempList))

    return feedback


def displayFeedback(feedback):
    '''
    Displays ongoing feedback guesses in a understndable manner
    '''
    grid = ""

    for x in range(len(feedback)):
        grid = "|"
        for y in feedback[x][0]:
            grid += y + "|"
        grid += "   " + str(feedback[x][1])
        print(grid)


def AIguess(feedback, guesses):  
   
    if len(guesses) == 0: 
        guess = "ADIEU"
    elif len(guesses) == 1: 
        guess = "SPORT"
    else: 
        #implement strategy

    #guess = guess.upper()

    return guess


def playWordle():
    '''
    Plays a complete game of wordle. Up to six guesses.
    Returns the hidden word an a list of all player guesses
    '''

    hiddenWord=pickHiddenWord()
    feedback = []
    guesses=[]
    GameOver = False

    print("\nWelcome to Wordle! \nYou have 6 chances to guess the hidden word. \nIf the letter is uppercase in the grid then it is at the correct position. \nIf the letter is lowercase, then that letter is in the hidden word but you placed it in the incorrect position. \nIf a dash appears, the letter is not in the word.\n")

    ai = bool("Activate AI? (true/false)")

    while not GameOver: 
        if ai == True: 
            guess = AIguess(feedback, guesses)
        elif ai == False:
            guess = getPlayerGuess()
        feedback = generateFeedback(guess, hiddenWord, feedback)
        displayFeedback(feedback)
        guesses.append(guess)
        if guess == hiddenWord or len(guesses) == 6: 
            GameOver = True

    return hiddenWord, guesses


if __name__ == "__main__":
    hiddenWord, guesses = playWordle() #steps 0 -3

    #4) When the game is over, display the hidden word
    print("\nThe correct word was: "+hiddenWord)

    if hiddenWord!=guesses[len(guesses)-1]:
        print("You lost.")
    else:
        print("You won in "+str(len(guesses))+ " guesses!")

    print("Your guesses:", guesses, "\n")