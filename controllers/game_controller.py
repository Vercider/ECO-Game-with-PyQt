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
    
    # --- 3.3 START-Button ---
    def on_start_game(self):
        self.view.update_resources(10, 10, 10)
        self.view.update_population(4, 4, 4)
        self.view.update_main_output(f"Dein Dorf erblüht\nDu bekommst Ressourcen.\nUnd es wurde eine Hütte gebaut.\nKlicke auf 'Nächste Runde' um weiter zu spielen!")
