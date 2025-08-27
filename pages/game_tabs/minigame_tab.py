#!/usr/bin/env python3
# ============================================
# Minigame Tab Component
# Converted from CTk to PyQt5 for Mario Party Toolkit
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy, QLabel, QComboBox, QMessageBox, QApplication, QGroupBox
from PyQt5.QtCore import Qt
from qfluentwidgets import SubtitleLabel, BodyLabel, ComboBox, PushButton, InfoBar, InfoBarPosition, FluentIcon

# Import minigame replacement functions for all supported games
try:
    from events.marioParty1_mgreplace import mgReplaceEvent_mp1
    from events.marioParty2_mgreplace import mgReplaceEvent_mp2
    from events.marioParty3_mgreplace import mgReplaceEvent_mp3
    from events.marioParty4_mgreplace import mgReplaceEvent_mp4
    from events.marioParty5_mgreplace import mgReplaceEvent_mp5
    from events.marioParty6_mgreplace import mgReplaceEvent_mp6
    from events.marioParty7_mgreplace import mgReplaceEvent_mp7
    from events.marioParty8_mgreplace import mgReplaceEvent_mp8
    from events.marioParty9_mgreplace import mgReplaceEvent_mp9
    from events.marioPartyDS_mgreplace import mgReplaceEvent_mpDS
except ImportError:
    # Handle missing imports gracefully
    pass


