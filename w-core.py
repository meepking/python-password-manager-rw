#this file contains the core functions of the password manager on windows based systems
import os
from time import sleep
from encryptor import *
from auth import authenticate
from log import *


def add_pswd(root_folder, site, uname, password):

    if os.path.exists(root_folder + '/' + site):
        pass
    else:
        os.mkdir(root_folder + '/' + site)
    folders_aligned = root_folder + '/' + site + '/' + uname + '/password.txt'
    if os.path.exists(folders_aligned):
        print('password is already added')
        sleep(1)
        ov_opt = input('do you wish to overwrite the current password with the new one?\n[y/n]: ')
        sleep(1)
        if ov_opt == 'y':
            print('alright, overwriting password...')
            sleep(2)
            if encrypt_opt == True:
                encrypt(folders_aligned, password)
            else:
                f = open(folders_aligned, 'w')
                f.write(password)
                f.close()
        elif ov_opt == 'n':
            print('keeping it the same? alright then')
            continue
    else:
        if encrypt_opt == True:
            encrypt(folders_aligned, password)
        else:
            f = open(folders_aligned, 'w')
            f.write(password)
            f.close()

def add_pswds(fileset):
    for e in fileset:
        pass