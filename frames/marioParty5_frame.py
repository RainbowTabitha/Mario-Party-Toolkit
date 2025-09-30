# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (tabitha@tabs.gay)
# Date: 7/12/2024
# License: MIT
# ============================================

# Import necessary functions and modules
from functions import *
from events.marioParty5_bonusStarReplace import *
from events.marioParty5_coins import *
from events.marioParty5_handicap import *
from events.marioParty5_mgreplace import *
from events.marioParty5_items import *
from events.marioParty5_boardSpecific import *
from events.marioParty5_battle import *

# Import custom tkinter module as ctk
import customtkinter as ctk

# Function to create the main interface for Mario Party 1
def create_mario_party_5_interface(frame):
    # Create a tabbed interface
    tabview = ctk.CTkTabview(frame, width=1110, height=885, fg_color=("#fcfcfc", "#323232"))
    tabview.grid(padx=10, pady=10)
    tabview.add("Coins Mods")
    tabview.add("Minigame Replacement")
    tabview.add("Capsule Mods")
    tabview.add("Bonus Star Replacement")
    tabview.add("Star Handicaps")
    tabview.add("Battle Minigame")
    tabview.add("Board Specific")
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

    # Create entry fields and checkboxes for Coins Mods tab
    blue_entry = create_entry(tabview.tab("Coins Mods"), 1, "assets/eventTags/blueSpace.png", " Gain  ", " Coins on a Blue Space.")
    red_entry = create_entry(tabview.tab("Coins Mods"), 2, "assets/eventTags/redSpace.png", " Lose  ", " Coins on a Red Space.")
    mgWin_entry = create_entry(tabview.tab("Coins Mods"), 3, "assets/eventTags/miniGame.png", " Gain  ", " Coins when winning a Minigame.")
    star_entry = create_entry(tabview.tab("Coins Mods"), 4, "assets/eventTags/starSpace.png", " Costs ", " Coins to buy a Star at a Star Space.")
    koopaBank_entry = create_entry(tabview.tab("Coins Mods"), 5, "assets/items/koopaBankCapsule.png", " Lend ", " Coins to Koopa Bank.")
    wiggler_entry = create_entry(tabview.tab("Coins Mods"), 6, "assets/eventTags/wigglerCapsule.png", " Costs ", " Coins to buy a Star with Wiggler.")
    chompCost_entry = create_entry(tabview.tab("Coins Mods"), 7, "assets/eventTags/chainChomp.png", " Costs ", " Coins to Steal a Star.")
    chompMin_entry = create_entry(tabview.tab("Coins Mods"), 8, "assets/eventTags/chainChomp.png", " Steal ", " Mininum when stealing Coins.")
    initial_entry = create_entry(tabview.tab("Coins Mods"), 9, "assets/eventTags/initialCoins.png", " Gain ", " Coins at the start of the game.")

    # Create button to generate coins modification codes
    parse_coins_button = ctk.CTkButton(master=tabview.tab("Coins Mods"), command=lambda: coinsEvent_mp5(blue_entry, red_entry, mgWin_entry, star_entry, wiggler_entry, chompCost_entry, chompMin_entry, koopaBank_entry, initial_entry), text="Generate Codes")
    parse_coins_button.place(x=10, y=800)

    # List of minigame names
    minigames_list = ["Coney Island", "Ground Pound Down", "Chimp Chase", "Chomp Romp", "Pushy Penguins", "Leaf Leap", "Night Light Fright", "Pop-Star Piranhas", "Mazed & Confused", "Dinger Derby", "Hydrostars", "Later Skater", "Will Flower", "Triple Jump", "Hotel Goomba", "Coin Cache", "Flatiator", "Squared Away", "Mario Mechs", "Revolving Fire", "Clock Stoppers", "Heat Stroke", "Beam Team", "Vicious Vending", "Big Top Drop", "Defuse or Lose", "ID UFO", "Mario Can-Can", "Handy Hoppers", "Berry Basket", "Bus Buffer", "Rumble Ready", "Submarathon", "Manic Mallets", "Astro-Logical", "Bill Blasters", "Tug-o-Dorrie", "Twist 'n' Out", "Lucky Lineup", "Random Ride", "Shock Absorbers", "Countdown Pound", "Whomp Maze", "Shy Guy Showdown", "Button Mashers", "Get a Rope", "Pump 'n' Jump", "Head Waiter", "Blown Away", "Merry Poppings", "Pound Peril", "Piece Out", "Bound of Music", "Wind Wavers", "Sky Survivor", "Cage-in Cookin'", "Rain of Fire", "Scaldin' Cauldron", "Frightmare", "Flower Shower", "Dodge Bomb", "Fish Upon a Star", "Rumble Fumble", "Quilt for Speed", "Tube It or Lose It", "Mathletes", "Fight Cards", "Banana Punch", "Da Vine Climb", "Mass A-peel", "Panic Pinball", "Banking Coins", "Frozen Frenzy", "Curvy Curbs", "Beach Volleyball", "Fish Sticks", "Ice Hockey"]   
    # Create labels, comboboxes, and button for Minigame Replacement tab
    replace_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" Replace  ", font=("Arial", 16))
    replace_label.grid(row=0, column=0)
    combobox_mingames_1 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_1.grid(row=0, column=1)
    with_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" with ", font=("Arial", 16))
    with_label.grid(row=0, column=2)
    combobox_mingames_2 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_2.grid(row=0, column=3)
    parse_minigame_button = ctk.CTkButton(master=tabview.tab("Minigame Replacement"), command=lambda: mgReplaceEvent_mp5(combobox_mingames_1, combobox_mingames_2, minigames_list), text="Generate Codes")
    parse_minigame_button.place(x=10, y=800)

    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/mushroomCapsule.png", 2, 1)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=2, column=2)
    mushroomCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    mushroomCapsulePrice5.grid(row=2, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=2, column=4)
    mushroomCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    mushroomCapsuleWeight5.grid(row=2, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.   ", font=("Arial", 16))
    label.grid(row=2, column=6)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/goldenMushroomCapsule.png", 3, 1)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=3, column=2)
    goldenMushroomCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    goldenMushroomCapsulePrice5.grid(row=3, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=3, column=4)
    goldenMushroomCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    goldenMushroomCapsuleWeight5.grid(row=3, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=3, column=6)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/cursedMushroomCapsule.png", 4, 1)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=4, column=2)
    cursedMushroomCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    cursedMushroomCapsulePrice5.grid(row=4, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=4, column=4)
    cursedMushroomCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    cursedMushroomCapsuleWeight5.grid(row=4, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=4, column=6)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/warpCapsule.png", 5, 1)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=5, column=2)
    warpPipeCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    warpPipeCapsulePrice5.grid(row=5, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=5, column=4)
    warpPipeCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    warpPipeCapsuleWeight5.grid(row=5, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=5, column=6)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/kleptoCapsule.png", 6, 1)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=6, column=2)
    kleptoCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    kleptoCapsulePrice5.grid(row=6, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=6, column=4)
    kleptoCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    kleptoCapsuleWeight5.grid(row=6, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=6, column=6)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/wigglerCapsule.png", 8, 1)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=8, column=2)
    flutterCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    flutterCapsulePrice5.grid(row=8, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=8, column=4)
    flutterCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    flutterCapsuleWeight5.grid(row=8, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=8, column=6)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/podobooCapsule5.png", 9, 1)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=9, column=2)
    podobooCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    podobooCapsulePrice5.grid(row=9, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=9, column=4)
    podobooCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    podobooCapsuleWeight5.grid(row=9, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=9, column=6)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/spinyCapsule.png", 10, 1)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=10, column=2)
    spinyCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    spinyCapsulePrice5.grid(row=10, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=10, column=4)
    spinyCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    spinyCapsuleWeight5.grid(row=10, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=10, column=6)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/coinBlockCapsule.png", 11, 1)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=11, column=2)
    coinBlockCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    coinBlockCapsulePrice5.grid(row=11, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=11, column=4)
    coinBlockCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    coinBlockCapsuleWeight5.grid(row=11, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=11, column=6)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/hammerBroCapsule.png", 12, 1)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=12, column=2)
    hammerBroCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    hammerBroCapsulePrice5.grid(row=12, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=12, column=4)
    hammerBroCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    hammerBroCapsuleWeight5.grid(row=12, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.  ", font=("Arial", 16))
    label.grid(row=12, column=6)

    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text="", font=("Arial", 16))
    label.grid(row=2, column=6)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/paraTroopaCapsule5.png", 2, 8)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=2, column=9)
    paraTroopaCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    paraTroopaCapsulePrice5.grid(row=2, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=2, column=11)
    paraTroopaCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    paraTroopaCapsuleWeight5.grid(row=2, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.  ", font=("Arial", 16))
    label.grid(row=2, column=13)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/bulletBillCapsule.png", 3, 8)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=3, column=9)
    bulletBillCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    bulletBillCapsulePrice5.grid(row=3, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=3, column=11)
    bulletBillCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    bulletBillCapsuleWeight5.grid(row=3, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=3, column=13)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/blizzardCapsule.png", 4, 8)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=4, column=9)
    blizzardCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    blizzardCapsulePrice5.grid(row=4, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=4, column=11)
    blizzardCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    blizzardCapsuleWeight5.grid(row=4, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=4, column=13)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/kamekCapsule.png", 5, 8)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=5, column=9)
    kamekCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    kamekCapsulePrice5.grid(row=5, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=5, column=11)
    kamekCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    kamekCapsuleWeight5.grid(row=5, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=5, column=13)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/koopaBankCapsule.png", 6, 8)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=6, column=9)
    koopaBankCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    koopaBankCapsulePrice5.grid(row=6, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=6, column=11)
    koopaBankCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    koopaBankCapsuleWeight5.grid(row=6, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=6, column=13)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/goombaCapsule.png", 8, 8)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=8, column=9)
    goombaCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    goombaCapsulePrice5.grid(row=8, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=8, column=11)
    goombaCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    goombaCapsuleWeight5.grid(row=8, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=8, column=13)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/bombCapsule.png", 9, 8)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=9, column=9)
    bombCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    bombCapsulePrice5.grid(row=9, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=9, column=11)
    bombCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    bombCapsuleWeight5.grid(row=9, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=9, column=13)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/tweesterCapsule.png", 10, 8)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=10, column=9)
    tweesterCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    tweesterCapsulePrice5.grid(row=10, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=10, column=11)
    tweesterCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    tweesterCapsuleWeight5.grid(row=10, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=10, column=13)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/lakituCapsule5.png", 11, 8)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=11, column=9)
    lakituCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    lakituCapsulePrice5.grid(row=11, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=11, column=11)
    lakituCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    lakituCapsuleWeight5.grid(row=11, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=11, column=13)
    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/ukikiCapsule.png", 12, 8)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=12, column=9)
    ukikiCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    ukikiCapsulePrice5.grid(row=12, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=12, column=11)
    ukikiCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    ukikiCapsuleWeight5.grid(row=12, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=12, column=13)

    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text="", font=("Arial", 16))
    label.grid(row=2, column=14)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/miracleCapsule.png", 2, 15)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=2, column=16)
    miracleCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    miracleCapsulePrice5.grid(row=2, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=2, column=18)
    miracleCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    miracleCapsuleWeight5.grid(row=2, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=2, column=20)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/snackCapsule.png", 3, 15)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=3, column=16)
    boneCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    boneCapsulePrice5.grid(row=3, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=3, column=18)
    boneCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    boneCapsuleWeight5.grid(row=3, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=3, column=20)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/plantCapsule.png", 4, 15)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=4, column=16)
    plantCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    plantCapsulePrice5.grid(row=4, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=4, column=18)
    plantCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    plantCapsuleWeight5.grid(row=4, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=4, column=20)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/chainChompCapsule.png", 5, 15)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=5, column=16)
    chainChompCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    chainChompCapsulePrice5.grid(row=5, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=5, column=18)
    chainChompCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    chainChompCapsuleWeight5.grid(row=5, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=5, column=20)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/chanceCapsule.png", 6, 15)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=6, column=16)
    chanceCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    chanceCapsulePrice5.grid(row=6, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=6, column=18)
    chanceCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    chanceCapsuleWeight5.grid(row=6, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=6, column=20)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/dkCapsule.png", 8, 15)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=8, column=16)
    dkCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    dkCapsulePrice5.grid(row=8, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=8, column=18)
    dkCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    dkCapsuleWeight5.grid(row=8, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=8, column=20)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/bowserCapsule.png", 9, 15)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=9, column=16)
    bowserCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    bowserCapsulePrice5.grid(row=9, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=9, column=18)
    bowserCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    bowserCapsuleWeight5.grid(row=9, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=9, column=20)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/duelCapsule.png", 10, 15)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=10, column=16)
    duelCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    duelCapsulePrice5.grid(row=10, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=10, column=18)
    duelCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    duelCapsuleWeight5.grid(row=10, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=10, column=20)

    
    icon = create_image_icon(tabview.tab("Capsule Mods"), "assets/items/toadyCapsule.png", 11, 15)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=11, column=16)
    magiKoopaCapsulePrice5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    magiKoopaCapsulePrice5.grid(row=11, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" and is ", font=("Arial", 16))
    label.grid(row=11, column=18)
    magiKoopaCapsuleWeight5 = ctk.CTkEntry(master=tabview.tab("Capsule Mods"), width=48, font=("Arial", 16, "bold"))
    magiKoopaCapsuleWeight5.grid(row=11, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text=" % common.", font=("Arial", 16))
    label.grid(row=11, column=20)

    warningLabel = ctk.CTkLabel(master=tabview.tab("Capsule Mods"), text="Shop Mod requires the Mushroom to cost 5 coins and atleast be enabled.", font=("Arial", 16, "bold"))
    warningLabel.place(x=10, y=500)

    parseButtonFiveItems = ctk.CTkButton(master=tabview.tab("Capsule Mods"), command=lambda: itemsEvent_mp5(bombCapsulePrice5, bombCapsuleWeight5, koopaBankCapsulePrice5, koopaBankCapsuleWeight5, bulletBillCapsulePrice5, bulletBillCapsuleWeight5, hammerBroCapsulePrice5, hammerBroCapsuleWeight5, coinBlockCapsulePrice5, coinBlockCapsuleWeight5, duelCapsulePrice5, duelCapsuleWeight5, mushroomCapsulePrice5, mushroomCapsuleWeight5, goldenMushroomCapsulePrice5, goldenMushroomCapsuleWeight5, cursedMushroomCapsulePrice5, cursedMushroomCapsuleWeight5, flutterCapsulePrice5, flutterCapsuleWeight5, spinyCapsulePrice5, spinyCapsuleWeight5, goombaCapsuleWeight5, goombaCapsulePrice5, plantCapsulePrice5, plantCapsuleWeight5, kleptoCapsuleWeight5, kleptoCapsulePrice5, kamekCapsuleWeight5, kamekCapsulePrice5, magiKoopaCapsuleWeight5, magiKoopaCapsulePrice5, blizzardCapsuleWeight5, blizzardCapsulePrice5, podobooCapsulePrice5, podobooCapsuleWeight5, paraTroopaCapsuleWeight5, paraTroopaCapsulePrice5, ukikiCapsulePrice5, ukikiCapsuleWeight5, tweesterCapsulePrice5, tweesterCapsuleWeight5, lakituCapsulePrice5, lakituCapsuleWeight5, warpPipeCapsulePrice5, warpPipeCapsuleWeight5, miracleCapsulePrice5, miracleCapsuleWeight5, boneCapsulePrice5, boneCapsuleWeight5, chanceCapsulePrice5, chanceCapsuleWeight5, chainChompCapsulePrice5, chainChompCapsuleWeight5, bowserCapsulePrice5, bowserCapsuleWeight5, dkCapsulePrice5, dkCapsuleWeight5), text="Generate Codes", )
    parseButtonFiveItems.place(x=10, y=800)

    parseButtonFive = ctk.CTkButton(master=tabview.tab("Capsule Mods"), command=lambda: savePresetItems5(bombCapsulePrice5, bombCapsuleWeight5, koopaBankCapsulePrice5, koopaBankCapsuleWeight5, bulletBillCapsulePrice5, bulletBillCapsuleWeight5, hammerBroCapsulePrice5, hammerBroCapsuleWeight5, coinBlockCapsulePrice5, coinBlockCapsuleWeight5, duelCapsulePrice5, duelCapsuleWeight5, mushroomCapsulePrice5, mushroomCapsuleWeight5, goldenMushroomCapsulePrice5, goldenMushroomCapsuleWeight5, cursedMushroomCapsulePrice5, cursedMushroomCapsuleWeight5, flutterCapsulePrice5, flutterCapsuleWeight5, spinyCapsulePrice5, spinyCapsuleWeight5, goombaCapsuleWeight5, goombaCapsulePrice5, plantCapsulePrice5, plantCapsuleWeight5, kleptoCapsuleWeight5, kleptoCapsulePrice5, kamekCapsuleWeight5, kamekCapsulePrice5, magiKoopaCapsuleWeight5, magiKoopaCapsulePrice5, blizzardCapsuleWeight5, blizzardCapsulePrice5, podobooCapsulePrice5, podobooCapsuleWeight5, paraTroopaCapsuleWeight5, paraTroopaCapsulePrice5, ukikiCapsulePrice5, ukikiCapsuleWeight5, tweesterCapsulePrice5, tweesterCapsuleWeight5, lakituCapsulePrice5, lakituCapsuleWeight5, warpPipeCapsulePrice5, warpPipeCapsuleWeight5, miracleCapsulePrice5, miracleCapsuleWeight5, boneCapsulePrice5, boneCapsuleWeight5, chanceCapsulePrice5, chanceCapsuleWeight5, chainChompCapsulePrice5, chainChompCapsuleWeight5, bowserCapsulePrice5, bowserCapsuleWeight5, dkCapsulePrice5, dkCapsuleWeight5), text="Save Preset", )
    parseButtonFive.place(x=160, y=800)

    parseButtonFive = ctk.CTkButton(master=tabview.tab("Capsule Mods"), command=lambda: loadPresetItems5(bombCapsulePrice5, bombCapsuleWeight5, koopaBankCapsulePrice5, koopaBankCapsuleWeight5, bulletBillCapsulePrice5, bulletBillCapsuleWeight5, hammerBroCapsulePrice5, hammerBroCapsuleWeight5, coinBlockCapsulePrice5, coinBlockCapsuleWeight5, duelCapsulePrice5, duelCapsuleWeight5, mushroomCapsulePrice5, mushroomCapsuleWeight5, goldenMushroomCapsulePrice5, goldenMushroomCapsuleWeight5, cursedMushroomCapsulePrice5, cursedMushroomCapsuleWeight5, flutterCapsulePrice5, flutterCapsuleWeight5, spinyCapsulePrice5, spinyCapsuleWeight5, goombaCapsuleWeight5, goombaCapsulePrice5, plantCapsulePrice5, plantCapsuleWeight5, kleptoCapsuleWeight5, kleptoCapsulePrice5, kamekCapsuleWeight5, kamekCapsulePrice5, magiKoopaCapsuleWeight5, magiKoopaCapsulePrice5, blizzardCapsuleWeight5, blizzardCapsulePrice5, podobooCapsulePrice5, podobooCapsuleWeight5, paraTroopaCapsuleWeight5, paraTroopaCapsulePrice5, ukikiCapsulePrice5, ukikiCapsuleWeight5, tweesterCapsulePrice5, tweesterCapsuleWeight5, lakituCapsulePrice5, lakituCapsuleWeight5, warpPipeCapsulePrice5, warpPipeCapsuleWeight5, miracleCapsulePrice5, miracleCapsuleWeight5, boneCapsulePrice5, boneCapsuleWeight5, chanceCapsulePrice5, chanceCapsuleWeight5, chainChompCapsulePrice5, chainChompCapsuleWeight5, bowserCapsulePrice5, bowserCapsuleWeight5, dkCapsulePrice5, dkCapsuleWeight5), text="Load Preset", )
    parseButtonFive.place(x=310, y=800)

    parseButtonFiveFillViaCode = ctk.CTkButton(master=tabview.tab("Capsule Mods"), command=lambda: fillViaCode5Actions(), text="Fill Via Code")
    parseButtonFiveFillViaCode.place(x=460, y=800)

    def fillViaCode5Actions():
        top = ctk.CTkToplevel(height=500, width=500)
        top.attributes('-topmost', True)
        top.title("Enter Code")
        
        enterCodeLabel = ctk.CTkLabel(master=top, text="Enter Code")
        enterCodeLabel.place(x=10, y=10)
        
        codeText = ctk.CTkTextbox(master=top, width=200, height=400)
        codeText.place(x=10, y=65)

        submitButton = ctk.CTkButton(master=top, command=lambda: fillViaCode5(top, codeText, bombCapsulePrice5, bombCapsuleWeight5, koopaBankCapsulePrice5, koopaBankCapsuleWeight5, bulletBillCapsulePrice5, bulletBillCapsuleWeight5, hammerBroCapsulePrice5, hammerBroCapsuleWeight5, coinBlockCapsulePrice5, coinBlockCapsuleWeight5, duelCapsulePrice5, duelCapsuleWeight5, mushroomCapsulePrice5, mushroomCapsuleWeight5, goldenMushroomCapsulePrice5, goldenMushroomCapsuleWeight5, cursedMushroomCapsulePrice5, cursedMushroomCapsuleWeight5, flutterCapsulePrice5, flutterCapsuleWeight5, spinyCapsulePrice5, spinyCapsuleWeight5, goombaCapsuleWeight5, goombaCapsulePrice5, plantCapsulePrice5, plantCapsuleWeight5, kleptoCapsuleWeight5, kleptoCapsulePrice5, kamekCapsuleWeight5, kamekCapsulePrice5, magiKoopaCapsuleWeight5, magiKoopaCapsulePrice5, blizzardCapsuleWeight5, blizzardCapsulePrice5, podobooCapsulePrice5, podobooCapsuleWeight5, paraTroopaCapsuleWeight5, paraTroopaCapsulePrice5, ukikiCapsulePrice5, ukikiCapsuleWeight5, tweesterCapsulePrice5, tweesterCapsuleWeight5, lakituCapsulePrice5, lakituCapsuleWeight5, warpPipeCapsulePrice5, warpPipeCapsuleWeight5, miracleCapsulePrice5, miracleCapsuleWeight5, boneCapsulePrice5, boneCapsuleWeight5, chanceCapsulePrice5, chanceCapsuleWeight5, chainChompCapsulePrice5, chainChompCapsuleWeight5, bowserCapsulePrice5, bowserCapsuleWeight5, dkCapsulePrice5, dkCapsuleWeight5), text="Submit")
        submitButton.place(x=250, y=425)

    stars6 = ["None", "Blue Star", "Red Star", "Capsule Space Star", "Happening Star", "Bowser Star", "Donkey Kong Star", "Current Coins Star", "Minigame Star", "Coin Star", "Star Star"]
    
    label = ctk.CTkLabel(master=tabview.tab("Bonus Star Replacement"), text=" Replace Minigame Star with:  ", font=("Arial", 16))
    label.grid(row=0, column=0, sticky="w")

    star1 = ctk.CTkComboBox(master=tabview.tab("Bonus Star Replacement"), values=stars6)
    star1.grid(row=0, column=1, pady=10)

    label = ctk.CTkLabel(master=tabview.tab("Bonus Star Replacement"), text=" Replace Coin Star with:  ", font=("Arial", 16))
    label.grid(row=1, column=0, sticky="w")

    star2 = ctk.CTkComboBox(master=tabview.tab("Bonus Star Replacement"), values=stars6)
    star2.grid(row=1, column=1, pady=10)

    label = ctk.CTkLabel(master=tabview.tab("Bonus Star Replacement"), text=" Replace Happening Star with:  ", font=("Arial", 16))
    label.grid(row=2, column=0, sticky="w")

    star3 = ctk.CTkComboBox(master=tabview.tab("Bonus Star Replacement"), values=stars6)
    star3.grid(row=2, column=1, pady=10)
    
    parseButton = ctk.CTkButton(master=tabview.tab("Bonus Star Replacement"), command=lambda: customBonusStarEvent_mp5(star1, star2, star3, stars6), text="Generate Codes")
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

    parse_stars_button = ctk.CTkButton(master=tabview.tab("Star Handicaps"), command=lambda: handicapEvent_mp5(p1Stars, p2Stars, p3Stars, p4Stars), text="Generate Codes")
    parse_stars_button.place(x=10, y=800)

    item_list = ["Nothing", "Golden Mushroom", "Poison Mushroom", "Warp Pipe", "Klepto", "Bubble", "Wiggler", "Hammer Bro", "Coin Block", "Spiny", "Paratroopa", "Goomba", "Bob-omb", "Koopa Bank", "Kamek", "Mr. Blizzard", "Piranha Plant", "Magikoopa", "Ukiki", "Lakitu","Tweester", "Duel", "Chain Chomp", "Bone", "Bowser", "Chance", "Miracle", "Donkey Kong"]   
    item_label = ctk.CTkLabel(master=tabview.tab("Board Specific"), text="Undersea Dream - Seashell Always Gives  ", font=("Arial", 16))
    item_label.grid(row=0, column=0, pady=10)
    comboItem = ctk.CTkComboBox(master=tabview.tab("Board Specific"), values=item_list)
    comboItem.grid(row=0, column=1)
    spinx_button = ctk.CTkButton(master=tabview.tab("Board Specific"), command=lambda: underseaEvent_mp5(comboSpinx, spinx_list), text="Generate Code")
    spinx_button.place(x=450, y=10)

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

    parse_stars_button = ctk.CTkButton(master=tabview.tab("Battle Minigame"), command=lambda: battleCoins_mp5(fiveCoins, tenCoins, twentyCoins, thirtyCoins, fiftyCoins), text="Generate Codes")
    parse_stars_button.place(x=10, y=800)

    return frame