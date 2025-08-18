#!/usr/bin/env python3
# ============================================
# Injector Page Component
# Handles code injection functionality
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QSizePolicy
from PyQt5.QtCore import Qt
from qfluentwidgets import SubtitleLabel, BodyLabel


class InjectorPage(QWidget):
    def __init__(self):
        super().__init__()
        self.setup_ui()

    def setup_ui(self):
        """Set up the injector page UI"""
        self.setObjectName("injectorPage")
        layout = QVBoxLayout(self)
        layout.setAlignment(Qt.AlignCenter)
        layout.setContentsMargins(50, 50, 50, 50)
        layout.setSpacing(24)
        
        # Set size policy for the page to allow resizing
        self.setSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        
        title = SubtitleLabel("Code Injector", self)
        title.setAlignment(Qt.AlignCenter)
        layout.addWidget(title)
        
        info = BodyLabel("Inject generated codes into your Mario Party games", self)
        info.setAlignment(Qt.AlignCenter)
        layout.addWidget(info)
        
        # TODO: Add code injection controls and functionality
