# 1.how can you take input in list
l=[]
count=int(input("how many nu,ber you want"))
for i in range(count):
    z=int(input("plese enter the nu,ber"))
    l.append(z)
print(l)    

# 2.find the greatest element in list
a=[2,96,69,77,145,20]
max=0
max2=0
index=0
for i in range(len(a)):
   if a[i]>max:
         max2=max
         max=a[i]
   elif a[i]>max2:
       max2=a[i]     
        
print(max , max2) 

a=[1,2,3,22,44,66,4,55,]
print(a.sort())