# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt, pyqtSignal, QSettings
from qfluentwidgets import SubtitleLabel, PushButton, setTheme, Theme, BodyLabel

# Import dark mode detection
try:
    import darkdetect
    DARKDETECT_AVAILABLE = True
except ImportError:
    DARKDETECT_AVAILABLE = False

# Import scale manager
from utils.scale_manager import ScaleManager


class SettingsPage(QWidget):
    # Signal emitted when theme changes
    themeChanged = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        # Track current theme state internally
        self.current_theme = self.load_theme_preference()
        self.setup_ui()

    def load_theme_preference(self):
        """Load theme preference from registry/settings"""
        settings = QSettings("Mario Party Toolkit", "Settings")
        # Default to system theme if no preference is saved
        saved_theme = settings.value("theme", "system")
        
        if saved_theme == "dark":
            return Theme.DARK
        elif saved_theme == "light":
            return Theme.LIGHT
        else:  # system or any other value
            # Use system theme as default
            if DARKDETECT_AVAILABLE:
                try:
                    return Theme.DARK if darkdetect.isDark() else Theme.LIGHT
                except Exception:
                    return Theme.LIGHT
            else:
                return Theme.LIGHT
    
    def save_theme_preference(self, theme):
        """Save theme preference to registry/settings"""
        settings = QSettings("Mario Party Toolkit", "Settings")
        if theme == Theme.DARK:
            settings.setValue("theme", "dark")
        elif theme == Theme.LIGHT:
            settings.setValue("theme", "light")
        print(f"✓ Theme preference saved: {settings.value('theme')}")

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
        self.theme_toggle_btn = PushButton("Toggle Theme", self)
        self.theme_toggle_btn.clicked.connect(self.toggle_theme)
        
        # Set initial button text based on current theme
        self.update_button_text()
        layout.addWidget(self.theme_toggle_btn)
        
        # Display info - show current scale (auto-calculated)
        current_scale_factor = ScaleManager.get_scale_factor()
        scale_info = BodyLabel(f"UI Scale: {int(current_scale_factor * 100)}% (Auto-fitted to display)", self)
        scale_info.setStyleSheet("color: gray;")
        scale_info.setAlignment(Qt.AlignCenter)
        layout.addWidget(scale_info)
        
        # Add more settings options here in the future
        layout.addStretch()
    
    def update_button_text(self):
        """Update button text based on current theme"""
        if self.current_theme == Theme.DARK:
            self.theme_toggle_btn.setText("Switch to Light Theme")
        else:
            self.theme_toggle_btn.setText("Switch to Dark Theme")

    def toggle_theme(self):
        """Toggle between light and dark themes"""
        try:
            # Toggle to opposite theme based on current internal state
            if self.current_theme == Theme.DARK:
                self.current_theme = Theme.LIGHT
                setTheme(Theme.LIGHT)
                print("✓ Theme changed to Light")
            else:
                self.current_theme = Theme.DARK
                setTheme(Theme.DARK)
                print("✓ Theme changed to Dark")
            
            # Update button text
            self.update_button_text()
            
            # Save preference to registry
            self.save_theme_preference(self.current_theme)
            
            # Emit signal to notify other components
            self.themeChanged.emit()
            
        except Exception as e:
            print(f"⚠️  Error toggling theme: {e}")
    
    def apply_current_theme(self):
        """Apply the current theme setting"""
        try:
            setTheme(self.current_theme)
            self.update_button_text()
            print(f"✓ Applied theme: {'Dark' if self.current_theme == Theme.DARK else 'Light'}")
        except Exception as e:
            print(f"⚠️  Error applying theme: {e}")