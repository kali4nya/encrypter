import os
from cryptography.fernet import Fernet

class colors:
    BLUE = '\033[94m'
    RESET = '\033[0m'

def decrypt_file(file_path, cipher):
    with open(file_path, 'rb') as f:
        encrypted_data = f.read()

    decrypted_data = cipher.decrypt(encrypted_data)

    with open(file_path, 'wb') as f:
        f.write(decrypted_data)

script_directory = os.path.dirname(os.path.abspath(__file__))

# Check if KEY.txt file exists
if os.path.exists("KEY.txt"):
    # Read the encryption key from KEY.txt
    with open("KEY.txt", "r") as key_file:
        encryption_key = key_file.read().encode()
    print("Encryption key read from KEY.txt.")
else:
    # Prompt the user to enter the encryption key
    encryption_key = input("Enter the encryption key: ").encode()

cipher = Fernet(encryption_key)

files_to_decrypt = [file for file in os.listdir(script_directory) if os.path.isfile(os.path.join(script_directory, file))]
files_to_decrypt = [file for file in files_to_decrypt if not (file.endswith('.py') or file == 'KEY.txt' or file == 'SAFETY_FILE')]

for file_name in files_to_decrypt:
    print(file_name)
    decrypt_file(os.path.join(script_directory, file_name), cipher)

print("")
if os.path.exists("KEY.txt"):
    try:
        os.remove("KEY.txt")
        print("KEY.txt has been deleted.")
    except Exception as e:
        print("An error occurred while deleting KEY.txt:", e)

if os.path.exists("SAFETY_FILE"):
    try:
        os.remove("SAFETY_FILE")
        print("SAFETY_FILE has been deleted.")
    except Exception as e:
        print("An error occurred while deleting SAFETY_FILE:", e)


print(colors.BLUE + "Decryption complete.")
input("Press Enter to exit...")
