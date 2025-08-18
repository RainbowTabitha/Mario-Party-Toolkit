#!/usr/bin/env python3
# ============================================
# Item Replacement Tab Component for Mario Party 2
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QLabel, QComboBox, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
from qfluentwidgets import SubtitleLabel, BodyLabel, ComboBox, PushButton

# Import item replacement event function for MP2
try:
    from events.marioParty2_itemReplace import itemReplace_mp2
except ImportError:
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
                padding: 12px 24px;  /* Reduced from 16px 32px */
                font-size: 15px;  /* Reduced from 16px */
                font-weight: 700;
                margin: 8px 0;  /* Reduced from 16px */
                min-height: 44px;  /* Reduced from 52px */
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
            items_list = [
                "None", "Mushroom", "Skeleton Key", "Plunder Chest", "Bowser BOMB", 
                "Dueling Glove", "Warp Block", "Golden Mushroom", "Boo Bell", 
                "Bowser Suit", "Magic Lamp"
            ]
        else:
            # Default item list for unsupported games
            items_list = ["Item 1", "Item 2", "Item 3", "Item 4"]
        
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
            QMessageBox.warning(self, "Invalid Selection", 
                              "Please select different items for replacement.")
            return
        
        try:
            # Call appropriate item replacement function based on game
            if self.game_id == "marioParty2":
                if 'itemReplace_mp2' in globals():
                    # Create mock objects to match the expected interface
                    class MockComboBox:
                        def __init__(self, text):
                            self._text = text
                        def get(self):
                            return self._text
                        def currentText(self):
                            return self._text
                    
                    # Create mock objects with current values
                    item1_combo = MockComboBox(item1)
                    item2_combo = MockComboBox(item2)
                    items_list = [self.item1_combo.itemText(i) for i in range(self.item1_combo.count())]
                    
                    itemReplace_mp2(item1_combo, item2_combo, items_list)
                else:
                    self.show_error("Mario Party 2 item replacement not available")
            else:
                self.show_error(f"Item replacement not supported for {self.game_id}")
                
        except Exception as e:
            self.show_error(f"Error generating codes: {str(e)}")
    
    def show_error(self, message):
        """Show error message to user"""
        QMessageBox.critical(self, "Error", message)
