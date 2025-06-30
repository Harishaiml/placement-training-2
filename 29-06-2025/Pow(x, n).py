def myPow(x, n):
    if n == 0: return 1
    if n < 0: return 1 / myPow(x, -n)
    if n % 2:
        return x * myPow(x, n - 1)
    else:
        half = myPow(x, n // 2)
        return half * half
