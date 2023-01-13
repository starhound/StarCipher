# StarCipher (Written and Maintained by Wesley Reid - http://starhound.com) 

import py.pycrypt
import pyperclip
import secretpy.cmdecorators as md
from py.pycrypt import reverse_cipher, rot13_cipher
from secretpy import (Atbash, CryptMachine, MyszkowskiTransposition, Trifid,
                      Zigzag, Scytale, Keyword, Porta, alphabet)

out = ''

SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = 24


def getType():
    while True:
        print("""\nSelect cipher type: 
        (1) Ceasar 
        (2) Zig-Zag 
        (3) Trifid
        (4) Reverse
        (5) Atbash
        (6) Rot13
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
    out = ceasarTranslatedMessage(mode, message, key)
    print(out)
    return out

#Completed
def zigzagCipher():
    mode = getMode()
    message = getMessage()
    key = getKey()
    cipher = Zigzag()
    print('\nYour translated text is:')
    if mode == 'e' or mode == 'encrypt':
        out = cipher.encrypt(message, key)
        print(out)
    else:
        out = cipher.decrypt(message, key, SYMBOLS)
        print(out)
    return out

#Complete
def reverseCipher(): 
    mode = getMode()
    message = getMessage()
    print('\nYour translated text is:')
    if mode == 'e' or mode == 'encrypt':
        out = py.pycrypt.reverse_cipher(message)
        print(out)
    else:
        out = reverse_cipher(message)
        print(out)
    return out


#Completed
def trifidCipher():
    mode = getMode()
    message = getMessage()
    key = getKey()
    machine = CryptMachine(Trifid(), key)
    print('\nYour translated text is:')
    if mode == 'e' or mode == 'encrypt':
        out = machine.encrypt(message)
        print(out)
    else:
        out = machine.decrypt(message)
        print(out)
    return out

#TODO: key input
def atbashCipher(): 
    mode = getMode()
    message = getMessage()
    cm = CryptMachine(Atbash())
    cm = md.NoSpaces(md.UpperCase(cm))
    print('\nYour translated text is:')
    if mode == 'e' or mode == 'encrypt':
        out = cm.encrypt(message)
        print(out)
    else:
        out = cm.decrypt(message)
        print(out)
    return out

#Completed
def rot13Cipher():
    mode = getMode()
    message = getMessage()
    print('\nYour translated text is:')
    out = '' 
    if mode == 'e' or mode == 'encrypt':
        out = py.pycrypt.rot13_cipher(message)
        print(out)
    else:
        out = rot13_cipher(message)
        print(out)
    return out

def copyPrompt(message):
    print("\nCopy output to clipboard? (y/n)")
    mode = input().lower()
    if mode == 'y' or mode == 'yes':
        pyperclip.copy(message)
        spam = pyperclip.paste()
        print('Text copied to clipboard.')

def determineType():
    type = getType() 
    if type == '1':
        out = ceasarCipher()
    if type == '2':
        out = zigzagCipher()
    if type == '3':
        out = trifidCipher()
    if type == '4': 
        out = reverseCipher() 
    if type == '5': 
        out = atbashCipher()
    if type == '6':
        out = rot13Cipher()
    if out:
        copyPrompt(out)

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
