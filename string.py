# 1.reverse order
a="shisir singh"
for i in range(len(a)-1,-1,-1):
    print(a[i],end="")

# 2.lower letter comes first
a="Hello I am HerrE"
b=" "
for i in a:
    if i.islower():
        b=b+i
for i in a:
    if i.isupper():
        b=b+i   
print(b)  

# 3.pallindrome is not
a="naman"
c=''
for i in range(len(a)-1,-1,-1):
    c=c+a[i]

if a==c:
    print('the given string is pallindrome')
else:
    print('its is not')         
    