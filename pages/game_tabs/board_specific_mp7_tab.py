# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

# ============================================
# Board Specific Tab Component for Mario Party 7
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLineEdit
from PyQt5.QtCore import Qt
from qfluentwidgets import SubtitleLabel, BodyLabel, ComboBox, PushButton, CardWidget, LineEdit

try:
    from events.marioParty7_boardSpecific import (
        spinxEvent_mp7, gliderEvent_mp7, chompEvent_mp7, 
        redChompEvent_mp7, gliderCostEvent_mp7, windmillEvent_mp7
    )
except ImportError:
    spinxEvent_mp7 = None
    gliderEvent_mp7 = None
    chompEvent_mp7 = None
    redChompEvent_mp7 = None
    gliderCostEvent_mp7 = None
    windmillEvent_mp7 = None


class BoardSpecificMp7Tab(QWidget):
    def __init__(self, game_id: str):
        super().__init__()
        self.game_id = game_id
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName(f"{self.game_id}BoardSpecificTab")

        layout = QVBoxLayout()
        layout.setSpacing(8)
        layout.setContentsMargins(16, 12, 16, 12)

        title = SubtitleLabel("Board Specific Mods")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        desc = BodyLabel("Modify board-specific features for Mario Party 7 boards.")
        desc.setAlignment(Qt.AlignCenter)
        layout.addWidget(desc)

        # Pyramid Park Features Card
        pyramid_card = CardWidget()
        pyramid_layout = QVBoxLayout()
        pyramid_layout.setContentsMargins(20, 16, 20, 16)
        pyramid_layout.setSpacing(16)
        pyramid_card.setLayout(pyramid_layout)

        pyramid_title = BodyLabel("Pyramid Park Features")
        pyramid_title.setStyleSheet("font-size: 18px; font-weight: bold; color: #8B4513;")
        pyramid_layout.addWidget(pyramid_title)

        # Spinx Event
        spinx_row = QHBoxLayout()
        spinx_row.setSpacing(12)

        spinx_label = BodyLabel("Spinx Always Gives:")
        spinx_label.setStyleSheet("font-size: 14px; min-width: 200px;")
        spinx_row.addWidget(spinx_label)

        self.spinx_combo = ComboBox()
        self.spinx_combo.addItems(["Do Nothing", "Blue to Red Spaces", "Half Chomp Price", "Coin Equality"])
        spinx_row.addWidget(self.spinx_combo)

        spinx_button = PushButton("Apply")
        spinx_button.clicked.connect(self.apply_spinx)
        spinx_row.addWidget(spinx_button)

        pyramid_layout.addLayout(spinx_row)

        # Black Chomp
        black_chomp_row = QHBoxLayout()
        black_chomp_row.setSpacing(12)

        black_chomp_label = BodyLabel("Black Chomp Reward:")
        black_chomp_label.setStyleSheet("font-size: 14px; min-width: 200px;")
        black_chomp_row.addWidget(black_chomp_label)

        self.black_chomp_entry = LineEdit()
        self.black_chomp_entry.setPlaceholderText("Enter coin amount")
        black_chomp_row.addWidget(self.black_chomp_entry)

        black_chomp_button = PushButton("Apply")
        black_chomp_button.clicked.connect(self.apply_black_chomp)
        black_chomp_row.addWidget(black_chomp_button)

        pyramid_layout.addLayout(black_chomp_row)

        # Red Chomp
        red_chomp_row = QHBoxLayout()
        red_chomp_row.setSpacing(12)

        red_chomp_label = BodyLabel("Red Chomp Reward:")
        red_chomp_label.setStyleSheet("font-size: 14px; min-width: 200px;")
        red_chomp_row.addWidget(red_chomp_label)

        self.red_chomp_entry = LineEdit()
        self.red_chomp_entry.setPlaceholderText("Enter coin amount")
        red_chomp_row.addWidget(self.red_chomp_entry)

        red_chomp_button = PushButton("Apply")
        red_chomp_button.clicked.connect(self.apply_red_chomp)
        red_chomp_row.addWidget(red_chomp_button)

        pyramid_layout.addLayout(red_chomp_row)
        layout.addWidget(pyramid_card)

        # Windmillville Features Card
        windmillville_card = CardWidget()
        windmillville_layout = QVBoxLayout()
        windmillville_layout.setContentsMargins(20, 16, 20, 16)
        windmillville_layout.setSpacing(16)
        windmillville_card.setLayout(windmillville_layout)

        windmillville_title = BodyLabel("Windmillville Features")
        windmillville_title.setStyleSheet("font-size: 18px; font-weight: bold; color: #4169E1;")
        windmillville_layout.addWidget(windmillville_title)

        # Glider Event
        glider_row = QHBoxLayout()
        glider_row.setSpacing(12)

        glider_label = BodyLabel("Glider Always Gives:")
        glider_label.setStyleSheet("font-size: 14px; min-width: 200px;")
        glider_row.addWidget(glider_label)

        self.glider_combo = ComboBox()
        self.glider_combo.addItems(["1 Star (right)", "2 Star (left)", "3 Star (center)"])
        glider_row.addWidget(self.glider_combo)

        glider_button = PushButton("Apply")
        glider_button.clicked.connect(self.apply_glider)
        glider_row.addWidget(glider_button)

        windmillville_layout.addLayout(glider_row)

        # Glider Cost
        glider_cost_row = QHBoxLayout()
        glider_cost_row.setSpacing(12)

        glider_cost_label = BodyLabel("Glider Cost:")
        glider_cost_label.setStyleSheet("font-size: 14px; min-width: 200px;")
        glider_cost_row.addWidget(glider_cost_label)

        self.glider_cost_entry = LineEdit()
        self.glider_cost_entry.setPlaceholderText("Enter coin cost")
        glider_cost_row.addWidget(self.glider_cost_entry)

        glider_cost_button = PushButton("Apply")
        glider_cost_button.clicked.connect(self.apply_glider_cost)
        glider_cost_row.addWidget(glider_cost_button)

        windmillville_layout.addLayout(glider_cost_row)

        # Windmill Event
        windmill_row = QHBoxLayout()
        windmill_row.setSpacing(12)

        windmill_label = BodyLabel("Windmill Max Reward:")
        windmill_label.setStyleSheet("font-size: 14px; min-width: 200px;")
        windmill_row.addWidget(windmill_label)

        self.windmill_entry = LineEdit()
        self.windmill_entry.setPlaceholderText("Enter coin amount")
        windmill_row.addWidget(self.windmill_entry)

        windmill_button = PushButton("Apply")
        windmill_button.clicked.connect(self.apply_windmill)
        windmill_row.addWidget(windmill_button)

        windmillville_layout.addLayout(windmill_row)
        layout.addWidget(windmillville_card)

        layout.addStretch()
        self.setLayout(layout)

    def apply_spinx(self):
        """Apply Spinx event modification"""
        if spinxEvent_mp7:
            # Create a mock object with get() method for compatibility
            class MockCombo:
                def __init__(self, combo_box):
                    self.combo_box = combo_box
                def get(self):
                    return self.combo_box.currentText()
            
            mock_combo = MockCombo(self.spinx_combo)
            spinx_list = ["Do Nothing", "Blue to Red Spaces", "Half Chomp Price", "Coin Equality"]
            spinxEvent_mp7(mock_combo, spinx_list)

    def apply_glider(self):
        """Apply Glider event modification"""
        if gliderEvent_mp7:
            # Create a mock object with get() method for compatibility
            class MockCombo:
                def __init__(self, combo_box):
                    self.combo_box = combo_box
                def get(self):
                    return self.combo_box.currentText()
            
            mock_combo = MockCombo(self.glider_combo)
            glider_list = ["1 Star (right)", "2 Star (left)", "3 Star (center)"]
            gliderEvent_mp7(mock_combo, glider_list)

    def apply_glider_cost(self):
        """Apply Glider cost modification"""
        if gliderCostEvent_mp7:
            # Create a mock object with get() method for compatibility
            class MockEntry:
                def __init__(self, line_edit):
                    self.line_edit = line_edit
                def get(self):
                    return self.line_edit.text()
            
            mock_entry = MockEntry(self.glider_cost_entry)
            gliderCostEvent_mp7(mock_entry)

    def apply_black_chomp(self):
        """Apply Black Chomp modification"""
        if chompEvent_mp7:
            # Create a mock object with get() method for compatibility
            class MockEntry:
                def __init__(self, line_edit):
                    self.line_edit = line_edit
                def get(self):
                    return self.line_edit.text()
            
            mock_entry = MockEntry(self.black_chomp_entry)
            chompEvent_mp7(mock_entry)

    def apply_red_chomp(self):
        """Apply Red Chomp modification"""
        if redChompEvent_mp7:
            # Create a mock object with get() method for compatibility
            class MockEntry:
                def __init__(self, line_edit):
                    self.line_edit = line_edit
                def get(self):
                    return self.line_edit.text()
            
            mock_entry = MockEntry(self.red_chomp_entry)
            redChompEvent_mp7(mock_entry)

    def apply_windmill(self):
        """Apply Windmill modification"""
        if windmillEvent_mp7:
            # Create a mock object with get() method for compatibility
            class MockEntry:
                def __init__(self, line_edit):
                    self.line_edit = line_edit
                def get(self):
                    return self.line_edit.text()
            
            mock_entry = MockEntry(self.windmill_entry)
            windmillEvent_mp7(mock_entry)