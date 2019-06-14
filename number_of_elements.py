a=[1,2,3,4,4,5]
g={}
count=0
for i in a:
    if i not in g:
        for j in a:
            if i==j:
                count+=1
        g[i]=count
        count=0
print(g)
                
            
