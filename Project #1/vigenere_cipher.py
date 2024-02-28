import itertools
from helper_functions import validate_word


def vigenere_encrypt(plain_text, key):
    encrypted_text = ''
    key_index = 0
    for char in plain_text:
        if char.isalpha(): # Check if the character is an alphabet letter
            shift = ord(key[key_index % len(key)]) - 97
            encrypted_char = chr((ord(char.lower()) - 97 + shift) % 26 + 97)
            encrypted_text += encrypted_char
            key_index += 1
        else:
            encrypted_text += char
    return encrypted_text


def vigenere_decrypt(encrypted_text, key):
    decrypted_text = ''
    key_index = 0
    for char in encrypted_text:
        if char.isalpha(): # Check if the character is an alphabet letter
            shift = ord(key[key_index % len(key)]) - 97
            encrypted_char = chr((ord(char.lower()) - 97 - shift) % 26 + 97)
            decrypted_text += encrypted_char
            key_index += 1
        else:
            decrypted_text += char
    return decrypted_text

def break_vigenere(ciphertext, keyword_length):
    # Generate all possible combinations of three-digit ASCII keys
    possible_keys = itertools.product(range(97, 123), repeat=keyword_length)

    # Convert ciphertext to lowercase for consistency
    ciphertext = ciphertext.lower()

    unique_results = {}

    for key in possible_keys:
        decrypted_text = ''
        key_str = ''.join(chr(k) for k in key)

        # Decrypt the text using the current key
        for i in range(len(ciphertext)):
            shift = ord(key_str[i % keyword_length]) - 97
            decrypted_char = chr((ord(ciphertext[i]) - shift - 97) % 26 + 97)
            decrypted_text += decrypted_char

        # Check if word already exists in dic
        if validate_word(decrypted_text):
            if decrypted_text not in unique_results:
                unique_results[decrypted_text] = key_str

    return unique_results