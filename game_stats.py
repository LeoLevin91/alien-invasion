class GameStats():
    """Отслежиавние статистики для игры"""

    def __init__(self, ai_settings):
        """Инициализирует статистику"""
        self.ai_setting = ai_settings
        self.game_active = True
        self.reset_stats()

    def reset_stats(self):
        """Инициализвция статистики изменяющийся в ходе игры"""
        self.ships_left = self.ai_setting.ship_limit