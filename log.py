import datetime
import os

def granted():
    file = 'C:/python password manager/config/access.txt'
    
    if not os.path.exists(file):
        start = True
    else:
        start = False
    
    f = open(file, 'a')
    t = datetime.datetime.now()
    
    if start == True:
        f.write('manager initiallized on: ' + t.strftime('%x') + ', at: ' + t.strftime('%X') + '\n')
        f.write('----------------------------------------\n')
    else:
        pass
    
    f.write('[' + t.strftime('%x') + ', ' + t.strftime('%X') + ']: login successful, access granted to manager or manager function\n')
    f.write('-------------------------------\n')
    f.close()
def denied():
    file = 'C:/python password manager/config/access.txt'
    
    if not os.path.exists(file):
        start = True
    else:
        start = False
    
    f = open(file, 'a')
    t = datetime.datetime.now()
    
    if start == True:
        f.write('manager initiallized on: ' + t.strftime('%x') + ', at: ' + t.strftime('%X') + '\n')
        f.write('----------------------------------------\n')
    else:
        pass
    
    f.write('[' + t.strftime('%x') + ', ' + t.strftime('%X') + ']: login falied; access denied\n')
    f.write('-------------------------------\n')
    f.close()
def add_pswd(username):
    file = 'C:/python password manager/config/access.txt'
    
    if not os.path.exists(file):
        start = True
    else:
        start = False
    
    f = open(file, 'a')
    t = datetime.datetime.now()
    
    if start == True:
        f.write('manager initiallized on: ' + t.strftime('%x') + ', at: ' + t.strftime('%X') + '\n')
        f.write('----------------------------------------\n')
    else:
        pass
    
    f.write('[' + t.strftime('%x') + ', ' + t.strftime('%X') + ']: new password has been added for username: ' + username + '\n')
    f.write('----------------------------------------\n')
    f.close()
def rm_pswd(username):
    file = 'C:/python password manager/config/access.txt'
    
    if not os.path.exists(file):
        start = True
    else:
        start = False
    
    f = open(file, 'a')
    t = datetime.datetime.now()
    
    if start == True:
        f.write('manager initiallized on: ' + t.strftime('%x') + ', at: ' + t.strftime('%X') + '\n')
        f.write('----------------------------------------\n')
    else:
        pass
    
    f.write('[' + t.strftime('%x') + ', ' + t.strftime('%X') + ']: password for: ' + username + ' has been removed from database\n')
    f.write('----------------------------------------\n')
    f.close()
def config_change(change):
    file = 'C:/python password manager/config/access.txt'
    
    if not os.path.exists(file):
        start = True
    else:
        start = False
    
    f = open(file, 'a')
    t = datetime.datetime.now()
    
    if start == True:
        f.write('manager initiallized on: ' + t.strftime('%x') + ', at: ' + t.strftime('%X') + '\n')
        f.write('----------------------------------------\n')
    else:
        pass
    
    f.write('[' + t.strftime('%x') + ', ' + t.strftime('%X') + ']: configuration has been modified\n')
    f.write('change made: ' + change + '\n')
    f.write('----------------------------------------\n')
    f.close()
def viewed(username):
    file = 'C:/python password manager/config/access.txt'
    
    if not os.path.exists(file):
        start = True
    else:
        start = False
    
    f = open(file, 'a')
    t = datetime.datetime.now()
    
    if start == True:
        f.write('manager initiallized on: ' + t.strftime('%x') + ', at: ' + t.strftime('%X') + '\n')
        f.write('----------------------------------------\n')
    else:
        pass
    
    f.write('[' + t.strftime('%x') + ', ' + t.strftime('%X') + ']: password file accessed for username: ' + username + '\n')
    f.write('-------------------------------\n')
    f.close()
def lockout_log():
    file = 'C:/python password manager/config/access.txt'

    if not os.path.exists(file):
        start = True
    else:
        start = False
    
    f = open(file, 'a')
    t = datetime.datetime.now()
    
    if start == True:
        f.write('manager initiallized on: ' + t.strftime('%x') + ', at: ' + t.strftime('%X') + '\n')
        f.write('----------------------------------------\n')
    else:
        pass
    
    f.write('[' + t.strftime('%x') + ', ' + t.strftime('%X') + ']: password has been entered too many times incorrectly, user access blocked for 12 hours\n')
    f.write('-------------------------------\n')
    f.close()