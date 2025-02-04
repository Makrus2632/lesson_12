import json
import os
from datetime import datetime

# Путь к папке output
output_dir = os.path.join(os.getcwd(), "project_root", "output")
# Создаём папку output, если она не существует
os.makedirs(output_dir, exist_ok=True)

# Путь для сохранения отчёта в формате JSON
report_file = os.path.join(output_dir, f"final_report_{datetime.now().strftime('%Y%m%d')}.json")

# Составляем отчёт
report_data = {
    "tasks": [
        {
            "task": "Задание 1: Работа с пользовательскими классами и JSON",
            "description": "Создание класса FileInfo для хранения информации о файлах.",
            "time_spent": "3 часа",
            "issues": "Некоторые файлы не были найдены при сереализации.",
            "solutions": "Исправлены пути к файлам, добавлена обработка ошибок.",
            "improvements": "Рекомендуется добавить проверку существования файлов перед сериализацией."
        },
        {
            "task": "Задание 2: Сериализация и JSON Schema",
            "description": "Сохранение информации о файлах в JSON и валидация через JSON Schema.",
            "time_spent": "2 часа",
            "issues": "Не было учтено местоположение JSON-файла для валидации.",
            "solutions": "Исправлены пути к файлам, уточнена схема валидации.",
            "improvements": "Рекомендуется дополнительно проверить валидность всех ключевых полей."
        },
        {
            "task": "Задание 3: Логирование",
            "description": "Добавление логирования в каждый скрипт для отслеживания ошибок.",
            "time_spent": "8 часов",
            "issues": "Логирование не работало из-за неправильных путей к файлам.",
            "solutions": "Исправлены пути и добавлены обработчики ошибок.",
            "improvements": "Рекомендуется добавить уровень логирования для отладки и информационных сообщений."
        },
        {
            "task": "Задание 4: Резервное копирование и восстановление данных",
            "description": "Создание архива и восстановление данных.",
            "time_spent": "6 часов",
            "issues": "Ошибка при восстановлении данных из архива.",
            "solutions": "Исправлен путь и добавлены проверки существования файла.",
            "improvements": "Добавить уведомление о завершении работы архивирования/восстановления."
        },
        {
            "task": "Задание 5: Генерация итогового отчёта",
            "description": "Генерация итогового отчёта по выполненной работе.",
            "time_spent": "1 час",
            "issues": "Проблем с созданием отчёта не возникало.",
            "solutions": "Использован код для создания отчёта в формате JSON.",
            "improvements": "Возможно добавление подробного анализа времени выполнения каждого задания."
        }
    ],
    "summary": {
        "total_time_spent": "20 часов",
        "conclusion": "Все задания были выполнены успешно с небольшими трудностями, связанными с путями к файлам и сериализацией данных. Рекомендуется уделить больше внимания валидации данных и проверке путей."
    }
}

# Сохраняем отчёт в формате JSON в папке output
try:
    with open(report_file, "w", encoding="utf-8") as f:
        json.dump(report_data, f, indent=4, ensure_ascii=False)
    print(f"Отчёт успешно сохранён в {report_file}")
except Exception as e:
    print(f"Ошибка при сохранении отчёта: {e}")
