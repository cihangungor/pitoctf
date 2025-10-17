import string
import random

class Encryption:

    chars = (string.ascii_letters + string.digits + string.punctuation) * 1000
    keychars = string.ascii_letters

    def KeyEncrypt(self, m:str, key=None):
        if key == None:
            key = self.RandomKey(len(m))

        encryptedOutput = ""
        for keychar, char in zip(key,m):
            encryptedOutput += self.chars[self.chars.index(char) + self.chars.index(keychar) ]

        return encryptedOutput

    def RandomKey(self, lenght:int):
        key = ""

        for i in range(lenght):
            char = random.choice(self.keychars)
            key = key + char

        return key