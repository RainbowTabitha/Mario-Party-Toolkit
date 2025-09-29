#!/usr/bin/env python3
# ============================================
# Capsule Mods Tab Component for Mario Party 5
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from qfluentwidgets import SubtitleLabel, BodyLabel, LineEdit, PushButton, CardWidget

from utils.resource_manager import ResourceManager

try:
    from events.marioParty5_items import itemsEvent_mp5
except ImportError:
    itemsEvent_mp5 = None


class CapsuleModsMp5Tab(QWidget):
    def __init__(self, game_id: str):
        super().__init__()
        self.game_id = game_id
        self.inputs = {}
        self.setup_ui()

    def setup_ui(self):
        self.setObjectName(f"{self.game_id}CapsuleModsTab")

        layout = QVBoxLayout()
        layout.setSpacing(8)
        layout.setContentsMargins(16, 12, 16, 12)

        title = SubtitleLabel("Capsule Mods (Prices & Weights)")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        desc = BodyLabel("Set capsule shop prices and distribution weights. All fields are required for MP5 generation.")
        desc.setAlignment(Qt.AlignCenter)
        layout.addWidget(desc)

        card = CardWidget()
        card_layout = QVBoxLayout()
        card_layout.setSpacing(16)
        card_layout.setContentsMargins(20, 16, 20, 16)
        card.setLayout(card_layout)

        # Scroll area
        scroll = QScrollArea()
        scroll.setWidgetResizable(True)
        scroll.setFrameShape(QFrame.NoFrame)
        scroll.viewport().setStyleSheet("background: transparent;")

        content = QWidget()
        content.setStyleSheet("background: transparent;")
        content_layout = QVBoxLayout(content)
        content_layout.setContentsMargins(0, 0, 0, 0)
        content_layout.setSpacing(10)

        # Capsule rows: label, icon, priceKey, weightKey (UI always shows price then weight side-by-side)
        # Order matches the old frame UI exactly
        rows = [
            ("Mushroom", "assets/items/mushroomCapsule.png", "mushroomCapsulePrice5", "mushroomCapsuleWeight5"),
            ("Super Mushroom", "assets/items/goldenMushroomCapsule.png", "goldenMushroomCapsulePrice5", "goldenMushroomCapsuleWeight5"),
            ("Cursed Mushroom", "assets/items/cursedMushroomCapsule.png", "cursedMushroomCapsulePrice5", "cursedMushroomCapsuleWeight5"),
            ("Warp Pipe", "assets/items/warpCapsule.png", "warpPipeCapsulePrice5", "warpPipeCapsuleWeight5"),
            ("Klepto", "assets/items/kleptoCapsule.png", "kleptoCapsulePrice5", "kleptoCapsuleWeight5"),
            ("Wiggler", "assets/items/wigglerCapsule.png", "flutterCapsulePrice5", "flutterCapsuleWeight5"),
            ("Podoboo", "assets/items/podobooCapsule5.png", "podobooCapsulePrice5", "podobooCapsuleWeight5"),
            ("Spiny", "assets/items/spinyCapsule.png", "spinyCapsulePrice5", "spinyCapsuleWeight5"),
            ("Coin Block", "assets/items/coinBlockCapsule.png", "coinBlockCapsulePrice5", "coinBlockCapsuleWeight5"),
            ("Hammer Bro", "assets/items/hammerBroCapsule.png", "hammerBroCapsulePrice5", "hammerBroCapsuleWeight5"),
            ("Paratroopa", "assets/items/paraTroopaCapsule.png", "paraTroopaCapsulePrice5", "paraTroopaCapsuleWeight5"),
            ("Bullet Bill", "assets/items/bulletBillCapsule.png", "bulletBillCapsulePrice5", "bulletBillCapsuleWeight5"),
            ("Mr. Blizzard", "assets/items/blizzardCapsule.png", "blizzardCapsulePrice5", "blizzardCapsuleWeight5"),
            ("Kamek", "assets/items/kamekCapsule.png", "kamekCapsulePrice5", "kamekCapsuleWeight5"),
            ("Magikoopa", "assets/items/toadyCapsule.png", "magiKoopaCapsulePrice5", "magiKoopaCapsuleWeight5"),
            ("Goomba", "assets/items/goombaCapsule.png", "goombaCapsulePrice5", "goombaCapsuleWeight5"),
            ("Piranha Plant", "assets/items/plantCapsule.png", "plantCapsulePrice5", "plantCapsuleWeight5"),
            ("Ukiki", "assets/items/ukikiCapsule.png", "ukikiCapsulePrice5", "ukikiCapsuleWeight5"),
            ("Tweester", "assets/items/tweesterCapsule.png", "tweesterCapsulePrice5", "tweesterCapsuleWeight5"),
            ("Lakitu", "assets/items/lakituCapsule.png", "lakituCapsulePrice5", "lakituCapsuleWeight5"),
            ("Miracle", "assets/items/miracleCapsule.png", "miracleCapsulePrice5", "miracleCapsuleWeight5"),
            ("Bone", "assets/items/snackCapsule.png", "boneCapsulePrice5", "boneCapsuleWeight5"),
            ("Chance", "assets/items/chanceCapsule.png", "chanceCapsulePrice5", "chanceCapsuleWeight5"),
            ("Chain Chomp", "assets/items/chainChompCapsule.png", "chainChompCapsulePrice5", "chainChompCapsuleWeight5"),
            ("Bowser", "assets/items/bowserCapsule.png", "bowserCapsulePrice5", "bowserCapsuleWeight5"),
            ("DK", "assets/items/dkCapsule.png", "dkCapsulePrice5", "dkCapsuleWeight5"),
            ("Bob-omb", "assets/items/bombCapsule.png", "bombCapsulePrice5", "bombCapsuleWeight5"),
            ("Koopa Bank", "assets/items/koopaBankCapsule.png", "koopaBankCapsulePrice5", "koopaBankCapsuleWeight5"),
            ("Duel", "assets/items/duelCapsule.png", "duelCapsulePrice5", "duelCapsuleWeight5"),
        ]

        # Build rows with Price and Weight side by side
        def add_capsule_row(display: str, icon_path: str, price_key: str, weight_key: str):
            row = QHBoxLayout()
            row.setSpacing(12)
            row.addWidget(self.create_image_label(icon_path, 28, 28))
            row.addWidget(BodyLabel(display + ":"))

            price_label = BodyLabel("Price:")
            row.addWidget(price_label)
            price_entry = LineEdit()
            price_entry.setFixedWidth(70)
            self.inputs[price_key] = price_entry
            row.addWidget(price_entry)

            weight_label = BodyLabel("Weight:")
            row.addWidget(weight_label)
            weight_entry = LineEdit()
            weight_entry.setFixedWidth(70)
            self.inputs[weight_key] = weight_entry
            row.addWidget(weight_entry)

            row.addStretch()
            content_layout.addLayout(row)

        for label, icon, price_key, weight_key in rows:
            add_capsule_row(label, icon, price_key, weight_key)

        scroll.setWidget(content)
        card_layout.addWidget(scroll)
        layout.addWidget(card)

        generate_btn = PushButton("Generate Codes")
        generate_btn.clicked.connect(self.generate_codes)
        layout.addWidget(generate_btn)

        layout.addStretch()
        self.setLayout(layout)

    def create_image_label(self, image_path: str, width: int = 28, height: int = 28):
        try:
            image_path = ResourceManager.get_resource_path(image_path)
            lbl = QLabel()
            pix = QPixmap(str(image_path))
            if not pix.isNull():
                lbl.setPixmap(pix.scaled(width, height, Qt.KeepAspectRatio, Qt.SmoothTransformation))
            else:
                lbl.setText("?")
            lbl.setFixedSize(width, height)
            lbl.setAlignment(Qt.AlignCenter)
            return lbl
        except Exception:
            fallback = QLabel("?")
            fallback.setFixedSize(width, height)
            fallback.setAlignment(Qt.AlignCenter)
            return fallback

    def generate_codes(self):
        if not itemsEvent_mp5:
            from qfluentwidgets import InfoBar, InfoBarPosition
            InfoBar.error(title="Error", content="MP5 capsule modification not available", orient=Qt.Horizontal, isClosable=True, position=InfoBarPosition.TOP, duration=3000, parent=self)
            return

        # Wrap LineEdits to expose .get()
        class EntryProxy:
            def __init__(self, line_edit: LineEdit):
                self._le = line_edit
            def get(self):
                return self._le.text()

        # Build argument list in exact signature order
        arg_order = [
            "bombCapsulePrice5", "bombCapsuleWeight5",
            "koopaBankCapsulePrice5", "koopaBankCapsuleWeight5",
            "bulletBillCapsulePrice5", "bulletBillCapsuleWeight5",
            "hammerBroCapsulePrice5", "hammerBroCapsuleWeight5",
            "coinBlockCapsulePrice5", "coinBlockCapsuleWeight5",
            "duelCapsulePrice5", "duelCapsuleWeight5",
            "mushroomCapsulePrice5", "mushroomCapsuleWeight5",
            "goldenMushroomCapsulePrice5", "goldenMushroomCapsuleWeight5",
            "cursedMushroomCapsulePrice5", "cursedMushroomCapsuleWeight5",
            "flutterCapsulePrice5", "flutterCapsuleWeight5",
            "spinyCapsulePrice5", "spinyCapsuleWeight5",
            "goombaCapsuleWeight5", "goombaCapsulePrice5",
            "plantCapsulePrice5", "plantCapsuleWeight5",
            "kleptoCapsuleWeight5", "kleptoCapsulePrice5",
            "kamekCapsuleWeight5", "kamekCapsulePrice5",
            "magiKoopaCapsuleWeight5", "magiKoopaCapsulePrice5",
            "blizzardCapsuleWeight5", "blizzardCapsulePrice5",
            "podobooCapsulePrice5", "podobooCapsuleWeight5",
            "paraTroopaCapsuleWeight5", "paraTroopaCapsulePrice5",
            "ukikiCapsulePrice5", "ukikiCapsuleWeight5",
            "tweesterCapsulePrice5", "tweesterCapsuleWeight5",
            "lakituCapsulePrice5", "lakituCapsuleWeight5",
            "warpPipeCapsulePrice5", "warpPipeCapsuleWeight5",
            "miracleCapsulePrice5", "miracleCapsuleWeight5",
            "boneCapsulePrice5", "boneCapsuleWeight5",
            "chanceCapsulePrice5", "chanceCapsuleWeight5",
            "chainChompCapsulePrice5", "chainChompCapsuleWeight5",
            "bowserCapsulePrice5", "bowserCapsuleWeight5",
            "dkCapsulePrice5", "dkCapsuleWeight5",
        ]

        args = [EntryProxy(self.inputs[name]) for name in arg_order]
        try:
            itemsEvent_mp5(*args)
        except Exception as e:
            from qfluentwidgets import InfoBar, InfoBarPosition
            InfoBar.error(title="Error", content=str(e), orient=Qt.Horizontal, isClosable=True, position=InfoBarPosition.TOP, duration=3000, parent=self)


