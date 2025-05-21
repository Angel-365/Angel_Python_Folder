# Assigning variables
a = 5
b = 2 
print ("Sum = ", a + b)
print ("Product = ", a*b)
print("Difference = ", a-b)
print ("Ratio/Dividend = ", a/b)

# Greeting multiple people
people = ["Manelisi", "Tshemo", "Lehlohonono"]
for item in people:
    print ("Hello, ", item)

# Compound interest problem 
starting_capital = 1000
interest = 1.05
monthly_contribution = 250
months = 8 
Total = starting_capital # Initially this is the amount I'm starting with
# Since we want calculating for 8 months
for each_month in range (months):
    Total = (Total*interest) + monthly_contribution
print("Total-amount = ", Total)

#Counting problems
count = 0
while count < 31:
    print (count)
    count +=1
    
numbers = range (1,11)
for x in numbers:
    print (x)

print ("count_down".upper())
count = 10
while count >0:
    print (count)
    count -=1