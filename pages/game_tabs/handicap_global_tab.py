# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy, QLabel, QLineEdit, QMessageBox, QGroupBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from qfluentwidgets import SubtitleLabel, BodyLabel, PushButton, LineEdit

from functions import fetchResource

# Import handicap event functions for all supported games
try:
    from events.marioParty1_handicap import handicapEvent_mp1
    from events.marioParty2_handicap import handicapEvent_mp2
    from events.marioParty3_handicap import handicapEvent_mp3
    from events.marioParty4_handicap import handicapEvent_mp4
    from events.marioParty5_handicap import handicapEvent_mp5
    from events.marioParty6_handicap import handicapEvent_mp6
    from events.marioParty7_handicap import handicapEvent_mp7
    from events.marioParty8_handicap import handicapEvent_mp8
    from events.marioParty9_handicap import handicapEvent_mp9
    from events.marioPartyDS_handicap import handicapEvent_mpDS
except ImportError:
    # Handle missing imports gracefully
    pass


class HandicapTab(QWidget):
    def __init__(self, game_id):
        super().__init__()
        self.game_id = game_id
        self.setup_ui()

    def setup_ui(self):
        """Set up the handicap tab UI"""
        self.setObjectName(f"{self.game_id}HandicapTab")
        # Main layout with reduced spacing
        layout = QVBoxLayout()
        layout.setSpacing(8)  # Reduced from 12
        layout.setContentsMargins(16, 8, 16, 8)  # Reduced top/bottom margins
        
        # Title with reduced margin
        title = SubtitleLabel("Player Star Handicaps")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Description with reduced margin
        desc = BodyLabel("Set starting star counts for each player:")
        desc.setAlignment(Qt.AlignCenter)
        layout.addWidget(desc)
        
        # Player Handicaps Card with acrylic effect
        from qfluentwidgets import CardWidget
        card = CardWidget()
        
        # Store reference to card
        self.handicap_group = card
        
        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(20, 16, 20, 16)
        card_layout.setSpacing(12)
        
        # Add title to the card
        card_title = SubtitleLabel("Player Starting Stars")
        card_title.setStyleSheet("font-size: 16px; font-weight: 600; margin-bottom: 8px;")
        card_layout.addWidget(card_title)
        
        card.setLayout(card_layout)
        
        # Use card_layout instead of group_layout for adding content
        group_layout = card_layout
        
        # Grid layout for player rows
        grid_layout = QVBoxLayout()
        grid_layout.setSpacing(8)  # Reduced from 12
        grid_layout.setContentsMargins(0, 0, 0, 0)
        
        # Player 1 Row
        p1_row = QHBoxLayout()
        p1_row.setSpacing(8)  # Reduced from 12
        
        # Add star icon
        p1_star_image = self.create_image_label("assets/eventTags/starSpace.png", 24, 24)
        p1_row.addWidget(p1_star_image)
        
        p1_label = BodyLabel("Player 1:")
        p1_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 60px;")  # Reduced min-width
        p1_row.addWidget(p1_label)
        
        self.p1_entry = LineEdit()
        self.p1_entry.setFixedWidth(50)  # Reduced from 60
        p1_row.addWidget(self.p1_entry)
        
        p1_row.addStretch()
        grid_layout.addLayout(p1_row)
        
        # Player 2 Row
        p2_row = QHBoxLayout()
        p2_row.setSpacing(8)  # Reduced from 12
        
        # Add star icon
        p2_star_image = self.create_image_label("assets/eventTags/starSpace.png", 24, 24)
        p2_row.addWidget(p2_star_image)
        
        p2_label = BodyLabel("Player 2:")
        p2_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 60px;")  # Reduced min-width
        p2_row.addWidget(p2_label)
        
        self.p2_entry = LineEdit()
        self.p2_entry.setFixedWidth(50)  # Reduced from 60
        p2_row.addWidget(self.p2_entry)
        
        p2_row.addStretch()
        grid_layout.addLayout(p2_row)
        
        # Player 3 Row
        p3_row = QHBoxLayout()
        p3_row.setSpacing(8)  # Reduced from 12
        
        # Add star icon
        p3_star_image = self.create_image_label("assets/eventTags/starSpace.png", 24, 24)
        p3_row.addWidget(p3_star_image)
        
        p3_label = BodyLabel("Player 3:")
        p3_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 60px;")  # Reduced min-width
        p3_row.addWidget(p3_label)
        
        self.p3_entry = LineEdit()
        self.p3_entry.setFixedWidth(50)  # Reduced from 60
        p3_row.addWidget(self.p3_entry)
        
        p3_row.addStretch()
        grid_layout.addLayout(p3_row)
        
        # Player 4 Row
        p4_row = QHBoxLayout()
        p4_row.setSpacing(8)  # Reduced from 12
        
        # Add star icon
        p4_star_image = self.create_image_label("assets/eventTags/starSpace.png", 24, 24)
        p4_row.addWidget(p4_star_image)
        
        p4_label = BodyLabel("Player 4:")
        p4_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 60px;")  # Reduced min-width
        p4_row.addWidget(p4_label)
        
        self.p4_entry = LineEdit()
        self.p4_entry.setFixedWidth(50)  # Reduced from 60
        p4_row.addWidget(self.p4_entry)
        
        p4_row.addStretch()
        grid_layout.addLayout(p4_row)
        
        # Add grid layout to group
        group_layout.addLayout(grid_layout)
        
        # Add card to main layout
        layout.addWidget(card)
        
        # Generate button
        generate_btn = PushButton("Generate Codes")
        generate_btn.clicked.connect(self.generate_codes)
        layout.addWidget(generate_btn)
        
        # Add stretch to push everything up
        layout.addStretch()
        
        self.setLayout(layout)

    def create_image_label(self, image_path, width=24, height=24):
        """Create a QLabel with an image from the assets folder"""
        try:
            # Get the image path from resource manager
            from utils.resource_manager import ResourceManager
            image_path = ResourceManager.get_resource_path(image_path)
            
            # Create QLabel and set image
            image_label = QLabel()
            pixmap = QPixmap(str(image_path))
            
            if not pixmap.isNull():
                # Scale the image to the specified dimensions
                scaled_pixmap = pixmap.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation)
                image_label.setPixmap(scaled_pixmap)
                image_label.setFixedSize(width, height)
                image_label.setAlignment(Qt.AlignCenter)
            else:
                # Fallback text if image fails to load
                image_label.setText("?")
                image_label.setFixedSize(width, height)
                image_label.setAlignment(Qt.AlignCenter)
                image_label.setStyleSheet("border: 1px solid gray; background: lightgray;")
            
            return image_label
            
        except Exception as e:
            # Fallback if image creation fails
            fallback_label = QLabel("?")
            fallback_label.setFixedSize(width, height)
            fallback_label.setAlignment(Qt.AlignCenter)
            fallback_label.setStyleSheet("border: 1px solid gray; background: lightgray;")
            return fallback_label

    def generate_codes(self):
        """Generate codes for the current game"""
        try:
            # Create mock objects to match the expected interface
            class MockEntry:
                def __init__(self, text):
                    self._text = text
                def get(self):
                    return self._text
                def text(self):
                    return self._text
            
            # Create mock objects with current values
            p1_stars = MockEntry(self.p1_entry.text())
            p2_stars = MockEntry(self.p2_entry.text())
            p3_stars = MockEntry(self.p3_entry.text())
            p4_stars = MockEntry(self.p4_entry.text())
            
            # Call appropriate handicap event function based on game
            if self.game_id == "marioParty1" and 'handicapEvent_mp1' in globals():
                handicapEvent_mp1(p1_stars, p2_stars, p3_stars, p4_stars)
            elif self.game_id == "marioParty2" and 'handicapEvent_mp2' in globals():
                handicapEvent_mp2(p1_stars, p2_stars, p3_stars, p4_stars)
            elif self.game_id == "marioParty3" and 'handicapEvent_mp3' in globals():
                handicapEvent_mp3(p1_stars, p2_stars, p3_stars, p4_stars)
            elif self.game_id == "marioParty4" and 'handicapEvent_mp4' in globals():
                handicapEvent_mp4(p1_stars, p2_stars, p3_stars, p4_stars)
            elif self.game_id == "marioParty5" and 'handicapEvent_mp5' in globals():
                handicapEvent_mp5(p1_stars, p2_stars, p3_stars, p4_stars)
            elif self.game_id == "marioParty6" and 'handicapEvent_mp6' in globals():
                handicapEvent_mp6(p1_stars, p2_stars, p3_stars, p4_stars)
            elif self.game_id == "marioParty7" and 'handicapEvent_mp7' in globals():
                handicapEvent_mp7(p1_stars, p2_stars, p3_stars, p4_stars)
            elif self.game_id == "marioParty8" and 'handicapEvent_mp8' in globals():
                handicapEvent_mp8(p1_stars, p2_stars, p3_stars, p4_stars)
            elif self.game_id == "marioParty9" and 'handicapEvent_mp9' in globals():
                handicapEvent_mp9(p1_stars, p2_stars, p3_stars, p4_stars)
            elif self.game_id == "marioPartyDS" and 'handicapEvent_mpDS' in globals():
                handicapEvent_mpDS(p1_stars, p2_stars, p3_stars, p4_stars)
            else:
                self.show_error(f"Handicap modification not available for {self.game_id}")
        except Exception as e:
            self.show_error(f"Error generating codes: {str(e)}")
    
    def show_error(self, message):
        """Show error message to user"""
        QMessageBox.critical(self, "Error", message)
    
    def update_handicap_group_theme(self):
        """Update the handicap group styling based on current theme"""
        from qfluentwidgets import isDarkTheme
        if isDarkTheme():
            self.handicap_group.setStyleSheet("""
                QGroupBox {
                    font-size: 16px;
                    font-weight: 600;
                    color: palette(text);
                    border: 2px solid palette(mid);
                    border-radius: 8px;
                    margin-top: 8px;
                    padding-top: 8px;
                    background: #3c3c3c;
                }
                QGroupBox::title {
                    subcontrol-origin: margin;
                    left: 16px;
                    padding: 0 8px 0 8px;
                    background: palette(highlight);
                    color: palette(highlighted-text);
                    border-radius: 6px;
                    font-weight: 700;
                }
            """)
        else:
            self.handicap_group.setStyleSheet("""
                QGroupBox {
                    font-size: 16px;
                    font-weight: 600;
                    color: palette(text);
                    border: 2px solid palette(mid);
                    border-radius: 8px;
                    margin-top: 8px;
                    padding-top: 8px;
                    background: #ffffff;
                }
                QGroupBox::title {
                    subcontrol-origin: margin;
                    left: 16px;
                    padding: 0 8px 0 8px;
                    background: palette(highlight);
                    color: palette(highlighted-text);
                    border-radius: 6px;
                    font-weight: 700;
                }
            """)
    
    def themeChanged(self):
        """Called when theme changes - update all styling"""
        self.update_handicap_group_theme()
