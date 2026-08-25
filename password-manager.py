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
    sleep(3)
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
    
    pswd_protection = pwp_check()

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
        except:
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
                                    encrypt(file_to_encrypt, pswd_to_add.encode())
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
                                f = open(root_folder + '/' + website + '/' + username_to_add + '/password.txt', 'w')
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
                                    encrypt(x[0], pswd_to_add.encode())
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
                                    encrypt(folders_aligned, password.encode())
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
                                encrypt(folders_aligned, password.encode())
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
                                        encrypt(e[0], password.encode())
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
                                    encrypt(e[0], password.encode())
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
                    auth(locking_pswd)
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
                            print('you currently have ' + str(len(current_websites)) + ' websites set in the manager, so let\'s get to it')
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
                        sleep(1)
                        if os.path.exists(root_folder + '/' + website):
                            pass
                        else:
                            print('website is not present, please try again')
                            sleep(1)
                            continue
                        username = input('[now enter the username of that site]: ')
                        folders_aligned = root_folder + '/' + website + '/' + username + '/password.txt'
                        sleep(1)
                        if os.path.exists(folders_aligned):
                            pass
                        else:
                            print('the username folder and/or the password file, does not exist, try again')
                            sleep(1)
                            continue

                        if encrypt_opt == True:
                            password = decrypt(folders_aligned)
                        else:
                            f = open(folders_aligned, 'r')
                            password = f.read()
                            f.close()

                        print('your password right now is ' + password)
                        sleep(1)
                        edit_opt = input('are you sure you want to change it?\n[y/n]: ')
                        sleep(1)
                        if edit_opt == 'y':
                            while True:
                                new_pswd = input('[input the password you want to use in place of the old one]: ')
                                sleep(1)
                                final_opt = input('are you sure you want to change your current password?\n[y/n]: ')
                                sleep(1)
                                if final_opt == 'y':
                                    if encrypt_opt == True:
                                        encrypt(folders_aligned, new_pswd.encode())
                                        print('password updated')
                                        sleep(1)
                                        break
                                    else:
                                        f = open(folders_aligned, 'w')
                                        f.write(new_pswd)
                                        f.close()
                                        print('password updated')
                                        sleep(1)
                                        break
                                elif final_opt == 'n':
                                    print('ok, but do you still want to edit that password?')
                                    opt = input('[y/n]: ')
                                    if opt == 'y':
                                        print('ok, then try again')
                                        sleep(1)
                                        continue
                                    elif opt == 'n':
                                        print('changed your mind? ok then')
                                        sleep(1)
                                        break
                                    else:
                                        print('that is not a valid option here, try again')
                                        sleep(1)
                                        continue
                                else:
                                    print('that is not a valid option, try again')
                                    sleep(1)
                                    continue
                        elif edit_opt == 'n':
                            print('changed your mind? that\'s fine')
                            sleep(1)
                            continue
                        else:
                            print('that is not a valid option, try again')
                            sleep(1)
                            continue
                    elif pswd_mod_mode == 2:
                        print('so you want to remove a password? ok then')
                        sleep(1)
                        website = input('[enter the website of the user you want to remove]: ')
                        sleep(1)
                        website_chk = root_folder + '/' + website

                        if os.path.exists(website_chk):
                            pass
                        else:
                            print('website does not exist, please try again')
                            sleep(1)
                            continue
                        username = input('[now enter the username of the password you wish to remove]: ')
                        sleep(1)

                        usr_chk = website_chk + '/' + username

                        if os.path.exists(usr_chk) and os.path.exists(usr_chk + '/password.txt'):
                            print('WARNING: you are about to remove a password from the manager, are you sure you want to proceed? this cannot be undone!')
                            final_opt = input('[y/n]: ')
                            sleep(1)
                            if final_opt == 'y':
                                print('ok then, deleting file and username...')
                                sleep(1)
                                folders_aligned = usr_chk + '/password.txt'
                                try:
                                    os.remove(folders_aligned)
                                except PermissionError:
                                    print('it would seem that there are issues with removing the file, something is blocking this script from removing the file. you will have to remove the file yourself via file explorer')
                                    sleep(3)
                                    continue
                                except FileNotFoundError:
                                    print('huh, I guess the file is already gone')
                                    sleep(1)
                                    print('so now the user folder can be removed')
                                    sleep(1)
                                    os.rmdir(usr_chk)
                                    print('and done!')
                                except:
                                    print('I guess something else has happened, to where the file cannot be removed by this script. you will have to do that yourself')
                                    sleep(1)
                                else:
                                    print('and done! now to remove user folder')
                                    sleep(1)
                                    os.rmdir(usr_chk)
                                    print('and its gone')
                                    sleep(1)
                                finally:
                                    if len(os.listdir(website_chk)) == 0:
                                        print('the website folder also appears to be empty, therefor will also be deleted')
                                        sleep(1)
                                        os.rmdir(website_chk)
                                        print('and done')
                                    else:
                                        pass
            elif menu_opt == 4:
                print('opening log...')
                sleep(2)
                f = open(config_folder + '/access.txt', 'r')
                main_file = f.read()
                f.close()
                print('[[[start of file]]]')
                sleep(1)
                print(main_file)
                sleep(1)
                print('[[[end of file]]]')
                input('[press enter to continue]')
            elif menu_opt == 5:
                print('so you want to change the manager configuration? ok then')
                sleep(1)
                if pswd_protection == True:
                    print('but first, you must enter in your password to change the config')
                    sleep(1)
                    auth(locking_pswd)
                    sleep(1)
                else:
                    pass

                rootfolder_modified = False
                encryptopt_modified = False
                lockpswd_modified = False
                lockopt_modified = False
                logopt_modified = False
                while True:
                    print('so what do you want to change?\n1: root folder\n2: option to encrypt passwords\n3: password protection\n4: change password for password protection system\n5: logging functionality')
                    config_opt = input('[enter your option]')
                    sleep(1)
                    if config_opt == 1:
                        if rootfolder_modified == True:
                            print('you already modified where your folder is going to be, you want to change it again, or do you want to restore it to what it was before?')
                            opt = input('[(c)hange/(r)estore]: ')
                            sleep(1)
                            if opt == 'c' or opt == 'change':
                                print('so you want to change it again? ok then')
                                sleep(1)
                                new_path = input('[enter the path you want to set instead]: ')
                                sleep(1)
                                if os.path.exists(new_path):
                                    pass
                                else:
                                    print('file path is not present, attepting to create path...')
                                    sleep(1)
                                    try:
                                        os.makedirs(new_path)
                                    except:
                                        print('path creation failed, you will have to create your desired path and try again')
                                        sleep(2)
                                        continue
                                    else:
                                        print('path created successfully')
                                        sleep(1)
                                print('now adding to file...')
                                sleep(1)
                                root_folder_file = 'C/password manager rw/config/root_folder.txt'
                                f = open(root_folder_file, 'w')
                                f.write(new_path)
                                f.close()
                                print('path added to file, returning to config menu...')
                                sleep(1)
                                continue
                            elif opt == 'r' or opt == 'restore':
                                print('back to the way it was huh? alright')
                                sleep(1)
                                print('using previously configured root folder...')
                                sleep(2)
                                root_folder_file = 'C/password manager rw/config/root_folder.txt'
                                f = open(root_folder_file, 'w')
                                f.write(root_folder)
                                f.close()
                                print('root folder restored to ' + root_folder)
                                sleep(1)
                                rootfolder_modified = False
                                continue
                        else:
                            print('so you want to change where your folder is')
                        sleep(1)
                        new_path = input('[enter the new path you wish to set(must be a valid path)]: ')
                        sleep(1)
                        if os.path.exists(new_path):
                            pass
                        else:
                            print('folder is not present, attempting to create folder...')
                            sleep(1)
                            try:
                                os.makedirs(new_path)
                            except:
                                print('path creation failed, please make sure that it is a valid path and try again')
                                continue
                            else:
                                print('folder creation successful, now adding to file')
                                sleep(1)
                            root_folder_file = 'C/password manager rw/config/root_folder.txt'
                            f = open(root_folder_file, 'w')
                            f.write(new_path)
                            f.close()
                            rootfolder_modified = True
                            print('root folder changed')
                            continue
                    elif config_opt == 2:
                        print('checking current option...')
                        sleep(2)
                        if encrypt_opt == True:
                            print('the option to encrypt your password files is currently enabled')
                            sleep(1)
                            print('are you sure you want to disable this?')
                            opt = input('[y/n]: ')
                            sleep(1)
                            if opt == 'y':
                                print('ok, disabling encryption...')
                                sleep(1)
                                f = open('C:/password manager rw/config/enc.txt', 'w')
                                f.write('False')
                                f.close()
                                print('encryption disabled')
                                sleep(1)
                                encryptopt_modified = True
                                continue
                            elif opt == 'n':
                                print('changed your mind? that is fine, it is better to keep this feature on anyway')
                                sleep(1)
                                continue
                            else:
                                print('that option is not valid, try again')
                                sleep(1)
                                continue
                        else:
                            print('encryption is currently disabled')
                            sleep(1)
                            print('do you want to enable encryption')
                            opt = input('[y/n]: ')
                            sleep(1)
                            if opt == 'y':
                                print('ok, enabling encryption')