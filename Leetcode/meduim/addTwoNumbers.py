def isPowerOfTwo(n):
    es = False
    while n >= 2:
        if n == 2:
            es = True
        n = n / 2
    print(es)
    return es

isPowerOfTwo(32)
        