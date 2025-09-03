#!/usr/bin/env python3
# ============================================
# Battle Minigame Tab Component for Mario Party 4
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from qfluentwidgets import SubtitleLabel, BodyLabel, LineEdit, PushButton

# Import resource manager for images
from utils.resource_manager import ResourceManager

# Import battle coins event function for MP4
try:
    from events.marioParty4_battle import battleCoins_mp4
except ImportError:
    pass


class BattleMinigameTab(QWidget):
    def __init__(self, game_id):
        super().__init__()
        self.game_id = game_id
        self.setup_ui()

    def setup_ui(self):
        """Set up the battle minigame tab UI"""
        self.setObjectName(f"{self.game_id}BattleMinigameTab")

        # Main layout
        layout = QVBoxLayout()
        layout.setSpacing(8)
        layout.setContentsMargins(16, 12, 16, 12)

        # Title
        title = SubtitleLabel("Battle Minigame Bounties")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Description
        desc = BodyLabel("Modify coin bounties awarded for winning battle minigames:")
        desc.setAlignment(Qt.AlignCenter)
        layout.addWidget(desc)

        # Battle minigame bounties group
        bounties_layout = QVBoxLayout()
        bounties_layout.setSpacing(16)

        # Create bounty input fields
        bounty_levels = [
            ("1st Place:", "5"),
            ("2nd Place:", "10"),
            ("3rd Place:", "20"),
            ("4th Place:", "30"),
            ("5th Place:", "50")
        ]

        for i, (label_text, default_value) in enumerate(bounty_levels, 1):
            bounty_layout = QHBoxLayout()
            bounty_layout.setSpacing(12)

            # Trophy icon (reuse battle icon)
            battle_icon = self.create_image_label("assets/eventTags/battle.png", 32, 32)
            bounty_layout.addWidget(battle_icon)

            # Place label
            place_label = BodyLabel(label_text)
            place_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            bounty_layout.addWidget(place_label)

            # Coin input
            entry = LineEdit()
            # Leave fields blank - users can fill in custom values
            entry.setFixedWidth(80)
            bounty_layout.addWidget(entry)

            # Coins label
            coins_label = BodyLabel("Coins")
            coins_label.setStyleSheet("font-size: 14px;")
            bounty_layout.addWidget(coins_label)

            # Store reference
            setattr(self, f"bounty_{i}_entry", entry)

            bounty_layout.addStretch()
            bounties_layout.addLayout(bounty_layout)

        layout.addLayout(bounties_layout)

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
        """Generate codes for battle minigame bounties"""
        try:
            if 'battleCoins_mp4' in globals():
                # Get bounty values
                bounties = []
                for i in range(1, 6):
                    entry = getattr(self, f"bounty_{i}_entry")
                    bounties.append(entry.text())

                # Create mock entry objects to match expected interface
                class MockEntry:
                    def __init__(self, text):
                        self._text = text
                    def get(self):
                        return self._text

                mock_bounties = [MockEntry(bounty) for bounty in bounties]

                battleCoins_mp4(*mock_bounties)
            else:
                self.show_error("Mario Party 4 battle minigame modification not available")

        except Exception as e:
            self.show_error(f"Error generating codes: {str(e)}")

    def show_error(self, message):
        """Show error message to user"""
        QMessageBox.critical(self, "Error", message)

    def themeChanged(self):
        """Called when theme changes - update all styling"""
        pass
