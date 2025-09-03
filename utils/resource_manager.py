#!/usr/bin/env python3
# ============================================
# Resource Manager Utility
# Handles resource loading and icon creation
# ============================================

import os
from PyQt5.QtGui import QIcon
from qfluentwidgets import FluentIcon


class ResourceManager:
    @staticmethod
    def get_resource_path(relative_path):
        """Get the absolute path to a resource file"""
        # Get the directory where this script is located
        current_dir = os.path.dirname(os.path.abspath(__file__))
        # Go up one level to the project root
        project_root = os.path.dirname(current_dir)
        # Construct the full path
        return os.path.join(project_root, relative_path)

    @staticmethod
    def get_icon(icon_path):
        """Get a QIcon from a resource path"""
        try:
            full_path = ResourceManager.get_resource_path(icon_path)
            if os.path.exists(full_path):
                icon = QIcon(str(full_path))
                if not icon.isNull():
                    return icon
                else:
                    print(f"⚠️  Failed to create icon from {icon_path}")
            else:
                print(f"⚠️  Icon file not found: {icon_path}")
        except Exception as e:
            print(f"⚠️  Error creating icon from {icon_path}: {e}")
        
        # Fallback to default icon
        return FluentIcon.APPLICATION

    @staticmethod
    def get_game_icon(logo_path):
        """Get a game icon from a logo file"""
        try:
            full_path = ResourceManager.get_resource_path(logo_path)
            if os.path.exists(full_path):
                icon = QIcon(str(full_path))
                if not icon.isNull():
                    print(f"✓ Game icon created from {logo_path}")
                    return icon
                else:
                    print(f"⚠️  Failed to create icon from {logo_path}")
            else:
                print(f"⚠️  Logo file not found: {logo_path}")
        except Exception as e:
            print(f"⚠️  Error creating game icon from {logo_path}: {e}")
        
        # Fallback to default game icon (FlunkentIcon.GAME)
        return FluentIcon.GAME

    @staticmethod
    def get_injector_icon():
        """Get the injector icon"""
        try:
            icon_path = ResourceManager.get_resource_path("assets/logos/injector.png")
            if os.path.exists(icon_path):
                icon = QIcon(str(icon_path))
                if not icon.isNull():
                    print("✓ Injector icon created from injector.png")
                    return icon
                else:
                    print("⚠️  Failed to create injector icon")
            else:
                print("⚠️  Injector icon file not found: assets/logos/injector.png")
        except Exception as e:
            print(f"⚠️  Error creating injector icon: {e}")
        
        # Fallback to default code icon (FluentIcon.CODE)
        return FluentIcon.CODE
