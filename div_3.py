def div_3(x):
    R=str(x)
    s=0
    for i in range(0,len(R)):
        s=s+int(R[i])
    if s%3==0:
        return True
    else:
        return False

x=int(input('donner x:'))
while not(x>0):
    x=int(input('donner x:'))
print(div_3(x))