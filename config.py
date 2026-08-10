from time import *
from getpass import getpass
import os
from encryptor import *


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
                os.mkdir(os.getcwd + '/config')
            except:
                print('huh, guess that failed too, perhaps there is a folder permission restriction. resolve that and try starting the script again')
            else:
                print('success, using' + os.getcwd() + '/config' + ' as configuration folder')
                return os.getcwd() + '/config'
        else:
            print('success, config folder added, continuing')
            return config_folder_path

def root_folder_check():
    config_folder_path = 'C:/python password manager rw/config'
    root_folder_file = config_folder_path + '/root_folder.txt'

    if os.path.exists(root_folder_file):
        f = open(root_folder_file, 'r')
        root_path = f.read()
        f.close()

        if os.path.exists(root_path):
            print('using path: ' + root_path + ' as the password root folder')
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
            if os.path.exists('C:/passwords'):
                print('folder already exists, no need to add')
                sleep(1)
            else:
                os.mkdir('C:/passwords')
            f = open(root_folder_file, 'w')
            f.write('C:/passwords')
            f.close()
            return 'C:/passwords'
        elif opt_1 == 'c' or opt_1 == 'C':
            print('so you want a custom path? make sure that it doesn\'t have any symbols that would not be allowed in folder creation')
            sleep(2)
            while True:
                folder_path_2_set = input('[enter the path you want to set as root folder(must be full path)]:')
                sleep(1)
                if folder_path_2_set.endswith('/'):
                    print('you should also make sure you don\'t add a slash at the end of the path as it won\'t work right with the rest o the script, please try again')
                    sleep(1)
                    continue
                if os.path.exists(folder_path_2_set):
                    print('folder already present, no need to add')
                    sleep(1)
                    print('writing to file...')
                    f = open(root_folder_file, 'w')
                    f.write(folder_path_2_set)
                    f.close()
                    sleep(1)
                    print('done, path now set as: ' + folder_path_2_set)
                    return folder_path_2_set
                else:
                    print('folder not present, will now attempt to make folder path...')
                    sleep(2)
                    try:
                        os.makedirs(folder_path_2_set)
                        sleep(2)
                    except:
                        print('path creation failed, this usually means it was invalid, or perms are not correctly configured for that set path, make sure the folder path is valid and the script has the correct permissions and try again')
                        sleep(2)
                        continue
                    else:
                        print('path creation success, now writing to file...')
                        sleep(2)
                        f = open(root_folder_file, 'w')
                        f.write(folder_path_2_set)
                        f.close()
                        print('done, path now set as: ' + folder_path_2_set)
                        return folder_path_2_set

def enc_opt_check():
    config_folder_path = 'C:/python password manager rw/config'
    option_file = config_folder_path + '/enc.txt'

    print('checking for encryption option file...')
    sleep(1)
    if os.path.exists(option_file):

        print('file present, reading...')
        f = open(option_file, 'r')
        opt = f.read()
        f.close()

        if opt == 'True':
            print('encryption feature enabled, passwords unreadable without this script')

            return True
        elif opt == 'False':
            print('WARNING: encryption feature disabled, all passwords are currently in plaintext and readable')

            return False
    
    else:
        print('file containing the option to encrypt password files is not present')
        sleep(2)
        print('this program is equipped to be able to protect your passwords further by encrypting the files to ensure they are unreadable when simply opening the file')
        sleep(2)
        print('this feature is optional, but is strongly recomended for better protection of your passwords')
        sleep(2)
        en_opt = input('do you wish to enable password encryption?\n[y/n]:')

        if en_opt == 'y':
            print('alright, encryption will be enabled')
            sleep(2)
            f = open(option_file, 'w')
            f.write('True')
            f.close()

            return True
        elif en_opt == 'n':
            print('ok, it will be disabled, but don\'t say I didn\'t warn you')
            sleep(2)
            f = open(option_file, 'w')
            f.write('False')
            f.close()

            return False
