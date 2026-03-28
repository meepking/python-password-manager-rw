import os
from time import sleep
import platform
import subprocess
import time
from getpass import getpass
from config import *
try:
    import cryptography
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
    ecrypt_opt = enc_opt_check()
    
    sleep(2)
    pswd_protection = pwp_check()

    sleep(2)
    locking_pswd = lock_check(pswd_protection)

    sleep(2)
    log_opt = log_opt_check()

    