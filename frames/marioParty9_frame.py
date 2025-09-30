# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

# Import necessary functions and modules
from functions import *
from events.marioParty9_mgreplace import *

from CTkToolTip import *

# Import custom tkinter module as ctk
import customtkinter as ctk
from CTkToolTip import *

# Function to create the main interface for Mario Party 1
def create_mario_party_9_interface(frame):
    # Create a tabbed interface
    tabview = ctk.CTkTabview(frame, width=1110, height=885, fg_color=("#fcfcfc", "#323232"))
    tabview.grid(padx=10, pady=10)
    tabview.add("Minigame Replacement")
    tabview.set("Minigame Replacement")

    # List of minigame names

    minigames_list = ["Ruins Rumble", "Hazard Hold", "Line in the Sand", "Block and Roll", "Tackle Takedown", "Weird Wheels", "Spike-n-Span", "Hole Hogs", "Pix Fix", "Mob Sleds", "Mecha March", "Bowser Pop", "Double Pounder", "Zoom Room", "Cage Match", "Crossfire Caverns", "Bumper Sparks", "Sand Trap", "Pair of Aces", "Pedal to the Paddle", "Urn It", "Billistics", "Snow Go", "Skyjinks", "Player Conveyor", "Fungi Frenzy", "Jigsaw Jumble", "Twist Ending", "Peak Precision", "Speeding Bullets", "Launch Break", "Polar Extreme", "Logger Heads", "Smash Compactor", "Goomba Bowling", "Pianta Pool", "Bumper Bubbles", "Buddy Bounce", "Pizza Me, Mario", "Chain Event", "Pit or Platter", "Skipping Class", "Flinger Painting", "Goomba Spotting", "Thwomper Room", "Ballistic Beach", "Plunder Ground", "Tumble Temple", "Tuber Tug", "Piranha Patch", "Upward Mobility", "Manor of Escape", "Toad and Go Seek", "Goomba Village", "Growing Up", "Card Smarts", "Bomb Barge", "Ring Leader", "Magma Mayhem", "Don't Look", "Pinball Fall", "Pier Pressure", "10 to Win", "Mecha Choice", "Sock It to Lakitu", "Whomp Stomp", "Deck Dry Bones", "Cheep Cheep Shot", "Spike Strike", "Bowser Jr. Breakdown", "Diddy's Banana Blast", "Wiggler Bounce", "Bombard King Bob-omb", "King Boo's Puzzle Attack", "Blooper Barrage", "Chain Chomp Romp", "Bowser's Block Battle", "DK's Banana Bonus"]    # Create labels, comboboxes, and button for Minigame Replacement tab
    replace_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" Replace  ", font=("Arial", 16))
    replace_label.grid(row=0, column=0)
    combobox_mingames_1 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_1.grid(row=0, column=1)
    with_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" with ", font=("Arial", 16))
    with_label.grid(row=0, column=2)
    combobox_mingames_2 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_2.grid(row=0, column=3)
    parse_minigame_button = ctk.CTkButton(master=tabview.tab("Minigame Replacement"), command=lambda: mgReplaceEvent_mp9(combobox_mingames_1, combobox_mingames_2, minigames_list), text="Generate Codes")
    parse_minigame_button.place(x=10, y=800)
    
    return frame
    