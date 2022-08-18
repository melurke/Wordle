import random

def GenerateClue(guess, solution): # Return the clue the game would give on a guess for a given solution
    solution_list = list(solution).copy()
    yellows = []
    clue = [""] * 5
    for index, letter in enumerate(guess):
        if letter == solution[index]:
            clue[index] = "G"
            for yellow in yellows:
                if yellow[1] == letter:
                    clue[max(yellows)[0]] = "B"
                    break
        elif letter in solution_list:
            solution_list.remove(letter)
            clue[index] = "Y"
            yellows.append([index, letter])
        else:
            clue[index] = "B"
    clueStr = ""
    for letter in clue:
        clueStr += letter
    return clueStr

with open("word_list.txt", "r") as file:
    word_list = []
    for line in file:
        word_list.append(line.strip())

with open("word_list_complete.txt", "r") as file:
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