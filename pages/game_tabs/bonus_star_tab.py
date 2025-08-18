#!/usr/bin/env python3
# ============================================
# Bonus Star Replacement Tab Component for Mario Party 2
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QLabel, QMessageBox, QPushButton
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

        title = QLabel("Bonus Star Replacement")
        title.setStyleSheet("""
            font-size: 24px;
            font-weight: 700;
            color: #E0E0E0;
            margin: 8px 0;
            text-align: center;
        """)
        layout.addWidget(title)

        desc = BodyLabel("Replace the three bonus stars with any other bonus star type:")
        desc.setStyleSheet("""
            font-size: 15px;
            color: #E0E0E0;
            margin-bottom: 8px;
            text-align: center;
        """)
        layout.addWidget(desc)

        group = QGroupBox("Bonus Star Replacement")
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

        self.stars2 = [
            "None", "Minigame Star", "Coin Star", "Happening Star", "Red Star", "Blue Star", "Chance Time Star", "Bowser Space Star", "Battle Space Star", "Item Space Star", "Bank Space Star"
        ]

        # Minigame Star
        mg_row = QHBoxLayout()
        mg_label = QLabel("Replace Minigame Star with:")
        mg_label.setStyleSheet("font-size: 16px; color: #E0E0E0; min-width: 200px;")
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
        coin_label = QLabel("Replace Coin Star with:")
        coin_label.setStyleSheet("font-size: 16px; color: #E0E0E0; min-width: 200px;")
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
        hap_label = QLabel("Replace Happening Star with:")
        hap_label.setStyleSheet("font-size: 16px; color: #E0E0E0; min-width: 200px;")
        hap_row.addWidget(hap_label)
        self.star3_combo = ComboBox()
        self.star3_combo.addItems(self.stars2)
        self.star3_combo.setCurrentText("Happening Star")
        self.star3_combo.setFixedWidth(220)
        hap_row.addWidget(self.star3_combo)
        hap_row.addStretch()
        group_layout.addLayout(hap_row)

        layout.addWidget(group)

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
        
        layout.addStretch()
        self.setLayout(layout)

    def generate_codes(self):
        if self.game_id == "marioParty2":
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
                    star1 = MockComboBox(self.star1_combo.currentText())
                    star2 = MockComboBox(self.star2_combo.currentText())
                    star3 = MockComboBox(self.star3_combo.currentText())
                    customBonusStarEvent_mp2(star1, star2, star3, self.stars2)
                    InfoBar.success(
                        title="Operation Successful",
                        content="Generated codes copied to clipboard!",
                        orient=Qt.Horizontal,
                        isClosable=True,
                        position=InfoBarPosition.TOP_RIGHT,
                        duration=2500,
                        parent=self.window()
                    )
                else:
                    self.show_error("Mario Party 2 bonus star replacement not available")
            except Exception as e:
                self.show_error(f"Error generating codes: {str(e)}")
        else:
            self.show_error(f"Bonus star replacement not supported for {self.game_id}")

    def show_error(self, message):
        InfoBar.error(
            title="Error",
            content=message,
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP_RIGHT,
            duration=2500,
            parent=self.window()
        )
