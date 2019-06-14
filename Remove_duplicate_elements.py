a=[1,1,2,3,4,4,5]
def removeduplicateelements(a):
    b=[]
    a.sort()
    for i in range(len(a)-1):
        if (a[i] != a[i+1]):
            b.append(a[i])
    b.append(a[len(a)-1])
    return(b)
print(removeduplicateelements(a))
