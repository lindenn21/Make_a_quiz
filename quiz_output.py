# 1. Read collected_data.txt
#

import random
with open("collected_data.txt", "r") as quiz:
    to_answer = quiz.readlines()

random.shuffle(to_answer)
print(to_answer)