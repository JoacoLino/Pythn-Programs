"""
Given an integer num, repeatedly add all its digits until the result has only one digit, and return it.

 

Example 1:

Input: num = 38
Output: 2
Explanation: The process is
38 --> 3 + 8 --> 11
11 --> 1 + 1 --> 2 
Since 2 has only one digit, return it.
Example 2:

Input: num = 0
Output: 0
"""
def sumarDigitos(num):
    num2 = 0
    while num > 0:
        num2 = num2 + num % 10
        num = num // 10
    return num2

def addDigits(num):
    num2 = sumarDigitos(num)
    salir = False
    while num2 > 9 and salir == False:
        num2 = sumarDigitos(num2)
    print(num2)
    return num2


    


addDigits(708538619)