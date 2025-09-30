# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

# ============================================
# Board Specific Tab Component for Mario Party 5
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout
from PyQt5.QtCore import Qt
from qfluentwidgets import SubtitleLabel, BodyLabel, ComboBox, PushButton, CardWidget

try:
    from events.marioParty5_boardSpecific import underseaEvent_mp5
except ImportError:
    underseaEvent_mp5 = None


class BoardSpecificMp5Tab(QWidget):
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

        desc = BodyLabel("Undersea Dream: Set the Seashell reward to a specific capsule.")
        desc.setAlignment(Qt.AlignCenter)
        layout.addWidget(desc)

        card = CardWidget()
        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(20, 16, 20, 16)
        card_layout.setSpacing(16)
        card.setLayout(card_layout)

        # Undersea Dream Seashell row
        row = QHBoxLayout()
        row.setSpacing(12)

        label = BodyLabel("Undersea Dream - Seashell Always Gives:")
        label.setStyleSheet("font-size: 16px; min-width: 280px;")
        row.addWidget(label)

        # Values pulled from old CTk frame
        self.item_list = [
            "Nothing", "Golden Mushroom", "Poison Mushroom", "Warp Pipe", "Klepto", "Bubble", "Wiggler",
            "Hammer Bro", "Coin Block", "Spiny", "Paratroopa", "Goomba", "Bob-omb", "Koopa Bank",
            "Kamek", "Mr. Blizzard", "Piranha Plant", "Magikoopa", "Ukiki", "Lakitu", "Tweester",
            "Duel", "Chain Chomp", "Bone", "Bowser", "Chance", "Miracle", "Donkey Kong"
        ]
        self.combo = ComboBox()
        self.combo.addItems(self.item_list)
        self.combo.setFixedWidth(280)
        row.addWidget(self.combo)

        row.addStretch()
        card_layout.addLayout(row)

        layout.addWidget(card)

        btn = PushButton("Generate Code")
        btn.clicked.connect(self.generate_codes)
        layout.addWidget(btn)

        layout.addStretch()
        self.setLayout(layout)

    def generate_codes(self):
        if not underseaEvent_mp5:
            from qfluentwidgets import InfoBar, InfoBarPosition
            InfoBar.error(title="Error", content="MP5 board-specific event not available", orient=Qt.Horizontal, isClosable=True, position=InfoBarPosition.TOP, duration=3000, parent=self)
            return

        class ComboProxy:
            def __init__(self, text: str):
                self._t = text
            def get(self):
                return self._t

        item = ComboProxy(self.combo.currentText())
        try:
            underseaEvent_mp5(item, self.item_list)
        except Exception as e:
            from qfluentwidgets import InfoBar, InfoBarPosition
            InfoBar.error(title="Error", content=str(e), orient=Qt.Horizontal, isClosable=True, position=InfoBarPosition.TOP, duration=3000, parent=self)


