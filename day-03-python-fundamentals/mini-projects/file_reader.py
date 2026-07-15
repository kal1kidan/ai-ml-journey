# Mini Project 2 - Safe File Reader

try:
    filename = input("Enter the file name: ")

    with open(filename, "r") as file:
        content = file.read()

    print("\nFile Content:")
    print(content)

    lines = len(content.splitlines())
    words = len(content.split())
    characters = len(content)

    print("\n----- File Statistics -----")
    print(f"Lines: {lines}")
    print(f"Words: {words}")
    print(f"Characters: {characters}")

except FileNotFoundError:
    print("Error: File not found.")

finally:
    print("\nProgram finished.")