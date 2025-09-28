#!/usr/bin/env python3
# ============================================
# Item Replacement Tab Component for Mario Party Toolkit
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QComboBox, QMessageBox, QApplication, QGroupBox
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
        title = SubtitleLabel("Item Replacement")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Description
        desc = BodyLabel("Replace specific item spaces with custom selections:")
        desc.setAlignment(Qt.AlignCenter)
        layout.addWidget(desc)
        
        # Check if this game supports item replacement
        if self.game_id not in ["marioParty2", "marioParty3"]:
            unsupported_label = BodyLabel("Item replacement is not supported for this game.")
            unsupported_label.setAlignment(Qt.AlignCenter)
            unsupported_label.setStyleSheet("font-size: 18px; margin: 32px 0; padding: 24px;")
            layout.addWidget(unsupported_label)
            layout.addStretch()
            self.setLayout(layout)
            return
        
        # Item Replacement Card with acrylic effect
        from qfluentwidgets import CardWidget
        card = CardWidget()
        
        # Store reference to card
        self.item_replace_group = card
        
        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(20, 16, 20, 16)
        card_layout.setSpacing(16)
        
        # Add title to the card
        card_title = SubtitleLabel("Item Replacement")
        card_title.setStyleSheet("font-size: 16px; font-weight: 600; margin-bottom: 8px;")
        card_layout.addWidget(card_title)
        
        card.setLayout(card_layout)
        
        # Use card_layout instead of group_layout for adding content
        group_layout = card_layout
        
        # Item selection row
        selection_row = QHBoxLayout()
        selection_row.setSpacing(16)
        
        # "Replace" label
        replace_label = BodyLabel("Replace")
        replace_label.setStyleSheet("font-size: 18px; font-weight: 600; min-width: 80px;")
        selection_row.addWidget(replace_label)
        
        # First item selection
        self.item1_combo = ComboBox()
        self.item1_combo.addItems(["Item Space", "Battle Space", "Bowser Space", "Chance Time Space", "Bank Space"])
        self.item1_combo.setCurrentText("Item Space")
        self.item1_combo.setFixedWidth(150)
        selection_row.addWidget(self.item1_combo)
        
        # "with" label
        with_label = BodyLabel("with")
        with_label.setStyleSheet("font-size: 18px; font-weight: 600; min-width: 40px;")
        selection_row.addWidget(with_label)
        
        # Second item selection
        self.item2_combo = ComboBox()
        self.item2_combo.addItems(["Item Space", "Battle Space", "Bowser Space", "Chance Time Space", "Bank Space"])
        self.item2_combo.setCurrentText("Battle Space")
        self.item2_combo.setFixedWidth(150)
        selection_row.addWidget(self.item2_combo)
        
        selection_row.addStretch()
        group_layout.addLayout(selection_row)
        
        # Add card to main layout
        layout.addWidget(card)
        
        # Generate button
        generate_btn = PushButton("Generate Codes")
        generate_btn.clicked.connect(self.generate_codes)
        layout.addWidget(generate_btn)
        
        # Add stretch to push everything up
        layout.addStretch()
        
        self.setLayout(layout)

    def generate_codes(self):
        """Generate codes for item replacement"""
        try:
            # Create mock objects to match the expected interface
            class MockComboBox:
                def __init__(self, text):
                    self._text = text
                def get(self):
                    return self._text
                def currentText(self):
                    return self._text

            # Create mock objects with current values
            item1 = MockComboBox(self.item1_combo.currentText())
            item2 = MockComboBox(self.item2_combo.currentText())

            # Call appropriate item replacement function based on game
            if self.game_id == "marioParty2" and 'itemReplace_mp2' in globals():
                # For MP2, we need to pass the items list as the third parameter
                items_list = ["None", "Mushroom", "Skeleton Key", "Plunder Chest", "Dueling Glove", "Warp Block", "Golden Mushroom", "Magic Lamp"]
                itemReplace_mp2(item1, item2, items_list)
            elif self.game_id == "marioParty3" and 'itemReplace_mp3' in globals():
                # For MP3, we need to pass the items list as the third parameter
                items_list = ["None", "Mushroom", "Skeleton Key", "Poison Mushroom", "Reverse Mushroo", "Cellular Shopper", "Warp Block", "Plunder Chest", "Bowser Phone", "Dueling Glove", "Lucky Lamp", "Golden Mushroom", "Boo Bell", "Boo Repellant", "Bowser Suit", "Magic Lamp", "Koopa Kard", "Barter Box", "Lucky Charm", "Wacky Watch"]
                itemReplace_mp3(item1, item2, items_list)
            else:
                self.show_error(f"Item replacement not available for {self.game_id}")
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
    
    def update_item_replace_group_theme(self):
        """Update the item replace group styling based on current theme"""
        from qfluentwidgets import isDarkTheme
        if isDarkTheme():
            self.item_replace_group.setStyleSheet("""
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
            self.item_replace_group.setStyleSheet("""
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
        self.update_item_replace_group_theme()
