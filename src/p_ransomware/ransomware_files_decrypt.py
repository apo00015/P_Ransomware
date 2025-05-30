import base64
import hashlib
import os

from cryptography.fernet import Fernet


def generate_key_from_password(password: str) -> bytes:
    key = hashlib.sha256(password.encode()).digest()
    return base64.urlsafe_b64encode(key)


def decrypt(fernet: Fernet, file_path: str):
    with open(file_path, "rb") as encrypted_file:
        datos_cifrados = encrypted_file.read()

    datos_originales = fernet.decrypt(datos_cifrados)

    with open(file_path, "wb") as decrypted_file:
        decrypted_file.write(datos_originales)


def encrypt(fernet: Fernet, file: str):
    with open(file, "rb") as original_file:
        datos = original_file.read()

        datos_cifrados = fernet.encrypt(datos)

    with open(file, "wb") as encrypted_file:
        encrypted_file.write(datos_cifrados)


def get_files(path_files) -> list:
    extensiones = (".pdf", ".json", ".csv", ".png", ".txt")

    return [
        os.path.join(path_files, archivo)
        for archivo in os.listdir(path_files)
        if archivo.lower().endswith(extensiones) and os.path.isfile(os.path.join(path_files, archivo))
    ]


def main() -> None:
    password = "mi_contraseña_segura"
    key = generate_key_from_password(password)
    fernet = Fernet(key)
    files = get_files("files/")
    print(files)
    for file in files:
        decrypt(fernet, file)


if __name__ == "__main__":
    main()
