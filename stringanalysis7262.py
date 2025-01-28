def stringsanalysis():
    st=input("enter string::")
    vow={'a','e','i','o','u'}
    v=c=d=0
    res=""
    for i in st: 
        res=i+res
        if i.isalpha():
            if i in vow:
                v+=1
            else :
                c+=1
        elif i.isdigit():
            d+=1
    sp=len(st)-c-v-d
    print("vowels: ",v)
    print("consonants: ",c)
    print("digits: ",d)
    print("reverse: ",res)
    print("special char: ",sp)
stringsanalysis()
