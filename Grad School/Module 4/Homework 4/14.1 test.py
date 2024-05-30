import sys
key_words = {"and", "as", "assert", "break", "class",
            "continue", "def", "del", "elif", "else",
            "except", "False", "finally", "for", "from",
            "global", "if", "import", "in", "is", "lambda",
            "None", "nonlocal", "not", "or", "pass", "raise",
            "return", "True", "try", "while", "with", "yield"}

filename = input("Enter a Python source code filename: ")

inputFile = open(filename, "r")

text = inputFile.read().split()  # Read and split words from the file
inputFile.close()

count = 0
for word in text:
    if word in key_words:  # Test if word is in key_Words
        count += 1

print("The number of keywords in", filename, "is", count)