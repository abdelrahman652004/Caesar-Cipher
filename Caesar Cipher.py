""" 
 ord('A') -> 65
 chr(65) -> 'A'
 
"""
def caesar_cipher(text,key,encrypt=True):
 key = -key if not encrypt else key
 encrypted_text = ""
 for char in text:
  if char.isalpha():
   base = ord('A') if char.isupper() else ord('a')
   encrypted_text += chr(base + (ord(char) - base + key) % 26)
  elif char.isdigit():
   encrypted_text += num_encrypt(char, key) if encrypt else num_decrypt(char, key)
  else: 
   encrypted_text += char 
  
 return encrypted_text
  

def num_encrypt(num,key):
 encrypted_num = str((int(num) + key) % 10)
 return encrypted_num

def num_decrypt(num,key):
  decrypted_num = str((int(num) - key + 10) % 10)
  return decrypted_num

text = input("Enter text (only English letters): ")
key  = int(input("Select key to encryption from 1 to 25 : "))
if key == 0 or key == 26:
    print("Warning: Key must be between 1 and 25.")
    exit()
elif not key.isdigit():
    print("Warning: Invalid input key must be number")
    exit()
operation = input("""Encryption or Decryption ?\n
                     for Encryption type encrypt or 1 \n
                     for Decryption type dncrypt or 2\n: """)

if operation.lower() == "encrypt" or operation == "1":
 encrypted_text = caesar_cipher(text,key)
 print(f"your text after encryption is '{encrypted_text}'")
elif operation.lower() == "decrypt" or operation == "2":
 decrypted_text = caesar_cipher(text,key,False)
 print(f"your text after decryption is '{decrypted_text}'")
else:
 print("Invalid Input")
