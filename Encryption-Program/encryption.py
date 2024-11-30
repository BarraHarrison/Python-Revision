import random
import string
import os
import json

# Define the file to store the key
KEY_FILE = "encryption_key.json"

# Create or load the key
def load_or_generate_key():
    characters = string.whitespace.replace("\n", "").replace("\r", "") + string.punctuation + string.digits + string.ascii_letters
    characters = list(characters)
    
    if os.path.exists(KEY_FILE):
        # Load the key from the file
        with open(KEY_FILE, "r") as file:
            key = json.load(file)
    else:
        # Generate a new key and save it
        key = characters.copy()
        random.shuffle(key)
        with open(KEY_FILE, "w") as file:
            json.dump(key, file)
    
    return characters, key

# Helper function for encryption
def encrypt_message(plain_text, characters, key):
    cipher_text = ""
    for letter in plain_text:
        if letter in characters:
            index = characters.index(letter)
            cipher_text += key[index]
        else:
            cipher_text += letter
    return cipher_text

# Helper function for decryption
def decrypt_message(cipher_text, characters, key):
    plain_text = ""
    for letter in cipher_text:
        if letter in key:
            index = key.index(letter)
            plain_text += characters[index]
        else:
            plain_text += letter
    return plain_text

# Load or generate the key
characters, key = load_or_generate_key()

# Encryption
plain_text = input("Enter a message to encrypt: ")
cipher_text = encrypt_message(plain_text, characters, key)

print(f"Original message: {plain_text}")
print(f"Encrypted message: {cipher_text}")

# Decryption
cipher_input = input("Enter a message to decrypt: ")
decrypted_message = decrypt_message(cipher_input, characters, key)

print(f"Encrypted message: {cipher_input}")
print(f"Decrypted message: {decrypted_message}")
