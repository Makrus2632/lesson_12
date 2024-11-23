# Этот скрипт разархивирует резервную копию.
# Каждое действие записывается в лог.

import shutil
import logging
from pathlib import Path

# Указываем пути
project_root = Path("project_root")
backups_dir = project_root / "backups"
logs_dir = project_root / "logs"
restore_dir = project_root / "data"

# Указываем резервный файл
backup_file = backups_dir / "backup_20241124.zip"

# Убедимся, что директория для логов существует
logs_dir.mkdir(parents=True, exist_ok=True)

# Настройка логирования
log_file = logs_dir / "restore_log.txt"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Разархивирование данных
try:
    restore_dir.mkdir(parents=True, exist_ok=True)  # Убедимся, что папка для восстановления существует
    shutil.unpack_archive(backup_file.as_posix(), restore_dir.as_posix())
    logging.info(f"Data restored from {backup_file} to {restore_dir}")
    print(f"Data restored to {restore_dir}")
except FileNotFoundError:
    logging.error(f"Backup file not found: {backup_file}")
    print(f"Error: Backup file not found: {backup_file}")
except Exception as e:
    logging.error(f"Failed to restore data: {e}")
    print(f"Error: Failed to restore data: {e}")
