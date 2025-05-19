print ("Hello World!")
# Assigning variables. Variables are more like containers that stores data or information that will be used whenever needed
#Assigning a string(s) to a variable
A = "My first step in learning python"
#Assigning an integer to a variable
B = 10
#Printing out the outcome
print (A)
print (B)
# Assigning multiple variables in one line
cars = "Ranger", "Hilux", "Land Cruiser"
#Unpacking is when you assign value from the list to a variables
x, y, z = cars
print (z, z, x, y)
# Count from 1 to 10, writing each number on its own line.
# The first option I used is:
print ("FIRST OPTION")
numbering = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
for x in numbering:
    print (x)
# The second option used by WTC is:
print ("SECOND OPTION")
number_range = range(1, 11)
for y in number_range:
    print (y)
# The third option is:
print ("THIRD OPTION")
count = 1
while count <= 10:
    print (count)
    count += 1
# HOW ABOUT COUNTING FROM 10 TO 1?...
print("alternative 1")
count = 10
while count >= 1:
    print (count)
    count -= 1
#GREETING MULTIPLE PEOPLE
names = ["Manelisi", "Tshemologo", "Lehlohonono", "Phawu"]
for item in names:
    print ("Hello,", item)