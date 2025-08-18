# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 2/21/2024
# License: MIT
# ============================================

import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from pathlib import Path
import sys
import requests
import sys
import webbrowser
import tkinter.filedialog
import os
import threading
import json
import subprocess

# PyQt5 imports for the new dialog function
try:
    from PyQt5.QtWidgets import QMessageBox, QApplication
    from PyQt5.QtCore import QTimer
    PYQT5_AVAILABLE = True
except ImportError:
    PYQT5_AVAILABLE = False

# QFluentWidgets imports for fluent design modals
try:
    from qfluentwidgets import InfoBar, InfoBarPosition, FluentIcon
    QFLUENT_AVAILABLE = True
except ImportError:
    QFLUENT_AVAILABLE = False

# Create a function for file selection
def select_file(file_label):
    filename = tkinter.filedialog.askopenfilename(filetypes=[("Z64 Files", "*.z64"), ("ISO Files", "*.iso"), ("WBFS Files", "*.wbfs"), ("All Files", "*.*")])    # Do something with the selected filename, e.g., display it in the entry
    file_label.configure(text=filename)

def fetchResource(resource_path: Path) -> Path:
    try:  # Running as *.exe; fetch resource from temp directory
        base_path = Path(sys._MEIPASS)
    except AttributeError:  # Running as script; return unmodified path
        return resource_path
    else:   # Return temp resource path
        return base_path.joinpath(resource_path)

def create_image_icon(frame, image_path, row, column):
    # Create and configure the canvas with the provided image
    image = Image.open(fetchResource(image_path))
    image = image.resize((48, 48))
    image_tk = ImageTk.PhotoImage(image)
    label = ctk.CTkLabel(frame, image=image_tk, font=("Arial", 1))
    label.configure(fg_color=['#fcfcfc', '#323232'], text=str(row)+":"+str(column)) # Windows fix
    label.image = image_tk  # Keep a reference to the image to prevent it from being garbage collected
    label.grid(row=row, column=column)

def create_banner(frame, image_path, row, column):
    # Create and configure the canvas with the provided image
    image = Image.open(fetchResource(image_path))
    image = image.resize((200, 75))
    image_tk = ImageTk.PhotoImage(image)
    label = ctk.CTkLabel(frame, image=image_tk)
    label.configure(fg_color=['#dbdbdb', '#2b2b2b'], text="") # Windows fix
    label.image = image_tk  # Keep a reference to the image to prevent it from being garbage collected
    label.grid(row=row, column=column)

def darken_color(r,g,b, factor):
    return [r*factor, g*factor, b*factor]

def is_file_greater_than_4gb(file_path):
    # Get the size of the file in bytes
    file_size_bytes = os.path.getsize(file_path)
    
    # Convert bytes to gigabytes
    file_size_gb = file_size_bytes / (1024**3)  # 1 GB = 1024**3 bytes
    
    # Check if the file size is greater than 4 GB
    return file_size_gb > 4

def get_capsule_value(capsule):
        try:
            return capsule.get()
        except:
            return 0
        
def find_lowest_integer(*args):
    if not args:
        return None  # Return None if no arguments are provided
    lowest = float('inf')  # Initialize lowest with positive infinity
    for num in args:  # Iterate over arguments
        if num != 0 and num < lowest:
            lowest = num
    if lowest == float('inf'):
        return None  # If no non-zero integers were found, return None
    return lowest

def findLowestIntegerWithZero(*args):
    if not args:
        return None  # Return None if no arguments are provided
    lowest = float('inf')  # Initialize lowest with positive infinity
    for num in args:  # Iterate over arguments
        if num < lowest:
            lowest = num
    if lowest == float('inf'):
        return None  # If no non-zero integers were found, return None
    return lowest
    
def is_file_less_than_100mb(file_path):
    # Get the size of the file in bytes
    file_size_bytes = os.path.getsize(file_path)
    
    # Convert bytes to megabytes
    file_size_mb = file_size_bytes / (1024**2)  # 1 MB = 1024**2 bytes
    
    # Check if the file size is less than 100 MB
    return file_size_mb < 100

