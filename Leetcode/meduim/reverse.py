"""
Given a signed 32-bit integer x, return x with its digits reversed. If reversing x causes the value to go outside the signed 32-bit integer range [-231, 231 - 1], then return 0.

Assume the environment does not allow you to store 64-bit integers (signed or unsigned).

 

Example 1:

Input: x = 123
Output: 321
Example 2:

Input: x = -123
Output: -321
Example 3:

Input: x = 120
Output: 21
"""
def reverse(x):
    a = []
    z = 0
    negative = False
    if x < 0:
        negative = True
        x = x * (-1)
    while x > 0:
        a.append(x%10)
        x = x // 10
    for i in a:
        z = z*10 + i
    if negative == True:
        z = z * (-1)
    if z > (2**31-1) or z < (-2**31):
        z = 0
    print(z)
    return z

reverse(1534236469)
