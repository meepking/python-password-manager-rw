from encryptor import *
from time import *
from getpass import getpass
from log import *
from config import silent_log_opt_check


def authenticate(current_pswd):
    attempts = 3
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