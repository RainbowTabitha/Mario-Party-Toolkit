#!/usr/bin/env python3
# ============================================
# Navigation Manager Component
# Handles navigation interface setup and page creation
# ============================================

from PyQt5.QtWidgets import QWidget
from qfluentwidgets import (
    NavigationInterface, NavigationItemPosition, FluentIcon
)

from pages.home_page import HomePage
from pages.mario_party_pages import MarioPartyPages
from pages.injector_page import InjectorPage
from pages.settings_page import SettingsPage
from pages.about_page import AboutPage
from utils.resource_manager import ResourceManager


class NavigationManager:
    def __init__(self, main_window):
        self.main_window = main_window
        self.navigation_interface = main_window.navigationInterface
        self.setup_navigation()

    def setup_navigation(self):
        """Set up the navigation interface with all Mario Party games"""
        
        # Hide the internal Fluent Design title bar
        self.navigation_interface.setReturnButtonVisible(False)
        self.navigation_interface.setAcrylicEnabled(False)
        
        # Try to minimize the internal title bar display
        try:
            self.navigation_interface.setMinimumWidth(200)
        except:
            pass  # Ignore if this method doesn't exist
        
        # Add all navigation items
        self.add_home_page()
        self.add_mario_party_pages()
        self.add_separator()
        self.add_injector_page()
        self.add_settings_page()
        self.add_about_page()
        
        # Set initial page
        self.navigation_interface.setCurrentItem('home')

    def add_home_page(self):
        """Add the home page to navigation"""
        self.main_window.addSubInterface(
            interface=HomePage(),
            icon=FluentIcon.HOME,
            text='Home',
            position=NavigationItemPosition.TOP
        )

    def add_mario_party_pages(self):
        """Add all Mario Party game pages to navigation"""
        mario_party_pages = MarioPartyPages()
        
        # Add each Mario Party game
        games = [
            ("marioParty1", "Mario Party 1", "assets/logos/marioParty1.png"),
            ("marioParty2", "Mario Party 2", "assets/logos/marioParty2.png"),
            ("marioParty3", "Mario Party 3", "assets/logos/marioParty3.png"),
            ("marioParty4", "Mario Party 4", "assets/logos/marioParty4.png"),
            ("marioParty5", "Mario Party 5", "assets/logos/marioParty5.png"),
            ("marioParty6", "Mario Party 6", "assets/logos/marioParty6.png"),
            ("marioParty7", "Mario Party 7", "assets/logos/marioParty7.png"),
            ("marioParty8", "Mario Party 8", "assets/logos/marioParty8.png"),
            ("marioParty9", "Mario Party 9", "assets/logos/marioParty9.png"),
            ("marioPartyDS", "Mario Party DS", "assets/logos/marioPartyDS.png"),
        ]
        
        for game_id, game_name, logo_path in games:
            page = mario_party_pages.create_game_page(game_id, game_name)
            icon = ResourceManager.get_game_icon(logo_path)
            
            self.main_window.addSubInterface(
                interface=page,
                icon=icon,
                text=game_name,
                position=NavigationItemPosition.TOP
            )

    def add_separator(self):
        """Add a separator in navigation"""
        self.navigation_interface.addSeparator()

    def add_injector_page(self):
        """Add the code injector page to navigation"""
        self.main_window.addSubInterface(
            interface=InjectorPage(),
            icon=ResourceManager.get_injector_icon(),
            text='Code Injector',
            position=NavigationItemPosition.TOP
        )

    def add_settings_page(self):
        """Add the settings page to navigation"""
        self.main_window.addSubInterface(
            interface=SettingsPage(),
            icon=FluentIcon.SETTING,
            text='Settings',
            position=NavigationItemPosition.BOTTOM
        )

    def add_about_page(self):
        """Add the about page to navigation"""
        self.main_window.addSubInterface(
            interface=AboutPage(),
            icon=FluentIcon.INFO,
            text='About',
            position=NavigationItemPosition.BOTTOM
        )
