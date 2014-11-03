import random

def get_len(wordslist):
    order = []
    i = 0 
    while i < len(wordslist):
        order.append(i)
        i += 1
    return order

def hangman(x):    
    if  x == 1:
        print("____________")
    if  x == 2:
        print("____________") 
        print("|          | ")
    if  x == 3:
        print("____________")
        print("|          | ")        
        print("|           O")
    if  x == 4:
        print("____________")
        print("|          | ")        
        print("|           O")        
        print("|          / |")
    if  x == 5:
        print("____________")
        print("|          | ")        
        print("|           O")        
        print("|          / |")        
        print("|           |")
    if  x == 6:
        print("____________")
        print("|          | ")        
        print("|           O")        
        print("|          / |")        
        print("|           |")        
        print("|          / |")
        print("|")
        print("|")

def errorchecking():
    while True:
        try:
            select = input("Please enter an integer number (0<=number<10) to choose the word in the list: ")
            if select == '':
                print("Empty input!")
            else:
                select = int(select)
                if select in get_len(words):
                    break#
                else:
                    print("Index out of range!")
        except Exception:
            print("Input must be an integer!")    
            
def set_up():
    print("The length of the word is: ",len(words[select]))
    n = len(words[select])
    rightlst = list(words[select])
    puzzles = '_'*(len(rightlst))
    printlst = list(puzzles)
    insert = 0 
    secscan = 0
    n1 = len(rightlst)
    match = 0
    determine = 0    
    
def count_and_match():
    while determine < n1 and firscan < 6:
            while True:
                guess = input("Please enter the letter you guess: ")
                if guess.isalpha() == True:
                    if len(guess) > 1:
                        print("You need to input a single alphabetic character!")
                    else:
                        break#
                else:
                    print("You need to print a single alphabetic character!")
                    
            if guess not in rightlst:
                firscan += 1
                print("The letter is not in the word.")
                print("Letters matched so far:",''.join(printlst))
                hangman(firscan)
            elif guess in printlst:
                firscan += 1
                print("Error,you have already get this letter.")
                print("The letter is not in the word.")
                print("Letters matched so far:",''.join(printlst))
                hangman(firscan)
            else:
                while insert < n1 :
                    if rightlst[insert] == guess:
                        match +=1
                        printlst[insert] = guess
                    insert += 1
                secscan = match
                insert = 0
                print("The letter is in the word.")
                print("Letters matched so far:",''.join(printlst))        
                firscan = firscan
            firscan = firscan
            determine = secscan
        
        if firscan == 6:
            print("Too many incorrect guesses. You lost!")
            print("The word was: ",words[select])
            print("Goodbye!")
        elif determine == n1:
            print("You have found the mystery word. You win!")
            print("Goodbye!")    


def main():
    words = ['cow', 'horse', 'deer', 'elephant', 'lion', 'tiger', 'baboon', 'donkey', 'fox', 'giraffe']
    print("Welcome to Hangman! Guess the mystery word with less than 6 mistakes!")
    
    while True:
        try:
            select = input("Please enter an integer number (0<=number<10) to choose the word in the list: ")
            if select == '':
                print("Empty input!")
            else:
                select = int(select)
                if select in get_len(words):
                    break#
                else:
                    print("Index out of range!")
        except Exception:
            print("Input must be an integer!")
    
    
            
    print("The length of the word is: ",len(words[select]))
    n = len(words[select])
    rightlst = list(words[select])
    puzzles = '_'*(len(rightlst))
    printlst = list(puzzles)
    insert = 0 
    secscan = 0
    n1 = len(rightlst)
    match = 0
    determine = 0    

    firscan = 0        
    while determine < n1 and firscan < 6:
        while True:
            guess = input("Please enter the letter you guess: ")
            if guess.isalpha() == True:
                if len(guess) > 1:
                    print("You need to input a single alphabetic character!")
                else:
                    break#
            else:
                print("You need to print a single alphabetic character!")
                
        if guess not in rightlst:
            firscan += 1
            print("The letter is not in the word.")
            print("Letters matched so far:",''.join(printlst))
            hangman(firscan)
        elif guess in printlst:
            firscan += 1
            print("Error,you have already get this letter.")
            print("The letter is not in the word.")
            print("Letters matched so far:",''.join(printlst))
            hangman(firscan)
        else:
            while insert < n1 :
                if rightlst[insert] == guess:
                    match +=1
                    printlst[insert] = guess
                insert += 1
            secscan = match
            insert = 0
            print("The letter is in the word.")
            print("Letters matched so far:",''.join(printlst))        
            firscan = firscan
        firscan = firscan
        determine = secscan
    
    if firscan == 6:
        print("Too many incorrect guesses. You lost!")
        print("The word was: ",words[select])
        print("Goodbye!")
    elif determine == n1:
        print("You have found the mystery word. You win!")
        print("Goodbye!")    
main()

def endings():
    if count1 == 6:
        print("Too many incorrect guesses. You lost!")
        print("The word was: ",words[select])
        print("Goodbye!")
    elif count == n1:
        print("You have found the mystery word. You win!")
        print("Goodbye!")        
