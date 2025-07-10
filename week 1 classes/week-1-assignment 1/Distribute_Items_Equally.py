# input from user
candies = int(input('Enter total candies: '))
students = int(input('Enter total students: '))


each_students = candies // students   # floor division
leftover = candies % students         # reminder


# result
print('Each student gets: ', each_students, 'candies')
print('Leftover candies: ', leftover)