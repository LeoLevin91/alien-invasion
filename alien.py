import pygame
from pygame.sprite import Sprite

class Alien(Sprite):
    """Класс для одного пришельца"""
    def __init__(self, ai_settings, screen):
        """Инициализирует пришельца и задает начальную его позицию"""
        super(Alien, self).__init__()
        self.screen = screen
        self.ai_settings = ai_settings

        # Загрузка пришельца через атрибут rect
        self.image = pygame.image.load('images/alien.bmp')
        self.rect = self.image.get_rect()

        # Каждый новый пришелец появляется в верхнем левом углу экрана
        self.rect.x = self.rect.width
        self.rect.y = self.rect.height

        # Сохранение точной позиции пришельца
        self.x = float(self.rect.x)

    def blitme(self):
        self.screen.blit(self.image, self.rect)
