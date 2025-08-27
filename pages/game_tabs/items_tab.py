#!/usr/bin/env python3
# ============================================
# Items Tab Component for Mario Party Toolkit
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QApplication, QGroupBox
from PyQt5.QtCore import Qt
from qfluentwidgets import SubtitleLabel, BodyLabel, LineEdit, CheckBox, PushButton, InfoBar, InfoBarPosition

# Import items event functions for supported games
try:
    from events.marioParty2_items import itemsEvent_mp2
    from events.marioParty3_items import itemsEvent_mp3
except ImportError:
    pass


class ItemsTab(QWidget):
    def __init__(self, game_id):
        super().__init__()
        self.game_id = game_id
        self.setup_ui()

    def setup_ui(self):
        """Set up the items tab UI"""
        self.setObjectName(f"{self.game_id}ItemsTab")
        
        # Main layout
        layout = QVBoxLayout()
        layout.setSpacing(8)
        layout.setContentsMargins(16, 12, 16, 12)
        
        # Title
        title = SubtitleLabel("Item Price Modifications")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Description
        desc = BodyLabel("Modify the prices for different items:")
        desc.setAlignment(Qt.AlignCenter)
        layout.addWidget(desc)
        
        # Check if this game supports item modifications
        if self.game_id not in ["marioParty2", "marioParty3"]:
            # Show unsupported message
            unsupported_label = BodyLabel("Item price modifications are not supported for this game.")
            unsupported_label.setAlignment(Qt.AlignCenter)
            unsupported_label.setStyleSheet("font-size: 18px; margin: 32px 0; padding: 24px;")
            layout.addWidget(unsupported_label)
            layout.addStretch()
            self.setLayout(layout)
            return
        
        # Item Prices Group
        group = QGroupBox("Item Prices")
        
        # Store reference to group for theme updates
        self.items_group = group
        
        # Apply initial styling
        self.update_items_group_theme()
        
        group_layout = QVBoxLayout()
        group_layout.setSpacing(12)
        group_layout.setContentsMargins(16, 12, 16, 12)
        group.setLayout(group_layout)
        
        # Create item entries based on game
        self.create_item_entries(group_layout)
        
        layout.addWidget(group)
        
        # Generate button
        generate_btn = PushButton("Generate Codes")
        generate_btn.clicked.connect(self.generate_codes)
        layout.addWidget(generate_btn)
        
        # Add stretch to push everything up
        layout.addStretch()
        
        self.setLayout(layout)

    def create_item_entries(self, group_layout):
        """Create item entry fields based on the current game"""
        if self.game_id == "marioParty2":
            self.create_mp2_items(group_layout)
        elif self.game_id == "marioParty3":
            self.create_mp3_items(group_layout)

    def create_mp2_items(self, group_layout):
        """Create Mario Party 2 item entries"""
        # Mushroom
        mushroom_row = QHBoxLayout()
        mushroom_label = BodyLabel("Mushroom:")
        mushroom_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px;")
        mushroom_row.addWidget(mushroom_label)
        
        self.mushroom_entry = LineEdit()
        self.mushroom_entry.setPlaceholderText("10")
        self.mushroom_entry.setText("10")
        self.mushroom_entry.setFixedWidth(60)
        mushroom_row.addWidget(self.mushroom_entry)
        
        mushroom_row.addStretch()
        group_layout.addLayout(mushroom_row)
        
        # Skeleton Key
        key_row = QHBoxLayout()
        key_label = BodyLabel("Skeleton Key:")
        key_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px;")
        key_row.addWidget(key_label)
        
        self.key_entry = LineEdit()
        self.key_entry.setPlaceholderText("15")
        self.key_entry.setText("15")
        self.key_entry.setFixedWidth(60)
        key_row.addWidget(self.key_entry)
        
        key_row.addStretch()
        group_layout.addLayout(key_row)
        
        # Plunder Chest
        chest_row = QHBoxLayout()
        chest_label = BodyLabel("Plunder Chest:")
        chest_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px;")
        chest_row.addWidget(chest_label)
        
        self.chest_entry = LineEdit()
        self.chest_entry.setPlaceholderText("20")
        self.chest_entry.setText("20")
        self.chest_entry.setFixedWidth(60)
        chest_row.addWidget(self.chest_entry)
        
        chest_row.addStretch()
        group_layout.addLayout(chest_row)

    def create_mp3_items(self, group_layout):
        """Create Mario Party 3 item entries"""
        # Mushroom
        mushroom_row = QHBoxLayout()
        mushroom_label = BodyLabel("Mushroom:")
        mushroom_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px;")
        mushroom_row.addWidget(mushroom_label)
        
        self.mushroom_entry = LineEdit()
        self.mushroom_entry.setPlaceholderText("10")
        self.mushroom_entry.setText("10")
        self.mushroom_entry.setFixedWidth(60)
        mushroom_row.addWidget(self.mushroom_entry)
        
        mushroom_row.addStretch()
        group_layout.addLayout(mushroom_row)
        
        # Skeleton Key
        key_row = QHBoxLayout()
        key_label = BodyLabel("Skeleton Key:")
        key_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px;")
        key_row.addWidget(key_label)
        
        self.key_entry = LineEdit()
        self.key_entry.setPlaceholderText("15")
        self.key_entry.setText("15")
        key_row.addWidget(self.key_entry)
        
        key_row.addStretch()
        group_layout.addLayout(key_row)
        
        # Plunder Chest
        chest_row = QHBoxLayout()
        chest_label = BodyLabel("Plunder Chest:")
        chest_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px;")
        chest_row.addWidget(chest_label)
        
        self.chest_entry = LineEdit()
        self.chest_entry.setPlaceholderText("20")
        self.chest_entry.setText("20")
        self.chest_entry.setFixedWidth(60)
        chest_row.addWidget(self.chest_entry)
        
        chest_row.addStretch()
        group_layout.addLayout(chest_row)

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
            mushroom_price = MockEntry(self.mushroom_entry.text())
            key_price = MockEntry(self.key_entry.text())
            chest_price = MockEntry(self.chest_entry.text())
            
            # Call appropriate items event function based on game
            if self.game_id == "marioParty2" and 'itemsEvent_mp2' in globals():
                itemsEvent_mp2(mushroom_price, key_price, chest_price)
            elif self.game_id == "marioParty3" and 'itemsEvent_mp3' in globals():
                itemsEvent_mp3(mushroom_price, key_price, chest_price)
            else:
                self.show_error(f"Items modification not available for {self.game_id}")
        except Exception as e:
            self.show_error(f"Error generating codes: {str(e)}")

    def show_error(self, message):
        """Show error message to user"""
        InfoBar.error(
            title="Error",
            content=message,
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=3000,
            parent=self
        )
    
    def update_items_group_theme(self):
        """Update the items group styling based on current theme"""
        from qfluentwidgets import isDarkTheme
        if isDarkTheme():
            self.items_group.setStyleSheet("""
                QGroupBox {
                    font-size: 16px;
                    font-weight: 600;
                    color: palette(text);
                    border: 2px solid palette(mid);
                    border-radius: 8px;
                    margin-top: 12px;
                    padding-top: 12px;
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
            self.items_group.setStyleSheet("""
                QGroupBox {
                    font-size: 16px;
                    font-weight: 600;
                    color: palette(text);
                    border: 2px solid palette(mid);
                    border-radius: 8px;
                    margin-top: 12px;
                    padding-top: 12px;
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
        self.update_items_group_theme()
