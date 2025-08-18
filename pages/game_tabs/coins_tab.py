#!/usr/bin/env python3
# ============================================
# Coins Tab Component for Mario Party 2
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QLabel, QLineEdit, QCheckBox, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
from qfluentwidgets import SubtitleLabel, BodyLabel, LineEdit, CheckBox, PushButton

# Import coins event functions for MP1 and MP2
try:
    from events.marioParty1_coins import coinsEvent_mp1
    from events.marioParty2_coins import coinsEvent_mp2
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
        title = QLabel("Coin Space Modifications")
        title.setStyleSheet("""
            font-size: 24px;
            font-weight: 700;
            color: #E0E0E0;
            margin: 8px 0;
            text-align: center;
        """)
        layout.addWidget(title)
        
        # Description
        desc = BodyLabel("Modify coin values for different space types:")
        desc.setStyleSheet("""
            font-size: 15px;
            color: #E0E0E0;
            margin-bottom: 8px;
            text-align: center;
        """)
        layout.addWidget(desc)
        
        # Coin Modifications Group
        group = QGroupBox("Space Modifications")
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
        
        # Blue Space Row
        blue_row = QHBoxLayout()
        blue_row.setSpacing(12)
        
        blue_label = QLabel("Blue Space:")
        blue_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px; color: #E0E0E0;")
        blue_row.addWidget(blue_label)
        
        self.blue_entry = LineEdit()
        self.blue_entry.setPlaceholderText("3")
        self.blue_entry.setText("3")
        self.blue_entry.setFixedWidth(60)
        self.blue_entry.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                font-weight: 600;
                padding: 6px 8px;
                border: 2px solid #4A90E2;
                border-radius: 6px;
                background: #1A1A1A;
                color: white;
                text-align: center;
            }
            QLineEdit:focus {
                border: 2px solid #5BA0F2;
                background: #2A2A2A;
            }
        """)
        blue_row.addWidget(self.blue_entry)
                
        self.blue_checkbox = CheckBox("Double on Last 5")
        self.blue_checkbox.setStyleSheet("""
            QCheckBox {
                font-size: 14px;
                color: #E0E0E0;
                spacing: 8px;
            }
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border: 2px solid #888;
                border-radius: 4px;
                background: #232323;
            }
            QCheckBox::indicator:checked {
                background: #4A90E2;
                border: 2px solid #4A90E2;
            }
            QCheckBox::indicator:focus {
                border: 2px solid #4A90E2;
            }
        """)
        blue_row.addWidget(self.blue_checkbox)
        
        blue_row.addStretch()
        group_layout.addLayout(blue_row)
        
        # Red Space Row
        red_row = QHBoxLayout()
        red_row.setSpacing(12)
        
        red_label = QLabel("Red Space:")
        red_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px; color: #E0E0E0;")
        red_row.addWidget(red_label)
        
        self.red_entry = LineEdit()
        self.red_entry.setPlaceholderText("3")
        self.red_entry.setText("3")
        self.red_entry.setFixedWidth(60)
        self.red_entry.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                font-weight: 600;
                padding: 6px 8px;
                border: 2px solid #E74C3C;
                border-radius: 6px;
                background: #1A1A1A;
                color: white;
                text-align: center;
            }
            QLineEdit:focus {
                border: 2px solid #F39C12;
                background: #2A2A2A;
            }
        """)
        red_row.addWidget(self.red_entry)
        
        self.red_checkbox = CheckBox("Double on Last 5")
        self.red_checkbox.setStyleSheet("""
            QCheckBox {
                font-size: 14px;
                color: #E0E0E0;
                spacing: 8px;
            }
            QCheckBox::indicator {
                width: 18px;
                height: 18px;
                border: 2px solid #888;
                border-radius: 4px;
                background: #232323;
            }
            QCheckBox::indicator:checked {
                background: #4A90E2;
                border: 2px solid #4A90E2;
            }
            QCheckBox::indicator:focus {
                border: 2px solid #4A90E2;
            }
        """)
        red_row.addWidget(self.red_checkbox)
        
        red_row.addStretch()
        group_layout.addLayout(red_row)
        
        # Star Space Row
        star_row = QHBoxLayout()
        star_row.setSpacing(12)
        
        star_label = QLabel("Star Space:")
        star_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px; color: #E0E0E0;")
        star_row.addWidget(star_label)
        
        self.star_entry = LineEdit()
        self.star_entry.setPlaceholderText("20")
        self.star_entry.setText("20")
        self.star_entry.setFixedWidth(60)
        self.star_entry.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                font-weight: 600;
                padding: 6px 8px;
                border: 2px solid #F39C12;
                border-radius: 6px;
                background: #1A1A1A;
                color: white;
                text-align: center;
            }
            QLineEdit:focus {
                border: 2px solid #F1C40F;
                background: #2A2A2A;
            }
        """)
        star_row.addWidget(self.star_entry)
                
        star_row.addStretch()
        group_layout.addLayout(star_row)
        
        # Koopa Bank Row (only for MP2+)
        if self.game_type != "basic" or self.game_id in ["marioParty2", "marioParty3", "marioParty4", "marioParty5", "marioParty6", "marioParty7", "marioParty8", "marioParty9", "marioPartyDS"]:
            koopa_row = QHBoxLayout()
            koopa_row.setSpacing(12)
            
            koopa_label = QLabel("Koopa Bank:")
            koopa_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px; color: #E0E0E0;")
            koopa_row.addWidget(koopa_label)
            
            self.koopa_entry = LineEdit()
            self.koopa_entry.setPlaceholderText("5")
            self.koopa_entry.setText("5")
            self.koopa_entry.setFixedWidth(60)
            self.koopa_entry.setStyleSheet("""
                QLineEdit {
                    font-size: 15px;
                    font-weight: 600;
                    padding: 6px 8px;
                    border: 2px solid #9B59B6;
                    border-radius: 6px;
                    background: #1A1A1A;
                    color: white;
                    text-align: center;
                }
                QLineEdit:focus {
                    border: 2px solid #8E44AD;
                    background: #2A2A2A;
                }
            """)
            koopa_row.addWidget(self.koopa_entry)
            
            koopa_row.addStretch()
            group_layout.addLayout(koopa_row)
        
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
        else:
            self.show_error(f"Coins modification not supported for {self.game_id}")
    
    def show_error(self, message):
        """Show error message to user"""
        QMessageBox.critical(self, "Error", message)
