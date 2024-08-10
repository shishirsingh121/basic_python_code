#number  is greater and smaller
a=int(input("enter the first number: "))
b=int(input("enter the second number: "))
if a>b:
    print("a is greater")
else:
    print("b is greater")
    
#2.accept the gender from user and print the respective greeting message
gender=input("please,enter your grnder f for female and m for male")
if (gender=='m'):
    print("hello sir")
else:
    print("hello, mam")
    
#3.for loops
n=int(input("enter the number"))
for i in range(1,n):
    print(i)
    
    
a=int(input("enter the number: "))
for i in range(1,n+1,i):
    print(i)
    
    
a=int(input("enter the number: "))
sum=1
for i in range(1,a+1):
    sum=sum*i;
print(sum)

#factor of given number 
a=int(input("enter the number: "))
for i in range(1,a+1):
     if a%i==0:
        print(i)
        
#storng number 
a=int(input("enter the number: "))
sum=0
for i in range(1,a):
     if a%i==0:
        sum=sum+i
if sum==a:
    print("given number is strong")
else:
    print("sorry it`s not a storng number")
    
#prime number or not
n=int(input("enter the number: "))
count=0
for i in range(1,n+1):
    if n%i==0:
        count=count+1
if count ==2:
    print("the given number is prime")
else :
    print("the given number is composite")

n=int(input('Enter the number:'))
for i in range(n):
    print("*" * i)
    
#right angle *
n=int(input('Enter the number:'))
for i in range(n+1):
    print("*" * i)
