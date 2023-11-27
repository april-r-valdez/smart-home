import sys
from Encryption import Encryption

class VigenereCipher(Encryption):
    mod = 26
    key = None
    
    
    def __init__(self, keyValue, 
                 modValue=26, 
                 removeSpace=True,          # Remove space
                 encryptSpace=False,         # Encrypt Space
                 encryptSymbol=False,        # Encypt Symbol
                 upperCaseAll=True,        # Uppercase ALL
                 reverseText = False    # Reverse Plain text
                 ) -> None:
        super().__init__(removeSpace, encryptSpace, encryptSymbol, upperCaseAll, reverseText)
        self.mod = modValue
        
        if not keyValue:
            print("Error need to provide key")
            sys.exit()        
        self.key = keyValue    
        self.name = "Vigenere Cipher"
    
        
    def encrypt(self, plainText):
        cleaned_plainText, indexToSkip = self.applySettings(plainText)    # Apply settings according to specification         
        cipherText = ""
        for i, char in enumerate(cleaned_plainText):
            if i not in indexToSkip:
                sub = chr(((ord(char.upper()) + ord(self.key[i % len(self.key)].upper())) % self.mod) + ord('A'))
                if char.islower():
                    cipherText += sub.lower() 
                else:
                    cipherText += sub
            else:
                cipherText += char                 
        return cipherText
    
    
    def decrypt(self, plainText):
        cleaned_cipherText, indexToSkip = self.applySettings(plainText)    # Apply settings according to specification         
        plainText = ""
        for i, char in enumerate(cleaned_cipherText):
            if i not in indexToSkip:
                sub = chr(((ord(char.upper()) - ord(self.key[i % len(self.key)].upper())) % self.mod) + ord('A'))
                if char.islower():
                    plainText += sub.lower() 
                else:
                    plainText += sub
            else:
                plainText += char                 
        return plainText