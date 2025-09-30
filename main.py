#!/usr/bin/env python3
# ============================================
# Mario Party Toolkit - Modular PyQt5 Version
# Author: Nayla Hanegan (tabitha@tabs.gay)
# Date: 7/12/2024
# License: MIT
# ============================================

import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon, QFont
from qfluentwidgets import FluentTranslator

from components.mario_party_toolkit import MarioPartyToolkit
from utils.resource_manager import ResourceManager
from version import versionString


def main():
    app = QApplication(sys.argv)
    
    # Set application-wide icon
    icon_path = ResourceManager.get_resource_path("assets/icons/diceBlock.png")
    if os.path.exists(icon_path):
        app.setWindowIcon(QIcon(str(icon_path)))
        print("✓ Application icon set")
    else:
        print("⚠️  Icon file not found")
    
    # Add translator for internationalization
    translator = FluentTranslator()
    app.installTranslator(translator)
    
    # Set application-wide font
    font = QFont("Segoe UI", 9)
    app.setFont(font)
    
    # Create and show the main window
    window = MarioPartyToolkit()
    window.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
