# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (tabitha@tabs.gay)
# Date: 5/12/2024
# License: MIT
# ============================================

# Import necessary functions and modules
from functions import *
from events.marioParty7_coins import *
from events.marioParty7_initialItems import *
from events.marioParty7_mgreplace import *
from events.marioParty7_boardSpecific import *
from events.marioParty7_handicap import *
from events.marioParty7_items import *
from events.marioParty7_spaceReplace import *
from events.marioParty7_bonusStarReplace import *
from events.marioParty7_battle import *

# Import custom tkinter module as ctk
import customtkinter as ctk
from CTkToolTip import *

# Function to create the main interface for Mario Party 1
def create_mario_party_7_interface(frame):
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
    character_entry = create_entry(tabview.tab("Coins Mods"), 3, "assets/eventTags/characterSpace7.png", " Gain  ", " Coins on your own Character Space.")
    mgWin_entry = create_entry(tabview.tab("Coins Mods"), 4, "assets/eventTags/miniGame.png", " Gain  ", " Coins when winning a Minigame.")

    star_entry = create_entry(tabview.tab("Coins Mods"), 5, "assets/eventTags/starSpace.png", " Costs ", " Coins to buy a Star at a Star Space and when using Flutter.  ")
    windmill_entryTooltip = CTkToolTip(star_entry, message="Works on Canal, Pagoda, Neon Heights, and Bowser.")

    star_last4_entry = create_entry(tabview.tab("Coins Mods"), 6, "assets/eventTags/starSpace.png", " Costs ", " Coins to buy a Star during Last 4 Turns.")
    hammerBro_entry = create_entry2(tabview.tab("Coins Mods"), 1, "assets/items/hammerBroCapsule.png", " Steal ", " Coins from Hammer Bro.")
    zap_entry = create_entry2(tabview.tab("Coins Mods"), 2, "assets/items/zapCapsule.png", " Lose ", " Coins from Zaps.")
    fireball_entry = create_entry2(tabview.tab("Coins Mods"), 3, "assets/items/fireballCapsule.png", " Steal ", " Coins from Fireballs.")
    vacuum_entry = create_entry2(tabview.tab("Coins Mods"), 4, "assets/items/vacuumCapsule.png", " Steal ", " Coins despite Vacuum Roulette.")
    flower_entry = create_entry2(tabview.tab("Coins Mods"), 5, "assets/items/flowerCapsule.png", " Gain ", " Per Space with Flower.")
    initial_entry = create_entry2(tabview.tab("Coins Mods"), 6, "assets/eventTags/initialCoins.png", " Gain ", " Coins at the start of the game.")

    # Create button to generate coins modification codes  
    parse_coins_button = ctk.CTkButton(master=tabview.tab("Coins Mods"), command=lambda: coinsEvent_mp7(blue_entry, red_entry, character_entry, mgWin_entry, star_entry, star_last4_entry, hammerBro_entry, zap_entry, fireball_entry, vacuum_entry, flower_entry, initial_entry), text="Generate Codes")
    parse_coins_button.place(x=10, y=800)

    # List of minigame names
    minigames_list = ["Catchy Tunes", "Bubble Brawl", "Track & Yield", "Fun Run", "Cointagious", "Snow Ride", "Picture This", "Ghost in the Hall", "Big Dripper", "Target Tag", "Pokey Pummel", "Take Me Ohm", "Kart Wheeled", "Balloon Busters", "Clock Watchers", "Dart Attack", "Oil Crisis", "La Bomba", "Spray Anything", "Balloonatic", "Spinner Cell", "Think Tank", "Flashfright", "Coin-op Bop", "Easy Pickings", "Wheel of Woe", "Boxing Day", "Be My Chum!", "StratosFEAR!", "Pogo-a-go-go", "Buzzstormer", "Tile and Error", "Battery Ram", "Cardinal Rule", "Ice Moves", "Bumper Crop", "Hop-O-Matic 4000", "Wingin' It", "Sphere Factor", "Herbicidal Maniac", "Pyramid Scheme", "World Piece", "Warp Pipe Dreams", "Weight for It", "Helipopper", "Monty's Revenge", "Deck Hands", "Mad Props", "Gimme a Sign", "Bridge Work", "Spin Doctor", "Hip Hop Drop", "Air Farce", "The Final Countdown", "Royal Rumpus", "Light Speed", "Apes of Wrath", "Fish & Cheeps", "Camp Ukiki", "Funstacle Course!", "Funderwall!", "Magmagical Journey!", "Tunnel of Lava!", "Treasure Dome!", "Slot-O-Whirl!", "Peel Out", "Bananas Faster", "Stump Change", "Jump, Man", "Vine Country", "A Bridge Too Short", "Spider Stomp", "Stick and Spin", "Bowser's Lovely Lift!"]    # Create labels, comboboxes, and button for Minigame Replacement tab
    replace_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" Replace  ", font=("Arial", 16))
    replace_label.grid(row=0, column=0)
    combobox_mingames_1 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_1.grid(row=0, column=1)
    with_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" with ", font=("Arial", 16))
    with_label.grid(row=0, column=2)
    combobox_mingames_2 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_2.grid(row=0, column=3)
    parse_minigame_button = ctk.CTkButton(master=tabview.tab("Minigame Replacement"), command=lambda: mgReplaceEvent_mp7(combobox_mingames_1, combobox_mingames_2, minigames_list), text="Generate Codes")
    parse_minigame_button.place(x=10, y=800)


    # ORB GEN
    scrollable_frame = ctk.CTkFrame(master=tabview.tab("Orb Mods"), fg_color=("#fcfcfc", "#2e2e2e"))
    scrollable_frame.grid(row=0, column=0, sticky="nsew", pady=(0, 50))
    # Configure grid to allow stretching
    tabview.tab("Orb Mods").grid_rowconfigure(0, weight=1)
    tabview.tab("Orb Mods").grid_columnconfigure(0, weight=1)
    scrollable_frame.grid_rowconfigure(0, weight=1)

    # Create a canvas for scrolling
    canvas = ctk.CTkCanvas(master=scrollable_frame, bg="#2e2e2e", highlightthickness=0)
    canvas.grid(row=0, column=0, sticky="nsew")

    # Create a vertical scrollbar linked to the canvas
    scrollbar = ctk.CTkScrollbar(master=scrollable_frame, orientation="vertical", command=canvas.yview, fg_color=("#ffffff", "#3a3a3a"))
    scrollbar.grid(row=0, column=1, sticky="ns")

    # Configure the canvas to work with the scrollbar
    canvas.configure(yscrollcommand=scrollbar.set)

    # Create a frame inside the canvas to hold the content
    content_frame = ctk.CTkFrame(master=canvas, fg_color=("#fcfcfc", "#2e2e2e"))
    canvas.create_window((0, 0), window=content_frame, anchor="nw")

    # Function to update the scroll region
    def update_scroll_region(event):
        canvas.configure(scrollregion=canvas.bbox("all"))

    content_frame.bind("<Configure>", update_scroll_region)
    
    # Configure the canvas to fill the width of the scrollable frame
    scrollable_frame.grid_columnconfigure(0, weight=1)  # Ensure the canvas fills the width
    canvas.grid_rowconfigure(0, weight=1)  # Ensure the canvas fills the height

    # Mushroom
    icon = create_image_icon(content_frame, "assets/items/mushroomCapsule.png", 2, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=2, column=2)
    label = ctk.CTkLabel(master=content_frame, text=" 5 ", font=("Arial", 24, "bold"))
    label.grid(row=2, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=2, column=4)
    label = ctk.CTkLabel(master=content_frame, text=" 5 ", font=("Arial", 24, "bold"))
    label.grid(row=2, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=2, column=6)
    label = ctk.CTkLabel(master=content_frame, text=" 5 ", font=("Arial", 24, "bold"))
    label.grid(row=2, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=2, column=8)
    mushroomCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mushroomCapsuleShopOdds12.grid(row=2, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=2, column=10)
    mushroomCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mushroomCapsuleShopOdds34.grid(row=2, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=2, column=12)
    mushroomCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mushroomCapsuleSpaceOdds1.grid(row=2, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=2, column=14)
    mushroomCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mushroomCapsuleSpaceOdds2.grid(row=2, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=2, column=16)
    mushroomCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mushroomCapsuleSpaceOdds34.grid(row=2, column=17)

    # Golden Mushroom
    icon = create_image_icon(content_frame, "assets/items/goldenMushroomCapsule.png", 3, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=3, column=2)
    goldenMushroomCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    goldenMushroomCapsulePrice1.grid(row=3, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=3, column=4)
    goldenMushroomCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    goldenMushroomCapsulePrice2.grid(row=3, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=3, column=6)
    goldenMushroomCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    goldenMushroomCapsulePrice34.grid(row=3, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=3, column=8)
    goldenMushroomCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    goldenMushroomCapsuleShopOdds12.grid(row=3, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=3, column=10)
    goldenMushroomCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    goldenMushroomCapsuleShopOdds34.grid(row=3, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=3, column=12)
    goldenMushroomCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    goldenMushroomCapsuleSpaceOdds1.grid(row=3, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=3, column=14)
    goldenMushroomCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    goldenMushroomCapsuleSpaceOdds2.grid(row=3, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=3, column=16)
    goldenMushroomCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    goldenMushroomCapsuleSpaceOdds34.grid(row=3, column=17)

    # Slow Mushroom
    icon = create_image_icon(content_frame, "assets/items/slowMushroomCapsule.png", 4, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=4, column=2)
    slowMushroomCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    slowMushroomCapsulePrice1.grid(row=4, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=4, column=4)
    slowMushroomCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    slowMushroomCapsulePrice2.grid(row=4, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=4, column=6)
    slowMushroomCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    slowMushroomCapsulePrice34.grid(row=4, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=4, column=8)
    slowMushroomCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    slowMushroomCapsuleShopOdds12.grid(row=4, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=4, column=10)
    slowMushroomCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    slowMushroomCapsuleShopOdds34.grid(row=4, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=4, column=12)
    slowMushroomCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    slowMushroomCapsuleSpaceOdds1.grid(row=4, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=4, column=14)
    slowMushroomCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    slowMushroomCapsuleSpaceOdds2.grid(row=4, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=4, column=16)
    slowMushroomCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    slowMushroomCapsuleSpaceOdds34.grid(row=4, column=17)

    # Metal Mushroom
    icon = create_image_icon(content_frame, "assets/items/metalMushroomCapsule.png", 5, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=5, column=2)
    metalMushroomCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    metalMushroomCapsulePrice1.grid(row=5, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=5, column=4)
    metalMushroomCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    metalMushroomCapsulePrice2.grid(row=5, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=5, column=6)
    metalMushroomCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    metalMushroomCapsulePrice34.grid(row=5, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=5, column=8)
    metalMushroomCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    metalMushroomCapsuleShopOdds12.grid(row=5, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=5, column=10)
    metalMushroomCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    metalMushroomCapsuleShopOdds34.grid(row=5, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=5, column=12)
    metalMushroomCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    metalMushroomCapsuleSpaceOdds1.grid(row=5, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=5, column=14)
    metalMushroomCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    metalMushroomCapsuleSpaceOdds2.grid(row=5, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=5, column=16)
    metalMushroomCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    metalMushroomCapsuleSpaceOdds34.grid(row=5, column=17)

    # Flutter
    icon = create_image_icon(content_frame, "assets/items/wigglerCapsule.png", 6, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=6, column=2)
    flutterCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    flutterCapsulePrice1.grid(row=6, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=6, column=4)
    flutterCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    flutterCapsulePrice2.grid(row=6, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=6, column=6)
    flutterCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    flutterCapsulePrice34.grid(row=6, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=6, column=8)
    flutterCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    flutterCapsuleShopOdds12.grid(row=6, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=6, column=10)
    flutterCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    flutterCapsuleShopOdds34.grid(row=6, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=6, column=12)
    flutterCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    flutterCapsuleSpaceOdds1.grid(row=6, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=6, column=14)
    flutterCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    flutterCapsuleSpaceOdds2.grid(row=6, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=6, column=16)
    flutterCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    flutterCapsuleSpaceOdds34.grid(row=6, column=17)

    # Cannon
    icon = create_image_icon(content_frame, "assets/items/cannonCapsule.png", 7, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=7, column=2)
    cannonCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    cannonCapsulePrice1.grid(row=7, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=7, column=4)
    cannonCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    cannonCapsulePrice2.grid(row=7, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=7, column=6)
    cannonCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    cannonCapsulePrice34.grid(row=7, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=7, column=8)
    cannonCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    cannonCapsuleShopOdds12.grid(row=7, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=7, column=10)
    cannonCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    cannonCapsuleShopOdds34.grid(row=7, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=7, column=12)
    cannonCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    cannonCapsuleSpaceOdds1.grid(row=7, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=7, column=14)
    cannonCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    cannonCapsuleSpaceOdds2.grid(row=7, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=7, column=16)
    cannonCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    cannonCapsuleSpaceOdds34.grid(row=7, column=17)

    # Lakitu
    icon = create_image_icon(content_frame, "assets/items/lakituCapsule.png", 8, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=8, column=2)
    lakituCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    lakituCapsulePrice1.grid(row=8, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=8, column=4)
    lakituCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    lakituCapsulePrice2.grid(row=8, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=8, column=6)
    lakituCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    lakituCapsulePrice34.grid(row=8, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=8, column=8)
    lakituCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    lakituCapsuleShopOdds12.grid(row=8, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=8, column=10)
    lakituCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    lakituCapsuleShopOdds34.grid(row=8, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=8, column=12)
    lakituCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    lakituCapsuleSpaceOdds1.grid(row=8, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=8, column=14)
    lakituCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    lakituCapsuleSpaceOdds2.grid(row=8, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=8, column=16)
    lakituCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    lakituCapsuleSpaceOdds34.grid(row=8, column=17)

    # Snack
    icon = create_image_icon(content_frame, "assets/items/snackCapsule7.png", 9, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=9, column=2)
    snackCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    snackCapsulePrice1.grid(row=9, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=9, column=4)
    snackCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    snackCapsulePrice2.grid(row=9, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=9, column=6)
    snackCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    snackCapsulePrice34.grid(row=9, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=9, column=8)
    snackCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    snackCapsuleShopOdds12.grid(row=9, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=9, column=10)
    snackCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    snackCapsuleShopOdds34.grid(row=9, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st / 2nd ", font=("Arial", 14))
    label.grid(row=9, column=12)
    snackCapsuleSpaceOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    snackCapsuleSpaceOdds12.grid(row=9, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=9, column=12)
    snackCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    snackCapsuleSpaceOdds1.grid(row=9, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=9, column=14)
    snackCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    snackCapsuleSpaceOdds2.grid(row=9, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=9, column=16)
    snackCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    snackCapsuleSpaceOdds34.grid(row=9, column=17)

    # Piranha Plant
    icon = create_image_icon(content_frame, "assets/items/plantCapsule.png", 10, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=10, column=2)
    piranhaPlantCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    piranhaPlantCapsulePrice1.grid(row=10, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=10, column=4)
    piranhaPlantCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    piranhaPlantCapsulePrice2.grid(row=10, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=10, column=6)
    piranhaPlantCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    piranhaPlantCapsulePrice34.grid(row=10, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=10, column=8)
    piranhaPlantCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    piranhaPlantCapsuleShopOdds12.grid(row=10, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=10, column=10)
    piranhaPlantCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    piranhaPlantCapsuleShopOdds34.grid(row=10, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=10, column=12)
    piranhaPlantCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    piranhaPlantCapsuleSpaceOdds1.grid(row=10, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=10, column=14)
    piranhaPlantCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    piranhaPlantCapsuleSpaceOdds2.grid(row=10, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=10, column=16)
    piranhaPlantCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    piranhaPlantCapsuleSpaceOdds34.grid(row=10, column=17)

    # Spear Guy
    icon = create_image_icon(content_frame, "assets/items/spearCapsule.png", 11, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=11, column=2)
    spearGuyCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    spearGuyCapsulePrice1.grid(row=11, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=11, column=4)
    spearGuyCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    spearGuyCapsulePrice2.grid(row=11, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=11, column=6)
    spearGuyCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    spearGuyCapsulePrice34.grid(row=11, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=11, column=8)
    spearGuyCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    spearGuyCapsuleShopOdds12.grid(row=11, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=11, column=10)
    spearGuyCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    spearGuyCapsuleShopOdds34.grid(row=11, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=11, column=12)
    spearGuyCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    spearGuyCapsuleSpaceOdds1.grid(row=11, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=11, column=14)
    spearGuyCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    spearGuyCapsuleSpaceOdds2.grid(row=11, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=11, column=16)
    spearGuyCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    spearGuyCapsuleSpaceOdds34.grid(row=11, column=17)

    # Hammer Bro
    icon = create_image_icon(content_frame, "assets/items/hammerBroCapsule.png", 12, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=12, column=2)
    hammerBroCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    hammerBroCapsulePrice1.grid(row=12, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=12, column=4)
    hammerBroCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    hammerBroCapsulePrice2.grid(row=12, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=12, column=6)
    hammerBroCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    hammerBroCapsulePrice34.grid(row=12, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=12, column=8)
    hammerBroCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    hammerBroCapsuleShopOdds12.grid(row=12, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=12, column=10)
    hammerBroCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    hammerBroCapsuleShopOdds34.grid(row=12, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=12, column=12)
    hammerBroCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    hammerBroCapsuleSpaceOdds1.grid(row=12, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=12, column=14)
    hammerBroCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    hammerBroCapsuleSpaceOdds2.grid(row=12, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=12, column=16)
    hammerBroCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    hammerBroCapsuleSpaceOdds34.grid(row=12, column=17)


    # Kamek
    icon = create_image_icon(content_frame, "assets/items/kamekCapsule.png", 13, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=13, column=2)
    kamekCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    kamekCapsulePrice1.grid(row=13, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=13, column=4)
    kamekCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    kamekCapsulePrice2.grid(row=13, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=13, column=6)
    kamekCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    kamekCapsulePrice34.grid(row=13, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=13, column=8)
    kamekCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    kamekCapsuleShopOdds12.grid(row=13, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=13, column=10)
    kamekCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    kamekCapsuleShopOdds34.grid(row=13, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=13, column=12)
    kamekCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    kamekCapsuleSpaceOdds1.grid(row=13, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=13, column=14)
    kamekCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    kamekCapsuleSpaceOdds2.grid(row=13, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=13, column=16)
    kamekCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    kamekCapsuleSpaceOdds34.grid(row=13, column=17)
    

    # Toady
    icon = create_image_icon(content_frame, "assets/items/toadyCapsule.png", 14, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=14, column=2)
    toadyCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    toadyCapsulePrice1.grid(row=14, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=14, column=4)
    toadyCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    toadyCapsulePrice2.grid(row=14, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=14, column=6)
    toadyCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    toadyCapsulePrice34.grid(row=14, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=14, column=8)
    toadyCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    toadyCapsuleShopOdds12.grid(row=14, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=14, column=10)
    toadyCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    toadyCapsuleShopOdds34.grid(row=14, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=14, column=12)
    toadyCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    toadyCapsuleSpaceOdds1.grid(row=14, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=14, column=14)
    toadyCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    toadyCapsuleSpaceOdds2.grid(row=14, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=14, column=16)
    toadyCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    toadyCapsuleSpaceOdds34.grid(row=14, column=17)

    # Mr. Blizzard
    icon = create_image_icon(content_frame, "assets/items/blizzardCapsule.png", 15, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=15, column=2)
    mrBlizzardCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mrBlizzardCapsulePrice1.grid(row=15, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=15, column=4)
    mrBlizzardCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mrBlizzardCapsulePrice2.grid(row=15, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=15, column=6)
    mrBlizzardCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mrBlizzardCapsulePrice34.grid(row=15, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=15, column=8)
    mrBlizzardCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mrBlizzardCapsuleShopOdds12.grid(row=15, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=15, column=10)
    mrBlizzardCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mrBlizzardCapsuleShopOdds34.grid(row=15, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=15, column=12)
    mrBlizzardCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mrBlizzardCapsuleSpaceOdds1.grid(row=15, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=15, column=14)
    mrBlizzardCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mrBlizzardCapsuleSpaceOdds2.grid(row=15, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=15, column=16)
    mrBlizzardCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mrBlizzardCapsuleSpaceOdds34.grid(row=15, column=17)

    # Bandit
    icon = create_image_icon(content_frame, "assets/items/banditCapsule.png", 16, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=16, column=2)
    banditCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    banditCapsulePrice1.grid(row=16, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=16, column=4)
    banditCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    banditCapsulePrice2.grid(row=16, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=16, column=6)
    banditCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    banditCapsulePrice34.grid(row=16, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=16, column=8)
    banditCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    banditCapsuleShopOdds12.grid(row=16, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=16, column=10)
    banditCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    banditCapsuleShopOdds34.grid(row=16, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=16, column=12)
    banditCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    banditCapsuleSpaceOdds1.grid(row=16, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=16, column=14)
    banditCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    banditCapsuleSpaceOdds2.grid(row=16, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=16, column=16)
    banditCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    banditCapsuleSpaceOdds34.grid(row=16, column=17)

    # Pink Boo
    icon = create_image_icon(content_frame, "assets/items/pinkBooCapsule.png", 17, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=17, column=2)
    pinkBooCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    pinkBooCapsulePrice1.grid(row=17, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=17, column=4)
    pinkBooCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    pinkBooCapsulePrice2.grid(row=17, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=17, column=6)
    pinkBooCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    pinkBooCapsulePrice34.grid(row=17, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=17, column=8)
    pinkBooCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    pinkBooCapsuleShopOdds12.grid(row=17, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=17, column=10)
    pinkBooCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    pinkBooCapsuleShopOdds34.grid(row=17, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=17, column=12)
    pinkBooCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    pinkBooCapsuleSpaceOdds1.grid(row=17, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=17, column=14)
    pinkBooCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    pinkBooCapsuleSpaceOdds2.grid(row=17, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=17, column=16)
    pinkBooCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    pinkBooCapsuleSpaceOdds34.grid(row=17, column=17)

    # Spiny
    icon = create_image_icon(content_frame, "assets/items/spinyCapsule.png", 18, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=18, column=2)
    spinyCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    spinyCapsulePrice1.grid(row=18, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=18, column=4)
    spinyCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    spinyCapsulePrice2.grid(row=18, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=18, column=6)
    spinyCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    spinyCapsulePrice34.grid(row=18, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=18, column=8)
    spinyCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    spinyCapsuleShopOdds12.grid(row=18, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=18, column=10)
    spinyCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    spinyCapsuleShopOdds34.grid(row=18, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=18, column=12)
    spinyCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    spinyCapsuleSpaceOdds1.grid(row=18, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=18, column=14)
    spinyCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    spinyCapsuleSpaceOdds2.grid(row=18, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=18, column=16)
    spinyCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    spinyCapsuleSpaceOdds34.grid(row=18, column=17)

    # Zap
    icon = create_image_icon(content_frame, "assets/items/zapCapsule.png", 19, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=19, column=2)
    zapCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    zapCapsulePrice1.grid(row=19, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=19, column=4)
    zapCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    zapCapsulePrice2.grid(row=19, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=19, column=6)
    zapCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    zapCapsulePrice34.grid(row=19, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=19, column=8)
    zapCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    zapCapsuleShopOdds12.grid(row=19, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=19, column=10)
    zapCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    zapCapsuleShopOdds34.grid(row=19, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=19, column=12)
    zapCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    zapCapsuleSpaceOdds1.grid(row=19, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=19, column=14)
    zapCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    zapCapsuleSpaceOdds2.grid(row=19, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=19, column=16)
    zapCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    zapCapsuleSpaceOdds34.grid(row=19, column=17)
    
    # Tweester
    icon = create_image_icon(content_frame, "assets/items/tweesterCapsule.png", 20, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=20, column=2)
    tweesterCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    tweesterCapsulePrice1.grid(row=20, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=20, column=4)
    tweesterCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    tweesterCapsulePrice2.grid(row=20, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=20, column=6)
    tweesterCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    tweesterCapsulePrice34.grid(row=20, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=20, column=8)
    tweesterCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    tweesterCapsuleShopOdds12.grid(row=20, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=20, column=10)
    tweesterCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    tweesterCapsuleShopOdds34.grid(row=20, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=20, column=12)
    tweesterCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    tweesterCapsuleSpaceOdds1.grid(row=20, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=20, column=14)
    tweesterCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    tweesterCapsuleSpaceOdds2.grid(row=20, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=20, column=16)
    tweesterCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    tweesterCapsuleSpaceOdds34.grid(row=20, column=17)

    # Thwomp
    icon = create_image_icon(content_frame, "assets/items/thwompCapsule.png", 21, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=21, column=2)
    thwompCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    thwompCapsulePrice1.grid(row=21, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=21, column=4)
    thwompCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    thwompCapsulePrice2.grid(row=21, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=21, column=6)
    thwompCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    thwompCapsulePrice34.grid(row=21, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=21, column=8)
    thwompCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    thwompCapsuleShopOdds12.grid(row=21, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=21, column=10)
    thwompCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    thwompCapsuleShopOdds34.grid(row=21, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=21, column=12)
    thwompCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    thwompCapsuleSpaceOdds1.grid(row=21, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=21, column=14)
    thwompCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    thwompCapsuleSpaceOdds2.grid(row=21, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=21, column=16)
    thwompCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    thwompCapsuleSpaceOdds34.grid(row=21, column=17)

    # Warp
    icon = create_image_icon(content_frame, "assets/items/warpCapsule.png", 22, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=22, column=2)
    warpCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    warpCapsulePrice1.grid(row=22, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=22, column=4)
    warpCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    warpCapsulePrice2.grid(row=22, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=22, column=6)
    warpCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    warpCapsulePrice34.grid(row=22, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=22, column=8)
    warpCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    warpCapsuleShopOdds12.grid(row=22, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=22, column=10)
    warpCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    warpCapsuleShopOdds34.grid(row=22, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=22, column=12)
    warpCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    warpCapsuleSpaceOdds1.grid(row=22, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=22, column=14)
    warpCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    warpCapsuleSpaceOdds2.grid(row=22, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=22, column=16)
    warpCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    warpCapsuleSpaceOdds34.grid(row=22, column=17)

    # Bomb
    icon = create_image_icon(content_frame, "assets/items/bombCapsule.png", 23, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=23, column=2)
    bombCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    bombCapsulePrice1.grid(row=23, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=23, column=4)
    bombCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    bombCapsulePrice2.grid(row=23, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=23, column=6)
    bombCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    bombCapsulePrice34.grid(row=23, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=23, column=8)
    bombCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    bombCapsuleShopOdds12.grid(row=23, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=23, column=10)
    bombCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    bombCapsuleShopOdds34.grid(row=23, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=23, column=12)
    bombCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    bombCapsuleSpaceOdds1.grid(row=23, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=23, column=14)
    bombCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    bombCapsuleSpaceOdds2.grid(row=23, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=23, column=16)
    bombCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    bombCapsuleSpaceOdds34.grid(row=23, column=17)

    # Fireball
    icon = create_image_icon(content_frame, "assets/items/fireballCapsule.png", 24, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=24, column=2)
    fireballCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    fireballCapsulePrice1.grid(row=24, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=24, column=4)
    fireballCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    fireballCapsulePrice2.grid(row=24, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=24, column=6)
    fireballCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    fireballCapsulePrice34.grid(row=24, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=24, column=8)
    fireballCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    fireballCapsuleShopOdds12.grid(row=24, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=24, column=10)
    fireballCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    fireballCapsuleShopOdds34.grid(row=24, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=24, column=12)
    fireballCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    fireballCapsuleSpaceOdds1.grid(row=24, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=24, column=14)
    fireballCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    fireballCapsuleSpaceOdds2.grid(row=24, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=24, column=16)
    fireballCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    fireballCapsuleSpaceOdds34.grid(row=24, column=17)

    # Flower
    icon = create_image_icon(content_frame, "assets/items/flowerCapsule.png", 25, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=25, column=2)
    flowerCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    flowerCapsulePrice1.grid(row=25, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=25, column=4)
    flowerCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    flowerCapsulePrice2.grid(row=25, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=25, column=6)
    flowerCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    flowerCapsulePrice34.grid(row=25, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=25, column=8)
    flowerCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    flowerCapsuleShopOdds12.grid(row=25, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=25, column=10)
    flowerCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    flowerCapsuleShopOdds34.grid(row=25, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=25, column=12)
    flowerCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    flowerCapsuleSpaceOdds1.grid(row=25, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=25, column=14)
    flowerCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    flowerCapsuleSpaceOdds2.grid(row=25, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=25, column=16)
    flowerCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    flowerCapsuleSpaceOdds34.grid(row=25, column=17)

    # Egg
    icon = create_image_icon(content_frame, "assets/items/eggCapsule.png", 26, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=26, column=2)
    eggCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    eggCapsulePrice1.grid(row=26, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=26, column=4)
    eggCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    eggCapsulePrice2.grid(row=26, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=26, column=6)
    eggCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    eggCapsulePrice34.grid(row=26, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=26, column=8)
    eggCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    eggCapsuleShopOdds12.grid(row=26, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=26, column=10)
    eggCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    eggCapsuleShopOdds34.grid(row=26, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=26, column=12)
    eggCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    eggCapsuleSpaceOdds1.grid(row=26, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=26, column=14)
    eggCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    eggCapsuleSpaceOdds2.grid(row=26, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=26, column=16)
    eggCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    eggCapsuleSpaceOdds34.grid(row=26, column=17)

    # Vacuum
    icon = create_image_icon(content_frame, "assets/items/vacuumCapsule.png", 27, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=27, column=2)
    vacuumCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    vacuumCapsulePrice1.grid(row=27, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=27, column=4)
    vacuumCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    vacuumCapsulePrice2.grid(row=27, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=27, column=6)
    vacuumCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    vacuumCapsulePrice34.grid(row=27, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=27, column=8)
    vacuumCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    vacuumCapsuleShopOdds12.grid(row=27, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=27, column=10)
    vacuumCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    vacuumCapsuleShopOdds34.grid(row=27, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=27, column=12)
    vacuumCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    vacuumCapsuleSpaceOdds1.grid(row=27, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=27, column=14)
    vacuumCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    vacuumCapsuleSpaceOdds2.grid(row=27, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=27, column=16)
    vacuumCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    vacuumCapsuleSpaceOdds34.grid(row=27, column=17)

    # Magic
    icon = create_image_icon(content_frame, "assets/items/magicCapsule.png", 28, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=28, column=2)
    magicCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    magicCapsulePrice1.grid(row=28, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=28, column=4)
    magicCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    magicCapsulePrice2.grid(row=28, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=28, column=6)
    magicCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    magicCapsulePrice34.grid(row=28, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=28, column=8)
    magicCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    magicCapsuleShopOdds12.grid(row=28, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=28, column=10)
    magicCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    magicCapsuleShopOdds34.grid(row=28, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=28, column=12)
    magicCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    magicCapsuleSpaceOdds1.grid(row=28, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=28, column=14)
    magicCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    magicCapsuleSpaceOdds2.grid(row=28, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=28, column=16)
    magicCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    magicCapsuleSpaceOdds34.grid(row=28, column=17)

    # Triple
    icon = create_image_icon(content_frame, "assets/items/tripleCapsule.png", 29, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=29, column=2)
    tripleCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    tripleCapsulePrice1.grid(row=29, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=29, column=4)
    tripleCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    tripleCapsulePrice2.grid(row=29, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=29, column=6)
    tripleCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    tripleCapsulePrice34.grid(row=29, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=29, column=8)
    tripleCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    tripleCapsuleShopOdds12.grid(row=29, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=29, column=10)
    tripleCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    tripleCapsuleShopOdds34.grid(row=29, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=29, column=12)
    tripleCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    tripleCapsuleSpaceOdds1.grid(row=29, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=29, column=14)
    tripleCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    tripleCapsuleSpaceOdds2.grid(row=29, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=29, column=16)
    tripleCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    tripleCapsuleSpaceOdds34.grid(row=29, column=17)

    # Koopa
    icon = create_image_icon(content_frame, "assets/items/koopaCapsule.png", 30, 1)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    label.grid(row=30, column=2)
    koopaCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    koopaCapsulePrice1.grid(row=30, column=3)
    label = ctk.CTkLabel(master=content_frame, text="  Cost\n    2nd  ", font=("Arial", 14))
    label.grid(row=30, column=4)
    koopaCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    koopaCapsulePrice2.grid(row=30, column=5)
    label = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    label.grid(row=30, column=6)
    koopaCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    koopaCapsulePrice34.grid(row=30, column=7)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    label.grid(row=30, column=8)
    koopaCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    koopaCapsuleShopOdds12.grid(row=30, column=9)
    label = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    label.grid(row=30, column=10)
    koopaCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    koopaCapsuleShopOdds34.grid(row=30, column=11)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    label.grid(row=30, column=12)
    koopaCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    koopaCapsuleSpaceOdds1.grid(row=30, column=13)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    label.grid(row=30, column=14)
    koopaCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    koopaCapsuleSpaceOdds2.grid(row=30, column=15)
    label = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    label.grid(row=30, column=16)
    koopaCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    koopaCapsuleSpaceOdds34.grid(row=30, column=17)

    # Cursed Mushroom Capsule
    icon = create_image_icon(content_frame, "assets/items/cursedMushroomCapsule7.png", 31, 1)
    labelPoison1 = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    labelPoison1.grid(row=31, column=2)
    poisonMushroomPrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    poisonMushroomPrice1.grid(row=31, column=3)
    labelPoison2 = ctk.CTkLabel(master=content_frame, text="  Cost\n   2nd  ", font=("Arial", 14))
    labelPoison2.grid(row=31, column=4)
    poisonMushroomPrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    poisonMushroomPrice2.grid(row=31, column=5)
    labelPoison3 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    labelPoison3.grid(row=31, column=6)
    poisonMushroomPrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    poisonMushroomPrice34.grid(row=31, column=7)
    labelPoison4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    labelPoison4.grid(row=31, column=8)
    poisonMushroomShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    poisonMushroomShopOdds12.grid(row=31, column=9)
    labelPoison5 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    labelPoison5.grid(row=31, column=10)
    poisonMushroomShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    poisonMushroomShopOdds34.grid(row=31, column=11)
    labelPoison6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    labelPoison6.grid(row=31, column=12)
    poisonMushroomSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    poisonMushroomSpaceOdds1.grid(row=31, column=13)
    labelPoison7 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    labelPoison7.grid(row=31, column=14)
    poisonMushroomSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    poisonMushroomSpaceOdds2.grid(row=31, column=15)
    labelPoison8 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    labelPoison8.grid(row=31, column=16)
    poisonMushroomSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    poisonMushroomSpaceOdds34.grid(row=31, column=17)

    # Duel Capsule
    icon = create_image_icon(content_frame, "assets/items/duelCapsule.png", 32, 1)
    labelDuel1 = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    labelDuel1.grid(row=32, column=2)
    duelCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    duelCapsulePrice1.grid(row=32, column=3)
    labelDuel2 = ctk.CTkLabel(master=content_frame, text="  Cost\n   2nd  ", font=("Arial", 14))
    labelDuel2.grid(row=32, column=4)
    duelCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    duelCapsulePrice2.grid(row=32, column=5)
    labelDuel3 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    labelDuel3.grid(row=32, column=6)
    duelCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    duelCapsulePrice34.grid(row=32, column=7)
    labelDuel4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    labelDuel4.grid(row=32, column=8)
    duelCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    duelCapsuleShopOdds12.grid(row=32, column=9)
    labelDuel5 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    labelDuel5.grid(row=32, column=10)
    duelCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    duelCapsuleShopOdds34.grid(row=32, column=11)
    labelDuel6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    labelDuel6.grid(row=32, column=12)
    duelCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    duelCapsuleSpaceOdds1.grid(row=32, column=13)
    labelDuel7 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    labelDuel7.grid(row=32, column=14)
    duelCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    duelCapsuleSpaceOdds2.grid(row=32, column=15)
    labelDuel8 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    labelDuel8.grid(row=32, column=16)
    duelCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    duelCapsuleSpaceOdds34.grid(row=32, column=17)

    # DK Capsule
    icon = create_image_icon(content_frame, "assets/items/dkCapsule.png", 33, 1)
    labelDK1 = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    labelDK1.grid(row=33, column=2)
    dkCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    dkCapsulePrice1.grid(row=33, column=3)
    labelDK2 = ctk.CTkLabel(master=content_frame, text="  Cost\n   2nd  ", font=("Arial", 14))
    labelDK2.grid(row=33, column=4)
    dkCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    dkCapsulePrice2.grid(row=33, column=5)
    labelDK3 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    labelDK3.grid(row=33, column=6)
    dkCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    dkCapsulePrice34.grid(row=33, column=7)
    labelDK4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    labelDK4.grid(row=33, column=8)
    dkCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    dkCapsuleShopOdds12.grid(row=33, column=9)
    labelDK5 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    labelDK5.grid(row=33, column=10)
    dkCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    dkCapsuleShopOdds34.grid(row=33, column=11)
    labelDK6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    labelDK6.grid(row=33, column=12)
    dkCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    dkCapsuleSpaceOdds1.grid(row=33, column=13)
    labelDK7 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    labelDK7.grid(row=33, column=14)
    dkCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    dkCapsuleSpaceOdds2.grid(row=33, column=15)
    labelDK8 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    labelDK8.grid(row=33, column=16)
    dkCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    dkCapsuleSpaceOdds34.grid(row=33, column=17)

    # Orb Bag Capsule
    icon = create_image_icon(content_frame, "assets/items/orbBagCapsule.png", 34, 1)
    labelOrbBag1 = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    labelOrbBag1.grid(row=34, column=2)
    orbBagCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    orbBagCapsulePrice1.grid(row=34, column=3)
    labelOrbBag2 = ctk.CTkLabel(master=content_frame, text="  Cost\n   2nd  ", font=("Arial", 14))
    labelOrbBag2.grid(row=34, column=4)
    orbBagCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    orbBagCapsulePrice2.grid(row=34, column=5)
    labelOrbBag3 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    labelOrbBag3.grid(row=34, column=6)
    orbBagCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    orbBagCapsulePrice34.grid(row=34, column=7)
    labelOrbBag4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    labelOrbBag4.grid(row=34, column=8)
    orbBagCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    orbBagCapsuleShopOdds12.grid(row=34, column=9)
    labelOrbBag5 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    labelOrbBag5.grid(row=34, column=10)
    orbBagCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    orbBagCapsuleShopOdds34.grid(row=34, column=11)
    labelOrbBag6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    labelOrbBag6.grid(row=34, column=12)
    orbBagCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    orbBagCapsuleSpaceOdds1.grid(row=34, column=13)
    labelOrbBag7 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    labelOrbBag7.grid(row=34, column=14)
    orbBagCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    orbBagCapsuleSpaceOdds2.grid(row=34, column=15)
    labelOrbBag8 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    labelOrbBag8.grid(row=34, column=16)
    orbBagCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    orbBagCapsuleSpaceOdds34.grid(row=34, column=17)

    # Mystery Capsule
    icon = create_image_icon(content_frame, "assets/items/mysteryCapsule.png", 35, 1)
    labelMystery1 = ctk.CTkLabel(master=content_frame, text="  Cost\n   1st  ", font=("Arial", 14))
    labelMystery1.grid(row=35, column=2)
    mysteryCapsulePrice1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mysteryCapsulePrice1.grid(row=35, column=3)
    labelMystery2 = ctk.CTkLabel(master=content_frame, text="  Cost\n   2nd  ", font=("Arial", 14))
    labelMystery2.grid(row=35, column=4)
    mysteryCapsulePrice2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mysteryCapsulePrice2.grid(row=35, column=5)
    labelMystery3 = ctk.CTkLabel(master=content_frame, text=" Cost\n  3rd / 4th ", font=("Arial", 14))
    labelMystery3.grid(row=35, column=6)
    mysteryCapsulePrice34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mysteryCapsulePrice34.grid(row=35, column=7)
    labelMystery4 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n    Early   ", font=("Arial", 14))
    labelMystery4.grid(row=35, column=8)
    mysteryCapsuleShopOdds12 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mysteryCapsuleShopOdds12.grid(row=35, column=9)
    labelMystery5 = ctk.CTkLabel(master=content_frame, text=" Shop Odd\n     Late    ", font=("Arial", 14))
    labelMystery5.grid(row=35, column=10)
    mysteryCapsuleShopOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mysteryCapsuleShopOdds34.grid(row=35, column=11)
    labelMystery6 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      1st ", font=("Arial", 14))
    labelMystery6.grid(row=35, column=12)
    mysteryCapsuleSpaceOdds1 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mysteryCapsuleSpaceOdds1.grid(row=35, column=13)
    labelMystery7 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      2nd ", font=("Arial", 14))
    labelMystery7.grid(row=35, column=14)
    mysteryCapsuleSpaceOdds2 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mysteryCapsuleSpaceOdds2.grid(row=35, column=15)
    labelMystery8 = ctk.CTkLabel(master=content_frame, text="     Pickup Odd  \n      3rd / 4th ", font=("Arial", 14))
    labelMystery8.grid(row=35, column=16)
    mysteryCapsuleSpaceOdds34 = ctk.CTkEntry(master=content_frame, width=48, font=("Arial", 16, "bold"))
    mysteryCapsuleSpaceOdds34.grid(row=35, column=17)

    global hide_custom
    hide_custom = False
    
    parseButton = ctk.CTkButton(master=tabview.tab("Orb Mods"), command=lambda: itemsEvent_mp7(
        mushroomCapsuleShopOdds12, mushroomCapsuleShopOdds34,
        mushroomCapsuleSpaceOdds1,mushroomCapsuleSpaceOdds2, mushroomCapsuleSpaceOdds34,
        goldenMushroomCapsulePrice1, goldenMushroomCapsulePrice2, goldenMushroomCapsulePrice34, 
        goldenMushroomCapsuleShopOdds12, goldenMushroomCapsuleShopOdds34, 
        goldenMushroomCapsuleSpaceOdds1, goldenMushroomCapsuleSpaceOdds2, goldenMushroomCapsuleSpaceOdds34,
        slowMushroomCapsulePrice1, slowMushroomCapsulePrice2, slowMushroomCapsulePrice34, 
        slowMushroomCapsuleShopOdds12, slowMushroomCapsuleShopOdds34, 
        slowMushroomCapsuleSpaceOdds1, slowMushroomCapsuleSpaceOdds2, slowMushroomCapsuleSpaceOdds34,
        metalMushroomCapsulePrice1, metalMushroomCapsulePrice2, metalMushroomCapsulePrice34, 
        metalMushroomCapsuleShopOdds12, metalMushroomCapsuleShopOdds34, 
        metalMushroomCapsuleSpaceOdds1, metalMushroomCapsuleSpaceOdds2, metalMushroomCapsuleSpaceOdds34,
        flutterCapsulePrice1, flutterCapsulePrice2, flutterCapsulePrice34, 
        flutterCapsuleShopOdds12, flutterCapsuleShopOdds34, 
        flutterCapsuleSpaceOdds1, flutterCapsuleSpaceOdds2, flutterCapsuleSpaceOdds34,
        cannonCapsulePrice1, cannonCapsulePrice2, cannonCapsulePrice34, 
        cannonCapsuleShopOdds12, cannonCapsuleShopOdds34, 
        cannonCapsuleSpaceOdds1, cannonCapsuleSpaceOdds2, cannonCapsuleSpaceOdds34,
        snackCapsulePrice1, snackCapsulePrice2, snackCapsulePrice34, 
        snackCapsuleShopOdds12, snackCapsuleShopOdds34, 
        snackCapsuleSpaceOdds1, snackCapsuleSpaceOdds2, snackCapsuleSpaceOdds34,
        lakituCapsulePrice1, lakituCapsulePrice2, lakituCapsulePrice34, 
        lakituCapsuleShopOdds12, lakituCapsuleShopOdds34, 
        lakituCapsuleSpaceOdds1, lakituCapsuleSpaceOdds2, lakituCapsuleSpaceOdds34,
        hammerBroCapsulePrice1, hammerBroCapsulePrice2, hammerBroCapsulePrice34, 
        hammerBroCapsuleShopOdds12, hammerBroCapsuleShopOdds34, 
        hammerBroCapsuleSpaceOdds1, hammerBroCapsuleSpaceOdds2, hammerBroCapsuleSpaceOdds34,
        piranhaPlantCapsulePrice1, piranhaPlantCapsulePrice2, piranhaPlantCapsulePrice34, 
        piranhaPlantCapsuleShopOdds12, piranhaPlantCapsuleShopOdds34, 
        piranhaPlantCapsuleSpaceOdds1, piranhaPlantCapsuleSpaceOdds2, piranhaPlantCapsuleSpaceOdds34,
        spearGuyCapsulePrice1, spearGuyCapsulePrice2, spearGuyCapsulePrice34, 
        spearGuyCapsuleShopOdds12, spearGuyCapsuleShopOdds34, 
        spearGuyCapsuleSpaceOdds1, spearGuyCapsuleSpaceOdds2, spearGuyCapsuleSpaceOdds34,
        kamekCapsulePrice1, kamekCapsulePrice2, kamekCapsulePrice34, 
        kamekCapsuleShopOdds12, kamekCapsuleShopOdds34, 
        kamekCapsuleSpaceOdds1, kamekCapsuleSpaceOdds2, kamekCapsuleSpaceOdds34,
        toadyCapsulePrice1, toadyCapsulePrice2, toadyCapsulePrice34, 
        toadyCapsuleShopOdds12, toadyCapsuleShopOdds34, 
        toadyCapsuleSpaceOdds1, toadyCapsuleSpaceOdds2, toadyCapsuleSpaceOdds34,
        mrBlizzardCapsulePrice1, mrBlizzardCapsulePrice2, mrBlizzardCapsulePrice34, 
        mrBlizzardCapsuleShopOdds12, mrBlizzardCapsuleShopOdds34, 
        mrBlizzardCapsuleSpaceOdds1, mrBlizzardCapsuleSpaceOdds2, mrBlizzardCapsuleSpaceOdds34,
        banditCapsulePrice1, banditCapsulePrice2, banditCapsulePrice34, 
        banditCapsuleShopOdds12, banditCapsuleShopOdds34, 
        banditCapsuleSpaceOdds1, banditCapsuleSpaceOdds2, banditCapsuleSpaceOdds34,
        pinkBooCapsulePrice1, pinkBooCapsulePrice2, pinkBooCapsulePrice34, 
        pinkBooCapsuleShopOdds12, pinkBooCapsuleShopOdds34, 
        pinkBooCapsuleSpaceOdds1, pinkBooCapsuleSpaceOdds2, pinkBooCapsuleSpaceOdds34,
        spinyCapsulePrice1, spinyCapsulePrice2, spinyCapsulePrice34, 
        spinyCapsuleShopOdds12, spinyCapsuleShopOdds34, 
        spinyCapsuleSpaceOdds1, spinyCapsuleSpaceOdds2, spinyCapsuleSpaceOdds34,
        zapCapsulePrice1, zapCapsulePrice2, zapCapsulePrice34, 
        zapCapsuleShopOdds12, zapCapsuleShopOdds34, 
        zapCapsuleSpaceOdds1, zapCapsuleSpaceOdds2, zapCapsuleSpaceOdds34,
        tweesterCapsulePrice1, tweesterCapsulePrice2, tweesterCapsulePrice34, 
        tweesterCapsuleShopOdds12, tweesterCapsuleShopOdds34, 
        tweesterCapsuleSpaceOdds1, tweesterCapsuleSpaceOdds2, tweesterCapsuleSpaceOdds34,
        thwompCapsulePrice1, thwompCapsulePrice2, thwompCapsulePrice34, 
        thwompCapsuleShopOdds12, thwompCapsuleShopOdds34, 
        thwompCapsuleSpaceOdds1, thwompCapsuleSpaceOdds2, thwompCapsuleSpaceOdds34,
        warpCapsulePrice1, warpCapsulePrice2, warpCapsulePrice34, 
        warpCapsuleShopOdds12, warpCapsuleShopOdds34, 
        warpCapsuleSpaceOdds1, warpCapsuleSpaceOdds2, warpCapsuleSpaceOdds34,
        bombCapsulePrice1, bombCapsulePrice2, bombCapsulePrice34, 
        bombCapsuleShopOdds12, bombCapsuleShopOdds34, 
        bombCapsuleSpaceOdds1, bombCapsuleSpaceOdds2, bombCapsuleSpaceOdds34,
        fireballCapsulePrice1, fireballCapsulePrice2, fireballCapsulePrice34, 
        fireballCapsuleShopOdds12, fireballCapsuleShopOdds34, 
        fireballCapsuleSpaceOdds1, fireballCapsuleSpaceOdds2, fireballCapsuleSpaceOdds34,
        flowerCapsulePrice1, flowerCapsulePrice2, flowerCapsulePrice34, 
        flowerCapsuleShopOdds12, flowerCapsuleShopOdds34, 
        flowerCapsuleSpaceOdds1, flowerCapsuleSpaceOdds2, flowerCapsuleSpaceOdds34,
        eggCapsulePrice1, eggCapsulePrice2, eggCapsulePrice34, 
        eggCapsuleShopOdds12, eggCapsuleShopOdds34, 
        eggCapsuleSpaceOdds1, eggCapsuleSpaceOdds2, eggCapsuleSpaceOdds34,
        vacuumCapsulePrice1, vacuumCapsulePrice2, vacuumCapsulePrice34, 
        vacuumCapsuleShopOdds12, vacuumCapsuleShopOdds34, 
        vacuumCapsuleSpaceOdds1, vacuumCapsuleSpaceOdds2, vacuumCapsuleSpaceOdds34,
        magicCapsulePrice1, magicCapsulePrice2, magicCapsulePrice34, 
        magicCapsuleShopOdds12, magicCapsuleShopOdds34, 
        magicCapsuleSpaceOdds1, magicCapsuleSpaceOdds2, magicCapsuleSpaceOdds34,
        tripleCapsulePrice1, tripleCapsulePrice2, tripleCapsulePrice34, 
        tripleCapsuleShopOdds12, tripleCapsuleShopOdds34, 
        tripleCapsuleSpaceOdds1, tripleCapsuleSpaceOdds2, tripleCapsuleSpaceOdds34,
        koopaCapsulePrice1, koopaCapsulePrice2, koopaCapsulePrice34, 
        koopaCapsuleShopOdds12, koopaCapsuleShopOdds34, 
        koopaCapsuleSpaceOdds1, koopaCapsuleSpaceOdds2, koopaCapsuleSpaceOdds34,
        poisonMushroomPrice1 if hide_custom == False else "0", 
        poisonMushroomPrice2 if hide_custom == False else "0", 
        poisonMushroomPrice34 if hide_custom == False else "0", 
        poisonMushroomShopOdds12 if hide_custom == False else "0", 
        poisonMushroomShopOdds34 if hide_custom == False else "0", 
        poisonMushroomSpaceOdds1 if hide_custom == False else "0", 
        poisonMushroomSpaceOdds2 if hide_custom == False else "0", 
        poisonMushroomSpaceOdds34 if hide_custom == False else "0", 
        orbBagCapsulePrice1 if hide_custom == False else "0", 
        orbBagCapsulePrice2 if hide_custom == False else "0", 
        orbBagCapsulePrice34 if hide_custom == False else "0", 
        orbBagCapsuleShopOdds12 if hide_custom == False else "0", 
        orbBagCapsuleShopOdds34 if hide_custom == False else "0", 
        orbBagCapsuleSpaceOdds1 if hide_custom == False else "0", 
        orbBagCapsuleSpaceOdds2 if hide_custom == False else "0", 
        orbBagCapsuleSpaceOdds34 if hide_custom == False else "0", 
        mysteryCapsulePrice1 if hide_custom == False else "0", 
        mysteryCapsulePrice2 if hide_custom == False else "0", 
        mysteryCapsulePrice34 if hide_custom == False else "0", 
        mysteryCapsuleShopOdds12 if hide_custom == False else "0", 
        mysteryCapsuleShopOdds34 if hide_custom == False else "0", 
        mysteryCapsuleSpaceOdds1 if hide_custom == False else "0", 
        mysteryCapsuleSpaceOdds2 if hide_custom == False else "0", 
        mysteryCapsuleSpaceOdds34 if hide_custom == False else "0", 
        dkCapsulePrice1 if hide_custom == False else "0", 
        dkCapsulePrice2 if hide_custom == False else "0", 
        dkCapsulePrice34 if hide_custom == False else "0", 
        dkCapsuleShopOdds12 if hide_custom == False else "0", 
        dkCapsuleShopOdds34 if hide_custom == False else "0", 
        dkCapsuleSpaceOdds1 if hide_custom == False else "0", 
        dkCapsuleSpaceOdds2 if hide_custom == False else "0", 
        dkCapsuleSpaceOdds34 if hide_custom == False else "0", 
        duelCapsulePrice1 if hide_custom == False else "0", 
        duelCapsulePrice2 if hide_custom == False else "0", 
        duelCapsulePrice34 if hide_custom == False else "0", 
        duelCapsuleShopOdds12 if hide_custom == False else "0", 
        duelCapsuleShopOdds34 if hide_custom == False else "0", 
        duelCapsuleSpaceOdds1 if hide_custom == False else "0", 
        duelCapsuleSpaceOdds2 if hide_custom == False else "0", 
        duelCapsuleSpaceOdds34 if hide_custom == False else "0"
    ), text="Generate Code")
    parseButton.place(x=10, y=800)


    parseButton = ctk.CTkButton(master=tabview.tab("Orb Mods"), command=lambda: savePresetItems7(
        mushroomCapsuleShopOdds12, mushroomCapsuleShopOdds34,
        mushroomCapsuleSpaceOdds1,mushroomCapsuleSpaceOdds2, mushroomCapsuleSpaceOdds34,
        goldenMushroomCapsulePrice1, goldenMushroomCapsulePrice2, goldenMushroomCapsulePrice34, 
        goldenMushroomCapsuleShopOdds12, goldenMushroomCapsuleShopOdds34, 
        goldenMushroomCapsuleSpaceOdds1, goldenMushroomCapsuleSpaceOdds2, goldenMushroomCapsuleSpaceOdds34,
        slowMushroomCapsulePrice1, slowMushroomCapsulePrice2, slowMushroomCapsulePrice34, 
        slowMushroomCapsuleShopOdds12, slowMushroomCapsuleShopOdds34, 
        slowMushroomCapsuleSpaceOdds1, slowMushroomCapsuleSpaceOdds2, slowMushroomCapsuleSpaceOdds34,
        metalMushroomCapsulePrice1, metalMushroomCapsulePrice2, metalMushroomCapsulePrice34, 
        metalMushroomCapsuleShopOdds12, metalMushroomCapsuleShopOdds34, 
        metalMushroomCapsuleSpaceOdds1, metalMushroomCapsuleSpaceOdds2, metalMushroomCapsuleSpaceOdds34,
        flutterCapsulePrice1, flutterCapsulePrice2, flutterCapsulePrice34, 
        flutterCapsuleShopOdds12, flutterCapsuleShopOdds34, 
        flutterCapsuleSpaceOdds1, flutterCapsuleSpaceOdds2, flutterCapsuleSpaceOdds34,
        cannonCapsulePrice1, cannonCapsulePrice2, cannonCapsulePrice34, 
        cannonCapsuleShopOdds12, cannonCapsuleShopOdds34, 
        cannonCapsuleSpaceOdds1, cannonCapsuleSpaceOdds2, cannonCapsuleSpaceOdds34,
        snackCapsulePrice1, snackCapsulePrice2, snackCapsulePrice34, 
        snackCapsuleShopOdds12, snackCapsuleShopOdds34, 
        snackCapsuleSpaceOdds1, snackCapsuleSpaceOdds2, snackCapsuleSpaceOdds34,
        lakituCapsulePrice1, lakituCapsulePrice2, lakituCapsulePrice34, 
        lakituCapsuleShopOdds12, lakituCapsuleShopOdds34, 
        lakituCapsuleSpaceOdds1, lakituCapsuleSpaceOdds2, lakituCapsuleSpaceOdds34,
        hammerBroCapsulePrice1, hammerBroCapsulePrice2, hammerBroCapsulePrice34, 
        hammerBroCapsuleShopOdds12, hammerBroCapsuleShopOdds34, 
        hammerBroCapsuleSpaceOdds1, hammerBroCapsuleSpaceOdds2, hammerBroCapsuleSpaceOdds34,
        piranhaPlantCapsulePrice1, piranhaPlantCapsulePrice2, piranhaPlantCapsulePrice34, 
        piranhaPlantCapsuleShopOdds12, piranhaPlantCapsuleShopOdds34, 
        piranhaPlantCapsuleSpaceOdds1, piranhaPlantCapsuleSpaceOdds2, piranhaPlantCapsuleSpaceOdds34,
        spearGuyCapsulePrice1, spearGuyCapsulePrice2, spearGuyCapsulePrice34, 
        spearGuyCapsuleShopOdds12, spearGuyCapsuleShopOdds34, 
        spearGuyCapsuleSpaceOdds1, spearGuyCapsuleSpaceOdds2, spearGuyCapsuleSpaceOdds34,
        kamekCapsulePrice1, kamekCapsulePrice2, kamekCapsulePrice34, 
        kamekCapsuleShopOdds12, kamekCapsuleShopOdds34, 
        kamekCapsuleSpaceOdds1, kamekCapsuleSpaceOdds2, kamekCapsuleSpaceOdds34,
        toadyCapsulePrice1, toadyCapsulePrice2, toadyCapsulePrice34, 
        toadyCapsuleShopOdds12, toadyCapsuleShopOdds34, 
        toadyCapsuleSpaceOdds1, toadyCapsuleSpaceOdds2, toadyCapsuleSpaceOdds34,
        mrBlizzardCapsulePrice1, mrBlizzardCapsulePrice2, mrBlizzardCapsulePrice34, 
        mrBlizzardCapsuleShopOdds12, mrBlizzardCapsuleShopOdds34, 
        mrBlizzardCapsuleSpaceOdds1, mrBlizzardCapsuleSpaceOdds2, mrBlizzardCapsuleSpaceOdds34,
        banditCapsulePrice1, banditCapsulePrice2, banditCapsulePrice34, 
        banditCapsuleShopOdds12, banditCapsuleShopOdds34, 
        banditCapsuleSpaceOdds1, banditCapsuleSpaceOdds2, banditCapsuleSpaceOdds34,
        pinkBooCapsulePrice1, pinkBooCapsulePrice2, pinkBooCapsulePrice34, 
        pinkBooCapsuleShopOdds12, pinkBooCapsuleShopOdds34, 
        pinkBooCapsuleSpaceOdds1, pinkBooCapsuleSpaceOdds2, pinkBooCapsuleSpaceOdds34,
        spinyCapsulePrice1, spinyCapsulePrice2, spinyCapsulePrice34, 
        spinyCapsuleShopOdds12, spinyCapsuleShopOdds34, 
        spinyCapsuleSpaceOdds1, spinyCapsuleSpaceOdds2, spinyCapsuleSpaceOdds34,
        zapCapsulePrice1, zapCapsulePrice2, zapCapsulePrice34, 
        zapCapsuleShopOdds12, zapCapsuleShopOdds34, 
        zapCapsuleSpaceOdds1, zapCapsuleSpaceOdds2, zapCapsuleSpaceOdds34,
        tweesterCapsulePrice1, tweesterCapsulePrice2, tweesterCapsulePrice34, 
        tweesterCapsuleShopOdds12, tweesterCapsuleShopOdds34, 
        tweesterCapsuleSpaceOdds1, tweesterCapsuleSpaceOdds2, tweesterCapsuleSpaceOdds34,
        thwompCapsulePrice1, thwompCapsulePrice2, thwompCapsulePrice34, 
        thwompCapsuleShopOdds12, thwompCapsuleShopOdds34, 
        thwompCapsuleSpaceOdds1, thwompCapsuleSpaceOdds2, thwompCapsuleSpaceOdds34,
        warpCapsulePrice1, warpCapsulePrice2, warpCapsulePrice34, 
        warpCapsuleShopOdds12, warpCapsuleShopOdds34, 
        warpCapsuleSpaceOdds1, warpCapsuleSpaceOdds2, warpCapsuleSpaceOdds34,
        bombCapsulePrice1, bombCapsulePrice2, bombCapsulePrice34, 
        bombCapsuleShopOdds12, bombCapsuleShopOdds34, 
        bombCapsuleSpaceOdds1, bombCapsuleSpaceOdds2, bombCapsuleSpaceOdds34,
        fireballCapsulePrice1, fireballCapsulePrice2, fireballCapsulePrice34, 
        fireballCapsuleShopOdds12, fireballCapsuleShopOdds34, 
        fireballCapsuleSpaceOdds1, fireballCapsuleSpaceOdds2, fireballCapsuleSpaceOdds34,
        flowerCapsulePrice1, flowerCapsulePrice2, flowerCapsulePrice34, 
        flowerCapsuleShopOdds12, flowerCapsuleShopOdds34, 
        flowerCapsuleSpaceOdds1, flowerCapsuleSpaceOdds2, flowerCapsuleSpaceOdds34,
        eggCapsulePrice1, eggCapsulePrice2, eggCapsulePrice34, 
        eggCapsuleShopOdds12, eggCapsuleShopOdds34, 
        eggCapsuleSpaceOdds1, eggCapsuleSpaceOdds2, eggCapsuleSpaceOdds34,
        vacuumCapsulePrice1, vacuumCapsulePrice2, vacuumCapsulePrice34, 
        vacuumCapsuleShopOdds12, vacuumCapsuleShopOdds34, 
        vacuumCapsuleSpaceOdds1, vacuumCapsuleSpaceOdds2, vacuumCapsuleSpaceOdds34,
        magicCapsulePrice1, magicCapsulePrice2, magicCapsulePrice34, 
        magicCapsuleShopOdds12, magicCapsuleShopOdds34, 
        magicCapsuleSpaceOdds1, magicCapsuleSpaceOdds2, magicCapsuleSpaceOdds34,
        tripleCapsulePrice1, tripleCapsulePrice2, tripleCapsulePrice34, 
        tripleCapsuleShopOdds12, tripleCapsuleShopOdds34, 
        tripleCapsuleSpaceOdds1, tripleCapsuleSpaceOdds2, tripleCapsuleSpaceOdds34,
        koopaCapsulePrice1, koopaCapsulePrice2, koopaCapsulePrice34, 
        koopaCapsuleShopOdds12, koopaCapsuleShopOdds34, 
        koopaCapsuleSpaceOdds1, koopaCapsuleSpaceOdds2, koopaCapsuleSpaceOdds34,
        poisonMushroomPrice1 if hide_custom == False else "0", 
        poisonMushroomPrice2 if hide_custom == False else "0", 
        poisonMushroomPrice34 if hide_custom == False else "0", 
        poisonMushroomShopOdds12 if hide_custom == False else "0", 
        poisonMushroomShopOdds34 if hide_custom == False else "0", 
        poisonMushroomSpaceOdds1 if hide_custom == False else "0", 
        poisonMushroomSpaceOdds2 if hide_custom == False else "0", 
        poisonMushroomSpaceOdds34 if hide_custom == False else "0", 
        orbBagCapsulePrice1 if hide_custom == False else "0", 
        orbBagCapsulePrice2 if hide_custom == False else "0", 
        orbBagCapsulePrice34 if hide_custom == False else "0", 
        orbBagCapsuleShopOdds12 if hide_custom == False else "0", 
        orbBagCapsuleShopOdds34 if hide_custom == False else "0", 
        orbBagCapsuleSpaceOdds1 if hide_custom == False else "0", 
        orbBagCapsuleSpaceOdds2 if hide_custom == False else "0", 
        orbBagCapsuleSpaceOdds34 if hide_custom == False else "0", 
        mysteryCapsulePrice1 if hide_custom == False else "0", 
        mysteryCapsulePrice2 if hide_custom == False else "0", 
        mysteryCapsulePrice34 if hide_custom == False else "0", 
        mysteryCapsuleShopOdds12 if hide_custom == False else "0", 
        mysteryCapsuleShopOdds34 if hide_custom == False else "0", 
        mysteryCapsuleSpaceOdds1 if hide_custom == False else "0", 
        mysteryCapsuleSpaceOdds2 if hide_custom == False else "0", 
        mysteryCapsuleSpaceOdds34 if hide_custom == False else "0", 
        dkCapsulePrice1 if hide_custom == False else "0", 
        dkCapsulePrice2 if hide_custom == False else "0", 
        dkCapsulePrice34 if hide_custom == False else "0", 
        dkCapsuleShopOdds12 if hide_custom == False else "0", 
        dkCapsuleShopOdds34 if hide_custom == False else "0", 
        dkCapsuleSpaceOdds1 if hide_custom == False else "0", 
        dkCapsuleSpaceOdds2 if hide_custom == False else "0", 
        dkCapsuleSpaceOdds34 if hide_custom == False else "0", 
        duelCapsulePrice1 if hide_custom == False else "0", 
        duelCapsulePrice2 if hide_custom == False else "0", 
        duelCapsulePrice34 if hide_custom == False else "0", 
        duelCapsuleShopOdds12 if hide_custom == False else "0", 
        duelCapsuleShopOdds34 if hide_custom == False else "0", 
        duelCapsuleSpaceOdds1 if hide_custom == False else "0", 
        duelCapsuleSpaceOdds2 if hide_custom == False else "0", 
        duelCapsuleSpaceOdds34 if hide_custom == False else "0"
    ), text="Save Preset")
    parseButton.place(x=160, y=800)

    parseButton = ctk.CTkButton(master=tabview.tab("Orb Mods"), command=lambda: loadPresetItems7(
        hide_custom,
        mushroomCapsuleShopOdds12, mushroomCapsuleShopOdds34,
        mushroomCapsuleSpaceOdds1,mushroomCapsuleSpaceOdds2, mushroomCapsuleSpaceOdds34,
        goldenMushroomCapsulePrice1, goldenMushroomCapsulePrice2, goldenMushroomCapsulePrice34, 
        goldenMushroomCapsuleShopOdds12, goldenMushroomCapsuleShopOdds34, 
        goldenMushroomCapsuleSpaceOdds1, goldenMushroomCapsuleSpaceOdds2, goldenMushroomCapsuleSpaceOdds34,
        slowMushroomCapsulePrice1, slowMushroomCapsulePrice2, slowMushroomCapsulePrice34, 
        slowMushroomCapsuleShopOdds12, slowMushroomCapsuleShopOdds34, 
        slowMushroomCapsuleSpaceOdds1, slowMushroomCapsuleSpaceOdds2, slowMushroomCapsuleSpaceOdds34,
        metalMushroomCapsulePrice1, metalMushroomCapsulePrice2, metalMushroomCapsulePrice34, 
        metalMushroomCapsuleShopOdds12, metalMushroomCapsuleShopOdds34, 
        metalMushroomCapsuleSpaceOdds1, metalMushroomCapsuleSpaceOdds2, metalMushroomCapsuleSpaceOdds34,
        flutterCapsulePrice1, flutterCapsulePrice2, flutterCapsulePrice34, 
        flutterCapsuleShopOdds12, flutterCapsuleShopOdds34, 
        flutterCapsuleSpaceOdds1, flutterCapsuleSpaceOdds2, flutterCapsuleSpaceOdds34,
        cannonCapsulePrice1, cannonCapsulePrice2, cannonCapsulePrice34, 
        cannonCapsuleShopOdds12, cannonCapsuleShopOdds34, 
        cannonCapsuleSpaceOdds1, cannonCapsuleSpaceOdds2, cannonCapsuleSpaceOdds34,
        snackCapsulePrice1, snackCapsulePrice2, snackCapsulePrice34, 
        snackCapsuleShopOdds12, snackCapsuleShopOdds34, 
        snackCapsuleSpaceOdds1, snackCapsuleSpaceOdds2, snackCapsuleSpaceOdds34,
        lakituCapsulePrice1, lakituCapsulePrice2, lakituCapsulePrice34, 
        lakituCapsuleShopOdds12, lakituCapsuleShopOdds34, 
        lakituCapsuleSpaceOdds1, lakituCapsuleSpaceOdds2, lakituCapsuleSpaceOdds34,
        hammerBroCapsulePrice1, hammerBroCapsulePrice2, hammerBroCapsulePrice34, 
        hammerBroCapsuleShopOdds12, hammerBroCapsuleShopOdds34, 
        hammerBroCapsuleSpaceOdds1, hammerBroCapsuleSpaceOdds2, hammerBroCapsuleSpaceOdds34,
        piranhaPlantCapsulePrice1, piranhaPlantCapsulePrice2, piranhaPlantCapsulePrice34, 
        piranhaPlantCapsuleShopOdds12, piranhaPlantCapsuleShopOdds34, 
        piranhaPlantCapsuleSpaceOdds1, piranhaPlantCapsuleSpaceOdds2, piranhaPlantCapsuleSpaceOdds34,
        spearGuyCapsulePrice1, spearGuyCapsulePrice2, spearGuyCapsulePrice34, 
        spearGuyCapsuleShopOdds12, spearGuyCapsuleShopOdds34, 
        spearGuyCapsuleSpaceOdds1, spearGuyCapsuleSpaceOdds2, spearGuyCapsuleSpaceOdds34,
        kamekCapsulePrice1, kamekCapsulePrice2, kamekCapsulePrice34, 
        kamekCapsuleShopOdds12, kamekCapsuleShopOdds34, 
        kamekCapsuleSpaceOdds1, kamekCapsuleSpaceOdds2, kamekCapsuleSpaceOdds34,
        toadyCapsulePrice1, toadyCapsulePrice2, toadyCapsulePrice34, 
        toadyCapsuleShopOdds12, toadyCapsuleShopOdds34, 
        toadyCapsuleSpaceOdds1, toadyCapsuleSpaceOdds2, toadyCapsuleSpaceOdds34,
        mrBlizzardCapsulePrice1, mrBlizzardCapsulePrice2, mrBlizzardCapsulePrice34, 
        mrBlizzardCapsuleShopOdds12, mrBlizzardCapsuleShopOdds34, 
        mrBlizzardCapsuleSpaceOdds1, mrBlizzardCapsuleSpaceOdds2, mrBlizzardCapsuleSpaceOdds34,
        banditCapsulePrice1, banditCapsulePrice2, banditCapsulePrice34, 
        banditCapsuleShopOdds12, banditCapsuleShopOdds34, 
        banditCapsuleSpaceOdds1, banditCapsuleSpaceOdds2, banditCapsuleSpaceOdds34,
        pinkBooCapsulePrice1, pinkBooCapsulePrice2, pinkBooCapsulePrice34, 
        pinkBooCapsuleShopOdds12, pinkBooCapsuleShopOdds34, 
        pinkBooCapsuleSpaceOdds1, pinkBooCapsuleSpaceOdds2, pinkBooCapsuleSpaceOdds34,
        spinyCapsulePrice1, spinyCapsulePrice2, spinyCapsulePrice34, 
        spinyCapsuleShopOdds12, spinyCapsuleShopOdds34, 
        spinyCapsuleSpaceOdds1, spinyCapsuleSpaceOdds2, spinyCapsuleSpaceOdds34,
        zapCapsulePrice1, zapCapsulePrice2, zapCapsulePrice34, 
        zapCapsuleShopOdds12, zapCapsuleShopOdds34, 
        zapCapsuleSpaceOdds1, zapCapsuleSpaceOdds2, zapCapsuleSpaceOdds34,
        tweesterCapsulePrice1, tweesterCapsulePrice2, tweesterCapsulePrice34, 
        tweesterCapsuleShopOdds12, tweesterCapsuleShopOdds34, 
        tweesterCapsuleSpaceOdds1, tweesterCapsuleSpaceOdds2, tweesterCapsuleSpaceOdds34,
        thwompCapsulePrice1, thwompCapsulePrice2, thwompCapsulePrice34, 
        thwompCapsuleShopOdds12, thwompCapsuleShopOdds34, 
        thwompCapsuleSpaceOdds1, thwompCapsuleSpaceOdds2, thwompCapsuleSpaceOdds34,
        warpCapsulePrice1, warpCapsulePrice2, warpCapsulePrice34, 
        warpCapsuleShopOdds12, warpCapsuleShopOdds34, 
        warpCapsuleSpaceOdds1, warpCapsuleSpaceOdds2, warpCapsuleSpaceOdds34,
        bombCapsulePrice1, bombCapsulePrice2, bombCapsulePrice34, 
        bombCapsuleShopOdds12, bombCapsuleShopOdds34, 
        bombCapsuleSpaceOdds1, bombCapsuleSpaceOdds2, bombCapsuleSpaceOdds34,
        fireballCapsulePrice1, fireballCapsulePrice2, fireballCapsulePrice34, 
        fireballCapsuleShopOdds12, fireballCapsuleShopOdds34, 
        fireballCapsuleSpaceOdds1, fireballCapsuleSpaceOdds2, fireballCapsuleSpaceOdds34,
        flowerCapsulePrice1, flowerCapsulePrice2, flowerCapsulePrice34, 
        flowerCapsuleShopOdds12, flowerCapsuleShopOdds34, 
        flowerCapsuleSpaceOdds1, flowerCapsuleSpaceOdds2, flowerCapsuleSpaceOdds34,
        eggCapsulePrice1, eggCapsulePrice2, eggCapsulePrice34, 
        eggCapsuleShopOdds12, eggCapsuleShopOdds34, 
        eggCapsuleSpaceOdds1, eggCapsuleSpaceOdds2, eggCapsuleSpaceOdds34,
        vacuumCapsulePrice1, vacuumCapsulePrice2, vacuumCapsulePrice34, 
        vacuumCapsuleShopOdds12, vacuumCapsuleShopOdds34, 
        vacuumCapsuleSpaceOdds1, vacuumCapsuleSpaceOdds2, vacuumCapsuleSpaceOdds34,
        magicCapsulePrice1, magicCapsulePrice2, magicCapsulePrice34, 
        magicCapsuleShopOdds12, magicCapsuleShopOdds34, 
        magicCapsuleSpaceOdds1, magicCapsuleSpaceOdds2, magicCapsuleSpaceOdds34,
        tripleCapsulePrice1, tripleCapsulePrice2, tripleCapsulePrice34, 
        tripleCapsuleShopOdds12, tripleCapsuleShopOdds34, 
        tripleCapsuleSpaceOdds1, tripleCapsuleSpaceOdds2, tripleCapsuleSpaceOdds34,
        koopaCapsulePrice1, koopaCapsulePrice2, koopaCapsulePrice34, 
        koopaCapsuleShopOdds12, koopaCapsuleShopOdds34, 
        koopaCapsuleSpaceOdds1, koopaCapsuleSpaceOdds2, koopaCapsuleSpaceOdds34,
        poisonMushroomPrice1 if hide_custom == False else "0", 
        poisonMushroomPrice2 if hide_custom == False else "0", 
        poisonMushroomPrice34 if hide_custom == False else "0", 
        poisonMushroomShopOdds12 if hide_custom == False else "0", 
        poisonMushroomShopOdds34 if hide_custom == False else "0", 
        poisonMushroomSpaceOdds1 if hide_custom == False else "0", 
        poisonMushroomSpaceOdds2 if hide_custom == False else "0", 
        poisonMushroomSpaceOdds34 if hide_custom == False else "0", 
        orbBagCapsulePrice1 if hide_custom == False else "0", 
        orbBagCapsulePrice2 if hide_custom == False else "0", 
        orbBagCapsulePrice34 if hide_custom == False else "0", 
        orbBagCapsuleShopOdds12 if hide_custom == False else "0", 
        orbBagCapsuleShopOdds34 if hide_custom == False else "0", 
        orbBagCapsuleSpaceOdds1 if hide_custom == False else "0", 
        orbBagCapsuleSpaceOdds2 if hide_custom == False else "0", 
        orbBagCapsuleSpaceOdds34 if hide_custom == False else "0", 
        mysteryCapsulePrice1 if hide_custom == False else "0", 
        mysteryCapsulePrice2 if hide_custom == False else "0", 
        mysteryCapsulePrice34 if hide_custom == False else "0", 
        mysteryCapsuleShopOdds12 if hide_custom == False else "0", 
        mysteryCapsuleShopOdds34 if hide_custom == False else "0", 
        mysteryCapsuleSpaceOdds1 if hide_custom == False else "0", 
        mysteryCapsuleSpaceOdds2 if hide_custom == False else "0", 
        mysteryCapsuleSpaceOdds34 if hide_custom == False else "0", 
        dkCapsulePrice1 if hide_custom == False else "0", 
        dkCapsulePrice2 if hide_custom == False else "0", 
        dkCapsulePrice34 if hide_custom == False else "0", 
        dkCapsuleShopOdds12 if hide_custom == False else "0", 
        dkCapsuleShopOdds34 if hide_custom == False else "0", 
        dkCapsuleSpaceOdds1 if hide_custom == False else "0", 
        dkCapsuleSpaceOdds2 if hide_custom == False else "0", 
        dkCapsuleSpaceOdds34 if hide_custom == False else "0", 
        duelCapsulePrice1 if hide_custom == False else "0", 
        duelCapsulePrice2 if hide_custom == False else "0", 
        duelCapsulePrice34 if hide_custom == False else "0", 
        duelCapsuleShopOdds12 if hide_custom == False else "0", 
        duelCapsuleShopOdds34 if hide_custom == False else "0", 
        duelCapsuleSpaceOdds1 if hide_custom == False else "0", 
        duelCapsuleSpaceOdds2 if hide_custom == False else "0", 
        duelCapsuleSpaceOdds34 if hide_custom == False else "0"
    ), text="Load Preset")
    parseButton.place(x=310, y=800)

    #parseButtonSevenFillViaCode = ctk.CTkButton(master=tabview.tab("Orb Mods"), command=lambda: fillViaCode7Actions(), text="Fill Via Code")
    #parseButtonSevenFillViaCode.place(x=460, y=800)

    hideCustomSwitch = ctk.CTkSwitch(master=tabview.tab("Orb Mods"), text="Show Custom Orbs")
    hideCustomSwitch.place(x=460, y=800) # x=610

    def toggle_hide_custom():
        global hide_custom
        hide_custom = not hide_custom

        if hide_custom:
            mysteryCapsulePrice1.grid_forget()
            mysteryCapsulePrice2.grid_forget()
            mysteryCapsulePrice34.grid_forget()
            mysteryCapsuleShopOdds12.grid_forget()
            mysteryCapsuleShopOdds34.grid_forget()
            mysteryCapsuleSpaceOdds1.grid_forget()
            mysteryCapsuleSpaceOdds2.grid_forget()
            mysteryCapsuleSpaceOdds34.grid_forget()
            dkCapsulePrice1.grid_forget()
            dkCapsulePrice2.grid_forget()
            dkCapsulePrice34.grid_forget()
            dkCapsuleShopOdds12.grid_forget()
            dkCapsuleShopOdds34.grid_forget()
            dkCapsuleSpaceOdds1.grid_forget()
            dkCapsuleSpaceOdds2.grid_forget()
            dkCapsuleSpaceOdds34.grid_forget()
            orbBagCapsulePrice1.grid_forget()
            orbBagCapsulePrice2.grid_forget()
            orbBagCapsulePrice34.grid_forget()
            orbBagCapsuleShopOdds12.grid_forget()
            orbBagCapsuleShopOdds34.grid_forget()
            orbBagCapsuleSpaceOdds1.grid_forget()
            orbBagCapsuleSpaceOdds2.grid_forget()
            orbBagCapsuleSpaceOdds34.grid_forget()
            duelCapsulePrice1.grid_forget()
            duelCapsulePrice2.grid_forget()
            duelCapsulePrice34.grid_forget()
            duelCapsuleShopOdds12.grid_forget()
            duelCapsuleShopOdds34.grid_forget()
            duelCapsuleSpaceOdds1.grid_forget()
            duelCapsuleSpaceOdds2.grid_forget()
            duelCapsuleSpaceOdds34.grid_forget()
            poisonMushroomPrice1.grid_forget()
            poisonMushroomPrice2.grid_forget()
            poisonMushroomPrice34.grid_forget()
            poisonMushroomShopOdds12.grid_forget()
            poisonMushroomShopOdds34.grid_forget()
            poisonMushroomSpaceOdds1.grid_forget()
            poisonMushroomSpaceOdds2.grid_forget()
            poisonMushroomSpaceOdds34.grid_forget()
            labelMystery1.grid_forget()
            labelMystery2.grid_forget()
            labelMystery3.grid_forget()
            labelMystery4.grid_forget()
            labelMystery5.grid_forget()
            labelMystery6.grid_forget()
            labelMystery7.grid_forget()
            labelMystery8.grid_forget()
            labelDK1.grid_forget()
            labelDK2.grid_forget()
            labelDK3.grid_forget()
            labelDK4.grid_forget()
            labelDK5.grid_forget()
            labelDK6.grid_forget()
            labelDK7.grid_forget()
            labelDK8.grid_forget()
            labelOrbBag1.grid_forget()
            labelOrbBag2.grid_forget()
            labelOrbBag3.grid_forget()
            labelOrbBag4.grid_forget() 
            labelOrbBag5.grid_forget() 
            labelOrbBag6.grid_forget()
            labelOrbBag7.grid_forget()
            labelOrbBag8.grid_forget()
            labelDuel1.grid_forget()
            labelDuel2.grid_forget()
            labelDuel3.grid_forget()
            labelDuel4.grid_forget()
            labelDuel5.grid_forget()
            labelDuel6.grid_forget()
            labelDuel7.grid_forget()
            labelDuel8.grid_forget()
            labelPoison1.grid_forget()
            labelPoison2.grid_forget()
            labelPoison3.grid_forget()
            labelPoison4.grid_forget() 
            labelPoison5.grid_forget() 
            labelPoison6.grid_forget()
            labelPoison7.grid_forget()
            labelPoison8.grid_forget()
            
            for widget in content_frame.winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "31:1":
                    widget.grid_forget()
            for widget in content_frame.winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "32:1":
                    widget.grid_forget()
            for widget in content_frame.winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "33:1":
                    widget.grid_forget()
            for widget in content_frame.winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "34:1":
                    widget.grid_forget()
            for widget in content_frame.winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "35:1":
                    widget.grid_forget()
        else:
            for widget in content_frame.winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "31:1":
                    widget.grid(row=31, column=1)
            for widget in content_frame.winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "32:1":
                    widget.grid(row=32, column=1)
            for widget in content_frame.winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "33:1":
                    widget.grid(row=33, column=1)
            for widget in content_frame.winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "34:1":
                    widget.grid(row=34, column=1)
            for widget in content_frame.winfo_children():
                if isinstance(widget, ctk.CTkLabel) and widget.cget("text") == "35:1":
                    widget.grid(row=35, column=1)

            # Mystery Capsule
            labelMystery1.grid(row=35, column=2)
            labelMystery2.grid(row=35, column=4)
            labelMystery3.grid(row=35, column=6)
            labelMystery4.grid(row=35, column=8)
            labelMystery5.grid(row=35, column=10)
            labelMystery6.grid(row=35, column=12)
            labelMystery7.grid(row=35, column=14)
            labelMystery8.grid(row=35, column=16)

            # Orb Bag Capsule
            labelOrbBag1.grid(row=34, column=2)
            labelOrbBag2.grid(row=34, column=4)
            labelOrbBag3.grid(row=34, column=6)
            labelOrbBag4.grid(row=34, column=8)
            labelOrbBag5.grid(row=34, column=10)
            labelOrbBag6.grid(row=34, column=12)
            labelOrbBag7.grid(row=34, column=14)
            labelOrbBag8.grid(row=34, column=16)

            # DK Capsule
            labelDK1.grid(row=33, column=2)
            labelDK2.grid(row=33, column=4)
            labelDK3.grid(row=33, column=6)
            labelDK4.grid(row=33, column=8)
            labelDK5.grid(row=33, column=10)
            labelDK6.grid(row=33, column=12)
            labelDK7.grid(row=33, column=14)
            labelDK8.grid(row=33, column=16)

            # Duel Capsule
            labelDuel1.grid(row=32, column=2)
            labelDuel2.grid(row=32, column=4)
            labelDuel3.grid(row=32, column=6)
            labelDuel4.grid(row=32, column=8)
            labelDuel5.grid(row=32, column=10)
            labelDuel6.grid(row=32, column=12)
            labelDuel7.grid(row=32, column=14)
            labelDuel8.grid(row=32, column=16)

            # Poison Mushroom
            labelPoison1.grid(row=31, column=2)
            labelPoison2.grid(row=31, column=4)
            labelPoison3.grid(row=31, column=6)
            labelPoison4.grid(row=31, column=8)
            labelPoison5.grid(row=31, column=10)
            labelPoison6.grid(row=31, column=12)
            labelPoison7.grid(row=31, column=14)
            labelPoison8.grid(row=31, column=16)

            # Prices and Odds for the last five items
            mysteryCapsulePrice1.grid(row=35, column=3)
            mysteryCapsulePrice2.grid(row=35, column=5)
            mysteryCapsulePrice34.grid(row=35, column=7)
            mysteryCapsuleShopOdds12.grid(row=35, column=9)
            mysteryCapsuleShopOdds34.grid(row=35, column=11)
            mysteryCapsuleSpaceOdds1.grid(row=35, column=13)
            mysteryCapsuleSpaceOdds2.grid(row=35, column=15)
            mysteryCapsuleSpaceOdds34.grid(row=35, column=17)

            dkCapsulePrice1.grid(row=34, column=3)
            dkCapsulePrice2.grid(row=34, column=5)
            dkCapsulePrice34.grid(row=34, column=7)
            dkCapsuleShopOdds12.grid(row=34, column=9)
            dkCapsuleShopOdds34.grid(row=34, column=11)
            dkCapsuleSpaceOdds1.grid(row=34, column=13)
            dkCapsuleSpaceOdds2.grid(row=34, column=15)
            dkCapsuleSpaceOdds34.grid(row=34, column=17)

            orbBagCapsulePrice1.grid(row=33, column=3)
            orbBagCapsulePrice2.grid(row=33, column=5)
            orbBagCapsulePrice34.grid(row=33, column=7)
            orbBagCapsuleShopOdds12.grid(row=33, column=9)
            orbBagCapsuleShopOdds34.grid(row=33, column=11)
            orbBagCapsuleSpaceOdds1.grid(row=33, column=13)
            orbBagCapsuleSpaceOdds2.grid(row=33, column=15)
            orbBagCapsuleSpaceOdds34.grid(row=33, column=17)

            poisonMushroomPrice1.grid(row=32, column=3)
            poisonMushroomPrice2.grid(row=32, column=5)
            poisonMushroomPrice34.grid(row=32, column=7)
            poisonMushroomShopOdds12.grid(row=32, column=9)
            poisonMushroomShopOdds34.grid(row=32, column=11)
            poisonMushroomSpaceOdds1.grid(row=32, column=13)
            poisonMushroomSpaceOdds2.grid(row=32, column=15)
            poisonMushroomSpaceOdds34.grid(row=32, column=17)

            duelCapsulePrice1.grid(row=31, column=3)
            duelCapsulePrice2.grid(row=31, column=5)
            duelCapsulePrice34.grid(row=31, column=7)
            duelCapsuleShopOdds12.grid(row=31, column=9)
            duelCapsuleShopOdds34.grid(row=31, column=11)
            duelCapsuleSpaceOdds1.grid(row=31, column=13)
            duelCapsuleSpaceOdds2.grid(row=31, column=15)
            duelCapsuleSpaceOdds34.grid(row=31, column=17)

    hideCustomSwitch.configure(command=toggle_hide_custom)
    toggle_hide_custom()

    #def fillViaCode7Actions():
    #    top = ctk.CTkToplevel(height=500, width=500)
    #    top.attributes('-topmost', True)
    #    top.title("Enter Code")
    #    
    #    enterCodeLabel = ctk.CTkLabel(master=top, text="Enter Code")
    #    enterCodeLabel.place(x=10, y=10)
    #    
    #    codeText = ctk.CTkTextbox(master=top, width=200, height=400)
    #    codeText.place(x=10, y=65)
    #    submitButton = ctk.CTkButton(master=top, command=lambda: fillViaCode7(hide_custom, top, codeText, mushroomCapsuleWeight7, goldenMushroomCapsulePrice7, goldenMushroomCapsuleWeight7, slowMushroomCapsulePrice7, slowMushroomCapsuleWeight7, metalMushroomCapsulePrice7, metalMushroomCapsuleWeight7, flutterCapsulePrice7, flutterCapsuleWeight7, cannonCapsulePrice7, cannonCapsuleWeight7, snackCapsulePrice7, snackCapsuleWeight7, lakituCapsulePrice7, lakituCapsuleWeight7, hammerBroCapsulePrice7, hammerBroCapsuleWeight7, plantCapsulePrice7, plantCapsuleWeight7, spearCapsulePrice7, spearCapsuleWeight7, kamekCapsulePrice7, kamekCapsuleWeight7, toadyCapsulePrice7, toadyCapsuleWeight7, blizzardCapsulePrice7, blizzardCapsuleWeight7, banditCapsulePrice7, banditCapsuleWeight7, pinkBooCapsulePrice7, pinkBooCapsuleWeight7, spinyCapsulePrice7, spinyCapsuleWeight7, zapCapsulePrice7, zapCapsuleWeight7, tweesterCapsulePrice7, tweesterCapsuleWeight7, thwompCapsulePrice7, thwompCapsuleWeight7, warpCapsulePrice7, warpCapsuleWeight7, bombCapsulePrice7, bombCapsuleWeight7, fireballCapsulePrice7, fireballCapsuleWeight7, flowerCapsulePrice7, flowerCapsuleWeight7, eggCapsulePrice7, eggCapsuleWeight7, vacuumCapsulePrice7, vacuumCapsuleWeight7, magicCapsulePrice7, magicCapsuleWeight7, tripleCapsulePrice7, tripleCapsuleWeight7, koopaCapsulePrice7, koopaCapsuleWeight7, dkCapsulePrice7 if hide_custom == False else "0", dkCapsuleWeight7 if hide_custom == False else "0", poisonMushroomPrice7 if hide_custom == False else "0", poisonMushroomWeight7 if hide_custom == False else "0", duelCapsulePrice7 if hide_custom == False else "0", duelCapsuleWeight7 if hide_custom == False else "0", mysteryCapsulePrice7 if hide_custom == False else "0", mysteryCapsuleWeight7 if hide_custom == False else "0", orbBagCapsulePrice7 if hide_custom == False else "0", orbBagCapsuleWeight7 if hide_custom == False else "0"), text="Submit")
    #    submitButton.place(x=250, y=425)

    spaces7 = ["None", "Invisible Space", "Blue Space", "Red Space", "Happening Space", "Bowser Space", "Duel Space", "DK Space", "Orb Space A", "Orb Space B", "Mic Space"]
    
    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" Replace  ", font=("Arial", 16))
    label.grid(row=0, column=0)

    spaceRep411 = ctk.CTkComboBox(master=tabview.tab("Space Replacement"), values=spaces7)
    spaceRep411.grid(row=0, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" with ", font=("Arial", 16))
    label.grid(row=0, column=2)

    spaceRep421 = ctk.CTkComboBox(master=tabview.tab("Space Replacement"), values=spaces7)
    spaceRep421.grid(row=0, column=3)

    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" (Slot A) ", font=("Arial", 16))
    label.grid(row=0, column=4)

    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" Replace  ", font=("Arial", 16))
    label.grid(row=1, column=0)

    spaceRep412 = ctk.CTkComboBox(master=tabview.tab("Space Replacement"), values=spaces7)
    spaceRep412.grid(row=1, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" with ", font=("Arial", 16))
    label.grid(row=1, column=2)

    spaceRep422 = ctk.CTkComboBox(master=tabview.tab("Space Replacement"), values=spaces7)
    spaceRep422.grid(row=1, column=3)

    label = ctk.CTkLabel(master=tabview.tab("Space Replacement"), text=" (Slot B) ", font=("Arial", 16))
    label.grid(row=1, column=4)

    parseButton = ctk.CTkButton(master=tabview.tab("Space Replacement"), command=lambda: spaceReplaceEvent_mp7(spaceRep411, spaceRep421, spaceRep412, spaceRep422, spaces7), text="Generate Codes")
    parseButton.place(x=10, y=800)

    items7 = ["None", "Mushroom", "Super Mushroom", "Slow 'Shroom", "Metal Mushroom", "Flutter", "Cannon", "Snack", "Lakitu", "Hammer Bro", "Piranha Plant", "Spear Guy", "Kamek", "Toady", "Mr. Blizzard", "Bandit", "Pink Boo", "Spiny", "Zap", "Tweester", "Thwomp", "Warp Pipe", "Bob-omb", "Fireball", "Flower", "Egg", "Vacuum", "Surprise", "Triple 'Shroom", "Koopa Kid"]
    
    label = ctk.CTkLabel(master=tabview.tab("Initial Orbs"), text=" Item 1:  ", font=("Arial", 16))
    label.grid(row=0, column=0)

    initalItem71 = ctk.CTkComboBox(master=tabview.tab("Initial Orbs"), values=items7)
    initalItem71.grid(row=0, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Initial Orbs"), text=" Item 2:  ", font=("Arial", 16))
    label.grid(row=1, column=0)
    
    initalItem72 = ctk.CTkComboBox(master=tabview.tab("Initial Orbs"), values=items7)
    initalItem72.grid(row=1, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Initial Orbs"), text=" Item 3:  ", font=("Arial", 16))
    label.grid(row=2, column=0)

    initalItem73 = ctk.CTkComboBox(master=tabview.tab("Initial Orbs"), values=items7)
    initalItem73.grid(row=2, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Initial Orbs"), text=" Item 4:  ", font=("Arial", 16))
    label.grid(row=3, column=0)

    initalItem74 = ctk.CTkComboBox(master=tabview.tab("Initial Orbs"), values=items7)
    initalItem74.grid(row=3, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Initial Orbs"), text=" (Only if Can Hold 5 Capsules in On)  ", font=("Arial", 16))
    label.grid(row=3, column=2, sticky="w")

    label = ctk.CTkLabel(master=tabview.tab("Initial Orbs"), text=" Item 5:  ", font=("Arial", 16))
    label.grid(row=4, column=0)

    initalItem75 = ctk.CTkComboBox(master=tabview.tab("Initial Orbs"), values=items7)
    initalItem75.grid(row=4, column=1)

    label = ctk.CTkLabel(master=tabview.tab("Initial Orbs"), text=" (Only if Can Hold 5 Capsules in On)  ", font=("Arial", 16))
    label.grid(row=4, column=2, sticky="w")

    parseButton = ctk.CTkButton(master=tabview.tab("Initial Orbs"), command=lambda: initialItemsEvent_mp7(initalItem71, initalItem72, initalItem73, initalItem74, initalItem75, items7), text="Generate Codes")
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

    parse_stars_button = ctk.CTkButton(master=tabview.tab("Star Handicaps"), command=lambda: handicapEvent_mp7(p1Stars, p2Stars, p3Stars, p4Stars), text="Generate Codes")
    parse_stars_button.place(x=10, y=800)

    spinx_list = ["Do Nothing", "Blue to Red Spaces", "Half Chomp Price", "Coin Equality"]
    label = ctk.CTkLabel(master=tabview.tab("Board Specific"), text="Pyramid Park - Spinx Event is               ", font=("Arial", 16))
    label.grid(row=0, column=0, pady=10)
    comboSpinx = ctk.CTkComboBox(master=tabview.tab("Board Specific"), values=spinx_list)
    comboSpinx.grid(row=0, column=1)
    spinx_button = ctk.CTkButton(master=tabview.tab("Board Specific"), command=lambda: spinxEvent_mp7(comboSpinx, spinx_list), text="Generate Code")
    spinx_button.place(x=430, y=10)

    label = ctk.CTkLabel(master=tabview.tab("Board Specific"), text=" Pyramid Park - Standard Chomp Costs", font=("Arial", 16))
    label.grid(row=1, column=0, pady=10)
    coinAmount = ctk.CTkEntry(master=tabview.tab("Board Specific"), width=100, font=("Arial", 16, "bold"), placeholder_text="10")
    coinAmount.grid(row=1, column=1)
    chomp_button = ctk.CTkButton(master=tabview.tab("Board Specific"), command=lambda: chompEvent_mp7(coinAmount), text="Generate Code")
    chomp_button.place(x=430, y=57)

    label = ctk.CTkLabel(master=tabview.tab("Board Specific"), text=" Pyramid Park - Red Chomp Costs        ", font=("Arial", 16))
    label.grid(row=2, column=0, pady=10)
    coin2Amount = ctk.CTkEntry(master=tabview.tab("Board Specific"), width=100, font=("Arial", 16, "bold"), placeholder_text="10")
    coin2Amount.grid(row=2, column=1)
    chomp_button = ctk.CTkButton(master=tabview.tab("Board Specific"), command=lambda: redChompEvent_mp7(coin2Amount), text="Generate Code")
    chomp_button.place(x=430, y=104)

    glider_list = ["1 Star (right)", "2 Star (left)", "3 Star (center)"]
    label = ctk.CTkLabel(master=tabview.tab("Board Specific"), text="Windmillville - Flower Glider Goes To  ", font=("Arial", 16))
    label.grid(row=3, column=0, pady=10)
    comboGlider = ctk.CTkComboBox(master=tabview.tab("Board Specific"), values=glider_list)
    comboGlider.grid(row=3, column=1)
    spinx_button = ctk.CTkButton(master=tabview.tab("Board Specific"), command=lambda: gliderEvent_mp7(comboSpinx, spinx_list), text="Generate Code")
    spinx_button.place(x=430, y=152)

    label = ctk.CTkLabel(master=tabview.tab("Board Specific"), text="Windmillville - Flower Glider Costs       ", font=("Arial", 16))
    label.grid(row=4, column=0, pady=10)
    coin3Amount = ctk.CTkEntry(master=tabview.tab("Board Specific"), width=100, font=("Arial", 16, "bold"), placeholder_text="10")
    coin3Amount.grid(row=4, column=1)
    chomp_button = ctk.CTkButton(master=tabview.tab("Board Specific"), command=lambda: gliderCostEvent_mp7(coin3Amount), text="Generate Code")
    chomp_button.place(x=430, y=200)

    label = ctk.CTkLabel(master=tabview.tab("Board Specific"), text="Windmillville - Invest Up Too                 ", font=("Arial", 16))
    label.grid(row=5, column=0, pady=10)
    coin4Amount = ctk.CTkEntry(master=tabview.tab("Board Specific"), width=100, font=("Arial", 16, "bold"), placeholder_text="100")
    coin4Amount.grid(row=5, column=1)
    chomp_button = ctk.CTkButton(master=tabview.tab("Board Specific"), command=lambda: gliderCostEvent_mp7(coin4Amount), text="Generate Code")
    chomp_button.place(x=430, y=252)

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

    parse_stars_button = ctk.CTkButton(master=tabview.tab("Battle Minigame"), command=lambda: battleCoins_mp7(fiveCoins, tenCoins, twentyCoins, thirtyCoins, fiftyCoins), text="Generate Codes")
    parse_stars_button.place(x=10, y=800)

    stars7 = ["None", "Blue Star", "Red Star", "Character Space Star", "Happening Star", "Duel Star", "Mic Star", "Bowser Star", "DK Star", "Minigame Star", "Coin Star", "Star Star", "Orb Star", "Shopping Star", "Running Star"]
    
    label = ctk.CTkLabel(master=tabview.tab("Bonus Star Replacement"), text=" Replace Minigame Star with:  ", font=("Arial", 16))
    label.grid(row=0, column=0, sticky="w")

    star1 = ctk.CTkComboBox(master=tabview.tab("Bonus Star Replacement"), values=stars7)
    star1.grid(row=0, column=1, pady=10)

    label = ctk.CTkLabel(master=tabview.tab("Bonus Star Replacement"), text=" Replace Orb Star with:  ", font=("Arial", 16))
    label.grid(row=1, column=0, sticky="w")

    star2 = ctk.CTkComboBox(master=tabview.tab("Bonus Star Replacement"), values=stars7)
    star2.grid(row=1, column=1, pady=10)

    label = ctk.CTkLabel(master=tabview.tab("Bonus Star Replacement"), text=" Replace Happening Star with:  ", font=("Arial", 16))
    label.grid(row=2, column=0, sticky="w")

    star3 = ctk.CTkComboBox(master=tabview.tab("Bonus Star Replacement"), values=stars7)
    star3.grid(row=2, column=1, pady=10)

    label = ctk.CTkLabel(master=tabview.tab("Bonus Star Replacement"), text=" Replace Red Star with:  ", font=("Arial", 16))
    label.grid(row=3, column=0, sticky="w")

    star4 = ctk.CTkComboBox(master=tabview.tab("Bonus Star Replacement"), values=stars7)
    star4.grid(row=3, column=1, pady=10)

    label = ctk.CTkLabel(master=tabview.tab("Bonus Star Replacement"), text=" Replace Running Star with:  ", font=("Arial", 16))
    label.grid(row=4, column=0, sticky="w")

    star5 = ctk.CTkComboBox(master=tabview.tab("Bonus Star Replacement"), values=stars7)
    star5.grid(row=4, column=1, pady=10)

    label = ctk.CTkLabel(master=tabview.tab("Bonus Star Replacement"), text=" Replace Shopping Star with:  ", font=("Arial", 16))
    label.grid(row=5, column=0, sticky="w")

    star6 = ctk.CTkComboBox(master=tabview.tab("Bonus Star Replacement"), values=stars7)
    star6.grid(row=5, column=1, pady=10)

    parseButton = ctk.CTkButton(master=tabview.tab("Bonus Star Replacement"), command=lambda: customBonusStarEvent_mp7(star1, star2, star3, star4, star5, star6, stars7), text="Generate Codes")
    parseButton.place(x=10, y=800)

    return frame
    