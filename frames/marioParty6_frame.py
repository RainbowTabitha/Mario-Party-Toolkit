# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

# Import necessary functions and modules
from functions import *
from events.marioParty6_bonusStarReplace import *
from events.marioParty6_coins import *
from events.marioParty6_initialItems import *
from events.marioParty6_mgreplace import *
from events.marioParty6_items import *
from events.marioParty6_handicap import *
from events.marioParty6_spaceReplace import *
from events.marioParty6_battle import *

# Import custom tkinter module as ctk
import customtkinter as ctk
from CTkToolTip import *

# Function to create the main interface for Mario Party 1
def create_mario_party_6_interface(frame):
    # Create a tabbed interface
    tabview = ctk.CTkTabview(frame, width=1110, height=885, fg_color=("#fcfcfc", "#323232"))
    tabview.grid(padx=10, pady=10)
    tabview.add("Coins Mods")
    tabview.add("Minigame Replacement")
    tabview.add("Orb Mods")
    tabview.add("Space Replacement")
    tabview.add("Initial Orbs")
    tabview.add("Battle Minigame")
    tabview.add("Star Handicaps")
    tabview.add("Bonus Star Replacement")
    tabview.set("Coins Mods")
    
    # Function to create an entry field and checkbox
    def create_entry(tab, row, icon_path, label_text, color):
        create_image_icon(tab, icon_path, row, 1)
        label = ctk.CTkLabel(master=tab, text=label_text, font=("Arial", 16))
        label.grid(row=row, column=2, sticky="w", pady=15)
        entry = ctk.CTkEntry(master=tab, width=48, font=("Arial", 16, "bold"))
        entry.grid(row=row, column=3)
        label1 = ctk.CTkLabel(master=tab, text=color, font=("Arial", 16))
        label1.grid(row=row, column=4, sticky="w")
        return entry
    
    # Function to create an entry field and checkbox
    def create_entry2(tab, row, icon_path, label_text, color):
        create_image_icon(tab, icon_path, row, 5)
        label = ctk.CTkLabel(master=tab, text=label_text, font=("Arial", 16))
        label.grid(row=row, column=6, sticky="w", pady=15)
        entry = ctk.CTkEntry(master=tab, width=48, font=("Arial", 16, "bold"))
        entry.grid(row=row, column=7)
        label1 = ctk.CTkLabel(master=tab, text=color, font=("Arial", 16))
        label1.grid(row=row, column=8, sticky="w")
        return entry

    # Create entry fields and checkboxes for Coins Mods tab
    blue_entry = create_entry(tabview.tab("Coins Mods"), 1, "assets/eventTags/blueSpace.png", " Gain  ", " Coins on a Blue Space.")
    red_entry = create_entry(tabview.tab("Coins Mods"), 2, "assets/eventTags/redSpace.png", " Lose  ", " Coins on a Red Space.")
    character_entry = create_entry(tabview.tab("Coins Mods"), 3, "assets/eventTags/characterSpace.png", " Gain  ", " Coins on your own Character Space.")
    mgWin_entry = create_entry(tabview.tab("Coins Mods"), 4, "assets/eventTags/miniGame.png", " Gain  ", " Coins when winning a Minigame.")
    star_entry = create_entry(tabview.tab("Coins Mods"), 5, "assets/eventTags/starSpace.png", " Costs ", " Coins to buy a Star at a Star Space and Flutter.       ")
    star_entryTooltip = CTkToolTip(star_entry, message="Works on Treetop, Garage, Castaway, and Clockwork.")
    
    pinkBooCoins_entry = create_entry2(tabview.tab("Coins Mods"), 1, "assets/eventTags/pinkBooCoins.png", " Costs ", " Coins to steal Coins.")
    pinkBooMin_entry = create_entry2(tabview.tab("Coins Mods"), 2, "assets/eventTags/pinkBooCoins.png", " Steal ", " Mininum when stealing Coins.")
    pinkBooStar_entry = create_entry2(tabview.tab("Coins Mods"), 3, "assets/eventTags/pinkBooStars.png", " Costs ", " Coins to steal a Star.")
    initial_entry = create_entry2(tabview.tab("Coins Mods"), 4, "assets/eventTags/initialCoins.png", " Gain ", " Coins at the start of the game.")
    zap_entry = create_entry2(tabview.tab("Coins Mods"), 5, "assets/items/zapCapsule.png", " Lose ", " Coins from Zaps.")

    # Create button to generate coins modification codes
    parse_coins_button = ctk.CTkButton(master=tabview.tab("Coins Mods"), command=lambda: coinsEvent_mp6(blue_entry, red_entry, character_entry, mgWin_entry, star_entry, pinkBooCoins_entry, pinkBooMin_entry, pinkBooStar_entry, initial_entry, zap_entry), text="Generate Codes")
    parse_coins_button.place(x=10, y=800)

    # List of minigame names
    minigames_list = ["Smashdance", "Odd Card Out", "Freeze Frame", "What Goes Up...", "Granite Getaway", "Circuit Maximus", "Catch You Letter", "Snow Whirled", "Daft Rafts", "Tricky Tires", "Treasure Trawlers", "Memory Lane", "Mowtown", "Cannonball Fun", "Note to Self", "Same is Lame", "Light Up My Night", "Lift Leapers", "Blooper Scooper", "Trap Ease Artist", "Pokey Punch-out", "Money Belt", "Cash Flow", "Cog Jog", "Sink or Swim", "Snow Brawl", "Ball Dozers", "Surge and Destroy", "Pop Star", "Stage Fright", "Conveyor Bolt", "Crate and Peril", "Ray of Fright", "Dust 'til Dawn", "Garden Grab", "Pixel Perfect", "Slot Trot", "Gondola Glide", "Light Breeze", "Body Builder", "Mole-it!", "Cashapult", "Jump the Gun", "Rocky Road", "Clean Team", "Hyper Sniper", "Insectiride", "Sunday Drivers", "Stamp By Me", "Throw Me a Bone", "Black Hole Boogie", "Full Tilt", "Sumo of Doom-o", "O-Zone", "Pitifall", "Mass Meteor", "Lunar-tics", "T Minus Five", "Asteroad Rage", "Boo'd Off the Stage", "Boonanza!", "Trick or Tree", "Something's Amist", "Wrasslin' Rapids", "Verbal Assault", "Shoot Yer Mouth Off", "Talkie Walkie", "Burnstile", "Word Herd", "Fruit Talktail", "Pit Boss", "Dizzy Rotisserie", "Dark 'n Crispy", "Tally Me Banana", "Banana Shake", "Pier Factor", "Seer Terror", "Block Star", "Lab Brats", "Strawberry Shortfuse", "Control Shtick", "Dunk Bros."]
    # Create labels, comboboxes, and button for Minigame Replacement tab
    replace_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" Replace  ", font=("Arial", 16))
    replace_label.grid(row=0, column=0)
    combobox_mingames_1 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_1.grid(row=0, column=1)
    with_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" with ", font=("Arial", 16))
    with_label.grid(row=0, column=2)
    combobox_mingames_2 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_2.grid(row=0, column=3)
    parse_minigame_button = ctk.CTkButton(master=tabview.tab("Minigame Replacement"), command=lambda: mgReplaceEvent_mp6(combobox_mingames_1, combobox_mingames_2, minigames_list), text="Generate Codes")
    parse_minigame_button.place(x=10, y=800)

    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/mushroomCapsule.png", 2, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=2, column=2)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" 5  ", font=("Arial", 24, "bold"))
    label.grid(row=2, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=2, column=4)
    mushroomCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    mushroomCapsuleWeight6.grid(row=2, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.   ", font=("Arial", 16))
    label.grid(row=2, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/goldenMushroomCapsule.png", 3, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=3, column=2)
    goldenMushroomCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    goldenMushroomCapsulePrice6.grid(row=3, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=3, column=4)
    goldenMushroomCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    goldenMushroomCapsuleWeight6.grid(row=3, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=3, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/slowMushroomCapsule.png", 4, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=4, column=2)
    slowMushroomCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    slowMushroomCapsulePrice6.grid(row=4, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=4, column=4)
    slowMushroomCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    slowMushroomCapsuleWeight6.grid(row=4, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=4, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/metalMushroomCapsule.png", 5, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=5, column=2)
    metalMushroomCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    metalMushroomCapsulePrice6.grid(row=5, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=5, column=4)
    metalMushroomCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    metalMushroomCapsuleWeight6.grid(row=5, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=5, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/warpCapsule.png", 6, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=6, column=2)
    warpPipeCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    warpPipeCapsulePrice6.grid(row=6, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=6, column=4)
    warpPipeCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    warpPipeCapsuleWeight6.grid(row=6, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=6, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/wigglerCapsule.png", 8, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=8, column=2)
    flutterCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    flutterCapsulePrice6.grid(row=8, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=8, column=4)
    flutterCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    flutterCapsuleWeight6.grid(row=8, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=8, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/cursedMushroomCapsule.png", 9, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=9, column=2)
    cursedMushroomCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    cursedMushroomCapsulePrice6.grid(row=9, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=9, column=4)
    cursedMushroomCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    cursedMushroomCapsuleWeight6.grid(row=9, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=9, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/spinyCapsule.png", 10, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=10, column=2)
    spinyCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    spinyCapsulePrice6.grid(row=10, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=10, column=4)
    spinyCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    spinyCapsuleWeight6.grid(row=10, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=10, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/goombaCapsule.png", 11, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=11, column=2)
    goombaCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    goombaCapsulePrice6.grid(row=11, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=11, column=4)
    goombaCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    goombaCapsuleWeight6.grid(row=11, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=11, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/plantCapsule.png", 12, 1)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=12, column=2)
    plantCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    plantCapsulePrice6.grid(row=12, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=12, column=4)
    plantCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    plantCapsuleWeight6.grid(row=12, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.  ", font=("Arial", 16))
    label.grid(row=12, column=6)

    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text="", font=("Arial", 16))
    label.grid(row=2, column=6)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/kamekCapsule.png", 2, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=2, column=9)
    kamekCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    kamekCapsulePrice6.grid(row=2, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=2, column=11)
    kamekCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    kamekCapsuleWeight6.grid(row=2, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.  ", font=("Arial", 16))
    label.grid(row=2, column=13)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/toadyCapsule.png", 3, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=3, column=9)
    toadyCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    toadyCapsulePrice6.grid(row=3, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=3, column=11)
    toadyCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    toadyCapsuleWeight6.grid(row=3, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=3, column=13)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/blizzardCapsule.png", 4, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=4, column=9)
    blizzardCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    blizzardCapsulePrice6.grid(row=4, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=4, column=11)
    blizzardCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    blizzardCapsuleWeight6.grid(row=4, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=4, column=13)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/kleptoCapsule.png", 5, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=5, column=9)
    kleptoCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    kleptoCapsulePrice6.grid(row=5, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=5, column=11)
    kleptoCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    kleptoCapsuleWeight6.grid(row=5, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=5, column=13)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/pinkBooCapsule.png", 6, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=6, column=9)
    pinkBooCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    pinkBooCapsulePrice6.grid(row=6, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=6, column=11)
    pinkBooCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    pinkBooCapsuleWeight6.grid(row=6, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=6, column=13)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/podobooCapsule.png", 6, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=6, column=9)
    podobooCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    podobooCapsulePrice6.grid(row=6, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=6, column=11)
    podobooCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    podobooCapsuleWeight6.grid(row=6, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=6, column=13)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/zapCapsule.png", 8, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=8, column=9)
    zapCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    zapCapsulePrice6.grid(row=8, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=8, column=11)
    zapCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    zapCapsuleWeight6.grid(row=8, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=8, column=13)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/tweesterCapsule.png", 9, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=9, column=9)
    tweesterCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    tweesterCapsulePrice6.grid(row=9, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=9, column=11)
    tweesterCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    tweesterCapsuleWeight6.grid(row=9, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=9, column=13)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/thwompCapsule.png", 10, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=10, column=9)
    thwompCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    thwompCapsulePrice6.grid(row=10, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=10, column=11)
    thwompCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    thwompCapsuleWeight6.grid(row=10, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=10, column=13)
    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/bulletBillCapsule.png", 11, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=11, column=9)
    bulletBillCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    bulletBillCapsulePrice6.grid(row=11, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=11, column=11)
    bulletBillCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    bulletBillCapsuleWeight6.grid(row=11, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=11, column=13)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/bombCapsule.png", 12, 8)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=12, column=9)
    bombCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    bombCapsulePrice6.grid(row=12, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=12, column=11)
    bombCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    bombCapsuleWeight6.grid(row=12, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.  ", font=("Arial", 16))
    label.grid(row=12, column=13)

    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text="", font=("Arial", 16))
    label.grid(row=2, column=14)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/paraTroopaCapsule.png", 2, 15)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=2, column=16)
    paraTroopaCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    paraTroopaCapsulePrice6.grid(row=2, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=2, column=18)
    paraTroopaCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    paraTroopaCapsuleWeight6.grid(row=2, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=2, column=20)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/snackCapsule.png", 3, 15)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=3, column=16)
    snackCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    snackCapsulePrice6.grid(row=3, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=3, column=18)
    snackCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    snackCapsuleWeight6.grid(row=3, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=3, column=20)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/gaddlightCapsule.png", 4, 15)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=4, column=16)
    gaddLightCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    gaddLightCapsulePrice6.grid(row=4, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=4, column=18)
    gaddLightCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    gaddLightCapsuleWeight6.grid(row=4, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=4, column=20)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/pinkBooCapsule.png", 5, 15)
    labelBoo1 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    labelBoo1.grid(row=5, column=16)
    pinkBooCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    pinkBooCapsulePrice6.grid(row=5, column=17)
    labelBoo2 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    labelBoo2.grid(row=5, column=18)
    pinkBooCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    pinkBooCapsuleWeight6.grid(row=5, column=19)
    labelBoo3 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    labelBoo3.grid(row=5, column=20)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/chanceCapsule.png", 6, 15)
    labelChance1 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    labelChance1.grid(row=6, column=16)
    chanceTimeCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    chanceTimeCapsulePrice6.grid(row=6, column=17)
    labelChance2 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    labelChance2.grid(row=6, column=18)
    chanceTimeCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    chanceTimeCapsuleWeight6.grid(row=6, column=19)
    labelChance3 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    labelChance3.grid(row=6, column=20)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/dkCapsule.png", 8, 15)
    labelDK1 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    labelDK1.grid(row=8, column=16)
    dkCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    dkCapsulePrice6.grid(row=8, column=17)
    labelDK2 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    labelDK2.grid(row=8, column=18)
    dkCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    dkCapsuleWeight6.grid(row=8, column=19)
    labelDK3 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    labelDK3.grid(row=8, column=20)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/bowserCapsule.png", 9, 15)
    labelBowser1 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    labelBowser1.grid(row=9, column=16)
    bowserCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    bowserCapsulePrice6.grid(row=9, column=17)
    labelBowser2 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    labelBowser2.grid(row=9, column=18)
    bowserCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    bowserCapsuleWeight6.grid(row=9, column=19)
    labelBowser3 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    labelBowser3.grid(row=9, column=20)

    
    icon = create_image_icon(tabview.tab("Orb Mods"), "assets/items/duelCapsule.png", 10, 15)
    labelDuel1 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" Costs  ", font=("Arial", 16))
    labelDuel1.grid(row=10, column=16)
    duelCapsulePrice6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    duelCapsulePrice6.grid(row=10, column=17)
    labelDuel2 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" and is ", font=("Arial", 16))
    labelDuel2.grid(row=10, column=18)
    duelCapsuleWeight6 = ctk.CTkEntry(master=tabview.tab("Orb Mods"), width=48, font=("Arial", 16, "bold"))
    duelCapsuleWeight6.grid(row=10, column=19)
    labelDuel3 = ctk.CTkLabel(master=tabview.tab("Orb Mods"), text=" % common.", font=("Arial", 16))
    labelDuel3.grid(row=10, column=20)


    parseButton = ctk.CTkButton(master=tabview.tab("Orb Mods"), command=lambda: itemsEvent_mp6(warpPipeCapsuleWeight6, warpPipeCapsulePrice6, mushroomCapsuleWeight6, goldenMushroomCapsulePrice6, goldenMushroomCapsuleWeight6, slowMushroomCapsulePrice6, slowMushroomCapsuleWeight6, metalMushroomCapsulePrice6, metalMushroomCapsuleWeight6, bulletBillCapsulePrice6, bulletBillCapsuleWeight6, flutterCapsulePrice6, flutterCapsuleWeight6, cursedMushroomCapsulePrice6, cursedMushroomCapsuleWeight6, spinyCapsulePrice6, spinyCapsuleWeight6, goombaCapsulePrice6, goombaCapsuleWeight6, plantCapsulePrice6, plantCapsuleWeight6, kleptoCapsulePrice6, kleptoCapsuleWeight6, toadyCapsulePrice6, toadyCapsuleWeight6, kamekCapsulePrice6, kamekCapsuleWeight6, blizzardCapsulePrice6, blizzardCapsuleWeight6, podobooCapsulePrice6, podobooCapsuleWeight6, zapCapsulePrice6, zapCapsuleWeight6, tweesterCapsulePrice6, tweesterCapsuleWeight6, thwompCapsulePrice6, thwompCapsuleWeight6, bombCapsulePrice6, bombCapsuleWeight6, paraTroopaCapsulePrice6, paraTroopaCapsuleWeight6, snackCapsulePrice6, snackCapsuleWeight6, gaddLightCapsulePrice6, gaddLightCapsuleWeight6, pinkBooCapsulePrice6 if hide_custom == False else "0", pinkBooCapsuleWeight6 if hide_custom == False else "0", chanceTimeCapsulePrice6 if hide_custom == False else "0", chanceTimeCapsuleWeight6 if hide_custom == False else "0", bowserCapsulePrice6 if hide_custom == False else "0", bowserCapsuleWeight6 if hide_custom == False else "0", dkCapsulePrice6 if hide_custom == False else "0", dkCapsuleWeight6 if hide_custom == False else "0", duelCapsulePrice6 if hide_custom == False else "0", duelCapsuleWeight6  if hide_custom == False else "0"), text="Generate Codes")
    parseButton.place(x=10, y=800)

    parseButton = ctk.CTkButton(master=tabview.tab("Orb Mods"), command=lambda: savePresetItems6(warpPipeCapsuleWeight6, warpPipeCapsulePrice6, mushroomCapsuleWeight6, goldenMushroomCapsulePrice6, goldenMushroomCapsuleWeight6, slowMushroomCapsulePrice6, slowMushroomCapsuleWeight6, metalMushroomCapsulePrice6, metalMushroomCapsuleWeight6, bulletBillCapsulePrice6, bulletBillCapsuleWeight6, flutterCapsulePrice6, flutterCapsuleWeight6, cursedMushroomCapsulePrice6, cursedMushroomCapsuleWeight6, spinyCapsulePrice6, spinyCapsuleWeight6, goombaCapsulePrice6, goombaCapsuleWeight6, plantCapsulePrice6, plantCapsuleWeight6, kleptoCapsulePrice6, kleptoCapsuleWeight6, toadyCapsulePrice6, toadyCapsuleWeight6, kamekCapsulePrice6, kamekCapsuleWeight6, blizzardCapsulePrice6, blizzardCapsuleWeight6, podobooCapsulePrice6, podobooCapsuleWeight6, zapCapsulePrice6, zapCapsuleWeight6, tweesterCapsulePrice6, tweesterCapsuleWeight6, thwompCapsulePrice6, thwompCapsuleWeight6, bombCapsulePrice6, bombCapsuleWeight6, paraTroopaCapsulePrice6, paraTroopaCapsuleWeight6, snackCapsulePrice6, snackCapsuleWeight6, gaddLightCapsulePrice6, gaddLightCapsuleWeight6, pinkBooCapsulePrice6 if hide_custom == False else "0", pinkBooCapsuleWeight6 if hide_custom == False else "0", chanceTimeCapsulePrice6 if hide_custom == False else "0", chanceTimeCapsuleWeight6 if hide_custom == False else "0", bowserCapsulePrice6 if hide_custom == False else "0", bowserCapsuleWeight6 if hide_custom == False else "0", dkCapsulePrice6 if hide_custom == False else "0", dkCapsuleWeight6 if hide_custom == False else "0", duelCapsulePrice6 if hide_custom == False else "0", duelCapsuleWeight6  if hide_custom == False else "0"), text="Save Preset")
    parseButton.place(x=160, y=800)

    parseButton = ctk.CTkButton(master=tabview.tab("Orb Mods"), command=lambda: loadPresetItems6(warpPipeCapsuleWeight6, warpPipeCapsulePrice6, mushroomCapsuleWeight6, goldenMushroomCapsulePrice6, goldenMushroomCapsuleWeight6, slowMushroomCapsulePrice6, slowMushroomCapsuleWeight6, metalMushroomCapsulePrice6, metalMushroomCapsuleWeight6, bulletBillCapsulePrice6, bulletBillCapsuleWeight6, flutterCapsulePrice6, flutterCapsuleWeight6, cursedMushroomCapsulePrice6, cursedMushroomCapsuleWeight6, spinyCapsulePrice6, spinyCapsuleWeight6, goombaCapsulePrice6, goombaCapsuleWeight6, plantCapsulePrice6, plantCapsuleWeight6, kleptoCapsulePrice6, kleptoCapsuleWeight6, toadyCapsulePrice6, toadyCapsuleWeight6, kamekCapsulePrice6, kamekCapsuleWeight6, blizzardCapsulePrice6, blizzardCapsuleWeight6, podobooCapsulePrice6, podobooCapsuleWeight6, zapCapsulePrice6, zapCapsuleWeight6, tweesterCapsulePrice6, tweesterCapsuleWeight6, thwompCapsulePrice6, thwompCapsuleWeight6, bombCapsulePrice6, bombCapsuleWeight6, paraTroopaCapsulePrice6, paraTroopaCapsuleWeight6, snackCapsulePrice6, snackCapsuleWeight6, gaddLightCapsulePrice6, gaddLightCapsuleWeight6, pinkBooCapsulePrice6 if hide_custom == False else "0", pinkBooCapsuleWeight6 if hide_custom == False else "0", chanceTimeCapsulePrice6 if hide_custom == False else "0", chanceTimeCapsuleWeight6 if hide_custom == False else "0", bowserCapsulePrice6 if hide_custom == False else "0", bowserCapsuleWeight6 if hide_custom == False else "0", dkCapsulePrice6 if hide_custom == False else "0", dkCapsuleWeight6 if hide_custom == False else "0", duelCapsulePrice6 if hide_custom == False else "0", duelCapsuleWeight6  if hide_custom == False else "0"), text="Load Preset")
    parseButton.place(x=310, y=800)

    hideCustomSwitch = ctk.CTkSwitch(master=tabview.tab("Orb Mods"), text="Show Custom Orbs")
    hideCustomSwitch.place(x=460, y=800)

    global hide_custom
    hide_custom = False

    def toggle_hide_custom():
        global hide_custom
        hide_custom = not hide_custom

        if hide_custom:
            duelCapsulePrice6.grid_forget()
            duelCapsuleWeight6.grid_forget()
            bowserCapsulePrice6.grid_forget()
            bowserCapsuleWeight6.grid_forget()
            dkCapsulePrice6.grid_forget()
            dkCapsuleWeight6.grid_forget()
            pinkBooCapsulePrice6.grid_forget()
            pinkBooCapsuleWeight6.grid_forget()
            chanceTimeCapsulePrice6.grid_forget()
            chanceTimeCapsuleWeight6.grid_forget()
            labelDuel1.grid_forget()
            labelDuel2.grid_forget()
            labelDuel3.grid_forget()
            labelDK1.grid_forget()
            labelDK2.grid_forget()
            labelDK3.grid_forget()
            labelBowser1.grid_forget()
            labelBowser2.grid_forget()
            labelBowser3.grid_forget()
            labelChance1.grid_forget()
            labelChance2.grid_forget()
            labelChance3.grid_forget()
            labelBoo1.grid_forget()
            labelBoo2.grid_forget()
            labelBoo3.grid_forget()
            for widget in tabview.tab("Orb Mods").winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "10:15":
                    widget.grid_forget()
            for widget in tabview.tab("Orb Mods").winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "9:15":
                    widget.grid_forget()
            for widget in tabview.tab("Orb Mods").winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "8:15":
                    widget.grid_forget()
            for widget in tabview.tab("Orb Mods").winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "5:15":
                    widget.grid_forget()
            for widget in tabview.tab("Orb Mods").winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "6:15":
                    widget.grid_forget()
        else:
            for widget in tabview.tab("Orb Mods").winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "10:15":
                    widget.grid(row=10, column=15)
            for widget in tabview.tab("Orb Mods").winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "9:15":
                    widget.grid(row=9, column=15)
            for widget in tabview.tab("Orb Mods").winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "8:15":
                    widget.grid(row=8, column=15)
            for widget in tabview.tab("Orb Mods").winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "5:15":
                    widget.grid(row=5, column=15)
            for widget in tabview.tab("Orb Mods").winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "6:15":
                    widget.grid(row=6, column=15)
            duelCapsulePrice6.grid(row=10, column=17)
            duelCapsuleWeight6.grid(row=10, column=19)
            bowserCapsulePrice6.grid(row=9, column=17)
            bowserCapsuleWeight6.grid(row=9, column=19)
            dkCapsulePrice6.grid(row=8, column=17)
            dkCapsuleWeight6.grid(row=8, column=19)
            pinkBooCapsulePrice6.grid(row=5, column=17)
            pinkBooCapsuleWeight6.grid(row=5, column=19)
            chanceTimeCapsulePrice6.grid(row=6, column=17)
            chanceTimeCapsuleWeight6.grid(row=6, column=19)
            labelDuel1.grid(row=10, column=16)
            labelDuel2.grid(row=10, column=18)
            labelDuel3.grid(row=10, column=20)
            labelDK1.grid(row=9, column=16)
            labelDK2.grid(row=9, column=18)
            labelDK3.grid(row=9, column=20)
            labelBowser1.grid(row=8, column=16)
            labelBowser2.grid(row=8, column=18)
            labelBowser3.grid(row=8, column=20)
            labelChance1.grid(row=6, column=16)
            labelChance2.grid(row=6, column=18)
            labelChance3.grid(row=6, column=20)
            labelBoo1.grid(row=5, column=16)
            labelBoo2.grid(row=5, column=18)
            labelBoo3.grid(row=5, column=20)

    hideCustomSwitch.configure(command=toggle_hide_custom)
    toggle_hide_custom()



    spaces6 = ["None", "Invisible Space", "Blue Space", "Red Space", "Happening Space", "Chance Time Space", "Duel Space", "Bowser/DK Space", "Orb Space"]
    
    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" Replace  ", font=("Arial", 16))
    label.grid(row=0, column=0)

    spaceRep411 = ctk.CTkComboBox(master=tabview.tab("Space Replacement"), values=spaces6)
    spaceRep411.grid(row=0, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" with ", font=("Arial", 16))
    label.grid(row=0, column=2)

    spaceRep421 = ctk.CTkComboBox(master=tabview.tab("Space Replacement"), values=spaces6)
    spaceRep421.grid(row=0, column=3)

    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" (Slot A) ", font=("Arial", 16))
    label.grid(row=0, column=4)

    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" Replace  ", font=("Arial", 16))
    label.grid(row=1, column=0)

    spaceRep412 = ctk.CTkComboBox(master=tabview.tab("Space Replacement"), values=spaces6)
    spaceRep412.grid(row=1, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" with ", font=("Arial", 16))
    label.grid(row=1, column=2)

    spaceRep422 = ctk.CTkComboBox(master=tabview.tab("Space Replacement"), values=spaces6)
    spaceRep422.grid(row=1, column=3)

    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" (Slot B) ", font=("Arial", 16))
    label.grid(row=1, column=4)

    parseButton = ctk.CTkButton(master=tabview.tab("Space Replacement"), command=lambda: spaceReplaceEvent_mp6(spaceRep411, spaceRep421, spaceRep412, spaceRep422, spaces6), text="Generate Codes")
    parseButton.place(x=10, y=800)

    items6 = ["None", "Mushroom", "Golden Mushroom", "Sluggish 'Shroom", "Metal Mushroom", "Bullet Bill", "Warp Pipe", "Flutter", "Cursed Mushroom", "Spiny", "Goomba", "Piranha Plant", "Klepto", "Toady", "Kamek", "Mr. Blizzard", "Podoboo", "Zap", "Tweester", "Thwomp", "Bob-omb", "Paratroopa", "Snack", "Boo-away", "Duel", "Miracle", "Bowser", "Donkey Kong", "Pink Boo"]
    
    label = ctk.CTkLabel(master=tabview.tab("Initial Orbs"), text=" Item 1:  ", font=("Arial", 16))
    label.grid(row=0, column=0)

    initalItem41 = ctk.CTkComboBox(master=tabview.tab("Initial Orbs"), values=items6)
    initalItem41.grid(row=0, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Initial Orbs"), text=" Item 2:  ", font=("Arial", 16))
    label.grid(row=1, column=0)

    initalItem42 = ctk.CTkComboBox(master=tabview.tab("Initial Orbs"), values=items6)
    initalItem42.grid(row=1, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Initial Orbs"), text=" Item 3:  ", font=("Arial", 16))
    label.grid(row=2, column=0)

    initalItem43 = ctk.CTkComboBox(master=tabview.tab("Initial Orbs"), values=items6)
    initalItem43.grid(row=2, column=1)

    parseButton = ctk.CTkButton(master=tabview.tab("Initial Orbs"), command=lambda: initialItemsEvent_mp6(initalItem41, initalItem42, initalItem43, items6), text="Generate Codes")
    parseButton.place(x=10, y=800)

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

    parse_stars_button = ctk.CTkButton(master=tabview.tab("Star Handicaps"), command=lambda: handicapEvent_mp6(p1Stars, p2Stars, p3Stars, p4Stars), text="Generate Codes")
    parse_stars_button.place(x=10, y=800)

    stars6 = ["None", "Blue Star", "Red Star", "Character Space Star", "Happening Star", "Bowser Star", "Chance Time Star", "Duel Star", "DK Star", "Minigame Star", "Current Coins Star", "Coin Star", "Star Star", "Orb Star"]
    
    label = ctk.CTkLabel(master=tabview.tab("Bonus Star Replacement"), text=" Replace Minigame Star with:  ", font=("Arial", 16))
    label.grid(row=0, column=0, sticky="w")

    star1 = ctk.CTkComboBox(master=tabview.tab("Bonus Star Replacement"), values=stars6)
    star1.grid(row=0, column=1, pady=10)

    label = ctk.CTkLabel(master=tabview.tab("Bonus Star Replacement"), text=" Replace Orb Star with:  ", font=("Arial", 16))
    label.grid(row=1, column=0, sticky="w")

    star2 = ctk.CTkComboBox(master=tabview.tab("Bonus Star Replacement"), values=stars6)
    star2.grid(row=1, column=1, pady=10)

    label = ctk.CTkLabel(master=tabview.tab("Bonus Star Replacement"), text=" Replace Happening Star with:  ", font=("Arial", 16))
    label.grid(row=2, column=0, sticky="w")

    star3 = ctk.CTkComboBox(master=tabview.tab("Bonus Star Replacement"), values=stars6)
    star3.grid(row=2, column=1, pady=10)

    parseButton = ctk.CTkButton(master=tabview.tab("Bonus Star Replacement"), command=lambda: customBonusStarEvent_mp6(star1, star2, star3, stars6), text="Generate Codes")
    parseButton.place(x=10, y=800)

    label = ctk.CTkLabel(master=tabview.tab("Battle Minigame"), text=" Replace 5 Coins with  ", font=("Arial", 16))
    label.grid(row=0, column=1, pady=10)
    fiveCoins = ctk.CTkEntry(master=tabview.tab("Battle Minigame"), width=48, font=("Arial", 16, "bold"))
    fiveCoins.grid(row=0, column=2)
    label = ctk.CTkLabel(master=tabview.tab("Battle Minigame"), text=" Coins ", font=("Arial", 16))
    label.grid(row=0, column=3)
    
    label = ctk.CTkLabel(master=tabview.tab("Battle Minigame"), text=" Replace 10 Coins with  ", font=("Arial", 16))
    label.grid(row=1, column=1, pady=10)
    tenCoins = ctk.CTkEntry(master=tabview.tab("Battle Minigame"), width=48, font=("Arial", 16, "bold"))
    tenCoins.grid(row=1, column=2)
    label = ctk.CTkLabel(master=tabview.tab("Battle Minigame"), text=" Coins ", font=("Arial", 16))
    label.grid(row=1, column=3)

    label = ctk.CTkLabel(master=tabview.tab("Battle Minigame"), text=" Replace 20 Coins with  ", font=("Arial", 16))
    label.grid(row=2, column=1, pady=10)
    twentyCoins = ctk.CTkEntry(master=tabview.tab("Battle Minigame"), width=48, font=("Arial", 16, "bold"))
    twentyCoins.grid(row=2, column=2)
    label = ctk.CTkLabel(master=tabview.tab("Battle Minigame"), text=" Coins ", font=("Arial", 16))
    label.grid(row=2, column=3)

    label = ctk.CTkLabel(master=tabview.tab("Battle Minigame"), text=" Replace 30 Coins with  ", font=("Arial", 16))
    label.grid(row=3, column=1, pady=10)
    thirtyCoins = ctk.CTkEntry(master=tabview.tab("Battle Minigame"), width=48, font=("Arial", 16, "bold"))
    thirtyCoins.grid(row=3, column=2)
    label = ctk.CTkLabel(master=tabview.tab("Battle Minigame"), text=" Coins ", font=("Arial", 16))
    label.grid(row=3, column=3)

    label = ctk.CTkLabel(master=tabview.tab("Battle Minigame"), text=" Replace 50 Coins with  ", font=("Arial", 16))
    label.grid(row=4, column=1, pady=10)
    fiftyCoins = ctk.CTkEntry(master=tabview.tab("Battle Minigame"), width=48, font=("Arial", 16, "bold"))
    fiftyCoins.grid(row=4, column=2)
    label = ctk.CTkLabel(master=tabview.tab("Battle Minigame"), text=" Coins ", font=("Arial", 16))
    label.grid(row=4, column=3)

    parse_stars_button = ctk.CTkButton(master=tabview.tab("Battle Minigame"), command=lambda: battleCoins_mp6(fiveCoins, tenCoins, twentyCoins, thirtyCoins, fiftyCoins), text="Generate Codes")
    parse_stars_button.place(x=10, y=800)

    return frame
    
