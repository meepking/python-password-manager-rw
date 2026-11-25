from encryptor import *
from time import *
from getpass import getpass
from log import *
from config import silent_log_opt_check


def authenticate():
    attempts = 3
    current_pswd = decrypt_lock
    log_opt = silent_log_opt_check()
    while True:
        pswd_input = getpass('[enter your password]: ')
        sleep(1)
        if pswd_input == current_pswd:
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
                print('no attempts remaining, locking access to script...')
                current_time = mktime(localtime())                    
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
                print('access denied, you have ' + str(attempts) + ' remaining, try again')
                sleep(1)
                if log_opt == True:
                    denied()
                else:
                    pass
                continue

def verify_file(lock_opt):
    lock_file = config_folder_path + '/lock.txt'
    if lock_opt == True:
        if os.path.exists('C:/python password manager rw/config/lock.txt'):
            pass
        else:
            print('locking password file is not present')
            sleep(1)
            print('since you have chosen to enable password protection, you must set one')
            sleep(2)
            print('do be warned that this file will be encrypted regardless of what you have chosen for you passwords that will end up in the root folder')
            sleep(3)
            while True:
                pswd_2_use = input('enter in the password you want to use\n[note: this will be the only time you will see it as you type it out]: ')
                sleep(1)
                if pswd_2_use == '':
                    print('password cannot be blank, try again')
                    sleep(1)
                    continue
                else:
                    pass
                
                final_opt = input('continue with this password?\n[y/n]: ')
                sleep(1)

                if final_opt == 'y':
                    print('alright then')
                    sleep(1)
                    encrypt(lock_file, pswd_2_use.encode())
                    break
                elif final_opt == 'n':
                    print('changed your mind? then try again')
                    sleep(1)
                    continue
                else:
                    print('invalid response, try again')
                    sleep(1)
                    continue
            print('new password has been set')
    else:
        pass