def pwp_check():
    config_folder_path = 'C:/python password manager rw/config'
    pwp_opt_file = config_folder_path + '/pwp_opt.txt'
    sleep(2)
    if os.path.exists(pwp_opt_file):
        f = open(pwp_opt_file, 'r')
        set_opt = f.read()
        f.close()

        if set_opt == 'True':

            return True
        elif set_opt == 'False':
            return False
    else:
        print('password protection option file not present')
        sleep(2)
        print('the password protection is a safegaurd against those who want to take your passwords who also have access to your computer')
        sleep(1)
        print('this feature is strongly recomended since this will also make sure that the only way to read the encrypted files is protected(if that is also enabled)')
        sleep(2)
        pwp_opt = input('do you wish to enable password protection?\n[y/n]:')
        sleep(1)
        if pwp_opt == 'y':
            print('alright, good, password protection will be enabled')
            sleep(1)
            print('oh, and just so you know, the password protection file with the password will be encrypted regardless of your preference')
            sleep(2)

            f = open(pwp_opt_file, 'w')
            f.write('True')
            f.close()
            return True
        elif pwp_opt == 'n':
            print('fine, it will be disabled. do be warned that I am not responsible for your passwords being stolen')
            sleep(2)

            f = open(pwp_opt_file, 'w')
            f.write('False')
            f.close()
            return False
        
def lock_check(pwp_opt):
    config_folder_path = 'C:/python password manager rw/config'
    lock_file = config_folder_path + '/lock.txt'

    if pwp_opt == True:

        if os.path.exists(lock_file):

            pswd = decrypt_lock()
            return pswd
        else:
            print('since you wanted to use password protection, you will need to create your password since you didn\'t make one yet')
            sleep(2)
            print('do keep in mind once again that this password will be encrypted regardless of your preference on whether you wanted it or not')
            sleep(3)
            while True:
                password_2_set = input('this will also be the only time you can see the password you enter here\n[enter the password you wish to create and set]: ')
                sleep(2)
                final_opt = input('proceed with this password?\n[y/n]:')
                sleep(1)
                if final_opt == 'y':
                    print('ok, now writing to file...')
                    sleep(2)
                    encrypt(lock_file, password_2_set.encode())
                    sleep(1)
                    print('password creation complete, you will need to enter it again upon entering the main interface of this script')
                    return password_2_set
                elif final_opt == 'n':
                    print('not ready yet? enter it again then')
                    sleep(1)
                    continue
                else:
                    print('hey, how about you pay attention to what is in the brackets, choose one of those answers')
                    continue
    elif pwp_opt == False:
        print('password protection disabled, no need to check for file')

def log_opt_check():
    config_folder_path = 'C:/python password manager rw/config'
    log_opt_file = config_folder_path + '/log-opt.txt'

    if os.path.exists(log_opt_file):
        f = open(log_opt_file, 'r')
        opt = f.read()
        f.close()

        if opt == 'True':
            print('logging function has been set to true')

            return True
        elif opt == 'False':
            print('logging function has been set to false')

            return False
        
    else:
        sleep(2)
        print('I have also put in a feature that will put in the times this script has been accessed, and what was accessed as well')
        sleep(2)
        print('this will help add another layer of security by a bit by showing you if someone tried to use the script')
        sleep(2)

        final_opt = input('do you wish to enable logging?\n[y/n]:')

        if final_opt == 'y':
            sleep(1)
            print('ok, logging set to true')
            sleep(1)

            f = open(log_opt_file, 'w')
            f.write('True')
            f.close()
            return True
        elif final_opt == 'n':
            sleep(1)
            print('ok, that is fine, this was a completely optional feature anyway')
            sleep(1)

            f = open(log_opt_file, 'w')
            f.write('False')
            f.close()
            return False
def silent_log_opt_check():
    config_folder_path = 'C:/python password manager rw/config'
    log_opt_file = config_folder_path + '/log-opt.txt'

    if os.path.exists(log_opt_file):
        f = open(log_opt_file, 'r')
        log_opt = f.read()
        f.close()

        if log_opt == 'True' or log_opt == True:
            return True
        else:
            return False
    else:
        return False
    