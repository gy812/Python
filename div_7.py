def div_7(n):
    while (n<=14):
        n=abs((n//10)-2*(n%10))
    return n in {0,7}
n=int(input('donner n:'))
print(div_7(n))