from tkinter import *
from tkinter import messagebox
l=[]
def home():
    try:
        T.destroy()
    except:
        pass
    global H
    H=Tk()
    H.geometry("880x500")
    H.title("welcome back")
    l1=Label(H,bg="purple2",fg="cyan",width="35",text="the traditional way to manage daily taks...",font=("times new roman",15,"bold"))
    l1.place(x=10,y=0)
    l2=Label(H,bg="purple2",fg="cyan",width="35",text="lets starts with ....python",font=("times new roman",15,"bold"))
    l2.place(x=440,y=0)
    f1=Frame(H,bg="skyblue", width="426",height="600")
    f1.place(x=10,y=30)
    #=======tabs of frame1 =========
    f11=Frame(f1,bg="red2", width="140",height="140")
    f11.place(x=50,y=80)
    l1=Label(f11,text="task-1",font=("times new roman",15,"bold"))
    l1.place(x=40,y=2)

    f12=Frame(f1,bg="cyan", width="140",height="140")
    f12.place(x=230,y=80)
    l1=Label(f12,text="task-2",font=("times new roman",15,"bold"))
    l1.place(x=40,y=2)

    f13=Frame(f1,bg="green2", width="140",height="140")
    f13.place(x=50,y=300)
    l1=Label(f13,text="task-3",font=("times new roman",15,"bold"))
    l1.place(x=40,y=2)

    f12=Frame(f1,bg="yellow2", width="140",height="140")
    f12.place(x=230,y=300)
    l1=Label(f12,text="task-4",font=("times new roman",15,"bold"))
    l1.place(x=40,y=2)
    #============================== modern model ========================
    f2=Frame(H,bg="cyan", width="427",height="600")
    f2.place(x=440,y=30)
    b1=Button(f2,text="create your to do list...",bg="green2",command=task,fg="white",width="30",height="10",font=("times new roman",15,"bold"))
    b1.place(x=25,y=60)

    
def task():
    global task,T
    try:
        sh.destroy()
    except:
        pass
    try:
        H.destroy()
    except:
        pass
    try:
        AD.destroy()
    except:
        pass
    T=Tk()
    T.geometry("650x600")
    T.title("your task manager")
    f2=Frame(T,bg="cyan", width="650",height="600")
    f2.place(x=10,y=10)
    l1=Label(f2,text="hii i am your daily task manager..",font=("times new roman",15,"bold"))
    l1.place(x=110,y=20)

    btn1=Button(f2,text="click here",command=add,font=("times new roman",12,"bold"),bg="green2",fg="white")
    btn1.place(x=250,y=70)
    l2=Label(f2,text="1. Add your task...",font=("times new roman",15,"bold"))
    l2.place(x=20,y=70)
    #=============================
    l3=Label(f2,text="2.  Remove your task...",font=("times new roman",15,"bold"))
    l3.place(x=20,y=120)
    btn1=Button(f2,text="click here",command=remove,font=("times new roman",12,"bold"),bg="green2",fg="white")
    btn1.place(x=250,y=120)
    #=============================
    l4=Label(f2,text="3. View tasks....",font=("times new roman",15,"bold"))
    l4.place(x=20,y=170)
    btn1=Button(f2,text="click here",command=view,font=("times new roman",12,"bold"),bg="green2",fg="white")
    btn1.place(x=250,y=170)
    #==============================
    l5=Label(f2,text="4. Exit....!",font=("times new roman",15,"bold"))
    l5.place(x=20,y=220)
    btn1=Button(f2,text="click here",command=home,font=("times new roman",12,"bold"),bg="green2",fg="white")
    btn1.place(x=250,y=220)
    #==============================


def add():
    global AD,scr,l
    try:
        T.destroy()
    except:
        pass
    AD=Tk()
    AD.geometry("650x600")
    AD.title("your task manager")
    f2=Frame(AD,bg="cyan", width="650",height="600")
    f2.place(x=10,y=10)
    l1=Label(f2,text="hii i am your daily task manager..",font=("times new roman",15,"bold"))
    l1.place(x=110,y=20)


    l2=Label(f2,text="1. Add your task...",font=("times new roman",15,"bold"))
    l2.place(x=20,y=70)
    e1=Entry(f2,text="enter your tasks here",font=("times new roman",15,"bold"))
    e1.place(x=190,y=70)
    def validation():
        global l
        if e1.get()!="" :
            if e1.get() not in  l:
                l.append(e1.get())
                l.append(",")
                messagebox.showinfo('Congratulations....!', 'your task is sucessefully added')
            else:
                messagebox.showerror('Python Error', 'this task already added')
        else:
            messagebox.showerror('Python Error', "your task can't be none")
            pass
        print(l)
        
    btn1=Button(f2,text="Add..!",command=validation,font=("times new roman",15,"bold"),width="9",bg="green2",fg="white")
    btn1.place(x=250,y=130)
    btn2=Button(f2,text="Back",command=task,font=("times new roman",15,"bold"),width="9",bg="red2",fg="white")
    btn2.place(x=100,y=130)

def remove():
    global remove
    try:
        T.destroy()
    except:
        pass
    RM=Tk()
    RM.geometry("650x600")
    RM.title("your task manager")
    f2=Frame(RM,bg="cyan", width="650",height="600")
    f2.place(x=10,y=10)
    l1=Label(f2,text="hii i am your daily task manager..",font=("times new roman",15,"bold"))
    l1.place(x=110,y=20)
    l2=Label(f2,text="1. Remove your task...",font=("times new roman",15,"bold"))
    l2.place(x=20,y=70)
    e2=Entry(f2,font=("times new roman",15,"bold"))
    e2.place(x=190,y=70)
    def validation():
        k=e2.get()
        if k != "" :
            if  k in l:
                l.remove(k)
                messagebox.showinfo('Congratulations....!', 'your task is sucessefully removed')
            else:
                messagebox.showerror('Python Error', 'this task is not in your list')
        else:
            messagebox.showerror('Python Error', "your task can't be none")
            pass
        print(l)
        
    btn1=Button(f2,text="Remove",command=validation,font=("times new roman",15,"bold"),width="9",bg="green2",fg="white")
    btn1.place(x=250,y=130)
    btn2=Button(f2,text="Back",command=task,font=("times new roman",15,"bold"),width="9",bg="red2",fg="white")
    btn2.place(x=100,y=130)

def view():
    global view,sh
    try:
        T.destroy()
    except:
        pass
    sh=Tk()
    sh.geometry("650x600")
    sh.title("your task manager")
    f3=Frame(sh,bg="cyan", width="650",height="600")
    f3.place(x=10,y=10)
    l1=Label(f3,text="hii i am your daily task manager..",font=("times new roman",15,"bold"))
    l1.place(x=110,y=20)
    l2=Label(f3,text="your pending tasks",font=("times new roman",15,"bold"))
    l2.place(x=100,y=100)
    kk=Message(text=l,font=("times new roman",15,"bold"),width="400",bg="yellow")
    kk.place(x=40,y=150)
    btn1=Button(f3,text="Refresh",font=("times new roman",15,"bold"),width="9",bg="green2",fg="white")
    btn1.place(x=250,y=300)
    btn2=Button(f3,text="Back",command=task,font=("times new roman",15,"bold"),width="9",bg="red2",fg="white")
    btn2.place(x=100,y=300)

home()
