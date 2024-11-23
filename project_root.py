# Этот скрипт создает структуру директорий и записывает лог об успешном создании каждой папки.

import os
import logging

# Создаем корневую директорию проекта
project_root = "project_root"
directories = [
    os.path.join(project_root, "data/raw"),
    os.path.join(project_root, "data/processed"),
    os.path.join(project_root, "logs"),
    os.path.join(project_root, "backups"),
    os.path.join(project_root, "output"),
]

# Создание структуры директорий
for directory in directories:
    os.makedirs(directory, exist_ok=True)
    logging.info(f"Directory created: {directory}")
    print(f"Created directory: {directory}")

# Настройка логирования
logging.basicConfig(filename="project_root/logs/creation_log.txt", level=logging.INFO, format="%(asctime)s - %(message)s")

# Логируем успешное создание директорий
for directory in directories:
    logging.info(f"Directory created or already exists: {directory}")
    

