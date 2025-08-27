from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6.QtCore import Qt  
import sys

# ---- 1.Hauptfuntion definieren ----
def main():
    # --- 1.1 QApplication-Instaz initiieren ---
    app = QApplication(sys.argv)

    # --- 1.2 Hauptfenster erstellen ---
    main_window = QMainWindow()
    main_window.setWindowTitle("ECO-Game")

    # --- 1.3 Hauptfenster anzeigen ---
    main_window.showFullScreen()

    # --- 1.4 Anwendungsschleife starten ---
    main_window.setWindowState(Qt.WindowState.WindowMaximized)
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
