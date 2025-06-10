from cryptography.fernet import Fernet

# Generate key and save to file
def generate_key():
    key = Fernet.generate_key()
    with open("key.key", "wb") as key_file:
        key_file.write(key)
    print("✅ Key generated and saved as key.key")

# Load the key from file
def load_key():
    return open("key.key", "rb").read()

# Encrypt the file
def encrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        data = file.read()
    encrypted = fernet.encrypt(data)
    with open(file_path + ".enc", "wb") as file:
        file.write(encrypted)
    print("✅ File encrypted successfully!")

# Decrypt the file
def decrypt_file(file_path):
    key = load_key()
    fernet = Fernet(key)
    with open(file_path, "rb") as file:
        data = file.read()
    decrypted = fernet.decrypt(data)
    with open(file_path.replace(".enc", "_decrypted.txt"), "wb") as file:
        file.write(decrypted)
    print("✅ File decrypted successfully!")

# Main menu
def main():
    print("=== Advanced Encryption Tool ===")
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    choice = input("Choose option (1/2/3): ")

    if choice == "1":
        generate_key()
    elif choice == "2":
        path = input("Enter full path of file to encrypt: ")
        encrypt_file(path)
    elif choice == "3":
        path = input("Enter full path of encrypted file (.enc): ")
        decrypt_file(path)
    else:
        print("❌ Invalid option.")

main()