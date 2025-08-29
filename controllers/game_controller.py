from views.main_window import MainWindow
from models.game_model import GameModel

# ---- 3.Controller-Klasse ----

class GameController:
    # --- 3.1 Controller initialisieren ---
    def __init__(self):
        self.model = GameModel() # Game-Logik einspeisen
        self.view = MainWindow() # GUI-Logik einspeisen
    
    # --- 3.2 GUI über Controller aufrufen ---
    def show(self):
        """Zeigt die Anwendung"""
        self.view.show()