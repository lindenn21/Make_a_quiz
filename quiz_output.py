# 1. Read collected_data.txt
# 2. Randomize the lines

import random
import time

for i in range(3, 0, -1):
    print(f"{i}\n")
    time.sleep(1)
print("GOODLUCK!!")

# Opens the txt file with inputted questions and answers
with open("collected_data.txt", "r") as the_quiz:
    quiz_content = the_quiz.readlines()

# This will put everything together once I append.
quiz = []
num = 0
while num < len(quiz_content):
    # Sets the line num and strip() cleans \n and unnecessary spaces
    line = quiz_content[num].strip()
    if line.startswith("Questions: "):
        question = line.strip()
        a = quiz_content[num + 1].strip()
        b = quiz_content[num + 2].strip()
        c = quiz_content[num + 3].strip()
        d = quiz_content[num + 4].strip()
        answer = quiz_content[num + 5].strip().upper()
        quiz.append({
            f"question": question,
            "choices": {"A": a, "B": b,
                        "C": c, "D": d},
            "correct_answer": answer
        })

        num += 6
    else:
        num += 1

random.shuffle(quiz)

score = 0
question_num = 1

for item in quiz:
    print(f"\nQuestion {question_num}: {item['question'][9:].strip()}") # reads only after the prefix "Question:"
    choices = item["choices"]
    print(f"A. {choices['A']}")
    print(f"B. {choices['B']}")
    print(f"C. {choices['C']}")
    print(f"D. {choices['D']}")
    users_answer = input("What is your answer?: (A/B/C/D): ").strip().upper()

    if users_answer == item['correct_answer'].upper():
        print("That is correct!")
        score += 1
        question_num += 1
    else:
        print(f"Wrong! The correct answer is {item['correct_answer']}")
        question_num += 1

print(f"Thank you! Your score is {score}")




















