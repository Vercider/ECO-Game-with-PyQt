from PyQt6.QtWidgets import QApplication, QMainWindow, QScrollArea, QWidget, QVBoxLayout, QLabel
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QPixmap, QBrush  
import sys

# ---- 1.Hauptfuntion definieren ----
def main():
    # --- 1.1 QApplication-Instaz initiieren ---
    app = QApplication(sys.argv)

    # --- 1.2 Hauptfenster erstellen ---
    main_window = QMainWindow()
    main_window.setWindowTitle("ECO-Game")

    # --- 1.3 Hintergrundbild setzen ---
    palette = QPalette()
    pixmap = QPixmap("ECO_BG_image.jpeg")
    palette.setBrush(QPalette.ColorRole.Window, QBrush(pixmap))
    main_window.setPalette(palette)

    # --- 1.4 Scrollbereich erstellen ---
    scroll_area = QScrollArea()
    content_widget = QWidget()

    # --- 1.5 Layout für den Inhalt ---
    layout = QVBoxLayout(content_widget)

    # --- 1.6 Titel-Label ---
    title_label = QLabel("ECO - Hauptmenü")
    title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: white; background-color: rgba(0,0,0,100);")

    # --- 1.7 Label zum Layout hinzufügen ---
    layout.addWidget(title_label)

    # --- 1.8 Content-Widget in Scroll-Area setzen ---
    scroll_area.setWidget(content_widget)
    scroll_area.setWidgetResizable(True)
    scroll_area.setStyleSheet("background: transparent;")

    # --- 1.9 Scrollarea als zentrales Widget setzen ---
    main_window.setCentralWidget(scroll_area)

    # --- 1.10 Hauptfenster anzeigen ---
    main_window.showFullScreen()

    # --- 1.11 Anwendungsschleife starten ---
    main_window.setWindowState(Qt.WindowState.WindowMaximized)
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
