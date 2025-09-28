#!/usr/bin/env python3
# ============================================
# Main Window Component
# Handles core window functionality, theme, and navigation
# ============================================

import os
import platform
from PyQt5.QtWidgets import QMainWindow, QSizePolicy
from PyQt5.QtCore import Qt, QTimer, QSettings
from PyQt5.QtGui import QIcon

from qfluentwidgets import FluentWindow, setTheme, Theme

# Import dark mode detection
try:
    import darkdetect
    DARKDETECT_AVAILABLE = True
except ImportError:
    DARKDETECT_AVAILABLE = False
    print("⚠️  darkdetect not available, using default light theme")

from utils.resource_manager import ResourceManager


class MainWindow(FluentWindow):
    def __init__(self):
        super().__init__()
        self.setup_window()
        self.setup_theme()
        self.setup_theme_monitoring()
        self.oldPos = None

    def setup_window(self):
        """Set up the main window properties"""
        self.setWindowTitle("Mario Party Toolkit")
        self.setWindowIcon(ResourceManager.get_icon("assets/icons/diceBlock.png"))
        self.setMinimumSize(1200, 800)
        self.resize(1400, 900)
        
        # Enable proper window dragging and resizing
        if platform.system() in ['Linux', 'Darwin']:  # Linux or macOS
            self.setWindowFlags(Qt.Window)
        else:  # Windows
            self.setWindowFlags(Qt.Window | Qt.CustomizeWindowHint)
        
        # Set size policy for proper scaling
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        # Enable window dragging
        self.setAttribute(Qt.WA_TranslucentBackground, False)
        self.setAttribute(Qt.WA_NoSystemBackground, False)

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

    def setup_theme(self):
        """Set the initial theme based on saved preference"""
        try:
            # Load saved theme preference
            theme = self.load_theme_preference()
            setTheme(theme)
            
            # Apply title bar styling after setting theme
            self.apply_title_bar_style()
            
            # Use QTimer to apply styling again after window is fully initialized
            QTimer.singleShot(100, self.apply_title_bar_style)
            
            if theme == Theme.DARK:
                print("✓ Dark theme applied (saved preference)")
            else:
                print("✓ Light theme applied (saved preference)")
                
        except Exception as e:
            print(f"⚠️  Error loading theme preference: {e}, using light theme")
            setTheme(Theme.LIGHT)
            self.apply_title_bar_style()
            QTimer.singleShot(100, self.apply_title_bar_style)

    def setup_theme_monitoring(self):
        """Setup monitoring for theme changes"""
        if DARKDETECT_AVAILABLE:
            try:
                # Create a timer to check for theme changes
                self.theme_timer = QTimer()
                self.theme_timer.timeout.connect(self.check_theme_change)
                self.theme_timer.start(1000)  # Check every second
                
                # Store current theme state
                self.current_theme_dark = darkdetect.isDark()
                print("✓ Theme monitoring enabled")
            except Exception as e:
                print(f"⚠️  Error setting up theme monitoring: {e}")

    def check_theme_change(self):
        """Check if system theme has changed and update accordingly"""
        try:
            if DARKDETECT_AVAILABLE:
                is_dark = darkdetect.isDark()
                if is_dark != self.current_theme_dark:
                    # Theme changed
                    if is_dark:
                        setTheme(Theme.DARK)
                        print("✓ Theme changed to Dark")
                    else:
                        setTheme(Theme.LIGHT)
                        print("✓ Theme changed to Light")
                    
                    # Refresh window title to ensure visibility
                    self.setWindowTitle("Mario Party Toolkit")
                    
                    # Refresh title bar styling for new theme
                    self.apply_title_bar_style()
                    
                    self.current_theme_dark = is_dark
        except Exception as e:
            # Silently handle errors to avoid spam
            pass

    def mousePressEvent(self, event):
        """Handle mouse press events for window dragging"""
        if event.button() == Qt.LeftButton:
            self.oldPos = event.globalPos()

    def mouseMoveEvent(self, event):
        """Handle mouse move events for window dragging"""
        if self.oldPos:
            delta = event.globalPos() - self.oldPos
            self.move(self.pos() + delta)
            self.oldPos = event.globalPos()

    def mouseReleaseEvent(self, event):
        """Handle mouse release events for window dragging"""
        if event.button() == Qt.LeftButton:
            self.oldPos = None

    def apply_title_bar_style(self):
        """Apply minimal styling to fix only the title bar text visibility."""
        try:
            # Import FluentWindow's theme detection
            from qfluentwidgets import isDarkTheme
            
            # Determine if we're in dark mode using FluentWindow's built-in detection
            is_dark_theme = isDarkTheme()
            
            # Set only text color - don't change backgrounds or other styling
            if is_dark_theme:
                text_color = "#FFFFFF"
            else:
                text_color = "#000000"
            
            # Apply minimal styling - only target title text, not the entire window
            title_style = f"""
            /* Only style title label text color */
            QLabel[objectName="titleLabel"] {{
                color: {text_color} !important;
            }}
            
            QWidget[objectName="titleBar"] QLabel {{
                color: {text_color} !important;
            }}
            """
            
            # Don't override the entire window stylesheet, just add our specific rule
            current_style = self.styleSheet()
            if "QLabel[objectName=\"titleLabel\"]" not in current_style:
                self.setStyleSheet(current_style + title_style)
            
            # Try to find and style title components directly without changing backgrounds
            self.force_title_bar_styling(text_color)
            
            print(f"✓ Title bar text color applied ({'Dark' if is_dark_theme else 'Light'} theme) - Text: {text_color}")
        except Exception as e:
            print(f"⚠️  Error applying title bar styling: {e}")
    
    def force_title_bar_styling(self, text_color):
        """Find and style only the title text, preserving all other styling"""
        try:
            from PyQt5.QtWidgets import QLabel, QWidget
            
            # Find all QLabel widgets that might be the title
            all_labels = self.findChildren(QLabel)
            for label in all_labels:
                # Check if this might be a title label
                if (label.text() == "Mario Party Toolkit" or 
                    label.objectName() in ["titleLabel", "title"] or
                    "title" in label.objectName().lower()):
                    # Only change text color, preserve existing styling
                    current_style = label.styleSheet()
                    # Remove any existing color declarations
                    import re
                    current_style = re.sub(r'color\s*:\s*[^;]+;?', '', current_style)
                    # Add our color
                    label.setStyleSheet(f"{current_style} color: {text_color} !important;")
                    print(f"  → Styled title label: {label.objectName()} / '{label.text()}'")
            
            # Find title bar widgets and style only their text labels
            all_widgets = self.findChildren(QWidget)
            for widget in all_widgets:
                if ("title" in widget.objectName().lower() and 
                    "bar" in widget.objectName().lower()):
                    print(f"  → Found title bar widget: {widget.objectName()}")
                    
                    # Style only text labels in title bar, not the container
                    for child in widget.findChildren(QLabel):
                        current_style = child.styleSheet()
                        # Remove any existing color declarations
                        import re
                        current_style = re.sub(r'color\s*:\s*[^;]+;?', '', current_style)
                        # Add our color
                        child.setStyleSheet(f"{current_style} color: {text_color} !important;")
                        print(f"    → Styled title bar label: '{child.text()}'")
                        
        except Exception as e:
            print(f"  ⚠️ Error in force styling: {e}")
