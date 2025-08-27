
# ---- 1.Game-Logik ----
# --- 1.1 Game-Klasse ertellen ---
class GameModel:
    # --- 1.1.1 Haupt-Variablenbestimmen ---
    def __init__(self):
        self._title = "ECO - Hauptmenü"
        self._score = 0

    # --- 1.1.2 Hauptvariablen als Properties übergeben ---
    @property
    def title(self):
        return self._title
    
    @title.setter
    def title(self, value):
        self._title = value

    @property
    def score(self):
        return self._score
    
    # --- 1.1.3 Update-Funktion für Score ---
    def update_score(self, points):
        self._score += points