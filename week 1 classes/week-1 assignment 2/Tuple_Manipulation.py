# Reverse the tuple 

# Orignal tuple
org_tuple = (10,20,30,40,50)

# reveresed the org tuple
reversed_tuple = org_tuple[::-1]

# result
print("\nOrignal Tuple: ", org_tuple)
print("Reversed Tuple: ", reversed_tuple)


# Access value 20 from the tuple

# Tuple banate hain
my_tuple = (10, 20, 30, 40, 50)

# The value 20 is at index 1 (because Python starts counting from 0)
value = my_tuple[1]

# Print karo value
print("\nThe value is:", value)


# Swap two tuples in Python

# Define Two tuples

tuple1 = (1,2,3)
tuple2 = (4,5,6)

print("\nOrignal tuples:" ,"Tuple 1: ", tuple1, "Tuple 2: ", tuple2)

# swap the tuple
tuple1, tuple2 = tuple2, tuple1

print("After Swapping:", "tuple 1: ", tuple1, "tuple 2: ", tuple2)