# 1. Read collected_data.txt
#
with open("collected_data.txt", "r") as quiz:
    to_answer = quiz.read()
print(to_answer)