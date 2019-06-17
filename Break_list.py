a = [1, 2, 3, 4, 5, 6, 7, 8,9] 
b=[]
d=4
c=len(a)//d
if int(c)*d ==len(a):
    n=c
else:
    n=c+1
for i in range(n):
    b.append(a[i*d:(i+1)*d])
print(b)
    
