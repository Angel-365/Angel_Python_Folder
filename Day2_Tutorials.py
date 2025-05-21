# Parity Tutorial
# Parity is when we check for a remainder of an integer
def parity(x):
    if x%2 == 0:
        return "Even"
    else:
        return "Odd"
x = 10
print ("Answer : ",parity(x))
# checking for AVERAGE value
def average_value(numbers):
    return (sum(numbers)/len(numbers))
numbers = [1, 5, 7, 10]
print ("average_value ", average_value(numbers))
print ("Sum : ", sum(numbers))
print("Length  = ", len(numbers))

