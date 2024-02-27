from helper_functions import validate_word

def caesar_cipher(sample, move):
    encrypted_text = ''
    for char in sample:
        if char.isalpha():  # Check if the character is an alphabet letter
            shifted_char = chr((ord(char.lower()) - 97 + move) % 26 + 97)
            if char.isupper():
                shifted_char = shifted_char.upper()
            encrypted_text += shifted_char
    return encrypted_text


def caesar_cipher_decrypt(sample, move):
    # Using caesar_cipher_encrypt func in opposite shift
    return caesar_cipher(sample, -move)


def caesar_cipher_decrypt_auto(ciphertext):
    # Decrypt code in every shift from range
    for shift in range(26):
        decrypted_text = caesar_cipher_decrypt(ciphertext, shift)
        words_list = decrypted_text.split()  # Save decrypted_text to list
        for word in words_list:
            if validate_word(word):
                return decrypted_text