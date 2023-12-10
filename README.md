# TextEncryption-Decryption

**PLEASE VIEW THIS readME as "CODE" OR DOWNLOAD TO SEE THE FULL FILE**
**REFERENCES PROVIDED AT THE BOTTOM OF THE FILE**

Description:

This script is designed to encrypt and decrypt messages using the Python cryptography library. This script provides a user-friendly interface to simplify the process. The script, when used for encrypting will accept parameters from the user like a message and file, and using the create_key function, which uses the "Fernet.generate_key()" method from the cryptography library generates a new key (Fernet keys are base64-encoded and used for Decryption and Encryption.), then using that key it creates a Fernet Cipher (A Fernet Cypher is a symmetric key encryption provided by the cryptography library.). The provided message is then encoded and encrypted using the cipher, the encrypted message is then written to the specified file using the w_file function. When used for Decrypting the script will accept a key and file parameter. The script uisng the r_file function will read the encrypted message contained in the provided file, then generates a Fernet cipher using the provided key. The encrypted message is then decrypted using the Fernet Cipher and displays the original message.

The w_file and r_file functions control the writing and reading of the data to and from the files. These functions use binary mode wb and rb for handling binary data and since our output is binary and needs to be store in files the wb and rb modes are used.

(************* Required Parameters and instructions on how they work will be listed in the USAGE GUIDE SECTION *************)

Depedencies & Installation instructions:

This Script makes use of the Python Cryptography module, please ensure installation of the Cryptography module before use

HOW TO INSTALL:

You can manually install the cryptography module via the Python Package index site - https://pypi.org/project/cryptography/#files

Or 

you can install with - pip install cryptography

Usage Guide:

The script makes use of the argparse library, users will provide arguments when running the script.

PLEASE NOTE: IN order to run this script you MUST be in the same directory as the EncryptDecrypt.py file

Required Parameters: The script checks for required parameters so if they aren't provided it will output a message notifying as such. In order to run this script it's required to be ran with either --encrypt or --decrypt and each option has it's own required Parameters.

Encryption - Required Parameters
--encrypt: Specifies the encryption operation.
--message: The message to be encrypted.
--file: The file to save the encrypted message.


How to run: python EncryptDecrypt.py --encrypt --message "Your message here" --file path/to/file

replacing "Your message here" and path/to/file with the desired file and message

Decryption - Required Parameters
--decrypt: Specifies the decryption operation.
--key: The key for decryption.
--file: The file containing the encrypted message.

How to run: python EncryptDecrypt.py --decrypt --key <insert_key_here> --file path/to/file

replacing <insert_key_here> with outputted key and path/to/file with the desired file


References:

https://thepythoncode.com/article/encrypt-decrypt-files-symmetric-python
https://pypi.org/project/cryptography/
https://chat.openai.com/
https://www.geeksforgeeks.org/encrypt-and-decrypt-files-using-python/




