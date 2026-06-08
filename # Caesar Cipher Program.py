message = input("Enter your message: ")
shift = int(input("Enter shift value: "))

encrypted_message = ""

for letter in message:
    if letter.isalpha():
        if letter.isupper():
            encrypted_message += chr((ord(letter) - 65 + shift) % 26 + 65)
        else:
            encrypted_message += chr((ord(letter) - 97 + shift) % 26 + 97)
    else:
        encrypted_message += letter

print("\nEncrypted message:", encrypted_message)

decrypted_message = ""

for letter in encrypted_message:
    if letter.isalpha():
        if letter.isupper():
            decrypted_message += chr((ord(letter) - 65 - shift) % 26 + 65)
        else:
            decrypted_message += chr((ord(letter) - 97 - shift) % 26 + 97)
    else:
        decrypted_message += letter

print("Decrypted message:", decrypted_message)