'''
Create a program that asks the user for a number and then prints out a list of all the divisors of that number. 
(If you don’t know what a divisor is, 
it is a number that divides evenly into another number. 
For example, 13 is a divisor of 26 because 26 / 13 has no remainder.)
'''
n = input("Please enter a number")
n = int(n)

divisor_list = [] 

number_range = range(1, n+1)

for number in number_range:
    if n % number == 0:
        divisor_list.append(number)
    else:
        pass

print (divisor_list)
