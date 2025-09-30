# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (tabitha@tabs.gay)
# Date: 5/4/2024
# License: MIT
# ============================================

# Import necessary functions and modules
from functions import *
from events.marioParty3_coins import *
from events.marioParty3_items import *
from events.marioParty3_itemReplace import *
from events.marioParty3_handicap import *
from events.marioParty3_mgreplace import *

# Import custom tkinter module as ctk
import customtkinter as ctk

# Function to create the main interface for Mario Party 1
def create_mario_party_3_interface(frame):
    # Create a tabbed interface
    tabview = ctk.CTkTabview(frame, width=1110, height=885, fg_color=("#fcfcfc", "#323232"))
    tabview.grid(padx=10, pady=10)
    tabview.add("Coins Mods")
    tabview.add("Minigame Replacement")
    tabview.add("Item Prices")
    tabview.add("Item Replacement")
    tabview.add("Star Handicaps")
    tabview.set("Coins Mods")

    # Function to create an entry field and checkbox
    def create_entry_and_checkbox(tab, row, icon_path, label_text, color, checkbox_text, placeholder):
        create_image_icon(tab, icon_path, row, 1)
        label = ctk.CTkLabel(master=tab, text=label_text, font=("Arial", 16))
        label.grid(row=row, column=2, sticky="w", pady=15)
        entry = ctk.CTkEntry(master=tab, width=48, font=("Arial", 16, "bold"), placeholder_text=placeholder)
        entry.grid(row=row, column=3)
        label1 = ctk.CTkLabel(master=tab, text=" Coins on a " + color + " Space. ", font=("Arial", 16))
        label1.grid(row=row, column=4, sticky="w")
        checkbox = ctk.CTkCheckBox(master=tab, text=checkbox_text, width=16, checkbox_width=16, checkbox_height=16)
        checkbox.grid(row=row, column=5)
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
    booHouseStar_entry = create_entry(tabview.tab("Coins Mods"), 5, "assets/eventTags/booHouseStars.png", " Costs ", " Coins when stealing a Star.", "50")
    booHouseCoins_entry = create_entry(tabview.tab("Coins Mods"), 6, "assets/eventTags/booHouseCoins.png", " Costs ", " Coins when stealing coins.", "5")

    # Create button to generate coins modification codes
    parse_coins_button = ctk.CTkButton(master=tabview.tab("Coins Mods"), command=lambda: coinsEvent_mp3(blue_entry, blue_checkbox, red_entry, red_checkbox, star_entry, booHouseCoins_entry, booHouseStar_entry, koopaBank_entry), text="Generate Codes")
    parse_coins_button.place(x=10, y=800)

    # List of minigame names
    minigames_list = ["Thwomp Pull", "River Raiders", "Tidal Toss", "Eatsa Pizza", "Baby Bowser Broadside", "Pump, Pump and Away", "Hyper Hydrants", "Picking Panic", "Treadmill Grill", "Toadstoll Titan", "Aces High", "Bounce 'n' Trounce", "Ice Rink Risk", "Locked Out", "Chip Shot Challenge", "Parasol Plummet", "Messy Memory", "Picture Imperfect", "Mario's Puzzle Party", "The Beat Goes On", "M. P. I. Q.", "Curtain Call", "Water Whirled", "Frigid Bridges", "Awful Tower", "Cheep Cheep Chase", "Pipe Cleaners", "Snowball Summit", "All Fired Up", "Stacked Deck", "Three Door Monty", "Rockin' Raceway", "Merry-Go-Chomp", "Slap Down", "Storm Chasers", "Eye Sore", "Vine With Me", "Popgun Pick-Off", "End of the Line", "Bowser Toss", "Baby Bowser Bonkers", "Motor Rooter", "Silly Screws", "Crowd Cover", "Tick Tock Hop", "Fowl Play", "Mecha-Marathon", "Hey, Batter, Batter!", "Bobbing Bow-loons", "Dorrie Dip", "Swinging with Sharks", "Swing 'n' Swipe", "Stardust Battle", "Game Guy's Roulette", "Game Guy's Lucky 7", "Game Guy's Magic Boxes", "Game Guy's Sweet Surprise", "Dizzy Dinghies", "Mario's Puzzle Party Pro"]
   
    # Create labels, comboboxes, and button for Minigame Replacement tab
    replace_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" Replace  ", font=("Arial", 16))
    replace_label.grid(row=0, column=0)
    combobox_mingames_1 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_1.grid(row=0, column=1)
    with_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" with ", font=("Arial", 16))
    with_label.grid(row=0, column=2)
    combobox_mingames_2 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_2.grid(row=0, column=3)
    parse_minigame_button = ctk.CTkButton(master=tabview.tab("Minigame Replacement"), command=lambda: mgReplaceEvent_mp3(combobox_mingames_1, combobox_mingames_2, minigames_list), text="Generate Codes")
    parse_minigame_button.place(x=10, y=800)

    icon = create_image_icon(tabview.tab("Item Prices"), "assets/items/mushroom.png", 1, 1)
    label = ctk.CTkLabel(master=tabview.tab("Item Prices"), text=" Costs  ", font=("Arial", 16), text_color="red")
    label.grid(row=1, column=2)
    mushroom3 = ctk.CTkEntry(master=tabview.tab("Item Prices"), width=48, font=("Arial", 16, "bold"), placeholder_text="5")
    mushroom3.grid(row=1, column=3)

    icon = create_image_icon(tabview.tab("Item Prices"), "assets/items/skeletonKey.png", 2, 1)
    label = ctk.CTkLabel(master=tabview.tab("Item Prices"), text=" Costs  ", font=("Arial", 16), text_color="red")
    label.grid(row=2, column=2)
    skeletonKey3 = ctk.CTkEntry(master=tabview.tab("Item Prices"), width=48, font=("Arial", 16, "bold"), placeholder_text="5")
    skeletonKey3.grid(row=2, column=3)

    icon = create_image_icon(tabview.tab("Item Prices"), "assets/items/poisonMushroom.png", 3, 1)
    label = ctk.CTkLabel(master=tabview.tab("Item Prices"), text=" Costs  ", font=("Arial", 16), text_color="red")
    label.grid(row=3, column=2)
    poisonMushroom3 = ctk.CTkEntry(master=tabview.tab("Item Prices"), width=48, font=("Arial", 16, "bold"), placeholder_text="5")
    poisonMushroom3.grid(row=3, column=3)

    icon = create_image_icon(tabview.tab("Item Prices"), "assets/items/reverseMushroom.png", 4, 1)
    label = ctk.CTkLabel(master=tabview.tab("Item Prices"), text=" Costs  ", font=("Arial", 16), text_color="red")
    label.grid(row=4, column=2)
    reverseMushroom3 = ctk.CTkEntry(master=tabview.tab("Item Prices"), width=48, font=("Arial", 16, "bold"), placeholder_text="5")
    reverseMushroom3.grid(row=4, column=3)

    icon = create_image_icon(tabview.tab("Item Prices"), "assets/items/goldenMushroom.png", 5, 1)
    label = ctk.CTkLabel(master=tabview.tab("Item Prices"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=5, column=2)
    goldenMushroom3 = ctk.CTkEntry(master=tabview.tab("Item Prices"), width=48, font=("Arial", 16, "bold"), placeholder_text="10")
    goldenMushroom3.grid(row=5, column=3)

    icon = create_image_icon(tabview.tab("Item Prices"), "assets/items/magicLamp.png", 6, 1)
    label = ctk.CTkLabel(master=tabview.tab("Item Prices"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=6, column=2)
    magicLamp3 = ctk.CTkEntry(master=tabview.tab("Item Prices"), width=48, font=("Arial", 16, "bold"), placeholder_text="20")
    magicLamp3.grid(row=6, column=3)

    label = ctk.CTkLabel(master=tabview.tab("Item Prices"), text="    ", font=("Arial", 16))
    label.grid(row=1, column=4)

    icon = create_image_icon(tabview.tab("Item Prices"), "assets/items/warpBlock.png", 1, 6)
    label = ctk.CTkLabel(master=tabview.tab("Item Prices"), text=" Costs  ", font=("Arial", 16), text_color="red")
    label.grid(row=1, column=7)
    warpBlock3 = ctk.CTkEntry(master=tabview.tab("Item Prices"), width=48, font=("Arial", 16, "bold"), placeholder_text="5")
    warpBlock3.grid(row=1, column=8)

    icon = create_image_icon(tabview.tab("Item Prices"), "assets/items/celluarShopper.png", 2, 6)
    label = ctk.CTkLabel(master=tabview.tab("Item Prices"), text=" Costs  ", font=("Arial", 16), text_color="red")
    label.grid(row=2, column=7)
    celluarShopper3 = ctk.CTkEntry(master=tabview.tab("Item Prices"), width=48, font=("Arial", 16, "bold"), placeholder_text="5")
    celluarShopper3.grid(row=2, column=8)

    icon = create_image_icon(tabview.tab("Item Prices"), "assets/items/bowserPhone.png", 3, 6)
    label = ctk.CTkLabel(master=tabview.tab("Item Prices"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=3, column=7)
    bowserPhone3 = ctk.CTkEntry(master=tabview.tab("Item Prices"), width=48, font=("Arial", 16, "bold"), placeholder_text="10")
    bowserPhone3.grid(row=3, column=8)

    icon = create_image_icon(tabview.tab("Item Prices"), "assets/items/duelingGlove.png", 4, 6)
    label = ctk.CTkLabel(master=tabview.tab("Item Prices"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=4, column=7)
    duelingGlove3 = ctk.CTkEntry(master=tabview.tab("Item Prices"), width=48, font=("Arial", 16, "bold"), placeholder_text="10")
    duelingGlove3.grid(row=4, column=8)

    icon = create_image_icon(tabview.tab("Item Prices"), "assets/items/luckyLamp.png", 5, 6)
    label = ctk.CTkLabel(master=tabview.tab("Item Prices"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=5, column=7)
    luckyLamp3 = ctk.CTkEntry(master=tabview.tab("Item Prices"), width=48, font=("Arial", 16, "bold"), placeholder_text="10")
    luckyLamp3.grid(row=5, column=8)

    label = ctk.CTkLabel(master=tabview.tab("Item Prices"), text="    ", font=("Arial", 16))
    label.grid(row=1, column=9)

    icon = create_image_icon(tabview.tab("Item Prices"), "assets/items/bowserSuit.png", 1, 10)
    label = ctk.CTkLabel(master=tabview.tab("Item Prices"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=1, column=11)
    bowserSuit3 = ctk.CTkEntry(master=tabview.tab("Item Prices"), width=48, font=("Arial", 16, "bold"), placeholder_text="5")
    bowserSuit3.grid(row=1, column=12)

    icon = create_image_icon(tabview.tab("Item Prices"), "assets/items/plunderChest.png", 2, 10)
    label = ctk.CTkLabel(master=tabview.tab("Item Prices"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=2, column=11)
    plunderChest3 = ctk.CTkEntry(master=tabview.tab("Item Prices"), width=48, font=("Arial", 16, "bold"), placeholder_text="10")
    plunderChest3.grid(row=2, column=12)

    icon = create_image_icon(tabview.tab("Item Prices"), "assets/items/booBell.png", 3, 10)
    label = ctk.CTkLabel(master=tabview.tab("Item Prices"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=3, column=11)
    booBell3 = ctk.CTkEntry(master=tabview.tab("Item Prices"), width=48, font=("Arial", 16, "bold"), placeholder_text="15")
    booBell3.grid(row=3, column=12)

    icon = create_image_icon(tabview.tab("Item Prices"), "assets/items/booRepellent.png", 4, 10)
    label = ctk.CTkLabel(master=tabview.tab("Item Prices"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=4, column=11)
    booRepellant3 = ctk.CTkEntry(master=tabview.tab("Item Prices"), width=48, font=("Arial", 16, "bold"), placeholder_text="10")
    booRepellant3.grid(row=4, column=12)

    icon = create_image_icon(tabview.tab("Item Prices"), "assets/items/itemBag3.png", 5, 10)
    label = ctk.CTkLabel(master=tabview.tab("Item Prices"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=5, column=11)
    itemBag3 = ctk.CTkEntry(master=tabview.tab("Item Prices"), width=48, font=("Arial", 16, "bold"), placeholder_text="30")
    itemBag3.grid(row=5, column=12)

    parseButtonThree = ctk.CTkButton(master=tabview.tab("Item Prices"), command=lambda: itemsEvent_mp3(mushroom3, skeletonKey3, poisonMushroom3, reverseMushroom3, goldenMushroom3, magicLamp3, warpBlock3, celluarShopper3, bowserPhone3, duelingGlove3, luckyLamp3, bowserSuit3, plunderChest3, booBell3, booRepellant3, itemBag3), text="Generate Codes")
    parseButtonThree.place(x=10, y=800)

    warningLabel = ctk.CTkLabel(master=tabview.tab("Item Prices"), text="These are not weights! 0 doesnt mean disabled.", font=("Arial", 16, "bold"))
    warningLabel.place(x=5, y=310)

    warningLabel = ctk.CTkLabel(master=tabview.tab("Item Prices"), text="Please set the items in RED the LOWEST PRICE and the SAME PRICE.", font=("Arial", 16, "bold"))
    warningLabel.place(x=5, y=280)

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

    parse_stars_button = ctk.CTkButton(master=tabview.tab("Star Handicaps"), command=lambda: handicapEvent_mp3(p1Stars, p2Stars, p3Stars, p4Stars), text="Generate Codes")
    parse_stars_button.place(x=10, y=800)

    # List of minigame names
    items3 = ["None", "Mushroom", "Skeleton Key", "Poison Mushroom", "Reverse Mushroo", "Cellular Shopper", "Warp Block", "Plunder Chest", "Bowser Phone", "Dueling Glove", "Lucky Lamp", "Golden Mushroom", "Boo Bell", "Boo Repellant", "Bowser Suit", "Magic Lamp", "Koopa Kard", "Barter Box", "Lucky Charm", "Wacky Watch"]
   
    label = ctk.CTkLabel(master=tabview.tab("Item Replacement"), text=" Replace  ", font=("Arial", 16))
    label.grid(row=0, column=0)

    itemSwap411 = ctk.CTkComboBox(master=tabview.tab("Item Replacement"), values=items3)
    itemSwap411.grid(row=0, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Item Replacement"), text=" with ", font=("Arial", 16))
    label.grid(row=0, column=2)

    itemSwap412 = ctk.CTkComboBox(master=tabview.tab("Item Replacement"), values=items3)
    itemSwap412.grid(row=0, column=3)

    parseButton = ctk.CTkButton(master=tabview.tab("Item Replacement"), command=lambda: itemReplace_mp3(itemSwap411, itemSwap412, items3), text="Generate Codes")
    parseButton.place(x=10, y=800)

    return frame