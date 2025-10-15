# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

# ============================================
# Shop Prices Tab Component for Mario Party 4
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy, QLabel, QLineEdit, QScrollArea, QFrame, QGroupBox, QPushButton, QMessageBox, QRadioButton, QButtonGroup
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from qfluentwidgets import SubtitleLabel, BodyLabel, LineEdit, PushButton, CardWidget, ScrollArea

# Import resource manager for images
from utils.resource_manager import ResourceManager

# Import shop price event functions for MP4
try:
    from events.marioParty4_items import itemsEvent_mp4ShopPrices, itemsEvent_mp4ShopDXPrices
except ImportError:
    pass


class ShopPricesTab(QWidget):
    def __init__(self, game_id, game_type="mp4"):
        super().__init__()
        self.game_id = game_id
        self.game_type = game_type  # "mp4" or "mp4dx"
        # Consistent column sizing for alignment
        self.icon_width = 32
        self.name_col_width = 140
        self.input_width = 60

        # Use dictionary to store widget references instead of dynamic attributes
        self.price_entries = {}

        self.setup_ui()

    def setup_ui(self):
        """Set up the shop prices tab UI"""
        self.setObjectName(f"{self.game_id}ShopPricesTab")
        
        # Set transparent background
        self.setAttribute(Qt.WA_TranslucentBackground, True)
        self.setStyleSheet("QWidget#marioParty4ShopPricesTab { background: transparent; }")

        # Main layout
        layout = QVBoxLayout()
        layout.setSpacing(8)
        layout.setContentsMargins(16, 12, 16, 12)

        # Title
        title = SubtitleLabel("Item Shop Price Modifications")
        title.setAlignment(Qt.AlignCenter)
        self.apply_label_theme(title, "")
        layout.addWidget(title)

        # Description
        desc = BodyLabel("Modify prices for items in the shop at different game stages:")
        desc.setAlignment(Qt.AlignCenter)
        self.apply_label_theme(desc, "")
        layout.addWidget(desc)

        # Create scroll area for the shop interface
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

        # Create shop modifications card
        shop_card = CardWidget()
        shop_card.setStyleSheet("CardWidget { background: rgba(255, 255, 255, 0.1); border: 1px solid rgba(255, 255, 255, 0.2); }")
        shop_card_layout = QVBoxLayout(shop_card)
        shop_card_layout.setContentsMargins(20, 16, 20, 16)
        shop_card_layout.setSpacing(16)

        # Add title to the card
        card_title = SubtitleLabel("Item Shop Prices")
        self.apply_label_theme(card_title, "font-size: 16px; font-weight: 600; margin-bottom: 8px;")
        shop_card_layout.addWidget(card_title)

        # Game version selection
        version_layout = QHBoxLayout()
        version_label = BodyLabel("Game Version:")
        self.apply_label_theme(version_label, "")
        version_layout.addWidget(version_label)

        # Create radio button group
        self.version_button_group = QButtonGroup()

        self.mp4_radio = QRadioButton("Mario Party 4")
        self.mp4dx_radio = QRadioButton("Mario Party 4 Deluxe")

        self.version_button_group.addButton(self.mp4_radio)
        self.version_button_group.addButton(self.mp4dx_radio)

        self.mp4_radio.setChecked(self.game_type == "mp4")
        self.mp4dx_radio.setChecked(self.game_type == "mp4dx")

        self.mp4_radio.clicked.connect(lambda: self.set_game_version("mp4"))
        self.mp4dx_radio.clicked.connect(lambda: self.set_game_version("mp4dx"))

        version_layout.addWidget(self.mp4_radio)
        version_layout.addWidget(self.mp4dx_radio)
        version_layout.addStretch()
        shop_card_layout.addLayout(version_layout)

        # Apply initial radio button styling
        self.update_radio_button_theme()

        # Create grid layout for item cards
        items_grid = QVBoxLayout()
        items_grid.setSpacing(12)

        # Create items based on game version
        self.create_version_items(items_grid)
        
        # Store reference to the items grid for later updates
        self.items_grid = items_grid

        shop_card_layout.addLayout(items_grid)
        container_layout.addWidget(shop_card)
        scroll_area.setWidget(container)
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

        # Reapply theme styling to prevent palette glitches in dark mode
        self.update_radio_button_theme()
        
        # Update the items UI to reflect the new game version
        if hasattr(self, 'items_grid'):
            self.update_items_ui(self.items_grid)

    def clear_item_rows(self, scroll_layout):
        """Clear all items by replacing the dynamic content container"""
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

        # Clear the price entries dictionary to prevent accumulation
        self.price_entries.clear()

    def create_dynamic_content_container(self):
        """Create a container widget for dynamic content"""
        container = QWidget()
        container.setObjectName('dynamic_content_container')
        container_layout = QVBoxLayout(container)
        container_layout.setContentsMargins(0, 0, 0, 0)
        container_layout.setSpacing(8)

        # Add the items
        self.create_version_items(container_layout)

        return container

    def update_min_coins_ui(self):
        """Update the min_coins UI based on current game version"""
        # Note: UI updates disabled for stability
        print(f"Min coins UI update requested for game type: {self.game_type}")

    def update_items_ui(self, scroll_layout):
        """Update the items UI based on current game version"""
        # Clear existing dynamic content
        self.clear_item_rows(scroll_layout)

        # Create new dynamic content container
        dynamic_container = self.create_dynamic_content_container()
        scroll_layout.addWidget(dynamic_container)

    def create_column_header(self, parent_layout):
        """Create column header with clear labels"""
        header_layout = QHBoxLayout()
        header_layout.setSpacing(12)
        header_layout.setContentsMargins(10, 5, 10, 5)

        # Empty space for icon
        icon_placeholder = QLabel("")
        icon_placeholder.setFixedWidth(self.icon_width)
        header_layout.addWidget(icon_placeholder)

        # Price columns for different stages and player counts
        stages = ["Early Game", "Mid Game", "Late Game"]
        player_counts = ["1 Player", "2 Players", "3-4 Players"]

        for stage in stages:
            for player_count in player_counts:
                col_label = BodyLabel(f"{stage}\n{player_count}")
                col_label.setAlignment(Qt.AlignCenter)
                header_layout.addWidget(col_label)

        header_layout.addStretch()
        parent_layout.addLayout(header_layout)

        # Add a separator line
        separator = QFrame()
        separator.setFrameShape(QFrame.HLine)
        separator.setFrameShadow(QFrame.Sunken)
        separator.setStyleSheet("color: palette(mid);")
        parent_layout.addWidget(separator)

    def create_item_row(self, parent_layout, item_name, item_icon):
        """Create a single card for an item"""
        # Create individual card for each item
        item_card = CardWidget()
        item_card.setStyleSheet("CardWidget { background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); }")
        item_card_layout = QVBoxLayout(item_card)
        item_card_layout.setContentsMargins(16, 12, 16, 12)
        item_card_layout.setSpacing(8)

        # Item title
        title = BodyLabel(item_name)
        self.apply_label_theme(title, "font-size: 14px; font-weight: 600; margin-bottom: 4px;")
        item_card_layout.addWidget(title)

        # Parameters layout
        params_layout = QHBoxLayout()
        params_layout.setSpacing(16)

        # Add item icon
        icon = self.create_image_label(item_icon, 32, 32)
        params_layout.addWidget(icon)

        # Price inputs for different stages
        stages = ["Early", "Mid", "Late"]
        item_key = item_name.lower().replace(" ", "_")
        self.create_price_inputs_card(params_layout, item_key, stages)

        item_card_layout.addLayout(params_layout)
        parent_layout.addWidget(item_card)

    def create_price_inputs_card(self, layout, item_key, stages):
        """Create price input fields for different game stages in card format"""
        for stage in stages:
            # Create stage section
            stage_layout = QVBoxLayout()
            stage_layout.setSpacing(4)

            stage_label = BodyLabel(f"{stage}:")
            self.apply_label_theme(stage_label, "font-size: 12px; font-weight: 600;")
            stage_layout.addWidget(stage_label)

            # Create inputs for player counts (1, 2, 3-4 players)
            for player_count in ["1", "2", "34"]:
                entry = LineEdit()
                entry.setPlaceholderText(f"{player_count}P")
                entry.setFixedWidth(60)
                entry.setFixedHeight(30)
                entry.setObjectName(f"{item_key}_{stage.lower()}_{player_count}")
                
                stage_layout.addWidget(entry)

                # Store reference for later access using dictionary
                self.price_entries[f"{item_key}_{stage.lower()}_{player_count}"] = entry

            layout.addLayout(stage_layout)

    def create_price_inputs(self, layout, item_key, stages):
        """Create price input fields for different game stages (legacy method)"""
        for stage in stages:
            # Create inputs for player counts (1, 2, 3-4 players)
            for player_count in ["1", "2", "34"]:
                entry = LineEdit()

                # Leave fields blank - users can fill in custom values
                entry.setFixedWidth(self.input_width)
                entry.setObjectName(f"{item_key}_{stage.lower()}_{player_count}")
                # Let QFluentWidgets handle theme-aware styling automatically
                layout.addWidget(entry)

                # Store reference for later access using dictionary
                self.price_entries[f"{item_key}_{stage.lower()}_{player_count}"] = entry

    def get_default_price(self, item_key, stage, player_count):
        """Get default price for item based on game version"""
        if self.game_type == "mp4dx":
            # MP4DX defaults
            defaults = {
                "mini_mushroom": "5",
                "mega_mushroom": "5",
                "super_mini_mushroom": "10",
                "super_mega_mushroom": "15",
                "mushroom": "5",
                "golden_mushroom": "10",
                "reverse_mushroom": "10",
                "poison_mushroom": "5",
                "triple_poison_mushroom": "15",
                "mini_mega_hammer": "10",
                "warp_pipe": "10",
                "swap_card": "15",
                "sparky_sticker": "5",
                "gaddlight": "15",
                "chomp_call": "10",
                "bowser_suit": "12",
                "crystal_ball": "25",
                "magic_lamp": "30",
                "item_bag": "30",
                "celluar_shopper": "5",
                "skeleton_key": "5",
                "plunder_chest": "15",
                "gaddbrush": "15",
                "warp_block": "5",
                "fly_guy": "12",
                "plus_block": "10",
                "minus_block": "10",
                "speed_block": "12",
                "slow_block": "12",
                "bowser_phone": "10",
                "double_dip": "12",
                "hidden_block_card": "40",
                "barter_box": "40",
                "super_warp_pipe": "40",
                "chance_time_charm": "40",
                "wacky_watch": "100"
            }
        else:  # MP4 defaults
            defaults = {
                "mini_mushroom": "5",
                "mega_mushroom": "5",
                "super_mini_mushroom": "15",  # Different from MP4DX
                "super_mega_mushroom": "15",
                "mini_mega_hammer": "10",
                "warp_pipe": "10",
                "swap_card": "15",
                "sparky_sticker": "15",  # Different from MP4DX
                "gaddlight": "15",
                "chomp_call": "15",  # Different from MP4DX
                "bowser_suit": "0",   # Different from MP4DX
                "crystal_ball": "25",
                "magic_lamp": "30",
                "item_bag": "30",
                "bowser_phone": "10",
                "double_dip": "12",
                "hidden_block_card": "40",
                "barter_box": "40",
                "plus_block": "10",
                "minus_block": "10",
                "speed_block": "12",
                "slow_block": "12"
            }

        return defaults.get(item_key, "5")

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
            # Note: min_coins functionality is not currently implemented in the backend
            # min_coins = self.min_coins_entry.text()

            # Collect all item prices
            item_prices = self.collect_item_prices()

            if self.game_type == "mp4dx":
                if 'itemsEvent_mp4ShopDXPrices' in globals():
                    # Call MP4DX function with collected parameters
                    itemsEvent_mp4ShopDXPrices(**item_prices)
                else:
                    self.show_error("Mario Party 4 Deluxe shop price modification not available")
            else:
                if 'itemsEvent_mp4ShopPrices' in globals():
                    # Call MP4 function with collected parameters
                    itemsEvent_mp4ShopPrices(**item_prices)
                else:
                    self.show_error("Mario Party 4 shop price modification not available")

        except Exception as e:
            self.show_error(f"Error generating codes: {str(e)}")

    def collect_item_prices(self):
        """Collect all item prices from the form"""
        prices = {}

        # Get the appropriate item list based on game type
        if self.game_type == "mp4":
            # MP4 items only
            item_list = [
                "mini_mushroom", "mega_mushroom", "super_mini_mushroom", "super_mega_mushroom",
                "mini_mega_hammer", "warp_pipe", "swap_card", "sparky_sticker",
                "gaddlight", "chomp_call", "bowser_suit", "crystal_ball",
                "magic_lamp", "item_bag"
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
                        entry_key = f"{item_key}_{stage}_{player_count}"
                        if entry_key in self.price_entries:
                            entry = self.price_entries[entry_key]
                            param_name = f"{camel_case_name}{stage.capitalize()}Price{player_count}"
                            prices[param_name] = entry.text()

        return prices

    def apply_label_theme(self, label, base_style=""):
        """Apply theme-aware styling to labels with explicit white text for dark mode"""
        from qfluentwidgets import isDarkTheme
        
        if isDarkTheme():
            # Dark theme - explicit white text
            color_style = "color: #ffffff;"
        else:
            # Light theme - dark text
            color_style = "color: #333333;"
        
        # Combine base style with color
        full_style = f"{base_style} {color_style}".strip()
        label.setStyleSheet(full_style)

    def calculate_minimum_coins(self):
        """Calculate minimum coins for MP4 based on lowest non-zero item price"""
        if self.game_type != "mp4" or not hasattr(self, 'min_coins_entry') or self.min_coins_entry is None:
            return

        try:
            min_price = float('inf')

            # Get all MP4 items
            item_list = [
                "mini_mushroom", "mega_mushroom", "super_mini_mushroom", "super_mega_mushroom",
                "mini_mega_hammer", "warp_pipe", "swap_card", "sparky_sticker",
                "gaddlight", "chomp_call", "bowser_suit", "crystal_ball",
                "magic_lamp", "item_bag", "bowser_phone", "double_dip",
                "hidden_block_card", "barter_box", "plus_block", "minus_block",
                "speed_block", "slow_block"
            ]

            stages = ["early", "mid", "late"]
            player_counts = ["1", "2", "34"]

            # Find the lowest non-zero price
            for item_key in item_list:
                for stage in stages:
                    for player_count in player_counts:
                        entry_key = f"{item_key}_{stage}_{player_count}"
                        if entry_key in self.price_entries:
                            entry = self.price_entries[entry_key]
                            try:
                                price = int(entry.text().strip())
                                if price > 0 and price < min_price:
                                    min_price = price
                            except ValueError:
                                continue  # Skip invalid entries

            # Update the minimum coins field if we found a valid price
            if min_price != float('inf'):
                self.min_coins_entry.setText(str(min_price))
            else:
                self.min_coins_entry.setText("0")  # Fallback if no valid prices found

        except Exception as e:
            print(f"Error calculating minimum coins: {e}")
            if hasattr(self, 'min_coins_entry') and self.min_coins_entry:
                self.min_coins_entry.setText("0")

    def show_error(self, message):
        """Show error message to user"""
        QMessageBox.critical(self, "Error", message)

    def create_version_items(self, parent_layout):
        """Create items for the current game version"""
        if self.game_type == "mp4":
            # MP4 items only
            all_items = [
                ("Mini Mushroom", "assets/items/miniMushroom.png"),
                ("Mega Mushroom", "assets/items/megaMushroom.png"),
                ("Sup Mini Mushroom", "assets/items/superMiniMushroom.png"),
                ("Sup Mega Mushroom", "assets/items/superMegaMushroom.png"),
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
                ("Sup Mini Mushroom", "assets/items/superMiniMushroom.png"),
                ("Sup Mega Mushroom", "assets/items/superMegaMushroom.png"),
                ("Mushroom", "assets/items/mushroom.png"),
                ("Golden Mushroom", "assets/items/goldenMushroom.png"),
                ("Reverse Mushroom", "assets/items/reverseMushroom.png"),
                ("Poison Mushroom", "assets/items/poisonMushroom.png"),
                ("Tri. Poison Mushroom", "assets/items/triplePoisonMushroom.png"),
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

        # Create items using card-based layout
        for i, (item_name, item_icon) in enumerate(all_items):
            self.create_item_row(parent_layout, item_name, item_icon)

    def create_minimal_item(self, scroll_layout):
        """Create initial items based on the current game version"""
        # Create dynamic content container
        dynamic_container = self.create_dynamic_content_container()
        scroll_layout.addWidget(dynamic_container)

    def themeChanged(self):
        """Called when theme changes - update all styling"""
        self.update_radio_button_theme()
        # Update CardWidget title theming
        if hasattr(self, 'scroll_area'):
            self.apply_scrollbar_theme(self.scroll_area)
        # QFluentWidgets LineEdit handles theme changes automatically
        # No manual styling needed

    def update_radio_button_theme(self):
        """Update radio button styling based on current theme"""
        from qfluentwidgets import isDarkTheme

        if isDarkTheme():
            # Dark theme styling for radio buttons
            radio_style = """
                QRadioButton {
                    background: transparent;
                    color: #ffffff;
                    font-size: 14px;
                    font-weight: 500;
                    spacing: 8px;
                    padding: 4px;
                }
                QRadioButton::indicator {
                    width: 16px;
                    height: 16px;
                    border: 2px solid #666666;
                    border-radius: 8px;
                    background: #3c3c3c;
                }
                QRadioButton::indicator:checked {
                    background: #0078d4;
                    border: 2px solid #0078d4;
                }
                QRadioButton::indicator:hover {
                    border: 2px solid #999999;
                }
                QRadioButton::indicator:checked:hover {
                    background: #106ebe;
                    border: 2px solid #106ebe;
                }
            """
        else:
            # Light theme styling for radio buttons
            radio_style = """
                QRadioButton {
                    background: transparent;
                    color: #333333;
                    font-size: 14px;
                    font-weight: 500;
                    spacing: 8px;
                    padding: 4px;
                }
                QRadioButton::indicator {
                    width: 16px;
                    height: 16px;
                    border: 2px solid #cccccc;
                    border-radius: 8px;
                    background: #ffffff;
                }
                QRadioButton::indicator:checked {
                    background: #0078d4;
                    border: 2px solid #0078d4;
                }
                QRadioButton::indicator:hover {
                    border: 2px solid #999999;
                }
                QRadioButton::indicator:checked:hover {
                    background: #106ebe;
                    border: 2px solid #106ebe;
                }
            """

        # Apply the styling to radio buttons
        self.mp4_radio.setStyleSheet(radio_style)
        self.mp4dx_radio.setStyleSheet(radio_style)

    def apply_scrollbar_theme(self, scroll_area):
        """Apply themed styling to QScrollArea scrollbars (light/dark)"""
        from qfluentwidgets import isDarkTheme
        if isDarkTheme():
            bar_style = """
                QScrollBar:vertical {
                    background: transparent;
                    width: 12px;
                    margin: 0px;
                }
                QScrollBar::handle:vertical {
                    background: #5a5a5a;
                    min-height: 24px;
                    border-radius: 6px;
                }
                QScrollBar::handle:vertical:hover {
                    background: #7a7a7a;
                }
                QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                    height: 0px;
                }
                QScrollBar:horizontal {
                    background: transparent;
                    height: 12px;
                    margin: 0px;
                }
                QScrollBar::handle:horizontal {
                    background: #5a5a5a;
                    min-width: 24px;
                    border-radius: 6px;
                }
                QScrollBar::handle:horizontal:hover {
                    background: #7a7a7a;
                }
                QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                    width: 0px;
                }
            """
        else:
            bar_style = """
                QScrollBar:vertical {
                    background: transparent;
                    width: 12px;
                    margin: 0px;
                }
                QScrollBar::handle:vertical {
                    background: #c4c4c4;
                    min-height: 24px;
                    border-radius: 6px;
                }
                QScrollBar::handle:vertical:hover {
                    background: #a0a0a0;
                }
                QScrollBar::add-line:vertical, QScrollBar::sub-line:vertical {
                    height: 0px;
                }
                QScrollBar:horizontal {
                    background: transparent;
                    height: 12px;
                    margin: 0px;
                }
                QScrollBar::handle:horizontal {
                    background: #c4c4c4;
                    min-width: 24px;
                    border-radius: 6px;
                }
                QScrollBar::handle:horizontal:hover {
                    background: #a0a0a0;
                }
                QScrollBar::add-line:horizontal, QScrollBar::sub-line:horizontal {
                    width: 0px;
                }
            """

        # Apply the style to both scrollbars
        try:
            scroll_area.verticalScrollBar().setStyleSheet(bar_style)
            scroll_area.horizontalScrollBar().setStyleSheet(bar_style)
        except Exception:
            pass
