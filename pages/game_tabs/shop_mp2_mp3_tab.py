#!/usr/bin/env python3
# ============================================
# Items Tab Component for Mario Party Toolkit
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QApplication, QGroupBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from qfluentwidgets import SubtitleLabel, BodyLabel, LineEdit, CheckBox, PushButton, InfoBar, InfoBarPosition, CardWidget, ScrollArea

# Import items event functions for supported games
try:
    from events.marioParty2_items import itemsEvent_mp2
    from events.marioParty3_items import itemsEvent_mp3
except ImportError:
    pass

# Import image utilities
from functions import fetchResource
from PyQt5.QtGui import QIcon


class ItemsTab(QWidget):
    def __init__(self, game_id):
        super().__init__()
        self.game_id = game_id
        self.setup_ui()

    def setup_ui(self):
        """Set up the items tab UI"""
        self.setObjectName(f"{self.game_id}ItemsTab")
        
        # Main layout
        layout = QVBoxLayout()
        layout.setSpacing(8)
        layout.setContentsMargins(16, 12, 16, 12)
        
        # Title
        title = SubtitleLabel("Item Price Modifications")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Description
        desc = BodyLabel("Modify the prices for different items:")
        desc.setAlignment(Qt.AlignCenter)
        layout.addWidget(desc)
        
        # Check if this game supports item modifications
        if self.game_id not in ["marioParty2", "marioParty3"]:
            # Show unsupported message
            unsupported_label = BodyLabel("Item price modifications are not supported for this game.")
            unsupported_label.setAlignment(Qt.AlignCenter)
            unsupported_label.setStyleSheet("font-size: 18px; margin: 32px 0; padding: 24px;")
            layout.addWidget(unsupported_label)
            layout.addStretch()
            self.setLayout(layout)
            return
        
        # Create scroll area for the items
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
        
        # Add title
        card_title = SubtitleLabel("Item Prices")
        card_title.setStyleSheet("font-size: 16px; font-weight: 600; margin-bottom: 8px;")
        container_layout.addWidget(card_title)
        
        # Create item entries based on game
        self.create_item_entries(container_layout)
        
        # Set the container as the scroll area's widget
        scroll_area.setWidget(container)
        layout.addWidget(scroll_area)
        
        # Generate button
        generate_btn = PushButton("Generate Codes")
        generate_btn.clicked.connect(self.generate_codes)
        layout.addWidget(generate_btn)
        
        # Add stretch to push everything up
        layout.addStretch()
        
        self.setLayout(layout)

    def create_item_entries(self, group_layout):
        """Create item entry fields based on the current game"""
        if self.game_id == "marioParty2":
            self.create_mp2_items(group_layout)
        elif self.game_id == "marioParty3":
            self.create_mp3_items(group_layout)

    def create_mp2_items(self, group_layout):
        """Create Mario Party 2 item entries"""
        
        # Create grid layout for items (similar to MP7)
        items_grid = QVBoxLayout()
        items_grid.setSpacing(12)
        
        # Define MP2 items with their properties
        self.mp2_items = [
            ("Mushroom", "assets/items/mushroom.png", "mushroom", False),
            ("Skeleton Key", "assets/items/skeletonKey.png", "key", False),
            ("Plunder Chest", "assets/items/plunderChest.png", "chest", False),
            ("Bowser Phone", "assets/items/bowserPhone.png", "phone", False),
            ("Dueling Glove", "assets/items/duelingGlove.png", "glove", False),
            ("Warp Block", "assets/items/warpBlock.png", "warp", False),
            ("Golden Mushroom", "assets/items/goldenMushroom.png", "golden", False),
            ("Magic Lamp", "assets/items/magicLamp.png", "lamp", False),
            ("Poison Mushroom", "assets/items/poisonMushroom.png", "poison", False),
            ("Reverse Mushroom", "assets/items/reverseMushroom.png", "reverse", False),
            ("Lucky Lamp", "assets/items/luckyLamp.png", "lucky", False),
            ("Warp Block", "assets/items/warpBlock.png", "warp2", False),
            ("Cellular Shopper", "assets/items/celluarShopper.png", "shopper", False),
            ("Boo Bell", "assets/items/booBell.png", "bell", False),
            ("Boo Repellant", "assets/items/booRepellent.png", "repellant", False),
            ("Bowser Suit", "assets/items/bowserSuit.png", "suit", False),
            ("Item Bag", "assets/items/itemBag3.png", "bag", False)
        ]
        
        # Create entries for each item
        for item_name, icon_path, item_key, is_red in self.mp2_items:
            item_group = self.create_mp2_item_group(item_name, icon_path, item_key, is_red)
            items_grid.addWidget(item_group)
        
        group_layout.addLayout(items_grid)
    
    def create_mp2_item_group(self, item_name, icon_path, item_key, is_red):
        """Create a group for a single MP2 item (MP7-style card format)"""
        
        # Create card widget (like MP7)
        group_card = CardWidget()
        group_card.setStyleSheet("CardWidget { background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); }")
        group_layout = QVBoxLayout(group_card)
        group_layout.setContentsMargins(16, 12, 16, 12)
        group_layout.setSpacing(8)

        # Item title (like MP7)
        title = BodyLabel(item_name)
        if is_red:
            title.setStyleSheet("font-size: 14px; font-weight: 600; margin-bottom: 4px; color: red;")
        else:
            title.setStyleSheet("font-size: 14px; font-weight: 600; margin-bottom: 4px;")
        group_layout.addWidget(title)

        # Create grid for parameters (like MP7)
        params_layout = QHBoxLayout()
        params_layout.setSpacing(8)

        # Add item icon (like MP7)
        icon = self.create_image_label(icon_path, 32, 32)
        params_layout.addWidget(icon)

        # Price parameters (like MP7 structure)
        price_layout = QVBoxLayout()
        price_layout.setSpacing(4)

        price_label = BodyLabel("Price:")
        price_label.setStyleSheet("font-size: 12px; font-weight: 600;")
        price_layout.addWidget(price_label)

        price_row = QHBoxLayout()
        price_row.setSpacing(4)

        # Single price entry (MP2/MP3 only need one price)
        price_entry = LineEdit()
        price_entry.setPlaceholderText("Coins")
        price_entry.setFixedWidth(70)
        price_entry.setFixedHeight(30)
        price_row.addWidget(price_entry)
        setattr(self, f"{item_key}_entry", price_entry)

        price_layout.addLayout(price_row)
        params_layout.addLayout(price_layout)

        group_layout.addLayout(params_layout)

        return group_card

    def create_mp3_items(self, group_layout):
        """Create Mario Party 3 item entries"""
        
        # Add pricing note for red items
        pricing_note = BodyLabel("Note: Items shown in red must have equal prices to work properly.")
        pricing_note.setStyleSheet("font-size: 14px; color: red; font-weight: 600; margin-bottom: 16px; padding: 8px; background: rgba(255, 0, 0, 0.1); border-radius: 4px;")
        group_layout.addWidget(pricing_note)
        
        # Create grid layout for items (similar to MP7)
        items_grid = QVBoxLayout()
        items_grid.setSpacing(12)
        
        # Define MP3 items with their properties
        self.mp3_items = [
            ("Mushroom", "assets/items/mushroom.png", "mushroom", True),  # Red text
            ("Skeleton Key", "assets/items/skeletonKey.png", "key", True),  # Red text
            ("Plunder Chest", "assets/items/plunderChest.png", "chest", False),
            ("Bowser Phone", "assets/items/bowserPhone.png", "phone", False),
            ("Dueling Glove", "assets/items/duelingGlove.png", "glove", False),
            ("Warp Block", "assets/items/warpBlock.png", "warp", True),  # Red text
            ("Golden Mushroom", "assets/items/goldenMushroom.png", "golden", False),
            ("Magic Lamp", "assets/items/magicLamp.png", "lamp", False),
            ("Poison Mushroom", "assets/items/poisonMushroom.png", "poison", True),  # Red text
            ("Reverse Mushroom", "assets/items/reverseMushroom.png", "reverse", True),  # Red text
            ("Lucky Lamp", "assets/items/luckyLamp.png", "lucky", False),
            ("Warp Block", "assets/items/warpBlock.png", "warp2", True),  # Red text (duplicate)
            ("Cellular Shopper", "assets/items/celluarShopper.png", "shopper", True),  # Red text
            ("Boo Bell", "assets/items/booBell.png", "bell", False),
            ("Boo Repellant", "assets/items/booRepellant.png", "repellant", False),
            ("Bowser Suit", "assets/items/bowserSuit.png", "suit", False),
            ("Item Bag", "assets/items/itemBag.png", "bag", False)
        ]
        
        # Create entries for each item
        for item_name, icon_path, item_key, is_red in self.mp3_items:
            item_group = self.create_mp3_item_group(item_name, icon_path, item_key, is_red)
            items_grid.addWidget(item_group)
        
        group_layout.addLayout(items_grid)
    
    def create_mp3_item_group(self, item_name, icon_path, item_key, is_red):
        """Create a group for a single MP3 item (MP7-style card format)"""
        
        # Create card widget (like MP7)
        group_card = CardWidget()
        group_card.setStyleSheet("CardWidget { background: rgba(255, 255, 255, 0.05); border: 1px solid rgba(255, 255, 255, 0.1); }")
        group_layout = QVBoxLayout(group_card)
        group_layout.setContentsMargins(16, 12, 16, 12)
        group_layout.setSpacing(8)

        # Item title (like MP7)
        title = BodyLabel(item_name)
        if is_red:
            title.setStyleSheet("font-size: 14px; font-weight: 600; margin-bottom: 4px; color: red;")
        else:
            title.setStyleSheet("font-size: 14px; font-weight: 600; margin-bottom: 4px;")
        group_layout.addWidget(title)

        # Create grid for parameters (like MP7)
        params_layout = QHBoxLayout()
        params_layout.setSpacing(8)

        # Add item icon (like MP7)
        icon = self.create_image_label(icon_path, 32, 32)
        params_layout.addWidget(icon)

        # Price parameters (like MP7 structure)
        price_layout = QVBoxLayout()
        price_layout.setSpacing(4)

        price_label = BodyLabel("Price:")
        price_label.setStyleSheet("font-size: 12px; font-weight: 600;")
        price_layout.addWidget(price_label)

        price_row = QHBoxLayout()
        price_row.setSpacing(4)

        # Single price entry (MP2/MP3 only need one price)
        price_entry = LineEdit()
        price_entry.setPlaceholderText("Coins")
        price_entry.setFixedWidth(70)
        price_entry.setFixedHeight(30)
        price_row.addWidget(price_entry)
        setattr(self, f"{item_key}_entry", price_entry)

        price_layout.addLayout(price_row)
        params_layout.addLayout(price_layout)

        group_layout.addLayout(params_layout)

        return group_card
    
    def create_image_label(self, image_path, width=32, height=32):
        """Create a QLabel with an image from the assets folder (MP7-style)"""
        try:
            # Get the image path from resource manager (like MP7)
            from utils.resource_manager import ResourceManager
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
        """Generate codes for the current game"""
        try:
            # Create mock objects to match the expected interface
            class MockEntry:
                def __init__(self, text):
                    self._text = text
                def get(self):
                    return self._text
                def text(self):
                    return self._text
            
            # Create mock objects with current values
            if self.game_id == "marioParty2":
                mushroom_price = MockEntry(self.mushroom_entry.text())
                key_price = MockEntry(self.key_entry.text())
                chest_price = MockEntry(self.chest_entry.text())
                phone_price = MockEntry(self.phone_entry.text())
                glove_price = MockEntry(self.glove_entry.text())
                warp_price = MockEntry(self.warp_entry.text())
                golden_price = MockEntry(self.golden_entry.text())
                lamp_price = MockEntry(self.lamp_entry.text())
                poison_price = MockEntry(self.poison_entry.text())
                reverse_price = MockEntry(self.reverse_entry.text())
                lucky_price = MockEntry(self.lucky_entry.text())
                warp2_price = MockEntry(self.warp2_entry.text())
                shopper_price = MockEntry(self.shopper_entry.text())
                bell_price = MockEntry(self.bell_entry.text())
                repellant_price = MockEntry(self.repellant_entry.text())
                suit_price = MockEntry(self.suit_entry.text())
                bag_price = MockEntry(self.bag_entry.text())
                
                # Call the MP2 items event function
                if itemsEvent_mp2:
                    itemsEvent_mp2(mushroom_price, key_price, chest_price, phone_price, glove_price, warp_price, golden_price, lamp_price, poison_price, reverse_price, lucky_price, warp2_price, shopper_price, bell_price, repellant_price, suit_price, bag_price)
                else:
                    self.show_error("Mario Party 2 item modifications not available")
                    
            elif self.game_id == "marioParty3":
                mushroom_price = MockEntry(self.mushroom_entry.text())
                key_price = MockEntry(self.key_entry.text())
                chest_price = MockEntry(self.chest_entry.text())
                phone_price = MockEntry(self.phone_entry.text())
                glove_price = MockEntry(self.glove_entry.text())
                warp_price = MockEntry(self.warp_entry.text())
                golden_price = MockEntry(self.golden_entry.text())
                lamp_price = MockEntry(self.lamp_entry.text())
                poison_price = MockEntry(self.poison_entry.text())
                reverse_price = MockEntry(self.reverse_entry.text())
                lucky_price = MockEntry(self.lucky_entry.text())
                warp2_price = MockEntry(self.warp2_entry.text())
                shopper_price = MockEntry(self.shopper_entry.text())
                bell_price = MockEntry(self.bell_entry.text())
                repellant_price = MockEntry(self.repellant_entry.text())
                suit_price = MockEntry(self.suit_entry.text())
                bag_price = MockEntry(self.bag_entry.text())

                # Call the MP3 items event function
                if itemsEvent_mp3:
                    itemsEvent_mp3(mushroom_price, key_price, chest_price, phone_price, glove_price, warp_price, golden_price, lamp_price, poison_price, reverse_price, lucky_price, warp2_price, shopper_price, bell_price, repellant_price, suit_price, bag_price)
                else:
                    self.show_error("Mario Party 3 item modifications not available")
                    
        except Exception as e:
            self.show_error(f"Error generating codes: {str(e)}")

    def show_error(self, message):
        """Show error message to user"""
        QMessageBox.critical(self, "Error", message)