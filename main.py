import os
import json
import hashlib
import random
import string
import base64
from cryptography.fernet import Fernet

# Function to generate a random wallet address
def generate_wallet_address():
    """Generate a random wallet address."""
    return '0x' + ''.join(random.choices(string.hexdigits, k=40))

# Function to generate a secure encryption key
def generate_encryption_key():
    """Generate a secure key for encryption."""
    return Fernet.generate_key()

# Function to save the encryption key securely
def save_encryption_key(key, filename):
    """Save the encryption key to a file."""
    with open(filename, 'wb') as key_file:
        key_file.write(key)
    print("Encryption key saved successfully!")

# Function to load the encryption key
def load_encryption_key(filename):
    """Load the encryption key from a file."""
    with open(filename, 'rb') as key_file:
        return key_file.read()

# Function to encrypt data
def encrypt_data(data, key):
    """Encrypt the given data using the provided key."""
    f = Fernet(key)
    encrypted_data = f.encrypt(data.encode())
    return encrypted_data

# Function to decrypt data
def decrypt_data(encrypted_data, key):
    """Decrypt the given data using the provided key."""
    f = Fernet(key)
    decrypted_data = f.decrypt(encrypted_data).decode()
    return decrypted_data

# Function to create a new wallet
def create_wallet():
    """Create a new cryptocurrency wallet."""
    address = generate_wallet_address()
    private_key = generate_encryption_key()
    wallet_data = {
        "address": address,
        "private_key": base64.urlsafe_b64encode(private_key).decode()
    }
    return wallet_data

# Function to save wallet data to file
def save_wallet_to_file(wallet_data, filename):
    """Save wallet data to a JSON file."""
    with open(filename, 'w') as wallet_file:
        json.dump(wallet_data, wallet_file)
    print("Wallet data saved successfully!")

# Function to load wallet data from file
def load_wallet_from_file(filename):
    """Load wallet data from a JSON file."""
    with open(filename, 'r') as wallet_file:
        return json.load(wallet_file)

# Function to display wallet details
def display_wallet(wallet_data):
    """Display wallet address and private key."""
    print(f"Wallet Address: {wallet_data['address']}")
    print(f"Private Key: {wallet_data['private_key']}")

# Function to create and encrypt a wallet
def create_and_encrypt_wallet():
    """Create and encrypt a new wallet."""
    wallet_data = create_wallet()
    filename = input("Enter filename to save wallet data: ")
    key = generate_encryption_key()
    save_encryption_key(key, "encryption_key.key")
    encrypted_private_key = encrypt_data(wallet_data["private_key"], key)
    wallet_data["private_key"] = encrypted_private_key.decode()
    save_wallet_to_file(wallet_data, filename)

# Function to load and decrypt a wallet
def load_and_decrypt_wallet():
    """Load and decrypt an existing wallet."""
    filename = input("Enter filename of wallet data: ")
    wallet_data = load_wallet_from_file(filename)
    key = load_encryption_key("encryption_key.key")
    decrypted_private_key = decrypt_data(wallet_data["private_key"].encode(), key)
    wallet_data["private_key"] = decrypted_private_key
    display_wallet(wallet_data)

# Main function to run the wallet application
def main():
    """Main function for cryptocurrency wallet application."""
    while True:
        print("\n--- Cryptocurrency Wallet ---")
        print("1. Create and Encrypt Wallet")
        print("2. Load and Decrypt Wallet")
        print("3. Exit")
        choice = input("Choose an option: ")
        if choice == '1':
            create_and_encrypt_wallet()
        elif choice == '2':
            load_and_decrypt_wallet()
        elif choice == '3':
            print("Exiting application. Goodbye!")
            break
        else:
            print("Invalid option. Please try again.")

# Run the main function if this script is executed
if __name__ == "__main__":
    main()
