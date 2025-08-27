from PyQt6.QtWidgets import QApplication, QMainWindow 
import sys

# ---- 1.Hauptfuntion definieren ----
def main():
    # --- 1.1 QApplication-Instaz initiieren ---
    app = QApplication(sys.argv)

    # --- 1.2 Hauptfenster erstellen ---
    main_window = QMainWindow()
    main_window.setWindowTitle("ECO-Game")
    main_window.setGeometry(100, 100, 800, 600)

    # --- 1.3 Hauptfenster anzeigen ---
    main_window.show()

    # --- 1.4 Anwendungsschleife starten ---
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
