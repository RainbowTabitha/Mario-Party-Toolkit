#!/usr/bin/env python3
# ============================================
# Mario Party Pages Factory
# Creates game-specific pages with modification tabs
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QTabWidget, QSizePolicy
from PyQt5.QtCore import Qt
from qfluentwidgets import BodyLabel

from pages.game_tabs.coins_global_tab import CoinsTab
from pages.game_tabs.block_weights_mp1_tab import BlockWeightsTab
from pages.game_tabs.minigame_global_tab import MinigameTab
from pages.game_tabs.handicap_global_tab import HandicapTab
from pages.game_tabs.shop_mp2_mp3_tab import ItemsTab
from pages.game_tabs.item_replace_global_tab import ItemReplaceTab
from pages.game_tabs.bonus_star_global_tab import BonusStarTab
from pages.game_tabs.shop_mp4_prices_tab import ShopPricesTab
from pages.game_tabs.shop_mp4_odds_tab import ShopOddsTab
from pages.game_tabs.inital_items_global_tab import InitialItemsTab
from pages.game_tabs.item_bag_mp4_tab import ItemBagTab
from pages.game_tabs.space_replacement_global_tab import SpaceReplacementTab
from pages.game_tabs.lottery_rewards_mp4_tab import LotteryRewardsTab
from pages.game_tabs.capsule_mods_mp5_tab import CapsuleModsMp5Tab
from pages.game_tabs.board_specific_mp5_tab import BoardSpecificMp5Tab
from pages.game_tabs.battle_minigame_global_tab import BattleMinigameTab


