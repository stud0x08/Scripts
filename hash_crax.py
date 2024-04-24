from urllib.request import urlopen
import hashlib

md5_hash = input('Enter md5 hash value: ')
passlist = str(urlopen('https://raw.githubusercontent.com/danielmiessler/SecLists/master/Passwords/xato-net-10-million-passwords.txt',).read(), 'utf-8')
for password in passlist.split('\n'):
    hashguess = hashlib.md5(bytes(password , 'utf-8')).hexdigest()
    if hashguess == md5_hash:
        print('Password is: ' + str(password))
        quit()
    else:
        print('Password not found')
print('Password not present in the list')
