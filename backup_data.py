# Cкрипт создает резервную копию всех файлов в data/ и сохраняет её в формате ZIP.
# Каждое действие записывается в лог с указанием местоположения резервной копии.

import shutil
from datetime import datetime
from pathlib import Path
import logging

# Указываем пути
project_root = Path("project_root")
data_dir = Path(project_root/"data")
backups_dir = Path(project_root/"backups")
logs_dir = Path(project_root/"logs")

# Указываем имя архива
backup_file = backups_dir / f"backup_{datetime.now().strftime('%Y%m%d')}"

# Настройка логирования
log_file = logs_dir / "backup_log.txt"
logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

# Создание архива
try:
    shutil.make_archive(backup_file.as_posix(), "zip", data_dir.as_posix())
    logging.info(f"Backup created at {backup_file}.zip")
    print(f"Backup created at {backup_file}.zip")
except Exception as e:
    logging.error(f"Failed to create backup: {e}")
    print(f"Error: Failed to create backup: {e}")
