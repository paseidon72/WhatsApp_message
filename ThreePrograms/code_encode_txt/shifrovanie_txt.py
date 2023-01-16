import pyAesCrypt

password = input('Enter password: ')
#encript
#pyAesCrypt.encryptFile('data.txt', 'data.txt.aes', password)
#descript
pyAesCrypt.decryptFile('data.txt.aes', 'dataout.txt', password)
