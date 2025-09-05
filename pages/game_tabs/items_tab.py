#!/usr/bin/env python3
# ============================================
# Items Tab Component for Mario Party Toolkit
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QApplication, QGroupBox
from PyQt5.QtCore import Qt
from qfluentwidgets import SubtitleLabel, BodyLabel, LineEdit, CheckBox, PushButton, InfoBar, InfoBarPosition

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
        
        # Item Prices Group
        group = QGroupBox("Item Prices")
        
        # Store reference to group for theme updates
        self.items_group = group
        
        # Apply initial styling
        self.update_items_group_theme()
        
        group_layout = QVBoxLayout()
        group_layout.setSpacing(12)
        group_layout.setContentsMargins(16, 12, 16, 12)
        group.setLayout(group_layout)
        
        # Create item entries based on game
        self.create_item_entries(group_layout)
        
        layout.addWidget(group)
        
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
        # Mushroom
        mushroom_row = QHBoxLayout()
        mushroom_row.setSpacing(12)

        # Mushroom icon
        mushroom_icon = QLabel()
        mushroom_icon.setPixmap(QIcon(str(fetchResource("assets/items/mushroom.png"))).pixmap(24, 24))
        mushroom_icon.setStyleSheet("padding: 2px;")
        mushroom_row.addWidget(mushroom_icon)

        mushroom_label = BodyLabel("Mushroom:")
        mushroom_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px;")
        mushroom_row.addWidget(mushroom_label)

        self.mushroom_entry = LineEdit()
        self.mushroom_entry.setFixedWidth(60)
        mushroom_row.addWidget(self.mushroom_entry)

        mushroom_row.addStretch()
        group_layout.addLayout(mushroom_row)

        # Skeleton Key
        key_row = QHBoxLayout()
        key_row.setSpacing(12)

        # Skeleton Key icon
        key_icon = QLabel()
        key_icon.setPixmap(QIcon(str(fetchResource("assets/items/skeletonKey.png"))).pixmap(24, 24))
        key_icon.setStyleSheet("padding: 2px;")
        key_row.addWidget(key_icon)

        key_label = BodyLabel("Skeleton Key:")
        key_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px;")
        key_row.addWidget(key_label)

        self.key_entry = LineEdit()
        self.key_entry.setFixedWidth(80)  # Make skeleton key wider
        key_row.addWidget(self.key_entry)

        key_row.addStretch()
        group_layout.addLayout(key_row)

        # Plunder Chest
        chest_row = QHBoxLayout()
        chest_row.setSpacing(12)

        # Plunder Chest icon
        chest_icon = QLabel()
        chest_icon.setPixmap(QIcon(str(fetchResource("assets/items/plunderChest.png"))).pixmap(24, 24))
        chest_icon.setStyleSheet("padding: 2px;")
        chest_row.addWidget(chest_icon)

        chest_label = BodyLabel("Plunder Chest:")
        chest_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px;")
        chest_row.addWidget(chest_label)

        self.chest_entry = LineEdit()
        self.chest_entry.setFixedWidth(60)
        chest_row.addWidget(self.chest_entry)

        chest_row.addStretch()
        group_layout.addLayout(chest_row)

        # Dueling Glove
        glove_row = QHBoxLayout()
        glove_row.setSpacing(12)

        # Dueling Glove icon
        glove_icon = QLabel()
        glove_icon.setPixmap(QIcon(str(fetchResource("assets/items/duelingGlove.png"))).pixmap(24, 24))
        glove_icon.setStyleSheet("padding: 2px;")
        glove_row.addWidget(glove_icon)

        glove_label = BodyLabel("Dueling Glove:")
        glove_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px;")
        glove_row.addWidget(glove_label)

        self.glove_entry = LineEdit()
        self.glove_entry.setFixedWidth(60)
        glove_row.addWidget(self.glove_entry)

        glove_row.addStretch()
        group_layout.addLayout(glove_row)

        # Warp Block
        warp_row = QHBoxLayout()
        warp_row.setSpacing(12)

        # Warp Block icon
        warp_icon = QLabel()
        warp_icon.setPixmap(QIcon(str(fetchResource("assets/items/warpBlock.png"))).pixmap(24, 24))
        warp_icon.setStyleSheet("padding: 2px;")
        warp_row.addWidget(warp_icon)

        warp_label = BodyLabel("Warp Block:")
        warp_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px;")
        warp_row.addWidget(warp_label)

        self.warp_entry = LineEdit()
        self.warp_entry.setFixedWidth(60)
        warp_row.addWidget(self.warp_entry)

        warp_row.addStretch()
        group_layout.addLayout(warp_row)

        # Golden Mushroom
        golden_row = QHBoxLayout()
        golden_row.setSpacing(12)

        # Golden Mushroom icon
        golden_icon = QLabel()
        golden_icon.setPixmap(QIcon(str(fetchResource("assets/items/goldenMushroom.png"))).pixmap(24, 24))
        golden_icon.setStyleSheet("padding: 2px;")
        golden_row.addWidget(golden_icon)

        golden_label = BodyLabel("Golden Mushroom:")
        golden_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px;")
        golden_row.addWidget(golden_label)

        self.golden_entry = LineEdit()
        self.golden_entry.setFixedWidth(60)
        golden_row.addWidget(self.golden_entry)

        golden_row.addStretch()
        group_layout.addLayout(golden_row)

        # Magic Lamp
        lamp_row = QHBoxLayout()
        lamp_row.setSpacing(12)

        # Magic Lamp icon
        lamp_icon = QLabel()
        lamp_icon.setPixmap(QIcon(str(fetchResource("assets/items/magicLamp.png"))).pixmap(24, 24))
        lamp_icon.setStyleSheet("padding: 2px;")
        lamp_row.addWidget(lamp_icon)

        lamp_label = BodyLabel("Magic Lamp:")
        lamp_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px;")
        lamp_row.addWidget(lamp_label)

        self.lamp_entry = LineEdit()
        self.lamp_entry.setFixedWidth(60)
        lamp_row.addWidget(self.lamp_entry)

        lamp_row.addStretch()
        group_layout.addLayout(lamp_row)

    def create_mp3_items(self, group_layout):
        """Create Mario Party 3 item entries"""
        # Mushroom
        mushroom_row = QHBoxLayout()
        mushroom_row.setSpacing(12)

        # Mushroom icon
        mushroom_icon = QLabel()
        mushroom_icon.setPixmap(QIcon(str(fetchResource("assets/items/mushroom.png"))).pixmap(24, 24))
        mushroom_icon.setStyleSheet("padding: 2px;")
        mushroom_row.addWidget(mushroom_icon)

        mushroom_label = BodyLabel("Mushroom:")
        mushroom_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px; color: red;")
        mushroom_row.addWidget(mushroom_label)
        
        self.mushroom_entry = LineEdit()
        self.mushroom_entry.setFixedWidth(60)
        mushroom_row.addWidget(self.mushroom_entry)
        
        mushroom_row.addStretch()
        group_layout.addLayout(mushroom_row)
        
        # Skeleton Key
        key_row = QHBoxLayout()
        key_row.setSpacing(12)

        # Skeleton Key icon
        key_icon = QLabel()
        key_icon.setPixmap(QIcon(str(fetchResource("assets/items/skeletonKey.png"))).pixmap(24, 24))
        key_icon.setStyleSheet("padding: 2px;")
        key_row.addWidget(key_icon)

        key_label = BodyLabel("Skeleton Key:")
        key_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px; color: red;")
        key_row.addWidget(key_label)

        self.key_entry = LineEdit()
        self.key_entry.setFixedWidth(80)  # Make skeleton key wider
        key_row.addWidget(self.key_entry)
        
        key_row.addStretch()
        group_layout.addLayout(key_row)

        # Plunder Chest
        chest_row = QHBoxLayout()
        chest_row.setSpacing(12)

        # Plunder Chest icon
        chest_icon = QLabel()
        chest_icon.setPixmap(QIcon(str(fetchResource("assets/items/plunderChest.png"))).pixmap(24, 24))
        chest_icon.setStyleSheet("padding: 2px;")
        chest_row.addWidget(chest_icon)

        chest_label = BodyLabel("Plunder Chest:")
        chest_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px;")
        chest_row.addWidget(chest_label)

        self.chest_entry = LineEdit()
        self.chest_entry.setFixedWidth(60)
        chest_row.addWidget(self.chest_entry)

        chest_row.addStretch()
        group_layout.addLayout(chest_row)

        # Poison Mushroom (red text)
        poison_row = QHBoxLayout()
        poison_row.setSpacing(12)

        # Poison Mushroom icon
        poison_icon = QLabel()
        poison_icon.setPixmap(QIcon(str(fetchResource("assets/items/poisonMushroom.png"))).pixmap(24, 24))
        poison_icon.setStyleSheet("padding: 2px;")
        poison_row.addWidget(poison_icon)

        poison_label = BodyLabel("Poison Mushroom:")
        poison_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px; color: red;")
        poison_row.addWidget(poison_label)

        self.poison_entry = LineEdit()
        self.poison_entry.setFixedWidth(60)
        poison_row.addWidget(self.poison_entry)

        poison_row.addStretch()
        group_layout.addLayout(poison_row)

        # Reverse Mushroom (red text)
        reverse_row = QHBoxLayout()
        reverse_row.setSpacing(12)

        # Reverse Mushroom icon
        reverse_icon = QLabel()
        reverse_icon.setPixmap(QIcon(str(fetchResource("assets/items/reverseMushroom.png"))).pixmap(24, 24))
        reverse_icon.setStyleSheet("padding: 2px;")
        reverse_row.addWidget(reverse_icon)

        reverse_label = BodyLabel("Reverse Mushroom:")
        reverse_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px; color: red;")
        reverse_row.addWidget(reverse_label)

        self.reverse_entry = LineEdit()
        self.reverse_entry.setFixedWidth(60)
        reverse_row.addWidget(self.reverse_entry)

        reverse_row.addStretch()
        group_layout.addLayout(reverse_row)

        # Golden Mushroom
        golden_row = QHBoxLayout()
        golden_row.setSpacing(12)

        # Golden Mushroom icon
        golden_icon = QLabel()
        golden_icon.setPixmap(QIcon(str(fetchResource("assets/items/goldenMushroom.png"))).pixmap(24, 24))
        golden_icon.setStyleSheet("padding: 2px;")
        golden_row.addWidget(golden_icon)

        golden_label = BodyLabel("Golden Mushroom:")
        golden_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px;")
        golden_row.addWidget(golden_label)

        self.golden_entry = LineEdit()
        self.golden_entry.setFixedWidth(60)
        golden_row.addWidget(self.golden_entry)

        golden_row.addStretch()
        group_layout.addLayout(golden_row)

        # Magic Lamp
        lamp_row = QHBoxLayout()
        lamp_row.setSpacing(12)

        # Magic Lamp icon
        lamp_icon = QLabel()
        lamp_icon.setPixmap(QIcon(str(fetchResource("assets/items/magicLamp.png"))).pixmap(24, 24))
        lamp_icon.setStyleSheet("padding: 2px;")
        lamp_row.addWidget(lamp_icon)

        lamp_label = BodyLabel("Magic Lamp:")
        lamp_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px;")
        lamp_row.addWidget(lamp_label)

        self.lamp_entry = LineEdit()
        self.lamp_entry.setFixedWidth(60)
        lamp_row.addWidget(self.lamp_entry)

        lamp_row.addStretch()
        group_layout.addLayout(lamp_row)

        # Warp Block (red text)
        warp_row = QHBoxLayout()
        warp_row.setSpacing(12)

        # Warp Block icon
        warp_icon = QLabel()
        warp_icon.setPixmap(QIcon(str(fetchResource("assets/items/warpBlock.png"))).pixmap(24, 24))
        warp_icon.setStyleSheet("padding: 2px;")
        warp_row.addWidget(warp_icon)

        warp_label = BodyLabel("Warp Block:")
        warp_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px; color: red;")
        warp_row.addWidget(warp_label)

        self.warp_entry = LineEdit()
        self.warp_entry.setFixedWidth(60)
        warp_row.addWidget(self.warp_entry)

        warp_row.addStretch()
        group_layout.addLayout(warp_row)

        # Cellular Shopper (red text)
        shopper_row = QHBoxLayout()
        shopper_row.setSpacing(12)

        # Cellular Shopper icon
        shopper_icon = QLabel()
        shopper_icon.setPixmap(QIcon(str(fetchResource("assets/items/celluarShopper.png"))).pixmap(24, 24))
        shopper_icon.setStyleSheet("padding: 2px;")
        shopper_row.addWidget(shopper_icon)

        shopper_label = BodyLabel("Cellular Shopper:")
        shopper_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px; color: red;")
        shopper_row.addWidget(shopper_label)

        self.shopper_entry = LineEdit()
        self.shopper_entry.setFixedWidth(60)
        shopper_row.addWidget(self.shopper_entry)

        shopper_row.addStretch()
        group_layout.addLayout(shopper_row)

        # Bowser Phone
        phone_row = QHBoxLayout()
        phone_row.setSpacing(12)

        # Bowser Phone icon
        phone_icon = QLabel()
        phone_icon.setPixmap(QIcon(str(fetchResource("assets/items/bowserPhone.png"))).pixmap(24, 24))
        phone_icon.setStyleSheet("padding: 2px;")
        phone_row.addWidget(phone_icon)

        phone_label = BodyLabel("Bowser Phone:")
        phone_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px;")
        phone_row.addWidget(phone_label)

        self.phone_entry = LineEdit()
        self.phone_entry.setFixedWidth(60)
        phone_row.addWidget(self.phone_entry)

        phone_row.addStretch()
        group_layout.addLayout(phone_row)

        # Dueling Glove
        glove_row = QHBoxLayout()
        glove_row.setSpacing(12)

        # Dueling Glove icon
        glove_icon = QLabel()
        glove_icon.setPixmap(QIcon(str(fetchResource("assets/items/duelingGlove.png"))).pixmap(24, 24))
        glove_icon.setStyleSheet("padding: 2px;")
        glove_row.addWidget(glove_icon)

        glove_label = BodyLabel("Dueling Glove:")
        glove_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px;")
        glove_row.addWidget(glove_label)

        self.glove_entry = LineEdit()
        self.glove_entry.setFixedWidth(60)
        glove_row.addWidget(self.glove_entry)

        glove_row.addStretch()
        group_layout.addLayout(glove_row)

        # Lucky Lamp
        lucky_row = QHBoxLayout()
        lucky_row.setSpacing(12)

        # Lucky Lamp icon
        lucky_icon = QLabel()
        lucky_icon.setPixmap(QIcon(str(fetchResource("assets/items/luckyLamp.png"))).pixmap(24, 24))
        lucky_icon.setStyleSheet("padding: 2px;")
        lucky_row.addWidget(lucky_icon)

        lucky_label = BodyLabel("Lucky Lamp:")
        lucky_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px;")
        lucky_row.addWidget(lucky_label)

        self.lucky_entry = LineEdit()
        self.lucky_entry.setFixedWidth(60)
        lucky_row.addWidget(self.lucky_entry)

        lucky_row.addStretch()
        group_layout.addLayout(lucky_row)

        # Bowser Suit
        suit_row = QHBoxLayout()
        suit_row.setSpacing(12)

        # Bowser Suit icon
        suit_icon = QLabel()
        suit_icon.setPixmap(QIcon(str(fetchResource("assets/items/bowserSuit.png"))).pixmap(24, 24))
        suit_icon.setStyleSheet("padding: 2px;")
        suit_row.addWidget(suit_icon)

        suit_label = BodyLabel("Bowser Suit:")
        suit_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px;")
        suit_row.addWidget(suit_label)

        self.suit_entry = LineEdit()
        self.suit_entry.setFixedWidth(60)
        suit_row.addWidget(self.suit_entry)

        suit_row.addStretch()
        group_layout.addLayout(suit_row)

        # Boo Bell
        bell_row = QHBoxLayout()
        bell_row.setSpacing(12)

        # Boo Bell icon
        bell_icon = QLabel()
        bell_icon.setPixmap(QIcon(str(fetchResource("assets/items/booBell.png"))).pixmap(24, 24))
        bell_icon.setStyleSheet("padding: 2px;")
        bell_row.addWidget(bell_icon)

        bell_label = BodyLabel("Boo Bell:")
        bell_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px;")
        bell_row.addWidget(bell_label)

        self.bell_entry = LineEdit()
        self.bell_entry.setFixedWidth(60)
        bell_row.addWidget(self.bell_entry)

        bell_row.addStretch()
        group_layout.addLayout(bell_row)

        # Boo Repellent
        repellent_row = QHBoxLayout()
        repellent_row.setSpacing(12)

        # Boo Repellent icon
        repellent_icon = QLabel()
        repellent_icon.setPixmap(QIcon(str(fetchResource("assets/items/booRepellent.png"))).pixmap(24, 24))
        repellent_icon.setStyleSheet("padding: 2px;")
        repellent_row.addWidget(repellent_icon)

        repellent_label = BodyLabel("Boo Repellent:")
        repellent_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px;")
        repellent_row.addWidget(repellent_label)

        self.repellent_entry = LineEdit()
        self.repellent_entry.setFixedWidth(60)
        repellent_row.addWidget(self.repellent_entry)

        repellent_row.addStretch()
        group_layout.addLayout(repellent_row)

        # Item Bag
        bag_row = QHBoxLayout()
        bag_row.setSpacing(12)

        # Item Bag icon
        bag_icon = QLabel()
        bag_icon.setPixmap(QIcon(str(fetchResource("assets/items/itemBag3.png"))).pixmap(24, 24))
        bag_icon.setStyleSheet("padding: 2px;")
        bag_row.addWidget(bag_icon)

        bag_label = BodyLabel("Item Bag:")
        bag_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 100px;")
        bag_row.addWidget(bag_label)

        self.bag_entry = LineEdit()
        self.bag_entry.setFixedWidth(60)
        bag_row.addWidget(self.bag_entry)

        bag_row.addStretch()
        group_layout.addLayout(bag_row)

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
                glove_price = MockEntry(self.glove_entry.text())
                warp_price = MockEntry(self.warp_entry.text())
                golden_price = MockEntry(self.golden_entry.text())
                lamp_price = MockEntry(self.lamp_entry.text())

                # Call appropriate items event function based on game
                if 'itemsEvent_mp2' in globals():
                    itemsEvent_mp2(mushroom_price, key_price, chest_price, glove_price, warp_price, golden_price, lamp_price)
                else:
                    self.show_error("Items modification not available for Mario Party 2")
            elif self.game_id == "marioParty3":
                mushroom_price = MockEntry(self.mushroom_entry.text())
                key_price = MockEntry(self.key_entry.text())
                poison_price = MockEntry(self.poison_entry.text())
                reverse_price = MockEntry(self.reverse_entry.text())
                golden_price = MockEntry(self.golden_entry.text())
                lamp_price = MockEntry(self.lamp_entry.text())
                warp_price = MockEntry(self.warp_entry.text())
                shopper_price = MockEntry(self.shopper_entry.text())
                phone_price = MockEntry(self.phone_entry.text())
                glove_price = MockEntry(self.glove_entry.text())
                lucky_price = MockEntry(self.lucky_entry.text())
                suit_price = MockEntry(self.suit_entry.text())
                chest_price = MockEntry(self.chest_entry.text())
                bell_price = MockEntry(self.bell_entry.text())
                repellent_price = MockEntry(self.repellent_entry.text())
                bag_price = MockEntry(self.bag_entry.text())

                # Call appropriate items event function based on game
                if 'itemsEvent_mp3' in globals():
                    itemsEvent_mp3(mushroom_price, key_price, poison_price, reverse_price, golden_price, lamp_price, warp_price, shopper_price, phone_price, glove_price, lucky_price, suit_price, chest_price, bell_price, repellent_price, bag_price)
                else:
                    self.show_error("Items modification not available for Mario Party 3")
        except Exception as e:
            self.show_error(f"Error generating codes: {str(e)}")

    def show_error(self, message):
        """Show error message to user"""
        InfoBar.error(
            title="Error",
            content=message,
            orient=Qt.Horizontal,
            isClosable=True,
            position=InfoBarPosition.TOP,
            duration=3000,
            parent=self
        )
    
    def update_items_group_theme(self):
        """Update the items group styling based on current theme"""
        from qfluentwidgets import isDarkTheme
        if isDarkTheme():
            self.items_group.setStyleSheet("""
                QGroupBox {
                    font-size: 16px;
                    font-weight: 600;
                    color: palette(text);
                    border: 2px solid palette(mid);
                    border-radius: 8px;
                    margin-top: 12px;
                    padding-top: 12px;
                    background: #3c3c3c;
                }
                QGroupBox::title {
                    subcontrol-origin: margin;
                    left: 16px;
                    padding: 0 8px 0 8px;
                    background: palette(highlight);
                    color: palette(highlighted-text);
                    border-radius: 6px;
                    font-weight: 700;
                }
            """)
        else:
            self.items_group.setStyleSheet("""
                QGroupBox {
                    font-size: 16px;
                    font-weight: 600;
                    color: palette(text);
                    border: 2px solid palette(mid);
                    border-radius: 8px;
                    margin-top: 12px;
                    padding-top: 12px;
                    background: #ffffff;
                }
                QGroupBox::title {
                    subcontrol-origin: margin;
                    left: 16px;
                    padding: 0 8px 0 8px;
                    background: palette(highlight);
                    color: palette(highlighted-text);
                    border-radius: 6px;
                    font-weight: 700;
                }
            """)
    
    def themeChanged(self):
        """Called when theme changes - update all styling"""
        self.update_items_group_theme()
