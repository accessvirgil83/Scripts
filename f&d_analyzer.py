import ctypes

# libc библиотеки
libc = ctypes.CDLL('libc.so.6')

# Структура dirent для Linux
class dirent(ctypes.Structure):
    _fields_ = [
        ('d_ino', ctypes.c_ulong),
        ('d_off', ctypes.c_long),
        ('d_reclen', ctypes.c_ushort),
        ('d_type', ctypes.c_ubyte),
        ('d_name', ctypes.c_char * 256)
    ]

# Объявляем функции
libc.opendir.restype = ctypes.c_void_p
libc.opendir.argtypes = [ctypes.c_char_p]

libc.readdir.restype = ctypes.POINTER(dirent)
libc.readdir.argtypes = [ctypes.c_void_p]

libc.closedir.restype = ctypes.c_int
libc.closedir.argtypes = [ctypes.c_void_p]

directory_path = b'./'  # байтовое
output_file = 'files_layer0.txt'

try:
    dirp = libc.opendir(directory_path)
    if not dirp:
        raise Exception("Не удалось открыть директорию.")

    entries = []

    while True:
        entry_ptr = libc.readdir(dirp)
        if not entry_ptr:
            break

        entry = entry_ptr.contents
        # Проверяем, что это файл или директория
 #       if entry.d_type in (4,4):  # 4=dir, 8=file
        if entry.d_type == 8:  # 4=dir, 8=file
            name = entry.d_name.decode('utf-8')
            # исключить "." и ".."
            if name not in (".", ".."):
                entries.append(name)

    libc.closedir(dirp)

    # Записать в файл
    with open(output_file, 'w', encoding='utf-8') as f:
        for name in entries:
            f.write(name + '\n')

    print(f"Записано {len(entries)} элементов (файлы и директории).")
except Exception as e:
    print(f"Ошибка: {e}")
