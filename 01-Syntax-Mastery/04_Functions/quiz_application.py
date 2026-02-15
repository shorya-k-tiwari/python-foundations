"""
Quiz Application
"""

questions = {
    "What is the capital of France?": "paris",
    "Which planet is known as the Red Planet?": "mars",
    "What is 5 + 7?": "12",
    "Who developed Python language?": "guido van rossum"
}

def ask_question(question, correct_answer):
    user_answer = input(f"{question}\nYour answer: ").strip().lower()
    if user_answer == correct_answer:
        print("Nice, that's right\n")
        return 1
    print(f"Not quite. The answer is: {correct_answer}\n")
    return 0

def run_quiz():
    score = 0
    total = len(questions)

    print("\nLet's do a quick quiz\n")
    for question, answer in questions.items():
        score += ask_question(question, answer)
    print("Quiz complete.")
    print(f"Your score: {score}/{total}")

def main():
    print("Python Quiz")
    run_quiz()

if __name__ == "__main__":
    main()
