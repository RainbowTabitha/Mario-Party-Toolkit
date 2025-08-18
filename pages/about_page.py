#!/usr/bin/env python3
# ============================================
# About Page Component
# Displays version information and credits
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt
from qfluentwidgets import SubtitleLabel, BodyLabel

from version import versionString


class AboutPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        """Set up the about page UI"""
        self.setObjectName("aboutPage")
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(50, 50, 50, 50)
        layout.setSpacing(24)
        
        # Set size policy for the page to allow resizing
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        title = SubtitleLabel("About Mario Party Toolkit", self)
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        # Version info
        version_label = BodyLabel(f"Version: {versionString}", self)
        version_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(version_label)
        
        # Description
        description = BodyLabel("A comprehensive toolkit for modifying Mario Party games", self)
        description.setAlignment(Qt.AlignCenter)
        layout.addWidget(description)
        
        # Features list
        features_label = BodyLabel("Features:", self)
        features_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(features_label)
        
        features_list = [
            "• Coin and star modifications",
            "• Minigame replacements", 
            "• Player handicaps",
            "• Item modifications",
            "• Code injection support",
            "• Dark/Light theme support"
        ]
        
        for feature in features_list:
            feature_label = BodyLabel(feature, self)
            feature_label.setAlignment(Qt.AlignCenter)
            layout.addWidget(feature_label)
        
        # Author info
        author_label = BodyLabel("Created by Nayla Hanegan", self)
        author_label.setAlignment(Qt.AlignCenter)
        layout.addWidget(author_label)
        
        layout.addStretch()
