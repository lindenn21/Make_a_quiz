# Create a program that makes a quiz, it includes questions, multiple choices, and scoring.

import time

# Opens collected_data.txt
file = open('collected_data.txt', 'w')

# List of questions
questions = []
print("Enter as many questions with multiple choices as you want: ")

# While loop: "Ask another question until the user chose to exit" as per sir's instructions.
while True:
    question = input(f"Enter a question: ")
    choice_a = input("Choice A: ")
    choice_b = input("Choice B: ")
    choice_c = input("Choice C: ")
    choice_d = input("Choice D: ")

# Asks for the correct answer among the choices.
    answer = input("What is the correct answer? (A, B, C OR D): ").upper()

# .append adds the inputted data into the list.
# Which is probably going to be important later on, based on how I plan to make this.
    questions.append({f"question: ": question,
                      "choices: ": {"A": choice_a,
                                    "B": choice_b,
                                    "C": choice_c,
                                    "D": choice_d}, "correct answer: ": answer})

    
# Writes the questions list into the txt file.
    file.write(f"Questions: {question}\n")
    file.write(f"A: {choice_a}\n")
    file.write(f"B: {choice_b}\n")
    file.write(f"C: {choice_c}\n")
    file.write(f"D: {choice_d}\n")
    file.write(f"{answer}\n")

# Asks the user if they want to add more questions for their quiz. If they answer N, it will stop.
    more_question = input("Would you like to add another question? (y/n): ").upper()
    if more_question != "Y":
        print(f"Preparing your quiz in..")
        for i in range(3, 0, -1):
            print(f"{i}")
            time.sleep(1)
        print("Your quiz is ready to be answered! Thank you.")
        break

file.close()



