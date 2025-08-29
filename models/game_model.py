# ---- 1.Game-Logik ----
# --- 1.1 Game-Klasse erstellen ---
class GameModel:
    # --- 1.1.1 Haupt-Variablen bestimmen ---
    def __init__(self):
        self.game_round = 0
        self.building_dict = {}