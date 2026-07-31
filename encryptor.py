from cryptography.fernet import Fernet
from time import sleep
import os 
def encrypt(file, password):
    key_file = 'C:/python password manager rw/config/encrypt_key.key'
    
    if os.path.exists(key_file):
        f = open(key_file, 'r')
        
        key = f.read()
        encoded_key = key.encode()
        f.close()
        
        fern = Fernet(encoded_key)
    else:
        
        f = open(key_file, 'w')
        
        key = Fernet.generate_key()
        
        f.write(key.decode())
        
        fern = Fernet(key)
        f.close()
    encrypted = fern.encrypt(password)
    
    f = open(file, 'w')
    
    f.write(encrypted.decode())
    f.close()
def decrypt(file):
    key_file = 'C:/python password manager rw/config/encrypt_key.key'
    
    if os.path.exists(key_file):
        f = open(key_file, 'r')
        
        key = f.read()
        encoded_key = key.encode()
        f.close()
        
        fern = Fernet(encoded_key)
    else:
        sleep(2)
        print('encryption key not found, decryption cannot continue')
        sleep(2)
        print('will now exit script')
        exit()
    
    f = open(file, 'r')
    
    contents = f.read()
    f.close()
    pre_decrypt = contents.encode()
    
    decrypted = fern.decrypt(pre_decrypt)
    sleep(2)
    print('your password is: ' + decrypted.decode())
    sleep(1)
    print('file will remain encrypted')
def decrypt_file(file):
    key_file = 'C:/python password manager rw/config/encrypt_key.key'
    
    if os.path.exists(key_file):
        f = open(key_file, 'r')
        
        key = f.read()
        encoded_key = key.encode()
        f.close()
        
        fern = Fernet(encoded_key)
    else:
        sleep(2)
        print('encryption key not found, decryption cannot continue')
        sleep(2)
        print('will now exit script')
        sleep(2)
        exit()
    
    f = open(file, 'r')
    
    contents = f.read()
    f.close()
    pre_decrypt = contents.encode()
    
    decrypted = fern.decrypt(pre_decrypt)
    f = open(file, 'w')
    f.write(decrypted.decode())
    f.close()
def encrypt_file(file):
    key_file = 'C:/python password manager rw/config/encrypt_key.key'
    
    if os.path.exists(key_file):
        f = open(key_file, 'r')
        
        key = f.read()
        encoded_key = key.encode()
        f.close()
        
        fern = Fernet(encoded_key)
    else:
        
        f = open(key_file, 'w')
        
        key = Fernet.generate_key()
        
        f.write(key.decode())
        
        fern = Fernet(key)
        f.close()
    f = open(file, 'r')
    
    password = f.read()
    f.close()
    pre_encrypt = password.encode()
    
    encrypted = fern.encrypt(password)
    
    f = open(file, 'w')
    
    f.write(encrypted.decode())
    f.close()
def decrypt_lock():
    pswd_file = 'C:/python password manager rw/config/lock.txt'
    key_file = 'C:/python password manager rw/config/encrypt_key.key'
    
    if os.path.exists(key_file):
        f = open(key_file, 'r')
        
        key = f.read()
        encoded_key = key.encode()
        f.close()
        
        fern = Fernet(encoded_key)
    else:
        sleep(2)
        print('encryption key not found, decryption cannot continue')
        sleep(2)
        print('will now exit script')
        exit()
    
    f = open(pswd_file, 'r')
    
    contents = f.read()
    f.close()
    pre_decrypt = contents.encode()
    
    decrypted = fern.decrypt(pre_decrypt)
    sleep(2)
    return decrypted.decode()
def m_decrypt(file):
    key_file = 'C:/python password manager rw/config/encrypt_key.key'
    
    if os.path.exists(key_file):
        f = open(key_file, 'r')
        
        key = f.read()
        encoded_key = key.encode()
        f.close()
        
        fern = Fernet(encoded_key)
    else:
        sleep(2)
        print('encryption key not found, decryption cannot continue')
        sleep(2)
        print('will now exit script')
        exit()
    
    f = open(file, 'r')
    
    contents = f.read()
    f.close()
    pre_decrypt = contents.encode()
    
    decrypted = fern.decrypt(pre_decrypt)
    return decrypted.decode()