# PyQt5-compatible dialog function
def createDialog(windowTitle, warn, info, buttonTxt=None):
    """
    Create a dialog box that works in both CTk and PyQt5 environments.
    In PyQt5 with QFluentWidgets, this creates a beautiful InfoBar.
    In PyQt5 without QFluentWidgets, this creates a QMessageBox.
    In CTk, it creates the original CTk dialog.
    """
    if QFLUENT_AVAILABLE and QApplication.instance() is not None:
        # Use QFluentWidgets InfoBar for beautiful fluent design
        try:
            # Get the main window to show the InfoBar
            main_window = QApplication.instance().activeWindow()
            if main_window is None:
                # Try to find any window
                for widget in QApplication.instance().topLevelWidgets():
                    if widget.isVisible():
                        main_window = widget
                        break
            
            if main_window:
                # Create InfoBar with appropriate styling
                if warn == "success":
                    info_bar = InfoBar.success(
                        title=windowTitle,
                        content=info,
                        orient=0,  # Horizontal
                        isClosable=True,
                        position=InfoBarPosition.TOP_RIGHT,
                        duration=3000,  # 3 seconds
                        parent=main_window
                    )
                elif warn == "error":
                    info_bar = InfoBar.error(
                        title=windowTitle,
                        content=info,
                        orient=0,  # Horizontal
                        isClosable=True,
                        position=InfoBarPosition.TOP_RIGHT,
                        duration=4000,  # 4 seconds for errors
                        parent=main_window
                    )
                else:
                    info_bar = InfoBar.info(
                        title=windowTitle,
                        content=info,
                        orient=0,  # Horizontal
                        isClosable=True,
                        position=InfoBarPosition.TOP_RIGHT,
                        duration=3000,  # 3 seconds
                        parent=main_window
                    )
                
                # Show the InfoBar
                info_bar.show()
                print(f"DEBUG: QFluentWidgets InfoBar shown: {windowTitle} - {info}")
                return
            else:
                print("DEBUG: Could not find main window for InfoBar")
        except Exception as e:
            print(f"DEBUG: Error creating InfoBar: {e}")
    
    if PYQT5_AVAILABLE and QApplication.instance() is not None:
        # Fallback to PyQt5 QMessageBox
        try:
            msg_box = QMessageBox()
            msg_box.setWindowTitle(windowTitle)
            msg_box.setText(info)
            
            # Set icon based on warn parameter
            if warn == "success":
                msg_box.setIcon(QMessageBox.Information)
            elif warn == "error":
                msg_box.setIcon(QMessageBox.Critical)
            else:
                msg_box.setIcon(QMessageBox.Information)
            
            # Add button if specified
            if buttonTxt:
                msg_box.addButton(buttonTxt, QMessageBox.AcceptRole)
            
            # Auto-close after 2.5 seconds
            timer = QTimer()
            timer.singleShot(2500, msg_box.close)
            
            msg_box.exec_()
            print(f"DEBUG: QMessageBox shown: {windowTitle} - {info}")
        except Exception as e:
            print(f"DEBUG: Error creating QMessageBox: {e}")
    else:
        # Fallback to original CTk implementation
        try:
            completeWindow = ctk.CTkToplevel()
            completeWindow.title(windowTitle)

            # Load success image and display it in the success window
            img = ctk.CTkImage(Image.open(fetchResource("assets/operation/" + warn + ".png")), size=(100, 100))
            imgLabel = ctk.CTkLabel(completeWindow, image=img, text="")
            imgLabel.grid(row=0, column=0, padx=10, pady=10)
            imgLabel.image = img  # Keep a reference to the image

            if buttonTxt is not None:
                try:
                    button = ctk.CTkButton(completeWindow, command=run_update, text=buttonTxt)
                    button.grid(row=1, column=0, padx=50, pady=10)
                except Exception as e:
                    print("Error creating button:", e)

            # Adjust geometry to place the window in the bottom right corner
            screen_width = completeWindow.winfo_screenwidth()
            screen_height = completeWindow.winfo_screenheight()
            window_width = completeWindow.winfo_reqwidth()
            window_height = completeWindow.winfo_reqheight()
            if sys.platform == "darwin":
                x_coordinate = screen_width - window_width
                y_coordinate = screen_height - window_height
            else:
                x_coordinate = screen_width - window_width - 230
                y_coordinate = screen_height - window_height - 20
            completeWindow.geometry(f"+{x_coordinate}+{y_coordinate}")

            # Configure row and column weights
            completeWindow.columnconfigure(0, weight=1)
            completeWindow.rowconfigure(0, weight=1)

            # Display success message in the success window
            label = ctk.CTkLabel(completeWindow, text=info, font=ctk.CTkFont(size=18))
            label.grid(row=0, column=1, padx=25, pady=10)
            
            # Function to close the window after 2.5 seconds
            def close_window():
                completeWindow.destroy()

            # Close the window after 2.5 seconds
            completeWindow.after(2500, close_window)

            completeWindow.focus()
            print(f"DEBUG: CTk dialog shown: {windowTitle} - {info}")
        except Exception as e:
            # If CTk also fails, just print the message
            print(f"[{windowTitle}] {info}")
            print(f"DEBUG: All dialog methods failed: {e}")

