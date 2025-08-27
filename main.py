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

    # --- 1.3 Bildschrimgröße ermitteln ---
    screen = app.primaryScreen()
    screen_size = screen.size()

    # --- 1.4 Hintergrundbild setzen ---
    palette = QPalette()
    pixmap = QPixmap("ECO_BG_image.jpeg")

    # --- 1.5 Bild auf Bildschirmgröße skalieren ---
    scaled_pixmap = pixmap.scaled(screen_size, Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation)
    palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_pixmap))
    main_window.setPalette(palette)

    # --- 1.6 Scrollbereich erstellen ---
    scroll_area = QScrollArea()
    content_widget = QWidget()

    # --- 1.7 Layout für den Inhalt ---
    layout = QVBoxLayout(content_widget)

    # --- 1.8 Titel-Label ---
    title_label = QLabel("ECO - Hauptmenü")
    title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
    title_label.setStyleSheet("font-size: 24px; font-weight: bold; color: white; background-color: rgba(0,0,0,100);")
    
    # --- 1.9 Label zum Layout hinzufügen ---
    layout.addWidget(title_label)

    # --- 1.10 Content-Widget in Scroll-Area setzen ---
    scroll_area.setWidget(content_widget)
    scroll_area.setWidgetResizable(True)
    scroll_area.setStyleSheet("background: transparent;")

    # --- 1.11 Scrollarea als zentrales Widget setzen ---
    main_window.setCentralWidget(scroll_area)

    # --- 1.12 Hauptfenster anzeigen ---
    main_window.setWindowState(Qt.WindowState.WindowMaximized)
    main_window.show()

    # --- 1.13 Anwendungsschleife starten ---
    sys.exit(app.exec())

if __name__ == "__main__":
    main()
