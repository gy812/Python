'''
ch='anis_elbahi'
def inverse(ch):
    S=''
    for i in range(len(ch),-1):
        S=S+ch[i]
    return S
S=inverse(ch)
print(S)
'''
'''
def miror(seq): 
   rseq = "" 
   for char in seq:
       rseq = char + rseq 
   return rseq

rseq=miror("abc")
print(rseq)
'''
ch='anis_elbahi'
for i in range(0,len(ch),-1) :
	print(i)