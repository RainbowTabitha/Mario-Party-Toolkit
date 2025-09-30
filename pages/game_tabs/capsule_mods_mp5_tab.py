# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

# ============================================
# Capsule Mods Tab Component for Mario Party 5
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QScrollArea, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from qfluentwidgets import SubtitleLabel, BodyLabel, LineEdit, PushButton, CardWidget, ScrollArea

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
        """Set up the capsule mods MP5 tab UI"""
        self.setObjectName(f"{self.game_id}CapsuleModsTab")
        
        # Set transparent background
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setStyleSheet("QWidget#marioParty5CapsuleModsTab { background: transparent; }")

        layout = QVBoxLayout()
        layout.setSpacing(8)
        layout.setContentsMargins(16, 12, 16, 12)

        title = SubtitleLabel("Capsule Modifications")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        desc = BodyLabel("Modify capsule prices and distribution weights:")
        desc.setAlignment(Qt.AlignCenter)
        layout.addWidget(desc)

        # Create scroll area for the capsule interface
        scroll_area = ScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setStyleSheet("ScrollArea { background: transparent; border: none; }")

        # Container widget for scroll area content
        container = QWidget()
        container.setStyleSheet("QWidget { background: transparent; }")
        container_layout = QVBoxLayout(container)
        container_layout.setContentsMargins(20, 16, 20, 16)
        container_layout.setSpacing(16)

        # Create capsule modifications card
        capsule_card = CardWidget()
        capsule_card.setStyleSheet("CardWidget { background: rgba(255, 255, 255, 0.1); border: 1px solid rgba(255, 255, 255, 0.2); }")
        capsule_card_layout = QVBoxLayout(capsule_card)
        capsule_card_layout.setContentsMargins(20, 16, 20, 16)
        capsule_card_layout.setSpacing(16)

        # Add title to the card
        card_title = SubtitleLabel("Capsule Modifications")
        card_title.setStyleSheet("font-size: 16px; font-weight: 600; margin-bottom: 8px;")
        capsule_card_layout.addWidget(card_title)

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

        # Create grid layout for capsule entries
        capsule_grid = QVBoxLayout()
        capsule_grid.setSpacing(12)

        # Build individual cards for each capsule
        def create_capsule_group(display: str, icon_path: str, price_key: str, weight_key: str):
            group_card = CardWidget()
            group_card.setStyleSheet("CardWidget { background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); }")
            group_layout = QVBoxLayout(group_card)
            group_layout.setContentsMargins(16, 12, 16, 12)
            group_layout.setSpacing(8)

            # Capsule title
            title = BodyLabel(display)
            title.setStyleSheet("font-size: 14px; font-weight: 600; margin-bottom: 4px;")
            group_layout.addWidget(title)

            # Parameters layout
            params_layout = QHBoxLayout()
            params_layout.setSpacing(16)

            # Add capsule icon
            icon = self.create_image_label(icon_path, 32, 32)
            params_layout.addWidget(icon)

            # Price section
            price_layout = QVBoxLayout()
            price_layout.setSpacing(4)

            price_label = BodyLabel("Price:")
            price_label.setStyleSheet("font-size: 12px; font-weight: 600;")
            price_layout.addWidget(price_label)

            price_entry = LineEdit()
            price_entry.setPlaceholderText("Price")
            price_entry.setFixedWidth(70)
            price_entry.setFixedHeight(30)
            price_layout.addWidget(price_entry)
            self.inputs[price_key] = price_entry

            params_layout.addLayout(price_layout)

            # Weight section
            weight_layout = QVBoxLayout()
            weight_layout.setSpacing(4)

            weight_label = BodyLabel("Weight:")
            weight_label.setStyleSheet("font-size: 12px; font-weight: 600;")
            weight_layout.addWidget(weight_label)

            weight_entry = LineEdit()
            weight_entry.setPlaceholderText("Weight")
            weight_entry.setFixedWidth(70)
            weight_entry.setFixedHeight(30)
            weight_layout.addWidget(weight_entry)
            self.inputs[weight_key] = weight_entry

            params_layout.addLayout(weight_layout)

            group_layout.addLayout(params_layout)
            return group_card

        for label, icon, price_key, weight_key in rows:
            capsule_group = create_capsule_group(label, icon, price_key, weight_key)
            capsule_grid.addWidget(capsule_group)

        capsule_card_layout.addLayout(capsule_grid)
        container_layout.addWidget(capsule_card)
        scroll_area.setWidget(container)
        layout.addWidget(scroll_area)

        generate_btn = PushButton("Generate Codes")
        generate_btn.clicked.connect(self.generate_codes)
        layout.addWidget(generate_btn)

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
                # Convert string to int, default to 0 if invalid
                try:
                    return int(self._le.text()) if self._le.text() else 0
                except (ValueError, TypeError):
                    return 0

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


