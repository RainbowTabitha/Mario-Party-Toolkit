# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

"""
Build script for Mario Party Toolkit
Creates standalone executables for different platforms
"""

import os
import sys
import platform
import subprocess
from pathlib import Path

def install_pyinstaller():
    """Install PyInstaller if not already installed"""
    try:
        import PyInstaller
        print("PyInstaller already installed")
    except ImportError:
        print("Installing PyInstaller...")
        subprocess.check_call([sys.executable, "-m", "pip", "install", "pyinstaller"])

def build_executable():
    """Build the executable for the current platform"""
    system = platform.system().lower()
    
    # Platform-specific settings
    if system == "windows":
        icon = "assets/icons/diceBlock.ico"
        output_name = "MarioPartyToolkit.exe"
    elif system == "darwin":  # macOS
        icon = "assets/icons/diceBlock.icns"
        output_name = "MarioPartyToolkit"
    else:  # Linux
        icon = "assets/icons/diceBlock.png"
        output_name = "MarioPartyToolkit"
    
    # Check if icon exists
    if not os.path.exists(icon):
        print(f"Warning: Icon file {icon} not found, building without icon")
        icon = ""
    
    # Build command
    cmd = [
        "pyinstaller",
        "--onefile",
        "--windowed",
        "--name", output_name,
        "--distpath", "dist",
        "--workpath", "build",
        "--specpath", "build"
    ]
    
    if icon:
        cmd.extend(["--icon", icon])
    
    cmd.append("main.py")
    
    print(f"Building for {system}...")
    print(f"Command: {' '.join(cmd)}")
    
    try:
        subprocess.check_call(cmd)
        print(f"Build successful! Executable created in dist/{output_name}")
    except subprocess.CalledProcessError as e:
        print(f"Build failed with error code {e.returncode}")
        sys.exit(1)

def main():
    """Main build function"""
    print("Mario Party Toolkit - Build Script")
    print("=" * 40)
    
    # Check if we're in the right directory
    if not os.path.exists("main.py"):
        print("Error: main.py not found. Please run this script from the project root directory.")
        sys.exit(1)
    
    # Install PyInstaller if needed
    install_pyinstaller()
    
    # Build the executable
    build_executable()
    
    print("\nBuild completed successfully!")

if __name__ == "__main__":
    main()
