# Input from user
total_questions = int(input("Enter total number of questions: "))
correct_answers = int(input("Enter number of correct answers: "))

# Calculate percentage
percentage = (correct_answers / total_questions) * 100

# Output result
print("Your score is:", percentage, "%")
