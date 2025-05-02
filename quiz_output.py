# 1. Read collected_data.txt
# 2. Randomize the lines

# Opens the txt file with inputted questions and answers
with open("collected_data.txt", "r") as the_quiz:
    quiz_content = the_quiz.readlines()

# This will put everything together once I append.
quiz = []
num = 0
while num < len(quiz_content):
    # Sets the line num and strip() cleans \n and unnecessary spaces
    line = quiz_content[num].strip()
    if line.startswith("Question:"):
        question = line[num].strip()
        a = line[num + 1].strip()
        b = line[num + 2].strip()
        c = line[num + 3].strip()
        d = line[num + 4].strip()
        answer = line[num + 5].strip()
        quiz.append({
            f"question": question,
            "choices": {"A": a, "B": b,
                        "C": c, "D": d},
            "correct answer": answer
        })

        num += 6
    else:
        num += 1

score = 0
question_num = 1

for item in quiz:
    print(f"\nQuestion: {question_num}: {item['question'][9:].strip()}") # reads only after the prefix "Question:"
    choices = item["choices"]
    print(f"A. {choices['A']}")
    print(f"B. {choices['B']}")
    print(f"C. {choices['C']}")
    print(f"D. {choices['D']}")



















