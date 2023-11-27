from Encryption import Encryption

class CaesarCipher(Encryption):
    shift = 13 # default to ROT13
    mod = 256
    
    def __init__(self, shiftValue,
                 modValue = 256, 
                 removeSpace=False,          # Remove space
                 encryptSpace=True,         # Encrypt Space
                 encryptSymbol=True,        # Encypt Symbol
                 upperCaseAll=True,        # Uppercase ALL
                 reverseText = False    # Reverse Plain text
                 ) -> None:
        super().__init__(removeSpace, encryptSpace, encryptSymbol, upperCaseAll, reverseText)
        self.shift = shiftValue
        self.mod = modValue
        self.name = "Ceasar Cipher"
     
        
    def encrypt(self, plainText):
        cleaned_plainText, indexToSkip = self.applySettings(plainText)

        cipherText = ""
        for i, char in enumerate(cleaned_plainText):
            if i not in indexToSkip:
                cipherText += chr((ord(char) + self.shift) % self.mod)
            else:
                cipherText += str(char)

        return cipherText

    def decrypt(self, cipherText):
        cleaned_cipherText, indexToSkip = self.applySettings(cipherText)

        plainText = ""
        for i, char in enumerate(cleaned_cipherText):
            if i not in indexToSkip:
                plainText += chr((ord(char) - self.shift) % self.mod)
            else:
                plainText += char

        return plainText
