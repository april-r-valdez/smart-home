from encryption import Encryption

class CaesarCipher(Encryption):
    shift = 13 # default to ROT13
    mod = 26
    
    def __init__(self, shiftValue,
                 modValue = 26, 
                 removeSpace=True,          # Remove space
                 encryptSpace=False,         # Encrypt Space
                 encryptSymbol=False,        # Encypt Symbol
                 upperCaseAll=True,        # Uppercase ALL
                 reverseText = False    # Reverse Plain text
                 ) -> None:
        super().__init__(removeSpace, encryptSpace, encryptSymbol, upperCaseAll, reverseText)
        self.shift = shiftValue
        self.mod = modValue
        self.name = "Ceasar Cipher"
     
        
    def encrypt(self, plainText):
        cleaned_plainText, indexToSkip = self.applySettings(plainText)    # Apply settings according to specification
        
        cipherText = ""
        for i, char in enumerate(cleaned_plainText):
            if i not in indexToSkip:
                if char.islower():
                    cipherText += chr(((ord(char) - ord('a') + self.shift) % self.mod) + ord('a'))
                else:
                    cipherText += chr(((ord(char) - ord('A') + self.shift) % self.mod) + ord('A')) 
            else:
                cipherText += char 
                
        return cipherText             


    def decrypt(self, cipherText):
        cleaned_cipherText, indexToSkip = self.applySettings(cipherText)
        
        plainText = ""
        
        for i, char in enumerate(cleaned_cipherText):
            if i not in indexToSkip:
                if char.islower():
                    plainText += chr(((ord(char) - ord('a') - self.shift) % self.mod) + ord('a'))
                else:
                    plainText += chr(((ord(char) - ord('A') - self.shift) % self.mod) + ord('A')) 
            else:
                plainText += char
                
        return plainText