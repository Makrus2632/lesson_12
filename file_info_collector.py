# Класс FileInfo собирает информацию о каждом файле.
# Сериализованные данные сохраняются в output/file_info.json и логируются.

import os
import json
import logging
from datetime import datetime

# Настройка логирования
# Убедимся, что директория для логов существует
log_dir = "project_root/logs"  # Исправили путь к директории для логов
os.makedirs(log_dir, exist_ok=True)

# Конфигурируем логирование, указываем файл и уровень логирования
logging.basicConfig(
    filename=os.path.join(log_dir, "file_info_collector.log"),  # Путь к файлу логов
    level=logging.INFO,  # Уровень логирования (информационные сообщения)
    format="%(asctime)s - %(levelname)s - %(message)s"  # Формат логируемых сообщений
)

# Класс FileInfo
class FileInfo:
    def __init__(self, name, path, size, created_at, modified_at):
        """
        Инициализация объекта FileInfo с параметрами:
        - name: имя файла
        - path: полный путь к файлу
        - size: размер файла в байтах
        - created_at: дата и время создания файла
        - modified_at: дата и время последнего изменения файла
        """
        self.name = name
        self.path = path
        self.size = size
        self.created_at = created_at
        self.modified_at = modified_at

    def to_dict(self):
        """
        Метод для получения словаря с информацией о файле.
        Возвращает атрибуты объекта как словарь.
        """
        return vars(self)  # Использует встроенный метод vars() для получения всех атрибутов объекта

# Сбор информации о файлах в указанной директории
def collect_file_info(directory):
    """
    Функция для сбора информации о всех файлах в директории:
    - Имя файла
    - Путь к файлу
    - Размер файла
    - Дата и время создания и изменения файла
    """
    file_info_list = []  # Список для хранения информации о файлах
    try:
        # Обход всех файлов в директории и поддиректориях
        for root, _, files in os.walk(directory):
            for file_name in files:
                file_path = os.path.join(root, file_name)  # Путь к файлу
                # Создаем объект FileInfo для каждого файла
                file_info = FileInfo(
                    file_name, file_path,  # Имя и путь
                    os.path.getsize(file_path),  # Размер файла
                    datetime.fromtimestamp(os.path.getctime(file_path)).isoformat(),  # Дата создания
                    datetime.fromtimestamp(os.path.getmtime(file_path)).isoformat()  # Дата последнего изменения
                )
                file_info_list.append(file_info.to_dict())  # Добавляем информацию о файле в список
        logging.info(f"Собрано информации о {len(file_info_list)} файлах.")  # Логируем количество собранных файлов
        return file_info_list  # Возвращаем собранные данные
    except Exception as e:
        logging.error(f"Ошибка при сборе информации: {e}")  # Логируем ошибку, если она возникла
        raise  # Поднимаем исключение

# Сохранение данных в JSON файл
def save_to_json(data, output_file):
    """
    Функция для сохранения данных в формате JSON в указанный файл.
    """
    try:
        with open(output_file, "w") as json_file:
            json.dump(data, json_file, indent=4)  # Сериализация данных в JSON с отступами
        logging.info(f"Данные успешно сохранены в {output_file}")  # Логируем успешное сохранение
    except Exception as e:
        logging.error(f"Ошибка при сохранении данных в {output_file}: {e}")  # Логируем ошибку
        raise  # Поднимаем исключение

# Основная часть скрипта
if __name__ == "__main__":
    # Путь к директории с обработанными файлами (с учетом правильной структуры проекта)
    processed_dir = "project_root/data/processed"  # Исправили путь для директории processed
    output_dir = "project_root/output"  # Путь для выходных данных
    output_file = os.path.join(output_dir, "file_info.json")  # Путь к итоговому JSON файлу

    # Проверяем, существуют ли директории
    if os.path.exists(processed_dir) and os.path.exists(output_dir):
        # Собираем информацию и сохраняем ее в JSON
        save_to_json(collect_file_info(processed_dir), output_file)
    else:
        logging.error(f"Директории не найдены: {processed_dir}, {output_dir}")  # Логируем ошибку, если директории не существуют
