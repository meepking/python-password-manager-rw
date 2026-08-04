import os
from time import sleep
import platform
import subprocess
import time
from getpass import getpass
from config import *
from log import *
from string import *
import secrets
from auth import authenticate as auth
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
    encrypt_opt = enc_opt_check()
    
    sleep(2)
    pswd_protection = pwp_check()

    sleep(2)
    locking_pswd = lock_check(pswd_protection)

    sleep(2)
    log_opt = log_opt_check()

    if pswd_protection == True:
       auth(locking_pswd)
    else:
        pass

    print('password manager active, what do you wish to do?')
    sleep(1)
    while True:
        print('choose an option:')
        try:
            menu_opt = int(input('1: create a password\n2: view a password\n3: modify a password\n4: view access log\n5: modify configuration\n6: view manager info\n7: exit program\n[choose an option]: '))
            sleep(1)
        except TypeError:
            print('must be an integer, or a number from the menu selection, try again')
        else:
            if menu_opt == 1:
                print('so you are adding a password?')
                sleep(1)
                try:
                    create_mode = int(input('so how many do you want to add?\nyour options are:\n1: only 1 password\n2: multiple passwords\n3: generate a password\n4: generate multiple passwords\n[choose your option]:'))
                except TypeError:
                    print('input must be a number, try again')
                    sleep(1)
                    continue
                except:
                    print('whatever you put in will not work as a valid input, input must be a number, try again')
                else:
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
                        else:
                            if os.path.exists(root_folder + '/' + website):
                                pass
                            else:
                                os.makedirs(root_folder + '/' + website)
                            os.mkdir(root_folder + '/' + website + '/' + username_to_add)
                            if encrypt_opt == True:
                                file_to_encrypt = root_folder + '/' + username_to_add + '/password.txt'
                                encrypt(file_to_encrypt, pswd_to_add)
                                sleep(2)
                                print('password file created and encrypted')
                            else:
                                f = open(root_folder + '/' + website + '/' + username_to_add + '/password.txt')
                                f.write(pswd_to_add)
                                f.close()
                                sleep(1)
                                print('password file created')
                    elif create_mode == 2:
                        print('so you need to make more than one? ok then, let\'s begin')
                        sleep(1)
                        fileset = []
                        while True:
                            website = input('[enter the website the username will be in, when done, leave this blank]:')
                            sleep(0.5)
                            if website == '':
                                break
                            else:
                                pass

                            username_to_add = input('[now enter the username to add for that website]:')
                            sleep(1)
                            folders_aligned = root_folder + '/' + website + '/' + username_to_add + '/password.txt'
                            data_block = [folders_aligned, website, username_to_add]
                            fileset.append(data_block)
                            print('username added to list, continuing')
                            continue

                        sleep(2)
                        print('alright, ' + str(len(fileset)) + ' passwords coming right up!')
                        sleep(2)
                        for x in fileset:
                            pswd_to_add = input('[enter the password you want to set for username ' + x[2] + 'in website ' + x[1] + ']: ')
                            sleep(1)
                            if os.path.exists(x[0]):
                                print('user already exists, overwrite?')
                                opt = input('[y/n]:')
                                sleep(1)
                                if opt == 'y':
                                    if encrypt_opt == True:
                                        encrypt(x[0], pswd_to_add)
                                        sleep(2)
                                        print('password overwritten and encrypted')
                                        continue
                                    else:
                                        f = open(x, 'w')
                                        f.write(pswd_to_add)
                                        f.close()
                                        sleep(1)
                                        print('password overwritten')
                                        sleep(1)
                                        continue
                                elif opt == 'n':
                                    print('password not overwritten and skipped')
                                    sleep(1)
                                    continue
                            else:
                                os.makedirs(root_folder + '/' + x[1] + '/' + x[2])
                                if encrypt_opt == True:
                                    encrypt(x[0], pswd_to_add)
                                    print('password file created and encrypted')
                                    sleep(1)
                                    continue
                                else:
                                    f = open(x, 'w')
                                    f.write(pswd_to_add)
                                    f.close()
                                    print('password file created')
                                    sleep(1)
                                    continue
                        
                        sleep(2)
                        print('alright, that seems to be done now')
                        sleep(1)
                        continue
                    elif create_mode == 3:
                        print('so you\'re going to rely on this script to make a password? ok then')
                        sleep(1)
                        print('do be warned that you are probably going to forget the password you have created here. but at least it\'s here, right?')
                        sleep(2)
                        print('alright, that is all I have to say about it, let\'s begin')
                        sleep(1)

                        website = input('[enter the website the username will be created]: ')

                        sleep(1)

                        username_to_add = input('[now enter the username that will be added to that website]')

                        website_check = root_folder + '/' + website
                        folders_aligned = root_folder + '/' + website + '/' + username_to_add + '/password.txt'

                        if os.path.exists(website_check):
                            pass
                        else:
                            os.makedirs(website_check)
                        sleep(1)
                        if os.path.exists(folders_aligned):
                            print('username already exists within this website folder')
                            sleep(2)
                            opt = input('overwrite password?\n[y/n]: ')

                            sleep(1)

                            if opt == 'y':
                                print('alright then')

                                pswd_len = int(input('first, how long do you need your password?\n[enter answer as an integer]: '))
                                sleep(1)
                                charset = ascii_letters + punctuation + digits

                                password = ''.join(secrets.choice(charset) for _ in range(pswd_len))

                                sleep(1)

                                print('password generation complete, your password for username: ' + username_to_add + ' is: ' + password + ' , now to put it on file')
                                sleep(1)

                                if encrypt_opt == True:
                                    encrypt(folders_aligned, password)
                                    sleep(1)

                                    print('generated password created to file and encrypted')
                                    sleep(1)
                                    continue
                                else:
                                    f = open(folders_aligned, 'w')
                                    f.write(password)
                                    f.close()

                                    print('generated password added to file')
                                    sleep(1)
                                    continue
                            elif opt == 'n':
                                print('change your mind, alright then')
                                sleep(1)
                                continue
                        else:
                            pswd_len = int(input('now enter the character length you need of your password\n[must be an integer]: '))

                            sleep(2)

                            charset = ascii_letters + digits + punctuation

                            password = ''.join(secrets.choice(charset) for _ in range(pswd_len))

                            print('password generation complete, your password is: ' + password)
                            sleep(1)
                            print('now adding to file...')
                            sleep(2)

                            if encrypt_opt == True:
                                encrypt(folders_aligned, password)
                                sleep(1)
                                print('password added and encrypted')
                                sleep(1)
                                continue
                            else:
                                f = open(folders_aligned, 'w')
                                f.write(password)
                                f.close()
                                print('password added')
                                sleep(1)
                                continue
                    elif create_mode == 4:
                        print('so you want to generate multiple passwords? ok then, let\'s begin')
                        sleep(2)

                        fileset = []
                        while True:
                            website = input('[enter the website the username will be added in(when done, leave this blank)]: ')
                            if website == '':
                                break
                            else:
                                pass
                            sleep(1)
                            username_to_add = input('[now add the username for that site]: ')

                            folders_aligned = root_folder + '/' + website + '/' + username_to_add + '/password.txt'

                            data_block = [folders_aligned, website, username_to_add]
                            sleep(1)
                            fileset.append(data_block)

                            print('password generation queued, continuing')
                            sleep(0.5)
                            continue
                        sleep(1)
                        print('all done? alright, ' + str(len(fileset)) + 'passwords to generate, coming right up')
                        sleep(1)

                        for e in fileset:
                            pswd_len = int(input('[enter the character length you wish the password for ' + e[2] + ' in website: ' + e[1] + ' to have]: '))

                            charset = ascii_letters + digits + punctuation
                            
                            password = ''.join(secrets.choice(charset) for _ in range(pswd_len))
                            sleep(1)
                            print('password is: ' + password)
                            if os.path.exists(e[0]):
                                print('though it would seem it already exists')
                                sleep(1)
                                ov_opt = input(' do you wish to overwrite the existing password\n[y/n]:')
                                sleep(1)
                                if ov_opt == 'y':
                                    print('overwriting...')
                                    sleep(1)
                                    if encrypt_opt == True:
                                        encrypt(e[0], password)
                                        print('overwrite complete')
                                        continue
                                    else:
                                        f = open(e[0], 'w')
                                        f.write(password)
                                        f.close()
                                        print('overwrite complete')
                                        continue
                                elif ov_opt == 'n':
                                    print('overwrite canceled and skipping to next one')
                                    sleep(1)
                                    continue
                            else:
                                if encrypt_opt == True:
                                    encrypt(e[0], password)
                                    print('password created and encrypted, continuing...')
                                    sleep(1)
                                    continue
                                else:
                                    f = open(e[0], 'w')
                                    f.write(password)
                                    f.close()
                                    print('password created, continuing')
                                    continue
                        sleep(1)
                        print('password generation complete')
                        sleep(1)
                        print('returning to menu...')
                        sleep(1)
                        continue
                    else:
                        print('that is not a valid option, try again')
                        sleep(1)
            elif menu_opt == 2:
                print('so you want to view a password? alright')
                sleep(1)
                if pswd_protection == True:
                    attempts = 3
                    print('but first, you must enter your password to view a password')
                    sleep(1)
                    
                else:
                    pass
                print('so what do you want to do?\noptions are:\n1: view a single password\n2: view multiple passwords\n3 view all passwords')
                sleep(0.5)
                try:
                    view_mode_opt = int(input('[enter your option]: '))
                except TypeError:
                    print('input must be a number, try again')
                    sleep(1)
                    continue
                else:
                    sleep(1)
                    if view_mode_opt == 1:
                        print('just one password? ok then')
                        sleep(2)
                        while True:
                            website = input('[enter the website of the user(or enter cancel to go back)]: ')
                            sleep(1)
                            if website == 'cancel':
                                print('don\'t want to view a password? fine then')
                                sleep(1)
                                break
                            if os.path.exists(root_folder + '/' + website):
                                break
                            else:
                                print('website folder does not exist, try again')
                                sleep(1)
                                continue
                        if website == 'cancel':
                            continue
                        else:
                            pass
                        sleep(1)
                        while True:
                            username = input('[now enter the username of that website you wish to the password of(or enter cancel to go back)]: ')
                            sleep(1)
                            if username == 'cancel':
                                print('changed your mind? fine then')
                                break
                            if os.path.exists(root_folder + '/' + website + '/' + username):
                                print('ok, so the username is there, but what about the password file?')
                                sleep(2)
                                if os.path.exists(root_folder + '/' + website + '/' + username + '/password.txt'):
                                    print('and the file is there too, good')
                                    sleep(1)
                                    break
                                else:
                                    print('it would appear that the file is not there, must have been deleted by you or someone else')
                                    sleep(1)
                                    opt = input('would you like to remove that user?\n[y/n]: ')
                                    sleep(1)
                                    if opt == 'y':
                                        print('alright, removing username...')
                                        sleep(1)
                                        try:
                                            os.rmdir(root_folder + '/' + website + '/' + username)
                                        except:
                                            print('for some reason, the folder cannot be removed, you may need to manually remove the folder')
                                            sleep(1)
                                        else:
                                            print('ok, that worked, moving on then')
                                            sleep(1)
                                        print('now, let\'s try that again')
                                        sleep(2)
                                        continue
                            else:
                                print('that username does not exist here, try again')
                                continue
                        sleep(1)
                        if username == 'cancel':
                            continue
                        print('alright, with all that out of the way,let\'s see that password')
                        sleep(3)

                        if encrypt_opt == True:
                            decrypt(root_folder + '/' + website + '/' + username + '/password.txt')
                            sleep(1)
                            continue
                        else:
                            f = open(root_folder + '/' + website + '/' + username + '/password.txt', 'r')
                            password = f.read()
                            f.close()
                            print('your password is: ' + password)
                            sleep(1)
                            continue
                    elif view_mode_opt == 2:
                        print('so you want to view multiple passwords? alright then')
                        sleep(2)
                        pswds_2_read = []
                        while True:
                            website = input('[enter the website of the username(leave blank to end selection)]: ')
                            sleep(1)
                            if website == '':
                                break
                            else:
                                pass
                            username = input('[now enter the username of that website to view the password of]: ')
                            sleep(1)
                            folders_aligned = root_folder + '/' + website + '/' + username + '/password.txt'
                            data_block = [folders_aligned, website, username]
                            pswds_2_read.append(data_block)
                            print('password queued, continuing...')
                            sleep(1)
                            continue
                        sleep(1)
                        print('alright, want to see ' + str(len(pswds_2_read)) + ' passwords? let\'s get started then')
                        sleep(1)

                        for e in pswds_2_read:
                            sleep(0.5)
                            if os.path.exists(e[0]):
                                if encrypt_opt == True:
                                    pswd = m_decrypt(e[0])
                                    sleep(1)
                                    print('password for username: ' + e[2] + ' in website: ' + e[1] + ' is: ' + pswd)
                                else:
                                    f = open(e[0], 'r')
                                    pswd = f.read()
                                    f.close()
                                    print('password for username: ' + e[2] + ' in website: ' + e[1] + ' is: ' + pswd)
                            else:
                                print('password skipped, does not exist')
                            sleep(0.5)
                        print('all passwords have been shown, returning to menu')
                        sleep(1)
                        continue
                    elif view_mode_opt == 3:
                        print('you want to view all your passwords? let\'s get started then')
                        sleep(1)
                        current_websites = os.listdir(root_folder)
                        if len(current_websites) <= 0:
                            print('there are no passwords to see here right now')
                            sleep(1)
                            continue
                        else:
                            print('you currently have ' + len(current_websites) + ' websites set in the manager, so let\'s get to it')
                        for e in current_websites:
                            print('users in website [' + e + ']:')
                            sleep(1)
                            usrlist = os.listdir(root_folder + '/' + e)
                            for x in usrlist:
                                folders_aligned = root_folder + '/' + e + '/' + x + '/password.txt'
                                if encrypt_opt == True:
                                    pswd = m_decrypt(folders_aligned)
                                    print('password for user ' + x + ' is: ' + pswd)
                                else:
                                    f = open(folders_aligned, 'r')
                                    pswd = f.read()
                                    f.close()
                                    print('password for user ' + x + ' is: ' + pswd)
                                sleep(0.5)
                            sleep(1)
                        print('all passwords listed, returning to menu')
                        continue
            elif menu_opt == 3:
                print('so you want to modify a password? ok then')
                sleep(1)
                if pswd_protection == True:
                    print('but first, you must enter your password to continue')
                    sleep(1)
                    auth(locking_pswd)
                    sleep(1)
                else:
                    pass
                print('since you want to modify a password, what exactly do you want to do?')
                sleep(1)
                try:
                    pswd_mod_mode = int(input('your options are:\n1: modify password\n2: remove a password\n[enter your option]: '))
                    sleep(1)
                except:
                    sleep(1)
                    print('that input is invalid, input must be a number, try again')
                    continue
                else:
                    if pswd_mod_mode == 1:
                        print('so you want to update/overwrite a password?')
                        sleep(1)
                        website = input('[enter the website that password is in]: ')