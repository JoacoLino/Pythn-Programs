"""
Given two binary strings a and b, return their sum as a binary string.

 

Example 1:

Input: a = "11", b = "1"
Output: "100"
Example 2:

Input: a = "1010", b = "1011"
Output: "10101"
"""
def addBinary(a, b):
    answer_str_d = ""
    cont_a = 0
    cont_b = 0
    a_int = 0
    b_int = 0
    answer = 0
    answer_str = ""
    for i in a:
        a_int = a_int + int(i)*(2**(len(a)-cont_a-1))
        cont_a += 1
    for x in b:
        b_int = b_int + int(x)*(2**(len(b)-cont_b-1))
        cont_b += 1
    answer = a_int + b_int
    if answer != 0:
        while answer >= 1:
            answer_str = answer_str + " " + str(answer%2)
            answer = answer // 2
        a = answer_str.split()
        a.reverse()
        for i in a:
            answer_str_d = answer_str_d + i
    else:
        answer_str_d = "0"
    print(answer_str_d)
    return answer_str_d


addBinary("0","0")
