with open("data/word_lists/word_list_complete.txt") as file:
    word_list = []
    for line in file:
        word_list.append(line.strip())

num_of_words = len(word_list)

letters = [0] * 26
alphabet = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r", "s", "t", "u", "v", "w", "x", "y", "z"]

for word in word_list:
    for index, letter in enumerate(alphabet):
        if letter in word:
            letters[index] += 1

for index, letter in enumerate(alphabet):
    print(f"{letter}: {letters[index]}")

for index, letter in enumerate(letters):
    letters[index] /= num_of_words

print(letters)