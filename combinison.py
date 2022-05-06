def combinison(n,p):
    return fact(n)/(fact(p)*fact(n-p))
"""
def fact(n):
    f=1
    for i n range(1,n+1):
        f=f*i
    return f

"""
def fact(n):
    if n==0:
        return 1
    else:
        return  n*fact(n-1)



n=int(input('donner n:'))
p=int(input('donner p:'))
while not((0<=p)and(p<=n)):
    p=int(input('donner p:'))

print(combinison(n,p))