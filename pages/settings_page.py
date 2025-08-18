#!/usr/bin/env python3
# ============================================
# Settings Page Component
# Handles theme toggling and other settings
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt
from qfluentwidgets import SubtitleLabel, PushButton

# Import dark mode detection
try:
    import darkdetect
    DARKDETECT_AVAILABLE = True
except ImportError:
    DARKDETECT_AVAILABLE = False

from qfluentwidgets import setTheme, Theme


class SettingsPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        """Set up the settings page UI"""
        self.setObjectName("settingsPage")
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(50, 50, 50, 50)
        layout.setSpacing(24)
        
        # Set size policy for the page to allow resizing
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        title = SubtitleLabel("Settings", self)
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Theme toggle button
        if DARKDETECT_AVAILABLE:
            self.theme_toggle_btn = PushButton("Toggle Theme", self)
            self.theme_toggle_btn.clicked.connect(self.toggle_theme)
            
            # Set initial button text based on current theme
            try:
                if darkdetect.isDark():
                    self.theme_toggle_btn.setText("Toggle Theme (Light)")
                else:
                    self.theme_toggle_btn.setText("Toggle Theme (Dark)")
            except Exception as e:
                print(f"⚠️  Error setting initial theme button text: {e}")
            
            layout.addWidget(self.theme_toggle_btn)
        
        # Add more settings options here in the future
        layout.addStretch()

    def toggle_theme(self):
        """Toggle between light and dark themes"""
        if DARKDETECT_AVAILABLE:
            try:
                # Get current theme state
                current_is_dark = darkdetect.isDark()
                
                # Toggle to opposite theme
                if current_is_dark:
                    setTheme(Theme.LIGHT)
                    self.theme_toggle_btn.setText("Toggle Theme (Dark)")
                    print("✓ Theme changed to Light")
                else:
                    setTheme(Theme.DARK)
                    self.theme_toggle_btn.setText("Toggle Theme (Light)")
                    print("✓ Theme changed to Dark")
                
            except Exception as e:
                print(f"⚠️  Error toggling theme: {e}")
        else:
            # Fallback to light theme if darkdetect is not available
            setTheme(Theme.LIGHT)
            self.theme_toggle_btn.setText("Toggle Theme (Light)")
            print("✓ Theme changed to Light (fallback)")
