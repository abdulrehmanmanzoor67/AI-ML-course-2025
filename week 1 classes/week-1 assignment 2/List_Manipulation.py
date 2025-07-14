# Reverse a List

print ('Start Here')

list = [20, 25, 35, 40, 60]

# Reverse the list using slicing
reversed_list = list[::-1]


print('Orignal list: ', list)
print('Reversed list: ', reversed_list)

print('End Here')


# Square Every Item in a List

print("Start Here")

list = [2, 5, 7, 9, 10]

# Square each number using list
squared_num = [num ** 2 for num in list]


print("Orignal list: ", list)
print("Squared list: ", squared_num)

print("End Here")

# Remove Empty Strings from a List

print("Start Here")

# List with empty strings
list = ["apple", "", "banana", "", "cherry", ""]

# Remove empty strings
cleaned_list = [word for word in list if word != ""]

print("Orignal List: ", list)
print("Cleaned List: ", cleaned_list)

print("End Here")

# Add New Item After a Specified Item

print("Start Here")

fruits = ["Apple", "Banana", "Cherry"]

# add new item
new_item = "Mango"

# After which item to add
after_item = "Banana"

if after_item in fruits:
    index = fruits.index(after_item)
    fruits.insert(index + 1, new_item)

print("Updated list: ", fruits)

print("End Here")

# Replace Item in List if Found

print("Start Here")

list = ["Apple", "Orange", "Banana", "Cherry"]

# item to replace
old_item = "Banana"

# add new item
new_item = "Mango"

for i in range(len(list)):
    if list[i] == old_item:
        list[i] = new_item


print("Updated list: ", list)

print("End Here")

