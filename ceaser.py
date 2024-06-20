def caesar_cipher_encrypt(text, shift):
    encrypted_text = ""
    for char in text:
        if char.isalpha():
            shift_base = 65 if char.isupper() else 97
            encrypted_char = chr((ord(char) - shift_base + shift) % 26 + shift_base)
            encrypted_text += encrypted_char
        else:
            encrypted_text += char
    return encrypted_text

def caesar_cipher_decrypt(text, shift):
    return caesar_cipher_encrypt(text, -shift)

def main():
    print("Caesar Cipher Program")
    while True:
        choice = input("Do you want to encrypt or decrypt a message? (e/d) or 'q' to quit: ").lower()
        if choice == 'q':
            print("Exiting the program.")
            break
        if choice not in ('e', 'd'):
            print("Invalid choice! Please select 'e' for encryption, 'd' for decryption, or 'q' to quit.")
            continue

        message = input("Enter your message: ")
        shift = int(input("Enter the shift value: "))

        if choice == 'e':
            result = caesar_cipher_encrypt(message, shift)
            print(f"Encrypted Message: {result}")
        else:
            result = caesar_cipher_decrypt(message, shift)
            print(f"Decrypted Message: {result}")

if __name__ == "__main__":
    main()
