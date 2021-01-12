a =list(input("enter: "))
b=""
d=""
for i in range(len(a)):
   
    if a[i] == '+' or a[i] == '-' or a[i] == '*' or a[i] == '/' or a[i] == '%':
        break
    else:
        b=b+a[i]

for i in range(0,len(b)):
    a.pop(0)

c=int(b)    

try:
    operator = a[0]
    a.pop(0)
except Exception as e:
    print("Enter atleast one operator")

if len(a) >0:
    for i in range(len(a)):
    
        if a[i] == '+' or a[i] == '-' or a[i] == '*' or a[i] == '/' or a[i] == '%':
            break
        else:
            d=d+a[i]

    for i in range(0,len(d)):
        a.pop(0)
   
    e=int(d)
else:
    print("Enter numbers after the operator")    

if len(d)>0:
    if operator == '+':
        print(c+e)
    elif operator =='-':
        print(c-e)
    if operator == '*':
        print(c*e)
    if operator == '/':
        print(c/e)
    if operator == '%':
        print((c*e)/100)                    
    else:
        pass     
else:
    pass