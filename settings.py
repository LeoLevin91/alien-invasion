class Settings():
    """Класс для хранения настроек"""
    def __init__(self):
        """Инициализация настроек игры"""
        #Параметры экрана
        self.screen_width = 680
        self.screen_height = 480
        self.bg_color = (230, 230, 230)
        self.ship_speed_factor = 1.2