# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (tabitha@tabs.gay)
# Date: 5/12/2024
# License: MIT
# ============================================

# Import necessary functions and modules
from functions import *
from events.marioParty8_coins import *
from events.marioParty8_items import *
from events.marioParty8_mgreplace import *

from CTkToolTip import *

# Import custom tkinter module as ctk
import customtkinter as ctk
from CTkToolTip import *

# Function to create the main interface for Mario Party 1
def create_mario_party_8_interface(frame):
    # Create a tabbed interface
    tabview = ctk.CTkTabview(frame, width=1110, height=885, fg_color=("#fcfcfc", "#323232"))
    tabview.grid(padx=10, pady=10)
    tabview.add("Coins Mods")
    tabview.add("Minigame Replacement")
    tabview.add("Candy Mods [BETA]")
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
    mgWin_entryTT = CTkToolTip(mgWin_entry, message="Some minigames may be broken. Please report if so.")

    star_entry = create_entry(tabview.tab("Coins Mods"), 4, "assets/eventTags/starSpace.png", " Costs ", " Coins to buy a Star.")
    star_entryTT = CTkToolTip(mgWin_entry, message="Works on DK's, Goomba's, King Boo's and Shy Guy's.")

    bitsize_entry = create_entry(tabview.tab("Coins Mods"), 5, "assets/eventTags/bitsizeCandy.png", " Gain ", " Coins when Bitsized.")
    bowlo_entry = create_entry(tabview.tab("Coins Mods"), 6, "assets/eventTags/bowloCandy.png", " Lose ", " Coins when Bowloed.")
    vampire_entry = create_entry(tabview.tab("Coins Mods"), 7, "assets/eventTags/vampireCandy.png", " Steal ", " Coins via Vampire despite Roulette.")

    hotel_entry = create_entry(tabview.tab("Coins Mods"), 8, "assets/eventTags/hotel.png", " Max ", " coins.")
    hotel_entryTooltip = CTkToolTip(hotel_entry, message="Max Coin Value is 255")

    # Create button to generate coins modification codes
    parse_coins_button = ctk.CTkButton(master=tabview.tab("Coins Mods"), command=lambda: coinsEvent_mp8(blue_entry, red_entry, mgWin_entry, star_entry, bitsize_entry, hotel_entry, bowlo_entry, vampire_entry), text="Generate Codes")
    parse_coins_button.place(x=10, y=800)

    # Create entry fields and dropdowns for Candy Mods Tab
    icon = create_image_icon(tabview.tab("Candy Mods [BETA]"), "assets/items/twice.png", 2, 1)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=2, column=2)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" 5  ", font=("Arial", 24, "bold"))
    label.grid(row=2, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" and is ", font=("Arial", 16))
    label.grid(row=2, column=4)
    twiceWeight4 = ctk.CTkEntry(master=tabview.tab("Candy Mods [BETA]"), width=48, font=("Arial", 16, "bold"))
    twiceWeight4.grid(row=2, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" % common.", font=("Arial", 16))
    label.grid(row=2, column=6)

    icon = create_image_icon(tabview.tab("Candy Mods [BETA]"), "assets/items/thrice.png", 3, 1)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=3, column=2)
    thricePrice4 = ctk.CTkEntry(master=tabview.tab("Candy Mods [BETA]"), width=48, font=("Arial", 16, "bold"))
    thricePrice4.grid(row=3, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" and is ", font=("Arial", 16))
    label.grid(row=3, column=4)
    thriceWeight4 = ctk.CTkEntry(master=tabview.tab("Candy Mods [BETA]"), width=48, font=("Arial", 16, "bold"))
    thriceWeight4.grid(row=3, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" % common.", font=("Arial", 16))
    label.grid(row=3, column=6)


    icon = create_image_icon(tabview.tab("Candy Mods [BETA]"), "assets/items/slowgo.png", 4, 1)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=4, column=2)
    slowgoPrice4 = ctk.CTkEntry(master=tabview.tab("Candy Mods [BETA]"), width=48, font=("Arial", 16, "bold"))
    slowgoPrice4.grid(row=4, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" and is ", font=("Arial", 16))
    label.grid(row=4, column=4)
    slowgoWeight4 = ctk.CTkEntry(master=tabview.tab("Candy Mods [BETA]"), width=48, font=("Arial", 16, "bold"))
    slowgoWeight4.grid(row=4, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" % common.", font=("Arial", 16))
    label.grid(row=4, column=6)
    
    icon = create_image_icon(tabview.tab("Candy Mods [BETA]"), "assets/items/springo.png", 5, 1)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=5, column=2)
    springoPrice4 = ctk.CTkEntry(master=tabview.tab("Candy Mods [BETA]"), width=48, font=("Arial", 16, "bold"))
    springoPrice4.grid(row=5, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" and is ", font=("Arial", 16))
    label.grid(row=5, column=4)
    springoWeight4 = ctk.CTkEntry(master=tabview.tab("Candy Mods [BETA]"), width=48, font=("Arial", 16, "bold"))
    springoWeight4.grid(row=5, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" % common.", font=("Arial", 16))
    label.grid(row=5, column=6)
    
    icon = create_image_icon(tabview.tab("Candy Mods [BETA]"), "assets/items/cashzap.png", 6, 1)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=6, column=2)
    cashzapPrice4 = ctk.CTkEntry(master=tabview.tab("Candy Mods [BETA]"), width=48, font=("Arial", 16, "bold"))
    cashzapPrice4.grid(row=6, column=3)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" and is ", font=("Arial", 16))
    label.grid(row=6, column=4)
    cashzapWeight4 = ctk.CTkEntry(master=tabview.tab("Candy Mods [BETA]"), width=48, font=("Arial", 16, "bold"))
    cashzapWeight4.grid(row=6, column=5)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" % common.", font=("Arial", 16))
    label.grid(row=6, column=6)

    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text="", font=("Arial", 16))
    label.grid(row=2, column=7)

    icon = create_image_icon(tabview.tab("Candy Mods [BETA]"), "assets/items/vampire.png", 2, 8)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=2, column=9)
    vampirePrice4 = ctk.CTkEntry(master=tabview.tab("Candy Mods [BETA]"), width=48, font=("Arial", 16, "bold"))
    vampirePrice4.grid(row=2, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" and is ", font=("Arial", 16))
    label.grid(row=2, column=11)
    vampireWeight4 = ctk.CTkEntry(master=tabview.tab("Candy Mods [BETA]"), width=48, font=("Arial", 16, "bold"))
    vampireWeight4.grid(row=2, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" % common.  ", font=("Arial", 16))
    label.grid(row=2, column=13)

    
    icon = create_image_icon(tabview.tab("Candy Mods [BETA]"), "assets/items/bitsize.png", 3, 8)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=3, column=9)
    bitsizePrice4 = ctk.CTkEntry(master=tabview.tab("Candy Mods [BETA]"), width=48, font=("Arial", 16, "bold"))
    bitsizePrice4.grid(row=3, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" and is ", font=("Arial", 16))
    label.grid(row=3, column=11)
    bitsizeWeight4 = ctk.CTkEntry(master=tabview.tab("Candy Mods [BETA]"), width=48, font=("Arial", 16, "bold"))
    bitsizeWeight4.grid(row=3, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" % common.", font=("Arial", 16))
    label.grid(row=3, column=13)

    
    icon = create_image_icon(tabview.tab("Candy Mods [BETA]"), "assets/items/bloway.png", 4, 8)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=4, column=9)
    blowayPrice4 = ctk.CTkEntry(master=tabview.tab("Candy Mods [BETA]"), width=48, font=("Arial", 16, "bold"))
    blowayPrice4.grid(row=4, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" and is ", font=("Arial", 16))
    label.grid(row=4, column=11)
    blowayWeight4 = ctk.CTkEntry(master=tabview.tab("Candy Mods [BETA]"), width=48, font=("Arial", 16, "bold"))
    blowayWeight4.grid(row=4, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" % common.", font=("Arial", 16))
    label.grid(row=4, column=13)

    
    icon = create_image_icon(tabview.tab("Candy Mods [BETA]"), "assets/items/bowlo.png", 5, 8)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=5, column=9)
    bowloPrice4 = ctk.CTkEntry(master=tabview.tab("Candy Mods [BETA]"), width=48, font=("Arial", 16, "bold"))
    bowloPrice4.grid(row=5, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" and is ", font=("Arial", 16))
    label.grid(row=5, column=11)
    bowloWeight4 = ctk.CTkEntry(master=tabview.tab("Candy Mods [BETA]"), width=48, font=("Arial", 16, "bold"))
    bowloWeight4.grid(row=5, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" % common.", font=("Arial", 16))
    label.grid(row=5, column=13)

    
    icon = create_image_icon(tabview.tab("Candy Mods [BETA]"), "assets/items/weeglee.png", 6, 8)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=6, column=9)
    weegleePrice4 = ctk.CTkEntry(master=tabview.tab("Candy Mods [BETA]"), width=48, font=("Arial", 16, "bold"))
    weegleePrice4.grid(row=6, column=10)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" and is ", font=("Arial", 16))
    label.grid(row=6, column=11)
    weegleeWeight4 = ctk.CTkEntry(master=tabview.tab("Candy Mods [BETA]"), width=48, font=("Arial", 16, "bold"))
    weegleeWeight4.grid(row=6, column=12)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" % common.", font=("Arial", 16))
    label.grid(row=6, column=13)

    
    icon = create_image_icon(tabview.tab("Candy Mods [BETA]"), "assets/items/thwompCandy.png", 2, 15)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=2, column=16)
    thwompPrice4 = ctk.CTkEntry(master=tabview.tab("Candy Mods [BETA]"), width=48, font=("Arial", 16, "bold"))
    thwompPrice4.grid(row=2, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" and is ", font=("Arial", 16))
    label.grid(row=2, column=18)
    thwompWeight4 = ctk.CTkEntry(master=tabview.tab("Candy Mods [BETA]"), width=48, font=("Arial", 16, "bold"))
    thwompWeight4.grid(row=2, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" % common.", font=("Arial", 16))
    label.grid(row=2, column=20)

    
    icon = create_image_icon(tabview.tab("Candy Mods [BETA]"), "assets/items/bulletCandy.png", 3, 15)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=3, column=16)
    bulletPrice4 = ctk.CTkEntry(master=tabview.tab("Candy Mods [BETA]"), width=48, font=("Arial", 16, "bold"))
    bulletPrice4.grid(row=3, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" and is ", font=("Arial", 16))
    label.grid(row=3, column=18)
    bulletWeight4 = ctk.CTkEntry(master=tabview.tab("Candy Mods [BETA]"), width=48, font=("Arial", 16, "bold"))
    bulletWeight4.grid(row=3, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" % common.", font=("Arial", 16))
    label.grid(row=3, column=20)

    
    icon = create_image_icon(tabview.tab("Candy Mods [BETA]"), "assets/items/bowserCandy.png", 4, 15)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=4, column=16)
    bowserPrice4 = ctk.CTkEntry(master=tabview.tab("Candy Mods [BETA]"), width=48, font=("Arial", 16, "bold"))
    bowserPrice4.grid(row=4, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" and is ", font=("Arial", 16))
    label.grid(row=4, column=18)
    bowserWeight4 = ctk.CTkEntry(master=tabview.tab("Candy Mods [BETA]"), width=48, font=("Arial", 16, "bold"))
    bowserWeight4.grid(row=4, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" % common.", font=("Arial", 16))
    label.grid(row=4, column=20)

    
    icon = create_image_icon(tabview.tab("Candy Mods [BETA]"), "assets/items/duelo.png", 5, 15)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" Costs  ", font=("Arial", 16))
    label.grid(row=5, column=16)
    dueloPrice4 = ctk.CTkEntry(master=tabview.tab("Candy Mods [BETA]"), width=48, font=("Arial", 16, "bold"))
    dueloPrice4.grid(row=5, column=17)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" and is ", font=("Arial", 16))
    label.grid(row=5, column=18)
    dueloWeight4 = ctk.CTkEntry(master=tabview.tab("Candy Mods [BETA]"), width=48, font=("Arial", 16, "bold"))
    dueloWeight4.grid(row=5, column=19)
    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text=" % common.", font=("Arial", 16))
    label.grid(row=5, column=20)

    label = ctk.CTkLabel(master=tabview.tab("Candy Mods [BETA]"), text="Board: ", font=("Arial", 16, "bold"))
    label.place(x=10, y=260)
    boardComboBox = ctk.CTkComboBox(master=tabview.tab("Candy Mods [BETA]"), values=["DK's Treetop Temple", "Shy Guy's Perplex Express"], width=250) # "Goomba's Booty Boardwalk", "King Boo's Haunted Hideaway", "Shy Guy's Perplex Express", "Koopa's Tycoon Town", "Bowser's Warped Orbit"
    boardComboBox.place(x=70, y=260)

    parseButton = ctk.CTkButton(master=tabview.tab("Candy Mods [BETA]"), command=lambda: itemsEvent_mp8(boardComboBox, twiceWeight4, thricePrice4, thriceWeight4, slowgoPrice4, slowgoWeight4, springoPrice4, springoWeight4, cashzapPrice4, cashzapWeight4, vampirePrice4, vampireWeight4, bitsizePrice4, bitsizeWeight4, blowayPrice4, blowayWeight4, bowloPrice4, bowloWeight4, weegleePrice4, weegleeWeight4, thwompPrice4, thwompWeight4, bulletPrice4, bulletWeight4, bowserPrice4, bowserWeight4, dueloPrice4, dueloWeight4), text="Generate Codes")
    parseButton.place(x=10, y=800)

    parseButton = ctk.CTkButton(master=tabview.tab("Candy Mods [BETA]"), command=lambda: savePresetItems8(twiceWeight4, thricePrice4, thriceWeight4, slowgoPrice4, slowgoWeight4, springoPrice4, springoWeight4, cashzapPrice4, cashzapWeight4, vampirePrice4, vampireWeight4, bitsizePrice4, bitsizeWeight4, blowayPrice4, blowayWeight4, bowloPrice4, bowloWeight4, weegleePrice4, weegleeWeight4, thwompPrice4, thwompWeight4, bulletPrice4, bulletWeight4, bowserPrice4, bowserWeight4, dueloPrice4, dueloWeight4), text="Save Preset")
    parseButton.place(x=160, y=800)

    parseButton = ctk.CTkButton(master=tabview.tab("Candy Mods [BETA]"), command=lambda: loadPresetItems8(twiceWeight4, thricePrice4, thriceWeight4, slowgoPrice4, slowgoWeight4, springoPrice4, springoWeight4, cashzapPrice4, cashzapWeight4, vampirePrice4, vampireWeight4, bitsizePrice4, bitsizeWeight4, blowayPrice4, blowayWeight4, bowloPrice4, bowloWeight4, weegleePrice4, weegleeWeight4, thwompPrice4, thwompWeight4, bulletPrice4, bulletWeight4, bowserPrice4, bowserWeight4, dueloPrice4, dueloWeight4), text="Load Preset")
    parseButton.place(x=310, y=800)

    # List of minigame names
    minigames_list = ["Speedy Graffiti", "Swing Kings", "Water Ski Spree", "Punch-a-Bunch", "Crank to Rank", "At the Chomp Wash", "Mosh-Pit Playroom", "Mario Matrix", "Hammer de Pokari", "Grabby Giridion", "Lava or Leave 'Em", "Kartastrophe", "Ribbon Game", "Aim of the Game", "Rudder Madness", "Gun the Runner", "Grabbin' Gold", "Power Trip", "Bob-ombs Away", "Swervin' Skies", "Picture Perfect", "Snow Way Out", "Thrash 'n' Crash", "Chump Rope", "Sick and Twisted", "Bumper Balloons", "Rowed to Victory", "Winner or Dinner", "Paint Misbehavin'", "Sugar Rush", "King of the Thrill", "Shake It Up", "Lean, Mean Ravine", "Boo-ting Gallery", "Crops 'n' Robbers", "In the Nick of Time", "Cut from the Team", "Snipe for the Picking", "Saucer Swarm", "Glacial Meltdown", "Attention Grabber", "Blazing Lassos", "Wing and a Scare", "Lob to Rob", "Pumper Cars", "Cosmic Slalom", "Lava Lobbers", "Loco Motives", "Specter Inspector", "Frozen Assets", "Breakneck Building", "Surf's Way Up", "Bull Riding", "Balancing Act", "Ion the Prize", "You're the Bob-omb", "Scooter Pursuit", "Cardiators", "Rotation Station", "Eyebrawl", "Table Menace", "Flagging Rights", "Trial by Tile", "Star Carnival Bowling", "Puzzle Pillars", "Canyon Cruisers", "Settle It in Court", "Moped Mayhem", "Flip the Chimp", "Pour to Score", "Fruit Picker", "Stampede", "Superstar Showdown", "Alpine Assault", "Treacherous Tightrope"]    # Create labels, comboboxes, and button for Minigame Replacement tab
    replace_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" Replace  ", font=("Arial", 16))
    replace_label.grid(row=0, column=0)
    combobox_mingames_1 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_1.grid(row=0, column=1)
    with_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" with ", font=("Arial", 16))
    with_label.grid(row=0, column=2)
    combobox_mingames_2 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_2.grid(row=0, column=3)
    parse_minigame_button = ctk.CTkButton(master=tabview.tab("Minigame Replacement"), command=lambda: mgReplaceEvent_mp8(combobox_mingames_1, combobox_mingames_2, minigames_list), text="Generate Codes")
    parse_minigame_button.place(x=10, y=800)
    
    return frame
    