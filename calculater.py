from tkinter import *
import math
root = Tk()
root.title('calculater')
root.geometry('450x400')
root.resizable(0,0)
ee=Entry(root,bd=10,width='30',font='Arial 27',bg='silver')
ee.pack()
def cu():
    try:
        
        n=ee.get()
        
        if '^' not in n and '√' not in n and 'x' not in n and '%' not in n:
            re = eval(n)
            ee.delete(0,'end')
            ee.insert(32, re)
        elif '^' in n :
            n=n.replace('^','**')
            re = eval(n)
            ee.delete(0,'end')
            ee.insert(32, re)
        elif '√' in n:
            m=n.index('√')
            b=str(n[m+1:])
            b+=')'
            n=n.replace( n[m+1:] ,b)
            n = n.replace( '√' ,'math.sqrt( ')
            re = eval(n)
            ee.delete(0,'end')
            ee.insert(32, re)
        elif 'x' in n:
            
            n=n.replace('x','*')
            re = eval(n)
            ee.delete(0,'end')
            ee.insert(32, re)
        elif '%' in n:
            
            n=n.replace('%','/100')
            re = eval(n)
            ee.delete(0,'end')
            ee.insert(32, re)
    except(SyntaxError,ZeroDivisionError,Exception)as e:
        ee.delete(0,'end')
        ee.insert(32, 'Error')
def cw():
    o=ee.get()
    o=list(o)
    del o[-1]
    o=''.join(o)
    ee.delete(0,'end')
    ee.insert(32, o)
def cns():
    ee.insert(32, '%')
def cq1():
    ee.insert(32, '(')
def cq2():
    ee.insert(32, ')')
def cf():
    ee.insert(32, '.')
def ct():
    ee.insert(32, '^2')
def ctt():
    ee.insert(32, '^')
def cj():
    ee.insert(32, '√')    
def cn():
    ee.insert(32, '-')
def cd():
    ee.insert(32, 'x')
def cq():
    ee.insert(32, '/')        
def cc():
    ee.delete(0,'end')
def cz():
    ee.insert(32, '+')
def c1():
    ee.insert(32, 1)
def c2():
    ee.insert(32, 2)
def c3():
    ee.insert(32, 3)
def c4():
    ee.insert(32, 4)
def c5():
    ee.insert(32, 5)
def c6():
    ee.insert(32, 6)
def c7():
    ee.insert(32, 7)
def c8():
    ee.insert(32, 8)
def c9():
    ee.insert(32, 9)
def c0():
    ee.insert(32, 0)


btn1=Button(root,text='7',bd=10,bg='silver',font='Arial 19 bold',padx=10,pady=5,command=c7)
btn1.place(x=10,y=60)
btn2=Button(root,text='8',bd=10,bg='silver',font='Arial 19 bold',padx=10,pady=5,command=c8)
btn2.place(x=80,y=60)

btn3=Button(root,text='9',bd=10,bg='silver',font='Arial 19 bold',padx=10,pady=5,command=c9)
btn3.place(x=150,y=60)

btn4=Button(root,text='4',bd=10,bg='silver',font='Arial 19 bold',padx=10,pady=5,command=c4)
btn4.place(x=10,y=140)

btn5=Button(root,text='1',bd=10,bg='silver',font='Arial 19 bold',padx=10,pady=5,command=c1)
btn5.place(x=10,y=220)

btn6=Button(root,text='5',bd=10,bg='silver',font='Arial 19 bold',padx=10,pady=5,command=c5)
btn6.place(x=80,y=140)
btn7=Button(root,text='6',bd=10,bg='silver',font='Arial 19 bold',padx=10,pady=5,command=c6)
btn7.place(x=150,y=140)
btn8=Button(root,text='2',bd=10,bg='silver',font='Arial 19 bold',padx=10,pady=5,command=c2)
btn8.place(x=80,y=220)
btn9=Button(root,text='3',bd=10,bg='silver',font='Arial 19 bold',padx=10,pady=5,command=c3)
btn9.place(x=150,y=220)

btn10=Button(root,text='+',bd=10,bg='skyblue',font='Arial 19 bold',padx=10,pady=5,command=cz)
btn10.place(x=220,y=60)
btn11=Button(root,text='=',bd=10,bg='yellow',font='Arial 19 bold',padx=7,pady=5,command=cu)
btn11.place(x=150,y=300)
btn12=Button(root,text='0',bd=10,bg='silver',font='Arial 19 bold',padx=10,pady=5,command=c0)
btn12.place(x=10,y=300)
btn13=Button(root,text='c',bd=10,bg='red',font='Arial 19 bold',padx=7,pady=5,command=cc)
btn13.place(x=80,y=300)
btn14=Button(root,text='-',bd=10,bg='skyblue',font='Arial 19 bold',padx=13,pady=5,command=cn)
btn14.place(x=220,y=140)
btn15=Button(root,text='x^2',bd=10,bg='skyblue',font='Arial 12 bold',padx=8,pady=15,command=ct)
btn15.place(x=220,y=220)
btn16=Button(root,text='.',bd=10,bg='skyblue',font='Arial 12 bold',padx=19,pady=15,command=cf)
btn16.place(x=220,y=300)
btn10=Button(root,text='x',bd=10,bg='skyblue',font='Arial 19 bold',padx=12,pady=5,command=cd)
btn10.place(x=295,y=60)
btn10=Button(root,text='/',bd=10,bg='skyblue',font='Arial 19 bold',padx=16,pady=5,command=cq)
btn10.place(x=295,y=140)
btn10=Button(root,text='x^y',bd=10,bg='skyblue',font='Arial 12 bold',padx=10,pady=15,command=ctt)
btn10.place(x=295,y=220)
btn10=Button(root,text='√x',bd=10,bg='skyblue',font='Arial 12 bold',padx=15,pady=15,command=cj)
btn10.place(x=295,y=300)
btn10=Button(root,text='(',bd=10,bg='skyblue',font='Arial 19 bold',padx=12,pady=5,command=cq1)
btn10.place(x=370,y=60)
btn10=Button(root,text=')',bd=10,bg='skyblue',font='Arial 19 bold',padx=12,pady=5,command=cq2)
btn10.place(x=370,y=140)
btn10=Button(root,text='%',bd=10,bg='skyblue',font='Arial 19 bold',padx=7,pady=5,command=cns)
btn10.place(x=370,y=220)
btn10=Button(root,text='->',bd=10,bg='red',font='Arial 19 bold',padx=5,pady=5,command=cw)
btn10.place(x=370,y=300)

root.mainloop()
