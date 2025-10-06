def quiz_app():
    questions = {
        "What is the capital of India?": "Delhi",
        "Which language is this quiz written in?": "Python",
        "Who developed Python?": "Guido van Rossum",
        "What is 5 + 3?": "8"
    }

    score = 0
    print("🎯 Welcome to the Quiz App!\n")

    for question, answer in questions.items():
        user_answer = input(f"{question} ").strip()
        if user_answer.lower() == answer.lower():
            print("✅ Correct!\n")
            score += 1
        else:
            print(f"❌ Wrong! Correct answer: {answer}\n")

    print(f"Your final score: {score}/{len(questions)}")

quiz_app()
