import pygame

# Инициализация Pygame
pygame.init()

# Получение размеров дисплея
infoObject = pygame.display.Info()
width = infoObject.current_w
height = infoObject.current_h

print(f"Размер экрана: {width}x{height}")

# Не забудьте завершить работу Pygame, если он больше не нужен
pygame.quit()
