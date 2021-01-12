from tkinter import*

def value_0():
    t1.delete("1.0",END)
    t2.insert(END,"0")
    t1.insert(END,t2.get("1.0",END))

def value_1():
    t1.delete("1.0",END)
    t2.insert(END,"1")
    t1.insert(END,t2.get("1.0",END))

def value_2():
    t1.delete("1.0",END)
    t2.insert(END,"2")
    t1.insert(END,t2.get("1.0",END))

def value_3():
    t1.delete("1.0",END)
    t2.insert(END,"3")
    t1.insert(END,t2.get("1.0",END))

def value_4():
    t1.delete("1.0",END)
    t2.insert(END,"4")
    t1.insert(END,t2.get("1.0",END))

def value_5():
    t1.delete("1.0",END)
    t2.insert(END,"5")
    t1.insert(END,t2.get("1.0",END))

def value_6():
    t1.delete("1.0",END)
    t2.insert(END,"6")
    t1.insert(END,t2.get("1.0",END))

def value_7():
    t1.delete("1.0",END)
    t2.insert(END,"7")
    t1.insert(END,t2.get("1.0",END))

def value_8():
    t1.delete("1.0",END)
    t2.insert(END,"8")
    t1.insert(END,t2.get("1.0",END))

def value_9():
    t1.delete("1.0",END)
    t2.insert(END,"9")
    t1.insert(END,t2.get("1.0",END))

def value_add():
    a = t2.get("1.0",END)
    c = 0
    for i in range(len(a)):
        if a[i] == "-":
            c = c+1
    if len(a) == 0 or '%' in a or a == "\n" or '+' in a  or '/' in a or '*' in a or "-" in a:
        if a[0] != "-" and c == 1:
            t1.insert(END,"")
        elif a[0] == "-" and c == 2:
            t1.insert(END,"")
        elif a[0] == "-" and c == 1:
            if len(a) == 0 or '%' in a or a == "\n" or '+' in a  or '/' in a or '*' in a:
                t1.insert(END,"")
            elif a[1] =="\n":
                t1.insert(END,"")
            else:
                t1.delete("1.0",END)
                t2.insert(END,"+")
                t1.insert(END,t2.get("1.0",END))
        else:
            pass
    else:
        t1.delete("1.0",END)
        t2.insert(END,"+")
        t1.insert(END,t2.get("1.0",END))

def value_sub():
    a = t2.get("1.0",END)
    c = 0
    for i in range(len(a)):
        if a[i] == "-":
            c = c+1
    if a[0] == "\n" and c == 0:
        if '+' in a  or '/' in a  or '%' in a  or '*' in a:
            t1.insert(END,"")
        else:    
            t1.delete("1.0",END)
            t2.insert(END,"-")
            t1.insert(END,t2.get("1.0",END))
    elif a[0] == "-" and c == 1:
        if '+' in a  or '/' in a  or '%' in a  or '*' in a:
            t1.insert(END,"")
        else:  
            t1.delete("1.0",END)
            t2.insert(END,"-")
            t1.insert(END,t2.get("1.0",END))
    elif a[0] == "-" and c == 2:
        t1.insert(END,"")
    elif a[0] != "-" and c == 1:
        t1.insert(END,"")
    else:
        t1.delete("1.0",END)
        t2.insert(END,"-")
        t1.insert(END,t2.get("1.0",END))
        

def value_mul():
    a = t2.get("1.0",END)
    c = 0
    for i in range(len(a)):
        if a[i] == "-":
            c = c+1
    if len(a) == 0 or '%' in a or a == "\n" or '+' in a  or '/' in a or '*' in a or "-" in a:
        if a[0] != "-" and c == 1:
            t1.insert(END,"")
        elif a[0] == "-" and c == 2:
            t1.insert(END,"")
        elif a[0] == "-" and c == 1:
            if len(a) == 0 or '%' in a or a == "\n" or '+' in a  or '/' in a or '*' in a:
                t1.insert(END,"")
            elif a[1] =="\n":
                t1.insert(END,"")
            else:
                t1.delete("1.0",END)
                t2.insert(END,"*")
                t1.insert(END,t2.get("1.0",END))
        else:
            pass
    else:
        t1.delete("1.0",END)
        t2.insert(END,"*")
        t1.insert(END,t2.get("1.0",END))

def value_div():
    a = t2.get("1.0",END)
    c = 0
    for i in range(len(a)):
        if a[i] == "-":
            c = c+1
    if len(a) == 0 or '%' in a or a == "\n" or '+' in a  or '/' in a or '*' in a or "-" in a:
        if a[0] != "-" and c == 1:
            t1.insert(END,"")
        elif a[0] == "-" and c == 2:
            t1.insert(END,"")
        elif a[0] == "-" and c == 1:
            if len(a) == 0 or '%' in a or a == "\n" or '+' in a  or '/' in a or '*' in a:
                t1.insert(END,"")
            elif a[1] =="\n":
                t1.insert(END,"")
            else:
                t1.delete("1.0",END)
                t2.insert(END,"/")
                t1.insert(END,t2.get("1.0",END))
        else:
            pass
    else:
        t1.delete("1.0",END)
        t2.insert(END,"/")
        t1.insert(END,t2.get("1.0",END))

