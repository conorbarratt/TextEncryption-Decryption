#ConorBarratt 000830777
from cryptography.fernet import Fernet # For encyption and decryption
import argparse # For parsing command line arguments
import os # For interacting with the OS

# Generating a Fernet key for encryption/decryption
def create_key():
    return Fernet.generate_key()

# Writing encrypted message to file
def w_file(filename, data):
    with open(filename, 'wb') as file:
        file.write(data)

# Reading encrypted message from file
def r_file(filename):
    with open(filename, 'rb') as file:
        return file.read()

# Encrypts the provided message and writes to file specified
def e_message(message, output_file):
    key = create_key() # Generated key
    cipher = Fernet(key) # Creates a Fernet cipher using the key
    encrypted_message = cipher.encrypt(message.encode()) # Encrypts the message 
    w_file(output_file, encrypted_message) # Uses the w_file function to write the encrypted message to the file
    print(f"Message encrypted and written to {output_file}") # Output showing the message was and encrypted and what file it was written to
    print(f"Generated Key: {key.decode()}") # Outputs generated key

# Decrypts the message from the provided file using provided key
def d_message(key, file_name):
    encrypted_message = r_file(file_name) # Uses the r_file function to to read the encrypted message from the provided file
    cipher = Fernet(key) # Creates a Fernet cipher using the provided key
    decrypted_message = cipher.decrypt(encrypted_message).decode() # Decrypts the message
    print(f"Decrypted Message: {decrypted_message}") # Outputs decrypted message 

# Sets up a command-line interface using argparse for encrypting and decrypting messages.
# Defines command-line arguments such as message, key, file, encryption, and decryption options.
def encrypt_decrypt():
    parser = argparse.ArgumentParser(description='Encrypt and decrypt messages.')
    # Defining command-line arguments
    parser.add_argument('--message', help='The message to be encrypted.')
    parser.add_argument('--key', help='The key used for encryption or decryption.')
    parser.add_argument('--file', help='The file to read from or write to.')
    parser.add_argument('--encrypt', action='store_true', help='Encrypt the provided message.')
    parser.add_argument('--decrypt', action='store_true', help='Decrypt the message from the file.')

    args = parser.parse_args()

    if args.encrypt:
        # Checking if both message and file are provided when encrypting
        if not args.message or not args.file:
            print("Error: Both --message and --file are required for encryption.")
            return
        
        # Performing encryption with provided Arguments (Message and File)
        e_message(args.message, args.file)

    elif args.decrypt:
        # Checking if both key and file are provided for decrpytion 
        if not args.key or not args.file:
            print("Error: --key and --file are required for decryption.")
            return
        
        # Checking if the specified file exists
        if not os.path.exists(args.file):
            print(f"Error: File '{args.file}' not found.")
            return

        # Performing decyption with provided Arguments (Key and File)
        key = args.key.encode()
        file_name = args.file
        d_message(key, file_name)

    else:
        # Encrypt or Decrypt was specified
        print("Error: Either --encrypt or --decrypt must be specified.")
        return

#  Calls the main function (encrypt_decrypt) to execute the encryption or decryption operation based on the provided command-line arguments.
if __name__ == '__main__':
    encrypt_decrypt()
