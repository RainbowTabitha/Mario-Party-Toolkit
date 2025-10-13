# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

import sys
import os
from PyQt5.QtWidgets import QApplication
from PyQt5.QtGui import QIcon, QFont
from PyQt5.QtCore import Qt
from qfluentwidgets import FluentTranslator

from components.mario_party_toolkit import MarioPartyToolkit
from utils.resource_manager import ResourceManager
from utils.scale_manager import ScaleManager
from version import versionString


def main():
    # Enable High DPI support for sharp rendering
    QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)
    
    app = QApplication(sys.argv)
    
    # Now calculate auto-scale based on display (after QApplication is created)
    scale_factor = ScaleManager.calculate_auto_scale()
    
    # Apply scaling by setting it in environment for future reference
    if scale_factor != 1.0:
        os.environ['QT_SCALE_FACTOR'] = str(scale_factor)
        print(f"✓ Auto scale factor: {scale_factor} ({int(scale_factor * 100)}%)")
    else:
        print(f"✓ Using default scale (100%)")
    
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
    
    # Set application-wide font with scaled size
    base_font_size = 9
    scaled_font_size = ScaleManager.get_scaled_font_size(base_font_size, scale_factor)
    font = QFont("Segoe UI", scaled_font_size)
    app.setFont(font)
    
    if scale_factor != 1.0:
        print(f"✓ Font size scaled: {base_font_size}pt → {scaled_font_size}pt")
    
    # Create and show the main window
    window = MarioPartyToolkit()
    window.show()
    
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
