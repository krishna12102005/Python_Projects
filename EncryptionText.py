import random
import string


encrypt_String = " " +string.digits + string.ascii_letters + string.punctuation

chars = list(encrypt_String)
keys = chars.copy()

random.shuffle(keys)


#Encryption
plain_text = input("Enter the Original word: ")
cipher_text = ""

for letter in plain_text:
    index = chars.index(letter)
    cipher_text += keys[index]


print(f"Your original text : {plain_text}")
print(f"Your cipher_text :{cipher_text}")


#Decryption
cipher = input("Enter the ciphertext: ")
original = ""

for let in cipher:
    index = keys.index(let)
    original+= chars[index]


print(f"Your cipher text is : {cipher}")
print(f"Your original text is :{original}")