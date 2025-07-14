# Check if a value exists in a dictionary

# Dictionary
student = {"name": "Abdul Rehman Manzoor","age": 22,"city": "Lahore"}

# Value to check
value_check = "Lahore"

# Check if value exists
if value_check in student.values():
    print("Yes, the value exists in the dictionary.")
else:
    print("No, the value does not exist.")

# Get the key of a minimum value from the following dictionary

# Marks of students
marks = {"Ali": 85,"Zara": 92,"Ahmed": 78,"Fatima": 88}

# Step 1: Use min() to find the key with the smallest value
min_key = min(marks, key=marks.get)

# Step 2: Print the result
print(f"The student with the lowest marks is {min_key} with {marks[min_key]} marks.")


# Delete a list of keys from a dictionary
my_profile = {"Name": 'Abdul Rehman Manzoor', "Age": 22, "Grade": 'A', "City": 'Lahore', "phone": '03014785526'}

# key remove from dictionary

key_remove = ["phone"]

# deleting key
for key in key_remove:
    if key in my_profile:
        del my_profile[key]


print("Updated key: ", my_profile)
