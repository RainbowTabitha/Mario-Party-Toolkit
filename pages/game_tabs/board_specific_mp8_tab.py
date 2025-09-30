# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

# ============================================
# Board Specific Tab Component for Mario Party 8
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtCore import Qt
from qfluentwidgets import SubtitleLabel, BodyLabel, PushButton, CardWidget, LineEdit

try:
    from events.marioParty8_boardSpecific import hotelMaxInvestEvent_mp8
except ImportError:
    hotelMaxInvestEvent_mp8 = None


class BoardSpecificMp8Tab(QWidget):
    def __init__(self, game_id: str):
        super().__init__()
        self.game_id = game_id
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName(f"{self.game_id}BoardSpecificTab")

        layout = QVBoxLayout()
        layout.setSpacing(8)
        layout.setContentsMargins(16, 12, 16, 12)

        title = SubtitleLabel("Board Specific Mods")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        desc = BodyLabel("Modify board-specific features for Mario Party 8 boards.")
        desc.setAlignment(Qt.AlignCenter)
        layout.addWidget(desc)

        # Koopa's Tycoon Town Features Card
        tycoon_card = CardWidget()
        tycoon_layout = QVBoxLayout()
        tycoon_layout.setContentsMargins(20, 16, 20, 16)
        tycoon_layout.setSpacing(16)
        tycoon_card.setLayout(tycoon_layout)

        # Add title to the card
        card_title = SubtitleLabel("Koopa's Tycoon Town")
        card_title.setStyleSheet("font-size: 16px; font-weight: 600; margin-bottom: 8px;")
        tycoon_layout.addWidget(card_title)

        # Hotel Max Investment Row
        hotel_row = QHBoxLayout()
        hotel_row.setSpacing(12)
        
        # Add hotel image
        hotel_image = self.create_image_label("assets/eventTags/hotel.png", 32, 32)
        hotel_row.addWidget(hotel_image)
        
        hotel_label = BodyLabel("Hotel Max Investment:")
        hotel_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 120px;")
        hotel_row.addWidget(hotel_label)
        
        self.hotel_entry = LineEdit()
        self.hotel_entry.setFixedWidth(60)
        hotel_row.addWidget(self.hotel_entry)
        
        hotel_row.addStretch()
        tycoon_layout.addLayout(hotel_row)

        layout.addWidget(tycoon_card)

        # Generate button
        generate_btn = PushButton("Generate Codes")
        generate_btn.clicked.connect(self.generate_codes)
        layout.addWidget(generate_btn)

        # Add stretch to push everything up
        layout.addStretch()

        self.setLayout(layout)

    def create_image_label(self, image_path, width=32, height=32):
        """Create a QLabel with an image from the assets folder"""
        try:
            # Get the image path from resource manager
            from utils.resource_manager import ResourceManager
            image_path = ResourceManager.get_resource_path(image_path)
            
            # Create QLabel and set image
            from PyQt5.QtWidgets import QLabel
            from PyQt5.QtGui import QPixmap
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
            from PyQt5.QtWidgets import QLabel
            fallback_label = QLabel("?")
            fallback_label.setFixedSize(width, height)
            fallback_label.setAlignment(Qt.AlignCenter)
            fallback_label.setStyleSheet("border: 1px solid gray; background: lightgray;")
            return fallback_label

    def generate_codes(self):
        """Generate codes for board specific modifications"""
        try:
            if hotelMaxInvestEvent_mp8:
                # Create mock object to match the expected interface
                class MockEntry:
                    def __init__(self, text):
                        self._text = text
                    def get(self):
                        return self._text
                    def text(self):
                        return self._text
                
                hotel_amount = MockEntry(self.hotel_entry.text())
                hotelMaxInvestEvent_mp8(hotel_amount)
            else:
                self.show_error("Mario Party 8 board specific modifications not available")
        except Exception as e:
            self.show_error(f"Error generating codes: {str(e)}")

    def show_error(self, message):
        """Show error message to user"""
        from PyQt5.QtWidgets import QMessageBox
        QMessageBox.critical(self, "Error", message)
