# Caesar-Cipher
A simple Python implementation of the Caesar Cipher for encryption and decryption.
# Caesar Cipher Encryption & Decryption

This project implements a simple **Caesar Cipher** algorithm that allows you to encrypt and decrypt text using a shift key.

## Features

- Encrypts and decrypts English letters (both uppercase and lowercase)
- Encrypts and decrypts numeric digits
- Handles special characters without modification
- Prevents invalid key values (only allows keys from 1 to 25)

## How It Works

- The user inputs a text string (English letters and numbers only)
- The user selects a shift key (between 1 and 25)
- The user chooses whether to encrypt or decrypt the text
- The program applies the Caesar Cipher algorithm and outputs the result

## Usage

1. Run the script
2. Enter the text you want to encrypt or decrypt
3. Enter a valid key (1-25)
4. Choose an operation:
   - Type `encrypt` or `1` for encryption
   - Type `decrypt` or `2` for decryption
5. The program will display the result

# Example

# Input:

```
Enter text (English letters and numbers only): Hello123
Select key for encryption (1 to 25): 3
Encryption or Decryption?
For Encryption, type "encrypt" or "1"
For Decryption, type "decrypt" or "2": encrypt
```

 Output:

```
Your text after encryption is: 'Khoor456'
```

 Requirements

- Python 3.x

 How to Run

```sh
python caesar_cipher.py
```

 Future Enhancements

- Add support for symbols and punctuation encryption
- Implement a graphical user interface (GUI)
- Support multiple languages
