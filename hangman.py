#Python program to illustrate Hangman 

#Python modules
import random
from collections import Counter

#List of Fruits to guess from
some_words = ['apple', 'banana', 'mango', 'strawberry', 'orange', 'grape', 'pineapple', 'apricot', 'lemon', 'coconut', 'watermelon', 'cherry', 'papaya', 'berry', 'peach', 'lychee', 'muskmelon']

#randomly choose a secret word from our "some_words" LIST
word = random.choice(some_words)

if __name__ == '__main__':
    print("Guess the word! HINT: word is a name of a fruit")

    for i in word:
        print("_", end=' ')  # Pritnting the empty spaces for letters of the word

    playing = True

    letter_guessed = ''
    chances = len(word) + 2
    correct = 0
    flag = 0

    try:
        while (chances != 0) and (flag == 0):
            print()
            chances -= 1

            try:
                guess = str(input("Enter a letter to guess: "))
            except:
                print("Enter only a letter!")
                continue

            #Validation of guess
            if not guess.isalpha():
                print("Enter only a LETTER")
                continue
            elif len(guess) > 1:
                print("Enter a SINGLE letter")
                continue
            elif guess in letter_guessed:
                print("you have already guessed that letter")
                continue

            #if letter is guessed correctly
            if guess in word:
                k = word.count(guess)
                for _ in range(k):
                    letter_guessed += guess #The guessed letter is added as many times as it occurs

                for char in word:
                        if char in letter_guessed and Counter(letter_guessed) != Counter(word):
                            print(char, end='')
                            correct += 1
                            #if user has guessed all the letters
                            #Once the corrrect word is fully guessed
                        elif (Counter(letter_guessed) == Counter(word)):
                            #the game end, even if chances remain
                            print("The word is : ", end ='')
                            print(word)
                            flag = 1
                            print("Conratulations, You won!")
                            break #break out of for loop
                            break #break out of the while loop
                        else:
                            print('_', end='')

            #Losing Condition
            if chances <= 0 and Counter(letter_guessed) != Counter(word):
                    print()
                    print("You lost!, Try again.")
                    print(f"The word was {format(word)}")

    except KeyboardInterrupt: #Catch Exception error
        print()
        print('Bye! Try again')
        exit()