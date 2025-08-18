#!/usr/bin/env python3
# ============================================
# Main Window Component
# Handles core window functionality, theme, and navigation
# ============================================

import os
import platform
from PyQt5.QtWidgets import QMainWindow, QSizePolicy
from PyQt5.QtCore import Qt, QTimer
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

    def setup_theme(self):
        """Set the initial theme based on system preference"""
        if DARKDETECT_AVAILABLE:
            try:
                if darkdetect.isDark():
                    setTheme(Theme.DARK)
                    print("✓ Dark theme applied (system preference)")
                else:
                    setTheme(Theme.LIGHT)
                    print("✓ Light theme applied (system preference)")
            except Exception as e:
                print(f"⚠️  Error detecting theme: {e}, using light theme")
                setTheme(Theme.LIGHT)
        else:
            # Fallback to light theme
            setTheme(Theme.LIGHT)
            print("✓ Light theme applied (default)")

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
        """Apply custom styling to the title bar to ensure proper text visibility."""
        try:
            # Apply custom stylesheet for the title bar
            title_style = """
            QMainWindow::title {
                background-color: transparent;
                color: palette(text);
                font-weight: bold;
                font-size: 14px;
            }
            
            QMainWindow {
                background-color: palette(window);
                color: palette(text);
            }
            """
            self.setStyleSheet(title_style)
            print("✓ Title bar styling applied")
        except Exception as e:
            print(f"⚠️  Error applying title bar styling: {e}")
