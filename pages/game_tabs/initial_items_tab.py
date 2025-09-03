#!/usr/bin/env python3
# ============================================
# Initial Items Tab Component for Mario Party 4
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from qfluentwidgets import SubtitleLabel, BodyLabel, ComboBox, PushButton

# Import resource manager for images
from utils.resource_manager import ResourceManager

# Import initial items event function for MP4
try:
    from events.marioParty4_initialItems import initialItemsEvent_mp4
except ImportError:
    pass


class InitialItemsTab(QWidget):
    def __init__(self, game_id):
        super().__init__()
        self.game_id = game_id
        self.setup_ui()

    def setup_ui(self):
        """Set up the initial items tab UI"""
        self.setObjectName(f"{self.game_id}InitialItemsTab")

        # Main layout
        layout = QVBoxLayout()
        layout.setSpacing(8)
        layout.setContentsMargins(16, 12, 16, 12)

        # Title
        title = SubtitleLabel("Starting Item Modifications")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Description
        desc = BodyLabel("Choose which items players start with at the beginning of the game:")
        desc.setAlignment(Qt.AlignCenter)
        layout.addWidget(desc)

        # Item list for MP4
        self.mp4_items = [
            "None",
            "Mini Mushroom",
            "Mega Mushroom",
            "Super Mini Mushroom",
            "Super Mega Mushroom",
            "Mini Mega Hammer",
            "Warp Pipe",
            "Swap Card",
            "Sparky Sticker",
            "Gaddlight",
            "Chomp Call",
            "Bowser Suit",
            "Crystal Ball",
            "Magic Lamp",
            "Item Bag"
        ]

        # Create item selection section
        items_group_layout = QVBoxLayout()
        items_group_layout.setSpacing(16)

        # Item slots
        for i in range(1, 4):
            slot_layout = QHBoxLayout()
            slot_layout.setSpacing(12)

            # Slot label
            slot_label = BodyLabel(f"Item Slot {i}:")
            slot_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            slot_layout.addWidget(slot_label)

            # Item combo box
            combo = ComboBox()
            combo.addItems(self.mp4_items)
            combo.setCurrentText("None")
            combo.setFixedWidth(200)
            slot_layout.addWidget(combo)

            # Store reference
            setattr(self, f"item_slot_{i}_combo", combo)

            slot_layout.addStretch()
            items_group_layout.addLayout(slot_layout)

        layout.addLayout(items_group_layout)

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
        """Generate codes for initial items"""
        try:
            if 'initialItemsEvent_mp4' in globals():
                # Get selected items
                item1 = self.item_slot_1_combo.currentText()
                item2 = self.item_slot_2_combo.currentText()
                item3 = self.item_slot_3_combo.currentText()

                # Create mock entry objects to match expected interface
                class MockEntry:
                    def __init__(self, text):
                        self._text = text
                    def get(self):
                        return self._text

                mock_item1 = MockEntry(item1)
                mock_item2 = MockEntry(item2)
                mock_item3 = MockEntry(item3)
                mock_items_list = self.mp4_items

                initialItemsEvent_mp4(mock_item1, mock_item2, mock_item3, mock_items_list)
            else:
                self.show_error("Mario Party 4 initial items modification not available")

        except Exception as e:
            self.show_error(f"Error generating codes: {str(e)}")

    def show_error(self, message):
        """Show error message to user"""
        QMessageBox.critical(self, "Error", message)

    def themeChanged(self):
        """Called when theme changes - update all styling"""
        pass
