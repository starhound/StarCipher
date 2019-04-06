# StarCipher (Written and Maintained by Wesley Reid - http://starhound.com) 

import py.pycrypt
from secretpy import Affine
from secretpy import Vigenere
from secretpy import Trifid
from secretpy import CryptMachine
from secretpy import Zigzag
from py.pycrypt import reverse_cipher

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = 24


def getType():
    while True:
        print("""\nSelect cipher type: 
        (1) Ceasar 
        (2) Zig-Zag 
        (3) Trifid
        (4) Reverse
        (5) Affine
        (6) Viginere
        """)
        mode = input().lower()
        if mode in 'ceasar 1 reverse 2 rot13 3 xor 4 affine 5 viginere 6'.split():
            return mode
        else:
            print('Please select value 1 through 6 for a cipher type.')

def getMode():
    while True:
        print('Do you wish to (e)ncrypt or (d)ecrypt a message?')
        mode = input().lower()
        if mode in 'encrypt e decrypt d'.split():
            return mode
        else:
            print('Enter either "encrypt" or "e" or "decrypt" or "d".')

def getMessage():
     print('\nEnter your message:')
     return input()

def getKey():
     key = 0
     while True:
        print('\nEnter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE):
           return key

def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)

#Some ciphers from secretpy expect string/letter based keys
def getKeyString():
     while True:
        print('\nEnter the key value (String Form):')
        key = input()
        if hasNumbers(key): 
            print('\nKey must be a string value.')
        else:
            if len(key) > 0:
                return key
            else:
                print("\nPlease enter a key with at least one letter length.")

def ceasarTranslatedMessage(mode, message, key):
    if mode[0] == 'd':
        key = -key
    translated = ''
    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)	
        if symbolIndex == -1: # Symbol not found in SYMBOLS.
            translated += symbol
        else:
            symbolIndex += key
            if symbolIndex >= len(SYMBOLS):
                symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0:
                symbolIndex += len(SYMBOLS)
            translated += SYMBOLS[symbolIndex]
    return translated

#Completed
def ceasarCipher():
    mode = getMode()
    message = getMessage()
    key = getKey()
    print('\nYour translated text is:')
    print(ceasarTranslatedMessage(mode, message, key))

#Completed
def zigzagCipher():
    mode = getMode()
    message = getMessage()
    key = getKey()
    cipher = Zigzag()
    if mode == 'e' or mode == 'encrypt':
        enc = cipher.encrypt(message, key)
        print('\nYour translated text is:')
        print(enc)
    else:
        enc = cipher.decrypt(message, key, SYMBOLS)
        print('\nYour translated text is:')
        print(enc)

#Complete
def reverseCipher(): 
    mode = getMode()
    message = getMessage()
    if mode == 'e' or mode == 'encrypt':
        print('\nYour translated text is:')
        print(py.pycrypt.reverse_cipher(message))
    else:
        print('\nYour translated text is:')
        print(reverse_cipher(message))


#Completed
def trifidCipher():
    mode = getMode()
    message = getMessage()
    key = getKey()
    machine = CryptMachine(Trifid(), key)
    print('\nYour translated text is:')
    if mode == 'e' or mode == 'encrypt':
        enc = machine.encrypt(message)
        print(enc)
    else:
        enc = machine.decrypt(message)
        print(enc)

#TODO: key input
def affineCipher(): 
    mode = getMode()
    cipher = Affine()
    message = getMessage()
    print('\nYour translated text is:')
    if mode == 'e' or mode == 'encrypt':
        enc = cipher.encrypt(message, [7, 8], SYMBOLS)
        print(enc)
    else:
        enc = cipher.decrypt(message, [7, 8], SYMBOLS)
        print(enc)

#Completed
def vigenereCipher():
    mode = getMode()
    cipher = Vigenere()
    message = getMessage()
    key = getKeyString()
    print('\nYour translated text is:')
    if mode == 'e' or mode == 'encrypt':
        enc = cipher.encrypt(message, key, SYMBOLS)
        print(enc)
    else:
        enc = cipher.decrypt(message, key, SYMBOLS)
        print(enc)

def determineType():
    type = getType() 
    if type == '1':
        ceasarCipher()
    if type == '2':
        zigzagCipher()
    if type == '3':
        trifidCipher()
    if type == '4': 
        reverseCipher() 
    if type == '5': 
        affineCipher()
    if type == '6':
        vigenereCipher()

def main():
    print("\nWelcome to the StarCipher v1.0")
    determineType()
    restart = input("\nDo you want to restart the program? (y/n) > ")
    if str(restart) == str("y") or str(restart) == str('yes'):
        print('\nRestarting...')
        main()
    else:
        print("\nThe program will be closed.")

main()