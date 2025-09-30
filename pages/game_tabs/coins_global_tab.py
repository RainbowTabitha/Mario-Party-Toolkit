# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

# ============================================
# Coins Tab Component for Mario Party 2
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QMessageBox, QGroupBox
from PyQt5.QtCore import Qt
from PyQt5.QtGui import QPixmap
from qfluentwidgets import SubtitleLabel, BodyLabel, LineEdit, CheckBox, PushButton

# Import resource manager for images
from utils.resource_manager import ResourceManager

# Import coins event functions for MP1, MP2, MP3, MP4, and MP5
try:
    from events.marioParty1_coins import coinsEvent_mp1
    from events.marioParty2_coins import coinsEvent_mp2
    from events.marioParty3_coins import coinsEvent_mp3
    from events.marioParty4_coins import coinsEvent_mp4
    from events.marioParty5_coins import coinsEvent_mp5
    from events.marioParty6_coins import coinsEvent_mp6
    from events.marioParty7_coins import coinsEvent_mp7
    from events.marioParty8_coins import coinsEvent_mp8
except ImportError:
    pass


class CoinsTab(QWidget):
    def __init__(self, game_id, game_type="basic"):
        super().__init__()
        self.game_id = game_id
        self.game_type = game_type
        self.setup_ui()

    def setup_ui(self):
        """Set up the coins tab UI"""
        self.setObjectName(f"{self.game_id}CoinsTab")
        
        # Main layout
        layout = QVBoxLayout()
        layout.setSpacing(8)
        layout.setContentsMargins(16, 12, 16, 12)
        
        # Title
        title = SubtitleLabel("Coin Modifications")
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Description
        desc = BodyLabel("Modify coin values for different space types:")
        desc.setAlignment(Qt.AlignCenter)
        layout.addWidget(desc)
        
        # Coin Modifications Card with acrylic effect
        from qfluentwidgets import CardWidget
        card = CardWidget()
        
        # Store reference to card
        self.coins_group = card
        
        card_layout = QVBoxLayout()
        card_layout.setContentsMargins(20, 16, 20, 16)
        card_layout.setSpacing(16)
        
        # Add title to the card
        card_title = SubtitleLabel("Coin Modifications")
        card_title.setStyleSheet("font-size: 16px; font-weight: 600; margin-bottom: 8px;")
        card_layout.addWidget(card_title)
        
        card.setLayout(card_layout)
        
        # Use card_layout instead of group_layout for adding content
        group_layout = card_layout
        
        # Blue Space Row
        blue_row = QHBoxLayout()
        blue_row.setSpacing(12)
        
        # Add blue space image
        blue_image = self.create_image_label("assets/eventTags/blueSpace.png", 32, 32)
        blue_row.addWidget(blue_image)
        
        blue_label = BodyLabel("Blue Space:")
        blue_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
        blue_row.addWidget(blue_label)
        
        self.blue_entry = LineEdit()
        # Leave fields blank - users can fill in custom values
        self.blue_entry.setFixedWidth(60)
        blue_row.addWidget(self.blue_entry)
                
        # Only show "Double on Last 5" checkbox for MP1, MP2, MP3
        if self.game_id in ["marioParty1", "marioParty2", "marioParty3"]:
            self.blue_checkbox = CheckBox("Double on Last 5")
            blue_row.addWidget(self.blue_checkbox)
        
        blue_row.addStretch()
        group_layout.addLayout(blue_row)
        
        # Red Space Row
        red_row = QHBoxLayout()
        red_row.setSpacing(12)
        
        # Add red space image
        red_image = self.create_image_label("assets/eventTags/redSpace.png", 32, 32)
        red_row.addWidget(red_image)
        
        red_label = BodyLabel("Red Space:")
        red_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
        red_row.addWidget(red_label)
        
        self.red_entry = LineEdit()
        # Leave fields blank - users can fill in custom values
        self.red_entry.setFixedWidth(60)
        red_row.addWidget(self.red_entry)
        
        # Only show "Double on Last 5" checkbox for MP1, MP2, MP3
        if self.game_id in ["marioParty1", "marioParty2", "marioParty3"]:
            self.red_checkbox = CheckBox("Double on Last 5")
            red_row.addWidget(self.red_checkbox)
        
        red_row.addStretch()
        group_layout.addLayout(red_row)
        
        # Star Space Row
        star_row = QHBoxLayout()
        star_row.setSpacing(12)
        
        # Add star space image
        star_image = self.create_image_label("assets/eventTags/starSpace.png", 32, 32)
        star_row.addWidget(star_image)
        
        star_label = BodyLabel("Star Space:")
        star_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
        star_row.addWidget(star_label)
        
        self.star_entry = LineEdit()
        # Leave fields blank - users can fill in custom values

        self.star_entry.setFixedWidth(60)
        star_row.addWidget(self.star_entry)
                
        star_row.addStretch()
        group_layout.addLayout(star_row)
        
        # Koopa Bank Row (only for MP2/MP3)
        if self.game_id in ["marioParty2", "marioParty3", "marioParty5"]:
            koopa_row = QHBoxLayout()
            koopa_row.setSpacing(12)
            
            # Add koopa bank image
            koopa_image = self.create_image_label("assets/eventTags/koopaBank3.png", 32, 32)
            koopa_row.addWidget(koopa_image)
            
            koopa_label = BodyLabel("Koopa Bank:")
            koopa_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            koopa_row.addWidget(koopa_label)
            
            self.koopa_entry = LineEdit()
            # Leave fields blank - users can fill in custom values
            self.koopa_entry.setFixedWidth(60)
            koopa_row.addWidget(self.koopa_entry)
            
            koopa_row.addStretch()
            group_layout.addLayout(koopa_row)
        
        # Mario Party 3 specific fields
        if self.game_id == "marioParty3":
            # Boo Coins Row
            boo_coins_row = QHBoxLayout()
            boo_coins_row.setSpacing(12)
            
            # Add boo coins image
            boo_coins_image = self.create_image_label("assets/eventTags/booHouseCoins.png", 32, 32)
            boo_coins_row.addWidget(boo_coins_image)
            
            boo_coins_label = BodyLabel("Boo Coins:")
            boo_coins_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            boo_coins_row.addWidget(boo_coins_label)
            
            self.boo_coins_entry = LineEdit()
            # Leave fields blank - users can fill in custom values

            self.boo_coins_entry.setFixedWidth(60)
            boo_coins_row.addWidget(self.boo_coins_entry)
            
            boo_coins_row.addStretch()
            group_layout.addLayout(boo_coins_row)
            
            # Boo Stars Row
            boo_stars_row = QHBoxLayout()
            boo_stars_row.setSpacing(12)
            
            # Add boo stars image
            boo_stars_image = self.create_image_label("assets/eventTags/booHouseStars.png", 32, 32)
            boo_stars_row.addWidget(boo_stars_image)
            
            boo_stars_label = BodyLabel("Boo Stars:")
            boo_stars_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            boo_stars_row.addWidget(boo_stars_label)
            
            self.boo_stars_entry = LineEdit()
            # Leave fields blank - users can fill in custom values

            self.boo_stars_entry.setFixedWidth(60)
            boo_stars_row.addWidget(self.boo_stars_entry)
            
            boo_stars_row.addStretch()
            group_layout.addLayout(boo_stars_row)
        
        # Additional coin mods for MP2+
        if self.game_type != "basic" or self.game_id in ["marioParty2", "marioParty3", "marioParty4", "marioParty5", "marioParty6", "marioParty7", "marioParty8", "marioParty9", "marioPartyDS"]:
            # Minigame Win Row
            mg_row = QHBoxLayout()
            mg_row.setSpacing(12)
            
            # Add minigame image
            mg_image = self.create_image_label("assets/eventTags/miniGame.png", 32, 32)
            mg_row.addWidget(mg_image)
            
            mg_label = BodyLabel("Minigame Win:")
            mg_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            mg_row.addWidget(mg_label)
            
            self.mg_entry = LineEdit()
            # Leave fields blank - users can fill in custom values

            self.mg_entry.setFixedWidth(60)
            mg_row.addWidget(self.mg_entry)
            
            mg_row.addStretch()
            group_layout.addLayout(mg_row)
            
            # Initial Coins Row
            initial_row = QHBoxLayout()
            initial_row.setSpacing(12)
            
            # Add initial coins image
            initial_image = self.create_image_label("assets/eventTags/initialCoins.png", 32, 32)
            initial_row.addWidget(initial_image)
            
            initial_label = BodyLabel("Initial Coins:")
            initial_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            initial_row.addWidget(initial_label)
            
            self.initial_entry = LineEdit()
            # Leave fields blank - users can fill in custom values

            self.initial_entry.setFixedWidth(60)
            initial_row.addWidget(self.initial_entry)
            
            initial_row.addStretch()
            group_layout.addLayout(initial_row)
        
        # Mario Party 4 specific fields
        if self.game_id == "marioParty4":
            # Mega Mushroom Row
            mega_row = QHBoxLayout()
            mega_row.setSpacing(12)
            
            mega_image = self.create_image_label("assets/items/megaMushroom.png", 32, 32)
            mega_row.addWidget(mega_image)
            
            mega_label = BodyLabel("Mega Mushroom:")
            mega_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            mega_row.addWidget(mega_label)
            
            self.mega_entry = LineEdit()

            self.mega_entry.setFixedWidth(60)
            mega_row.addWidget(self.mega_entry)
            
            mega_row.addStretch()
            group_layout.addLayout(mega_row)
            
            # Bowser Suit Row
            bowser_row = QHBoxLayout()
            bowser_row.setSpacing(12)
            
            bowser_image = self.create_image_label("assets/items/bowserSuit4.png", 32, 32)
            bowser_row.addWidget(bowser_image)
            
            bowser_label = BodyLabel("Bowser Suit:")
            bowser_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            bowser_row.addWidget(bowser_label)
            
            self.bowser_entry = LineEdit()
            self.bowser_entry.setFixedWidth(60)
            bowser_row.addWidget(self.bowser_entry)
            
            bowser_row.addStretch()
            group_layout.addLayout(bowser_row)
            
            # Lottery Row
            lottery_row = QHBoxLayout()
            lottery_row.setSpacing(12)
            
            lottery_image = self.create_image_label("assets/eventTags/lottery4.png", 32, 32)
            lottery_row.addWidget(lottery_image)
            
            lottery_label = BodyLabel("Lottery:")
            lottery_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            lottery_row.addWidget(lottery_label)
            
            self.lottery_entry = LineEdit()
            self.lottery_entry.setFixedWidth(60)
            lottery_row.addWidget(self.lottery_entry)
            
            lottery_row.addStretch()
            group_layout.addLayout(lottery_row)
            
            # Boo Star Steal Price Row
            boo_star_row = QHBoxLayout()
            boo_star_row.setSpacing(12)
            
            boo_star_image = self.create_image_label("assets/eventTags/booHouseStars.png", 32, 32)
            boo_star_row.addWidget(boo_star_image)
            
            boo_star_label = BodyLabel("Boo Star Steal:")
            boo_star_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            boo_star_row.addWidget(boo_star_label)
            
            self.boo_star_entry = LineEdit()
            self.boo_star_entry.setFixedWidth(60)
            boo_star_row.addWidget(self.boo_star_entry)
            
            boo_star_row.addStretch()
            group_layout.addLayout(boo_star_row)
            
            # Boo Coin Steal Price Row
            boo_coins_row = QHBoxLayout()
            boo_coins_row.setSpacing(12)
            
            boo_coins_image = self.create_image_label("assets/eventTags/booHouseCoins.png", 32, 32)
            boo_coins_row.addWidget(boo_coins_image)
            
            boo_coins_label = BodyLabel("Boo Coin Steal:")
            boo_coins_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            boo_coins_row.addWidget(boo_coins_label)
            
            self.boo_coins_entry = LineEdit()
            self.boo_coins_entry.setFixedWidth(60)
            boo_coins_row.addWidget(self.boo_coins_entry)
            
            boo_coins_row.addStretch()
            group_layout.addLayout(boo_coins_row)
            
            # Boo Minimum Coins Row
            boo_minimum_row = QHBoxLayout()
            boo_minimum_row.setSpacing(12)
            
            boo_minimum_image = self.create_image_label("assets/eventTags/booHouseCoins.png", 32, 32)
            boo_minimum_row.addWidget(boo_minimum_image)
            
            boo_minimum_label = BodyLabel("Boo Min Coins:")
            boo_minimum_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            boo_minimum_row.addWidget(boo_minimum_label)
            
            self.boo_minimum_entry = LineEdit()
            self.boo_minimum_entry.setFixedWidth(60)
            boo_minimum_row.addWidget(self.boo_minimum_entry)
            
            boo_minimum_row.addStretch()
            group_layout.addLayout(boo_minimum_row)
        
        # Mario Party 5 specific fields
        if self.game_id == "marioParty5":
            # Wiggler Row
            wiggler_row = QHBoxLayout()
            wiggler_row.setSpacing(12)
            
            wiggler_image = self.create_image_label("assets/eventTags/wigglerCapsule.png", 32, 32)
            wiggler_row.addWidget(wiggler_image)
            
            wiggler_label = BodyLabel("Wiggler:")
            wiggler_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            wiggler_row.addWidget(wiggler_label)
            
            self.wiggler_entry = LineEdit()
            self.wiggler_entry.setFixedWidth(60)
            wiggler_row.addWidget(self.wiggler_entry)
            
            wiggler_row.addStretch()
            group_layout.addLayout(wiggler_row)
            
            # Chain Chomp Row
            chomp_row = QHBoxLayout()
            chomp_row.setSpacing(12)
            
            chomp_image = self.create_image_label("assets/eventTags/chainChomp.png", 32, 32)
            chomp_row.addWidget(chomp_image)
            
            chomp_label = BodyLabel("Chain Chomp:")
            chomp_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            chomp_row.addWidget(chomp_label)
            
            self.chomp_entry = LineEdit()
            self.chomp_entry.setFixedWidth(60)
            chomp_row.addWidget(self.chomp_entry)
            
            chomp_row.addStretch()
            group_layout.addLayout(chomp_row)

            # Chain Chomp Min Steal (base) Row
            chomp_min_row = QHBoxLayout()
            chomp_min_row.setSpacing(12)

            chomp_min_image = self.create_image_label("assets/eventTags/chainChomp.png", 32, 32)
            chomp_min_row.addWidget(chomp_min_image)

            chomp_min_label = BodyLabel("Chomp Min (Coins):")
            chomp_min_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            chomp_min_row.addWidget(chomp_min_label)

            self.chomp_min_entry = LineEdit()
            self.chomp_min_entry.setFixedWidth(60)
            chomp_min_row.addWidget(self.chomp_min_entry)

            chomp_min_row.addStretch()
            group_layout.addLayout(chomp_min_row)
        
        # Mario Party 6 specific fields
        if self.game_id == "marioParty6":
            # Character Space Row
            character_row = QHBoxLayout()
            character_row.setSpacing(12)
            
            character_image = self.create_image_label("assets/eventTags/characterSpace.png", 32, 32)
            character_row.addWidget(character_image)
            
            character_label = BodyLabel("Character Space:")
            character_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            character_row.addWidget(character_label)
            
            self.character_entry = LineEdit()
            self.character_entry.setFixedWidth(60)
            character_row.addWidget(self.character_entry)
            
            character_row.addStretch()
            group_layout.addLayout(character_row)
            
            # Pink Boo Coins Row
            pink_boo_coins_row = QHBoxLayout()
            pink_boo_coins_row.setSpacing(12)
            
            pink_boo_coins_image = self.create_image_label("assets/eventTags/pinkBooCoins.png", 32, 32)
            pink_boo_coins_row.addWidget(pink_boo_coins_image)
            
            pink_boo_coins_label = BodyLabel("Pink Boo Coins:")
            pink_boo_coins_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            pink_boo_coins_row.addWidget(pink_boo_coins_label)
            
            self.pink_boo_coins_entry = LineEdit()
            self.pink_boo_coins_entry.setFixedWidth(60)
            pink_boo_coins_row.addWidget(self.pink_boo_coins_entry)
            
            pink_boo_coins_row.addStretch()
            group_layout.addLayout(pink_boo_coins_row)
            
            # Pink Boo Minimum Row
            pink_boo_min_row = QHBoxLayout()
            pink_boo_min_row.setSpacing(12)
            
            pink_boo_min_image = self.create_image_label("assets/eventTags/pinkBooCoins.png", 32, 32)
            pink_boo_min_row.addWidget(pink_boo_min_image)
            
            pink_boo_min_label = BodyLabel("Pink Boo Min:")
            pink_boo_min_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            pink_boo_min_row.addWidget(pink_boo_min_label)
            
            self.pink_boo_min_entry = LineEdit()
            self.pink_boo_min_entry.setFixedWidth(60)
            pink_boo_min_row.addWidget(self.pink_boo_min_entry)
            
            pink_boo_min_row.addStretch()
            group_layout.addLayout(pink_boo_min_row)
            
            # Pink Boo Stars Row
            pink_boo_stars_row = QHBoxLayout()
            pink_boo_stars_row.setSpacing(12)
            
            pink_boo_stars_image = self.create_image_label("assets/eventTags/pinkBooStars.png", 32, 32)
            pink_boo_stars_row.addWidget(pink_boo_stars_image)
            
            pink_boo_stars_label = BodyLabel("Pink Boo Stars:")
            pink_boo_stars_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            pink_boo_stars_row.addWidget(pink_boo_stars_label)
            
            self.pink_boo_stars_entry = LineEdit()
            self.pink_boo_stars_entry.setFixedWidth(60)
            pink_boo_stars_row.addWidget(self.pink_boo_stars_entry)
            
            pink_boo_stars_row.addStretch()
            group_layout.addLayout(pink_boo_stars_row)
            
            # Zap Orb Row
            zap_row = QHBoxLayout()
            zap_row.setSpacing(12)
            
            zap_image = self.create_image_label("assets/items/zapCapsule.png", 32, 32)
            zap_row.addWidget(zap_image)
            
            zap_label = BodyLabel("Zap Orb:")
            zap_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            zap_row.addWidget(zap_label)
            
            self.zap_entry = LineEdit()
            self.zap_entry.setFixedWidth(60)
            zap_row.addWidget(self.zap_entry)
            
            zap_row.addStretch()
            group_layout.addLayout(zap_row)
        
        # Mario Party 7 specific fields
        if self.game_id == "marioParty7":
            # Character Space Row
            character_row = QHBoxLayout()
            character_row.setSpacing(12)
            
            character_image = self.create_image_label("assets/eventTags/characterSpace7.png", 32, 32)
            character_row.addWidget(character_image)
            
            character_label = BodyLabel("Character Space:")
            character_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            character_row.addWidget(character_label)
            
            self.character_entry = LineEdit()
            self.character_entry.setFixedWidth(60)
            character_row.addWidget(self.character_entry)
            
            character_row.addStretch()
            group_layout.addLayout(character_row)
            
            # Star Last 5 Row
            star_last5_row = QHBoxLayout()
            star_last5_row.setSpacing(12)
            
            star_last5_image = self.create_image_label("assets/eventTags/starSpace.png", 32, 32)
            star_last5_row.addWidget(star_last5_image)
            
            star_last5_label = BodyLabel("Star Last 5:")
            star_last5_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            star_last5_row.addWidget(star_last5_label)
            
            self.star_last5_entry = LineEdit()
            self.star_last5_entry.setFixedWidth(60)
            star_last5_row.addWidget(self.star_last5_entry)
            
            star_last5_row.addStretch()
            group_layout.addLayout(star_last5_row)
            
            # Hammer Bro Row
            hammer_bro_row = QHBoxLayout()
            hammer_bro_row.setSpacing(12)
            
            hammer_bro_image = self.create_image_label("assets/items/hammerBroCapsule.png", 32, 32)
            hammer_bro_row.addWidget(hammer_bro_image)
            
            hammer_bro_label = BodyLabel("Hammer Bro:")
            hammer_bro_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            hammer_bro_row.addWidget(hammer_bro_label)
            
            self.hammer_bro_entry = LineEdit()
            self.hammer_bro_entry.setFixedWidth(60)
            hammer_bro_row.addWidget(self.hammer_bro_entry)
            
            hammer_bro_row.addStretch()
            group_layout.addLayout(hammer_bro_row)
            
            # Zap Orb Row
            zap_row = QHBoxLayout()
            zap_row.setSpacing(12)
            
            zap_image = self.create_image_label("assets/items/zapCapsule.png", 32, 32)
            zap_row.addWidget(zap_image)
            
            zap_label = BodyLabel("Zap Orb:")
            zap_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            zap_row.addWidget(zap_label)
            
            self.zap_entry = LineEdit()
            self.zap_entry.setFixedWidth(60)
            zap_row.addWidget(self.zap_entry)
            
            zap_row.addStretch()
            group_layout.addLayout(zap_row)
            
            # Fireball Row
            fireball_row = QHBoxLayout()
            fireball_row.setSpacing(12)
            
            fireball_image = self.create_image_label("assets/items/fireballCapsule.png", 32, 32)
            fireball_row.addWidget(fireball_image)
            
            fireball_label = BodyLabel("Fireball:")
            fireball_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            fireball_row.addWidget(fireball_label)
            
            self.fireball_entry = LineEdit()
            self.fireball_entry.setFixedWidth(60)
            fireball_row.addWidget(self.fireball_entry)
            
            fireball_row.addStretch()
            group_layout.addLayout(fireball_row)
            
            # Vacuum Row
            vacuum_row = QHBoxLayout()
            vacuum_row.setSpacing(12)
            
            vacuum_image = self.create_image_label("assets/items/vacuumCapsule.png", 32, 32)
            vacuum_row.addWidget(vacuum_image)
            
            vacuum_label = BodyLabel("Vacuum:")
            vacuum_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            vacuum_row.addWidget(vacuum_label)
            
            self.vacuum_entry = LineEdit()
            self.vacuum_entry.setFixedWidth(60)
            vacuum_row.addWidget(self.vacuum_entry)
            
            vacuum_row.addStretch()
            group_layout.addLayout(vacuum_row)
            
            # Flower Row
            flower_row = QHBoxLayout()
            flower_row.setSpacing(12)
            
            flower_image = self.create_image_label("assets/items/flowerCapsule.png", 32, 32)
            flower_row.addWidget(flower_image)
            
            flower_label = BodyLabel("Flower:")
            flower_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            flower_row.addWidget(flower_label)
            
            self.flower_entry = LineEdit()
            self.flower_entry.setFixedWidth(60)
            flower_row.addWidget(self.flower_entry)
            
            flower_row.addStretch()
            group_layout.addLayout(flower_row)

        # Mario Party 8 specific fields
        if self.game_id == "marioParty8":
            # Bitsize Row
            bitsize_row = QHBoxLayout()
            bitsize_row.setSpacing(12)
            
            bitsize_image = self.create_image_label("assets/eventTags/bitsizeCandy.png", 32, 32)
            bitsize_row.addWidget(bitsize_image)
            
            bitsize_label = BodyLabel("Bitsize:")
            bitsize_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            bitsize_row.addWidget(bitsize_label)
            
            self.bitsize_entry = LineEdit()
            self.bitsize_entry.setFixedWidth(60)
            bitsize_row.addWidget(self.bitsize_entry)
            
            bitsize_row.addStretch()
            group_layout.addLayout(bitsize_row)
            
            # Bowlo Row
            bowlo_row = QHBoxLayout()
            bowlo_row.setSpacing(12)
            
            bowlo_image = self.create_image_label("assets/eventTags/bowloCandy.png", 32, 32)
            bowlo_row.addWidget(bowlo_image)
            
            bowlo_label = BodyLabel("Bowlo:")
            bowlo_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            bowlo_row.addWidget(bowlo_label)
            
            self.bowlo_entry = LineEdit()
            self.bowlo_entry.setFixedWidth(60)
            bowlo_row.addWidget(self.bowlo_entry)
            
            bowlo_row.addStretch()
            group_layout.addLayout(bowlo_row)
            
            # Vampire Row
            vampire_row = QHBoxLayout()
            vampire_row.setSpacing(12)
            
            vampire_image = self.create_image_label("assets/eventTags/vampireCandy.png", 32, 32)
            vampire_row.addWidget(vampire_image)
            
            vampire_label = BodyLabel("Vampire:")
            vampire_label.setStyleSheet("font-size: 15px; font-weight: 600; min-width: 80px;")
            vampire_row.addWidget(vampire_label)
            
            self.vampire_entry = LineEdit()
            self.vampire_entry.setFixedWidth(60)
            vampire_row.addWidget(self.vampire_entry)
            
            vampire_row.addStretch()
            group_layout.addLayout(vampire_row)
            
        
        layout.addWidget(card)
        
        # Generate button with reduced margins
        generate_btn = PushButton("Generate Codes")
        generate_btn.clicked.connect(self.generate_codes)
        layout.addWidget(generate_btn)
        
        # Add stretch to push everything up
        layout.addStretch()
        
        self.setLayout(layout)

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
        """Generate codes for the current game"""
        if self.game_id == "marioParty1":
            try:
                if 'coinsEvent_mp1' in globals():
                    # Create mock objects to match the expected interface
                    class MockEntry:
                        def __init__(self, text):
                            self._text = text
                        def get(self):
                            return self._text
                        def text(self):
                            return self._text
                    
                    class MockCheckBox:
                        def __init__(self, checked):
                            self._checked = checked
                        def get(self):
                            return self._checked
                        def isChecked(self):
                            return self._checked
                    
                    # Create mock objects with current values
                    blue_amount = MockEntry(self.blue_entry.text())
                    blue_tick = MockCheckBox(self.blue_checkbox.isChecked())
                    red_amount = MockEntry(self.red_entry.text())
                    red_tick = MockCheckBox(self.red_checkbox.isChecked())
                    star_amount = MockEntry(self.star_entry.text())
                    
                    coinsEvent_mp1(blue_amount, blue_tick, red_amount, red_tick, star_amount)
                else:
                    self.show_error("Mario Party 1 coins modification not available")
            except Exception as e:
                self.show_error(f"Error generating codes: {str(e)}")
        elif self.game_id == "marioParty2":
            try:
                if 'coinsEvent_mp2' in globals():
                    # Create mock objects to match the expected interface
                    class MockEntry:
                        def __init__(self, text):
                            self._text = text
                        def get(self):
                            return self._text
                        def text(self):
                            return self._text
                    
                    class MockCheckBox:
                        def __init__(self, checked):
                            self._checked = checked
                        def get(self):
                            return self._checked
                        def isChecked(self):
                            return self._checked
                    
                    # Create mock objects with current values
                    blue_amount = MockEntry(self.blue_entry.text())
                    blue_tick = MockCheckBox(self.blue_checkbox.isChecked())
                    red_amount = MockEntry(self.red_entry.text())
                    red_tick = MockCheckBox(self.red_checkbox.isChecked())
                    star_amount = MockEntry(self.star_entry.text())
                    
                    # Only include koopa_amount if koopa_entry exists
                    koopa_amount = MockEntry(self.koopa_entry.text()) if hasattr(self, 'koopa_entry') else MockEntry("5")
                    
                    # Include new fields if they exist
                    mg_amount = MockEntry(self.mg_entry.text()) if hasattr(self, 'mg_entry') else MockEntry("10")
                    initial_amount = MockEntry(self.initial_entry.text()) if hasattr(self, 'initial_entry') else MockEntry("10")
                    
                    coinsEvent_mp2(blue_amount, blue_tick, red_amount, red_tick, star_amount, koopa_amount)
                else:
                    self.show_error("Mario Party 2 coins modification not available")
            except Exception as e:
                self.show_error(f"Error generating codes: {str(e)}")
        elif self.game_id == "marioParty3":
            try:
                if 'coinsEvent_mp3' in globals():
                    # Create mock objects to match the expected interface
                    class MockEntry:
                        def __init__(self, text):
                            self._text = text
                        def get(self):
                            return self._text
                        def text(self):
                            return self._text
                    
                    class MockCheckBox:
                        def __init__(self, checked):
                            self._checked = checked
                        def get(self):
                            return self._checked
                        def isChecked(self):
                            return self._checked
                    
                    # Create mock objects with current values
                    blue_amount = MockEntry(self.blue_entry.text())
                    blue_tick = MockCheckBox(self.blue_checkbox.isChecked())
                    red_amount = MockEntry(self.red_entry.text())
                    red_tick = MockCheckBox(self.red_checkbox.isChecked())
                    star_amount = MockEntry(self.star_entry.text())
                    koopa_amount = MockEntry(self.koopa_entry.text()) if hasattr(self, 'koopa_entry') else MockEntry("5")
                    boo_coins = MockEntry(self.boo_coins_entry.text()) if hasattr(self, 'boo_coins_entry') else MockEntry("10")
                    boo_stars = MockEntry(self.boo_stars_entry.text()) if hasattr(self, 'boo_stars_entry') else MockEntry("15")
                    
                    # Include new fields if they exist
                    mg_amount = MockEntry(self.mg_entry.text()) if hasattr(self, 'mg_entry') else MockEntry("10")
                    initial_amount = MockEntry(self.initial_entry.text()) if hasattr(self, 'initial_entry') else MockEntry("10")
                    
                    coinsEvent_mp3(blue_amount, blue_tick, red_amount, red_tick, star_amount, boo_coins, boo_stars, koopa_amount)
                else:
                    self.show_error("Mario Party 3 coins modification not available")
            except Exception as e:
                self.show_error(f"Error generating codes: {str(e)}")
        elif self.game_id == "marioParty4":
            try:
                if 'coinsEvent_mp4' in globals():
                    # Create mock objects to match the expected interface
                    class MockEntry:
                        def __init__(self, text):
                            self._text = text
                        def get(self):
                            return self._text
                        def text(self):
                            return self._text
                    
                    class MockCheckBox:
                        def __init__(self, checked):
                            self._checked = checked
                        def get(self):
                            return self._checked
                        def isChecked(self):
                            return self._checked
                    
                    # Create mock objects with current values
                    blue_amount = MockEntry(self.blue_entry.text())
                    red_amount = MockEntry(self.red_entry.text())
                    mg_amount = MockEntry(self.mg_entry.text()) if hasattr(self, 'mg_entry') else MockEntry("10")
                    star_amount = MockEntry(self.star_entry.text())
                    mega_amount = MockEntry(self.mega_entry.text()) if hasattr(self, 'mega_entry') else MockEntry("20")
                    boo_star_amount = MockEntry(self.boo_star_entry.text()) if hasattr(self, 'boo_star_entry') else MockEntry("15")
                    boo_coins_amount = MockEntry(self.boo_coins_entry.text()) if hasattr(self, 'boo_coins_entry') else MockEntry("10")
                    lottery_amount = MockEntry(self.lottery_entry.text()) if hasattr(self, 'lottery_entry') else MockEntry("50")
                    boo_minimum_amount = MockEntry(self.boo_minimum_entry.text()) if hasattr(self, 'boo_minimum_entry') else MockEntry("5")
                    bowser_amount = MockEntry(self.bowser_entry.text()) if hasattr(self, 'bowser_entry') else MockEntry("30")
                    initial_amount = MockEntry(self.initial_entry.text()) if hasattr(self, 'initial_entry') else MockEntry("10")
                    
                    coinsEvent_mp4(blue_amount, red_amount, mg_amount, star_amount, mega_amount, boo_star_amount, boo_coins_amount, lottery_amount, boo_minimum_amount, bowser_amount, initial_amount)
                else:
                    self.show_error("Mario Party 4 coins modification not available")
            except Exception as e:
                self.show_error(f"Error generating codes: {str(e)}")
        elif self.game_id == "marioParty5":
            try:
                if 'coinsEvent_mp5' in globals():
                    class MockEntry:
                        def __init__(self, text):
                            self._text = text
                        def get(self):
                            return self._text
                        def text(self):
                            return self._text

                    # Create mock objects with current values
                    blue_amount = MockEntry(self.blue_entry.text())
                    red_amount = MockEntry(self.red_entry.text())
                    mg_amount = MockEntry(self.mg_entry.text() if hasattr(self, 'mg_entry') else "")
                    star_amount = MockEntry(self.star_entry.text())
                    wiggler_amount = MockEntry(self.wiggler_entry.text() if hasattr(self, 'wiggler_entry') else "")
                    chomp_star_amount = MockEntry(self.chomp_entry.text() if hasattr(self, 'chomp_entry') else "")
                    chomp_weight_amount = MockEntry(self.chomp_min_entry.text() if hasattr(self, 'chomp_min_entry') else "")
                    koopa_amount = MockEntry(self.koopa_entry.text() if hasattr(self, 'koopa_entry') else "")
                    initial_amount = MockEntry(self.initial_entry.text() if hasattr(self, 'initial_entry') else "")

                    coinsEvent_mp5(
                        blue_amount,
                        red_amount,
                        mg_amount,
                        star_amount,
                        wiggler_amount,
                        chomp_star_amount,
                        chomp_weight_amount,
                        koopa_amount,
                        initial_amount
                    )
                else:
                    self.show_error("Mario Party 5 coins modification not available")
            except Exception as e:
                self.show_error(f"Error generating codes: {str(e)}")
        elif self.game_id == "marioParty6":
            try:
                if 'coinsEvent_mp6' in globals():
                    # Create mock objects to match the expected interface
                    class MockEntry:
                        def __init__(self, text):
                            self._text = text
                        def get(self):
                            return self._text
                        def text(self):
                            return self._text
                    
                    # Create mock objects with current values
                    blue_amount = MockEntry(self.blue_entry.text())
                    red_amount = MockEntry(self.red_entry.text())
                    character_amount = MockEntry(self.character_entry.text() if hasattr(self, 'character_entry') else "")
                    mg_amount = MockEntry(self.mg_entry.text() if hasattr(self, 'mg_entry') else "")
                    star_amount = MockEntry(self.star_entry.text())
                    pink_boo_coins_amount = MockEntry(self.pink_boo_coins_entry.text() if hasattr(self, 'pink_boo_coins_entry') else "")
                    pink_boo_min_amount = MockEntry(self.pink_boo_min_entry.text() if hasattr(self, 'pink_boo_min_entry') else "")
                    pink_boo_stars_amount = MockEntry(self.pink_boo_stars_entry.text() if hasattr(self, 'pink_boo_stars_entry') else "")
                    initial_amount = MockEntry(self.initial_entry.text() if hasattr(self, 'initial_entry') else "")
                    zap_amount = MockEntry(self.zap_entry.text() if hasattr(self, 'zap_entry') else "")

                    coinsEvent_mp6(
                        blue_amount,
                        red_amount,
                        character_amount,
                        mg_amount,
                        star_amount,
                        pink_boo_coins_amount,
                        pink_boo_min_amount,
                        pink_boo_stars_amount,
                        initial_amount,
                        zap_amount
                    )
                else:
                    self.show_error("Mario Party 6 coins modification not available")
            except Exception as e:
                self.show_error(f"Error generating codes: {str(e)}")
        elif self.game_id == "marioParty7":
            try:
                if 'coinsEvent_mp7' in globals():
                    # Create mock objects to match the expected interface
                    class MockEntry:
                        def __init__(self, text):
                            self._text = text
                        def get(self):
                            return self._text
                        def text(self):
                            return self._text
                    
                    # Create mock objects with current values
                    blue_amount = MockEntry(self.blue_entry.text())
                    red_amount = MockEntry(self.red_entry.text())
                    character_amount = MockEntry(self.character_entry.text() if hasattr(self, 'character_entry') else "")
                    mg_amount = MockEntry(self.mg_entry.text() if hasattr(self, 'mg_entry') else "")
                    star_amount = MockEntry(self.star_entry.text())
                    star_last5_amount = MockEntry(self.star_last5_entry.text() if hasattr(self, 'star_last5_entry') else "")
                    hammer_bro_amount = MockEntry(self.hammer_bro_entry.text() if hasattr(self, 'hammer_bro_entry') else "")
                    zap_amount = MockEntry(self.zap_entry.text() if hasattr(self, 'zap_entry') else "")
                    fireball_amount = MockEntry(self.fireball_entry.text() if hasattr(self, 'fireball_entry') else "")
                    vacuum_amount = MockEntry(self.vacuum_entry.text() if hasattr(self, 'vacuum_entry') else "")
                    flower_amount = MockEntry(self.flower_entry.text() if hasattr(self, 'flower_entry') else "")
                    initial_amount = MockEntry(self.initial_entry.text() if hasattr(self, 'initial_entry') else "")

                    coinsEvent_mp7(
                        blue_amount,
                        red_amount,
                        character_amount,
                        mg_amount,
                        star_amount,
                        star_last5_amount,
                        hammer_bro_amount,
                        zap_amount,
                        fireball_amount,
                        vacuum_amount,
                        flower_amount,
                        initial_amount
                    )
                else:
                    self.show_error("Mario Party 7 coins modification not available")
            except Exception as e:
                self.show_error(f"Error generating codes: {str(e)}")
        elif self.game_id == "marioParty8":
            try:
                if 'coinsEvent_mp8' in globals():
                    # Create mock objects to match the expected interface
                    class MockEntry:
                        def __init__(self, text):
                            self._text = text
                        def get(self):
                            return self._text
                        def text(self):
                            return self._text
                    
                    # Create mock objects with current values
                    blue_amount = MockEntry(self.blue_entry.text())
                    red_amount = MockEntry(self.red_entry.text())
                    mg_amount = MockEntry(self.mg_entry.text() if hasattr(self, 'mg_entry') else "")
                    star_amount = MockEntry(self.star_entry.text())
                    bitsize_amount = MockEntry(self.bitsize_entry.text() if hasattr(self, 'bitsize_entry') else "")
                    bowlo_amount = MockEntry(self.bowlo_entry.text() if hasattr(self, 'bowlo_entry') else "")
                    vampire_amount = MockEntry(self.vampire_entry.text() if hasattr(self, 'vampire_entry') else "")

                    coinsEvent_mp8(
                        blue_amount,
                        red_amount,
                        mg_amount,
                        star_amount,
                        bitsize_amount,
                        bowlo_amount,
                        vampire_amount
                    )
                else:
                    self.show_error("Mario Party 8 coins modification not available")
            except Exception as e:
                self.show_error(f"Error generating codes: {str(e)}")
        else:
            self.show_error(f"Coins modification not supported for {self.game_id}")
    
    def show_error(self, message):
        """Show error message to user"""
        QMessageBox.critical(self, "Error", message)
    
    def update_coins_group_theme(self):
        """Update the coins group styling based on current theme"""
        from qfluentwidgets import isDarkTheme
        if isDarkTheme():
            self.coins_group.setStyleSheet("""
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
            self.coins_group.setStyleSheet("""
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
        self.update_coins_group_theme()
