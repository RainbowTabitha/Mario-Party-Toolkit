# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 10/13/2025
# License: MIT
# ============================================

from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QApplication


class ScaleManager:
    """Manages UI scaling - automatically calculated based on display size"""
    
    # Base resolution for 100% scaling (1920x1080 is standard Full HD)
    BASE_WIDTH = 1920
    BASE_HEIGHT = 1080
    
    DEFAULT_SCALE = 1.0
    
    @staticmethod
    def calculate_auto_scale():
        """Automatically calculate scale factor based on display size"""
        try:
            # Try to get the primary screen
            app = QApplication.instance()
            if app:
                screen = app.primaryScreen()
                if screen:
                    screen_geometry = screen.availableGeometry()
                    screen_width = screen_geometry.width()
                    screen_height = screen_geometry.height()
                    
                    # Calculate scale based on screen dimensions
                    # Use the smaller ratio to ensure everything fits
                    width_ratio = screen_width / ScaleManager.BASE_WIDTH
                    height_ratio = screen_height / ScaleManager.BASE_HEIGHT
                    
                    # Use the smaller ratio and round to nearest 0.25
                    auto_scale = min(width_ratio, height_ratio)
                    auto_scale = round(auto_scale * 4) / 4  # Round to nearest 0.25
                    
                    # Clamp between 0.75 and 3.0
                    auto_scale = max(0.75, min(3.0, auto_scale))
                    
                    print(f"✓ Auto-calculated scale: {auto_scale} (Display: {screen_width}x{screen_height})")
                    return auto_scale
        except Exception as e:
            print(f"⚠️  Error calculating auto scale: {e}")
        
        return ScaleManager.DEFAULT_SCALE
    
    @staticmethod
    def get_scale_factor():
        """Get the current scale factor - auto-calculated or from settings cache"""
        settings = QSettings("Mario Party Toolkit", "Settings")
        
        # Check if we have a cached auto-scale value
        cached_scale = settings.value("auto_scale_factor", None)
        
        if cached_scale is not None:
            try:
                return float(cached_scale)
            except (ValueError, TypeError):
                pass
        
        # Calculate and cache the auto scale
        auto_scale = ScaleManager.calculate_auto_scale()
        settings.setValue("auto_scale_factor", auto_scale)
        return auto_scale
    
    @staticmethod
    def get_scale_percentage():
        """Get the current scale as a percentage string (e.g., '100%')"""
        scale = ScaleManager.get_scale_factor()
        return f"{int(scale * 100)}%"
    
    @staticmethod
    def get_scaled_font_size(base_size, scale_factor=None):
        """Get scaled font size"""
        if scale_factor is None:
            scale_factor = ScaleManager.get_scale_factor()
        return int(base_size * scale_factor)

