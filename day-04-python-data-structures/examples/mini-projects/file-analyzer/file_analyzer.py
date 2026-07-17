import os

folder = os.path.dirname(__file__)
filename = input("Please enter a file name: ")

entry = os.path.join(folder, filename)

try:
    with open(entry, "r") as file:
        content = file.read()

    print(content)

    number_of_lines = len(content.splitlines())
    number_of_words = len(content.split())
    number_of_characters = len(content)

    print(f"Number of lines: {number_of_lines}")
    print(f"Number of words: {number_of_words}")
    print(f"Number of characters: {number_of_characters}")


    words_in_file = content.split()

    word_count = {}

    for word in words_in_file:
        word = word.lower().strip(".,!?;:")

        if word in word_count:
            word_count[word] += 1
        else:
            word_count[word] = 1


    most_common_word = max(word_count, key=word_count.get)

    print("Most common word:", most_common_word)
    print("Used:", word_count[most_common_word], "times")


except FileNotFoundError:
    print("File doesn't exist")