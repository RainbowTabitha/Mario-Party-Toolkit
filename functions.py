# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 1/18/2024
# License: MIT
# ============================================

import tkinter as tk
import customtkinter as ctk
from PIL import Image, ImageTk
from pathlib import Path
import requests
import sys
import webbrowser
from version import current_version

def createDialog(windowTitle, warn, info, buttonTxt=None):
    completeWindow = ctk.CTkToplevel()
    completeWindow.geometry("600x165")
    completeWindow.title(windowTitle)
    
    # Load success image and display it in the success window
    img = ctk.CTkImage(Image.open(fetchResource("assets/" + warn + ".png")), size=(100, 100))
    imgLabel = ctk.CTkLabel(completeWindow, image=img, text="")
    imgLabel.grid(row=0, column=0, padx=10, pady=10)
    imgLabel.image = img  # Keep a reference to the image
    
    try:
        button = ctk.CTkButton(completeWindow, command=run_update, text=buttonTxt)
        button.grid(row=1, column=0, padx=50, pady=10)
    except:
        pass

    # Configure row and column weights
    completeWindow.columnconfigure(0, weight=1)
    completeWindow.rowconfigure(0, weight=1)
    
    # Display success message in the success window
    label = ctk.CTkLabel(completeWindow, text=info, font=ctk.CTkFont(size=18))
    label.grid(row=0, column=1, padx=25, pady=10)
    completeWindow.focus()

def updateEmu():
    pass

def fetchResource(resource_path: Path) -> Path:
    try:  # Running as *.exe; fetch resource from temp directory
        base_path = Path(sys._MEIPASS)
    except AttributeError:  # Running as script; return unmodified path
        return resource_path
    else:   # Return temp resource path
        return base_path.joinpath(resource_path)

def create_image_icon(frame, image_path, row, column):
    # Create and configure the canvas with the provided image
    image = Image.open(fetchResource(image_path)).convert("RGBA")
    image = image.resize((32, 32))
    image_tk = ImageTk.PhotoImage(image)
    
    canvas = ctk.CTkCanvas(master=frame, background="#2b2b2b", highlightthickness=0, width=image.width, height=image.height)
    canvas.grid(row=row, column=column)
    canvas.create_image(0, 0, anchor="nw", image=image_tk)

    return canvas, image_tk

def check_for_updates():
    pastebin_url = "https://pastebin.com/raw/MrpYHUHy"
    response = requests.get(pastebin_url)
    
    if response.status_code == 200:
        latest_version = response.text.strip()
                
        if latest_version > current_version:
            createDialog("Update Available", "update", "A new version is available. Please update.", "Update Now")
    else:
        createDialog("Error", "error", "Unable to check for updates!")

def run_update():
    url = "https://github.com/EndangeredNayla/Mario-Party-Toolkit/releases"
    webbrowser.open_new_tab(url)