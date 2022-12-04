import os
from cryptography.fernet import Fernet

whitelist = ['ransomware.py', 'decryption-key.key', 'decrypt.py']
root = 'C:/Users/jings/Desktop/p-projs/malicious/ransomware/test'

def getFiles(path):
    files = []
    for item in os.listdir(path):
        if item in whitelist:
            continue
        elif os.path.isfile(path + '/' + item):
            files.append(path + '/' + item)
        elif os.path.isdir(path + '/' + item):
            files += (getFiles(path + '/' + item))
    return files


def main():
    files = getFiles(root)

    with open('decryption-key.key', 'rb') as decryptKey:
        key = decryptKey.read()

    for file in files:
        with open(file, 'rb') as f:
            contents = f.read()
            decryptedContents = Fernet(key).decrypt(contents)
        with open(file, 'wb') as f:
            f.write(decryptedContents)

    print('Files decrypted with key', key)


if __name__ == '__main__':
    main()
