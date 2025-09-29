#!/usr/bin/env python3
# ============================================
# Items MP7 Tab Component for Mario Party 7
# Full orb modifications with all standard items
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QScrollArea, QFrame
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from qfluentwidgets import SubtitleLabel, BodyLabel, LineEdit, PushButton, ScrollArea, CardWidget

# Import resource manager for images
from utils.resource_manager import ResourceManager

# Import items event function for MP7
try:
    from events.marioParty7_items import itemsEvent_mp7
except ImportError:
    pass


class ItemsMP7Tab(QWidget):
    def __init__(self, game_id):
        super().__init__()
        self.game_id = game_id
        self.setup_ui()

    def setup_ui(self):
        """Set up the items MP7 tab UI"""
        self.setObjectName(f"{self.game_id}ItemsMP7Tab")
        
        # Set transparent background
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setStyleSheet("QWidget#marioParty7ItemsMP7Tab { background: transparent; }")

        # Main layout
        layout = QVBoxLayout()
        layout.setSpacing(8)
        layout.setContentsMargins(16, 12, 16, 12)

        # Title
        title = SubtitleLabel("Orb Modifications")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Description
        desc = BodyLabel("Modify orb costs, shop odds, and space odds:")
        desc.setAlignment(Qt.AlignCenter)
        layout.addWidget(desc)

        # Create scroll area for the complex orb interface
        scroll_area = ScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setStyleSheet("QScrollArea { background: transparent; border: none; }")

        # Container widget for scroll area content
        container = QWidget()
        container.setStyleSheet("QWidget { background: transparent; }")
        container_layout = QVBoxLayout(container)
        container_layout.setContentsMargins(20, 16, 20, 16)
        container_layout.setSpacing(16)

        # Create orb modifications card
        orb_card = CardWidget()
        orb_card.setStyleSheet("CardWidget { background: rgba(255, 255, 255, 0.1); border: 1px solid rgba(255, 255, 255, 0.2); }")
        orb_card_layout = QVBoxLayout(orb_card)
        orb_card_layout.setContentsMargins(20, 16, 20, 16)
        orb_card_layout.setSpacing(16)

        # Add title to the card
        card_title = SubtitleLabel("Orb Modifications")
        card_title.setStyleSheet("font-size: 16px; font-weight: 600; margin-bottom: 8px;")
        orb_card_layout.addWidget(card_title)

        # Create grid layout for orb entries
        orb_grid = QVBoxLayout()
        orb_grid.setSpacing(12)

        # Define all the items with their parameters
        self.items = [
            ("Mushroom", "assets/items/mushroomCapsule.png", "mushroom"),
            ("Golden Mushroom", "assets/items/goldenMushroomCapsule.png", "goldenMushroom"),
            ("Slow Mushroom", "assets/items/slowMushroomCapsule.png", "slowMushroom"),
            ("Metal Mushroom", "assets/items/metalMushroomCapsule.png", "metalMushroom"),
            ("Flutter", "assets/items/wigglerCapsule.png", "flutter"),
            ("Cannon", "assets/items/cannonCapsule.png", "cannon"),
            ("Snack", "assets/items/snackCapsule.png", "snack"),
            ("Lakitu", "assets/items/lakituCapsule.png", "lakitu"),
            ("Hammer Bro", "assets/items/hammerBroCapsule.png", "hammerBro"),
            ("Piranha Plant", "assets/items/plantCapsule.png", "piranhaPlant"),
            ("Spear Guy", "assets/items/spearCapsule.png", "spearGuy"),
            ("Kamek", "assets/items/kamekCapsule.png", "kamek"),
            ("Toady", "assets/items/toadyCapsule.png", "toady"),
            ("Mr. Blizzard", "assets/items/blizzardCapsule.png", "mrBlizzard"),
            ("Bandit", "assets/items/banditCapsule.png", "bandit"),
            ("Pink Boo", "assets/items/pinkBooCapsule.png", "pinkBoo"),
            ("Spiny", "assets/items/spinyCapsule.png", "spiny"),
            ("Zap", "assets/items/zapCapsule.png", "zap"),
            ("Tweester", "assets/items/tweesterCapsule.png", "tweester"),
            ("Thwomp", "assets/items/thwompCapsule.png", "thwomp"),
            ("Warp Pipe", "assets/items/warpCapsule.png", "warp"),
            ("Bob-omb", "assets/items/bombCapsule.png", "bomb"),
            ("Fireball", "assets/items/fireballCapsule.png", "fireball"),
            ("Flower", "assets/items/flowerCapsule.png", "flower"),
            ("Egg", "assets/items/eggCapsule.png", "egg"),
            ("Vacuum", "assets/items/vacuumCapsule.png", "vacuum"),
            ("Magic", "assets/items/magicCapsule.png", "magic"),
            ("Triple Mushroom", "assets/items/tripleCapsule.png", "triple"),
            ("Koopa Kid", "assets/items/koopaCapsule.png", "koopa")
        ]

        # Create entries for each item
        for item_name, icon_path, item_key in self.items:
            item_group = self.create_item_group(item_name, icon_path, item_key)
            orb_grid.addWidget(item_group)

        orb_card_layout.addLayout(orb_grid)
        container_layout.addWidget(orb_card)

        # Set the container as the scroll area's widget
        scroll_area.setWidget(container)
        layout.addWidget(scroll_area)

        # Generate button
        generate_btn = PushButton("Generate Codes")
        generate_btn.clicked.connect(self.generate_codes)
        layout.addWidget(generate_btn)

        self.setLayout(layout)

    def create_item_group(self, item_name, icon_path, item_key):
        """Create a group for a single item with all its parameters"""
        group_card = CardWidget()
        group_card.setStyleSheet("CardWidget { background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); }")
        group_layout = QVBoxLayout(group_card)
        group_layout.setContentsMargins(16, 12, 16, 12)
        group_layout.setSpacing(8)

        # Item title
        title = BodyLabel(item_name)
        title.setStyleSheet("font-size: 14px; font-weight: 600; margin-bottom: 4px;")
        group_layout.addWidget(title)

        # Create grid for parameters
        params_layout = QHBoxLayout()
        params_layout.setSpacing(8)

        # Add item icon
        icon = self.create_image_label(icon_path, 32, 32)
        params_layout.addWidget(icon)

        # Price parameters
        price_layout = QVBoxLayout()
        price_layout.setSpacing(4)

        price_label = BodyLabel("Prices:")
        price_label.setStyleSheet("font-size: 12px; font-weight: 600;")
        price_layout.addWidget(price_label)

        price_row = QHBoxLayout()
        price_row.setSpacing(4)

        # Price entries
        price1_entry = LineEdit()
        price1_entry.setPlaceholderText("1st")
        price1_entry.setFixedWidth(70)
        price1_entry.setFixedHeight(30)
        price_row.addWidget(price1_entry)
        setattr(self, f"{item_key}_price1", price1_entry)

        price2_entry = LineEdit()
        price2_entry.setPlaceholderText("2nd")
        price2_entry.setFixedWidth(70)
        price2_entry.setFixedHeight(30)
        price_row.addWidget(price2_entry)
        setattr(self, f"{item_key}_price2", price2_entry)

        price34_entry = LineEdit()
        price34_entry.setPlaceholderText("3rd/4th")
        price34_entry.setFixedWidth(70)
        price34_entry.setFixedHeight(30)
        price_row.addWidget(price34_entry)
        setattr(self, f"{item_key}_price34", price34_entry)

        price_layout.addLayout(price_row)
        params_layout.addLayout(price_layout)

        # Shop odds parameters
        shop_layout = QVBoxLayout()
        shop_layout.setSpacing(4)

        shop_label = BodyLabel("Shop Odds:")
        shop_label.setStyleSheet("font-size: 12px; font-weight: 600;")
        shop_layout.addWidget(shop_label)

        shop_row = QHBoxLayout()
        shop_row.setSpacing(4)

        shop12_entry = LineEdit()
        shop12_entry.setPlaceholderText("Early")
        shop12_entry.setFixedWidth(70)
        shop12_entry.setFixedHeight(30)
        shop_row.addWidget(shop12_entry)
        setattr(self, f"{item_key}_shop12", shop12_entry)

        shop34_entry = LineEdit()
        shop34_entry.setPlaceholderText("Late")
        shop34_entry.setFixedWidth(70)
        shop34_entry.setFixedHeight(30)
        shop_row.addWidget(shop34_entry)
        setattr(self, f"{item_key}_shop34", shop34_entry)

        shop_layout.addLayout(shop_row)
        params_layout.addLayout(shop_layout)

        # Space odds parameters
        space_layout = QVBoxLayout()
        space_layout.setSpacing(4)

        space_label = BodyLabel("Space Odds:")
        space_label.setStyleSheet("font-size: 12px; font-weight: 600;")
        space_layout.addWidget(space_label)

        space_row = QHBoxLayout()
        space_row.setSpacing(4)

        space1_entry = LineEdit()
        space1_entry.setPlaceholderText("1st")
        space1_entry.setFixedWidth(70)
        space1_entry.setFixedHeight(30)
        space_row.addWidget(space1_entry)
        setattr(self, f"{item_key}_space1", space1_entry)

        space2_entry = LineEdit()
        space2_entry.setPlaceholderText("2nd")
        space2_entry.setFixedWidth(70)
        space2_entry.setFixedHeight(30)
        space_row.addWidget(space2_entry)
        setattr(self, f"{item_key}_space2", space2_entry)

        space34_entry = LineEdit()
        space34_entry.setPlaceholderText("3rd/4th")
        space34_entry.setFixedWidth(70)
        space34_entry.setFixedHeight(30)
        space_row.addWidget(space34_entry)
        setattr(self, f"{item_key}_space34", space34_entry)

        space_layout.addLayout(space_row)
        params_layout.addLayout(space_layout)

        group_layout.addLayout(params_layout)
        return group_card

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
        """Generate codes for orb modifications"""
        try:
            if 'itemsEvent_mp7' in globals():
                # Create mock entry objects for all parameters
                class MockEntry:
                    def __init__(self, value):
                        # Convert string to int, default to 0 if invalid
                        try:
                            self._value = int(value) if value else 0
                        except (ValueError, TypeError):
                            self._value = 0
                    def get(self):
                        return self._value

                # Get all the parameters in the correct order
                params = []
                
                # Mushroom parameters
                params.extend([
                    MockEntry(getattr(self, 'mushroom_shop12', None).text() if getattr(self, 'mushroom_shop12', None) else "0"),
                    MockEntry(getattr(self, 'mushroom_shop34', None).text() if getattr(self, 'mushroom_shop34', None) else "0"),
                    MockEntry(getattr(self, 'mushroom_space1', None).text() if getattr(self, 'mushroom_space1', None) else "0"),
                    MockEntry(getattr(self, 'mushroom_space2', None).text() if getattr(self, 'mushroom_space2', None) else "0"),
                    MockEntry(getattr(self, 'mushroom_space34', None).text() if getattr(self, 'mushroom_space34', None) else "0"),
                ])
                
                # Golden Mushroom parameters
                params.extend([
                    MockEntry(getattr(self, 'goldenMushroom_price1', MockEntry("0")).text()),
                    MockEntry(getattr(self, 'goldenMushroom_price2', MockEntry("0")).text()),
                    MockEntry(getattr(self, 'goldenMushroom_price34', MockEntry("0")).text()),
                    MockEntry(getattr(self, 'goldenMushroom_shop12', MockEntry("0")).text()),
                    MockEntry(getattr(self, 'goldenMushroom_shop34', MockEntry("0")).text()),
                    MockEntry(getattr(self, 'goldenMushroom_space1', MockEntry("0")).text()),
                    MockEntry(getattr(self, 'goldenMushroom_space2', MockEntry("0")).text()),
                    MockEntry(getattr(self, 'goldenMushroom_space34', MockEntry("0")).text()),
                ])
                
                # Continue with all other items...
                # For brevity, I'll add the most important ones
                for item_name, _, item_key in self.items[2:]:  # Skip mushroom and golden mushroom
                    params.extend([
                        MockEntry(getattr(self, f'{item_key}_price1', MockEntry("0")).text()),
                        MockEntry(getattr(self, f'{item_key}_price2', MockEntry("0")).text()),
                        MockEntry(getattr(self, f'{item_key}_price34', MockEntry("0")).text()),
                        MockEntry(getattr(self, f'{item_key}_shop12', MockEntry("0")).text()),
                        MockEntry(getattr(self, f'{item_key}_shop34', MockEntry("0")).text()),
                        MockEntry(getattr(self, f'{item_key}_space1', MockEntry("0")).text()),
                        MockEntry(getattr(self, f'{item_key}_space2', MockEntry("0")).text()),
                        MockEntry(getattr(self, f'{item_key}_space34', MockEntry("0")).text()),
                    ])

                # Call the event function with all parameters
                itemsEvent_mp7(*params)
            else:
                self.show_error("Mario Party 7 items modification not available")

        except Exception as e:
            self.show_error(f"Error generating codes: {str(e)}")

    def show_error(self, message):
        """Show error message to user"""
        QMessageBox.critical(self, "Error", message)
