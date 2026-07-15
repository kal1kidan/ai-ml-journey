# -----------------------------
# Mini Project 1 - Text Analyzer
# -----------------------------

paragraph = input("Please enter a paragraph: ")

words = paragraph.split()

# Count total words
word_count = len(words)

# Count how many times "Python" appears
python_count = 0

for word in words:
    cleaned_word = word.strip(".,!?;:").lower()

    if cleaned_word == "python":
        python_count += 1

# Find the longest word
longest_word = ""

for word in words:
    cleaned_word = word.strip(".,!?;:").lower()
    if len(cleaned_word) > len(longest_word):
        longest_word = cleaned_word

# Find unique words
unique_words = set(words)

# Display results
print("\n----- Text Analysis -----")

print("Total words:", word_count)
print("Python appears:", python_count, "time(s)")
print("Longest word:", longest_word)

print("\nUnique words:")
for word in unique_words:
    print(word)


