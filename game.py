import random

def processGuess(answer, guess, double_letter, letter_double):
    position = 0
    clue = ""
    secret_word = answer
    guessed_double_letter = False

    for letter in guess:
        if double_letter:
            if letter == letter_double and guessed_double_letter:
                clue += "B"
            elif letter == letter_double:
                guessed_double_letter = True
                
                if letter == secret_word[position]:
                    clue += "G"
                elif letter in secret_word:
                    clue += "Y"
                else:
                    clue += "B"
            else:
                if letter == secret_word[position]:
                    clue += "G"
                elif letter in secret_word:
                    clue += "Y"
                else:
                    clue += "B"
        else:
            if letter == secret_word[position]:
                clue += "G"
            elif letter in secret_word:
                clue += "Y"
            else:
                clue += "B"

        position += 1

    print(clue)

    return clue == "GGGGG"

word_list = []
word_file = open("word_list.txt")
word_list_complete = []
word_file_complete = open("word_list_complete.txt")

for word in word_file:
    word_list.append(word.strip())

for word in word_file_complete:
    word_list_complete.append(word.strip())

answer = random.choice(word_list)

num_of_guesses = 0
guessed_correctly = False

while num_of_guesses < 6 and not guessed_correctly:
    guess = input("Type a 5-letter word: ")

    while not guess in word_list_complete:
        print("Your guess is not in the word list. Please try again.")
        guess = input("Type a 5-letter word: ")

    print("You have guessed " + guess + ".")
    num_of_guesses += 1

    double_letter = False
    letter_double = ""

    letters = []

    for i in range(0, len(guess)):
        if guess[i] in letters:
            double_letter = True
            letter_double = guess[i]
        letters.append(guess[i])

    if processGuess(answer, guess, double_letter, letter_double):
        print("Congratulations! You have guessed the word in", num_of_guesses, "guesses!")
        guessed_correctly = True
            
if not guessed_correctly:    
    print("You have run out of tries. The word was " + answer + ".")
