# 1.
a={1:10,2:20,3:30,9:22}
b={4:20,8:30}
c=a
c.update(b)
print(c)
print(a)


# 2.sum
a={1:10,2:20,3:30,9:22}

sum=0
for i in a.values():
    sum=sum+i
print(sum)    

# 3.count frequency
a=[1,2,2,3,3,3,2,1,5,6,7,4]
dict={}
for i in a:
    if i in dict.keys():
        dict[i]=dict[i]+i
    else:
        dict[i]=1
print(dict)        

# 4.combine two dictionary
a={1:10,2:20,3:30,9:22}
b={9:20,8:30}
for i in b.keys():
    if i in a.keys():
        a[i]=a[i]+b[i]
    else:
        a[i] =b[i]   
print(a)        