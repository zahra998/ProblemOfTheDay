'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''
a = input("Enter the first number: ")
b = input("Enter the secound number: ")
c = input("Enter the third number: ")
largest = 0

if a == b == c:
    
    print('The entered numbers are equal')

elif (a >= b) and (a >= c):

    largest = a
    print(largest + " is the largest number")

elif (b >= a) and (b >= c):

    largest = b
    print(largest + " is the largest number")
else:

    largest = c
    print(largest + " is the largest number")



