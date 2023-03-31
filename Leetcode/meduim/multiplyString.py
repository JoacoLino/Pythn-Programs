def multiply(num1, num2):
    n1 = 0
    n2 = 0
    l = []
    a = ""
    for i in num1:
        x = digito_a_numero(i)
        n1 = n1 *10 + x
    for k in num2:
        y = digito_a_numero(k)
        n2 = n2*10 + y
    m = n1 * n2
    while m > 0:
        l.append(m%10)
        m = m // 10
    l.reverse()
    for w in l:
        j  = numero_a_digito(w)
        a = a + j
    print(a)
    return a




def digito_a_numero(n):
    if n == "0":
        n = 0
    if n == "1":
        n = 1
    if n == "2":
        n = 2
    if n == "3":
        n = 3
    if n == "4":
        n = 4
    if n == "5":
        n = 5
    if n == "6":
        n = 6
    if n == "7":
        n = 7
    if n == "8":
        n = 8
    if n == "9":
        n = 9
    return n

def numero_a_digito(n):
    if n == 0:
        n = "0"
    if n == 1:
        n = "1"
    if n == 2:
        n = "2"
    if n == 3:
        n = "3"
    if n == 4:
        n = "4"
    if n == 5:
        n = "5"
    if n == 6:
        n = "6"
    if n == 7:
        n = "7"
    if n == 8:
        n = "8"
    if n == 9:
        n = "9"
    return n


multiply("123","456")