import hashlib
def myhash(t):
    md5 = hashlib.md5()
    md5.update(t.encode('utf-8'))
    return md5.hexdigest()

def myshaone(t):
    sha = hashlib.sha1()
    sha.update(t.encode('utf-8'))
    return sha.hexdigest()
