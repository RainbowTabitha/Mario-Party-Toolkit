#!/usr/bin/env python3
# ============================================
# Handicap Tab Component
# Converted from CTk to PyQt5 for Mario Party 1
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QSizePolicy, QLabel, QLineEdit, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QIcon, QPixmap
from qfluentwidgets import SubtitleLabel, BodyLabel

from functions import fetchResource

# Import handicap event functions for all supported games
try:
    from events.marioParty1_handicap import handicapEvent_mp1
    from events.marioParty2_handicap import handicapEvent_mp2
    from events.marioParty3_handicap import handicapEvent_mp3
    from events.marioParty4_handicap import handicapEvent_mp4
    from events.marioParty5_handicap import handicapEvent_mp5
    from events.marioParty6_handicap import handicapEvent_mp6
    from events.marioParty7_handicap import handicapEvent_mp7
    from events.marioParty8_handicap import handicapEvent_mp8
    from events.marioParty9_handicap import handicapEvent_mp9
    from events.marioPartyDS_handicap import handicapEvent_mpDS
except ImportError:
    # Handle missing imports gracefully
    pass


class HandicapTab(QWidget):
    def __init__(self, game_id):
        super().__init__()
        self.game_id = game_id
        self.setup_ui()

    def setup_ui(self):
        """Set up the handicap tab UI"""
        self.setObjectName(f"{self.game_id}HandicapTab")
        # Main layout with reduced spacing
        layout = QVBoxLayout()
        layout.setSpacing(8)  # Reduced from 12
        layout.setContentsMargins(16, 8, 16, 8)  # Reduced top/bottom margins
        
        # Title with reduced margin
        title = QLabel("Player Star Handicaps")
        title.setStyleSheet("""
            font-size: 24px;
            font-weight: 700;
            color: #E0E0E0;
            margin: 8px 0;  /* Reduced from 16px */
            text-align: center;
        """)
        layout.addWidget(title)
        
        # Description with reduced margin
        desc = BodyLabel("Set starting star counts for each player:")
        desc.setStyleSheet("""
            font-size: 15px;
            color: #E0E0E0;
            margin-bottom: 4px;  /* Reduced from 8px */
            text-align: center;
        """)
        layout.addWidget(desc)
        
        # Player Handicaps Group
        group = QGroupBox("Player Starting Stars")
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
        
        # Grid layout for player rows
        grid_layout = QVBoxLayout()
        grid_layout.setSpacing(8)  # Reduced from 12
        grid_layout.setContentsMargins(0, 0, 0, 0)
        
        # Player 1 Row
        p1_row = QHBoxLayout()
        p1_row.setSpacing(8)  # Reduced from 12
        
        p1_label = QLabel("Player 1:")
        p1_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 60px; color: #E0E0E0;")  # Reduced min-width
        p1_row.addWidget(p1_label)
        
        self.p1_entry = QLineEdit()
        self.p1_entry.setPlaceholderText("0")
        self.p1_entry.setText("0")
        self.p1_entry.setFixedWidth(50)  # Reduced from 60
        self.p1_entry.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                font-weight: 600;
                padding: 6px 8px;  /* Reduced from 8px 10px */
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
        p1_row.addWidget(self.p1_entry)
        
        p1_desc = QLabel("starting stars")
        p1_desc.setStyleSheet("font-size: 15px; color: #D0D0D0; margin: 0 12px; font-weight: 500;")  # Reduced margin
        p1_row.addWidget(p1_desc)
        
        p1_row.addStretch()
        grid_layout.addLayout(p1_row)
        
        # Player 2 Row
        p2_row = QHBoxLayout()
        p2_row.setSpacing(8)  # Reduced from 12
        
        p2_label = QLabel("Player 2:")
        p2_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 60px; color: #E0E0E0;")  # Reduced min-width
        p2_row.addWidget(p2_label)
        
        self.p2_entry = QLineEdit()
        self.p2_entry.setPlaceholderText("0")
        self.p2_entry.setText("0")
        self.p2_entry.setFixedWidth(50)  # Reduced from 60
        self.p2_entry.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                font-weight: 600;
                padding: 6px 8px;  /* Reduced from 8px 10px */
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
        p2_row.addWidget(self.p2_entry)
        
        p2_desc = QLabel("starting stars")
        p2_desc.setStyleSheet("font-size: 15px; color: #D0D0D0; margin: 0 12px; font-weight: 500;")  # Reduced margin
        p2_row.addWidget(p2_desc)
        
        p2_row.addStretch()
        grid_layout.addLayout(p2_row)
        
        # Player 3 Row
        p3_row = QHBoxLayout()
        p3_row.setSpacing(8)  # Reduced from 12
        
        p3_label = QLabel("Player 3:")
        p3_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 60px; color: #E0E0E0;")  # Reduced min-width
        p3_row.addWidget(p3_label)
        
        self.p3_entry = QLineEdit()
        self.p3_entry.setPlaceholderText("0")
        self.p3_entry.setText("0")
        self.p3_entry.setFixedWidth(50)  # Reduced from 60
        self.p3_entry.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                font-weight: 600;
                padding: 6px 8px;  /* Reduced from 8px 10px */
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
        p3_row.addWidget(self.p3_entry)
        
        p3_desc = QLabel("starting stars")
        p3_desc.setStyleSheet("font-size: 15px; color: #D0D0D0; margin: 0 12px; font-weight: 500;")  # Reduced margin
        p3_row.addWidget(p3_desc)
        
        p3_row.addStretch()
        grid_layout.addLayout(p3_row)
        
        # Player 4 Row
        p4_row = QHBoxLayout()
        p4_row.setSpacing(8)  # Reduced from 12
        
        p4_label = QLabel("Player 4:")
        p4_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 60px; color: #E0E0E0;")  # Reduced min-width
        p4_row.addWidget(p4_label)
        
        self.p4_entry = QLineEdit()
        self.p4_entry.setPlaceholderText("0")
        self.p4_entry.setText("0")
        self.p4_entry.setFixedWidth(50)  # Reduced from 60
        self.p4_entry.setStyleSheet("""
            QLineEdit {
                font-size: 15px;
                font-weight: 600;
                padding: 6px 8px;  /* Reduced from 8px 10px */
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
        p4_row.addWidget(self.p4_entry)
        
        p4_desc = QLabel("starting stars")
        p4_desc.setStyleSheet("font-size: 15px; color: #D0D0D0; margin: 0 12px; font-weight: 500;")  # Reduced margin
        p4_row.addWidget(p4_desc)
        
        p4_row.addStretch()
        grid_layout.addLayout(p4_row)
        
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
        # Get player handicap values
        p1_stars = self.p1_entry.text() or "0"
        p2_stars = self.p2_entry.text() or "0"
        p3_stars = self.p3_entry.text() or "0"
        p4_stars = self.p4_entry.text() or "0"
        
        try:
            # Call appropriate handicap function based on game
            if self.game_id == "marioParty1":
                if 'handicapEvent_mp1' in globals():
                    handicapEvent_mp1(self.p1_entry, self.p2_entry, self.p3_entry, self.p4_entry)
                else:
                    self.show_error("Mario Party 1 handicap not available")
            elif self.game_id == "marioParty2":
                if 'handicapEvent_mp2' in globals():
                    handicapEvent_mp2(self.p1_entry, self.p2_entry, self.p3_entry, self.p4_entry)
                else:
                    self.show_error("Mario Party 2 handicap not available")
            elif self.game_id == "marioParty3":
                if 'handicapEvent_mp3' in globals():
                    handicapEvent_mp3(self.p1_entry, self.p2_entry, self.p3_entry, self.p4_entry)
                else:
                    self.show_error("Mario Party 3 handicap not available")
            elif self.game_id == "marioParty4":
                if 'handicapEvent_mp4' in globals():
                    handicapEvent_mp4(self.p1_entry, self.p2_entry, self.p3_entry, self.p4_entry)
                else:
                    self.show_error("Mario Party 4 handicap not available")
            elif self.game_id == "marioParty5":
                if 'handicapEvent_mp5' in globals():
                    handicapEvent_mp5(self.p1_entry, self.p2_entry, self.p3_entry, self.p4_entry)
                else:
                    self.show_error("Mario Party 5 handicap not available")
            elif self.game_id == "marioParty6":
                if 'handicapEvent_mp6' in globals():
                    handicapEvent_mp6(self.p1_entry, self.p2_entry, self.p3_entry, self.p4_entry)
                else:
                    self.show_error("Mario Party 6 handicap not available")
            elif self.game_id == "marioParty7":
                if 'handicapEvent_mp7' in globals():
                    handicapEvent_mp7(self.p1_entry, self.p2_entry, self.p3_entry, self.p4_entry)
                else:
                    self.show_error("Mario Party 7 handicap not available")
            elif self.game_id == "marioParty8":
                if 'handicapEvent_mp8' in globals():
                    handicapEvent_mp8(self.p1_entry, self.p2_entry, self.p3_entry, self.p4_entry)
                else:
                    self.show_error("Mario Party 8 handicap not available")
            elif self.game_id == "marioParty9":
                if 'handicapEvent_mp9' in globals():
                    handicapEvent_mp9(self.p1_entry, self.p2_entry, self.p3_entry, self.p4_entry)
                else:
                    self.show_error("Mario Party 9 handicap not available")
            elif self.game_id == "marioPartyDS":
                if 'handicapEvent_mpDS' in globals():
                    handicapEvent_mpDS(self.p1_entry, self.p2_entry, self.p3_entry, self.p4_entry)
                else:
                    self.show_error("Mario Party DS handicap not available")
            else:
                self.show_error(f"Handicap not supported for {self.game_id}")
                
        except Exception as e:
            self.show_error(f"Error generating codes: {str(e)}")
    
    def show_error(self, message):
        """Show error message to user"""
        QMessageBox.critical(self, "Error", message)
