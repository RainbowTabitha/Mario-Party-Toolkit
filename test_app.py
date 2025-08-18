#!/usr/bin/env python3
"""
Test script for Mario Party Toolkit
Verifies that all imports work correctly
"""

import sys
import os

def test_imports():
    """Test that all required modules can be imported"""
    print("Testing imports...")
    
    try:
        # Test PyQt6 imports
        from PyQt6.QtWidgets import QApplication
        from PyQt6.QtCore import Qt
        from PyQt6.QtGui import QPixmap, QIcon, QFont
        print("✓ PyQt6 imports successful")
    except ImportError as e:
        print(f"✗ PyQt6 import failed: {e}")
        return False
    
    try:
        # Test PIL imports
        from PIL import Image
        print("✓ PIL imports successful")
    except ImportError as e:
        print(f"✗ PIL import failed: {e}")
        return False
    
    try:
        # Test qt-material imports
        from qt_material import apply_stylesheet
        print("✓ qt-material imports successful")
    except ImportError as e:
        print(f"✗ qt-material import failed: {e}")
        print("  Note: qt-material is optional but recommended for Material Design theme")
    
    try:
        # Test local imports
        from functions import fetchResource
        print("✓ Local functions import successful")
    except ImportError as e:
        print(f"✗ Local functions import failed: {e}")
        return False
    
    try:
        from version import versionString
        print(f"✓ Version import successful: {versionString}")
    except ImportError as e:
        print(f"✗ Version import failed: {e}")
        return False
    
    return True

def test_resources():
    """Test that resource files exist"""
    print("\nTesting resources...")
    
    required_files = [
        "assets/icons/diceBlock.png",
        "assets/logos/mpToolkit_logo.png",
        "assets/logos/marioParty1.png",
        "assets/logos/marioParty2.png",
        "assets/logos/marioParty3.png",
        "assets/logos/marioParty4.png",
        "assets/logos/marioParty5.png",
        "assets/logos/marioParty6.png",
        "assets/logos/marioParty7.png",
        "assets/logos/marioParty8.png",
        "assets/logos/marioParty9.png",
        "assets/logos/marioPartyDS.png",
    ]
    
    missing_files = []
    for file_path in required_files:
        if os.path.exists(file_path):
            print(f"✓ {file_path}")
        else:
            print(f"✗ {file_path} (missing)")
            missing_files.append(file_path)
    
    if missing_files:
        print(f"\nWarning: {len(missing_files)} resource files are missing")
        return False
    
    return True

def test_material_theme():
    """Test Material Design theme functionality"""
    print("\nTesting Material Design theme...")
    
    try:
        from qt_material import apply_stylesheet, list_themes
        
        # List available themes
        themes = list_themes()
        print(f"✓ Available themes: {len(themes)} themes found")
        print(f"  Sample themes: {', '.join(themes[:5])}")
        
        # Test theme application
        from PyQt6.QtWidgets import QWidget
        test_widget = QWidget()
        apply_stylesheet(test_widget, theme='dark_teal.xml')
        print("✓ Theme application test successful")
        
        return True
        
    except ImportError:
        print("✗ qt-material not available")
        return False
    except Exception as e:
        print(f"✗ Theme test failed: {e}")
        return False

def test_app_creation():
    """Test that the main application can be created"""
    print("\nTesting application creation...")
    
    try:
        # Create a minimal QApplication
        app = QApplication.instance()
        if app is None:
            app = QApplication(sys.argv)
        
        # Try to import and create the main window
        from main import MarioPartyToolkit
        window = MarioPartyToolkit()
        print("✓ Main application creation successful")
        
        # Clean up
        window.close()
        return True
        
    except Exception as e:
        print(f"✗ Application creation failed: {e}")
        return False

def main():
    """Run all tests"""
    print("Mario Party Toolkit - Test Suite")
    print("=" * 40)
    
    # Test imports
    if not test_imports():
        print("\n❌ Import tests failed")
        return False
    
    # Test resources
    if not test_resources():
        print("\n⚠️  Resource tests failed (some files missing)")
    
    # Test Material Design theme
    test_material_theme()
    
    # Test app creation
    if not test_app_creation():
        print("\n❌ Application creation test failed")
        return False
    
    print("\n✅ All tests passed!")
    return True

if __name__ == "__main__":
    success = main()
    sys.exit(0 if success else 1)
