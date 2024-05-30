"""
Author: Emeka Udogwu
Comment: MET CS 521 - Fall 2
Date: November 21 2019
Homework Problem: 11.3
Sort Grades of students
"""

# Create empty list
student_list = []
# Students' answers to the questions
answers = [
    ['A', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
    ['D', 'B', 'A', 'B', 'C', 'A', 'E', 'E', 'A', 'D'],
    ['E', 'D', 'D', 'A', 'C', 'B', 'E', 'E', 'A', 'D'],
    ['C', 'B', 'A', 'E', 'D', 'C', 'E', 'E', 'A', 'D'],
    ['A', 'B', 'D', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
    ['B', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
    ['B', 'B', 'A', 'C', 'C', 'D', 'E', 'E', 'A', 'D'],
    ['E', 'B', 'E', 'C', 'C', 'D', 'E', 'E', 'A', 'D']]

keys = ['D', 'B', 'D', 'C', 'C', 'D', 'A', 'E', 'A', 'D']
for i in range(len(answers)):
    # Grade one student and counts the number correct
    correct_count = 0
    for j in range(len(answers[i])):
        if answers[i][j] == keys[j]:
            correct_count += 1
# After counted, get pair and place in list
    student_list.append([correct_count, i])
# Student list gets sorted in order
student_list.sort()
# Print out student and grade according to list
for grade, student in student_list:
    print("Student", student, "'s correct count is", grade)
