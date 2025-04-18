from cryptography.fernet import Fernet
import os

def generate_key():
    return Fernet.generate_key()

def load_key_from_input():
    key_input = input("Enter your key: ").strip()
    try:
        return key_input.encode()
    except:
        print("Invalid key format.")
        return None

def encrypt_file(input_file, output_file, key):
    try:
        fernet = Fernet(key)
        with open(input_file, 'rb') as file:
            original_data = file.read()
        encrypted_data = fernet.encrypt(original_data)
        with open(output_file, 'wb') as file:
            file.write(encrypted_data)
        print(f"File encrypted successfully and saved as {output_file}")
    except Exception as e:
        print(f"Encryption failed: {e}")

def decrypt_file(input_file, output_file, key):
    try:
        fernet = Fernet(key)
        with open(input_file, 'rb') as file:
            encrypted_data = file.read()
        decrypted_data = fernet.decrypt(encrypted_data)
        with open(output_file, 'wb') as file:
            file.write(decrypted_data)
        print(f"File decrypted successfully and saved as {output_file}")
    except Exception as e:
        print(f"Decryption failed: {e}")

def main():
    print("=== File Encryption/Decryption Tool ===")
    print("1. Generate Key")
    print("2. Encrypt File")
    print("3. Decrypt File")
    choice = input("Choose an option (1/2/3): ").strip()

    if choice == '1':
        key = generate_key()
        print(f"Your secret key (keep it safe!):\n{key.decode()}")
    elif choice in ['2', '3']:
        key = load_key_from_input()
        if key is None:
            return

        input_file = input("Enter path to input file: ").strip()
        output_file = input("Enter path to save output file: ").strip()

        if not os.path.exists(input_file):
            print("Input file does not exist.")
            return

        if choice == '2':
            encrypt_file(input_file, output_file, key)
        else:
            decrypt_file(input_file, output_file, key)
    else:
        print("Invalid option.")

if __name__ == "__main__":
    main()
