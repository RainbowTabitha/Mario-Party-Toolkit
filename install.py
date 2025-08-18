#!/usr/bin/env python3
"""
Installation script for Mario Party Toolkit
Installs dependencies and sets up the environment
"""

import sys
import subprocess
import os
from pathlib import Path

def check_python_version():
    """Check if Python version is compatible"""
    if sys.version_info < (3, 8):
        print("❌ Python 3.8 or higher is required")
        print(f"Current version: {sys.version}")
        return False
    
    print(f"✓ Python {sys.version_info.major}.{sys.version_info.minor} detected")
    return True

def install_dependencies():
    """Install required Python packages"""
    print("\nInstalling dependencies...")
    
    try:
        subprocess.check_call([
            sys.executable, "-m", "pip", "install", "-r", "requirements.txt", "--break-system-packages"
        ])
        print("✓ Dependencies installed successfully")
        return True
    except subprocess.CalledProcessError as e:
        print(f"✗ Failed to install dependencies: {e}")
        return False

def create_directories():
    """Create necessary directories"""
    print("\nCreating directories...")
    
    directories = ["dist", "build", "logs"]
    
    for directory in directories:
        Path(directory).mkdir(exist_ok=True)
        print(f"✓ Created directory: {directory}")

def check_assets():
    """Check if asset files exist"""
    print("\nChecking assets...")
    
    required_dirs = ["assets", "assets/icons", "assets/logos", "assets/items", "assets/eventTags"]
    
    for directory in required_dirs:
        if os.path.exists(directory):
            print(f"✓ {directory}")
        else:
            print(f"✗ {directory} (missing)")
            Path(directory).mkdir(parents=True, exist_ok=True)
            print(f"  Created {directory}")

def create_launcher_scripts():
    """Create platform-specific launcher scripts"""
    print("\nCreating launcher scripts...")
    
    if sys.platform.startswith('win'):
        # Windows batch file
        with open("run.bat", "w") as f:
            f.write("@echo off\n")
            f.write("python run.py\n")
            f.write("pause\n")
        print("✓ Created run.bat")
        
    elif sys.platform.startswith('darwin'):
        # macOS shell script
        with open("run.sh", "w") as f:
            f.write("#!/bin/bash\n")
            f.write("python3 run.py\n")
        os.chmod("run.sh", 0o755)
        print("✓ Created run.sh")
        
    else:
        # Linux shell script
        with open("run.sh", "w") as f:
            f.write("#!/bin/bash\n")
            f.write("python3 run.py\n")
        os.chmod("run.sh", 0o755)
        print("✓ Created run.sh")

def main():
    """Main installation function"""
    print("Mario Party Toolkit - Installation")
    print("=" * 40)
    
    # Check Python version
    if not check_python_version():
        sys.exit(1)
    
    # Install dependencies
    if not install_dependencies():
        print("\n❌ Installation failed")
        sys.exit(1)
    
    # Create directories
    create_directories()
    
    # Check assets
    check_assets()
    
    # Create launcher scripts
    create_launcher_scripts()
    
    print("\n✅ Installation completed successfully!")
    print("\nTo run the application:")
    
    if sys.platform.startswith('win'):
        print("  Double-click run.bat or run: python run.py")
    else:
        print("  Run: ./run.sh or python3 run.py")
    
    print("\nTo build an executable:")
    print("  python build.py")

if __name__ == "__main__":
    main()
