import random

def FindLetterPositions(word, letter):
    positions = []
    pos = word.find(letter)
    while pos != -1:
        positions.append(pos)
        pos = word.find(letter, pos + 1)
    return positions

def GenerateClue(solution, guess):
    clue = ["B"] * len(solution)
    countedPos = []

    for index, (solutionLetter, guessLetter) in enumerate(zip(solution, guess)):
        if solutionLetter == guessLetter:
            clue[index] = "G"
            countedPos.append(index)

    for index, letter in enumerate(guess):
        if letter in solution and clue[index] != "G":
            positions = FindLetterPositions(solution, letter)
            for pos in positions:
                if pos not in countedPos:
                    clue[index] = "Y"
                    countedPos.append(pos)
                    break
    clueStr = ""
    for letter in clue:
        clueStr += letter
    return clueStr

with open("data/word_lists/word_list.txt", "r") as file:
    word_list = []
    for line in file:
        word_list.append(line.strip())

with open("data/word_lists/word_list_complete.txt", "r") as file:
    word_list_complete = []
    for line in file:
        word_list_complete.append(line.strip())

word_list.sort()
word_list_complete.sort()

def Main():
    while True:
        solution = random.choice(word_list)
        won_game = False

        for num_of_guesses in range(1, 7):
            guess = ""
            while not guess in word_list_complete:
                guess = input(f"\nWhat is your {num_of_guesses}. guess? ").lower()
                if not guess in word_list_complete:
                    print("The guess is not valid. Please try again:")
            clue = GenerateClue(guess, solution)
            print(f"The clue is {clue}")
            if clue == "GGGGG":
                print(f"Congratulations! You won the game in {num_of_guesses} guesses!")
                won_game = True
                break
            num_of_guesses += 1

        if not won_game:
            print(f"\nYou have run out of guesses! The solution was {solution}.")
        print("\n\n------------------------------------")
    
if __name__ == "__main__":
    Main()