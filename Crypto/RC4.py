#-*- coding: utf-8 -*-
PublicKey=[]
Box=[]
KeyStream=[]
cryption=[]

def Clear():
    PublicKey = []
    Box = []
    KeyStream = []
    cryption = []
def Init_Box(string):
    """
    初始化 置换盒
    第一步：
    Box[i]=i
    T[i]=Public_key[i % len]
    第二步:
    j=0
    j=(j+Box[i]+T[i])%256
    swap(Box[i],Box[j])
    """
    PublicKey=string
    for i in range(256):
        Box.append(i)
    Len=len(PublicKey)
    j = 0
    for i in range(256):
        index = ord(PublicKey[(i % Len)])
        j = (j + Box[i] + index) % 256
        Box[i], Box[j] = Box[j], Box[i]  # 交换Box[i]和Box[j]

def do_encrypt(string):
    """
    加密
    string : 待加/解密的字符串
    i=i+1 % 256
    j=j+Box[i] % 256
    swap(Box[i],Box[j])
    r=Box[i]+Box[j] %256
    """
    i=0
    j=0
    for s in string:
        i=(i+1)%256
        j=(j+Box[i]) %256
        Box[i],Box[j]=Box[j],Box[i]
        r=(Box[i]+Box[j])%256
        R=Box[r]
        KeyStream.append(R)
        cryption.append(chr(ord(s) ^ R))
    return ''.join(cryption)

def do_decrypt(string):
    #解密
    out=[]
    i=0
    for s in string:
        out.append(chr(ord(s) ^ KeyStream[i]))
        i=i+1
    return ''.join(out)
