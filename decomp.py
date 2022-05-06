def decomp(x):
    R=str(x)+"="
    i=2
    while x!=1:
        if x%i==0:
            R=R+str(i)+"*"
            x=x//i
        else:
            i=i+1
    return R[:len(R)-1]
print(decomp(100))