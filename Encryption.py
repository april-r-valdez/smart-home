from abc import abstractmethod

class Encryption:
    upperCaseAll = None
    removeSpace = None
    encryptSpace = None
    encryptSymbol = None
    reverseText = None
    name = "Main"
    
    def __init__(self, removeSpace=True, encryptSpace=False, encryptSymbol=False, upperCaseAll=True, reverseText=False) -> None:
        self.removeSpace = removeSpace
        self.encryptSpace = encryptSpace
        self.encryptSymbol = encryptSymbol
        self.upperCaseAll = upperCaseAll
        self.reverseText = reverseText
    
    def describe(self):
        return {
            "name" : self.name 
        }
        
    def getSettings(self):
        return {
            "Space Removed" : self.removeSpace,
            "Space Encrypt" : self.encryptSpace,
            "Symbol Encrypt" : self.encryptSymbol
        }
    
    
    # Returns cleaned plaintext and indexes to skip  
    def applySettings(self, plainText):
        if self.removeSpace:
            plainText = self.deleteSpace(plainText) 
        
        if self.upperCaseAll:
            plainText = self.convertToUppercase(plainText)
            
        if self.reverseText:
            plainText = self.reverseString(plainText)
            
        return plainText, [i for i, char in enumerate(plainText) if not char.isalpha()]
            
    @abstractmethod 
    def encrypt(self, plainText):
        pass
    
    @abstractmethod
    def decrypt(self, cipherText):
        pass
    
    def deleteSpace(self, plainText):
        return plainText.replace(" ", "")
    
    def convertToUppercase(self, plainText):
        return plainText.upper()
    
    def reverseString(self, text):
        return ''.join(reversed(text))