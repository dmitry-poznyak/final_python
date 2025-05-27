import os
import logging
from collections import namedtuple
import argparse

# Настройка логирования
logging.basicConfig(filename='directory_log.txt', level=logging.INFO,
                    format='%(asctime)s - %(message)s')

# Определение namedtuple
ItemInfo = namedtuple('ItemInfo', ['name', 'extension', 'is_dir', 'parent'])

# Получение пути из командной строки
parser = argparse.ArgumentParser(description="Анализ содержимого директории")
parser.add_argument("path", help="Путь до директории")
args = parser.parse_args()

if not os.path.isdir(args.path):
    print("Указанный путь не является директорией.")
    exit(1)

# Обход содержимого
for item in os.listdir(args.path):
    full_path = os.path.join(args.path, item)
    is_dir = os.path.isdir(full_path)
    name, ext = os.path.splitext(item)
    ext = ext[1:] if ext else ''
    info = ItemInfo(name=name if not is_dir else item,
                    extension=ext,
                    is_dir=is_dir,
                    parent=os.path.basename(args.path))
    logging.info(info)
    print(info)
