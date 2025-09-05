#!/usr/bin/env python3
# ============================================
# Shop Odds Tab Component for Mario Party 4
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QScrollArea, QFrame, QGroupBox, QPushButton, QMessageBox, QRadioButton, QButtonGroup
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from qfluentwidgets import SubtitleLabel, BodyLabel, LineEdit, PushButton, CardWidget

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

        # Themed card container using Fluent design
        card = CardWidget()
        self.shop_odds_card = card
        card_layout = QVBoxLayout()
        card_layout.setSpacing(16)
        card_layout.setContentsMargins(20, 16, 20, 16)
        card.setLayout(card_layout)

        # Add title to the card
        card_title = SubtitleLabel("Item Shop Odds")
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

        # Create dynamic content container for items
        dynamic_container = self.create_dynamic_content_container()
        scroll_layout.addWidget(dynamic_container)

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
        if hasattr(self, 'shop_odds_card'):
            # CardWidget handles its own theming automatically
            self.scroll_widget.setStyleSheet("background: transparent;")
        # Refresh card title color so it doesn't revert
        try:
            self.update_card_title_theme()
        except Exception:
            pass
        self.apply_content_text_theme()
        # Ensure inputs keep white background after version toggle
        for attr in dir(self):
            if attr.endswith('_entry'):
                try:
                    widget = getattr(self, attr)
                    self.apply_white_lineedit_style(widget)
                except Exception:
                    continue

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
        
        # Clear all entry attributes to prevent accessing deleted widgets
        for attr in list(dir(self)):
            if attr.endswith('_entry'):
                try:
                    delattr(self, attr)
                except (AttributeError, RuntimeError):
                    # Ignore errors if attribute doesn't exist or widget is deleted
                    continue

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
                # Always render inputs with white background for readability
                self.apply_white_lineedit_style(entry)
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
                            try:
                                entry = getattr(self, entry_name)
                                param_name = f"{camel_case_name}{stage.capitalize()}Odds{player_count}"
                                odds[param_name] = entry.text()
                            except RuntimeError:
                                # Widget has been deleted, skip this entry
                                continue

        return odds

    def show_error(self, message):
        """Show error message to user"""
        QMessageBox.critical(self, "Error", message)

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
        # Reinforce white backgrounds aftert theme switch
        for attr in dir(self):
            if attr.endswith('_entry'):
                try:
                    widget = getattr(self, attr)
                    self.apply_white_lineedit_style(widget)
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

        try:
            scroll_area.verticalScrollBar().setStyleSheet(bar_style)
            scroll_area.horizontalScrollBar().setStyleSheet(bar_style)
        except Exception:
            pass

    def apply_content_text_theme(self):
        """Force text colors for labels and line edits to follow current palette"""
        if hasattr(self, 'scroll_widget') and self.scroll_widget:
            base_style = "background: transparent;"
            text_rules = " QLabel { color: palette(text); } "
            self.scroll_widget.setStyleSheet(f"{base_style}{text_rules}")
        # Update dynamically created LineEdits with fixed white background + black text
        for attr in dir(self):
            if attr.endswith('_entry'):
                try:
                    widget = getattr(self, attr)
                    if isinstance(widget, LineEdit) or isinstance(widget, QLineEdit):
                        self.apply_white_lineedit_style(widget)
                except Exception:
                    continue

    def apply_white_lineedit_style(self, widget):
        """Apply white background/black text styling to inputs (Windows-safe)."""
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
