def quiz_game():
    question = {
        "What is the capital of France?": "Paris",
        "What is 5 + 6?": "11",
        "What is the square root of 16?": "4",
        "Who wrote 'To kill a Mockingbird'?": "Harper Lee"
    }
    
score = 0

for question , answer in question.items():
    user_answer = input(f"{question}")
    if  user_answer.lower() == answer.lower():
        print("Correct")
        score += 1
    else:
        print(f"Wrong! correct answer is {answer}")

print(f"\n Your  final score is: {score} out of {len(question)}")


quiz_game()