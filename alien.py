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

    def check_edges(self):
        """Возвращает True если пришелец нахоидтся у края экрана"""
        screen_rect = self.screen.get_rect()
        if self.rect.right >= screen_rect.right:
            return True
        elif self.rect.left <= 0:
            return True

    def update(self):
        """Перемещения пришельцев вправо"""
        self.x += (self.ai_settings.alien_speed_factor * self.ai_settings.fleet_direction)
        self.rect.x = self.x