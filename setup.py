import os
from cryptography.fernet import Fernet
import argparse

files_list = []


def basePath(file):
    return os.path.join(".\Sample", file)


for file in os.listdir('./Sample'):
    if file == "secret.py":
        continue
    if os.path.isfile(basePath(file)):
        files_list.append(file)


def Generate_key():
    key = Fernet.generate_key()
    with open('secret.key', "wb") as keyFile:
        keyFile.write(key)


def read_secretKey():
    with open('secret.key', "rb") as readSecret:
        key_secret = readSecret.read()
    return key_secret


def Encrypted_Files():
    for file in files_list:
        with open(basePath(file), "rb") as readFile:
            contents = readFile.read()
        content_encrypted = Fernet(read_secretKey()).encrypt(contents)
        with open(basePath(file), "wb") as writeFile:
            writeFile.write(content_encrypted)

    print("Encrypted Files Done")


def Decryption_Files():
    for file in files_list:
        with open(basePath(file), "rb") as readFile:
            contents = readFile.read()
        content_decrypted = Fernet(read_secretKey()).decrypt(contents)
        with open(basePath(file), "wb") as writeFile:
            writeFile.write(content_decrypted)

    print("Decrypted Files Done")


def delete_secret_key():
    os.remove('./secret.key')


def decrypted_file():
    read_secretKey()
    Decryption_Files()
    delete_secret_key()


def encrypted_File():
    Generate_key()
    Encrypted_Files()


if __name__ == '__main__':

    parser = argparse.ArgumentParser(
        description="Example Encrypt or Decrypt files")
    parser.add_argument('-e', '--encrypt',
                        help="Encrypt the Files that are in Sample Folder.")
    parser.add_argument('-d', '--decrypt',
                        help="Decrypt the Files that are in Sample Folder.")

    args = parser.parse_args()

    if args.encrypt:
        encrypted_File()

    elif args.decrypt:
        decrypted_file()
