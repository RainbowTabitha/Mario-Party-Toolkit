#!/usr/bin/env python3
# ============================================
# Space Replacement Tab Component for Mario Party 4
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QMessageBox, QGroupBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from qfluentwidgets import SubtitleLabel, BodyLabel, ComboBox, PushButton

# Import resource manager for images
from utils.resource_manager import ResourceManager

# Import space replacement event functions for MP4
try:
    from events.marioParty4_spaceReplace import spaceReplaceEvent_mp4
except ImportError:
    pass


class SpaceReplacementTab(QWidget):
    def __init__(self, game_id):
        super().__init__()
        self.game_id = game_id
        self.setup_ui()

    def setup_ui(self):
        """Set up the space replacement tab UI"""
        self.setObjectName(f"{self.game_id}SpaceReplacementTab")

        # Main layout
        layout = QVBoxLayout()
        layout.setSpacing(8)
        layout.setContentsMargins(16, 12, 16, 12)

        # Title
        title = SubtitleLabel("Space Replacement")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Description
        desc = BodyLabel("Replace one space type with another on the game board:")
        desc.setAlignment(Qt.AlignCenter)
        layout.addWidget(desc)

        # Themed card container with acrylic effect
        from qfluentwidgets import CardWidget
        card = CardWidget()
        
        # Store reference to card
        self.space_replacement_group = card
        
        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(20, 16, 20, 16)
        card_layout.setSpacing(16)
        
        # Add title to the card
        card_title = SubtitleLabel("Space Replacement")
        card_title.setStyleSheet("font-size: 16px; font-weight: 600; margin-bottom: 8px;")
        card_layout.addWidget(card_title)
        
        card.setLayout(card_layout)
        
        # Use card_layout instead of group_layout for adding content
        group_layout = card_layout

        # Space types for MP4
        self.mp4_spaces = [
            "Blue Space",
            "Red Space",
            "Happening Space",
            "Fortune Space",
            "Bowser Space",
            "Battle Space",
            "Item Space",
            "Warp Space",
            "Chance Time Space"
        ]

        # Space replacement section
        replace_layout = QVBoxLayout()
        replace_layout.setSpacing(16)

        # Replace from
        from_layout = QHBoxLayout()
        from_layout.setSpacing(12)

        from_label = BodyLabel("Replace:")
        from_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 60px;")
        from_layout.addWidget(from_label)

        self.from_combo = ComboBox()
        self.from_combo.addItems(self.mp4_spaces)
        self.from_combo.setCurrentText("Blue Space")
        self.from_combo.setFixedWidth(150)
        from_layout.addWidget(self.from_combo)

        from_layout.addStretch()
        replace_layout.addLayout(from_layout)

        # Replace with
        with_layout = QHBoxLayout()
        with_layout.setSpacing(12)

        with_label = BodyLabel("With:")
        with_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 60px;")
        with_layout.addWidget(with_label)

        self.with_combo = ComboBox()
        self.with_combo.addItems(self.mp4_spaces)
        self.with_combo.setCurrentText("Red Space")
        self.with_combo.setFixedWidth(150)
        with_layout.addWidget(self.with_combo)

        with_layout.addStretch()
        replace_layout.addLayout(with_layout)

        # Slot selection
        slot_layout = QHBoxLayout()
        slot_layout.setSpacing(12)

        slot_label = BodyLabel("Slot:")
        slot_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 60px;")
        slot_layout.addWidget(slot_label)

        self.slot_combo = ComboBox()
        self.slot_combo.addItems(["Slot A", "Slot B"])
        self.slot_combo.setCurrentText("Slot A")
        self.slot_combo.setFixedWidth(100)
        slot_layout.addWidget(self.slot_combo)

        slot_layout.addStretch()
        replace_layout.addLayout(slot_layout)

        group_layout.addLayout(replace_layout)

        # Add card to main layout
        layout.addWidget(card)

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
        """Generate codes for space replacement"""
        try:
            if 'spaceReplaceEvent_mp4' in globals():
                # Get replacement values
                from_space = self.from_combo.currentText()
                to_space = self.with_combo.currentText()
                slot = self.slot_combo.currentText()

                # Create mock entry objects to match expected interface
                class MockEntry:
                    def __init__(self, text):
                        self._text = text
                    def get(self):
                        return self._text

                mock_from = MockEntry(from_space)
                mock_to = MockEntry(to_space)
                mock_slot = MockEntry(slot)

                spaceReplaceEvent_mp4(mock_from, mock_to, mock_slot)
            else:
                self.show_error("Mario Party 4 space replacement modification not available")

        except Exception as e:
            self.show_error(f"Error generating codes: {str(e)}")

    def show_error(self, message):
        """Show error message to user"""
        QMessageBox.critical(self, "Error", message)