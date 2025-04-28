import unittest
from playfair import PlayfairCipher

class TestPlayfairCipher(unittest.TestCase):
    def setUp(self):
        self.cipher = PlayfairCipher("KEYWORD")

    def test_encrypt(self):
        encrypted_text = self.cipher.encrypt("HELLOWORLD")
        self.assertEqual(encrypted_text, "GYIZSCOKCFBU") 

    def test_decrypt(self):
        decrypted_text = self.cipher.decrypt("GYIZSCOKCFBU")
        self.assertEqual(decrypted_text, "HELXLOWORLDX") 

    def test_encrypt_with_repeated_characters(self):
        encrypted_text = self.cipher.encrypt("BALLOON")
        self.assertEqual(encrypted_text, "CBIZSCES") 

    def test_decrypt_with_repeated_characters(self):
        decrypted_text = self.cipher.decrypt("CBIZSCES")
        self.assertEqual(decrypted_text, "BALXLOON")  

    def test_encrypt_with_j(self):
        encrypted_text = self.cipher.encrypt("JUMP")
        self.assertEqual(encrypted_text, "GXNQ") 

    def test_decrypt_with_j(self):
        decrypted_text = self.cipher.decrypt("GXNQ")
        self.assertEqual(decrypted_text, "IUMP") 

if __name__ == "__main__":
    unittest.main()
