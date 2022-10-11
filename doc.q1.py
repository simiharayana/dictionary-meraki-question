a="the queck dog"
b=a.split()
print(b)
i=0
c="dog"
d="cat"
s=" "
while i<len(b):
    if b[i]==c:
        s+=d+" "
    else:
        s+=b[i]+" "
    i+=1
print(s)