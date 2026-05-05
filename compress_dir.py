import os
import zipfile

# Название файла со списком директорий
dirs_list_file = 'directory.txt'
# Название архива
archive_name = 'directories_archive.zip'

# Читаем список директорий
with open(dirs_list_file, 'r', encoding='utf-8') as f:
    directories = [line.strip() for line in f if line.strip()]

# Создаём ZIP-архив
with zipfile.ZipFile(archive_name, 'w', zipfile.ZIP_DEFLATED) as zipf:
    for dir_path in directories:
        if os.path.exists(dir_path) and os.path.isdir(dir_path):
            # Обход всех файлов и подкаталогов в текущем каталоге
            for root, dirs, files in os.walk(dir_path):
                for file in files:
                    file_path = os.path.join(root, file)
                    # Относительный путь внутри архива
                    arcname = os.path.relpath(file_path, start=dir_path)
                    # Можно добавить префикс с именем каталога, чтобы отличать
                    arcname_full = os.path.join(os.path.basename(dir_path), arcname)
                    zipf.write(file_path, arcname=arcname_full)
            print(f'Добавлены: {dir_path}')
        else:
            print(f'Каталог не найден или недоступен: {dir_path}')

print('Архивация завершена.')
