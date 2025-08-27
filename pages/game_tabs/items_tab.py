#!/usr/bin/env python3
# ============================================
# Items Tab Component for Mario Party Toolkit
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QLabel, QLineEdit, QPushButton, QMessageBox, QApplication
from PyQt5.QtCore import Qt
from qfluentwidgets import SubtitleLabel, BodyLabel, LineEdit, PushButton, InfoBar, InfoBarPosition

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
        title = QLabel("Item Price Modifications")
        title.setStyleSheet("""
            font-size: 24px;
            font-weight: 700;
            color: #E0E0E0;
            margin: 8px 0;
            text-align: center;
        """)
        layout.addWidget(title)
        
        # Description
        desc = BodyLabel("Modify the prices for different items:")
        desc.setStyleSheet("""
            font-size: 15px;
            color: #E0E0E0;
            margin-bottom: 8px;
            text-align: center;
        """)
        layout.addWidget(desc)
        
        # Check if this game supports item modifications
        if self.game_id not in ["marioParty2", "marioParty3"]:
            # Show unsupported message
            unsupported_label = QLabel("Item price modifications are not supported for this game.")
            unsupported_label.setStyleSheet("""
                font-size: 16px;
                color: #E0E0E0;
                margin: 20px 0;
                text-align: center;
                padding: 20px;
                background: #2A2A2A;
                border-radius: 8px;
                border: 2px solid #555555;
            """)
            layout.addWidget(unsupported_label)
            layout.addStretch()
            self.setLayout(layout)
            return
        
        # Item Prices Group
        group = QGroupBox("Item Prices")
        group.setStyleSheet("""
            QGroupBox {
                font-size: 16px;
                font-weight: 600;
                color: palette(text);
                border: 2px solid #3C3C3C;
                border-radius: 8px;
                margin-top: 12px;
                padding-top: 12px;
                background: #2A2A2A;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 16px;
                padding: 0 8px 0 8px;
                background: #4A90E2;
                color: white;
                border-radius: 6px;
                font-weight: 700;
            }
        """)
        
        group_layout = QVBoxLayout()
        group_layout.setSpacing(12)
        group_layout.setContentsMargins(16, 12, 16, 12)
        group.setLayout(group_layout)
        
        # Create item entries based on game
        self.create_item_entries(group_layout)
        
        layout.addWidget(group)
        
        # Generate button with reduced margins
        generate_btn = QPushButton("Generate Codes")
        generate_btn.setStyleSheet("""
            QPushButton {
                background: #4A90E2;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 12px 24px;
                font-size: 15px;
                font-weight: 700;
                margin: 8px 0;
                min-height: 44px;
            }
            QPushButton:hover {
                background: #5BA0F2;
            }
            QPushButton:pressed {
                background: #357ABD;
            }
        """)
        generate_btn.clicked.connect(self.generate_codes)
        layout.addWidget(generate_btn)
        
        # Add stretch to push everything up
        layout.addStretch()
        
        self.setLayout(layout)
    
    def is_dark_mode(self):
        """Detect if the current theme is dark mode"""
        try:
            # Get the application instance and check if it has a dark theme
            app = QApplication.instance()
            if app:
                # Check the application's palette to determine if it's dark mode
                palette = app.palette()
                background_color = palette.color(palette.Window)
                # If background is dark, assume dark mode
                return background_color.lightness() < 128
        except:
            pass
        # Default to dark mode if we can't detect
        return True
    
    def create_item_entries(self, group_layout):
        """Create item entry fields based on the current game"""
        if self.game_id == "marioParty2":
            # MP2 items (7 items)
            items_config = [
                "Mushroom",
                "Skeleton Key",
                "Plunder Chest",
                "Dueling Glove",
                "Warp Block",
                "Golden Mushroom",
                "Magic Lamp"
            ]
        elif self.game_id == "marioParty3":
            # MP3 items (16 items)
            items_config = [
                "Mushroom",
                "Skeleton Key", 
                "Poison Mushroom",
                "Reverse Mushroom",
                "Warp Block",
                "Cellular Shopper",
                "Golden Mushroom",
                "Magic Lamp",
                "Bowser Phone",
                "Dueling Glove",
                "Lucky Lamp",
                "Bowser Suit",
                "Plunder Chest",
                "Boo Bell",
                "Boo Repellent",
                "Item Bag"
            ]
        else:
            return
        
        # Create two-column layout
        columns_layout = QHBoxLayout()
        columns_layout.setSpacing(20)
        
        # Left column
        left_column = QVBoxLayout()
        left_column.setSpacing(12)
        
        # Right column
        right_column = QVBoxLayout()
        right_column.setSpacing(12)
        
        # Split items between columns
        mid_point = len(items_config) // 2
        left_items = items_config[:mid_point]
        right_items = items_config[mid_point:]
        
        # Create entry fields for left column
        self.item_entries = {}
        for item_name in left_items:
            item_row = QHBoxLayout()
            item_row.setSpacing(12)
            
            # Set label color based on light/dark mode
            label_color = "#FFFFFF" if self.is_dark_mode() else "#000000"
            if self.game_id == "marioParty3":
                if item_name in ["Mushroom", "Skeleton Key", "Poison Mushroom", "Reverse Mushroom", "Cellular Shopper", "Warp Block"]:
                    label_color = '#ff0000'
            item_label = QLabel(f"{item_name}:")
            item_label.setStyleSheet(f"font-size: 15px; font-weight: 600; min-width: 120px; color: {label_color};")
            item_row.addWidget(item_label)
            
            item_entry = LineEdit()
            item_entry.setPlaceholderText("")
            item_entry.setText("")
            item_entry.setFixedWidth(60)
            
            # Set text box color based on light/dark mode
            text_color = "#FFFFFF" if self.is_dark_mode() else "#000000"
            
            item_entry.setStyleSheet(f"""
                QLineEdit {{
                    font-size: 15px;
                    font-weight: 600;
                    padding: 6px 8px;
                    border: 2px solid #4A90E2;
                    border-radius: 6px;
                    background: #1A1A1A;
                    color: {text_color};
                    text-align: center;
                }}
                QLineEdit:focus {{
                    border: 2px solid #5BA0F2;
                    background: #2A2A2A;
                }}
            """)
            item_row.addWidget(item_entry)
            
            # Store reference to entry
            self.item_entries[item_name.lower().replace(" ", "")] = item_entry
            
            item_row.addStretch()
            left_column.addLayout(item_row)
        
        # Create entry fields for right column
        for item_name in right_items:
            item_row = QHBoxLayout()
            item_row.setSpacing(12)
            
            # Set label color based on light/dark mode
            label_color = "#FFFFFF" if self.is_dark_mode() else "#000000"
            item_label = QLabel(f"{item_name}:")
            item_label.setStyleSheet(f"font-size: 15px; font-weight: 600; min-width: 120px; color: {label_color};")
            item_row.addWidget(item_label)
            
            item_entry = LineEdit()
            item_entry.setPlaceholderText("")
            item_entry.setText("")
            item_entry.setFixedWidth(60)
            
            # Set text box color based on light/dark mode
            text_color = "#FFFFFF" if self.is_dark_mode() else "#000000"
            
            item_entry.setStyleSheet(f"""
                QLineEdit {{
                    font-size: 15px;
                    font-weight: 600;
                    padding: 6px 8px;
                    border: 2px solid #4A90E2;
                    border-radius: 6px;
                    background: #1A1A1A;
                    color: {text_color};
                    text-align: center;
                }}
                QLineEdit:focus {{
                    border: 2px solid #5BA0F2;
                    background: #2A2A2A;
                }}
            """)
            item_row.addWidget(item_entry)
            
            # Store reference to entry
            self.item_entries[item_name.lower().replace(" ", "")] = item_entry
            
            item_row.addStretch()
            right_column.addLayout(item_row)
        
        # Add columns to the main layout
        columns_layout.addLayout(left_column)
        columns_layout.addLayout(right_column)
        
        group_layout.addLayout(columns_layout)
    
    def generate_codes(self):
        """Generate codes for the current game"""
        try:
            if self.game_id == "marioParty2":
                if 'itemsEvent_mp2' in globals():
                    # Create mock objects to match the expected interface
                    class MockEntry:
                        def __init__(self, text):
                            self._text = text
                        def get(self):
                            return self._text
                        def text(self):
                            return self._text
                    
                    # Create mock objects with current values
                    mushroom = MockEntry(self.item_entries["mushroom"].text())
                    skeleton_key = MockEntry(self.item_entries["skeletonkey"].text())
                    plunder_chest = MockEntry(self.item_entries["plunderchest"].text())
                    dueling_glove = MockEntry(self.item_entries["duelingglove"].text())
                    warp_block = MockEntry(self.item_entries["warpblock"].text())
                    golden_mushroom = MockEntry(self.item_entries["goldenmushroom"].text())
                    magic_lamp = MockEntry(self.item_entries["magiclamp"].text())
                    
                    itemsEvent_mp2(mushroom, skeleton_key, plunder_chest, dueling_glove, warp_block, golden_mushroom, magic_lamp)
                else:
                    self.show_error("Mario Party 2 items modification not available")
            elif self.game_id == "marioParty3":
                if 'itemsEvent_mp3' in globals():
                    # Create mock objects to match the expected interface
                    class MockEntry:
                        def __init__(self, text):
                            self._text = text
                        def get(self):
                            return self._text
                        def text(self):
                            return self._text
                    
                    # Create mock objects with current values for MP3
                    mushroom = MockEntry(self.item_entries["mushroom"].text())
                    skeleton_key = MockEntry(self.item_entries["skeletonkey"].text())
                    poison_mushroom = MockEntry(self.item_entries["poisonmushroom"].text())
                    reverse_mushroom = MockEntry(self.item_entries["reversemushroom"].text())
                    golden_mushroom = MockEntry(self.item_entries["goldenmushroom"].text())
                    magic_lamp = MockEntry(self.item_entries["magiclamp"].text())
                    warp_block = MockEntry(self.item_entries["warpblock"].text())
                    cellular_shopper = MockEntry(self.item_entries["cellularshopper"].text())
                    bowser_phone = MockEntry(self.item_entries["bowserphone"].text())
                    dueling_glove = MockEntry(self.item_entries["duelingglove"].text())
                    lucky_lamp = MockEntry(self.item_entries["luckylamp"].text())
                    bowser_suit = MockEntry(self.item_entries["bowsersuit"].text())
                    plunder_chest = MockEntry(self.item_entries["plunderchest"].text())
                    boo_bell = MockEntry(self.item_entries["boobell"].text())
                    boo_repellent = MockEntry(self.item_entries["boorepellent"].text())
                    item_bag = MockEntry(self.item_entries["itembag"].text())
                    
                    itemsEvent_mp3(mushroom, skeleton_key, poison_mushroom, reverse_mushroom, golden_mushroom, 
                                 magic_lamp, warp_block, cellular_shopper, bowser_phone, dueling_glove, 
                                 lucky_lamp, bowser_suit, plunder_chest, boo_bell, boo_repellent, item_bag)
                else:
                    self.show_error("Mario Party 3 items modification not available")
            else:
                self.show_error(f"Items modification not supported for {self.game_id}")
        except Exception as e:
            self.show_error(f"Error generating codes: {str(e)}")
    
    def show_error(self, message):
        """Show error message to user"""
        QMessageBox.critical(self, "Error", message)
