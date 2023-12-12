"""
    With symmetric encryption, only one key is used for
    encrypt/decrypt. This is bette known as the secret key.
    
    
    Nomrally it is a specific code: random string of letters or
    numbers produced by random number generator.
    
    The following is based on the Fernet algorithm in the 
    'cryptography' module

"""

from cryptography.fernet import Fernet
# Put this somewhere safe!
key = Fernet.generate_key()
f = Fernet(key)
token = f.encrypt(b"a really secret message. not for prying eyes.")
print(token)
print(f.decrypt(token))