# created by: Simon Vianen
# Wordl is a word guessing game where you have to guess a word by guessing letters in it.
# The game is played in the terminal.
# The word is randomly generated from an API.

import requests

MAX_POINTS = 10
corect_guesses = 0
incorect_guesses = 0
redacted_word = []
letters = []
amount_of_guesses = 0

# check if word length is between is valid. 
# should be between 5 and 10 or 0/none for random length
def check_word_lenght(word_length):
    if word_length == 0 or word_length == None:
        return
    if word_length > 10 or word_length < 5:
        print('your number was ' + str(word_length))
        word_length = input('Please enter a number between 5 and 10')
        quit_game(word_length)
        word_length = int(word_length)
        check_word_lenght(word_length)
    return

# get a random word from the API
# if word_length is 0 or None, don't use the word length parameter
# else use the word length parameter
def api_call(word_length):
    api_url = 'https://random-word.ryanrk.com/api/en/word/random'
    word_length_api = '/?length='
    if word_length != 0 or word_length != None:
        api_url = api_url + word_length_api + str(word_length)
    response = requests.get(api_url)
    if response.status_code != 200:
        return None
    response = response.text[1:-1]
    response = response.lower()
    return response

# split the word into letters and replace them with underscores
def split_word(word):
    letters = list(word)
    letters = [x for x in letters if x != '"']
    for letter in letters:
        redacted_word.append('_')
    return letters

# print the redacted word
def print_plaing_field():
    print(' '.join(redacted_word))

# check if the letter is in the word
def check_letter(guess, letters, corect_guesses, incorect_guesses):
    if guess in letters:
        corect_guesses += 1
        return True
    incorect_guesses += 1
    return False

# replace the underscore with the letter if it is in the word
def replace_letter(letter, letters):
    if letter in letters:
        for i in range(len(letters)):
            if letters[i] == letter:
                redacted_word[i] = letter
    return

# check if the user wants to quit the game
def quit_game(input):
    if input == 'quit' or input == 'exit':
        print('Goodbye!')
        exit()

# calculate the score
def calculate_score( amount_of_guesses, corect_guesses, incorect_guesses):
    if incorect_guesses == 0:
        score = MAX_POINTS /1
    else :
        score = MAX_POINTS / incorect_guesses
    score = score * corect_guesses
    score = score - amount_of_guesses
    return score

# ask the user for a letter and check if it is in the word
def ask_letter(letters, amount_of_guesses, corect_guesses, incorect_guesses):
    while True:
        guess = input('letter: ')
        amount_of_guesses+=1
        quit_game(guess)
        if check_letter(guess, letters, corect_guesses, incorect_guesses):
            corect_guesses += 1
            replace_letter(guess, letters)
            print_plaing_field()
        else:
            incorect_guesses += 1
            print('wrong letter')
        
        if '_' not in redacted_word:
            print('You win!')
            your_score = calculate_score(amount_of_guesses, corect_guesses, incorect_guesses)
            print ('Your score is: ' + str(your_score))
            break

# print the welcome text and instructions
def welcome_text():
    print('Welcome to Wordl!')
    print('You will be given a random word and you have to guess it')
    print('guess a letter and if it is in the word, it will be shown')
    print('If you guess the word you win, if not you lose')
    print('Good luck!')
    print("if you don't want to choose a word length, give 0 ")

def start_playing(corect_guesses, incorect_guesses):
    amount_of_guesses = 0
    welcome_text()
    word_length = input('How long do you want your word?(between 5 and 10) ')
    quit_game(word_length)
    word_length = int(word_length)
    check_word_lenght(word_length)
    word = api_call(word_length)
    letters = split_word(word)
    print_plaing_field()
    ask_letter(letters, amount_of_guesses, corect_guesses, incorect_guesses)

start_playing(corect_guesses, incorect_guesses)
