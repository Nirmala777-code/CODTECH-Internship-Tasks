import hashlib

def get_hash(file_path):
    with open(file_path, 'rb') as file:
        data = file.read()
        return hashlib.sha256(data).hexdigest()

file_path = input("Enter full file path: ")
hash_value = get_hash(file_path)
print("SHA-256 Hash:", hash_value)