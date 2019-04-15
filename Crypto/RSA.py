#-*- coding: utf-8 -*-
from tkinter import messagebox
from binascii import *
import base64

def gcd(p,q):
    if q == 0:
        return p
    else:
        return gcd(q, p%q)

def analyze(n):
    item = 2
    flag = False
    while item < n:
        if n % item == 0:
            if gcd(item, int(n / item)) == 1:
                return (item, int(n / item))
        item += 1
    if not flag:
        return flag
def RSA_Get_Key(e, euler):
    k = 1
    while True:
        if (e * k) % euler == 1:
            return k
        k += 1

def RSA_Get_D(n, e):
    if n >= 999999:
        messagebox.showerror('Error', 'N is too long!')
        return
    if analyze(n):
        p, q = analyze(n)
    else:
        messagebox.showerror('Error', 'illegal input(N)')
        return
    d = int(RSA_Get_Key(e, ((p-1)*(q-1))))
    return d

def RSA_Encode(m, e, n):
    res = ''
    for i in range(0, len(m), 2):
        data = int((chr(m[i])+chr(m[i+1])), 16)
        result = 1
        temp = e
        while temp != 0:
            if temp & 1 == 1:
                result = (result * data) % n
            temp >>= 1
            if temp != 0:
                data = (data * data) % n
        res += hex(result).split('0x')[1].zfill(3)
    res = str(base64.b64encode(res.encode('utf-8')), 'utf-8')
    return res


def RSA_Decode(c, d, n):
    c = base64.b64decode(c).decode('utf-8')
    list = []
    res = ''
    for i in range(0,len(c), 3):
        list.append(int((c[i]+c[i+1]+c[i+2]), 16))
    for i in list:
        temp = d
        result = 1
        while temp != 0:
            if temp & 1 == 1:
                result = (result * i) % n
            temp >>= 1
            if temp != 0:
                i = (i * i) % n
        res += hex(result).split('0x')[1]
    res = a2b_hex(res.encode('utf-8')).decode('utf-8')
    return res


def translate(m, n):
    if n < 255 :
        messagebox.showerror('Error', 'N is too small!')
    encrypt = b2a_hex(m.encode('utf-8'))
    return encrypt

