#-*- coding: utf-8 -*-
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
from Crypto.RSA import *
from Crypto.hash import *
def RSA_Encrypt():
    entry_c.delete(0.0,END)
    e = int(var_e.get().split()[0])
    n = int(entry_n.get(0.0,END).split()[0])
    m = int(entry_m.get(0.0,END).split()[0])
    c = fastExpMod(m,e,n)
    entry_c.insert(1.0,str(c))
def RSA_Clear():
    entry_e.delete(0,END)
    entry_n.delete(0.0,END)
    entry_m.delete(0.0,END)
    entry_c.delete(0.0,END)

def RSA_Decrypt():
    entry_m.delete(0.0,END)
    e = int(var_e.get().split()[0])
    n = int(entry_n.get(0.0, END).split()[0])
    c = int(entry_c.get(0.0, END).split()[0])
    d = RSA_Get_D(n,e)
    m = fastExpMod(c,d,n)
    entry_m.insert(1.0,str(m))

def hash_encrypt():
    entry_res.delete(0.0, END)
    t=entry_text.get(0.0, END).split()[0]
    text=myhash(t)
    text1=myshaone(t)
    entry_res.insert(1.0, str(text))
    entry_res1.insert(1.0,str(text1))

def hash_clear():
    entry_text.delete(0.0, END)
    entry_res.delete(0.0, END)
    entry_res1.delete(0.0, END)
#-------Main-----------------
window = Tk()
window.title("Crypto Programme")
window.geometry('640x540')
window.resizable(0,0)
#---------------------------

#-------标签布局--------------
Menu = ttk.Notebook(window)
tab1 = ttk.Frame(Menu)
Menu.add(tab1,text='   RSA   ')
tab2 = ttk.Frame(Menu)
Menu.add(tab2,text='   DES   ')
tab3 = ttk.Frame(Menu)
Menu.add(tab3,text='  流密码  ')
tab4 = ttk.Frame(Menu)
Menu.add(tab4,text='仿射加密')
tab5 = ttk.Frame(Menu)
Menu.add(tab5,text='D-H认证')
tab6 = ttk.Frame(Menu)
Menu.add(tab6,text='散列函数')
Menu.pack(expand=1,fill="both")
#------------------------------

#--------RSA布局-----------------
UI_RSA = ttk.LabelFrame(tab1,text='RSA')
UI_RSA.grid(column=0,row=0,padx=8,pady=4)
ttk.Label(UI_RSA,text="公钥(E)").grid(column=0,row=0,sticky='NW')
var_e = StringVar()
entry_e = ttk.Entry(UI_RSA,width=30,textvariable=var_e)
entry_e.grid(column=1,row=0,padx=2,sticky='NW')

ttk.Label(UI_RSA,text="模数(N)").grid(column=0,row=1,pady=40,sticky='NW')
entry_n = Text(UI_RSA,height=7,width=60,highlightcolor='blue')
entry_n.grid(column=1,row=1,padx=2,pady=5,sticky='NW')

ttk.Label(UI_RSA,text="明文(M)").grid(column=0,row=2,pady=40,sticky='NW')
entry_m = Text(UI_RSA,height=7,width=60,highlightcolor='blue')
entry_m.grid(column=1,row=2,padx=2,pady=5,sticky='NW')

ttk.Label(UI_RSA,text="密文(C)").grid(column=0,row=3,pady=40,sticky='NW')
entry_c = Text(UI_RSA,height=7,width=60,highlightcolor='blue')
entry_c.grid(column=1,row=3,padx=2,pady=5,sticky='NW')

ttk.Button(UI_RSA,text='加密',width=6,command=RSA_Encrypt).place(x=410)
ttk.Button(UI_RSA,text='解密',width=6,command=RSA_Decrypt).place(x=475)
ttk.Button(UI_RSA,text='清空',width=6,command=RSA_Clear).place(x=540)

ttk.Label(UI_RSA,text='加密: c=(m ^ e) mod n              解密: m=(c ^ d) mod n').grid(column=1,row=4,sticky='NW')

#--------------散列-------------
UI_hash = ttk.LabelFrame(tab6,text='散列函数')
UI_hash.grid(column=0,row=0,padx=8,pady=4)
ttk.Label(UI_hash,text="明文").grid(column=0,row=0,pady=40,sticky='NW')
entry_text = Text(UI_hash,height=7,width=60,highlightcolor='blue')
entry_text.grid(column=1,row=0,padx=2,pady=5,sticky='NW')

ttk.Label(UI_hash,text="MD5生成").grid(column=0,row=2,pady=40,sticky='NW')
entry_res = Text(UI_hash,height=7,width=60,highlightcolor='blue')
entry_res.grid(column=1,row=2,padx=2,pady=5,sticky='NW')

ttk.Label(UI_hash,text="SHA-1生成").grid(column=0,row=4,pady=40,sticky='NW')
entry_res1 = Text(UI_hash,height=7,width=60,highlightcolor='blue')
entry_res1.grid(column=1,row=4,padx=2,pady=5,sticky='NW')

ttk.Label(UI_hash,text="    ").grid(column=0,row=5,pady=10,sticky='NW')

ttk.Button(UI_hash,text='生成',width=6,command=hash_encrypt).place(x=510,y=400)
ttk.Button(UI_hash,text='清空',width=6,command=hash_clear).place(x=440,y=400)
#-------------------------------
#---------介绍------------------
bottom = Frame(window)
Label(bottom,text='Crypto Tools',bd=2).pack(side=LEFT,fill=X)
Label(bottom,text='By:密码学组组组').pack(side=LEFT,fill=X)
bottom.pack(side=BOTTOM,anchor='sw')
window.iconbitmap('Crypto.ico')
#-------------------------------
window.mainloop()