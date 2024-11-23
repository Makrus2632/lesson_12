# Скрипт собирает информацию о каждом обработанном файле и записывает её в JSON-файл.
# Каждое действие записывается в лог для отслеживания.

import json
import time
import os
import logging
from pathlib import Path  # Добавлен импорт Path

# Настройка логирования
log_file = "project_root/logs/serialization_log.txt"
os.makedirs(os.path.dirname(log_file), exist_ok=True)
logging.basicConfig(filename=log_file, level=logging.INFO, format="%(asctime)s - %(message)s")

processed_data_path = Path("project_root/data/processed")
output_file = Path("project_root/output/processed_data.json")
processed_files_data = []

# Убеждаемся, что директория для JSON существует
os.makedirs(output_file.parent, exist_ok=True)

# Сериализация данных
for file in processed_data_path.glob("*.txt"):
    with open(file, "r", encoding="utf-8") as f:
        content = f.read()
    file_info = {
        "filename": file.name,
        "original_text": content,
        "processed_text": content.swapcase(),
        "size_bytes": file.stat().st_size,
        "last_modified": time.ctime(file.stat().st_mtime),
    }
    processed_files_data.append(file_info)

# Сохранение в JSON
with open(output_file, "w", encoding="utf-8") as json_file:
    json.dump(processed_files_data, json_file, indent=4)
    logging.info(f"Serialized data saved to {output_file}")
    print(f"Serialized data saved to {output_file}")

