def caesar_cipher(text, shift, encrypt=True):
    result = ""
    
    # Adjust the shift for decryption
    if not encrypt:
        shift = -shift
    
    # Loop through each character in the text
    for char in text:
        # Check if the character is an uppercase letter
        if char.isupper():
            # Find the position in the alphabet (0-25)
            # Shift the character and wrap around using modulo 26
            result += chr((ord(char) + shift - 65) % 26 + 65)
        # Check if the character is a lowercase letter
        elif char.islower():
            result += chr((ord(char) + shift - 97) % 26 + 97)
        else:
            # If it's not a letter, leave it as is
            result += char
    
    return result

# Get user input for the message, shift value, and operation
message = input("Enter the message: ")
shift = int(input("Enter the shift value: "))
choice = input("Do you want to encrypt or decrypt? (e/d): ").lower()

# Decide whether to encrypt or decrypt
if choice == 'e':
    encrypted_message = caesar_cipher(message, shift, encrypt=True)
    print("Encrypted message:", encrypted_message)
elif choice == 'd':
    decrypted_message = caesar_cipher(message, shift, encrypt=False)
    print("Decrypted message:", decrypted_message)
else:
    print("Invalid choice! Please enter 'e' for encryption or 'd' for decryption.")