class MinigameTab(QWidget):
    def __init__(self, game_id):
        super().__init__()
        self.game_id = game_id
        self.setup_ui()

    def setup_ui(self):
        """Set up the minigame tab UI"""
        self.setObjectName(f"{self.game_id}MinigameTab")
        
        # Main layout
        layout = QVBoxLayout()
        layout.setSpacing(8)
        layout.setContentsMargins(16, 12, 16, 12)
        
        # Title
        title = SubtitleLabel("Minigame Replacement")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Description
        desc = BodyLabel("Replace specific minigames with custom selections:")
        desc.setAlignment(Qt.AlignCenter)
        layout.addWidget(desc)
        
        # Minigame Replacement Group
        group = QGroupBox("Minigame Replacement")
        
        # Store reference to group for theme updates
        self.minigame_group = group
        
        # Apply initial styling
        self.update_minigame_group_theme()
        
        group_layout = QVBoxLayout()
        group.setLayout(group_layout)
        
        # Minigame selection row
        selection_row = QHBoxLayout()
        selection_row.setSpacing(16)
        
        # "Replace" label
        replace_label = BodyLabel("Replace")
        replace_label.setStyleSheet("font-size: 18px; font-weight: 600; min-width: 80px;")
        selection_row.addWidget(replace_label)
        
        # First minigame selection
        self.mg1_combo = ComboBox()
        self.mg1_combo.setFixedWidth(200)
        selection_row.addWidget(self.mg1_combo)
        
        # "with" label
        with_label = BodyLabel("with")
        with_label.setStyleSheet("font-size: 18px; font-weight: 600; min-width: 60px;")
        selection_row.addWidget(with_label)
        
        # Second minigame selection
        self.mg2_combo = ComboBox()
        self.mg2_combo.setFixedWidth(200)
        selection_row.addWidget(self.mg2_combo)
        
        selection_row.addStretch()
        group_layout.addLayout(selection_row)
        
        # Add group to main layout
        layout.addWidget(group)
        
        # Generate button
        generate_btn = PushButton("Generate Codes")
        generate_btn.clicked.connect(self.generate_codes)
        layout.addWidget(generate_btn)
        
        # Add stretch to push everything up
        layout.addStretch()
        
        self.setLayout(layout)
        
        # Populate minigame lists
        self.populate_minigame_lists()

    def populate_minigame_lists(self):
        """Populate minigame lists based on the current game"""
        if self.game_id == "marioParty1":
            # Based on the hex array in marioParty1_mgreplace.py
            minigames_list = [
                "NONE", "Bumper Balls", "Coin Block Blitz", "Coin Block Bash", "Coin Block Battle",
                "Coin Block Blast", "Coin Block Blitz", "Coin Block Bash", "Coin Block Battle"
            ]
        elif self.game_id == "marioParty2":
            # Based on the hex array in marioParty2_mgreplace.py
            minigames_list = [
                "NONE", "Bumper Balls", "Coin Block Blitz", "Coin Block Bash", "Coin Block Battle",
                "Coin Block Blast", "Coin Block Blitz", "Coin Block Bash", "Coin Block Battle"
            ]
        elif self.game_id == "marioParty3":
            # Based on the hex array in marioParty3_mgreplace.py
            minigames_list = [
                "NONE", "Bumper Balls", "Coin Block Blitz", "Coin Block Bash", "Coin Block Battle",
                "Coin Block Blast", "Coin Block Blitz", "Coin Block Bash", "Coin Block Battle"
            ]
        elif self.game_id == "marioParty4":
            # Based on the hex array in marioParty4_mgreplace.py
            minigames_list = [
                "NONE", "Bumper Balls", "Coin Block Blitz", "Coin Block Bash", "Coin Block Battle",
                "Coin Block Blast", "Coin Block Blitz", "Coin Block Bash", "Coin Block Battle"
            ]
        elif self.game_id == "marioParty5":
            # Based on the hex array in marioParty5_mgreplace.py
            minigames_list = [
                "NONE", "Bumper Balls", "Coin Block Blitz", "Coin Block Bash", "Coin Block Battle",
                "Coin Block Blast", "Coin Block Blitz", "Coin Block Bash", "Coin Block Battle"
            ]
        elif self.game_id == "marioParty6":
            # Based on the hex array in marioParty6_mgreplace.py
            minigames_list = [
                "NONE", "Bumper Balls", "Coin Block Blitz", "Coin Block Bash", "Coin Block Battle",
                "Coin Block Blast", "Coin Block Blitz", "Coin Block Bash", "Coin Block Battle"
            ]
        elif self.game_id == "marioParty7":
            # Based on the hex array in marioParty7_mgreplace.py
            minigames_list = [
                "NONE", "Bumper Balls", "Coin Block Blitz", "Coin Block Bash", "Coin Block Battle",
                "Coin Block Blast", "Coin Block Blitz", "Coin Block Bash", "Coin Block Battle"
            ]
        elif self.game_id == "marioParty8":
            # Based on the hex array in marioParty8_mgreplace.py
            minigames_list = [
                "NONE", "Bumper Balls", "Coin Block Blitz", "Coin Block Bash", "Coin Block Battle",
                "Coin Block Blast", "Coin Block Blitz", "Coin Block Bash", "Coin Block Battle"
            ]
        elif self.game_id == "marioParty9":
            # Based on the hex array in marioParty9_mgreplace.py
            minigames_list = [
                "NONE", "Bumper Balls", "Coin Block Blitz", "Coin Block Bash", "Coin Block Battle",
                "Coin Block Blast", "Coin Block Blitz", "Coin Block Bash", "Coin Block Battle"
            ]
        elif self.game_id == "marioPartyDS":
            # Based on the hex array in marioPartyDS_mgreplace.py
            minigames_list = [
                "NONE", "Bumper Balls", "Coin Block Blitz", "Coin Block Bash", "Coin Block Battle",
                "Coin Block Blast", "Coin Block Blitz", "Coin Block Bash", "Coin Block Battle"
            ]
        else:
            # Default list for unsupported games
            minigames_list = ["NONE"]
        
        # Populate both combo boxes
        self.mg1_combo.addItems(minigames_list)
        self.mg2_combo.addItems(minigames_list)
        
        # Set default selections
        if len(minigames_list) > 0:
            self.mg1_combo.setCurrentText(minigames_list[0])
            if len(minigames_list) > 1:
                self.mg2_combo.setCurrentText(minigames_list[1])

    def generate_codes(self):
        """Generate codes for the current game"""
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
            mg1 = MockComboBox(self.mg1_combo.currentText())
            mg2 = MockComboBox(self.mg2_combo.currentText())

            # Call appropriate minigame replacement function based on game
            if self.game_id == "marioParty1" and 'mgReplaceEvent_mp1' in globals():
                mgReplaceEvent_mp1(mg1, mg2)
            elif self.game_id == "marioParty2" and 'mgReplaceEvent_mp2' in globals():
                mgReplaceEvent_mp2(mg1, mg2)
            elif self.game_id == "marioParty3" and 'mgReplaceEvent_mp3' in globals():
                mgReplaceEvent_mp3(mg1, mg2)
            elif self.game_id == "marioParty4" and 'mgReplaceEvent_mp4' in globals():
                mgReplaceEvent_mp4(mg1, mg2)
            elif self.game_id == "marioParty5" and 'mgReplaceEvent_mp5' in globals():
                mgReplaceEvent_mp5(mg1, mg2)
            elif self.game_id == "marioParty6" and 'mgReplaceEvent_mp6' in globals():
                mgReplaceEvent_mp6(mg1, mg2)
            elif self.game_id == "marioParty7" and 'mgReplaceEvent_mp7' in globals():
                mgReplaceEvent_mp7(mg1, mg2)
            elif self.game_id == "marioParty8" and 'mgReplaceEvent_mp8' in globals():
                mgReplaceEvent_mp8(mg1, mg2)
            elif self.game_id == "marioParty9" and 'mgReplaceEvent_mp9' in globals():
                mgReplaceEvent_mp9(mg1, mg2)
            elif self.game_id == "marioPartyDS" and 'mgReplaceEvent_mpDS' in globals():
                mgReplaceEvent_mpDS(mg1, mg2)
            else:
                self.show_error(f"Minigame replacement not available for {self.game_id}")
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
    
    def update_minigame_group_theme(self):
        """Update the minigame group styling based on current theme"""
        from qfluentwidgets import isDarkTheme
        if isDarkTheme():
            self.minigame_group.setStyleSheet("""
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
            self.minigame_group.setStyleSheet("""
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
        self.update_minigame_group_theme()
