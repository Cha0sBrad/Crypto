letters_lower = 'abcdefghijklmnopqrstuvwxyz'
letters_upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'


def affine(a, b, message):
    """加密过程"""
    if gcd(a,b) != 1 or gcd(a,26) != 1:
        return "Error!"
    cipher = ''
    for i in message:
        for j in range(len(letters_lower)):
            if i == letters_lower[j]:
                cipher += chr(((a * j + b) % 26) + 65).lower()
                break
            if i == letters_upper[j]:
                cipher += chr(((a * j + b) % 26) + 65).upper()
                break
            elif j == len(letters_lower)-1:
                cipher += i
    return cipher


def gcd(a, b):
    """欧几里得"""
    while a != 0:
        a, b = b % a, a #a0=a ; a=b%a ; b=a0
    return b


def find_mod_reverse(a, m):
    u1, u2, u3 = 1, 0, a
    v1, v2, v3 = 0, 1, m
    while v3 != 0:
        q = u3 // v3

        v1, v2, v3, u1, u2, u3 = (u1-q*v1), (u2-q*v2), (u3-q*v3), v1, v2, v3
    return u1 % m


def decrypt(a, b, cipher):
    if gcd(a,b) != 1 or gcd(a,26) != 1:
        return "Error!"
    message = ''
    for i in cipher:
        for j in range(len(letters_lower)):
            if i == letters_lower[j]:
                message += chr(((find_mod_reverse(a, 26) * (j - b)) % 26) + 65).lower()
                break
            if i == letters_upper[j]:
                message += chr(((find_mod_reverse(a, 26) * (j - b)) % 26) + 65).upper()
                break
            elif j == len(letters_lower) - 1:
                message += i
    return message

