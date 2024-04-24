import hashlib

print('------------------------\n'
      'Hashes available - md5,sha256 & sha512\n'
      '----------------------------------\n')

hashval = input('Enter any string: ')
hash1 = hashlib.md5()
hash1.update(hashval.encode())
print(hash1.hexdigest())

hash2 = hashlib.sha256()
hash2.update(hashval.encode())
print(hash2.hexdigest())

hash4 = hashlib.sha512()
hash4.update(hashval.encode())
print(hash4.hexdigest())