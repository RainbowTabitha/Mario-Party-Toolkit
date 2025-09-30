# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

# Import necessary functions and modules
from functions import *
from version import *

# Import custom tkinter module as ctk
import customtkinter as ctk

def welcome_interface(frame):
    label1 = ctk.CTkLabel(frame, text="Welcome to the Mario Party Toolkit.", font=("Arial", 32, "bold"))
    label1.grid(column=1, row=1, padx=32, pady=32)
    label1 = ctk.CTkLabel(frame, text=f"You are running version: {versionString}", font=("Arial", 24, "bold"))
    label1.grid(column=1, row=2)

    return frame