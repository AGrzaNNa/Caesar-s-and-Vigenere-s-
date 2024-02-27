# Import necessary functions
from caesar_cipher import *
from vigenere_cipher import *

def main_menu():
    while True:
        print("\nWelcome to Scrypt Panel!\n")
        print("1. Caesar Cipher")
        print("2. Vigenère Cipher")
        print("3. Exit")
        choice = input("Select option: ")

        if choice == '1':
            caesar_cipher_menu()
        elif choice == '2':
            vigenere_cipher_menu()
        elif choice == '3':
            print("Exiting...")
            break
        else:
            print("Invalid choice. Please select a valid option.")


def caesar_cipher_menu():
    while True:
        print("\n")
        print("1. Crypt code")
        print("2. Decrypt code")
        print("3. Back to main menu")
        choice = input("Select option: ")

        if choice == '1':
            encrypt_text()
        elif choice == '2':
            decrypt_text()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please select a valid option.")

def encrypt_text():
    input_text = input("\n""Write word: ")
    if validate_word(input_text):
        shift = int(input("Write shift: "))
        encrypted_text = caesar_cipher(input_text, shift)
        print("Encrypted text:", encrypted_text)
    else:
        print(f"The word '{input_text}' is not in the English dictionary.")


def decrypt_text():
    print("1. Decrypt code manually")
    print("2. Decrypt code automatically")
    choice = input("Select option: ")

    if choice == '1':
        input_text = input("\n""Write word: ")
        shift = int(input("Write shift: "))
        print("Decrypted text:", caesar_cipher_decrypt(input_text, shift))
    elif choice == '2':
        input_text = input("\n""Write word: ")
        print("Decrypted text:", caesar_cipher_decrypt_auto(input_text))
    else:
        print("Invalid choice")


def vigenere_cipher_menu():
    while True:
        print("\n")
        print("1. Crypt code")
        print("2. Decrypt code")
        print("3. Back to main menu")
        choice = input("Select option: ")

        if choice == '1':
            encrypt_text_vigenere()
        elif choice == '2':
            decrypt_text_vigenere()
        elif choice == '3':
            break
        else:
            print("Invalid choice. Please select a valid option.")


def encrypt_text_vigenere():
    plaintext = input("\n""Write word: ")
    if validate_word(plaintext):
        key = input("Write key: ")
        print("Encrypted text:", vigenere_encrypt(plaintext, key))
    else:
        print(f"The word '{plaintext}' is not in the English dictionary.")


def decrypt_text_vigenere():
    print("1. Decrypt code manually")
    print("2. Decrypt code automatically")
    choice = input("Select option: ")
    if choice == '1':
        plaintext = input("\n""Write word: ")
        key = input("Write key: ")
        print("Decrypted text:", vigenere_decrypt(plaintext, key))
    elif choice == '2':
        ciphertext = input("\n""Write word: ")
        print("Decrypted text:", break_vigenere(ciphertext, 3))
    else:
        print("Invalid choice")


if __name__ == "__main__":
    main_menu()
