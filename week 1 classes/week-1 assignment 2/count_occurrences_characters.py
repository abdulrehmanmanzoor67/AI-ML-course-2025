
# Input from User

text = input('Enter a string: ')

# Dictionary to store character counts

character_count = {}

for char in text:
    if char in character_count:
        character_count[char] += 1

    else:
        character_count[char] = 1

# Print Result:

for char, count in character_count.items():
    print(f"'{char}' appears {count} times") 