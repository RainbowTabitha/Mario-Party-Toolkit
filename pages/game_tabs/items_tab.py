#!/usr/bin/env python3
# ============================================
# Items Tab Component for Mario Party 2
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
from qfluentwidgets import SubtitleLabel, BodyLabel, LineEdit, PushButton

# Import items event function for MP2
try:
    from events.marioParty2_items import itemsEvent_mp2
except ImportError:
    pass


class ItemsTab(QWidget):
    def __init__(self, game_id):
        super().__init__()
        self.game_id = game_id
        self.setup_ui()

    def setup_ui(self):
        """Set up the items tab UI"""
        self.setObjectName(f"{self.game_id}ItemsTab")
        
        # Main layout
        layout = QVBoxLayout()
        layout.setSpacing(8)
        layout.setContentsMargins(16, 12, 16, 12)
        
        # Title
        title = QLabel("Item Price Modifications")
        title.setStyleSheet("""
            font-size: 24px;
            font-weight: 700;
            color: #E0E0E0;
            margin: 8px 0;
            text-align: center;
        """)
        layout.addWidget(title)
        
        # Description
        desc = BodyLabel("Modify the prices for different items:")
        desc.setStyleSheet("""
            font-size: 15px;
            color: #E0E0E0;
            margin-bottom: 8px;
            text-align: center;
        """)
        layout.addWidget(desc)
        
        # Item Prices Group
        group = QGroupBox("Item Prices")
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
        
        # Mushroom Row
        mushroom_row = QHBoxLayout()
        mushroom_row.setSpacing(12)
        
        mushroom_label = QLabel("Mushroom:")
        mushroom_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px; color: #E0E0E0;")
        mushroom_row.addWidget(mushroom_label)
        
        self.mushroom_entry = LineEdit()
        self.mushroom_entry.setPlaceholderText("10")
        self.mushroom_entry.setText("10")
        self.mushroom_entry.setFixedWidth(60)
        self.mushroom_entry.setStyleSheet("""
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
        mushroom_row.addWidget(self.mushroom_entry)

        mushroom_row.addStretch()
        group_layout.addLayout(mushroom_row)
        
        # Skeleton Key Row
        skeleton_row = QHBoxLayout()
        skeleton_row.setSpacing(12)
        
        skeleton_label = QLabel("Skeleton Key:")
        skeleton_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px; color: #E0E0E0;")
        skeleton_row.addWidget(skeleton_label)
        
        self.skeleton_entry = LineEdit()
        self.skeleton_entry.setPlaceholderText("10")
        self.skeleton_entry.setText("10")
        self.skeleton_entry.setFixedWidth(60)
        self.skeleton_entry.setStyleSheet("""
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
        skeleton_row.addWidget(self.skeleton_entry)
        
        skeleton_row.addStretch()
        group_layout.addLayout(skeleton_row)
        
        # Plunder Chest Row
        plunder_row = QHBoxLayout()
        plunder_row.setSpacing(12)
        
        plunder_label = QLabel("Plunder Chest:")
        plunder_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px; color: #E0E0E0;")
        plunder_row.addWidget(plunder_label)
        
        self.plunder_entry = LineEdit()
        self.plunder_entry.setPlaceholderText("15")
        self.plunder_entry.setText("15")
        self.plunder_entry.setFixedWidth(60)
        self.plunder_entry.setStyleSheet("""
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
        plunder_row.addWidget(self.plunder_entry)
        
        plunder_row.addStretch()
        group_layout.addLayout(plunder_row)
        
        # Dueling Glove Row
        dueling_row = QHBoxLayout()
        dueling_row.setSpacing(12)
        
        dueling_label = QLabel("Dueling Glove:")
        dueling_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px; color: #E0E0E0;")
        dueling_row.addWidget(dueling_label)
        
        self.dueling_entry = LineEdit()
        self.dueling_entry.setPlaceholderText("15")
        self.dueling_entry.setText("15")
        self.dueling_entry.setFixedWidth(60)
        self.dueling_entry.setStyleSheet("""
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
        dueling_row.addWidget(self.dueling_entry)
        
        dueling_row.addStretch()
        group_layout.addLayout(dueling_row)
        
        # Warp Block Row
        warp_row = QHBoxLayout()
        warp_row.setSpacing(12)
        
        warp_label = QLabel("Warp Block:")
        warp_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px; color: #E0E0E0;")
        warp_row.addWidget(warp_label)
        
        self.warp_entry = LineEdit()
        self.warp_entry.setPlaceholderText("20")
        self.warp_entry.setText("20")
        self.warp_entry.setFixedWidth(60)
        self.warp_entry.setStyleSheet("""
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
        warp_row.addWidget(self.warp_entry)
        
        warp_row.addStretch()
        group_layout.addLayout(warp_row)
        
        # Golden Mushroom Row
        golden_row = QHBoxLayout()
        golden_row.setSpacing(12)
        
        golden_label = QLabel("Golden Mushroom:")
        golden_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px; color: #E0E0E0;")
        golden_row.addWidget(golden_label)
        
        self.golden_entry = LineEdit()
        self.golden_entry.setPlaceholderText("30")
        self.golden_entry.setText("30")
        self.golden_entry.setFixedWidth(60)
        self.golden_entry.setStyleSheet("""
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
        golden_row.addWidget(self.golden_entry)
        
        golden_row.addStretch()
        group_layout.addLayout(golden_row)
        
        # Magic Lamp Row
        lamp_row = QHBoxLayout()
        lamp_row.setSpacing(12)
        
        lamp_label = QLabel("Magic Lamp:")
        lamp_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px; color: #E0E0E0;")
        lamp_row.addWidget(lamp_label)
        
        self.lamp_entry = LineEdit()
        self.lamp_entry.setPlaceholderText("30")
        self.lamp_entry.setText("30")
        self.lamp_entry.setFixedWidth(60)
        self.lamp_entry.setStyleSheet("""
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
        lamp_row.addWidget(self.lamp_entry)
        
        lamp_row.addStretch()
        group_layout.addLayout(lamp_row)
        
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
        if self.game_id == "marioParty2":
            try:
                if 'itemsEvent_mp2' in globals():
                    # Create mock objects to match the expected interface
                    class MockEntry:
                        def __init__(self, text):
                            self._text = text
                        def get(self):
                            return self._text
                        def text(self):
                            return self._text
                    
                    # Create mock objects with current values
                    mushroom = MockEntry(self.mushroom_entry.text())
                    skeleton_key = MockEntry(self.skeleton_entry.text())
                    plunder_chest = MockEntry(self.plunder_entry.text())
                    dueling_glove = MockEntry(self.dueling_entry.text())
                    warp_block = MockEntry(self.warp_entry.text())
                    golden_mushroom = MockEntry(self.golden_entry.text())
                    magic_lamp = MockEntry(self.lamp_entry.text())
                    
                    itemsEvent_mp2(mushroom, skeleton_key, plunder_chest, dueling_glove, warp_block, golden_mushroom, magic_lamp)
                else:
                    self.show_error("Mario Party 2 items modification not available")
            except Exception as e:
                self.show_error(f"Error generating codes: {str(e)}")
        else:
            self.show_error(f"Items modification not supported for {self.game_id}")
    
    def show_error(self, message):
        """Show error message to user"""
        QMessageBox.critical(self, "Error", message)