def pick_color():
    pick_color = AskColor()
    color = pick_color.get()
    # Save the color to a JSON file
    with open('settings.json', 'w') as json_file:
        json.dump({"color": color}, json_file)
    createDialog("Operation Successful", "success", "Color preset saved to JSON.\nPlease restart your Toolkit.", None)

def hex_to_rgb(hex_color):
    hex_color = hex_color.lstrip('#')
    
    # Convert hexadecimal to integer
    rgb = tuple(int(hex_color[i:i+2], 16) for i in (0, 2, 4))
    
    return rgb

def system_color():
    if sys.platform == "darwin":
        try:
            sysColor = subprocess.run(["defaults", "read", "-g", "AppleAccentColor"], capture_output=True, text=True)
            sysColor = sysColor.stdout.strip()
        except:
            sysColor = "7"
        if sysColor == "6":
            sysColor = "#f74f9e" # Pink
            sysColorAlt = "#c42b66"
        elif sysColor == "5":
            sysColor = "#a550a7" # Purple
            sysColorAlt = "#863b7f"
        elif sysColor == "4" or sysColor == "7":
            sysColor = "#007aff" # Blue
            sysColorAlt = "#0054b3"
        elif sysColor == "3":
            sysColor = "#62ba46" # Green
            sysColorAlt = "#4f9e37"
        elif sysColor == "2":
            sysColor = "#ffc600" # Yellow
            sysColorAlt = "#cc9200"
        elif sysColor == "1": 
            sysColor = "#f7821b" # Orange
            sysColorAlt = "#ae5b14"
        elif sysColor == "0": 
            sysColor = "#ff5257" # Red
            sysColorAlt = "#cc2c30"
        elif sysColor == "-1":
            sysColor = "#8c8c8c" # Graphite
            sysColorAlt = "#5c5c5c"
        return sysColor, sysColorAlt
    elif sys.platform == "win32":
        sysColor = get_windows_system_color()[4]
        sysColor1 = get_windows_system_color()[0]
        sysColor2 = get_windows_system_color()[1]
        sysColor3 = get_windows_system_color()[2]
        sysColorAlt = darken_color(sysColor1, sysColor2, sysColor3, 0.75)
        sysColorAlt = "#{0:02x}{1:02x}{2:02x}".format(int(sysColorAlt[0]), int(sysColorAlt[1]), int(sysColorAlt[2]))
        return sysColor, sysColorAlt

def pick_color_system():
    with open("settings.json", 'r') as json_file:
        data = json.load(json_file)
    sysColor, sysColorAlt = system_color()
    data['color'] = sysColor
    with open("settings.json", 'w') as json_file:
        json.dump(data, json_file)
    createDialog("Operation Successful", "success", "Color preset reset to system.\nPlease restart your Toolkit.", None)