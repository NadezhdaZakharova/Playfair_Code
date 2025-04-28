import string

class PlayfairCipher:
    def __init__(self, key):
        self.key = self.prepare_key(key)
        self.matrix = self.create_matrix(self.key)

    def prepare_key(self, key):
        key = key.upper().replace("J", "I")
        key = ''.join(sorted(set(key), key=lambda x: key.index(x)))
        return key

    def create_matrix(self, key):
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ" 
        matrix = []
        for char in key:
            if char not in matrix:
                matrix.append(char)
        for char in alphabet:
            if char not in matrix:
                matrix.append(char)
        return [matrix[i:i + 5] for i in range(0, 25, 5)]

    def find_position(self, char):
        for i, row in enumerate(self.matrix):
            if char in row:
                return i, row.index(char)
        return None

    def encrypt_pair(self, a, b):
        row1, col1 = self.find_position(a)
        row2, col2 = self.find_position(b)

        if row1 == row2:  
            return self.matrix[row1][(col1 + 1) % 5] + self.matrix[row2][(col2 + 1) % 5]
        elif col1 == col2:  
            return self.matrix[(row1 + 1) % 5][col1] + self.matrix[(row2 + 1) % 5][col2]
        else:  
            return self.matrix[row1][col2] + self.matrix[row2][col1]

    def encrypt(self, plaintext):
        plaintext = plaintext.upper().replace("J", "I").replace(" ", "")
        pairs = []
        
        i = 0
        while i < len(plaintext):
            a = plaintext[i]
            b = plaintext[i + 1] if (i + 1) < len(plaintext) else 'X'
            if a == b:  
                pairs.append((a, 'X'))
                i += 1
            else:
                pairs.append((a, b))
                i += 2
        
        ciphertext = ''.join(self.encrypt_pair(a, b) for a, b in pairs)
        return ciphertext

    def decrypt_pair(self, a, b):
        row1, col1 = self.find_position(a)
        row2, col2 = self.find_position(b)

        if row1 == row2:  
            return self.matrix[row1][(col1 - 1) % 5] + self.matrix[row2][(col2 - 1) % 5]
        elif col1 == col2:  
            return self.matrix[(row1 - 1) % 5][col1] + self.matrix[(row2 - 1) % 5][col2]
        else:  
            return self.matrix[row1][col2] + self.matrix[row2][col1]

    def decrypt(self, ciphertext):
        if len(ciphertext) % 2 != 0:
            ciphertext += 'X'

        pairs = [(ciphertext[i], ciphertext[i + 1]) for i in range(0, len(ciphertext), 2)]
        
        plaintext = ''.join(self.decrypt_pair(a, b) for a, b in pairs)
        
        return plaintext

