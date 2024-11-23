# Этот скрипт создает текстовые файлы в директории data/raw с разными кодировками и добавляет запись о каждом файле в лог.

import os
import datetime
import logging

# Данные для создания текстовых файлов
files_data = {
    "project_root/data/raw/file_russian.txt": ("Привет, мир!", "utf-8"),
    "project_root/data/raw/file_english.txt": ("Hello, world!", "iso-8859-1"),
}

# Создание файлов с разными кодировками
for file_path, (content, encoding) in files_data.items():
    with open(file_path, "w", encoding=encoding) as f:
        f.write(content)
    logging.info(f"Created file: {file_path} with encoding {encoding}")
    print(f"Created file: {file_path} with encoding {encoding}")

# Запись лога выполнения операций
log_file = os.path.join("project_root", "logs", "creation_log.txt")
with open(log_file, "a") as log:
    log.write(f"{datetime.datetime.now()}: Created directories and files.\n")
    print(f"Log updated at {log_file}")
    
