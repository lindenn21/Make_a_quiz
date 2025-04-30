# 1. Read collected_data.txt
# 2. Randomize the lines

import random

# Opens the txt file with inputted questions and answers
with open("collected_data.txt", "r") as the_quiz:
    quiz_content = the_quiz.readlines()

random.shuffle(quiz_content)

quiz = []
num = 0
while num < len(quiz_content):

