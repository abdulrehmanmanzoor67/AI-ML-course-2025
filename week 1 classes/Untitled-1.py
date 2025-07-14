my_string = ("50")
print(type(my_string))

new_type= (int(my_string))
print(type(new_type))

my_string1 = "pakistan"
sub_string = my_string1[3:5]
sub_string1 = my_string1[7:8]
print(sub_string.lower())
print(sub_string1.lower())

institute = ["Nexskill", 20, 40.5]
print(institute)
print(type(institute))

for i in institute:
    print(i)


institute1 = ('Fahad Iqbal Sheikh',"Nexskill", 2010 ,40.5 )
print(type(institute1))
print(institute1)

for i in institute1:
    print(i)


institute2 = {"Name": "Fahad Iqbal Sheikh", "institute": "Nexskill", "distance": 40.5, "year": 2010}
print(type(institute2))


for i in institute2:
    print(i)


institute3 = {"Fahad Iqbal Sheikh", "Nexkill", 2010, 40.5 }
print(type(institute3))
print(institute3)

for i in institute3:
    print(i)