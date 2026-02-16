from time import *
from getpass import getpass
import os



def folder_check():
    config_folder_path = 'C:/python password manager rw/config'
    if os.path.exists(config_folder_path):
        print('config folder present, no need to add')
        return config_folder_path
    else:
        print('config folder not present, adding...')
        sleep(1)
        try:
            os.mkdir(config_folder_path)
        except:
            print('failed, using current directory...')
            sleep(1)
            try:
                os.mkdir(os.getcwd + '\config')
            except:
                print('huh, guess that failed too, perhaps there is a folder permission restriction. resolve that and try starting the script again')
            else:
                print('success, using' + os.getcwd() + '\config' + ' as configuration folder')
                return os.getcwd() + '\config'
        else:
            print('success, config folder added, continuing')
            return config_folder_path

