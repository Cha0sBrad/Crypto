# -*- coding: utf-8 -*-
from socket import *
import random
def createPrime():
    while True:
        p = random.randint(2,1000)
        flag = True
        for i in range(2,p-1):
            if p % i == 0:
                flag = False
                break
        if flag :
            return p

def get_generator(p):
    a = 2
    list = []
    while a < p:
        flag = 1
        while flag != p:
            if pow(a, flag, p) == 1:
                break
            flag += 1
        if flag == (p-1):
            list.append(a)
        a += 1
    return list[random.randint(0,len(list)-1)]

def Get_Calculation(p, a ,X):
    result = 1
    while X != 0:
        if X & 1 == 1:
            result = (result * a) % p
        X >>= 1
        if X != 0:
            a = (a * a) % p
    return result

def Get_Key(X, Y, p):
    result = 1
    while X != 0:
        if X & 1 == 1:
            result = (result * Y) % p
        X >>= 1
        if X != 0:
            Y = (Y * Y) % p
    return result

def Terminal_A(a, p):
    HOST = '0.0.0.0'
    PORT = 2333
    BUFSIZ = 1024
    ADDR = (HOST, PORT)
    tcpSerSock = socket(AF_INET, SOCK_STREAM)
    tcpSerSock.bind(ADDR)
    tcpSerSock.listen(5)

    while True:
        tcpCliSock, addr = tcpSerSock.accept()
        YB = int(tcpCliSock.recv(BUFSIZ).decode('utf-8'))
        if not YB:
            break
        XA = random.randint(0, (p - 1))
        YA = str(Get_Calculation(p, a, XA))
        tcpCliSock.send(YA.encode('utf-8'))
        Key = str(Get_Key(XA, YB, p))
        return Key, YA
    tcpSerSock.close()

def Terminal_B(a, p):
    HOST = '127.0.0.1'
    PORT = 2333
    BUFSIZ = 1024
    ADDR = (HOST, PORT)

    tcpCliSock = socket(AF_INET, SOCK_STREAM)
    tcpCliSock.connect(ADDR)
    while True:
        XB = random.randint(0, (p - 1))
        YB = str(Get_Calculation(p, a, XB))
        tcpCliSock.send(YB.encode('utf-8'))
        YA = int(tcpCliSock.recv(BUFSIZ).decode('utf-8'))
        if not YA:
            break
        Key = str(Get_Key(XB, YA, p))
        return Key, YB
    tcpCliSock.close()
