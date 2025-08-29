from PyQt6.QtWidgets import (QMainWindow, QScrollArea, QWidget, QVBoxLayout, 
                            QHBoxLayout, QGridLayout, QLabel, QApplication, 
                            QPushButton, QFrame)
from PyQt6.QtCore import Qt
from PyQt6.QtGui import QPixmap, QPalette, QBrush

# ---- 2. Hauptfenster-Klasse ----
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        
        # ✅ FALLBACK: Standard-Werte setzen
        self.button_width = 200
        self.font_size_medium = 16
        self.min_layout_width = 1400
        self.min_layout_height = 900
        
        self.setup_ui()

    # --- 2.1 UI-Setup ---
    def setup_ui(self):
        """Erstellung der Benutzeroberfläche"""
        # -- 2.1.1 Hauptfenster-Titel --
        self.setWindowTitle("ECO-Game")
        
        # -- 2.1.2 Bildschirmgröße ermitteln --
        screen = QApplication.primaryScreen()
        self.screen_size = screen.size()

        # -- 2.1.3 Responsive-Funktion --
        self.calc_responsive_sizes()

        # -- 2.1.4 Hintergrund und Layout erstellen --
        self.setup_background()
        self.setup_layout()
        
        # -- 2.1.5 Fenster maximieren --
        self.setWindowState(Qt.WindowState.WindowMaximized)

    def calc_responsive_sizes(self):
        """Berechnet responsive Größen basierend auf Bildschirmgröße"""
        self.base_width = self.screen_size.width()
        self.base_height = self.screen_size.height()
        
        # Button-Breiten
        self.button_width = int(self.base_width * 0.15)
        
        # ✅ FINALE Button-Höhen
        self.button_height_combined = 250    # Für "Nächste Runde"
        self.button_height_large = 90        # Für START, BAUEN, SPEICHERN, LADEN
        self.button_height_small = 60        # Für Bau-Buttons
        
        # Schriftgrößen
        self.font_size_medium = max(int(self.base_height * 0.018), 14)
        
        # ✅ ZURÜCK AUF ORIGINAL: Layout-Größen
        self.min_layout_width = int(self.base_width * 0.95)
        self.min_layout_height = int(self.base_height * 0.8)

    # --- 2.1.6 Shadow-Push-Button Methode mit anpassbarer Schriftgröße ---
    def create_shadow_push_button(self, text, color, hover_color, height, text_color="white", hover_text_color="white", font_multiplier=1.0):
        """Button mit Schatten-Push-Effekt und anpassbarer Schriftgröße"""
        button = QPushButton(text)
        button.setFixedHeight(height)
        button.setStyleSheet(f"""
            QPushButton {{ 
                background-color: {color};
                color: {text_color};
                font-weight: bold; 
                font-size: {int(self.font_size_medium * font_multiplier)}px;
                border: 2px solid black;
                border-radius: 8px;
                padding: 8px;
                /* Schatten-Effekt simulieren */
                margin: 0px 4px 4px 0px;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 {color}, stop:1 darker({color}));
            }}
            QPushButton:hover {{ 
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 {hover_color}, stop:1 darker({hover_color}));
                color: {hover_text_color};
                margin: 1px 3px 3px 1px;
            }}
            QPushButton:pressed {{ 
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 darker({hover_color}), stop:1 {hover_color});
                color: {hover_text_color};
                margin: 2px 2px 2px 2px;  /* Komplett "eingedrückt" */
                padding: 6px;
            }}
        """)
        return button

    # --- 2.2 Hintergrund-Setup ---
    def setup_background(self):
        """✅ KORRIGIERT: Richtiges Hintergrundbild verwenden"""
        try:
            # -- 2.2.1 ✅ RICHTIGES Hintergrundbild laden --
            background_path = "pics/ECO_BG_image.jpeg"  # ✅ Das mittelalterliche Dorf-Bild
            pixmap = QPixmap(background_path)
            
            if pixmap.isNull():
                raise FileNotFoundError("Hintergrundbild nicht gefunden")
            
            # -- 2.2.2 Hintergrundbild skalieren --
            scaled_pixmap = pixmap.scaled(self.size(), Qt.AspectRatioMode.KeepAspectRatioByExpanding, Qt.TransformationMode.SmoothTransformation)
            
            # -- 2.2.3 Hintergrundbild als Palette setzen --
            palette = self.palette()
            palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_pixmap))
            self.setPalette(palette)
        except:
            # ✅ Fallback: Braun/Beige-Farben passend zum mittelalterlichen Thema
            self.setStyleSheet("background-color: #8B7355;")  # Erdbraun

    # --- 2.3 Haupt-Layout-Initialisierung ---
    def setup_layout(self):
        """Haupt-Layout-Initiierung"""
        # -- 2.3.1 Scrollbereich erstellen --
        scroll_area = QScrollArea()
        main_widget = QWidget()
        main_widget.setMinimumSize(self.min_layout_width, self.min_layout_height)

        # -- 2.3.2 Grid-Layout --
        grid_layout = QGridLayout(main_widget)
        grid_layout.setSpacing(5)
        grid_layout.setContentsMargins(5, 5, 5, 5)

        # Spalten-Verhältnis
        grid_layout.setColumnStretch(0, 2) # Links: 2 Teilstücke
        grid_layout.setColumnStretch(1, 4) # Mitte: 4 Teilstücke
        grid_layout.setColumnStretch(2, 2) # Rechts: 2 Teilstücke

        # Zeilen-Verhältnis
        grid_layout.setRowStretch(0, 0) # Header: Feste Höhe
        grid_layout.setRowStretch(1, 3) # Hauptbereich: 3 Teile
        grid_layout.setRowStretch(2, 1) # Bau-Ebene: 1 Teil

        # -- 2.3.3 Layout-Bereiche erstellen --
        self.create_header(grid_layout)
        self.create_left_panel(grid_layout)
        self.create_main_output(grid_layout)
        self.create_right_panel(grid_layout)
        self.create_building_area(grid_layout)

        # -- 2.3.4 ✅ ZURÜCK AUF ORIGINAL: Scroll-Area konfigurieren --
        scroll_area.setWidget(main_widget)
        scroll_area.setWidgetResizable(True)
        scroll_area.setStyleSheet("background: transparent;")

        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAsNeeded)

        # -- 2.3.5 Scroll-Area als Hauptinhalt setzen --
        self.setCentralWidget(scroll_area)

    # --- 2.4 Header-Bereich ---
    def create_header(self, grid_layout):
        """Header mit transparentem Hintergrund"""
        # -- 2.4.1 Header-Frame --
        header_frame = QFrame()
        header_frame.setStyleSheet("QFrame { border: 2px solid black; background-color: rgba(173, 216, 230, 180); }")
        header_layout = QHBoxLayout(header_frame)

        # -- 2.4.2 Titel-Label --
        self.title_label = QLabel("ECO - Hauptmenü")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet(f"font-size: {int(self.font_size_medium * 1.5)}px; font-weight: bold; color: black;")

        # -- 2.4.3 Header-Layout --
        header_layout.addWidget(self.title_label)
        grid_layout.addWidget(header_frame, 0, 0, 1, 3)

    # --- 2.5 Linkes Panel ---
    def create_left_panel(self, grid_layout):
        """Linkes Panel mit passenden mittelalterlichen Farben"""
        left_frame = QFrame()
        left_frame.setStyleSheet("QFrame { border: 2px solid black; background-color: transparent; }")
        left_layout = QVBoxLayout(left_frame)
        left_layout.setSpacing(10)
        left_layout.setContentsMargins(10, 10, 10, 10)

        # -- 2.5.1 ✅ Ressourcen-Frame mit mittelalterlichen Farben --
        resources_frame = QFrame()
        resources_frame.setStyleSheet("""
            QFrame { 
                border: 2px solid #8B4513; 
                border-radius: 8px;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #F5DEB3, stop:1 #DEB887);
                margin: 2px 4px 4px 2px;  /* ✅ Qt-Schatten */
            }
        """)  # ✅ Braun/Beige
        resources_layout = QVBoxLayout(resources_frame)
        resources_layout.setContentsMargins(5, 5, 5, 5)

        # -- 2.5.2 ✅ Ressourcen-Titel mit Hintergrund --
        resources_title = QLabel("Ressourcen")
        resources_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        resources_title.setStyleSheet(f"""
            font-weight: bold; 
            font-size: {self.font_size_medium}px; 
            color: #654321;
            background-color: #F5DEB3;
        """)  # ✅ Gleicher Hintergrund wie Frame

        # -- 2.5.3 ✅ Ressourcen-Labels mit Hintergrund --
        self.food_label = QLabel("🌾 Nahrung: 0")
        self.food_label.setStyleSheet(f"""
            font-size: {self.font_size_medium}px; 
            color: #8B4513;
            background-color: #F5DEB3;
        """)  # ✅ Gleicher Hintergrund wie Frame
        self.food_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.wood_label = QLabel("🪵 Holz: 0")
        self.wood_label.setStyleSheet(f"""
            font-size: {self.font_size_medium}px; 
            color: #8B4513;
            background-color: #F5DEB3;
        """)  # ✅ Gleicher Hintergrund wie Frame
        self.wood_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.stone_label = QLabel("🗿 Stein: 0")
        self.stone_label.setStyleSheet(f"""
            font-size: {self.font_size_medium}px; 
            color: #8B4513;
            background-color: #F5DEB3;
        """)  # ✅ Gleicher Hintergrund wie Frame
        self.stone_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Ressourcen-Layout zusammenfügen
        resources_layout.addWidget(resources_title)
        resources_layout.addWidget(self.food_label)
        resources_layout.addWidget(self.wood_label)
        resources_layout.addWidget(self.stone_label)

        # -- 2.5.4 ✅ Bevölkerungs-Frame mit mittelalterlichen Farben --
        population_frame = QFrame()
        population_frame.setStyleSheet("""
            QFrame { 
                border: 2px solid #4B0082; 
                border-radius: 12px;
                background: qlineargradient(x1:0, y1:0, x2:0, y2:1,
                    stop:0 #E6E6FA, stop:0.3 #DDA0DD, stop:1 #D8BFD8);
                margin: 2px 4px 4px 2px;
            }
        """)  # ✅ Lila/Lavendel
        population_layout = QVBoxLayout(population_frame)
        population_layout.setContentsMargins(5, 5, 5, 5)

        # -- 2.5.5 ✅ Bevölkerungs-Titel mit Hintergrund --
        population_title = QLabel("Bevölkerung")
        population_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        population_title.setStyleSheet(f"""
            font-weight: bold; 
            font-size: {self.font_size_medium}px; 
            color: #4B0082;
            background-color: #E6E6FA;
        """)  # ✅ Gleicher Hintergrund wie Frame

        # -- 2.5.6 ✅ Bevölkerungs-Label mit Hintergrund --
        self.population_label = QLabel("👥 0 / 0 / 0")
        self.population_label.setStyleSheet(f"""
            font-size: {self.font_size_medium}px; 
            color: #4B0082;
            background-color: #E6E6FA;
        """)  # ✅ Gleicher Hintergrund wie Frame
        self.population_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        # Bevölkerungs-Layout zusammenfügen
        population_layout.addWidget(population_title)
        population_layout.addWidget(self.population_label)

        # -- 2.5.7 START Button --
        self.start_button = self.create_shadow_push_button(
            "START", 
            "green",
            "darkgreen",
            self.button_height_large,
            "white",
            "white"
        )

        # -- 2.5.8 BAUEN Button --
        self.build_button = self.create_shadow_push_button(
            "BAUEN", 
            "lightblue",
            "blue",
            self.button_height_large,
            "black",
            "white"
        )

        # -- 2.5.9 Layout zusammenfügen --
        left_layout.addWidget(resources_frame)
        left_layout.addWidget(population_frame)  
        left_layout.addWidget(self.start_button)
        left_layout.addWidget(self.build_button)
        left_layout.addStretch()

        grid_layout.addWidget(left_frame, 1, 0, 1, 1)

    # --- 2.6 Haupt-Ausgabebereich ---
    def create_main_output(self, grid_layout):
        """Haupt-Ausgabebereich mit transparentem Hintergrund"""
        # -- 2.6.1 Haupt-Output-Frame --
        main_output_frame = QFrame()
        main_output_frame.setStyleSheet("QFrame { border: 2px solid black; background-color: rgba(0, 0, 0, 180); }")
        main_output_layout = QVBoxLayout(main_output_frame)

        # -- 2.6.2 Haupt-Output-Text --
        self.main_output_text = QLabel("Willkommen bei ECO!\n\nDrücke START um ein Spiel zu starten oder\nLADEN um einen Spielstand zu laden.")
        self.main_output_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_output_text.setStyleSheet(f"color: white; font-size: {int(self.font_size_medium * 2.0)}px; font-weight: bold;")

        # -- 2.6.3 Haupt-Output-Layout --
        main_output_layout.addWidget(self.main_output_text)
        grid_layout.addWidget(main_output_frame, 1, 1, 1, 1)

    # --- 2.7 Rechtes Panel ---
    def create_right_panel(self, grid_layout):
        """Rechtes Panel mit vergrößertem "Nächste Runde" Button"""
        right_frame = QFrame()
        right_frame.setStyleSheet("QFrame { border: 2px solid black; background-color: transparent; }")
        right_layout = QVBoxLayout(right_frame)
        right_layout.setSpacing(10)
        right_layout.setContentsMargins(10, 10, 10, 10)

        # -- 2.7.1 ✅ VERGRÖßERTER "Nächste Runde" Button --
        self.next_round_button = self.create_shadow_push_button(
            "Nächste\nRunde", 
            "lightgray",
            "gray",
            self.button_height_combined,  # ✅ Jetzt 250px statt 185px
            "black",
            "white",
            2.2  # ✅ Noch größere Schrift (war 1.8)
        )

        # -- 2.7.2 SPEICHERN Button --
        self.save_button = self.create_shadow_push_button(
            "SPEICHERN", 
            "lightblue",
            "blue",
            self.button_height_large,
            "black",
            "white"
        )

        # -- 2.7.3 LADEN Button --
        self.load_button = self.create_shadow_push_button(
            "LADEN", 
            "orange",
            "darkorange",
            self.button_height_large,
            "black",
            "white"
        )

        # -- 2.7.4 Layout zusammenfügen --
        right_layout.addWidget(self.next_round_button)
        right_layout.addWidget(self.save_button)
        right_layout.addWidget(self.load_button)
        right_layout.addStretch()

        grid_layout.addWidget(right_frame, 1, 2, 1, 1)

    # --- 2.8 Bau-Bereich (UNVERÄNDERT - nur Platzhalter) ---
    def create_building_area(self, grid_layout):
        """Bau-Bereich mit einfachen Platzhalter-Buttons"""
        # -- 2.8.1 Bau-Frame --
        building_frame = QFrame()
        building_frame.setStyleSheet("QFrame { border: 2px solid black; background-color: transparent; }")
        self.building_layout = QHBoxLayout(building_frame)

        grid_layout.addWidget(building_frame, 2, 0, 1, 3)  # ✅ Frame zu Grid hinzufügen

    # --- 2.9 Update-Methoden ---
    def update_resources(self, food, wood, stone):
        """Aktualisiert die Ressourcenanzeige"""
        self.food_label.setText(f"🌾 Nahrung: {food}")
        self.wood_label.setText(f"🪵 Holz: {wood}")
        self.stone_label.setText(f"🗿 Stein: {stone}")

    def update_population(self, avail_worker, current_worker , max_worker):
        """Aktualisiert die Bevölkerungsanzeige"""
        self.population_label.setText(f"👥 {avail_worker} / {current_worker} / {max_worker}")

    def update_main_output(self, text):
        """Aktualisiert die Hauptausgabe"""
        self.main_output_text.setText(text)

    # --- 2.10 START-Button-Controller-Verbindung ---
    def set_controller(self, controller):
        """Controller setzen und Button-Events verbinden"""
        self.controller = controller
        self.start_button.clicked.connect(controller.on_start_game)

    # --- 2.11 Gebäude bauen ---
    def add_building_to_area(self, building_type, state="building"):
        """Fügt Gebäude zum Bau-Bereich hinzu"""
        # building types: "Bauernhof", "Holzverschlag", "Hütte", "Steinbruch" als Dateinamen
        try:
            pixmap = QPixmap(f"pics/{building_type}.png")
            if not pixmap.isNull():
                building_icon = QLabel()
                building_icon.setPixmap(pixmap.scaled(
                    self.button_height_large,
                    self.button_height_large,
                    Qt.AspectRatioMode.KeepAspectRatio,
                    Qt.TransformationMode.SmoothTransformation
                ))
                building_icon.setAlignment(Qt.AlignmentFlag.AlignCenter)

                self.building_layout.addWidget(building_icon)
        except Exception as e:
            print(f"Fehler beim laden von {building_type}.png: {e}")