class MarioPartyPages:
    def __init__(self):
        self.tab_factories = {
            'marioParty1': self.create_mp1_tabs,
            'marioParty2': self.create_mp2_tabs,
            'marioParty3': self.create_mp3_tabs,
            'marioParty4': self.create_mp4_tabs,
            'marioParty5': self.create_mp5_tabs,
            'marioParty6': self.create_mp6_tabs,
            'marioParty7': self.create_mp7_tabs,
            'marioParty8': self.create_mp8_tabs,
            'marioParty9': self.create_mp9_tabs,
            'marioPartyDS': self.create_mpds_tabs,
        }
        
        # Store references to all tabs for theme updates
        self.all_tabs = []

    def create_game_page(self, game_id, game_name):
        """Create a page for a specific Mario Party game"""
        page = QWidget()
        page.setObjectName(f"{game_id}Page")
        layout = QVBoxLayout(page)
        layout.setContentsMargins(32, 32, 32, 32)
        layout.setSpacing(20)
        
        # Set size policy for the page to allow resizing
        page.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        # Create tab widget with modern styling
        tab_widget = QTabWidget()
        tab_widget.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        # Style the tab widget with consistent gray theme
        tab_widget.setStyleSheet(self.get_tab_stylesheet())
        layout.addWidget(tab_widget)
        
        # Create tabs based on game
        if game_id in self.tab_factories:
            self.tab_factories[game_id](tab_widget)
        else:
            # Default placeholder for games not yet implemented
            placeholder_tab = QWidget()
            placeholder_layout = QVBoxLayout(placeholder_tab)
            placeholder_layout.setAlignment(Qt.AlignCenter)
            placeholder_layout.addWidget(BodyLabel(f"{game_name} - Coming Soon", placeholder_tab))
            tab_widget.addTab(placeholder_tab, "Coming Soon")
        
        return page

    def get_tab_stylesheet(self):
        """Get the stylesheet for tab widgets"""
        return """
            QTabWidget::pane {
                border: none;
                background: transparent;
                margin: 0;
                padding: 0;
            }
            QTabWidget::tab-bar {
                alignment: left;
                background: transparent;
                border: none;
                margin: 0;
                padding: 0;
            }
            QTabBar::tab {
                background: palette(button);
                color: palette(text);
                border: none;
                border-radius: 8px 8px 0 0;
                padding: 16px 24px;
                margin-right: 2px;
                font-size: 14px;
                font-weight: 500;
                min-width: 140px;
                min-height: 24px;
                border-bottom: 2px solid transparent;
            }
            QTabBar::tab:selected {
                background: palette(light);
                color: palette(text);
                border-bottom: 2px solid palette(mid);
            }
            QTabBar::tab:hover:!selected {
                background: palette(mid);
                color: palette(text);
            }
        """

    def apply_tab_style(self, tab_widget):
        tab_widget.setStyleSheet("""
            QTabBar::tab {
                min-width: 10px;
                max-width: 300px;
                padding: 4px 16px;
                margin-right: 1px;
                border-radius: 6px;
            }
            QTabBar::tab:selected {
                background: #4A90E2;
                color: white;
            }
            QTabBar::tab:!selected {
                background: #232323;
                color: #E0E0E0;
            }
            QTabWidget::pane {
                border: none;
            }
        """)
        tab_widget.tabBar().setMovable(True)
        tab_widget.tabBar().setUsesScrollButtons(True)
        # Dynamically size tabs to fit text
        from PyQt5.QtGui import QFontMetrics
        font_metrics = QFontMetrics(tab_widget.tabBar().font())
        for i in range(tab_widget.count()):
            text = tab_widget.tabText(i)
            width = font_metrics.width(text)
            tab_widget.tabBar().setTabMinimumWidth(i, width)
            tab_widget.tabBar().setTabMaximumWidth(i, width)

    def create_mp1_tabs(self, tab_widget):
        self.apply_tab_style(tab_widget)
        """Create tabs for Mario Party 1 - Basic coin structure"""
        # Coins Mods tab - MP1 only has 3 basic coin fields
        coins_global_tab = CoinsTab("marioParty1", "basic")
        tab_widget.addTab(coins_global_tab, "Coins Mods")
        self.all_tabs.append(coins_global_tab)
        
        # Block Weights tab
        block_tab = BlockWeightsTab("marioParty1")
        tab_widget.addTab(block_tab, "Block Weights")
        self.all_tabs.append(block_tab)
        
        # Minigame Replacement tab
        mg_tab = MinigameTab("marioParty1")
        tab_widget.addTab(mg_tab, "Minigame Replacement")
        self.all_tabs.append(mg_tab)
        
        # Star Handicaps tab
        handicap_global_tab = HandicapTab("marioParty1")
        tab_widget.addTab(handicap_global_tab, "Star Handicaps")
        self.all_tabs.append(handicap_global_tab)
    
    def update_all_tabs_theme(self):
        """Update theme for all tabs when theme changes"""
        for tab in self.all_tabs:
            if hasattr(tab, 'themeChanged'):
                tab.themeChanged()

    def create_mp2_tabs(self, tab_widget):
        self.apply_tab_style(tab_widget)
        """Create tabs for Mario Party 2 - Similar to MP1 but with Koopa Bank"""
        # Coins Mods tab - MP2 has basic coins + Koopa Bank
        coins_global_tab = CoinsTab("marioParty2", "basic")
        tab_widget.addTab(coins_global_tab, "Coins Mods")
        self.all_tabs.append(coins_global_tab)
        
        # Items tab - MP2 item price modifications
        shop_mp2_mp3_tab = ItemsTab("marioParty2")
        tab_widget.addTab(shop_mp2_mp3_tab, "Item Prices")
        self.all_tabs.append(shop_mp2_mp3_tab)
        
        # Item Replacement tab - MP2 item space replacement
        item_replace_global_tab = ItemReplaceTab("marioParty2")
        tab_widget.addTab(item_replace_global_tab, "Item Replacement")
        self.all_tabs.append(item_replace_global_tab)
        
        # Minigame Replacement tab
        mg_tab = MinigameTab("marioParty2")
        tab_widget.addTab(mg_tab, "Minigame Replacement")
        self.all_tabs.append(mg_tab)
        
        # Star Handicaps tab
        handicap_global_tab = HandicapTab("marioParty2")
        tab_widget.addTab(handicap_global_tab, "Star Handicaps")
        self.all_tabs.append(handicap_global_tab)
        
        # Bonus Star Replacement tab
        bonus_star_global_tab = BonusStarTab("marioParty2")
        tab_widget.addTab(bonus_star_global_tab, "Bonus Star Replacement")
        self.all_tabs.append(bonus_star_global_tab)

    def create_mp3_tabs(self, tab_widget):
        self.apply_tab_style(tab_widget)
        """Create tabs for Mario Party 3 - Advanced coin structure with Boo options"""
        # Coins Mods tab - MP3 has basic coins + Koopa Bank + Boo Coins/Stars
        coins_global_tab = CoinsTab("marioParty3", "basic")
        tab_widget.addTab(coins_global_tab, "Coins Mods")
        self.all_tabs.append(coins_global_tab)
        
        # Minigame Replacement tab
        mg_tab = MinigameTab("marioParty3")
        tab_widget.addTab(mg_tab, "Minigame Replacement")
        self.all_tabs.append(mg_tab)
        
        # Items tab - MP3 item price modifications
        shop_mp2_mp3_tab = ItemsTab("marioParty3")
        tab_widget.addTab(shop_mp2_mp3_tab, "Item Prices")
        self.all_tabs.append(shop_mp2_mp3_tab)
        
        # Item Replacement tab - MP3 item space replacement
        item_replace_global_tab = ItemReplaceTab("marioParty3")
        tab_widget.addTab(item_replace_global_tab, "Item Replacement")
        self.all_tabs.append(item_replace_global_tab)
        
        # Star Handicaps tab
        handicap_global_tab = HandicapTab("marioParty3")
        tab_widget.addTab(handicap_global_tab, "Star Handicaps")
        self.all_tabs.append(handicap_global_tab)

    def create_mp4_tabs(self, tab_widget):
        self.apply_tab_style(tab_widget)
        """Create tabs for Mario Party 4 - Complete feature set with complex item logic"""
        # Coins Mods tab - MP4 has many coin fields (11 total)
        coins_global_tab = CoinsTab("marioParty4", "advanced")
        tab_widget.addTab(coins_global_tab, "Coins Mods")
        self.all_tabs.append(coins_global_tab)

        # Minigame Replacement tab
        mg_tab = MinigameTab("marioParty4")
        tab_widget.addTab(mg_tab, "Minigame Replacement")
        self.all_tabs.append(mg_tab)

        # Shop Prices tab - Complex item pricing system
        shop_mp4_prices_tab = ShopPricesTab("marioParty4", "mp4")
        tab_widget.addTab(shop_mp4_prices_tab, "Shop Prices")
        self.all_tabs.append(shop_mp4_prices_tab)

        # Shop Odds tab - Item appearance odds
        shop_mp4_odds_tab = ShopOddsTab("marioParty4", "mp4")
        tab_widget.addTab(shop_mp4_odds_tab, "Shop Odds")
        self.all_tabs.append(shop_mp4_odds_tab)

        # Initial Items tab - Starting item selection
        inital_items_global_tab = InitialItemsTab("marioParty4")
        tab_widget.addTab(inital_items_global_tab, "Initial Items")
        self.all_tabs.append(inital_items_global_tab)

        # Item Bag tab - Item bag modifications
        item_bag_mp4_tab = ItemBagTab("marioParty4")
        tab_widget.addTab(item_bag_mp4_tab, "Item Bag")
        self.all_tabs.append(item_bag_mp4_tab)

        # Space Replacement tab - Board space modifications
        space_replace_tab = SpaceReplacementTab("marioParty4")
        tab_widget.addTab(space_replace_tab, "Space Replacement")
        self.all_tabs.append(space_replace_tab)

        # Lottery Rewards tab - Lottery prize modifications
        lottery_tab = LotteryRewardsTab("marioParty4")
        tab_widget.addTab(lottery_tab, "Lottery Rewards")
        self.all_tabs.append(lottery_tab)

        # Battle Minigame tab - Battle minigame bounties
        battle_tab = BattleMinigameTab("marioParty4")
        tab_widget.addTab(battle_tab, "Battle Minigame")
        self.all_tabs.append(battle_tab)

        # Star Handicaps tab
        handicap_global_tab = HandicapTab("marioParty4")
        tab_widget.addTab(handicap_global_tab, "Star Handicaps")
        self.all_tabs.append(handicap_global_tab)

    def create_mp5_tabs(self, tab_widget):
        self.apply_tab_style(tab_widget)
        """Create tabs for Mario Party 5 - Advanced coin structure"""
        # Coins Mods tab - MP5 has advanced coin fields
        coins_global_tab = CoinsTab("marioParty5", "advanced")
        tab_widget.addTab(coins_global_tab, "Coins Mods")
        self.all_tabs.append(coins_global_tab)
        
        # Minigame Replacement tab
        mg_tab = MinigameTab("marioParty5")
        tab_widget.addTab(mg_tab, "Minigame Replacement")
        self.all_tabs.append(mg_tab)
        
        # Bonus Star Replace tab
        bonus_star_global_tab = BonusStarTab("marioParty5")
        tab_widget.addTab(bonus_star_global_tab, "Bonus Star Replacement")
        self.all_tabs.append(bonus_star_global_tab)

        # Battle Minigame tab
        battle_tab = BattleMinigameTab("marioParty5")
        tab_widget.addTab(battle_tab, "Battle Minigame")
        self.all_tabs.append(battle_tab)

        # Capsule Mods tab (custom for MP5)
        capsule_tab = CapsuleModsMp5Tab("marioParty5")
        tab_widget.addTab(capsule_tab, "Capsule Mods")
        self.all_tabs.append(capsule_tab)

        # Board Specific tab
        board_tab = BoardSpecificMp5Tab("marioParty5")
        tab_widget.addTab(board_tab, "Board Specific")
        self.all_tabs.append(board_tab)

        # Star Handicaps tab
        handicap_global_tab = HandicapTab("marioParty5")
        tab_widget.addTab(handicap_global_tab, "Star Handicaps")
        self.all_tabs.append(handicap_global_tab)

    def create_mp6_tabs(self, tab_widget):
        self.apply_tab_style(tab_widget)
        """Create tabs for Mario Party 6 - Advanced coin structure with Pink Boo"""
        # Coins Mods tab - MP6 has advanced coin fields + Pink Boo options
        coins_global_tab = CoinsTab("marioParty6", "advanced")
        tab_widget.addTab(coins_global_tab, "Coins Mods")
        
        # Minigame Replacement tab
        mg_tab = MinigameTab("marioParty6")
        tab_widget.addTab(mg_tab, "Minigame Replacement")
        
        # Item Mods tab (Orb Mods)
        item_tab = ItemReplaceTab("marioParty6")
        tab_widget.addTab(item_tab, "Orb Mods")
        
        # Space Replacement tab
        space_tab = SpaceReplacementTab("marioParty6")
        tab_widget.addTab(space_tab, "Space Replacement")
        
        # Initial Items tab
        initial_items_tab = InitialItemsTab("marioParty6")
        tab_widget.addTab(initial_items_tab, "Initial Orbs")
        
        # Battle Minigame tab
        battle_tab = BattleMinigameTab("marioParty6")
        tab_widget.addTab(battle_tab, "Battle Minigame")
        
        # Star Handicaps tab
        handicap_global_tab = HandicapTab("marioParty6")
        tab_widget.addTab(handicap_global_tab, "Star Handicaps")
        
        # Bonus Star Replacement tab
        bonus_star_tab = BonusStarTab("marioParty6")
        tab_widget.addTab(bonus_star_tab, "Bonus Star Replacement")

    def create_mp7_tabs(self, tab_widget):
        self.apply_tab_style(tab_widget)
        """Create tabs for Mario Party 7 - Advanced coin structure with Last 5 option"""
        # Coins Mods tab - MP7 has advanced coin fields + Last 5 star cost option
        coins_global_tab = CoinsTab("marioParty7", "advanced")
        tab_widget.addTab(coins_global_tab, "Coins Mods")
    
        
        # Minigame Replacement tab
        mg_tab = MinigameTab("marioParty7")
        tab_widget.addTab(mg_tab, "Minigame Replacement")
        
        # Star Handicaps tab
        handicap_global_tab = HandicapTab("marioParty7")
        tab_widget.addTab(handicap_global_tab, "Star Handicaps")

    def create_mp8_tabs(self, tab_widget):
        self.apply_tab_style(tab_widget)
        """Create tabs for Mario Party 8 - Basic coin structure"""
        # Coins Mods tab - MP8 has basic coin fields
        coins_global_tab = CoinsTab("marioParty8", "basic")
        tab_widget.addTab(coins_global_tab, "Coins Mods")
    
        # Minigame Replacement tab
        mg_tab = MinigameTab("marioParty8")
        tab_widget.addTab(mg_tab, "Minigame Replacement")
        
        # Star Handicaps tab
        handicap_global_tab = HandicapTab("marioParty8")
        tab_widget.addTab(handicap_global_tab, "Star Handicaps")

    def create_mp9_tabs(self, tab_widget):
        self.apply_tab_style(tab_widget)
        """Create tabs for Mario Party 9 - Basic coin structure"""
        # Coins Mods tab - MP9 has basic coin fields
        coins_global_tab = CoinsTab("marioParty9", "basic")
        tab_widget.addTab(coins_global_tab, "Coins Mods")

        
        # Minigame Replacement tab
        mg_tab = MinigameTab("marioParty9")
        tab_widget.addTab(mg_tab, "Minigame Replacement")
        
        # Star Handicaps tab
        handicap_global_tab = HandicapTab("marioParty9")
        tab_widget.addTab(handicap_global_tab, "Star Handicaps")

    def create_mpds_tabs(self, tab_widget):
        self.apply_tab_style(tab_widget)
        """Create tabs for Mario Party DS - Basic coin structure"""
        # Coins Mods tab - MPDS has basic coin fields
        coins_global_tab = CoinsTab("marioPartyDS", "basic")
        tab_widget.addTab(coins_global_tab, "Coins Mods")
    
        
        # Minigame Replacement tab
        mg_tab = MinigameTab("marioPartyDS")
        tab_widget.addTab(mg_tab, "Minigame Replacement")
        
        # Star Handicaps tab
        handicap_global_tab = HandicapTab("marioPartyDS")
        tab_widget.addTab(handicap_global_tab, "Star Handicaps")
