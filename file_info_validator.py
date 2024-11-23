import json
import os
import logging
from jsonschema import validate, ValidationError, exceptions

# Настройка логирования
logging.basicConfig(
    filename="project_root/logs/json_validation_log.txt",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)

# Путь к JSON файлу, который нужно проверить
json_file_path = os.path.join(os.getcwd(), "project_root", "output", "file_info.json")

# JSON Schema для валидации
file_info_schema = {
    "type": "array",
    "items": {
        "type": "object",
        "properties": {
            "name": {"type": "string"},
            "path": {"type": "string"},
            "size": {"type": "integer"},
            "created_at": {"type": "string", "format": "date-time"},
            "modified_at": {"type": "string", "format": "date-time"},
        },
        "required": ["name", "path", "size", "created_at", "modified_at"],
        "additionalProperties": False  # Запрещает дополнительные поля
    }
}

# Функция для проверки валидности JSON
def validate_json(json_data, schema):
    try:
        validate(instance=json_data, schema=schema)
        print("JSON файл валиден.")
    except ValidationError as e:
        print(f"Ошибка валидации: {e.message}")
    except exceptions.SchemaError as e:
        print(f"Ошибка схемы: {e.message}")
    except Exception as e:
        print(f"Неизвестная ошибка: {e}")

# Загрузка и валидация JSON
try:
    with open(json_file_path, "r") as json_file:
        file_info_data = json.load(json_file)
        validate_json(file_info_data, file_info_schema)
except FileNotFoundError:
    print(f"Файл {json_file_path} не найден.")
except json.JSONDecodeError:
    print(f"Ошибка при чтении JSON файла: {json_file_path}")
except Exception as e:
    print(f"Ошибка: {e}")

