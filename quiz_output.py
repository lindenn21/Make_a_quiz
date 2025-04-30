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






