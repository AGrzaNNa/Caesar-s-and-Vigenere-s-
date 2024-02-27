import unittest
from caesar_cipher import caesar_cipher, caesar_cipher_decrypt, caesar_cipher_decrypt_auto
from vigenere_cipher import vigenere_encrypt, vigenere_decrypt

class TestCiphers(unittest.TestCase):

    def test_caesar_cipher(self):
        plaintext = "dog"
        shift = 3
        expected_encrypted_text = "grj"
        self.assertEqual(caesar_cipher(plaintext, shift), expected_encrypted_text)

    def test_caesar_cipher_decrypt(self):
        encrypted_text = "grj"
        shift = 3
        expected_decrypted_text = "dog"
        self.assertEqual(caesar_cipher_decrypt(encrypted_text, shift), expected_decrypted_text)

    def test_caesar_cipher_decrypt_auto(self):
        encrypted_text = "grj"
        expected_decrypted_text = "dog"
        self.assertEqual(caesar_cipher_decrypt_auto(encrypted_text), expected_decrypted_text)

    def test_vigenere_cipher(self):
        plaintext = "dog"
        key = "key"
        expected_encrypted_text = "nse"
        self.assertEqual(vigenere_encrypt(plaintext, key), expected_encrypted_text)

    def test_vigenere_cipher_decrypt(self):
        encrypted_text = "nse"
        key = "key"
        expected_decrypted_text = "dog"
        self.assertEqual(vigenere_decrypt(encrypted_text, key), expected_decrypted_text)


