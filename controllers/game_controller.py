from views.main_window import MainWindow
from models.game_model import GameModel

# ---- 3.Controller-Klasse ----

class GameController:
    # --- 3.1 Controller initialisieren ---
    def __init__(self):
        self.model = GameModel() # Game-Logik einspeisen
        self.view = MainWindow() # GUI-Logik einspeisen
        
        # -- 3.1.1 Game und GUI verknüpfen und Titel verändern  --
        self.view.update_title(self.model.title)
    
    # --- 3.2 GUI über Controller aufrufen ---
    def show(self):
        """Zeigt die Anwendung"""
        self.view.show()
    
    # --- 3.3 Game-Titel ändern(PLACEHOLDER) ---
    def update_game_title(self, new_title):
        """Ändert den Spieltitel"""
        # Schritt 1: Model aktualisieren
        self.model.title = new_title
        
        # Schritt 2: View aktualisieren
        self.view.update_title(self.model.title)
    
    # --- 3.4 Punkte Aktualisieren(PLACEHOLDER) ---
    def add_points(self, points):
        """Fügt Punkte zum Score hinzu"""
        # Schritt 1: Model aktualisieren
        self.model.update_score(points)
        
        # Schritt 2: Weitere Aktionen (z.B. Score in GUI anzeigen)
        print(f"Neuer Score: {self.model.score}")