#!/usr/bin/env python3
# ============================================
# Block Weights Tab Component
# Converted from CTk to PyQt5 for Mario Party 1
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy, QLabel, QLineEdit, QGroupBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from qfluentwidgets import SubtitleLabel, BodyLabel, PushButton, LineEdit

from functions import fetchResource
from events.marioParty1_items import itemsEvent_mp1


class BlockWeightsTab(QWidget):
    def __init__(self, game_id):
        super().__init__()
        self.game_id = game_id
        self.setup_ui()

    def setup_ui(self):
        """Set up the block weights tab UI"""
        self.setObjectName(f"{self.game_id}BlockWeightsTab")
        
        # Main layout with reduced spacing
        layout = QVBoxLayout()
        layout.setSpacing(8)  # Reduced from 12
        layout.setContentsMargins(16, 8, 16, 8)  # Reduced top/bottom margins
        
        # Title with reduced margin
        title = SubtitleLabel("Dice Block Weight Modifications")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Description with reduced margin
        desc = BodyLabel("Modify the weights for different dice block types:")
        desc.setAlignment(Qt.AlignCenter)
        layout.addWidget(desc)
        
        # Dice Block Weights Group
        group = QGroupBox("Dice Block Weights")
        
        # Store reference to group for theme updates
        self.block_weights_group = group
        
        # Apply initial styling
        self.update_block_weights_group_theme()
        
        # Group layout with reduced spacing
        group_layout = QVBoxLayout()
        group_layout.setSpacing(6)  # Reduced from 8
        group_layout.setContentsMargins(16, 8, 16, 8)  # Reduced top/bottom margins
        group.setLayout(group_layout)
        
        # Grid layout for the dice block rows
        grid_layout = QVBoxLayout()
        grid_layout.setSpacing(8)  # Reduced from 12
        grid_layout.setContentsMargins(0, 0, 0, 0)
        
        # Plus Block Row
        plus_row = QHBoxLayout()
        plus_row.setSpacing(8)  # Reduced from 12
        
        # Plus icon
        plus_icon = QLabel()
        plus_icon.setPixmap(QIcon(str(fetchResource("assets/items/plusBlock.png"))).pixmap(20, 20))  # Reduced from 24x24
        plus_icon.setStyleSheet("padding: 2px;")  # Reduced from 4px
        plus_row.addWidget(plus_icon)
        
        # Plus label
        plus_label = BodyLabel("Plus Block:")
        plus_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")  # Removed color
        plus_row.addWidget(plus_label)
        
        # Plus input
        self.plus_entry = LineEdit()
        self.plus_entry.setPlaceholderText("1")
        self.plus_entry.setText("1")
        self.plus_entry.setFixedWidth(50)  # Reduced from 60
        plus_row.addWidget(self.plus_entry)
        
        plus_row.addStretch()
        grid_layout.addLayout(plus_row)
        
        # Minus Block Row
        minus_row = QHBoxLayout()
        minus_row.setSpacing(8)  # Reduced from 12
        
        # Minus icon
        minus_icon = QLabel()
        minus_icon.setPixmap(QIcon(str(fetchResource("assets/items/minusBlock.png"))).pixmap(20, 20))  # Reduced from 24x24
        minus_icon.setStyleSheet("padding: 2px;")  # Reduced from 4px
        minus_row.addWidget(minus_icon)
        
        # Minus label
        minus_label = BodyLabel("Minus Block:")
        minus_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")  # Removed color
        minus_row.addWidget(minus_label)
        
        # Minus input
        self.minus_entry = LineEdit()
        self.minus_entry.setPlaceholderText("1")
        self.minus_entry.setText("1")
        self.minus_entry.setFixedWidth(50)  # Reduced from 60
        minus_row.addWidget(self.minus_entry)
        
        minus_row.addStretch()
        grid_layout.addLayout(minus_row)
        
        # Speed Block Row
        speed_row = QHBoxLayout()
        speed_row.setSpacing(8)  # Reduced from 12
        
        # Speed icon
        speed_icon = QLabel()
        speed_icon.setPixmap(QIcon(str(fetchResource("assets/items/speedBlock.png"))).pixmap(20, 20))  # Reduced from 24x24
        speed_icon.setStyleSheet("padding: 2px;")  # Reduced from 4px
        speed_row.addWidget(speed_icon)
        
        # Speed label
        speed_label = BodyLabel("Speed Block:")
        speed_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")  # Removed color
        speed_row.addWidget(speed_label)
        
        # Speed input
        self.speed_entry = LineEdit()
        self.speed_entry.setPlaceholderText("1")
        self.speed_entry.setText("1")
        self.speed_entry.setFixedWidth(50)  # Reduced from 60
        speed_row.addWidget(self.speed_entry)
        
        speed_row.addStretch()
        grid_layout.addLayout(speed_row)
        
        # Slow Block Row
        slow_row = QHBoxLayout()
        slow_row.setSpacing(8)  # Reduced from 12
        
        # Slow icon
        slow_icon = QLabel()
        slow_icon.setPixmap(QIcon(str(fetchResource("assets/items/slowBlock.png"))).pixmap(20, 20))  # Reduced from 24x24
        slow_icon.setStyleSheet("padding: 2px;")  # Reduced from 4px
        slow_row.addWidget(slow_icon)
        
        # Slow label
        slow_label = BodyLabel("Slow Block:")
        slow_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")  # Removed color
        slow_row.addWidget(slow_label)
        
        # Slow input
        self.slow_entry = LineEdit()
        self.slow_entry.setPlaceholderText("1")
        self.slow_entry.setText("1")
        self.slow_entry.setFixedWidth(50)  # Reduced from 60
        slow_row.addWidget(self.slow_entry)
        
        slow_row.addStretch()
        grid_layout.addLayout(slow_row)
        
        # Warp Block Row
        warp_row = QHBoxLayout()
        warp_row.setSpacing(8)  # Reduced from 12
        
        # Warp icon
        warp_icon = QLabel()
        warp_icon.setPixmap(QIcon(str(fetchResource("assets/items/warpBlock.png"))).pixmap(20, 20))  # Reduced from 24x24
        warp_icon.setStyleSheet("padding: 2px;")  # Reduced from 4px
        warp_row.addWidget(warp_icon)
        
        # Warp label
        warp_label = BodyLabel("Warp Block:")
        warp_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")  # Removed color
        warp_row.addWidget(warp_label)
        
        # Warp input
        self.warp_entry = LineEdit()
        self.warp_entry.setPlaceholderText("1")
        self.warp_entry.setText("1")
        self.warp_entry.setFixedWidth(50)  # Reduced from 60
        warp_row.addWidget(self.warp_entry)
        
        warp_row.addStretch()
        grid_layout.addLayout(warp_row)
        
        # Add grid layout to group
        group_layout.addLayout(grid_layout)
        
        # Add group to main layout
        layout.addWidget(group)
        
        # Generate button
        generate_btn = PushButton("Generate Codes")
        generate_btn.clicked.connect(self.generate_codes)
        layout.addWidget(generate_btn)
        
        # Add stretch to push everything up
        layout.addStretch()
        
        self.setLayout(layout)
    
    def generate_codes(self):
        """Generate codes for the current game"""
        try:
            if 'itemsEvent_mp1' in globals():
                # Create mock objects to match the expected interface
                class MockEntry:
                    def __init__(self, text):
                        self._text = text
                    def get(self):
                        return self._text
                    def text(self):
                        return self._text
                
                # Create mock objects with current values
                plus_amount = MockEntry(self.plus_entry.text())
                minus_amount = MockEntry(self.minus_entry.text())
                speed_amount = MockEntry(self.speed_entry.text())
                slow_amount = MockEntry(self.slow_entry.text())
                warp_amount = MockEntry(self.warp_entry.text())
                
                itemsEvent_mp1(plus_amount, minus_amount, speed_amount, slow_amount, warp_amount)
            else:
                self.show_error("Block weights modification not available")
        except Exception as e:
            self.show_error(f"Error generating codes: {str(e)}")
    
    def show_error(self, message):
        """Show error message to user"""
        from qfluentwidgets import InfoBar, InfoBarPosition
        InfoBar.error(
            title="Error",
            content=message,
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=3000,
            parent=self
        )
    
    def update_block_weights_group_theme(self):
        """Update the block weights group styling based on current theme"""
        from qfluentwidgets import isDarkTheme
        if isDarkTheme():
            self.block_weights_group.setStyleSheet("""
                QGroupBox {
                    font-size: 16px;
                    font-weight: 600;
                    color: palette(text);
                    border: 2px solid palette(mid);
                    border-radius: 8px;
                    margin-top: 8px;
                    padding-top: 8px;
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
            self.block_weights_group.setStyleSheet("""
                QGroupBox {
                    font-size: 16px;
                    font-weight: 600;
                    color: palette(text);
                    border: 2px solid palette(mid);
                    border-radius: 8px;
                    margin-top: 8px;
                    padding-top: 8px;
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
        self.update_block_weights_group_theme()
