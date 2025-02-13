//Interactive AI Quiz Bot

import random

questions = {
    "What does AI stand for?": ["Artificial Intelligence", "Automated Interface", "Advanced Internet"],
    "Which language is commonly used for AI?": ["Python", "Java", "C++"],
}

def quiz():
    score = 0
    for question, options in questions.items():
        print(f"\n{question}")
        for i, option in enumerate(options, 1):
            print(f"{i}. {option}")
        answer = input("Your answer (1/2/3): ")
        if answer == "1":
            print("Correct!")
            score += 1
        else:
            print("Wrong!")
    print(f"\nYour final score: {score}/{len(questions)}")

if __name__ == "__main__":
    quiz()
