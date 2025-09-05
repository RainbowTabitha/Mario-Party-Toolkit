#!/usr/bin/env python3
# ============================================
# Shop Prices Tab Component for Mario Party 4
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QSizePolicy, QLabel, QLineEdit, QScrollArea, QFrame, QGroupBox, QPushButton, QMessageBox, QRadioButton, QButtonGroup
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from qfluentwidgets import SubtitleLabel, BodyLabel, LineEdit, PushButton, CardWidget

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

        # Main layout
        layout = QVBoxLayout()
        layout.setSpacing(8)
        layout.setContentsMargins(16, 12, 16, 12)

        # Title
        title = SubtitleLabel("Item Shop Price Modifications")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)

        # Description
        desc = BodyLabel("Modify prices for items in the shop at different game stages:")
        desc.setAlignment(Qt.AlignCenter)
        layout.addWidget(desc)

        # Themed card container using Fluent design
        card = CardWidget()
        self.shop_prices_card = card
        card_layout = QVBoxLayout()
        card_layout.setSpacing(16)
        card_layout.setContentsMargins(20, 16, 20, 16)
        card.setLayout(card_layout)

        # Add title to the card
        card_title = SubtitleLabel("Item Shop Prices")
        card_title.setObjectName("card_title")
        self.card_title = card_title
        card_layout.addWidget(card_title)

        # Scrollable area for the form
        scroll_area = QScrollArea()
        self.scroll_area = scroll_area
        scroll_area.setWidgetResizable(True)
        scroll_area.setHorizontalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setVerticalScrollBarPolicy(Qt.ScrollBarAsNeeded)
        scroll_area.setFrameShape(QFrame.NoFrame)
        # Make scroll area blend with group background
        scroll_area.setStyleSheet("QScrollArea { border: none; background: transparent; }")
        scroll_area.viewport().setStyleSheet("background: transparent;")

        # Container widget for scroll area
        self.scroll_widget = QWidget()
        self.scroll_widget.setStyleSheet("background: transparent;")
        scroll_layout = QVBoxLayout(self.scroll_widget)
        scroll_layout.setSpacing(16)

        # Game version selection
        version_layout = QHBoxLayout()
        version_layout.addWidget(BodyLabel("Game Version:"))

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
        # Place version selector at the top of the card (not inside scroller)
        card_layout.addLayout(version_layout)

        # Apply initial radio button styling
        self.update_radio_button_theme()

        # Create header with column labels
        self.create_column_header(scroll_layout)

        # Create minimal items for testing
        self.create_minimal_item(scroll_layout)

        # Add some bottom spacing
        spacer = QFrame()
        spacer.setFixedHeight(12)
        spacer.setFrameShape(QFrame.NoFrame)
        scroll_layout.addWidget(spacer)

        # Set scroll widget and add to card
        scroll_area.setWidget(self.scroll_widget)
        card_layout.addWidget(scroll_area)

        # Theme the scrollbars to match current theme
        self.apply_scrollbar_theme(scroll_area)

        # Add card to main layout
        layout.addWidget(card)

        # Generate button
        generate_btn = PushButton("Generate Codes")
        generate_btn.clicked.connect(self.generate_codes)
        layout.addWidget(generate_btn)

        self.setLayout(layout)

        # Ensure text colors match theme after widget shows
        try:
            from PyQt5.QtCore import QTimer
            QTimer.singleShot(0, self.apply_content_text_theme)
            QTimer.singleShot(0, self.update_card_title_theme)
        except Exception:
            self.apply_content_text_theme()
            self.update_card_title_theme()

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

        # Reapply theme styling to prevent palette glitches in dark mode
        self.update_radio_button_theme()
        if hasattr(self, 'scroll_widget'):
            self.scroll_widget.setStyleSheet("background: transparent;")
        # Refresh card title color so it doesn't revert
        try:
            self.update_card_title_theme()
        except Exception:
            pass
        # Ensure new inputs keep white background
        for entry in getattr(self, 'price_entries', {}).values():
            try:
                self.apply_white_lineedit_style(entry)
            except Exception:
                continue

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

        # Item name column
        item_header = BodyLabel("Item")
        item_header.setStyleSheet(f"font-size: 14px; font-weight: 700; min-width: {self.name_col_width}px;")
        header_layout.addWidget(item_header)

        # Price columns for different stages and player counts
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

        # Price inputs for different stages
        stages = ["Early", "Mid", "Late"]
        item_key = item_name.lower().replace(" ", "_")
        self.create_price_inputs(item_layout, item_key, stages)

        item_layout.addStretch()
        parent_layout.addLayout(item_layout)

    def create_price_inputs(self, layout, item_key, stages):
        """Create price input fields for different game stages"""
        for stage in stages:
            # Create inputs for player counts (1, 2, 3-4 players)
            for player_count in ["1", "2", "34"]:
                entry = LineEdit()

                # Leave fields blank - users can fill in custom values
                entry.setFixedWidth(self.input_width)
                entry.setObjectName(f"{item_key}_{stage.lower()}_{player_count}")
                # Always render inputs with white background for readability
                self.apply_white_lineedit_style(entry)
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

    def create_version_items(self, scroll_layout):
        """Create items for the current game version"""
        if self.game_type == "mp4":
            items_to_create = [
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
                ("Bowser Phone", "assets/items/bowserPhone.png"),
                ("Double Dip", "assets/items/doubleDip.png"),
            ]
        else:  # MP4 DX
            items_to_create = [
                ("Mini Mushroom", "assets/items/miniMushroom.png"),
                ("Mega Mushroom", "assets/items/megaMushroom.png"),
                ("Sup Mini Mushroom", "assets/items/superMiniMushroom.png"),
                ("Sup Mega Mushroom", "assets/items/superMegaMushroom.png"),
                ("Mushroom", "assets/items/mushroom.png"),
                ("Golden Mushroom", "assets/items/goldenMushroom.png"),
                ("Reverse Mushroom", "assets/items/reverseMushroom.png"),
                ("Poison Mushroom", "assets/items/poisonMushroom.png"),
                ("Tri, Poison Mushroom", "assets/items/triplePoisonMushroom.png"),
                ("Mini Mega Hammer", "assets/items/miniMegaHammer.png"),
                ("Warp Pipe", "assets/items/warpPipe.png"),
                ("Swap Card", "assets/items/swapCard.png"),
                ("Sparky Sticker", "assets/items/sparkySticker.png"),
                ("Gaddlight", "assets/items/gaddlight.png"),
                ("Chomp Call", "assets/items/chompCall.png"),
                ("Bowser Suit", "assets/items/bowserSuit4.png"),
            ]

        # Create items (limited for stability)
        for i, (item_name, item_icon) in enumerate(items_to_create):
            if i >= 12:  # Allow more items for better UX
                break
            self.create_item_row(scroll_layout, item_name, item_icon)

        # Add spacer at the end
        spacer = QFrame()
        spacer.setFixedHeight(12)
        spacer.setFrameShape(QFrame.NoFrame)
        scroll_layout.addWidget(spacer)

    def create_minimal_item(self, scroll_layout):
        """Create initial items based on the current game version"""
        # Create dynamic content container
        dynamic_container = self.create_dynamic_content_container()
        scroll_layout.addWidget(dynamic_container)

    def update_card_title_theme(self):
        """Update CardWidget title styling based on current theme"""
        if hasattr(self, 'card_title') and self.card_title:
            from qfluentwidgets import isDarkTheme
            if isDarkTheme():
                self.card_title.setStyleSheet("color: #ffffff; font-size: 16px; font-weight: 600; margin-bottom: 8px;")
            else:
                self.card_title.setStyleSheet("color: #333333; font-size: 16px; font-weight: 600; margin-bottom: 8px;")

    def themeChanged(self):
        """Called when theme changes - update all styling"""
        self.update_radio_button_theme()
        # Update CardWidget title theming
        self.update_card_title_theme()
        if hasattr(self, 'scroll_area'):
            self.apply_scrollbar_theme(self.scroll_area)
        self.apply_content_text_theme()
        # Reinforce white backgrounds after theme switch
        for entry in getattr(self, 'price_entries', {}).values():
            try:
                self.apply_white_lineedit_style(entry)
            except Exception:
                continue

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

    def apply_content_text_theme(self):
        """Force text colors for labels and line edits to follow current palette"""
        # Apply at container level so all children inherit
        if hasattr(self, 'scroll_widget') and self.scroll_widget:
            base_style = "background: transparent;"
            text_rules = " QLabel { color: palette(text); } QLineEdit { color: palette(text); } "
            # Merge with any existing style (keep background transparent)
            self.scroll_widget.setStyleSheet(f"{base_style}{text_rules}")
        # Also ensure individual entries keep white background/black text
        for entry in getattr(self, 'price_entries', {}).values():
            try:
                self.apply_white_lineedit_style(entry)
            except Exception:
                continue

    def apply_white_lineedit_style(self, widget):
        """Apply a Windows-safe white background style to LineEdits"""
        try:
            widget.setAttribute(Qt.WA_StyledBackground, True)
        except Exception:
            pass
        widget.setStyleSheet("""
            QLineEdit {
                background-color: #ffffff;
                color: #000000;
                selection-background-color: #cfe8ff;
                selection-color: #000000;
                border: 1px solid palette(mid);
                border-radius: 6px;
            }
            QLineEdit:disabled {
                background-color: #f0f0f0;
                color: #808080;
            }
            QLineEdit:hover {
                border: 1px solid #8c8c8c;
            }
            QLineEdit:focus {
                border: 1px solid #0078d4;
            }
        """)
