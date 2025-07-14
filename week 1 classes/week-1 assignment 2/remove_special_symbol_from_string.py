import string

text = input('Enter a string: ')


# string clean formula

clean_text = ""

for char in text:
    if char.isalnum() or char.isspace():
        clean_text += char

print('clean text: ', clean_text)