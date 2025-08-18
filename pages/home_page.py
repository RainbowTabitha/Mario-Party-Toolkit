#!/usr/bin/env python3
# ============================================
# Home Page Component
# Displays welcome message and version information
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt
from qfluentwidgets import SubtitleLabel, BodyLabel

from version import versionString


class HomePage(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        """Set up the home page UI"""
        self.setObjectName("homePage")
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(60, 60, 60, 60)
        layout.setSpacing(32)
        
        # Set size policy for the page to allow resizing
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        # Welcome title
        title = SubtitleLabel("Welcome to the Mario Party Toolkit", self)
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Version info
        version_label = BodyLabel(f"You are running version: {versionString}", self)
        version_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(version_label)
