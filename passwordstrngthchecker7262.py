def check(p):
    if len(p)<8:
        return "weak"
    u=l=d=sp=0
    for i in p:
        if 'A'<=i<='Z':
            u=True
        elif 'a'<=i<='z':
            l=True
        elif '0'<=i<='9':
            d=True
        elif not ('A'<=i<='Z' or 'a'<=i<='z' or '0'<=i<='9'):
            sp=True
    if u and l and d and sp:
        return "strong"
    return "weak"
print(check(input("enter password")))