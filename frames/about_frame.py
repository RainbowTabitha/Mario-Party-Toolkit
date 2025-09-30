# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (tabitha@tabs.gay)
# Date: 5/4/2024
# License: MIT
# ============================================

# Import necessary functions and modules
from functions import *
from version import *

# Import custom tkinter module as ctk
import customtkinter as ctk

def get_mit_license_text():
        mit_license_text = """
MIT License

Copyright (c) 2023 - 2024 Nayla Hanegan

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
        return mit_license_text

def get_credits_text():
        credits_text = """
CREDITS

- Nayla for Program Work

- manifestrev for Program Work

- Rain for Gecko Codes

- Ralf for Gecko Codes

- WolfGC64 for Gecko Codes
"""
        return credits_text

def get_about_text():
        about_text = """
Mario Party Toolkit

Originally Created for DarkSpine's Code Chaos now known as Mario Party Mayhem

Expanding to be a all in one modding toolkit for many variables thats should be customizable in Mario Party.
"""
        return about_text

def about_interface(frame):
    tabview = ctk.CTkTabview(frame, width=2000, height=850)
    tabview.pack(padx=20, pady=20)
    tabview.add("Credits")
    tabview.add("About")
    tabview.add("License")
    tabview.set("About")
    mit_license_widget = ctk.CTkLabel(tabview.tab("License"), width=80, height=20, text=(get_mit_license_text()))
    mit_license_widget.pack(padx=10, pady=10)
    credits_widget = ctk.CTkLabel(tabview.tab("Credits"), width=80, height=20, text=(get_credits_text()))
    credits_widget.pack(padx=10, pady=10)
    about_widget = ctk.CTkLabel(tabview.tab("About"), width=80, height=20, text=(get_about_text()))
    about_widget.pack(padx=10, pady=10)

    return frame