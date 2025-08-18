#!/usr/bin/env python3
# ============================================
# Block Weights Tab Component
# Converted from CTk to PyQt5 for Mario Party 1
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QSizePolicy, QLabel, QLineEdit, QPushButton
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from qfluentwidgets import SubtitleLabel, BodyLabel

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
        title = QLabel("Dice Block Weight Modifications")
        title.setStyleSheet("""
            font-size: 24px;
            font-weight: 700;
            color: #E0E0E0;
            margin: 8px 0;  /* Reduced from 16px */
            text-align: center;
        """)
        layout.addWidget(title)
        
        # Description with reduced margin
        desc = BodyLabel("Modify the weights for different dice block types:")
        desc.setStyleSheet("""
            font-size: 15px;
            color: #E0E0E2;
            margin-bottom: 4px;  /* Reduced from 8px */
            text-align: center;
        """)
        layout.addWidget(desc)
        
        # Dice Block Weights Group
        group = QGroupBox("Dice Block Weights")
        group.setStyleSheet("""
            QGroupBox {
                font-size: 16px;
                font-weight: 600;
                color: palette(text);
                border: 2px solid #3C3C3C;
                border-radius: 8px;
                margin-top: 8px;  /* Reduced from 16px */
                padding-top: 8px;  /* Reduced from 16px */
                background: #2A2A2A;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 16px;
                padding: 0 8px 0 8px;  /* Reduced from 12px */
                background: #4A90E2;
                color: white;
                border-radius: 6px;
                font-weight: 700;
            }
        """)
        
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
        plus_icon.setPixmap(QIcon(fetchResource("assets/items/plusBlock.png")).pixmap(20, 20))  # Reduced from 24x24
        plus_icon.setStyleSheet("padding: 2px;")  # Reduced from 4px
        plus_row.addWidget(plus_icon)
        
        # Plus label
        plus_label = QLabel("Plus Block:")
        plus_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px; color: #2ECC71;")  # Reduced min-width
        plus_row.addWidget(plus_label)
        
        # Plus input
        self.plus_entry = QLineEdit()
        self.plus_entry.setPlaceholderText("1")
        self.plus_entry.setText("1")
        self.plus_entry.setFixedWidth(50)  # Reduced from 60
        self.plus_entry.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                font-weight: 600;
                padding: 6px 8px;  /* Reduced from 8px 10px */
                border: 2px solid #2ECC71;
                border-radius: 6px;
                background: #1A1A1A;
                color: white;
                text-align: center;
            }
            QLineEdit:focus {
                border: 2px solid #3EDC81;
                background: #2A2A2A;
            }
        """)
        plus_row.addWidget(self.plus_entry)
        
        # Plus description
        plus_desc = QLabel("weight (1-10)")
        plus_desc.setStyleSheet("font-size: 15px; color: #D0D0D0; margin: 0 12px; font-weight: 500;")  # Reduced margin
        plus_row.addWidget(plus_desc)
        
        plus_row.addStretch()
        grid_layout.addLayout(plus_row)
        
        # Minus Block Row
        minus_row = QHBoxLayout()
        minus_row.setSpacing(8)  # Reduced from 12
        
        # Minus icon
        minus_icon = QLabel()
        minus_icon.setPixmap(QIcon(fetchResource("assets/items/minusBlock.png")).pixmap(20, 20))  # Reduced from 24x24
        minus_icon.setStyleSheet("padding: 2px;")  # Reduced from 4px
        minus_row.addWidget(minus_icon)
        
        # Minus label
        minus_label = QLabel("Minus Block:")
        minus_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px; color: #E74C3C;")  # Reduced min-width
        minus_row.addWidget(minus_label)
        
        # Minus input
        self.minus_entry = QLineEdit()
        self.minus_entry.setPlaceholderText("1")
        self.minus_entry.setText("1")
        self.minus_entry.setFixedWidth(50)  # Reduced from 60
        self.minus_entry.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                font-weight: 600;
                padding: 6px 8px;  /* Reduced from 8px 10px */
                border: 2px solid #E74C3C;
                border-radius: 6px;
                background: #1A1A1A;
                color: white;
                text-align: center;
            }
            QLineEdit:focus {
                border: 2px solid #F75C4C;
                background: #2A2A2A;
            }
        """)
        minus_row.addWidget(self.minus_entry)
        
        # Minus description
        minus_desc = QLabel("weight (1-10)")
        minus_desc.setStyleSheet("font-size: 15px; color: #D0D0D0; margin: 0 12px; font-weight: 500;")  # Reduced margin
        minus_row.addWidget(minus_desc)
        
        minus_row.addStretch()
        grid_layout.addLayout(minus_row)
        
        # Speed Block Row
        speed_row = QHBoxLayout()
        speed_row.setSpacing(8)  # Reduced from 12
        
        # Speed icon
        speed_icon = QLabel()
        speed_icon.setPixmap(QIcon(fetchResource("assets/items/speedBlock.png")).pixmap(20, 20))  # Reduced from 24x24
        speed_icon.setStyleSheet("padding: 2px;")  # Reduced from 4px
        speed_row.addWidget(speed_icon)
        
        # Speed label
        speed_label = QLabel("Speed Block:")
        speed_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px; color: #3498DB;")  # Reduced min-width
        speed_row.addWidget(speed_label)
        
        # Speed input
        self.speed_entry = QLineEdit()
        self.speed_entry.setPlaceholderText("1")
        self.speed_entry.setText("1")
        self.speed_entry.setFixedWidth(50)  # Reduced from 60
        self.speed_entry.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                font-weight: 600;
                padding: 6px 8px;  /* Reduced from 8px 10px */
                border: 2px solid #3498DB;
                border-radius: 6px;
                background: #1A1A1A;
                color: white;
                text-align: center;
            }
            QLineEdit:focus {
                border: 2px solid #5DADE2;
                background: #2A2A2A;
            }
        """)
        speed_row.addWidget(self.speed_entry)
        
        # Speed description
        speed_desc = QLabel("weight (1-10)")
        speed_desc.setStyleSheet("font-size: 15px; color: #D0D0D0; margin: 0 12px; font-weight: 500;")  # Reduced margin
        speed_row.addWidget(speed_desc)
        
        speed_row.addStretch()
        grid_layout.addLayout(speed_row)
        
        # Slow Block Row
        slow_row = QHBoxLayout()
        slow_row.setSpacing(8)  # Reduced from 12
        
        # Slow icon
        slow_icon = QLabel()
        slow_icon.setPixmap(QIcon(fetchResource("assets/items/slowBlock.png")).pixmap(20, 20))  # Reduced from 24x24
        slow_icon.setStyleSheet("padding: 2px;")  # Reduced from 4px
        slow_row.addWidget(slow_icon)
        
        # Slow label
        slow_label = QLabel("Slow Block:")
        slow_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px; color: #F39C12;")  # Reduced min-width
        slow_row.addWidget(slow_label)
        
        # Slow input
        self.slow_entry = QLineEdit()
        self.slow_entry.setPlaceholderText("1")
        self.slow_entry.setText("1")
        self.slow_entry.setFixedWidth(50)  # Reduced from 60
        self.slow_entry.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                font-weight: 600;
                padding: 6px 8px;  /* Reduced from 8px 10px */
                border: 2px solid #F39C12;
                border-radius: 6px;
                background: #1A1A1A;
                color: white;
                text-align: center;
            }
            QLineEdit:focus {
                border: 2px solid #F4B350;
                background: #2A2A2A;
            }
        """)
        slow_row.addWidget(self.slow_entry)
        
        # Slow description
        slow_desc = QLabel("weight (1-10)")
        slow_desc.setStyleSheet("font-size: 15px; color: #D0D0D0; margin: 0 12px; font-weight: 500;")  # Reduced margin
        slow_row.addWidget(slow_desc)
        
        slow_row.addStretch()
        grid_layout.addLayout(slow_row)
        
        # Warp Block Row
        warp_row = QHBoxLayout()
        warp_row.setSpacing(8)  # Reduced from 12
        
        # Warp icon
        warp_icon = QLabel()
        warp_icon.setPixmap(QIcon(fetchResource("assets/items/warpBlock.png")).pixmap(20, 20))  # Reduced from 24x24
        warp_icon.setStyleSheet("padding: 2px;")  # Reduced from 4px
        warp_row.addWidget(warp_icon)
        
        # Warp label
        warp_label = QLabel("Warp Block:")
        warp_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px; color: #9B59B6;")  # Reduced min-width
        warp_row.addWidget(warp_label)
        
        # Warp input
        self.warp_entry = QLineEdit()
        self.warp_entry.setPlaceholderText("1")
        self.warp_entry.setText("1")
        self.warp_entry.setFixedWidth(50)  # Reduced from 60
        self.warp_entry.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                font-weight: 600;
                padding: 6px 8px;  /* Reduced from 8px 10px */
                border: 2px solid #9B59B6;
                border-radius: 6px;
                background: #1A1A1A;
                color: white;
                text-align: center;
            }
            QLineEdit:focus {
                border: 2px solid #BB8FCE;
                background: #2A2A2A;
            }
        """)
        warp_row.addWidget(self.warp_entry)
        
        # Warp description
        warp_desc = QLabel("weight (1-10)")
        warp_desc.setStyleSheet("font-size: 15px; color: #D0D0D0; margin: 0 12px; font-weight: 500;")  # Reduced margin
        warp_row.addWidget(warp_desc)
        
        warp_row.addStretch()
        grid_layout.addLayout(warp_row)
        
        # Standard Dice Block Row
        standard_row = QHBoxLayout()
        standard_row.setSpacing(8)
        
        # Standard dice icon
        standard_icon = QLabel()
        standard_icon.setPixmap(QIcon(fetchResource("assets/icons/diceBlock.png")).pixmap(20, 20))  # Reduced from 24x24
        standard_icon.setStyleSheet("padding: 2px;")  # Reduced from 4px
        standard_row.addWidget(standard_icon)
        
        # Standard dice label
        standard_label = QLabel("Standard Dice:")
        standard_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px; color: #34495E;")  # Reduced min-width
        standard_row.addWidget(standard_label)
        
        # Standard dice input
        self.standard_entry = QLineEdit()
        self.standard_entry.setPlaceholderText("1")
        self.standard_entry.setText("1")
        self.standard_entry.setFixedWidth(50)  # Reduced from 60
        self.standard_entry.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                font-weight: 600;
                padding: 6px 8px;  /* Reduced from 8px 10px */
                border: 2px solid #34495E;
                border-radius: 6px;
                background: #1A1A1A;
                color: white;
                text-align: center;
            }
            QLineEdit:focus {
                border: 2px solid #5D6D7E;
                background: #2A2A2A;
            }
        """)
        standard_row.addWidget(self.standard_entry)
        
        # Standard dice description
        standard_desc = QLabel("weight (1-10)")
        standard_desc.setStyleSheet("font-size: 15px; color: #D0D0D0; margin: 0 12px; font-weight: 500;")  # Reduced margin
        standard_row.addWidget(standard_desc)
        
        standard_row.addStretch()
        grid_layout.addLayout(standard_row)
        
        group_layout.addLayout(grid_layout)
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
            self.generate_mp1_codes()
        else:
            # Placeholder for other games
            print(f"Block weights tab for {self.game_id} - TODO: Implement")

    def generate_mp1_codes(self):
        """Generate Mario Party 1 block weight codes using the original event function"""
        try:
            # Call the original MP1 items event function
            itemsEvent_mp1(self.plus_entry, self.minus_entry, self.speed_entry, self.slow_entry, self.warp_entry, self.standard_entry)
        except Exception as e:
            print(f"Error generating MP1 block weight codes: {e}")
            # Fallback: just print the values
            print(f"Plus: {self.plus_entry.text() or '1'}")
            print(f"Minus: {self.minus_entry.text() or '1'}")
            print(f"Speed: {self.speed_entry.text() or '1'}")
            print(f"Slow: {self.slow_entry.text() or '1'}")
            print(f"Warp: {self.warp_entry.text() or '1'}")
            print(f"Standard: {self.standard_entry.text() or '1'}")
