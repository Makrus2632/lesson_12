# Этот скрипт читает файлы из data/raw, выполняет преобразование текста и сохраняет результаты в data/processed
# Каждое действие записывается в лог, чтобы было видно, какой файл был обработан и куда он был сохранен.

from pathlib import Path
import logging

# Указываю базовые директории
raw_data_path = Path("project_root/data/raw")
processed_data_path = Path("project_root/data/processed")
logs_dir = Path("project_root/logs")

# Настройка логирования
log_file = logs_dir / "process_raw_data.log"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Чтение и преобразование данных
for file in raw_data_path.glob("*.txt"):
    try:
        # Чтение исходного файла
        with open(file, "r", encoding="utf-8", errors="replace") as f:
            content = f.read()

        # Преобразование текста
        processed_content = content.swapcase()  # Заменяем заглавные на строчные и наоборот

        # Сохранение обработанных данных
        processed_file = processed_data_path / f"{file.stem}_processed.txt"
        with open(processed_file, "w", encoding="utf-8") as pf:
            pf.write(processed_content)

        # Запись информации в лог
        logging.info(f"Processed file: {file} -> {processed_file}")
        print(f"Processed file saved: {processed_file}")

    except Exception as e:
        # Логируем ошибки при обработке
        logging.error(f"Error processing file {file}: {e}")
        print(f"Error processing file {file}: {e}")
