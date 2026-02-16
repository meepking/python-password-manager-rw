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

def root_folder_check():
    config_folder_path = 'C:/python password manager rw/config'
    root_folder_file = config_folder_path + '/config/root_folder.txt'

    if os.path.exists(root_folder_file):
        f = open(root_folder_file, 'r')
        root_path = f.read()
        f.close()

        if os.path.exists(root_path):
            print('using path: ' + root_path + ' as the paasword root folder')
            return root_path
        else:
            print('for some reason, the root folder is not there, therefore will be added')
            try:
                os.makedirs(root_path)
            except:
                print('it would appear the root folder could not be made, it seems it would be best if the folder was made manually\n so, make the folder in this exact path: ' + root_path)
                sleep(3)
                input('[press enter to exit]')
                exit()
            else:
                print('root folder created, continuing...')
                return root_path
    else:
        print('root folder not present')
        sleep(2)
        print('the root folder is where all your passwords will go when they have been added')
        sleep(1)
        print('for this, it is up to you where you want the root folder to be present, or you could use the default option')
        sleep(1)
        opt_1 = input('so what will it be? would you want to define your own folder, or just use the default?\n[(D)efault/(c)ustom]:')
        sleep(2)
        if opt_1 == 'd' or opt_1 == 'D':
            print('alright, using default, which is: C:/passwords')
            sleep(2)
            os.mkdir('C:/passwords')
            return 'C:/passwords'
        elif opt_1 == 'c' or opt_1 == 'C':
            print('so you want a custom path? make sure that it doesn\'t have any symbols that would not be allowed in folder creation')