"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: November 21 2019
Homework Problem: 14.1
Search key words
"""

import os.path
import sys
key_words = {"and", "as", "assert", "break", "class",
            "continue", "def", "del", "elif", "else",
            "except", "False", "finally", "for", "from",
            "global", "if", "import", "in", "is", "lambda",
            "None", "nonlocal", "not", "or", "pass", "raise",
            "return", "True", "try", "while", "with", "yield"}

filename = input("Enter a Python source code filename: ").strip()

if not os.path.isfile(filename):  # Check if target file exists
      print("File", filename, "does not exist")
      sys.exit()

# Open files for input
inputFile = open(filename, "r")
# Read and split words from the file to list
text = inputFile.read().split()
inputFile.close()