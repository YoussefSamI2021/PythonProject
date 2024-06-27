class CaesarCipher:
    
    def __init__(self):
        self.key = None
        self.antikey = None

    def set_key(self, key):
        self.key = key
        self.antikey = {v: k for k, v in self.key.items()}

    def encrypt_string(self, string):
        self.check_input(string)
        encrypted = ""
        for char in string:
            if char.isalpha():
                encrypted += self.key.get(char.lower(), char)
            else:
                encrypted += char
        return encrypted

    def decrypt_string(self, string):
        decrypted = ""
        for char in string:
            if char.isalpha():
                decrypted += self.antikey.get(char.lower(), char)
            else:
                decrypted += char
        return decrypted
    

    def check_input(self, string):
        if not all(char.isalpha() or char.isspace() for char in string):
            raise ValueError("Invalid input: Only alphabets and spaces allowed")

    @classmethod
    def get_cipher(cls, cistring, key, encrypt: bool):
        cipher = cls()
        cipher.set_key(key)
        if encrypt :
            return cipher.encrypt_string(cistring)
        else : 
            return cipher.decrypt_string(cistring)
        
        
