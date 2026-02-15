# AIM: Develop a Python program that reads a text file and 
# prints words of specified lengths (e.g., three, four, 
# five, etc.) found within the file.
# Coder: Soni Chauhan
# Date: 11/02/2026

print("--- Extracting Words from Text File ---\n")

with open("story.txt", "r") as file:
    content = file.read()
    words = content.split()
    word_length = int(input("Enter length of Words: "))
    unique_set = set()

    for word in words:
        word = word.lower()
        if len(word) == word_length:
            unique_set.add(word)

    print(f"\nWords with length {word_length} are: {sorted(unique_set)}")        

