import ctypes

# Определяем структуру для получения размеров экрана
class RECT(ctypes.Structure):
    _fields_ = [
        ("left", ctypes.c_long),
        ("top", ctypes.c_long),
        ("right", ctypes.c_long),
        ("bottom", ctypes.c_long),
    ]

# Загружаем библиотеку user32.dll
user32 = ctypes.WinDLL('user32', use_last_error=True)

# Получаем дескриптор окна (указание 0 для всего экрана)
hWnd = None  # Для всего экрана

# Создаем структуру RECT для хранения размеров
rect = RECT()

# Получение размеров экрана
result = user32.GetClientRect(hWnd, ctypes.byref(rect))
if result:
    width = rect.right - rect.left
    height = rect.bottom - rect.top
    print(f"Размер экрана: {width}x{height}")
else:
    print("Не удалось определить размер экрана")
