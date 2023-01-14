# StarCipher (Written and Maintained by Wesley Reid - http://starhound.com) 

# ----- IMPORTS -----------------------------------------------------------
import py.pycrypt
import pyperclip
import secretpy.cmdecorators as md
from py.pycrypt import reverse_cipher, rot13_cipher
from secretpy import (Atbash, CryptMachine, MyszkowskiTransposition, Trifid,
                      Zigzag, Scytale, Keyword, Porta, alphabet)
# -------------------------------------------------------------------------

# ----- CONSTANTS ---------------------------------------------------------
out = ''
SYMBOLS = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'
MAX_KEY_SIZE = 24
# -------------------------------------------------------------------------

# ----- MAIN/STARTER FUNCTION ---------------------------------------------
def main():
    print("\nWelcome to the StarCipher v1.0")
    determineType()
    restart = input("\nDo you want to restart the program? (y/n) > ")
    if str(restart) == str("y") or str(restart) == str('yes'):
        print('\nRestarting...')
        main()
    else:
        print("\nThe program will be closed.")
# -------------------------------------------------------------------------

# ----- GET & HELPER FUNCTIONS --------------------------------------------
def getType():
    while True:
        type = """\nSelect cipher type: 
        (1) Ceasar 
        (2) Zig-Zag 
        (3) Trifid
        (4) Reverse
        (5) Atbash
        (6) Rot13
        (7) Myszkowski
        (8) Scytale
        (9) Keyword
        (0) Porta
        """
        mode = input().lower()
        type = type.replace('(', ' ').replace(')', ' ').lower()
        return mode if mode in type.split() else print('Please select value 1 through 6 for a cipher type.')
      
def determineType():
    type = getType() 
    if type == '1': out = ceasarCipher()
    if type == '2': out = zigzagCipher()
    if type == '3': out = trifidCipher()
    if type == '4':  out = reverseCipher() 
    if type == '5':  out = atbashCipher()
    if type == '6': out = rot13Cipher()
    if type == '7': out = myszkowskiCipher()
    if type == '8': out = scytaleCipher()
    if type == '9': out = keywordCipher()
    if type == '0': out = portaCipher()
    if out: copyPrompt(out)

# determineType helper function
def copyPrompt(message):
    print("\nCopy output to clipboard? (y/n)")
    mode = input().lower()
    if mode == 'y' or mode == 'yes':
        pyperclip.copy(message)
        spam = pyperclip.paste()
        print('Text copied to clipboard.')
                 
def getMode():
    while True:
        print('Do you wish to (e)ncrypt or (d)ecrypt a message?')
        mode = input().lower()
        str = 'Enter either "encrypt" or "e" or "decrypt" or "d".'
        return mode if mode in 'encrypt e decrypt d'.split() else print(str)

def getMessage():
     print('\nEnter your message:')
     return input()

# only takes number keys
def getKey():
     key = 0
     while True:
        print('\nEnter the key number (1-%s)' % (MAX_KEY_SIZE))
        key = int(input())
        if (key >= 1 and key <= MAX_KEY_SIZE): return key

#Some ciphers from secretpy expect string/letter based keys
def getKeyString():
     while True:
        print('\nEnter the key value (String Form):')
        key = input()
        if not hasNumbers(key): 
            return key if len(key) > 0 else print("\nPlease enter a key with at least one letter length.")
        else: 
             print('\nKey must be a string value.')

# helper function for getKeyString() 
def hasNumbers(inputString):
    return any(char.isdigit() for char in inputString)
# -------------------------------------------------------------------------

# ----- EXECUTE FUNCTIONS -------------------------------------------------
# only for ciphers from secretpy
def executeModeSecretPy(cipher, message):
    print('\nYour translated text is:')
    if mode == 'e' or mode == 'encrypt':
        out = cipher.encrypt(message)
    else:
        out = cipher.decrypt(message)
    print(out)
    return out
  
# only for ciphers from py.pycrypt
def executeModePycrypt(cipher, message, encrypt, decrypt):
    print('\nYour translated text is:')
    if mode == 'e' or mode == 'encrypt':
        out = encrypt
        print(out)
    else:
        out = decrypt
        print(out)
    return out

# -------------------------------------------------------------------------

# ----- PY.PYCRYPT CIPHERS ------------------------------------------------
def ceasarCipher():
    mode = getMode()
    message = getMessage()
    key = getKey()
    print('\nYour translated text is:')
    out = ceasarTranslatedMessage(mode, message, key)
    print(out)
    return out

# helper function for  ceasarCipher()
def ceasarTranslatedMessage(mode, message, key):
    if mode[0] == 'd': key = -key
    translated = ''
    for symbol in message:
        symbolIndex = SYMBOLS.find(symbol)	
        if symbolIndex != -1:
            symbolIndex += key
            if symbolIndex >= len(SYMBOLS): symbolIndex -= len(SYMBOLS)
            elif symbolIndex < 0: symbolIndex += len(SYMBOLS)
            translated += SYMBOLS[symbolIndex]
        else: 
            translated += symbol
    return translated

def reverseCipher(): 
    mode = getMode()
    message = getMessage()
    encrypt = py.pycrypt.reverse_cipher(message)
    decrypt = reverse_cipher(message)
    executeModePycrypt(cipher, message, encrypt, decrypt)
    return out
  
def rot13Cipher():
    mode = getMode()
    message = getMessage()
    encrypt = py.pycrypt.rot13_cipher(message)
    decrypt = rot13_cipher(message)
    executeModePycrypt(cipher, message, encrypt, decrypt)
    return out
# -------------------------------------------------------------------------

# ----- SECRETPY CIPHERS --------------------------------------------------
def zigzagCipher():
    mode = getMode()
    message = getMessage()
    key = getKey()
    cipher = CryptMachine(Zigzag(), key)
    executeModeSecretPy(cipher, message)
    return out

def trifidCipher():
    mode = getMode()
    message = getMessage()
    key = getKey()
    cipher = CryptMachine(Trifid(), key)
    executeModeSecretPy(cipher, message)
    return out

def atbashCipher(): 
    mode = getMode()
    message = getMessage()
    cipher = CryptMachine(Atbash())
    cipher = md.NoSpaces(md.UpperCase(cipher))
    executeModeSecretPy(cipher, message)
    return out

def myszkowskiCipher():
    mode = getMode()
    message = getMessage()
    key = getKeyString()
    cipher =  CryptMachine(MyszkowskiTransposition(), key)
    executeModeSecretPy(cipher, message)
    return out
  
def keywordCipher():
    mode = getMode()
    message = getMessage()
    key = getKeyString()
    cipher =  CryptMachine(Keyword(), key)
    executeModeSecretPy(cipher, message)
    return out
  
def portaCipher():
    mode = getMode()
    message = getMessage()
    key = getKeyString()
    cipher =  CryptMachine(Porta(), key)
    executeModeSecretPy(cipher, message)
    return out
# -------------------------------------------------------------------------

# ----- EXECUTE -----------------------------------------------------------      
if __name__ == '__main__':
    main()
# -------------------------------------------------------------------------      
