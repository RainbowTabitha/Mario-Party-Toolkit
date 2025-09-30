# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (tabitha@tabs.gay)
# Date: 5/12/2024
# License: MIT
# ============================================

# Import necessary functions and modules
from functions import *
from events.marioPartyDS_mgreplace import *

from CTkToolTip import *

# Import custom tkinter module as ctk
import customtkinter as ctk
from CTkToolTip import *

# Function to create the main interface for Mario Party 1
def create_mario_party_DS_interface(frame):
    # Create a tabbed interface
    tabview = ctk.CTkTabview(frame, width=1110, height=885, fg_color=("#fcfcfc", "#323232"))
    tabview.grid(padx=10, pady=10)
    tabview.add("Minigame Replacement")
    tabview.set("Minigame Replacement")

    # List of minigame names

    minigames_list = ["Goomba Wrangler", "Rail Riders", "Dress for Success", "Camera Shy", "Hedge Honcho", "Study Fall", "Domino Effect", "Cherry-Go-Round", "Trace Cadets", "Soccer Survival", "Hot Shots", "Call of the Goomba", "Pedal Pushers", "Roller Coasters", "Get the Lead Out", "Shortcut Circuit", "Big Blowout", "Trash Landing", "Cheep Cheep Chance", "Whomp-a-thon", "Twist and Route", "Crater Crawl", "Boogie Beam", "Parachutin' Gallery", "Boo Tag", "Dust Buddies", "Cyber Scamper", "Soap Surfers", "Sweet Sleuth", "Tidal Fools", "Raft Riot", "All Geared Up", "Power Washer", "Peek-a-Boo", "Fast Food Frenzy", "Track Star", "Shuffleboard Showdown", "Flash and Dash", "Rubber Ducky Rodeo", "Plush Crush", "Rotisserie Rampage", "Nothing to Luge", "Penny Pinchers", "Gusty Blizzard", "Soil Toil", "Double Vision", "Memory Mash", "Cube Crushers", "Mole Thrill", "Sprinkler Scalers", "Cucumberjacks", "Hanger Management", "Book It!", "Airbrushers", "Toppling Terror", "Crazy Crosshairs", "Shorty Scorers", "Cheep Chump", "Star Catchers", "Short Fuse", "Globe Gunners", "Chips and Dips", "Feed and Seed", "Hammer Chime", "Hexoskeleton", "Book Bash", "Bowser's Block Party", "Mario's Puzzle Party", "Bob-omb Breakers", "Piece Out", "Block Star", "Stick & Spin", "Triangle Twister"]    # Create labels, comboboxes, and button for Minigame Replacement tab
    replace_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" Replace  ", font=("Arial", 16))
    replace_label.grid(row=0, column=0)
    combobox_mingames_1 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_1.grid(row=0, column=1)
    with_label = ctk.CTkLabel(master=tabview.tab("Minigame Replacement"), text=" with ", font=("Arial", 16))
    with_label.grid(row=0, column=2)
    combobox_mingames_2 = ctk.CTkComboBox(master=tabview.tab("Minigame Replacement"), values=minigames_list)
    combobox_mingames_2.grid(row=0, column=3)
    parse_minigame_button = ctk.CTkButton(master=tabview.tab("Minigame Replacement"), command=lambda: mgReplaceEvent_mpDS(combobox_mingames_1, combobox_mingames_2, minigames_list), text="Generate Codes")
    parse_minigame_button.place(x=10, y=800)
    
    return frame
    