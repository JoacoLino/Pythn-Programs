"""
Given an integer n, return true if it is a power of two. Otherwise, return false.

An integer n is a power of two, if there exists an integer x such that n == 2x.

 

Example 1:

Input: n = 1
Output: true
Explanation: 20 = 1
Example 2:

Input: n = 16
Output: true
Explanation: 24 = 16
Example 3:

Input: n = 3
Output: false
"""
def isPowerOfTwo(n):
    es = False
    while n >= 2 or n == 1:
        if n == 2:
            es = True
        elif n == 1:
            es== True
        n = n / 2
    print(es)
    return es

isPowerOfTwo(32)