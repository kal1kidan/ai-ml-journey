with open("sample.txt", "w") as file:
    file.write("Python is amazing.\nAI is the future.\nPractice every day.")

with open("sample.txt", "r") as file:
    content = file.read()

print(content)

number_of_lines = len(content.splitlines())
number_of_words = len(content.split())
number_of_characters = len(content)

print("Number of lines:", number_of_lines)
print("Number of words:", number_of_words)
print("Number of characters:", number_of_characters)


entry = input("Enter your journal entry: ")

with open("journal.txt", "a") as file:
    file.write(entry + "\n\n")

with open("journal.txt", "r") as file:
    journal_content = file.read()

print("\nYour Journal Entries:")
print(journal_content)