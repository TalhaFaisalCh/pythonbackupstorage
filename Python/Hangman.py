from FunctionsONLYasModules import read_file
import random
print('Welcome to Hangman!')
WordList, tries = read_file('words.txt'), 7  
word2guess = WordList[random.randint(0 , len(WordList) - 1)].lower()
print('Guess the word!', ' _ '*len(word2guess))
guessed_letters = ['_'] * len(word2guess)
while tries >= 1:
    choice = input('Guess the word: ').lower()
    if choice in word2guess:
        guessed_letters = [word2guess[i] if choice == word2guess[i] else guessed_letters[i] for i in range(0, len(word2guess))]
        print(guessed_letters)  
    else:
        tries -= 1
        print('You have', tries, 'tries remaining!')
    if '_' not in guessed_letters:
        print('CONGURATULATIONS! you guessed the word!')
        quit()
print('You lost noob, the word was:', word2guess)                                                                                   