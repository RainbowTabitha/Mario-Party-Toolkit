#!/usr/bin/env python3
# ============================================
# Coins Tab Component for Mario Party 2
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QGroupBox
from PyQt5.QtCore import Qt
from qfluentwidgets import SubtitleLabel, BodyLabel, LineEdit, CheckBox, PushButton

# Import coins event functions for MP1, MP2, and MP3
try:
    from events.marioParty1_coins import coinsEvent_mp1
    from events.marioParty2_coins import coinsEvent_mp2
    from events.marioParty3_coins import coinsEvent_mp3
except ImportError:
    pass


class CoinsTab(QWidget):
    def __init__(self, game_id, game_type="basic"):
        super().__init__()
        self.game_id = game_id
        self.game_type = game_type
        self.setup_ui()

    def setup_ui(self):
        """Set up the coins tab UI"""
        self.setObjectName(f"{self.game_id}CoinsTab")
        
        # Main layout
        layout = QVBoxLayout()
        layout.setSpacing(8)
        layout.setContentsMargins(16, 12, 16, 12)
        
        # Title
        title = SubtitleLabel("Coin Space Modifications")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Description
        desc = BodyLabel("Modify coin values for different space types:")
        desc.setAlignment(Qt.AlignCenter)
        layout.addWidget(desc)
        
        # Coin Modifications Group using QGroupBox with themed styling
        group = QGroupBox("Space Modifications")
        
        # Store reference to group for theme updates
        self.coins_group = group
        
        # Apply initial styling
        self.update_coins_group_theme()
        
        group_layout = QVBoxLayout()
        group.setLayout(group_layout)
        
        # Blue Space Row
        blue_row = QHBoxLayout()
        blue_row.setSpacing(12)
        
        blue_label = BodyLabel("Blue Space:")
        blue_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
        blue_row.addWidget(blue_label)
        
        self.blue_entry = LineEdit()
        self.blue_entry.setPlaceholderText("3")
        self.blue_entry.setText("3")
        self.blue_entry.setFixedWidth(60)
        blue_row.addWidget(self.blue_entry)
                
        self.blue_checkbox = CheckBox("Double on Last 5")
        blue_row.addWidget(self.blue_checkbox)
        
        blue_row.addStretch()
        group_layout.addLayout(blue_row)
        
        # Red Space Row
        red_row = QHBoxLayout()
        red_row.setSpacing(12)
        
        red_label = BodyLabel("Red Space:")
        red_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
        red_row.addWidget(red_label)
        
        self.red_entry = LineEdit()
        self.red_entry.setPlaceholderText("3")
        self.red_entry.setText("3")
        self.red_entry.setFixedWidth(60)
        red_row.addWidget(self.red_entry)
        
        self.red_checkbox = CheckBox("Double on Last 5")
        red_row.addWidget(self.red_checkbox)
        
        red_row.addStretch()
        group_layout.addLayout(red_row)
        
        # Star Space Row
        star_row = QHBoxLayout()
        star_row.setSpacing(12)
        
        star_label = BodyLabel("Star Space:")
        star_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
        star_row.addWidget(star_label)
        
        self.star_entry = LineEdit()
        self.star_entry.setPlaceholderText("20")
        self.star_entry.setText("20")
        self.star_entry.setFixedWidth(60)
        star_row.addWidget(self.star_entry)
                
        star_row.addStretch()
        group_layout.addLayout(star_row)
        
        # Koopa Bank Row (only for MP2+)
        if self.game_type != "basic" or self.game_id in ["marioParty2", "marioParty3", "marioParty4", "marioParty5", "marioParty6", "marioParty7", "marioParty8", "marioParty9", "marioPartyDS"]:
            koopa_row = QHBoxLayout()
            koopa_row.setSpacing(12)
            
            koopa_label = BodyLabel("Koopa Bank:")
            koopa_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            koopa_row.addWidget(koopa_label)
            
            self.koopa_entry = LineEdit()
            self.koopa_entry.setPlaceholderText("5")
            self.koopa_entry.setText("5")
            self.koopa_entry.setFixedWidth(60)
            koopa_row.addWidget(self.koopa_entry)
            
            koopa_row.addStretch()
            group_layout.addLayout(koopa_row)
        
        # Mario Party 3 specific fields
        if self.game_id == "marioParty3":
 
            boo_coins_row = QHBoxLayout()
            boo_coins_row.setSpacing(12)
            
            boo_coins_label = BodyLabel("Boo Coins:")
            boo_coins_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            boo_coins_row.addWidget(boo_coins_label)
            
            self.boo_coins_entry = LineEdit()
            self.boo_coins_entry.setPlaceholderText("10")
            self.boo_coins_entry.setText("10")
            self.boo_coins_entry.setFixedWidth(60)
            boo_coins_row.addWidget(self.boo_coins_entry)
            
            boo_coins_row.addStretch()
            group_layout.addLayout(boo_coins_row)
            
            # Boo Stars Row
            boo_stars_row = QHBoxLayout()
            boo_stars_row.setSpacing(12)
            
            boo_stars_label = BodyLabel("Boo Stars:")
            boo_stars_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            boo_stars_row.addWidget(boo_stars_label)
            
            self.boo_stars_entry = LineEdit()
            self.boo_stars_entry.setPlaceholderText("15")
            self.boo_stars_entry.setText("15")
            self.boo_stars_entry.setFixedWidth(60)
            boo_stars_row.addWidget(self.boo_stars_entry)
            
            boo_stars_row.addStretch()
            group_layout.addLayout(boo_stars_row)
        
        layout.addWidget(group)
        
        # Generate button with reduced margins
        generate_btn = PushButton("Generate Codes")
        generate_btn.clicked.connect(self.generate_codes)
        layout.addWidget(generate_btn)
        
        # Add stretch to push everything up
        layout.addStretch()
        
        self.setLayout(layout)
    
    def generate_codes(self):
        """Generate codes for the current game"""
        if self.game_id == "marioParty1":
            try:
                if 'coinsEvent_mp1' in globals():
                    # Create mock objects to match the expected interface
                    class MockEntry:
                        def __init__(self, text):
                            self._text = text
                        def get(self):
                            return self._text
                        def text(self):
                            return self._text
                    
                    class MockCheckBox:
                        def __init__(self, checked):
                            self._checked = checked
                        def get(self):
                            return self._checked
                        def isChecked(self):
                            return self._checked
                    
                    # Create mock objects with current values
                    blue_amount = MockEntry(self.blue_entry.text())
                    blue_tick = MockCheckBox(self.blue_checkbox.isChecked())
                    red_amount = MockEntry(self.red_entry.text())
                    red_tick = MockCheckBox(self.red_checkbox.isChecked())
                    star_amount = MockEntry(self.star_entry.text())
                    
                    coinsEvent_mp1(blue_amount, blue_tick, red_amount, red_tick, star_amount)
                else:
                    self.show_error("Mario Party 1 coins modification not available")
            except Exception as e:
                self.show_error(f"Error generating codes: {str(e)}")
        elif self.game_id == "marioParty2":
            try:
                if 'coinsEvent_mp2' in globals():
                    # Create mock objects to match the expected interface
                    class MockEntry:
                        def __init__(self, text):
                            self._text = text
                        def get(self):
                            return self._text
                        def text(self):
                            return self._text
                    
                    class MockCheckBox:
                        def __init__(self, checked):
                            self._checked = checked
                        def get(self):
                            return self._checked
                        def isChecked(self):
                            return self._checked
                    
                    # Create mock objects with current values
                    blue_amount = MockEntry(self.blue_entry.text())
                    blue_tick = MockCheckBox(self.blue_checkbox.isChecked())
                    red_amount = MockEntry(self.red_entry.text())
                    red_tick = MockCheckBox(self.red_checkbox.isChecked())
                    star_amount = MockEntry(self.star_entry.text())
                    
                    # Only include koopa_amount if koopa_entry exists
                    koopa_amount = MockEntry(self.koopa_entry.text()) if hasattr(self, 'koopa_entry') else MockEntry("5")
                    
                    coinsEvent_mp2(blue_amount, blue_tick, red_amount, red_tick, star_amount, koopa_amount)
                else:
                    self.show_error("Mario Party 2 coins modification not available")
            except Exception as e:
                self.show_error(f"Error generating codes: {str(e)}")
        elif self.game_id == "marioParty3":
            try:
                if 'coinsEvent_mp3' in globals():
                    # Create mock objects to match the expected interface
                    class MockEntry:
                        def __init__(self, text):
                            self._text = text
                        def get(self):
                            return self._text
                        def text(self):
                            return self._text
                    
                    class MockCheckBox:
                        def __init__(self, checked):
                            self._checked = checked
                        def get(self):
                            return self._checked
                        def isChecked(self):
                            return self._checked
                    
                    # Create mock objects with current values
                    blue_amount = MockEntry(self.blue_entry.text())
                    blue_tick = MockCheckBox(self.blue_checkbox.isChecked())
                    red_amount = MockEntry(self.red_entry.text())
                    red_tick = MockCheckBox(self.red_checkbox.isChecked())
                    star_amount = MockEntry(self.star_entry.text())
                    koopa_amount = MockEntry(self.koopa_entry.text()) if hasattr(self, 'koopa_entry') else MockEntry("5")
                    boo_coins = MockEntry(self.boo_coins_entry.text()) if hasattr(self, 'boo_coins_entry') else MockEntry("10")
                    boo_stars = MockEntry(self.boo_stars_entry.text()) if hasattr(self, 'boo_stars_entry') else MockEntry("15")
                    
                    coinsEvent_mp3(blue_amount, blue_tick, red_amount, red_tick, star_amount, boo_coins, boo_stars, koopa_amount)
                else:
                    self.show_error("Mario Party 3 coins modification not available")
            except Exception as e:
                self.show_error(f"Error generating codes: {str(e)}")
        else:
            self.show_error(f"Coins modification not supported for {self.game_id}")
    
    def show_error(self, message):
        """Show error message to user"""
        QMessageBox.critical(self, "Error", message)
    
    def update_coins_group_theme(self):
        """Update the coins group styling based on current theme"""
        from qfluentwidgets import isDarkTheme
        if isDarkTheme():
            self.coins_group.setStyleSheet("""
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
            self.coins_group.setStyleSheet("""
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
        self.update_coins_group_theme()
