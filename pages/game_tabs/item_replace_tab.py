#!/usr/bin/env python3
# ============================================
# Item Replacement Tab Component for Mario Party Toolkit
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QLabel, QComboBox, QPushButton, QMessageBox, QApplication
from PyQt5.QtCore import Qt
from qfluentwidgets import SubtitleLabel, BodyLabel, ComboBox, PushButton, InfoBar, InfoBarPosition

# Import item replacement event functions for supported games
try:
    from events.marioParty2_itemReplace import itemReplace_mp2
    from events.marioParty3_itemReplace import itemReplace_mp3
except ImportError:
    # Handle missing imports gracefully
    pass


class ItemReplaceTab(QWidget):
    def __init__(self, game_id):
        super().__init__()
        self.game_id = game_id
        self.setup_ui()

    def setup_ui(self):
        """Set up the item replacement tab UI"""
        self.setObjectName(f"{self.game_id}ItemReplaceTab")
        
        # Main layout
        layout = QVBoxLayout()
        layout.setSpacing(8)
        layout.setContentsMargins(16, 12, 16, 12)
        
        # Title
        title = QLabel("Item Replacement")
        title.setStyleSheet("""
            font-size: 24px;
            font-weight: 700;
            color: #E0E0E0;
            margin: 8px 0;
            text-align: center;
        """)
        layout.addWidget(title)
        
        # Check if this game supports item replacement
        if self.game_id not in ["marioParty2", "marioParty3"]:
            # Show unsupported message
            unsupported_label = QLabel("Item replacement is not supported for this game.")
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
        
        # Description
        desc = BodyLabel("Replace specific item spaces with different items:")
        desc.setStyleSheet("""
            font-size: 15px;
            color: #E0E0E0;
            margin-bottom: 8px;
            text-align: center;
        """)
        layout.addWidget(desc)
        
        # Item Replacement Group
        group = QGroupBox("Item Replacement")
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
        group_layout.setSpacing(16)
        group_layout.setContentsMargins(20, 16, 20, 16)
        group.setLayout(group_layout)
        
        # Item selection row
        selection_row = QHBoxLayout()
        selection_row.setSpacing(16)
        
        # "Replace" label
        replace_label = QLabel("Replace")
        replace_label.setStyleSheet("""
            font-size: 18px;
            font-weight: 600;
            color: #E0E0E0;
            min-width: 80px;
        """)
        selection_row.addWidget(replace_label)
        
        # First item selection
        self.item1_combo = ComboBox()
        self.item1_combo.setFixedWidth(200)
        self.item1_combo.setStyleSheet("""
            QComboBox {
                font-size: 16px;
                font-weight: 600;
                padding: 8px 12px;
                border: 2px solid #555555;
                border-radius: 6px;
                background: #2A2A2A;
                color: white;
                min-height: 36px;
            }
            QComboBox:hover {
                border: 2px solid #4A90E2;
                background: #333333;
            }
            QComboBox:focus {
                border: 2px solid #4A90E2;
                background: #333333;
            }
            QComboBox::drop-down {
                border: none;
                width: 20px;
            }
            QComboBox::down-arrow {
                image: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIiIGhlaWdodD0iOCIgdmlld0JveD0iMCAwIDEyIDgiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxwYXRoIGQ9Ik0xIDEuNUw2IDYuNUwxMSAxLjUiIHN0cm9rZT0iI0UwRTBFMCIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiLz4KPC9zdmc+);
            }
            QComboBox QAbstractItemView {
                background: #2A2A2A;
                border: 2px solid #4A90E2;
                border-radius: 6px;
                selection-background-color: #4A90E2;
                outline: none;
            }
        """)
        selection_row.addWidget(self.item1_combo)
        
        # "with" label
        with_label = QLabel("with")
        with_label.setStyleSheet("""
            font-size: 18px;
            font-weight: 600;
            color: #E0E0E0;
            min-width: 60px;
        """)
        selection_row.addWidget(with_label)
        
        # Second item selection
        self.item2_combo = ComboBox()
        self.item2_combo.setFixedWidth(200)
        self.item2_combo.setStyleSheet("""
            QComboBox {
                font-size: 16px;
                font-weight: 600;
                padding: 8px 12px;
                border: 2px solid #555555;
                border-radius: 6px;
                background: #2A2A2A;
                color: white;
                min-height: 36px;
            }
            QComboBox:hover {
                border: 2px solid #4A90E2;
                background: #333333;
            }
            QComboBox:focus {
                border: 2px solid #4A90E2;
                background: #333333;
            }
            QComboBox::drop-down {
                border: none;
                width: 20px;
            }
            QComboBox::down-arrow {
                image: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIiIGhlaWdodD0iOCIgdmlld0JveD0iMCAwIDEyIDgiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxwYXRoIGQ9Ik0xIDEuNUw2IDYuNUwxMSAxLjUiIHN0cm9rZT0iI0UwRTBFMCIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiLz4KPC9zdmc+);
            }
            QComboBox QAbstractItemView {
                background: #2A2A2A;
                border: 2px solid #4A90E2;
                border-radius: 6px;
                selection-background-color: #4A90E2;
                outline: none;
            }
        """)
        selection_row.addWidget(self.item2_combo)
        
        selection_row.addStretch()
        group_layout.addLayout(selection_row)
        
        # Populate item lists
        self.populate_item_lists()
        
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
    
    def populate_item_lists(self):
        """Populate item lists based on the current game"""
        if self.game_id == "marioParty2":
            # Based on the hex array in marioParty2_itemReplace.py
            items_list = [
                "NONE", "Mushroom", "Skeleton Key", "Plunder Chest", "Bowser BOMB", 
                "Dueling Glove", "Warp Block", "Golden Mushroom", "Boo Bell", "Magic Lamp"
            ]
        elif self.game_id == "marioParty3":
            # Based on the hex array in marioParty3_itemReplace.py
            items_list = [
                "NONE", "Mushroom", "Skeleton Key", "Plunder Chest", "Bowser BOMB", 
                "Dueling Glove", "Warp Block", "Golden Mushroom", "Boo Bell", "Magic Lamp",
                "Bowser Phone", "Bowser Suit", "Cellular Shopper", "Lucky Lamp", "Poison Mushroom",
                "Reverse Mushroom", "Mini Mushroom", "Mega Mushroom", "Warp Pipe", "Boo Repellent"
            ]
        else:
            # This shouldn't happen since we check earlier, but just in case
            items_list = ["NONE"]
        
        # Populate both combo boxes
        self.item1_combo.addItems(items_list)
        self.item2_combo.addItems(items_list)
        
        # Set default selections
        if len(items_list) > 0:
            self.item1_combo.setCurrentText(items_list[0])
            if len(items_list) > 1:
                self.item2_combo.setCurrentText(items_list[1])
    
    def generate_codes(self):
        """Generate codes for the current game"""
        # Get selected items
        item1 = self.item1_combo.currentText()
        item2 = self.item2_combo.currentText()
        
        # Validate selection
        if item1 == item2:
            main_window = QApplication.instance().activeWindow()
            InfoBar.error(
                title="Invalid Selection",
                content="Please select different items for replacement.",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP_RIGHT,
                duration=2500,
                parent=main_window
            )
            return
        
        try:
            # Create mock objects that match the expected interface
            # The functions expect .get() method calls, so we need to create compatible objects
            class MockItemWidget:
                def __init__(self, text):
                    self._text = text
                def get(self):
                    return self._text
            
            # Create mock objects with current values
            item1_widget = MockItemWidget(item1)
            item2_widget = MockItemWidget(item2)
            
            # Get the items list for the current game
            if self.game_id == "marioParty2":
                items_list = ["NONE", "Mushroom", "Skeleton Key", "Plunder Chest", "Bowser BOMB", 
                             "Dueling Glove", "Warp Block", "Golden Mushroom", "Boo Bell", "Magic Lamp"]
            elif self.game_id == "marioParty3":
                items_list = ["NONE", "Mushroom", "Skeleton Key", "Plunder Chest", "Bowser BOMB", 
                             "Dueling Glove", "Warp Block", "Golden Mushroom", "Boo Bell", "Magic Lamp",
                             "Bowser Phone", "Bowser Suit", "Cellular Shopper", "Lucky Lamp", "Poison Mushroom",
                             "Reverse Mushroom", "Mini Mushroom", "Mega Mushroom", "Warp Pipe", "Boo Repellent"]
            else:
                self.show_error(f"Item replacement not supported for {self.game_id}")
                return
            
            # Call appropriate item replacement function based on game
            if self.game_id == "marioParty2":
                if 'itemReplace_mp2' in globals():
                    itemReplace_mp2(item1_widget, item2_widget, items_list)
                else:
                    self.show_error("Mario Party 2 item replacement not available")
            elif self.game_id == "marioParty3":
                if 'itemReplace_mp3' in globals():
                    itemReplace_mp3(item1_widget, item2_widget, items_list)
                else:
                    self.show_error("Mario Party 3 item replacement not available")
            else:
                self.show_error(f"Item replacement not supported for {self.game_id}")
                
        except Exception as e:
            self.show_error(f"Error generating codes: {str(e)}")
    
    def show_error(self, message):
        """Show error message to user"""
        QMessageBox.critical(self, "Error", message)
