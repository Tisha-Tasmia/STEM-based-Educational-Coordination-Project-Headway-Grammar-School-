//Basic AI tutor program

import random

questions = {
    "What is AI?": "AI stands for Artificial Intelligence.",
    "What is Machine Learning?": "Machine Learning is a subset of AI that enables computers to learn from data.",
}

def ai_tutor():
    print("Welcome to AI Tutor! Ask me anything about AI.")
    while True:
        user_input = input("You: ")
        if user_input.lower() == "exit":
            print("Goodbye!")
            break
        response = questions.get(user_input, "I'm not sure. Try another question!")
        print("Tutor:", response)

if __name__ == "__main__":
    ai_tutor()
