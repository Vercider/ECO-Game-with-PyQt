from PyQt6.QtWidgets import (QMainWindow, QScrollArea, QWidget, QVBoxLayout, 
                            QHBoxLayout, QGridLayout, QLabel, QApplication, 
                            QPushButton, QFrame)
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
        
        # -- 2.1.2 Bildschirmgröße ermitteln --
        screen = QApplication.primaryScreen()
        self.screen_size = screen.size()
        
        # -- 2.1.3 Hintergrund und Layout erstellen --
        self.setup_background()  # ✅ HINZUGEFÜGT
        self.setup_layout()      # ✅ HINZUGEFÜGT
        
        # -- 2.1.4 Fenster maximieren --
        self.setWindowState(Qt.WindowState.WindowMaximized)

    # --- 2.2 Hintergrund-Initialisierung ---
    def setup_background(self):
        """Setzt das Hintergrundbild"""
        # -- 2.2.1 Palette erstellen --
        palette = QPalette()
        pixmap = QPixmap("ECO_BG_image.jpeg")
        
        # -- 2.2.2 Bild skalieren --
        scaled_pixmap = pixmap.scaled(
            self.screen_size, 
            Qt.AspectRatioMode.KeepAspectRatioByExpanding, 
            Qt.TransformationMode.SmoothTransformation
        )
        
        # -- 2.2.3 Hintergrund setzen --
        palette.setBrush(QPalette.ColorRole.Window, QBrush(scaled_pixmap))
        self.setPalette(palette)

    # --- 2.3 Haupt-Layout-Initialisierung ---
    def setup_layout(self):
        """Haupt-Layout-Initiierung"""
        # -- 2.3.1 Scrollbereich erstellen --
        scroll_area = QScrollArea()
        main_widget = QWidget()
        main_widget.setMinimumSize(1400, 900) # min. Layout für Scrollbereich

        # -- 2.3.2 Grid-Layout --
        grid_layout = QGridLayout(main_widget) # Grid-Umbau
        grid_layout.setSpacing(5)

        # Spalten-Verhältnis "Links" Labels + Buttons / "Mitte" Hauptausgabe / "Rechts" Buttons
        grid_layout.setColumnStretch(0, 1) # Links: 1 Teilstück
        grid_layout.setColumnStretch(1, 3) # Mitte: 3 Teilstücke
        grid_layout.setColumnStretch(2, 1) # Rechts: 1 Teilstück

        # Zeilen-Verhältnis
        grid_layout.setRowStretch(0, 0) # Header: fest definierte Höhe
        grid_layout.setRowStretch(1, 2) # Hauptbereich: 2 Teilstücke
        grid_layout.setRowStretch(2, 1) # Bau-Ebene: 1 Teilstück  

        # -- 2.3.3 Layout-Bereiche erstellen --
        self.create_header(grid_layout)
        self.create_left_panel(grid_layout)
        self.create_main_output(grid_layout)
        self.create_right_panel(grid_layout)
        self.create_building_area(grid_layout)

        # -- 2.3.4 Scroll-Area konfigurieren --
        scroll_area.setWidget(main_widget)
        scroll_area.setWidgetResizable(False)
        scroll_area.setStyleSheet("background: transparent;")

        # -- 2.3.5 Scroll-Area als Hauptinhalt setzen --
        self.setCentralWidget(scroll_area)

    # --- 2.4 Grid-Einzelelemente erschaffen und einbinden ---
    def create_header(self, grid_layout):
        """Header mit Spieletitel erschaffen"""
        header_frame = QFrame()
        header_frame.setFixedHeight(60)
        header_frame.setStyleSheet("""
            QFrame { 
                background-color: rgba(173, 216, 230, 200); 
                border: 2px solid black;
                border-radius: 5px;
            }
        """)

        header_layout = QHBoxLayout(header_frame)
        self.title_label = QLabel("Eco -Die Wirtschaftsaufbausimulation")
        self.title_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.title_label.setStyleSheet("font-size: 20px; font-weight: bold; color: black;")
        header_layout.addWidget(self.title_label)

        grid_layout.addWidget(header_frame, 0, 0, 1, 3)

    # --- 2.5 Linkes Panel ---
        # -- 2.5.1 Frame-Bindung für Linken Frame
    def create_left_panel(self, grid_layout):
        """Linkes Panel: Ressourcen, Bevölkerung, START, BAUEN"""
        left_frame = QFrame()
        left_frame.setStyleSheet("QFrame { border: 2px solid black; background-color: rgba(255,255,255,150); }")
        left_layout = QVBoxLayout(left_frame)
        left_layout.setSpacing(10)

        # -- 2.5.2 Ressourcen-Anzeige --
        ressources_frame = QFrame()
        ressources_frame.setStyleSheet("""
            QFrame { 
                background-color: white; 
                border: 1px solid gray; 
                border-radius: 3px; 
                padding: 5px;
            }
        """)
        ressources_layout = QVBoxLayout(ressources_frame)

        ressources_title = QLabel("Ressourcen")
        ressources_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        ressources_title.setStyleSheet("font-weight: bold; font-size: 14px;")
        ressources_layout.addWidget(ressources_title)

        self.food_label = QLabel("Nahrung: 0")
        self.food_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.wood_label = QLabel("Holz: 0")
        self.wood_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.stone_label = QLabel("Stein: 0")
        self.stone_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        for label in [self.food_label, self.wood_label, self.stone_label]:
            label.setStyleSheet("font-size: 12px; padding: 2px;")
            ressources_layout.addWidget(label)

        # -- 2.5.3 Bevölkerung-Anzeige --
        population_frame = QFrame()
        population_frame.setStyleSheet("""
            QFrame { 
                background-color: white; 
                border: 1px solid gray; 
                border-radius: 3px; 
                padding: 5px;
            }
        """)
        population_layout = QVBoxLayout(population_frame)

        population_title = QLabel("Bevölkerung")
        population_title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        population_title.setStyleSheet("font-weight: bold; font-size: 14px;")
        population_layout.addWidget(population_title)

        self.population_label = QLabel("0 / 0 / 0")
        self.population_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.population_label.setStyleSheet("font-size: 12px; padding: 2px;")
        population_layout.addWidget(self.population_label)

        # -- 2.5.4 START-Button --
        self.start_button = QPushButton("START")
        self.start_button.setFixedSize(300, 125)
        self.start_button.setStyleSheet("""
            QPushButton { 
                background-color: lightgreen; 
                font-weight: bold; 
                font-size: 25px;
                border: 2px solid darkgreen;
                border-radius: 5px;
                padding: 8px;
            }
            QPushButton:hover { background-color: green; }
        """)

        # -- 2.5.5 BAUEN-Button --
        self.build_button = QPushButton("BAUEN")
        self.build_button.setFixedSize(300, 125)
        self.build_button.setStyleSheet("""
            QPushButton { 
                background-color: lightblue; 
                font-weight: bold; 
                font-size: 25px;
                border: 2px solid darkblue;
                border-radius: 5px;
                padding: 8px;
            }
            QPushButton:hover { background-color: blue; color: white; }
        """)

        # -- 2.5.6 Layout zusammenfügen --
        left_layout.addWidget(ressources_frame)
        left_layout.addWidget(population_frame)
        left_layout.addWidget(self.start_button)
        left_layout.addWidget(self.build_button)

        grid_layout.addWidget(left_frame, 1, 0, 1, 1)

    # --- 2.6 Hauptausgabe ---
        # -- 2.6.1 Frame Einbindung für Mitte Frame --
    def create_main_output(self, grid_layout):
        """Zentrale Hauptausgabe"""
        main_frame = QFrame()
        main_frame.setStyleSheet("""
            QFrame { 
                background-color: black; 
                border: 2px solid gray;
                border-radius: 5px;
            }
        """)

        # -- 2.6.2 Hauptausgabe-Label definieren -- 
        main_layout = QVBoxLayout(main_frame)

        # -- 2.6.3 Text für Hauptausgabe definieren --
        self.main_output_text = QLabel("Willkommen bei ECO!\n\nDrücke START um ein Spiel zu starten oder\n LADEN um einen Spielstand zu laden.")
        self.main_output_text.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.main_output_text.setWordWrap(True)
        self.main_output_text.setStyleSheet("""
            color: white; 
            font-size: 35px; 
            padding: 15px;
        """)

        main_layout.addWidget(self.main_output_text)

        grid_layout.addWidget(main_frame, 1, 1, 1, 1)
    
    # --- 2.7 Rechtes Panel ---
        # -- 2.7.1 Frame Einbindung für Rechten Frame --
    def create_right_panel(self, grid_layout):
        """Rechtes Panel: Nächste Runde, SPEICHERN, LADEN"""
        right_frame = QFrame()
        right_frame.setStyleSheet("QFrame { border: 2px solid black; background-color: rgba(255,255,255,150); }")
        right_layout = QVBoxLayout(right_frame)
        right_layout.setSpacing(15)

        # -- 2.7.2 Nächste Runde Button --
        self.next_round_button = QPushButton("Nächste Runde")
        self.next_round_button.setFixedSize(300, 250)
        self.next_round_button.setStyleSheet("""
            QPushButton { 
                background-color: lightgray; 
                font-weight: bold; 
                font-size: 30px;
                border: 2px solid darkgray;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover { background-color: gray; }
        """)
        
        # -- 2.7.3 Speichern Button --
        self.save_button = QPushButton("SPEICHERN")
        self.save_button.setFixedSize(300, 125)
        self.save_button.setStyleSheet("""
            QPushButton { 
                background-color: lightblue; 
                font-weight: bold; 
                font-size: 25px;
                border: 2px solid darkblue;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover { background-color: blue; color: white; }
        """)

        # -- 2.7.4 Laden Button --
        self.load_button = QPushButton("LADEN")
        self.load_button.setFixedSize(300, 125)
        self.load_button.setStyleSheet("""
            QPushButton { 
                background-color: orange; 
                font-weight: bold; 
                font-size: 25px;
                border: 2px solid darkorange;
                border-radius: 5px;
                padding: 10px;
            }
            QPushButton:hover { background-color: darkorange; }
        """)

        # -- 2.7.5 Layout zusammenfügen --
        right_layout.addWidget(self.next_round_button)
        right_layout.addWidget(self.save_button)
        right_layout.addWidget(self.load_button)
        right_layout.addStretch(2)

        grid_layout.addWidget(right_frame, 1, 2, 1, 1)

    # --- 2.8 Bau-Ebene ---
        # -- 2.8.1 Frame Einbindung für Bau Frame --
    def create_building_area(self, grid_layout):
        """Bau-Ebene mit Gebäude-Icons"""
        building_frame = QFrame()
        building_frame.setStyleSheet("""
            QFrame { 
                border: 2px solid black; 
                background-color: rgba(245,245,245,200);
                border-radius: 5px;
            }
        """)

        building_layout = QVBoxLayout(building_frame)
        building_layout.setContentsMargins(5, 5, 5, 5)
        building_layout.setSpacing(0)

        # -- 2.8.2 Bau-Ebenen-Label --
        icons_layout = QHBoxLayout()
        icons_layout.setContentsMargins(0, 0, 0, 0)  

        buildings = ["🏠 Haus", "🪚 Sägewerk", "⛰️ Steinbruch", "🌾 Farm", "🏪 Markt"]
        self.build_buttons = []

        for building in buildings:
            button = QPushButton(building)
            button.setStyleSheet("""
                QPushButton { 
                    background-color: white; 
                    border: 2px solid gray;
                    border-radius: 8px;
                    padding: 15px;
                    font-size: 12px;
                    min-width: 80px;
                    min-height: 60px;
                }
                QPushButton:hover { 
                    background-color: lightblue; 
                    border-color: blue;
                }
            """)
            self.build_buttons.append(button)
            icons_layout.addWidget(button)
        
        icons_layout.addStretch()
        building_layout.addLayout(icons_layout)
        building_layout.addStretch()

        grid_layout.addWidget(building_frame, 2, 0, 1, 3)
    
    # --- 2.9 Update-Methoden ---
        # -- 2.9.1 Update-Ressourcen --
    def update_ressources(self, food, wood, stone):
        """Aktualisiert die Ressourcenanzeige"""
        self.food_label.setText(f"Nahrung: {food}")
        self.wood_label.setText(f"Holz: {wood}")
        self.stone_label.setText(f"Stein: {stone}")

        # -- 2.9.2 Update-Bevölkerung --
    def update_population(self, current, max_pop):
        """Aktualisiert die Bevölkerungsanzeige"""
        self.population_label.setText(f"{current} / {max_pop}")

        # -- 2.9.3 Update_Hauptausgabe --
    def update_main_output(self, text):
        """Aktualisiert die Hauptausgabe"""
        self.main_output_text.setText(text)
    
    # --- 2.10 Titel-Label-Update ---
    def update_title(self, title):
        """Aktualsiert den Titel"""
        self.title_label.setText(title)









        

        
    