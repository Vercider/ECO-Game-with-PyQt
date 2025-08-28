from PyQt6.QtWidgets import QApplication
import sys
from controllers.game_controller import GameController

# ---- 4.Haupt-Initialisierung ----
# --- 4.1 COntroller-Initialisierung ---
def main():
    # -- 4.1.1 QApplication-Instanz erstellen --
    app = QApplication(sys.argv)
    
    # -- 4.1.2 Game-Controller erstellen und initialisieren --
    controller = GameController()
    
    # -- 4.1.3 Anwendung über Controller anzeigen --
    controller.show()
    
    # -- 4.1.4 Event-Loop starten und auf Beenden warten --
    sys.exit(app.exec())

# ---- 4.2 Programmstart ----
if __name__ == "__main__":
    main()