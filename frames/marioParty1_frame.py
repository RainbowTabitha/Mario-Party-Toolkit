# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (tabitha@tabs.gay)
# Date: 7/24/2024
# License: MIT
# ============================================

# Import necessary functions and modules
from functions import *
from events.marioParty1_coins import *
from events.marioParty1_handicap import *
from events.marioParty1_mgreplace import *
from events.marioParty1_items import *

# Import custom tkinter module as ctk
import customtkinter as ctk

# Function to create the main interface for Mario Party 1
def create_mario_party_1_interface(frame):
    # Create a tabbed interface
    tabview = ctk.CTkTabview(frame, width=1110, height=885, fg_color=("#fcfcfc", "#323232"))
    tabview.grid(padx=10, pady=10)
    tabview.add("Coins Mods")
    tabview.add("Block Weights")
    tabview.add("Minigame Replacement")
    tabview.add("Star Handicaps")
    tabview.set("Coins Mods")

    # Function to create an entry field and checkbox
    def create_entry_and_checkbox(tab, row, icon_path, label_text, color, checkbox_text, placeholder):
        create_image_icon(tab, icon_path, row, 1)
        label = ctk.CTkLabel(master=tab, text=label_text, font=("Arial", 16))
        label.grid(row=row, column=2, pady=15)
        entry = ctk.CTkEntry(master=tab, width=48, font=("Arial", 16, "bold"), placeholder_text=placeholder)
        entry.grid(row=row, column=3)
        label1 = ctk.CTkLabel(master=tab, text=" Coins on a " + color + " Space. ", font=("Arial", 16))
        label1.grid(row=row, column=4)
        checkbox = ctk.CTkCheckBox(master=tab, text=checkbox_text, width=16, checkbox_width=16, checkbox_height=16)
        checkbox.grid(row=row, column=5, padx=10, pady=10)
        return entry, checkbox

    # Function to create an entry field and checkbox
    def create_entry(tab, row, icon_path, label_text, color, placeholder):
        create_image_icon(tab, icon_path, row, 1)
        label = ctk.CTkLabel(master=tab, text=label_text, font=("Arial", 16))
        label.grid(row=row, column=2, sticky="w", pady=15)
        entry = ctk.CTkEntry(master=tab, width=48, font=("Arial", 16, "bold"), placeholder_text=placeholder)
        entry.grid(row=row, column=3)
        label1 = ctk.CTkLabel(master=tab, text=color, font=("Arial", 16))
        label1.grid(row=row, column=4, sticky="w")
        return entry
    
    # Create entry fields and checkboxes for Coins Mods tab
    blue_entry, blue_checkbox = create_entry_and_checkbox(tabview.tab("Coins Mods"), 1, "assets/eventTags/blueSpace.png", " Gain  ", "Blue", "Double the coins on Last 5", "3")
    red_entry, red_checkbox = create_entry_and_checkbox(tabview.tab("Coins Mods"), 2, "assets/eventTags/redSpace.png", " Lose  ", "Red", "Double the coins on Last 5", "3")
    star_entry = create_entry(tabview.tab("Coins Mods"), 3, "assets/eventTags/starSpace.png", " Costs ", " Coins to buy a Star.", "20")

    # Create button to generate coins modification codes
    parse_coins_button = ctk.CTkButton(master=tabview.tab("Coins Mods"), command=lambda: coinsEvent_mp1(blue_entry, blue_checkbox, red_entry, red_checkbox, star_entry), text="Generate Codes")
    parse_coins_button.place(x=10, y=800)

    # List of minigame names
    minigames_list = ["Memory Match", "Slot Machine", "Buried Treasure", "Treasure Divers", "Shell Game", "Slot Car Derby 1", "Hot Bob-omb", "Slot Car Derby 2", "Pipe Maze", "Ghost Guess", "Musical Mushroom", "Pedal Power", "Crazy Cutter", "Face Lift", "Whack-a-Plant", "Bash 'n' Cash", "Bowl Over", "Ground Pound", "Balloon Burst", "Coin Block Blitz", "Coin Block Bash", "Skateboard Scamper", "Box Mountain Mayhem", "Platform Peril", "Teetering Towers", "Mushroom Mix-Up", "Bumper Ball Maze 1", "Grab Bag", "Bobsled Run", "Bumper Balls", "TightRope Treachery", "Knock Block Tower", "Tipsy Tourney", "Bombs Away", "Crane Game", "Bumper Ball Maze 2", "Mario Bandstand", "Desert Dash", "Shy Guy Says", "Limbo Dance", "Bombsketball", "Cast Aways", "Key-pa-Way", "Running of the Bulb", "Hot Rope Jump", "Handcar Havoc", "Deep Sea Divers", "Piranha's Pursuit", "Tug o' War", "Paddle Battle", "Bumper Ball Maze 3", "Coin Shower Flower", "Hammer Drop"]

    # Create labels, comboboxes, and button for Minigame Replacement tab
    replace_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" Replace  ", font=("Arial", 16))
    replace_label.grid(row=0, column=0)
    combobox_mingames_1 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_1.grid(row=0, column=1)
    with_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" with ", font=("Arial", 16))
    with_label.grid(row=0, column=2)
    combobox_mingames_2 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_2.grid(row=0, column=3)
    parse_minigame_button = ctk.CTkButton(master=tabview.tab("Minigame Replacement"), command=lambda: mgReplaceEvent_mp1(combobox_mingames_1, combobox_mingames_2, minigames_list), text="Generate Codes")
    parse_minigame_button.place(x=10, y=800)

    icon = create_image_icon(tabview.tab("Star Handicaps"), "assets/eventTags/starSpace.png", 0, 0)
    label = ctk.CTkLabel(master=tabview.tab("Star Handicaps"), text=" P1 Starts with  ", font=("Arial", 16))
    label.grid(row=0, column=1)
    p1Stars = ctk.CTkEntry(master=tabview.tab("Star Handicaps"), width=48, font=("Arial", 16, "bold"))
    p1Stars.grid(row=0, column=2)
    label = ctk.CTkLabel(master=tabview.tab("Star Handicaps"), text=" Stars ", font=("Arial", 16))
    label.grid(row=0, column=3)
    
    icon = create_image_icon(tabview.tab("Star Handicaps"), "assets/eventTags/starSpace.png", 1, 0)
    label = ctk.CTkLabel(master=tabview.tab("Star Handicaps"), text=" P2 Starts with  ", font=("Arial", 16))
    label.grid(row=1, column=1)
    p2Stars = ctk.CTkEntry(master=tabview.tab("Star Handicaps"), width=48, font=("Arial", 16, "bold"))
    p2Stars.grid(row=1, column=2)
    label = ctk.CTkLabel(master=tabview.tab("Star Handicaps"), text=" Stars ", font=("Arial", 16))
    label.grid(row=1, column=3)

    icon = create_image_icon(tabview.tab("Star Handicaps"), "assets/eventTags/starSpace.png", 2, 0)
    label = ctk.CTkLabel(master=tabview.tab("Star Handicaps"), text=" P3 Starts with  ", font=("Arial", 16))
    label.grid(row=2, column=1)
    p3Stars = ctk.CTkEntry(master=tabview.tab("Star Handicaps"), width=48, font=("Arial", 16, "bold"))
    p3Stars.grid(row=2, column=2)
    label = ctk.CTkLabel(master=tabview.tab("Star Handicaps"), text=" Stars ", font=("Arial", 16))
    label.grid(row=2, column=3)

    icon = create_image_icon(tabview.tab("Star Handicaps"), "assets/eventTags/starSpace.png", 3, 0)
    label = ctk.CTkLabel(master=tabview.tab("Star Handicaps"), text=" P4 Starts with  ", font=("Arial", 16))
    label.grid(row=3, column=1)
    p4Stars = ctk.CTkEntry(master=tabview.tab("Star Handicaps"), width=48, font=("Arial", 16, "bold"))
    p4Stars.grid(row=3, column=2)
    label = ctk.CTkLabel(master=tabview.tab("Star Handicaps"), text=" Stars ", font=("Arial", 16))
    label.grid(row=3, column=3)

    parse_stars_button = ctk.CTkButton(master=tabview.tab("Star Handicaps"), command=lambda: handicapEvent_mp1(p1Stars, p2Stars, p3Stars, p4Stars), text="Generate Codes")
    parse_stars_button.place(x=10, y=800)

    icon = create_image_icon(tabview.tab("Block Weights"), "assets/items/plusBlock.png", 1, 1)
    label = ctk.CTkLabel(master=tabview.tab("Block Weights"), text=" Weight:  ", font=("Arial", 16))
    label.grid(row=1, column=2)
    plus = ctk.CTkEntry(master=tabview.tab("Block Weights"), width=48, font=("Arial", 16, "bold"))
    plus.grid(row=1, column=3)

    icon = create_image_icon(tabview.tab("Block Weights"), "assets/items/minusBlock.png", 2, 1)
    label = ctk.CTkLabel(master=tabview.tab("Block Weights"), text=" Weight:  ", font=("Arial", 16))
    label.grid(row=2, column=2)
    minus = ctk.CTkEntry(master=tabview.tab("Block Weights"), width=48, font=("Arial", 16, "bold"))
    minus.grid(row=2, column=3)

    icon = create_image_icon(tabview.tab("Block Weights"), "assets/items/speedBlock.png", 3, 1)
    label = ctk.CTkLabel(master=tabview.tab("Block Weights"), text=" Weight:  ", font=("Arial", 16))
    label.grid(row=3, column=2)
    speed = ctk.CTkEntry(master=tabview.tab("Block Weights"), width=48, font=("Arial", 16, "bold"))
    speed.grid(row=3, column=3)

    icon = create_image_icon(tabview.tab("Block Weights"), "assets/items/slowBlock.png", 4, 1)
    label = ctk.CTkLabel(master=tabview.tab("Block Weights"), text=" Weight:  ", font=("Arial", 16))
    label.grid(row=4, column=2)
    slow = ctk.CTkEntry(master=tabview.tab("Block Weights"), width=48, font=("Arial", 16, "bold"))
    slow.grid(row=4, column=3)

    icon = create_image_icon(tabview.tab("Block Weights"), "assets/items/warpBlock1.png", 5, 1)
    label = ctk.CTkLabel(master=tabview.tab("Block Weights"), text=" Weight:  ", font=("Arial", 16))
    label.grid(row=5, column=2)
    warp1 = ctk.CTkEntry(master=tabview.tab("Block Weights"), width=48, font=("Arial", 16, "bold"))
    warp1.grid(row=5, column=3)

    icon = create_image_icon(tabview.tab("Block Weights"), "assets/icons/diceBlock.png", 6, 1)
    label = ctk.CTkLabel(master=tabview.tab("Block Weights"), text=" Weight:  ", font=("Arial", 16))
    label.grid(row=6, column=2)
    stock1 = ctk.CTkEntry(master=tabview.tab("Block Weights"), width=48, font=("Arial", 16, "bold"))
    stock1.grid(row=6, column=3)

    warningLabel = ctk.CTkLabel(master=tabview.tab("Block Weights"), text="These are weights. These are the\nodds of dice showing.", font=("Arial", 16, "bold"))
    warningLabel.place(x=5, y=330)

    parseButtonTwo = ctk.CTkButton(master=tabview.tab("Block Weights"), command=lambda: itemsEvent_mp1(plus, minus, speed, slow, warp1, stock1), text="Generate Codes")
    parseButtonTwo.place(x=10, y=800)

    return frame