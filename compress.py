import zipfile
import os

# Название файла со списком файлов

list_file = '../files_upload_layer1.txt'
# Название архива, который создадим
archive_name = 'selected_files_layer1.zip'
dir_path = "./upload"

os.chdir(dir_path)
# Читаем список файлов из файла
with open(list_file, 'r', encoding='utf-8') as f:
    files = [line.strip() for line in f if line.strip()]  # убираем пустые строки

# Создаём ZIP-архив
with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for file in files:
        if os.path.exists(file):
            zipf.write(file, arcname=os.path.basename(file))
            print(f'Добавлено: {file}')
        else:
            print(f'Файл не найден: {file}')

print(f'Архив "{archive_name}" создан.')
