#!/usr/bin/env python3
# ============================================
# Lottery Rewards Tab Component for Mario Party 4
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QComboBox, QMessageBox, QGroupBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from qfluentwidgets import SubtitleLabel, BodyLabel, LineEdit, ComboBox, PushButton

# Import resource manager for images
from utils.resource_manager import ResourceManager

# Import lottery event function for MP4
try:
    from events.marioParty4_lotteryPrize import itemsLotteryEvent_mp4
except ImportError:
    pass


class LotteryRewardsTab(QWidget):
    def __init__(self, game_id):
        super().__init__()
        self.game_id = game_id
        self.setup_ui()

    def setup_ui(self):
        """Set up the lottery rewards tab UI"""
        self.setObjectName(f"{self.game_id}LotteryRewardsTab")

        # Main layout
        layout = QVBoxLayout()
        layout.setSpacing(8)
        layout.setContentsMargins(16, 12, 16, 12)

        # Title
        title = SubtitleLabel("Lottery Prize Modifications")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Description
        desc = BodyLabel("Modify the prizes awarded by the Lottery space:")
        desc.setAlignment(Qt.AlignCenter)
        layout.addWidget(desc)

        # Themed group container
        group = QGroupBox("Lottery Rewards")
        self.lottery_rewards_group = group
        self.update_lottery_rewards_group_theme()
        group_layout = QVBoxLayout()
        group_layout.setSpacing(16)
        group_layout.setContentsMargins(20, 16, 20, 16)
        group.setLayout(group_layout)

        # Lottery prizes group
        prizes_layout = QVBoxLayout()
        prizes_layout.setSpacing(16)

        # 1st Place Prize
        first_layout = QHBoxLayout()
        first_layout.setSpacing(12)

        # Lottery icon
        lottery_icon = self.create_image_label("assets/eventTags/lottery4.png", 32, 32)
        first_layout.addWidget(lottery_icon)

        first_label = BodyLabel("1st Place:")
        first_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
        first_layout.addWidget(first_label)

        self.first_prize_entry = LineEdit()
        # Leave fields blank - users can fill in custom values
        self.first_prize_entry.setFixedWidth(80)
        first_layout.addWidget(self.first_prize_entry)

        first_coins_label = BodyLabel("Coins")
        first_coins_label.setStyleSheet("font-size: 14px;")
        first_layout.addWidget(first_coins_label)

        first_layout.addStretch()
        prizes_layout.addLayout(first_layout)

        # 2nd Place Prize
        second_layout = QHBoxLayout()
        second_layout.setSpacing(12)

        second_icon = self.create_image_label("assets/eventTags/lottery4.png", 32, 32)
        second_layout.addWidget(second_icon)

        second_label = BodyLabel("2nd Place:")
        second_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
        second_layout.addWidget(second_label)

        self.second_prize_entry = LineEdit()
        # Leave fields blank - users can fill in custom values
        self.second_prize_entry.setFixedWidth(80)
        second_layout.addWidget(self.second_prize_entry)

        second_coins_label = BodyLabel("Coins")
        second_coins_label.setStyleSheet("font-size: 14px;")
        second_layout.addWidget(second_coins_label)

        second_layout.addStretch()
        prizes_layout.addLayout(second_layout)

        # 3rd Place Prizes (Item selection)
        third_layout = QHBoxLayout()
        third_layout.setSpacing(12)

        third_icon = self.create_image_label("assets/eventTags/lottery4.png", 32, 32)
        third_layout.addWidget(third_icon)

        third_label = BodyLabel("3rd Place:")
        third_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
        third_layout.addWidget(third_label)

        # Item list for MP4 lottery prizes
        self.mp4_lottery_items = [
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

        self.third_prize_combo1 = ComboBox()
        self.third_prize_combo1.addItems(self.mp4_lottery_items)
        self.third_prize_combo1.setCurrentText("Mini Mushroom")
        self.third_prize_combo1.setFixedWidth(150)
        third_layout.addWidget(self.third_prize_combo1)

        or_label = BodyLabel("or")
        or_label.setStyleSheet("font-size: 14px;")
        third_layout.addWidget(or_label)

        self.third_prize_combo2 = ComboBox()
        self.third_prize_combo2.addItems(self.mp4_lottery_items)
        self.third_prize_combo2.setCurrentText("Mega Mushroom")
        self.third_prize_combo2.setFixedWidth(150)
        third_layout.addWidget(self.third_prize_combo2)

        third_layout.addStretch()
        prizes_layout.addLayout(third_layout)

        group_layout.addLayout(prizes_layout)

        # Add group to main layout
        layout.addWidget(group)

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
        """Generate codes for lottery prizes"""
        try:
            if 'itemsLotteryEvent_mp4' in globals():
                # Get prize values
                first_prize = self.first_prize_entry.text()
                second_prize = self.second_prize_entry.text()
                third_prize1 = self.third_prize_combo1.currentText()
                third_prize2 = self.third_prize_combo2.currentText()

                # Create mock entry objects to match expected interface
                class MockEntry:
                    def __init__(self, text):
                        self._text = text
                    def get(self):
                        return self._text

                mock_first = MockEntry(first_prize)
                mock_second = MockEntry(second_prize)
                mock_third1 = MockEntry(third_prize1)
                mock_third2 = MockEntry(third_prize2)
                mock_items_list = self.mp4_lottery_items

                itemsLotteryEvent_mp4(mock_first, mock_second, mock_third1, mock_third2, mock_items_list)
            else:
                self.show_error("Mario Party 4 lottery modification not available")

        except Exception as e:
            self.show_error(f"Error generating codes: {str(e)}")

    def show_error(self, message):
        """Show error message to user"""
        QMessageBox.critical(self, "Error", message)

    def themeChanged(self):
        """Called when theme changes - update all styling"""
        self.update_lottery_rewards_group_theme()

    def update_lottery_rewards_group_theme(self):
        """Update group styling based on current theme"""
        from qfluentwidgets import isDarkTheme
        if isDarkTheme():
            self.lottery_rewards_group.setStyleSheet("""
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
            self.lottery_rewards_group.setStyleSheet("""
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
