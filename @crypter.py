import os
from cryptography.fernet import Fernet

class colors:
    BLUE = '\033[94m'
    RESET = '\033[0m'
    RED = '\033[91m'

script_directory = os.path.dirname(os.path.abspath(__file__))

if os.path.exists(script_directory + "\\" + "SAFETY_FILE"):
    print(colors.RED + "WATCH OUT - SAFETY_FILE ALREADY EXISTS")
    print(colors.RED + "FILES ARE PROPABLY ALREADY ENCRYPTED")
    input("Press Enter to exit...")
    exit()

key = Fernet.generate_key()
cipher = Fernet(key)

files_to_encrypt = [file for file in os.listdir(script_directory) if os.path.isfile(os.path.join(script_directory, file))]
files_to_encrypt = [file for file in files_to_encrypt if not file.endswith('.py')]

for file_name in files_to_encrypt:
    print(file_name)
    with open(os.path.join(script_directory, file_name), 'rb') as f:
        file_data = f.read()

    encrypted_data = cipher.encrypt(file_data)

    with open(os.path.join(script_directory, file_name), 'wb') as f:
        f.write(encrypted_data)

decryption_key = key.decode()

print("")
print(colors.BLUE + "Encryption Key: ", key.decode())

with open(str(script_directory + "\\" + "KEY.txt"), 'w') as file:
    # Write the string to the file
    file.write(str(decryption_key))

with open("SAFETY_FILE", 'w') as file:
    pass

input("Press Enter to exit...")