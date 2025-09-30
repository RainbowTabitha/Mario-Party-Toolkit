# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

# Import necessary functions and modules
from functions import *
from events.marioParty2_coins import *
from events.marioParty2_items import *
from events.marioParty2_itemReplace import *
from events.marioParty2_handicap import *
from events.marioParty2_mgreplace import *
from events.marioParty2_bonusStarReplace import *

# Import custom tkinter module as ctk
import customtkinter as ctk

# Function to create the main interface for Mario Party 1
def create_mario_party_2_interface(frame):
    # Create a tabbed interface
    tabview = ctk.CTkTabview(frame, width=1110, height=885, fg_color=("#fcfcfc", "#323232"))
    tabview.grid(padx=10, pady=10)
    tabview.add("Coins Mods")
    tabview.add("Minigame Replacement")
    tabview.add("Item Prices")
    tabview.add("Item Replacement")
    tabview.add("Star Handicaps")
    tabview.add("Bonus Star Replacement")
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
    koopaBank_entry = create_entry(tabview.tab("Coins Mods"), 4, "assets/eventTags/koopaBank3.png", " Lend  ", " Coins to Koopa Bank,", "5")

    # Create button to generate coins modification codes
    parse_coins_button = ctk.CTkButton(master=tabview.tab("Coins Mods"), command=lambda: coinsEvent_mp2(blue_entry, blue_checkbox, red_entry, red_checkbox, star_entry, koopaBank_entry), text="Generate Codes")
    parse_coins_button.place(x=10, y=800)

    # List of minigame names
    minigames_list = ["BOWSER Slots", "Roll Out the Barrels", "Coffin Congestion", "Hammer Slammer", "Give Me a Brake!", "Mallet-Go Round", "Grab Bag", "Bumper Balloon Cars", "Rakin' 'em In", "Day at the Races", "Face Lift", "Crazy Cutters", "Hot BOB-OMB", "Bowl Over", "Rainbow Run", "Crane Game", "Move to the Music", "BOB-OMB Barrage", "Look Away", "Shock Drop or Roll", "Lights Out", "Filet Relay", "Archer-ival", "TOAD Bandstand", "Bobsled Run", "Handcar Havoc", "Balloon Burst", "Sky Pilots", "Speed Hockey", "Cake Factory", "Dungeon Dash", "Magnet Carta", "Lava Tile Isle", "Hot Rope Jump", "Shell Shocked", "TOAD in the Box", "Mecha-Marathon", "Roll Call", "Abandon Ship", "Platform Peril", "Totem Pole Pound", "Bumper Balls", "Bombs Away", "Tipsy Tourney", "Honeycomb Havoc", "Hexagon Heat", "Skateboard Scamper", "Slot Car Derby", "Shy Guy Says", "Sneak 'n' Snore", "Driver's Ed", "BOWSER's Big Blast", "Looney Lumberjacks", "Torpedo Targets", "Destruction Duet", "Dizzy Dancing", "Tile Driver", "Quicksand Cache", "Deep Sea Salvage"]
   
    # Create labels, comboboxes, and button for Minigame Replacement tab
    replace_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" Replace  ", font=("Arial", 16))
    replace_label.grid(row=0, column=0)
    combobox_mingames_1 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_1.grid(row=0, column=1)
    with_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" with ", font=("Arial", 16))
    with_label.grid(row=0, column=2)
    combobox_mingames_2 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_2.grid(row=0, column=3)
    parse_minigame_button = ctk.CTkButton(master=tabview.tab("Minigame Replacement"), command=lambda: mgReplaceEvent_mp2(combobox_mingames_1, combobox_mingames_2, minigames_list), text="Generate Codes")
    parse_minigame_button.place(x=10, y=800)

    # List of minigame names
    items2 = ["None", "Mushroom", "Skeleton Key", "Plunder Chest", "Bowser BOMB", "Dueling Glove", "Warp Block", "Golden Mushroom", "Boo Bell", "Bowser Suit", "Magic Lamp"]
   
    label = ctk.CTkLabel(master=tabview.tab("Item Replacement"), text=" Replace  ", font=("Arial", 16))
    label.grid(row=0, column=0)

    itemSwap411 = ctk.CTkComboBox(master=tabview.tab("Item Replacement"), values=items2)
    itemSwap411.grid(row=0, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Item Replacement"), text=" with ", font=("Arial", 16))
    label.grid(row=0, column=2)

    itemSwap412 = ctk.CTkComboBox(master=tabview.tab("Item Replacement"), values=items2)
    itemSwap412.grid(row=0, column=3)

    parseButton = ctk.CTkButton(master=tabview.tab("Item Replacement"), command=lambda: itemReplace_mp2(itemSwap411, itemSwap412, items2), text="Generate Codes")
    parseButton.place(x=10, y=800)

    icon = create_image_icon(tabview.tab("Item Prices"), "assets/items/mushroom.png", 1, 1)
    label = ctk.CTkLabel(master=tabview.tab("Item Prices"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=1, column=2)
    mushroom2 = ctk.CTkEntry(master=tabview.tab("Item Prices"), width=48, font=("Arial", 16, "bold"), placeholder_text="10")
    mushroom2.grid(row=1, column=3)

    icon = create_image_icon(tabview.tab("Item Prices"), "assets/items/skeletonKey.png", 2, 1)
    label = ctk.CTkLabel(master=tabview.tab("Item Prices"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=2, column=2)
    skeletonKey2 = ctk.CTkEntry(master=tabview.tab("Item Prices"), width=48, font=("Arial", 16, "bold"), placeholder_text="10")
    skeletonKey2.grid(row=2, column=3)

    icon = create_image_icon(tabview.tab("Item Prices"), "assets/items/plunderChest.png", 3, 1)
    label = ctk.CTkLabel(master=tabview.tab("Item Prices"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=3, column=2)
    plunderChest2 = ctk.CTkEntry(master=tabview.tab("Item Prices"), width=48, font=("Arial", 16, "bold"), placeholder_text="15")
    plunderChest2.grid(row=3, column=3)

    icon = create_image_icon(tabview.tab("Item Prices"), "assets/items/duelingGlove.png", 4, 1)
    label = ctk.CTkLabel(master=tabview.tab("Item Prices"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=4, column=2)
    duelingGlove2 = ctk.CTkEntry(master=tabview.tab("Item Prices"), width=48, font=("Arial", 16, "bold"), placeholder_text="15")
    duelingGlove2.grid(row=4, column=3)

    label = ctk.CTkLabel(master=tabview.tab("Item Prices"), text="    ", font=("Arial", 16))
    label.grid(row=4, column=5)

    icon = create_image_icon(tabview.tab("Item Prices"), "assets/items/warpBlock.png", 1, 6)
    label = ctk.CTkLabel(master=tabview.tab("Item Prices"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=1, column=7)
    warpBlock2 = ctk.CTkEntry(master=tabview.tab("Item Prices"), width=48, font=("Arial", 16, "bold"), placeholder_text="15")
    warpBlock2.grid(row=1, column=8)

    icon = create_image_icon(tabview.tab("Item Prices"), "assets/items/goldenMushroom.png", 2, 6)
    label = ctk.CTkLabel(master=tabview.tab("Item Prices"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=2, column=7)
    goldenMushroom2 = ctk.CTkEntry(master=tabview.tab("Item Prices"), width=48, font=("Arial", 16, "bold"), placeholder_text="20")
    goldenMushroom2.grid(row=2, column=8)

    icon = create_image_icon(tabview.tab("Item Prices"), "assets/items/magicLamp.png", 3, 6)
    label = ctk.CTkLabel(master=tabview.tab("Item Prices"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=3, column=7)
    magicLamp2 = ctk.CTkEntry(master=tabview.tab("Item Prices"), width=48, font=("Arial", 16, "bold"), placeholder_text="30")
    magicLamp2.grid(row=3, column=8)

    parseButtonTwo = ctk.CTkButton(master=tabview.tab("Item Prices"), command=lambda: itemsEvent_mp2(mushroom2, skeletonKey2, plunderChest2, duelingGlove2, warpBlock2, goldenMushroom2, magicLamp2), text="Generate Codes")
    parseButtonTwo.place(x=10, y=800)

    warningLabel = ctk.CTkLabel(master=tabview.tab("Item Prices"), text="These are not weights! 0 doesnt mean disabled.", font=("Arial", 16, "bold"))
    warningLabel.place(x=5, y=210)

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

    parse_stars_button = ctk.CTkButton(master=tabview.tab("Star Handicaps"), command=lambda: handicapEvent_mp2(p1Stars, p2Stars, p3Stars, p4Stars), text="Generate Codes")
    parse_stars_button.place(x=10, y=800)
    
    stars2 = ["None", "Minigame Star", "Coin Star", "Happening Star", "Red Star", "Blue Star", "Chance Time Star", "Bowser Space Star", "Battle Space Star", "Item Space Star", "Bank Space Star"]
    
    label = ctk.CTkLabel(master=tabview.tab("Bonus Star Replacement"), text=" Replace Minigame Star with:  ", font=("Arial", 16))
    label.grid(row=0, column=0, sticky="w")

    star1 = ctk.CTkComboBox(master=tabview.tab("Bonus Star Replacement"), values=stars2)
    star1.grid(row=0, column=1, pady=10)

    label = ctk.CTkLabel(master=tabview.tab("Bonus Star Replacement"), text=" Replace Coin Star with:  ", font=("Arial", 16))
    label.grid(row=1, column=0, sticky="w")

    star2 = ctk.CTkComboBox(master=tabview.tab("Bonus Star Replacement"), values=stars2)
    star2.grid(row=1, column=1, pady=10)

    label = ctk.CTkLabel(master=tabview.tab("Bonus Star Replacement"), text=" Replace Happening Star with:  ", font=("Arial", 16))
    label.grid(row=2, column=0, sticky="w")

    star3 = ctk.CTkComboBox(master=tabview.tab("Bonus Star Replacement"), values=stars2)
    star3.grid(row=2, column=1, pady=10)
    
    parseButton = ctk.CTkButton(master=tabview.tab("Bonus Star Replacement"), command=lambda: customBonusStarEvent_mp2(star1, star2, star3, stars2), text="Generate Codes")
    parseButton.place(x=10, y=800)
    return frame