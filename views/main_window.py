from PyQt6.QtWidgets import QMainWindow, QScrollArea, QWidget, QVBoxLayout, QLabel, QApplication
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPalette, QPixmap, QBrush

# ---- 2.Hauptfenster-Klasse ----
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setup_ui()
    # --- 2.1 Hauptfenster-Initialisierung ---
    def setup_ui(self):
        """Erstellung der Benutzeroberfläche"""
        # -- 2.1.1 Hauptfenster-Titel --
        self.setWindowTitle("ECO-Game")

        # -- 2.1.2 Bildschrimgröße ermitteln --
        screen = QApplication.primaryScreen() # Hauptbildschirm
        self.screen_size = screen.size() # Größe als Instanzvariable speichern

        # -- 2.1.3 Hintergrund und Layout erstellen --
        self.setup_background() # Hintergrundfuktion aufrufen
        self.setup_layout() # Layoutfunktion aufrufen

        # -- 2.1.4 Fenster maximieren --
        self.setWindowState(Qt.WindowState.WindowMaximized)

    # --- 2.2 Hintergrund-Initialisierung ---
    def setup_background(self):
        """Setzt das Hintergrundbild"""
        # -- 2.2.1 Palette erstellen --
        palette = QPalette()

        # -- 2.2.2 Bild laden --
        pixmap = QPixmap("ECO_BG_image.jpeg")

        # -- 2.2.3 Bild auf Bildschirmgröße skalieren --
        scaled_pixmap = pixmap.scaled(
            self.screen_size,
            Qt.AspectRatioMode.KeepAspectRatioByExpanding,
            Qt.TransformationMode.SmoothTransformation
        )

        # -- 2.2.4 Bild als Hintergrund setzen --
        palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_pixmap))

        # -- 2.2.5 Palette auf Fenster anwenden --
        self.setPalette(palette)

    # --- 2.3 Haupt-Layout-Initialisierung ---
    def setup_layout(self):
        """Haupt-Layout-Initiierung"""
        # -- 2.3.1 Scrollbereich erstellen --
        scroll_area = QScrollArea() # Contaainer der scrollen kann
        content_widget = QWidget() # Das Widget das gecrollt wird
        layout = QVBoxLayout(content_widget) # Vertikales Layout für content_widget

        # -- 2.3.2 Titel-Label erstellen --
        self.title_label = QLabel("ECO- Hauptmenü") # Labelname
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter) # Zentrierung
        self.title_label.setStyleSheet(
            "font-size: 24px; font-weight: bold; color: white; "
            "background-color: rgba(0,0,0,100); padding: 20px; border-radius: 10px;"  # background-color (klein)
        ) # StSh angewendet

        # -- 2.3.3 Label zim Layout hinzufügen --
        layout.addWidget(self.title_label)

        # -- 2.3.4 Scroll-Area konfigurieren --
        scroll_area.setWidget(content_widget) # content_widget in ScrollArea
        scroll_area.setWidgetResizable(True) # Widget kann sich anpassen
        scroll_area.setStyleSheet("background: transparent;") # Tarnsparenter Hintergrund

        # -- 2.3.5 Scroll-Area als Hauptinhalt setzen --
        self.setCentralWidget(scroll_area)

    # --- 2.4 Titel-Label-Update  ---
    def update_title(self, title):
        """Aktualisiert den Titel (Für CONTROLLER)"""
        self.title_label.setText(title)   