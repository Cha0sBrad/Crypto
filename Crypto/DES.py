#-*- coding: utf-8 -*-
from pyDes import *
import base64
def des_Encrypt(cmbCurr,entry_key,entry_vi,entry_wait):
    if(cmbCurr == 0):
        k = des(entry_key,ECB,pad=None,padmode=PAD_PKCS5)
        e = k.encrypt(entry_wait.encode('utf-8'))
        e = base64.b64encode(e)
        return e
    else:
        k = des(entry_key,CBC,entry_vi,pad=None,padmode=PAD_PKCS5)
        e = k.encrypt(entry_wait.encode('utf-8'))
        e = base64.b64encode(e)
        return e

def des_Decrypt(cmbCurr,entry_key,entry_vi,entry_wait):
    if(cmbCurr == 0):
        k = des(entry_key,ECB, pad=None, padmode=PAD_PKCS5)
        d = k.decrypt(base64.b64decode(entry_wait))
        d = d.decode('utf-8')
        return d
    else:
        k = des(entry_key, CBC, entry_vi, pad=None, padmode=PAD_PKCS5)
        d = k.decrypt(base64.b64decode(entry_wait))
        d = d.decode('utf-8')
        return d



