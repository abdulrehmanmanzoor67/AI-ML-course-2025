# Print first 10 natural numbers using while 

number = 1

# loop until 10
while number <= 10:
    print('\n',number)
    number += 1


# Take Input from user , and print even number till that input number

limit = int(input("Enter a Number: "))

print("\nEven number till",limit , "are: ")

for num in range(0, limit + 1):
    if num % 2 == 0:
        print(num)

# Take Input from user , and print odd number till that input number 
limit = int(input("Enter a Number: "))

print("Odd number till", limit, "are: ")

for i in range (0, limit + 1):
    if i % 2 != 0:
        print(i)



#  Take Input from user , and print prime number till that input number

limit = int(input("Enter a number: "))

print(f"Prime numbers between 1 and {limit} are:")

for num in range(2, limit + 1):
    is_prime = True


    for i in range(2, int(num ** 0.5) + 1):
        if num % i == 0:
            is_prime = False  
            break

    if is_prime:
        print(num)



#  Print multiplication table of a given number 

num = int(input("Enter a number: "))

# print 1 to till 10
print(f"\nMultiplication Table of {num}:\n")

for i in range(1, 11):
    print(f"{num} x {i} = {num * i}")