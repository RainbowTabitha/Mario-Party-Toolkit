#!/usr/bin/env python3
# ============================================
# Bonus Star Replacement Tab Component for Mario Party 2
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QMessageBox, QGroupBox
from PyQt5.QtCore import Qt
from qfluentwidgets import SubtitleLabel, BodyLabel, ComboBox, PushButton, InfoBar, InfoBarPosition

try:
    from events.marioParty2_bonusStarReplace import customBonusStarEvent_mp2
except ImportError:
    pass

class BonusStarTab(QWidget):
    def __init__(self, game_id):
        super().__init__()
        self.game_id = game_id
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName(f"{self.game_id}BonusStarTab")
        layout = QVBoxLayout()
        layout.setSpacing(8)
        layout.setContentsMargins(16, 12, 16, 12)

        title = SubtitleLabel("Bonus Star Replacement")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        desc = BodyLabel("Replace the three bonus stars with any other bonus star type:")
        desc.setAlignment(Qt.AlignCenter)
        layout.addWidget(desc)

        group = QGroupBox("Bonus Star Replacement")
        
        # Store reference to group for theme updates
        self.bonus_star_group = group
        
        # Apply initial styling
        self.update_bonus_star_group_theme()
        
        group_layout = QVBoxLayout()
        group_layout.setSpacing(16)
        group_layout.setContentsMargins(20, 16, 20, 16)
        group.setLayout(group_layout)

        self.stars2 = [
            "None", "Minigame Star", "Coin Star", "Happening Star", "Red Star", "Blue Star", "Chance Time Star", "Bowser Space Star", "Battle Space Star", "Item Space Star", "Bank Space Star"
        ]

        # Minigame Star
        mg_row = QHBoxLayout()
        mg_label = BodyLabel("Replace Minigame Star with:")
        mg_label.setStyleSheet("font-size: 16px; min-width: 200px;")
        mg_row.addWidget(mg_label)
        self.star1_combo = ComboBox()
        self.star1_combo.addItems(self.stars2)
        self.star1_combo.setCurrentText("Minigame Star")
        self.star1_combo.setFixedWidth(220)
        mg_row.addWidget(self.star1_combo)
        mg_row.addStretch()
        group_layout.addLayout(mg_row)

        # Coin Star
        coin_row = QHBoxLayout()
        coin_label = BodyLabel("Replace Coin Star with:")
        coin_label.setStyleSheet("font-size: 16px; min-width: 200px;")
        coin_row.addWidget(coin_label)
        self.star2_combo = ComboBox()
        self.star2_combo.addItems(self.stars2)
        self.star2_combo.setCurrentText("Coin Star")
        self.star2_combo.setFixedWidth(220)
        coin_row.addWidget(self.star2_combo)
        coin_row.addStretch()
        group_layout.addLayout(coin_row)

        # Happening Star
        hap_row = QHBoxLayout()
        hap_label = BodyLabel("Replace Happening Star with:")
        hap_label.setStyleSheet("font-size: 16px; min-width: 200px;")
        hap_row.addWidget(hap_label)
        self.star3_combo = ComboBox()
        self.star3_combo.addItems(self.stars2)
        self.star3_combo.setCurrentText("Happening Star")
        self.star3_combo.setFixedWidth(220)
        hap_row.addWidget(self.star3_combo)
        hap_row.addStretch()
        group_layout.addLayout(hap_row)

        layout.addWidget(group)

        # Generate button
        generate_btn = PushButton("Generate Codes")
        generate_btn.clicked.connect(self.generate_codes)
        layout.addWidget(generate_btn)

        # Add stretch to push everything up
        layout.addStretch()

        self.setLayout(layout)

    def generate_codes(self):
        """Generate codes for bonus star replacement"""
        try:
            if 'customBonusStarEvent_mp2' in globals():
                # Create mock objects to match the expected interface
                class MockComboBox:
                    def __init__(self, text):
                        self._text = text
                    def get(self):
                        return self._text
                    def currentText(self):
                        return self._text

                # Create mock objects with current values
                star1 = MockComboBox(self.star1_combo.currentText())
                star2 = MockComboBox(self.star2_combo.currentText())
                star3 = MockComboBox(self.star3_combo.currentText())

                customBonusStarEvent_mp2(star1, star2, star3, self.stars2)
            else:
                self.show_error("Bonus star replacement not available")
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
    
    def update_bonus_star_group_theme(self):
        """Update the bonus star group styling based on current theme"""
        from qfluentwidgets import isDarkTheme
        if isDarkTheme():
            self.bonus_star_group.setStyleSheet("""
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
            self.bonus_star_group.setStyleSheet("""
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
        self.update_bonus_star_group_theme()
