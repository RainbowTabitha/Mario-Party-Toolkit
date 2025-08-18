# Mario Party Toolkit

A comprehensive desktop application for modifying Mario Party games, built with PyQt6 and featuring a beautiful Material Design theme.

## Features

- **Mario Party 1-9 & DS Support**: Tools for all major Mario Party games
- **Code Generation**: Generate cheat codes for various game modifications
- **Material Design UI**: Beautiful, modern interface with qt-material theme
- **Cross-Platform**: Works on Windows, macOS, and Linux
- **Native Integration**: Can call external executables and tools
- **Responsive Layout**: Clean, intuitive interface that adapts to different screen sizes

## Requirements

- Python 3.8 or higher
- PyQt6
- Pillow (PIL)
- requests
- qt-material (for Material Design theme)

## Installation

1. Clone the repository:
```bash
git clone https://github.com/yourusername/Mario-Party-Toolkit.git
cd Mario-Party-Toolkit
```

2. Install dependencies:
```bash
python install.py
```

3. Run the application:
```bash
python run.py
```

## Material Design Theme

The application uses the `qt-material` package to provide a beautiful Material Design interface:

- **Dark Teal Theme**: Modern dark theme with teal accents
- **Responsive Elements**: Smooth animations and hover effects
- **Professional Look**: Clean, modern interface that looks great on all platforms
- **Fallback Support**: Gracefully falls back to default styling if qt-material is unavailable

### Available Themes

The qt-material package provides many theme options. You can easily change themes by modifying the `apply_material_theme()` method in `main.py`:

```python
# Change from dark_teal.xml to other themes like:
# - dark_blue.xml
# - dark_pink.xml
# - light_blue.xml
# - light_teal.xml
apply_stylesheet(self, theme='dark_blue.xml')
```

## Usage

The application provides a tabbed interface for different Mario Party games:

- **Coins Mods**: Modify coin amounts for different space types
- **Block Weights**: Adjust dice block probabilities
- **Minigame Replacement**: Replace minigames with others
- **Star Handicaps**: Set starting star counts for players
- **Item Modifications**: Change item effects and availability

## Project Structure

```
Mario-Party-Toolkit/
├── main.py              # Main PyQt6 application with Material Design
├── run.py               # Launcher script
├── functions.py         # Utility functions
├── codes/               # Game-specific code generation
├── events/              # Event handling logic
├── assets/              # Images and resources
├── requirements.txt     # Python dependencies including qt-material
├── install.py           # Installation helper script
├── build.py             # Build script for executables
└── test_app.py          # Testing script
```

## Building

### Windows
```bash
python build.py
# Or manually:
pyinstaller --onefile --windowed --icon=assets/icons/diceBlock.ico main.py
```

### macOS
```bash
python build.py
# Or manually:
pyinstaller --onefile --windowed --icon=assets/icons/diceBlock.icns main.py
```

### Linux
```bash
python build.py
# Or manually:
pyinstaller --onefile --windowed --icon=assets/icons/diceBlock.png main.py
```

## Testing

Run the test suite to verify everything works correctly:

```bash
python test_app.py
```

This will test:
- All required imports
- Resource file availability
- Material Design theme functionality
- Application creation

## Contributing

1. Fork the repository
2. Create a feature branch
3. Make your changes
4. Submit a pull request

## License

This project is licensed under the MIT License - see the [LICENSE.md](LICENSE.md) file for details.

## Credits

- **Author**: Nayla Hanegan (naylahanegan@gmail.com)
- **Original Framework**: CustomTkinter
- **New Framework**: PyQt6 with qt-material
- **License**: MIT

## Support

If you encounter any issues or have questions, please open an issue on GitHub.
