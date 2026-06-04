import os
from time import sleep
import platform
import subprocess
import time
from getpass import getpass
from config import *
from log import *
try:
    import cryptography # pyright: ignore[reportMissingImports]
except ModuleNotFoundError:
    print('the cryptography library is currently not present and must be installed')
    sleep(2)
    print('installing cryptography...')
    sleep(0.5)
    subprocess.run('pip install cryptography', capture_output=True)
    sleep(1)
    print('install complete, will now exit script, start it again for module to take effect, if it shows that it fails, you may not have pip installed and implemented')
    exit()
else:
    pass

current_os = platform.system()

if current_os == 'Windows':
    print('windows detected, using windows filesystem format')

    sleep(2)


    if os.path.exists('lockout.txt'):
        print('lockout file is present, checking file...')
        sleep(2)
        
        lockout_check_file = open('lockout.txt', 'r')
        current_time = time.mktime(time.localtime())
        time_in_file = float(lockout_check_file.read())
        lockout_check_file.close()

        if time_in_file > current_time:
            print('lockout has not expired, therefore will not continue into program')
            sleep(2)
            print('please wait until ' + time_in_file.strftime('%x') + ', ' + time_in_file.strftime('%X') + 'until you can access the program again')
            sleep(3)
            exit()
        else:
            print('lockout has expired, so the file is no longer needed')
            sleep(1)
            os.remove('lockout.txt')
        
    else:
        pass

    config_folder = folder_check()

    sleep(1)
    root_folder = root_folder_check()

    
    sleep(2)
    encrypt_opt = enc_opt_check()
    
    sleep(2)
    pswd_protection = pwp_check()

    sleep(2)
    locking_pswd = lock_check(pswd_protection)

    sleep(2)
    log_opt = log_opt_check()

    if pswd_protection == True:
        attempts = 3
        while True:
            pswd_input = getpass('[please enter your password]:')
            sleep(1)
            if pswd_input == locking_pswd:
                print('access granted')
                sleep(1)
                if log_opt == True:
                    granted()
                else:
                    pass
                break
            else:
                attempts = attempts - 1
                
                if attempts <= 0:
                    current_time = time.mktime(localtime())

                    lockout_time = current_time + 86400.0
                    f = open('lockout.txt', 'w')
                    f.write(lockout_time)
                    f.close()
                    sleep(1)
                    print('you have now been blocked from accessing this script. you will be able to access the script again after:' + lockout_time.strftime('%x') + ', ' + lockout_time.strftime('%X'))
                    sleep(2)
                    if log_opt == True:
                        lockout_log()
                    else:
                        pass
                    exit()
                else:
                
                    print('access denied, you have: ' + str(attempts) + ' left before lockout\nplease try again')
                    if log_opt == True:
                        denied()
                    else:
                        pass
                    continue
    else:
        pass

    print('password manager active, what do you wish to do?')
    sleep(1)
    while True:
        print('choose an option:')
        try:
            menu_opt = int(input('1: create a password\n2: view a password\n3: modify a password\n4: view access log\n5: modify configuration\n6: view manager info\n7: exit program'))
            sleep(1)
        except TypeError:
            print('must be an integer, or a number from the menu selection, try again')
        else:
            if menu_opt == 1:
                print('so you are adding a password?')
                sleep(1)
                create_mode = input('so how many do you want to add?\nyour options are:\n1: only 1 password\n2: multiple passwords\n3: generate a password\n4: generate multiple passwords\n[choose your option]:')
                
                if create_mode == 1:
                    print('just one? ok then')
                    sleep(2)
                    website = input('[enter the website the username was created on]: ')
                    sleep(1)
                    username_to_add = input('[enter the username of the created user on that website]: ')
                    sleep(1)
                    pswd_to_add = input('[now enter the password you wish to make]: ')
                    if os.path.exists(root_folder + '/' + website + '/' + username_to_add):
                        print('user already exists with that website in this system')
                        sleep(1)
                        opt = input('overwrite current password?\n[y/n]: ')
                        sleep(1)
                        if opt == 'y':
                            print('alright, overwriting password file...')
                            sleep(2)
                            if encrypt_opt == True:
                                file_to_encrypt = root_folder + '/' + website + '/' + username_to_add + '/password.txt'
                                encrypt(file_to_encrypt, pswd_to_add)
                                print('password updated')
                                sleep(1)
                                continue
                            else:
                                f = open(root_folder + '/' + website + '/' + username_to_add + '/password.txt', 'w')
                                f.write(pswd_to_add)
                                f.close()
                                print('password updated')
                                sleep(1)
                                continue
                        elif opt == 'n':
                            print('change your mind? alright then, overwrite and creation has been canceled')
                            sleep(1)
                            continue
                elif create_mode == 2:
                    print('so you need to make more than one? ok then, let\'s begin')

                    