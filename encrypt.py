from cryptography.fernet import Fernet

def get_key():
    return Fernet.generate_key()

def encrypt_text_file(filename, key):
    with open(filename, 'rb') as f:
        data = f.read()
    
    cipher = Fernet(key)
    encrypted = cipher.encrypt(data)

    with open("encrypted_" + filename, 'wb') as f:
        f.write(encrypted)

    print("File encrypted!")

def decrypt_text_file(filename, key):
    with open(filename, 'rb') as f:
        encrypted_data = f.read()
    
    cipher = Fernet(key)
    decrypted = cipher.decrypt(encrypted_data)

    with open("decrypted_" + filename, 'wb') as f:
        f.write(decrypted)

    print("File decrypted!")

# run
choice = input("Encrypt or Decrypt? (e/d): ").lower()
file = input("File name: ")

if choice == 'e':
    key = get_key()
    print("Save this key somewhere safe:", key.decode())
    encrypt_text_file(file, key)
elif choice == 'd':
    user_key = input("Enter your key: ").encode()
    decrypt_text_file(file, user_key)
else:
    print("Invalid choice")
