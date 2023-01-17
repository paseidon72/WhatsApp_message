from PyPDF2 import PdfReader, PdfWriter


def encrypt_file():
    file_path = input("[+] Enter file path: ")
    password = input("[+] Enter password: ")
    reader = PdfReader(f"{file_path}")
    writer = PdfWriter()

# Додайте всі сторінки до автора
    for page in reader.pages:
        writer.add_page(page)

# Додайте пароль до нового PDF-файлу
    writer.encrypt(password)

# Збережіть новий PDF у файл
    with open(f"{file_path}", "wb") as f:
        writer.write(f)
        print("Your file encrypt")


def decrypt_file():
    file_path = input("[+] Enter file path: ")
    password = input("[+] Enter password: ")
    reader = PdfReader(f"{file_path}")
    writer = PdfWriter()

    if reader.is_encrypted:
        reader.decrypt(password)

    # Add all pages to the writer
    for page in reader.pages:
        writer.add_page(page)

    # Save the new PDF to a file
    with open(f"{file_path}", "wb") as f:
        writer.write(f)
        print("Your file decrypt")


def main():
    choose = input("[+] Enter 0 to encrypt the file\n[+] Enter 1 to decrypt: ")
    encrypt_file() if choose == "0" else decrypt_file()


if __name__ == "__main__":
    main()
