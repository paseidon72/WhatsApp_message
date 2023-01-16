import os.path

# pip install PyPDF2
from PyPDF2 import PdfWriter
from PyPDF2 import PdfReader
from PyPDF2.errors import PdfReadError


# установка пароля на файл
# получение имени файла, создание объекта писателя
# добавление в цикле станиц в писателя, установка пароля
# сохранение файла
def encrypt_pdf(pdf_path, pswd):
    encrypt_file_name = f'{os.path.split(pdf_path)[1].split(".")[0]}_enc.pdf'
    pdf_enc_writer = PdfWriter()

    for page in range(PdfReader(pdf_path).numPages):
        pdf_enc_writer.addPage(PdfReader(pdf_path).getPage(page))
        print(f'[+] Добавлена страница {page+1}')

    pdf_enc_writer.encrypt(pswd)
    with open(encrypt_file_name, 'wb') as file:
        pdf_enc_writer.write(file)

    print(f'[+] Пароль на файл {encrypt_file_name} установлен')


# снятие пароля с файла
# получение имени файла, создание объекта писателя
# создание объекта чтеца, проверка, есть ли пароль на файле
# добавление в цикле страниц документа в писателя
# блок try-except для проверки правильности пароля, сохранение файла
def decrypt_pdf(pdf_path, pswd):
    if '_enc' in os.path.split(pdf_path)[1].split(".")[0]:
        decrypt_file_name = f'{os.path.split(pdf_path)[1].split(".")[0].split("_")[0]}_dec.pdf'
    else:
        decrypt_file_name = f'{os.path.split(pdf_path)[1].split(".")[0]}_dec.pdf'
    pdf_dec_writer = PdfWriter()
    pdf_dec_reader = PdfReader(pdf_path)

    if pdf_dec_reader.isEncrypted:
        pdf_dec_reader.decrypt(pswd)
    else:
        print('[+] На файле нет пароля')
        return

    try:
        for page in range(pdf_dec_reader.numPages):
            pdf_dec_writer.addPage(pdf_dec_reader.getPage(page))
            print(f'[+] Добавлена страница {page+1}')
    except PdfReadError:
        print('\t[-] Вы ввели неправильный пароль\n')
        main()
        return

    with open(decrypt_file_name, 'wb') as file:
        pdf_dec_writer.write(file)

    print(f'[+] Пароль с файла {decrypt_file_name} снят')


# получаем путь к файлу и пароль
# проверяем указанный путь к файлу
# проверяем пользовательский выбор
def main():
    user_choise = input('[+] Выберите действие:\n\t[1] Установить пароль\n\t[2] Снять пароль\n\t[3] Выход\n\t>>> ')
    if user_choise == "1":
        while not os.path.isfile(pdf_path := input('\t[+] Введите путь к файлу PDF: ')):
            print('\t[-] По указанному пути файла не существует!')
        pswd = input('\t[+] Введите пароль для установки: ')
        encrypt_pdf(pdf_path, pswd)
    elif user_choise == "2":
        while not os.path.isfile(pdf_path := input('\t[+] Введите путь к файлу PDF: ')):
            print('\t[-] По указанному пути файла не существует!')
        pswd = input('\t[+] Введите пароль PDF: ')
        decrypt_pdf(pdf_path, pswd)
    elif user_choise == "3":
        exit(0)
    else:
        print('\n[+] ВВЕДЕННЫЕ ДАННЫЕ МНЕ НЕ ПОНЯТНЫ. ПОВТОРИТЕ ВСЕ СНАЧАЛА!\n')
        main()


if __name__ == "__main__":
    main()

