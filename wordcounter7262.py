s=input("enter words")
w=s.split()
w_c={}
for i in w:
    if i in w_c:
        w_c[i]+=1
    else:
        w_c[i]=1
print(w_c)
