# Input marks of 5 subjects
sub1 = float(input("Enter marks of Subject 1: "))
sub2 = float(input("Enter marks of Subject 2: "))
sub3 = float(input("Enter marks of Subject 3: "))
sub4 = float(input("Enter marks of Subject 4: "))
sub5 = float(input("Enter marks of Subject 5: "))

# Total marks
total_marks = sub1 + sub2 + sub3 + sub4 + sub5

# Average marks
average = total_marks / 5

# Percentage (assuming each subject is out of 100)
percentage = (total_marks / 500) * 100

# Output
print("Total Marks =", total_marks)
print("Average Marks =", average)
print("Percentage =", percentage, "%")
