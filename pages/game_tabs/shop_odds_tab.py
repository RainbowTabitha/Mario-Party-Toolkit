#!/usr/bin/env python3
# ============================================
# Shop Odds Tab Component for Mario Party 4
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QScrollArea, QFrame, QGroupBox, QPushButton, QMessageBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from qfluentwidgets import SubtitleLabel, BodyLabel, LineEdit, PushButton

# Import resource manager for images
from utils.resource_manager import ResourceManager

# Import shop odds event functions for MP4
try:
    from events.marioParty4_items2 import itemsEvent_mp4ShopOdds, itemsEvent_mp4ShopOddsDX
except ImportError:
    pass


class ShopOddsTab(QWidget):
    def __init__(self, game_id, game_type="mp4"):
        super().__init__()
        self.game_id = game_id
        self.game_type = game_type  # "mp4" or "mp4dx"
        # Consistent column sizing for alignment
        self.icon_width = 32
        self.name_col_width = 140
        self.input_width = 60
        self.setup_ui()

    def setup_ui(self):
        """Set up the shop odds tab UI"""
        self.setObjectName(f"{self.game_id}ShopOddsTab")

        # Main layout
        layout = QVBoxLayout()
        layout.setSpacing(8)
        layout.setContentsMargins(16, 12, 16, 12)

        # Title
        title = SubtitleLabel("Item Shop Odds Modifications")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Description
        desc = BodyLabel("Modify odds for items appearing in the shop at different game stages:")
        desc.setAlignment(Qt.AlignCenter)
        layout.addWidget(desc)

        # Scrollable area for the form
        scroll_area = QScrollArea()
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)

        # Container widget for scroll area
        self.scroll_widget = QWidget()
        scroll_layout = QVBoxLayout(self.scroll_widget)
        scroll_layout.setSpacing(16)

        # Game version selection
        version_layout = QHBoxLayout()
        version_layout.addWidget(BodyLabel("Game Version:"))
        self.mp4_radio = QPushButton("Mario Party 4")
        self.mp4dx_radio = QPushButton("Mario Party 4 Deluxe")
        self.mp4_radio.setCheckable(True)
        self.mp4dx_radio.setCheckable(True)
        self.mp4_radio.setChecked(self.game_type == "mp4")
        self.mp4dx_radio.setChecked(self.game_type == "mp4dx")
        self.mp4_radio.clicked.connect(lambda: self.set_game_version("mp4"))
        self.mp4dx_radio.clicked.connect(lambda: self.set_game_version("mp4dx"))
        version_layout.addWidget(self.mp4_radio)
        version_layout.addWidget(self.mp4dx_radio)
        version_layout.addStretch()
        scroll_layout.addLayout(version_layout)

        # Create dynamic content container for items
        dynamic_container = self.create_dynamic_content_container()
        scroll_layout.addWidget(dynamic_container)

        # Set scroll widget and add to layout
        scroll_area.setWidget(self.scroll_widget)
        layout.addWidget(scroll_area)

        # Generate button
        generate_btn = PushButton("Generate Codes")
        generate_btn.clicked.connect(self.generate_codes)
        layout.addWidget(generate_btn)

        self.setLayout(layout)

    def set_game_version(self, version):
        """Set the game version (mp4 or mp4dx)"""
        self.game_type = version
        if version == "mp4":
            self.mp4_radio.setChecked(True)
            self.mp4dx_radio.setChecked(False)
        else:
            self.mp4_radio.setChecked(False)
            self.mp4dx_radio.setChecked(True)

        # Update the displayed items based on the new game version
        self.update_items_ui(self.scroll_widget.layout())

    def clear_item_rows(self, scroll_layout):
        """Clear all items by removing the dynamic content container"""
        # Find and remove the dynamic content container
        for i in range(scroll_layout.count()):
            item = scroll_layout.itemAt(i)
            if item and item.widget():
                widget = item.widget()
                # Look for our dynamic content container (QWidget with object name)
                if hasattr(widget, 'objectName') and widget.objectName() == 'dynamic_content_container':
                    scroll_layout.removeWidget(widget)
                    widget.deleteLater()
                    break

    def update_items_ui(self, scroll_layout):
        """Update the items UI based on current game version"""
        # Clear existing dynamic content
        self.clear_item_rows(scroll_layout)

        # Create new dynamic content container
        dynamic_container = self.create_dynamic_content_container()
        scroll_layout.addWidget(dynamic_container)

    def create_dynamic_content_container(self):
        """Create a container widget for dynamic content"""
        container = QWidget()
        container.setObjectName('dynamic_content_container')
        container_layout = QVBoxLayout(container)
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(8)

        # Create all items list based on current game version
        if self.game_type == "mp4":
            # MP4 items only
            all_items = [
                ("Mini Mushroom", "assets/items/miniMushroom.png"),
                ("Mega Mushroom", "assets/items/megaMushroom.png"),
                ("Super Mini Mushroom", "assets/items/superMiniMushroom.png"),
                ("Super Mega Mushroom", "assets/items/superMegaMushroom.png"),
                ("Mini Mega Hammer", "assets/items/miniMegaHammer.png"),
                ("Warp Pipe", "assets/items/warpPipe.png"),
                ("Swap Card", "assets/items/swapCard.png"),
                ("Sparky Sticker", "assets/items/sparkySticker.png"),
                ("Gaddlight", "assets/items/gaddlight.png"),
                ("Chomp Call", "assets/items/chompCall.png"),
                ("Bowser Suit", "assets/items/bowserSuit4.png"),
                ("Crystal Ball", "assets/items/crystalBall.png"),
                ("Magic Lamp", "assets/items/magicLamp.png"),
                ("Item Bag", "assets/items/itemBag4.png"),
            ]
        else:
            # MP4DX items (includes all MP4 items plus additional ones)
            all_items = [
                ("Mini Mushroom", "assets/items/miniMushroom.png"),
                ("Mega Mushroom", "assets/items/megaMushroom.png"),
                ("Super Mini Mushroom", "assets/items/superMiniMushroom.png"),
                ("Super Mega Mushroom", "assets/items/superMegaMushroom.png"),
                ("Mushroom", "assets/items/mushroom.png"),
                ("Golden Mushroom", "assets/items/goldenMushroom.png"),
                ("Reverse Mushroom", "assets/items/reverseMushroom.png"),
                ("Poison Mushroom", "assets/items/poisonMushroom.png"),
                ("Triple Poison Mushroom", "assets/items/triplePoisonMushroom.png"),
                ("Mini Mega Hammer", "assets/items/miniMegaHammer.png"),
                ("Warp Pipe", "assets/items/warpPipe.png"),
                ("Swap Card", "assets/items/swapCard.png"),
                ("Sparky Sticker", "assets/items/sparkySticker.png"),
                ("Gaddlight", "assets/items/gaddlight.png"),
                ("Chomp Call", "assets/items/chompCall.png"),
                ("Bowser Suit", "assets/items/bowserSuit4.png"),
                ("Crystal Ball", "assets/items/crystalBall.png"),
                ("Magic Lamp", "assets/items/magicLamp.png"),
                ("Item Bag", "assets/items/itemBag4.png"),
                ("Cellular Shopper", "assets/items/celluarShopper.png"),
                ("Skeleton Key", "assets/items/skeletonKey.png"),
                ("Plunder Chest", "assets/items/plunderChest.png"),
                ("Gaddbrush", "assets/items/gaddbrush.png"),
                ("Warp Block", "assets/items/warpBlock.png"),
                ("Fly Guy", "assets/items/flyGuy.png"),
                ("Plus Block", "assets/items/plusBlock.png"),
                ("Minus Block", "assets/items/minusBlock.png"),
                ("Speed Block", "assets/items/speedBlock.png"),
                ("Slow Block", "assets/items/slowBlock.png"),
                ("Bowser Phone", "assets/items/bowserPhone.png"),
                ("Double Dip", "assets/items/doubleDip.png"),
                ("Hidden Block Card", "assets/items/hiddenBlockCard.png"),
                ("Barter Box", "assets/items/barterBox.png"),
                ("Super Warp Pipe", "assets/items/superWarpPipe.png"),
                ("Chance Time Charm", "assets/items/chanceTimeCharm.png"),
                ("Wacky Watch", "assets/items/wackyWatch.png"),
            ]

        # Create header with column labels
        self.create_column_header(container_layout)

        # Create all items without categories
        for item_name, item_icon in all_items:
            self.create_item_row(container_layout, item_name, item_icon)

        # Add some bottom spacing to avoid overlap with the Generate button
        spacer = QFrame()
        spacer.setFixedHeight(12)
        spacer.setFrameShape(QFrame.NoFrame)
        container_layout.addWidget(spacer)

        return container

    def create_column_header(self, parent_layout):
        """Create column header with clear labels"""
        header_layout = QHBoxLayout()
        header_layout.setSpacing(12)
        header_layout.setContentsMargins(10, 5, 10, 5)

        # Empty space for icon
        icon_placeholder = QLabel("")
        icon_placeholder.setFixedWidth(self.icon_width)
        header_layout.addWidget(icon_placeholder)

        # Item name column
        item_header = BodyLabel("Item")
        item_header.setStyleSheet(f"font-size: 14px; font-weight: 700; min-width: {self.name_col_width}px;")
        header_layout.addWidget(item_header)

        # Odds columns for different stages and player counts
        stages = ["Early Game", "Mid Game", "Late Game"]
        player_counts = ["1 Player", "2 Players", "3-4 Players"]

        for stage in stages:
            for player_count in player_counts:
                col_label = BodyLabel(f"{stage}\n{player_count}")
                col_label.setStyleSheet(f"font-size: 12px; font-weight: 600; text-align: center; min-width: {self.input_width}px;")
                col_label.setAlignment(Qt.AlignCenter)
                header_layout.addWidget(col_label)

        header_layout.addStretch()
        parent_layout.addLayout(header_layout)

        # Add a separator line
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setStyleSheet("color: #cccccc;")
        parent_layout.addWidget(separator)

    def create_item_row(self, parent_layout, item_name, item_icon):
        """Create a single row for an item"""
        item_layout = QHBoxLayout()
        item_layout.setSpacing(12)
        item_layout.setContentsMargins(10, 5, 10, 5)

        # Item icon
        icon_label = self.create_image_label(item_icon, self.icon_width, self.icon_width)
        item_layout.addWidget(icon_label)

        # Item name
        name_label = BodyLabel(item_name)
        name_label.setStyleSheet(f"font-size: 14px; font-weight: 600; min-width: {self.name_col_width}px;")
        item_layout.addWidget(name_label)

        # Odds inputs for different stages
        stages = ["Early", "Mid", "Late"]
        item_key = item_name.lower().replace(" ", "_")
        self.create_odds_inputs(item_layout, item_key, stages)

        item_layout.addStretch()
        parent_layout.addLayout(item_layout)

    def create_odds_inputs(self, layout, item_key, stages):
        """Create odds input fields for different game stages"""
        for stage in stages:
            # Create inputs for player counts (1, 2, 3-4 players)
            for player_count in ["1", "2", "34"]:
                entry = LineEdit()
                # Leave fields blank - users can fill in custom values
                entry.setFixedWidth(self.input_width)
                entry.setObjectName(f"{item_key}_{stage.lower()}_{player_count}")
                layout.addWidget(entry)

                # Store reference for later access
                setattr(self, f"{item_key}_{stage.lower()}_{player_count}_entry", entry)

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
        """Generate codes for the current game version"""
        try:
            # Collect all item odds
            item_odds = self.collect_item_odds()

            if self.game_type == "mp4dx":
                if 'itemsEvent_mp4ShopOddsDX' in globals():
                    # Call MP4DX function with collected parameters
                    itemsEvent_mp4ShopOddsDX(**item_odds)
                else:
                    self.show_error("Mario Party 4 Deluxe shop odds modification not available")
            else:
                if 'itemsEvent_mp4ShopOdds' in globals():
                    # Call MP4 function with collected parameters
                    itemsEvent_mp4ShopOdds(**item_odds)
                else:
                    self.show_error("Mario Party 4 shop odds modification not available")

        except Exception as e:
            self.show_error(f"Error generating codes: {str(e)}")

    def collect_item_odds(self):
        """Collect all item odds from the form"""
        odds = {}

        # Get the appropriate item list based on game type
        if self.game_type == "mp4":
            # MP4 items only
            item_list = [
                "mini_mushroom", "mega_mushroom", "super_mini_mushroom", "super_mega_mushroom",
                "mini_mega_hammer", "warp_pipe", "swap_card", "sparky_sticker",
                "gaddlight", "chomp_call", "bowser_suit", "crystal_ball",
                "magic_lamp", "item_bag", "bowser_phone", "double_dip",
                "hidden_block_card", "barter_box", "plus_block", "minus_block",
                "speed_block", "slow_block"
            ]
        else:
            # MP4DX items (includes all MP4 items plus additional ones)
            item_list = [
                "mini_mushroom", "mega_mushroom", "super_mini_mushroom", "super_mega_mushroom",
                "mushroom", "golden_mushroom", "reverse_mushroom", "poison_mushroom",
                "triple_poison_mushroom", "mini_mega_hammer", "warp_pipe", "swap_card",
                "sparky_sticker", "gaddlight", "chomp_call", "bowser_suit",
                "crystal_ball", "magic_lamp", "item_bag", "celluar_shopper",
                "skeleton_key", "plunder_chest", "gaddbrush", "warp_block",
                "fly_guy", "plus_block", "minus_block", "speed_block",
                "slow_block", "bowser_phone", "double_dip", "hidden_block_card",
                "barter_box", "super_warp_pipe", "chance_time_charm", "wacky_watch"
            ]

        # Define camelCase parameter name mapping
        item_mapping = {
            "mini_mushroom": "miniMushroom",
            "mega_mushroom": "megaMushroom",
            "super_mini_mushroom": "superMiniMushroom",
            "super_mega_mushroom": "superMegaMushroom",
            "mushroom": "mushroom",
            "golden_mushroom": "goldenMushroom",
            "reverse_mushroom": "reverseMushroom",
            "poison_mushroom": "poisonMushroom",
            "triple_poison_mushroom": "triplePoisonMushroom",
            "mini_mega_hammer": "miniMegaHammer",
            "warp_pipe": "warpPipe",
            "swap_card": "swapCard",
            "sparky_sticker": "sparkySticker",
            "gaddlight": "gaddlight",
            "chomp_call": "chompCall",
            "bowser_suit": "bowserSuit",
            "crystal_ball": "crystalBall",
            "magic_lamp": "magicLamp",
            "item_bag": "itemBag",
            "celluar_shopper": "celluarShopper",
            "skeleton_key": "skeletonKey",
            "plunder_chest": "plunderChest",
            "gaddbrush": "gaddbrush",
            "warp_block": "warpBlock",
            "fly_guy": "flyGuy",
            "plus_block": "plusBlock",
            "minus_block": "minusBlock",
            "speed_block": "speedBlock",
            "slow_block": "slowBlock",
            "bowser_phone": "bowserPhone",
            "double_dip": "doubleDip",
            "hidden_block_card": "hiddenBlockCard",
            "barter_box": "barterBox",
            "super_warp_pipe": "superWarpPipe",
            "chance_time_charm": "chanceTimeCharm",
            "wacky_watch": "wackyWatch"
        }

        stages = ["early", "mid", "late"]
        player_counts = ["1", "2", "34"]

        for item_key in item_list:
            if item_key in item_mapping:
                camel_case_name = item_mapping[item_key]
                for stage in stages:
                    for player_count in player_counts:
                        entry_name = f"{item_key}_{stage}_{player_count}_entry"
                        if hasattr(self, entry_name):
                            entry = getattr(self, entry_name)
                            param_name = f"{camel_case_name}{stage.capitalize()}Odds{player_count}"
                            odds[param_name] = entry.text()

        return odds

    def show_error(self, message):
        """Show error message to user"""
        QMessageBox.critical(self, "Error", message)

    def themeChanged(self):
        """Called when theme changes - update all styling"""
        from qfluentwidgets import isDarkTheme

        # Update radio button styling
        if isDarkTheme():
            # Dark theme styling
            radio_style = """
                QPushButton {
                    background: #3c3c3c;
                    border: 1px solid #555555;
                    border-radius: 4px;
                    padding: 6px 12px;
                    color: #ffffff;
                    font-weight: 500;
                }
                QPushButton:checked {
                    background: #0078d4;
                    border: 1px solid #0078d4;
                    color: #ffffff;
                }
                QPushButton:hover {
                    background: #4c4c4c;
                    border: 1px solid #666666;
                }
                QPushButton:checked:hover {
                    background: #106ebe;
                    border: 1px solid #106ebe;
                }
            """
        else:
            # Light theme styling
            radio_style = """
                QPushButton {
                    background: #ffffff;
                    border: 1px solid #cccccc;
                    border-radius: 4px;
                    padding: 6px 12px;
                    color: #333333;
                    font-weight: 500;
                }
                QPushButton:checked {
                    background: #0078d4;
                    border: 1px solid #0078d4;
                    color: #ffffff;
                }
                QPushButton:hover {
                    background: #f5f5f5;
                    border: 1px solid #999999;
                }
                QPushButton:checked:hover {
                    background: #106ebe;
                    border: 1px solid #106ebe;
                }
            """

        self.mp4_radio.setStyleSheet(radio_style)
        self.mp4dx_radio.setStyleSheet(radio_style)
