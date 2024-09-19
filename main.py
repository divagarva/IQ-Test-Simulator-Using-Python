import random

# Define the questions
questions = [
    {
        "question": "What comes next in the sequence: 2, 4, 8, 16, ?",
        "options": ["20", "32", "24", "30"],
        "answer": "32"
    },
    {
        "question": "Solve: 15 + 3 * 2 = ?",
        "options": ["21", "16", "19", "22"],
        "answer": "21"
    },
    {
        "question": "Which word does not belong: Cat, Dog, Bird, Fish?",
        "options": ["Fish", "Bird", "Dog", "Cat"],
        "answer": "Fish"
    },
    {
        "question": "Find the odd one out: 25, 36, 49, 63?",
        "options": ["49", "25", "36", "63"],
        "answer": "63"
    },
    {
        "question": "If all Bloops are Razzies and all Razzies are Lazzies, then all Bloops are definitely Lazzies. True or False?",
        "options": ["True", "False"],
        "answer": "True"
    }
]


# Function to run the IQ test
def iq_test():
    score = 0
    # Randomize the order of the questions
    random.shuffle(questions)

    for i, q in enumerate(questions):
        print(f"Q{i + 1}: {q['question']}")
        for idx, option in enumerate(q['options'], 1):
            print(f"{idx}. {option}")

        # Get the user's answer
        user_answer = input("Enter the correct option number: ")

        # Check if the answer is correct
        if q['options'][int(user_answer) - 1] == q['answer']:
            score += 1
        print()  # For spacing between questions

    return score


# Function to calculate the IQ level based on score
def calculate_iq(score, total):
    percentage = (score / total) * 100
    if percentage >= 80:
        return "Genius"
    elif percentage >= 60:
        return "Above Average"
    elif percentage >= 40:
        return "Average"
    else:
        return "Below Average"


# Main execution
if __name__ == "__main__":
    print("Welcome to the IQ Test Simulator!\n")

    total_questions = len(questions)
    score = iq_test()

    # Calculate IQ level based on the score
    iq_level = calculate_iq(score, total_questions)
    print(f"Your score is {score}/{total_questions}. You are {iq_level}.")