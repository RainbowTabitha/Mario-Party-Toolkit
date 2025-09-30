# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

# Import necessary functions and modules
from functions import *
from events.general_inject import *
from version import *

# Import custom tkinter module as ctk
import customtkinter as ctk

def injector_interface(frame):
    # Create button for file selection
    select_file_button = ctk.CTkButton(master=frame, text="Select ROM", command=lambda: select_file(file_label))
    select_file_button.place(x=10, y=10)

    # Create label for file selection
    file_label = ctk.CTkLabel(master=frame, text="path/to/rom/file")
    file_label.place(x=160, y=10)

    file_label2 = ctk.CTkLabel(master=frame, text="Codes:")
    file_label2.place(x=10, y=60)

    cheatCodeEntry = ctk.CTkTextbox(master=frame, width=200, height=500)
    cheatCodeEntry.place(x=10, y=65)

    injectCodes = ctk.CTkButton(master=frame, command=lambda: general_injection(file_label, cheatCodeEntry), text="Inject Codes")
    injectCodes.place(x=10, y=590)