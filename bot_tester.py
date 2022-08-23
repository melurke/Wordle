def FindLetterPositions(word, letter):
    positions = []
    pos = word.find(letter)
    while pos != -1:
        positions.append(pos)
        pos = word.find(letter, pos + 1)
    return positions

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

def Green(word, greenLetters, greenPositions):
    for index, letter in enumerate(greenLetters):
        if word[greenPositions[index]] != letter:
            return False
    return True

def Yellow(word, yellowLetters, yellowPositions):
    for index, letter in enumerate(yellowLetters):
        if word[yellowPositions[index]] == letter:
            return False
        elif not letter in word:
            return False
    return True

def Black(word, blackLetters, greenLetters):
    for letter in blackLetters:
        if letter in word:
            if letter in greenLetters and word[word.index(letter)] == letter:
                pass
            else:
                return False
    return True

def AddLetters(guess, clue):
    greenLetters = []
    greenPositions = []
    yellowLetters = []
    yellowPositions = []
    blackLetters = []

    for index, letter in enumerate(clue):
        if letter == "G":
            greenLetters.append(guess[index])
            greenPositions.append(index)
        elif letter == "Y":
            yellowLetters.append(guess[index])
            yellowPositions.append(index)
        else:
            blackLetters.append(guess[index])
    blackLetters = list(dict.fromkeys(blackLetters))

    for letter in blackLetters.copy():
        if letter in greenLetters or letter in yellowLetters:
          blackLetters.remove(letter)

    return [greenLetters, greenPositions, yellowLetters, yellowPositions, blackLetters]

def GetPossibleSolutions(guessedWords, wordList, greenLetters, greenPositions, yellowLetters, yellowPositions, blackLetters):
    possibleSolutions = []
    for word in wordList:
        if Green(word, greenLetters, greenPositions) and Yellow(word, yellowLetters, yellowPositions) and Black(word, blackLetters, greenLetters) and not word in guessedWords:
            possibleSolutions.append(word)
    return possibleSolutions

def GetWordClues(possibleSolutions, allWords):
    clues = []
    for word in allWords: 
        wordClues = []
        for solution in possibleSolutions:
            currentClue = GenerateClue(solution, word)
            if not currentClue in wordClues:
                wordClues.append(currentClue)
        clues.append([len(wordClues), word, wordClues])
    clues.sort()
    clues.reverse()
    return clues

def Play(guess, clue, guessedWords, wordList, allWords, greenLetters, greenPositions, yellowLetters, yellowPositions, blackLetters):
    newLists = AddLetters(guess, clue)
    greenLetters += newLists[0]
    greenPositions += newLists[1]
    yellowLetters += newLists[2]
    yellowPositions += newLists[3]
    blackLetters += newLists[4]

    possibleSolutions = GetPossibleSolutions(guessedWords, wordList, greenLetters, greenPositions, yellowLetters, yellowPositions, blackLetters)

    if len(possibleSolutions) == 1 or len(possibleSolutions) == 2:
        return possibleSolutions[0]

    clues = GetWordClues(possibleSolutions, allWords)
    return clues[0][1]

def ProcessGames(games):
    average = 0
    numbers = [0] * 6
    for game in games:
        average += game
        numbers[game-1] += 1
    average /= len(games)
    return [average, numbers]

with open("data/word_lists/word_list.txt", "r") as file:
    wordList = []
    for line in file:
        wordList.append(line.strip())

with open("data/word_lists/word_list_complete.txt", "r") as file:
    allWords = []
    for line in file:
        allWords.append(line.strip())

wordList.sort()
allWords.sort()

games = []

def Main():
    for index, solution in enumerate(wordList):
        greenLetters = []
        greenPositions = []
        yellowLetters = []
        yellowPositions = []
        blackLetters = []
        guessedWords = []
        guesses = []

        guess = "trace"
        for numOfGuesses in range(1, 7):
            guesses.append(guess)
            clue = GenerateClue(solution, guess)

            if clue == "GGGGG" or numOfGuesses == 6:
                games.append(numOfGuesses)
                print(str(index / len(wordList) * 100)[0:5], solution, numOfGuesses)
                break

            guessedWords.append(guess)
            guess = Play(guess, clue, guessedWords, wordList, allWords, greenLetters, greenPositions, yellowLetters, yellowPositions, blackLetters)

    process = ProcessGames(games)
    for index, number in enumerate(process[1]):
        print(f"{index + 1}: {number}")
    print(f"Average: {process[0]}")

if __name__ == "__main__":
    Main()