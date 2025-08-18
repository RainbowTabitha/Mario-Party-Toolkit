#!/usr/bin/env python3
# ============================================
# Mario Party Toolkit Application
# Main application class that integrates all components
# ============================================

from components.main_window import MainWindow
from components.navigation_manager import NavigationManager


class MarioPartyToolkit(MainWindow):
    def __init__(self):
        super().__init__()
        
        # Create navigation interface
        self.navigation_manager = NavigationManager(self)
        
        # Apply title bar styling
        self.apply_title_bar_style()