def value_per():
    a = t2.get("1.0",END)
    c = 0
    for i in range(len(a)):
        if a[i] == "-":
            c = c+1
    if len(a) == 0 or '%' in a or a == "\n" or '+' in a  or '/' in a or '*' in a or "-" in a:
        if a[0] != "-" and c == 1:
            t1.insert(END,"")
        elif a[0] == "-" and c == 2:
            t1.insert(END,"")
        elif a[0] == "-" and c == 1:
            if len(a) == 0 or '%' in a or a == "\n" or '+' in a  or '/' in a or '*' in a:
                t1.insert(END,"")
            elif a[1] =="\n":
                t1.insert(END,"")
            else:
                t1.delete("1.0",END)
                t2.insert(END,"%")
                t1.insert(END,t2.get("1.0",END))
        else:
            pass
    else:
        t1.delete("1.0",END)
        t2.insert(END,"%")
        t1.insert(END,t2.get("1.0",END))

def value_eq():
    f = t1.get("1.0",END)
    a=list(f)
    a.pop(-1)
    a.pop(-1)
    oppsub = ""
    if a[0] == "-":
        oppsub = "-"
        a.pop(0)
    else:
        pass
    if len(a)>0:
        b=""
        d=""
        for i in range(len(a)):
        
            if a[i] == '+' or a[i] == '-' or a[i] == '*' or a[i] == '/' or a[i] == '%':
                break
            else:
                b = b+a[i]

        for i in range(0,len(b)):
            a.pop(0)

        c = int(b)  

        try:
            operator = a[0]
            a.pop(0)
        except Exception as e:
            t2.delete("1.0",END) 
            t1.delete("1.0",END)
            

        if len(a) >0:
            for i in range(len(a)):
            
                if a[i] == '+' or a[i] == '-' or a[i] == '*' or a[i] == '/' or a[i] == '%':
                    break
                else:
                    d = d+a[i]

            for i in range(0,len(d)):
                a.pop(0)
        
            e = int(d)
        else:
            t2.delete("1.0",END) 
            t1.delete("1.0",END)
        
        g = 0

        if oppsub == "-":
            g = 2*c
            c = c-g
        else:
            g = 0

        if len(d)>0:
            if operator == '+':
                result = c+e
                t2.delete("1.0",END) 
                t1.delete("1.0",END)
                t1.insert(END,result)
            elif operator =='-':
                result = c-e
                t2.delete("1.0",END) 
                t1.delete("1.0",END)
                t1.insert(END,result)
            if operator == '*':
                result = c*e
                t2.delete("1.0",END) 
                t1.delete("1.0",END)
                t1.insert(END,result)
            if operator == '/':
                try:  
                    result = c/e 
                    t2.delete("1.0",END) 
                    t1.delete("1.0",END)
                    t1.insert(END,result)
                except Exception as e:
                    t2.delete("1.0",END) 
                    t1.delete("1.0",END)
            if operator == '%':
                result = (c*e)/100
                t2.delete("1.0",END)
                t1.delete("1.0",END)
                t1.insert(END,result)                   
            else:
                pass     
        else:
            pass
    else:
        t2.delete("1.0",END) 
        t1.delete("1.0",END)
    t2.delete("1.0",END)
def value_ac():
    t1.delete("1.0",END)
    t2.delete("1.0",END)


window = Tk()

window.wm_title("Calculator")

t2 = Text(window)
t1=Text(window,height=1,width=24)
t1.grid(row=0,column=0,columnspan=10)

b1=Button(window,text="1",height=2,width=4,command = value_1)
b1.grid(row=5,column=0,columnspan=2)

b2=Button(window,text="2",height=2,width=4,command = value_2)
b2.grid(row=5,column=2,columnspan=2)

b3=Button(window,text="3",height=2,width=4,command = value_3)
b3.grid(row=5,column=4,columnspan=2)

b4=Button(window,text="4",height=2,width=4,command = value_4)
b4.grid(row=3,column=0,columnspan=2)

b5=Button(window,text="5",height=2,width=4,command = value_5)
b5.grid(row=3,column=2,columnspan=2)

b6=Button(window,text="6",height=2,width=4,command = value_6)
b6.grid(row=3,column=4,columnspan=2)

b7=Button(window,text="7",height=2,width=4,command = value_7)
b7.grid(row=1,column=0,columnspan=2)

b8=Button(window,text="8",height=2,width=4,command = value_8)
b8.grid(row=1,column=2,columnspan=2)

b9=Button(window,text="9",height=2,width=4,command = value_9)
b9.grid(row=1,column=4,columnspan=2)

b0=Button(window,text="0",height=2,width=10,command = value_0)
b0.grid(row=7,column=0,columnspan=4)

badd=Button(window,text="+",height=2,width=4,command = value_add)
badd.grid(row=5,column=6,columnspan=2)

bsub=Button(window,text="-",height=2,width=4,command = value_sub)
bsub.grid(row=5,column=8,columnspan=2)

bmul=Button(window,text="*",height=2,width=4,command = value_mul)
bmul.grid(row=3,column=6,columnspan=2)

bdiv=Button(window,text="/",height=2,width=4,command = value_div)
bdiv.grid(row=3,column=8,columnspan=2)

bper=Button(window,text="%",height=2,width=4,command = value_per)
bper.grid(row=1,column=6,columnspan=2)

beq=Button(window,text="=",height=2,width=4,command = value_eq)
beq.grid(row=1,column=8,columnspan=2)

bac=Button(window,text="AC",height=2,width=4,command = value_ac)
bac.grid(row=7,column=4,columnspan=2)

bcl=Button(window,text="Close",height=2,width=10,command = window.destroy)
bcl.grid(row=7,column=6,columnspan=4)

window.mainloop()