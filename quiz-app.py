# Simple Quiz App

# List of quiz questions and their answers
quiz = [
    {"question": "What is the capital of France?", "answer": "Paris"},
    {"question": "What is 5 + 7?", "answer": "12"},
    {"question": "What is the largest planet in our solar system?", "answer": "Jupiter"},
    {"question": "What is the square root of 64?", "answer": "8"},
    {"question": "Who wrote 'To Kill a Mockingbird'?", "answer": "Harper Lee"}
]

# Initialize score
score = 0

# Function to run the quiz.
def run_quiz():
    global score
    print("Welcome to the Quiz App!")
    print("------------------------")

    # Loop through each question in the quiz
    for q in quiz:
        # Ask the question
        user_answer = input(q["question"] + " ")

        # Check if the answer is correct
        if user_answer.lower() == q["answer"].lower():
            print("Correct!\n")
            score += 1
        else:
            print(f"Wrong! The correct answer is {q['answer']}\n")

    # Display the final score
    print(f"Your final score is {score}/{len(quiz)}")

# Run the quiz
if __name__ == "__main__":
    run_quiz()
