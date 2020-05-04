# encrypt and decrypt a message
s='This is a SECRET! message.'
keyU='ABCDEFGHIJKLMNOPQRSTUVWXYZ'
keyL='abcdefghijklmnopqrstuvwxyz'
special=' !.'
encoded_message=""
for c in s:
    if c in keyU:
        index = keyU.index(c)+1
        if index >= len(keyU) : index = 0 
        encoded_message += keyU[index]
    elif c in keyL:
        index = keyL.index(c)+1
        if index >= len(keyL) : index = 0 
        encoded_message += keyL[index]
    elif c in special:
        index = special.index(c)+1
        if index >= len(special) : index = 0 
        encoded_message += special[index]
    else :
        encoded_message += c
print(encoded_message)
# exit(0)
decoded_message=""
for c in encoded_message:
    if c in keyU:
        index = keyU.index(c)-1
        if index < 0 : index = len(keyU) - 1 
        decoded_message += keyU[index]
    elif c in keyL:
        index = keyL.index(c)-1
        if index < 0  : index = len(keyL) - 1 
        decoded_message += keyL[index]
    elif c in special:
        index = special.index(c)-1
        if index < 0  : index = len(special) - 1 
        decoded_message += special[index]
    else :
        decoded_message += c
print(decoded_message)
# exit(0)

from cryptography.fernet import Fernet # pip install cryptography
key = Fernet.generate_key()
f = Fernet(key)
e = f.encrypt(b"This is a SECRET! message.")
print(e)
# >>> token
# b'gAAAAABeoDZ_0JJUN27VNrhaxufhSIGdvkIwUlLfon5uYbnJHmw2TU26PK3dGn1badO6g1JGljrFSGE6ilOk2xZQC3WC1FKbbkZE41SZd3UwMofXO5_vZCE='
d = f.decrypt(e)
print(d)
# b'This is a SECRET! message.'
