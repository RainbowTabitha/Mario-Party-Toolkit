#!/usr/bin/env python3
# ============================================
# Minigame Tab Component
# Converted from CTk to PyQt5 for Mario Party Toolkit
# ============================================

from PyQt5.QtWidgets import QWidget, QVBoxLayout, QHBoxLayout, QGroupBox, QSizePolicy, QLabel, QComboBox, QPushButton, QMessageBox, QApplication
from PyQt5.QtCore import Qt
from qfluentwidgets import SubtitleLabel, BodyLabel, ComboBox, PushButton, InfoBar, InfoBarPosition, FluentIcon

# Import minigame replacement functions for all supported games
try:
    from events.marioParty1_mgreplace import mgReplaceEvent_mp1
    from events.marioParty2_mgreplace import mgReplaceEvent_mp2
    from events.marioParty3_mgreplace import mgReplaceEvent_mp3
    from events.marioParty4_mgreplace import mgReplaceEvent_mp4
    from events.marioParty5_mgreplace import mgReplaceEvent_mp5
    from events.marioParty6_mgreplace import mgReplaceEvent_mp6
    from events.marioParty7_mgreplace import mgReplaceEvent_mp7
    from events.marioParty8_mgreplace import mgReplaceEvent_mp8
    from events.marioParty9_mgreplace import mgReplaceEvent_mp9
    from events.marioPartyDS_mgreplace import mgReplaceEvent_mpDS
except ImportError:
    # Handle missing imports gracefully
    pass


class MinigameTab(QWidget):
    def __init__(self, game_id):
        super().__init__()
        self.game_id = game_id
        self.setup_ui()

    def setup_ui(self):
        """Set up the minigame tab UI"""
        self.setObjectName(f"{self.game_id}MinigameTab")
        
        # Main layout
        layout = QVBoxLayout()
        layout.setSpacing(8)
        layout.setContentsMargins(16, 12, 16, 12)
        
        # Title
        title = QLabel("Minigame Replacement")
        title.setStyleSheet("""
            font-size: 24px;
            font-weight: 700;
            color: #E0E0E0;
            margin: 8px 0;
            text-align: center;
        """)
        layout.addWidget(title)
        
        # Description
        desc = BodyLabel("Replace specific minigames with custom selections:")
        desc.setStyleSheet("""
            font-size: 15px;
            color: #E0E0E0;
            margin-bottom: 8px;
            text-align: center;
        """)
        layout.addWidget(desc)
        
        # Minigame Replacement Group
        group = QGroupBox("Minigame Replacement")
        group.setStyleSheet("""
            QGroupBox {
                font-size: 16px;
                font-weight: 600;
                color: palette(text);
                border: 2px solid #3C3C3C;
                border-radius: 8px;
                margin-top: 12px;
                padding-top: 12px;
                background: #2A2A2A;
            }
            QGroupBox::title {
                subcontrol-origin: margin;
                left: 16px;
                padding: 0 8px 0 8px;
                background: #4A90E2;
                color: white;
                border-radius: 6px;
                font-weight: 700;
            }
        """)
        
        group_layout = QVBoxLayout()
        group_layout.setSpacing(12)
        group_layout.setContentsMargins(16, 12, 16, 12)
        group.setLayout(group_layout)
        
        # Minigame selection row
        selection_row = QHBoxLayout()
        selection_row.setSpacing(16)
        
        # "Replace" label
        replace_label = QLabel("Replace")
        replace_label.setStyleSheet("""
            font-size: 18px;
            font-weight: 600;
            color: #E0E0E0;
            min-width: 80px;
        """)
        selection_row.addWidget(replace_label)
        
        # First minigame selection
        self.mg1_combo = ComboBox()
        self.mg1_combo.setFixedWidth(200)
        self.mg1_combo.setStyleSheet("""
            QComboBox {
                font-size: 16px;
                font-weight: 600;
                padding: 8px 12px;
                border: 2px solid #555555;
                border-radius: 6px;
                background: #2A2A2A;
                color: white;
                min-height: 36px;
            }
            QComboBox:hover {
                border: 2px solid #4A90E2;
                background: #333333;
            }
            QComboBox:focus {
                border: 2px solid #4A90E2;
                background: #333333;
            }
            QComboBox::drop-down {
                border: none;
                width: 20px;
            }
            QComboBox::down-arrow {
                image: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIiIGhlaWdodD0iOCIgdmlld0JveD0iMCAwIDEyIDgiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxwYXRoIGQ9Ik0xIDEuNUw2IDYuNUwxMSAxLjUiIHN0cm9rZT0iI0UwRTBFMCIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiLz4KPC9zdmc+);
            }
            QComboBox QAbstractItemView {
                background: #2A2A2A;
                border: 2px solid #4A90E2;
                border-radius: 6px;
                selection-background-color: #4A90E2;
                outline: none;
            }
        """)
        selection_row.addWidget(self.mg1_combo)
        
        # "with" label
        with_label = QLabel("with")
        with_label.setStyleSheet("""
            font-size: 18px;
            font-weight: 600;
            color: #E0E0E0;
            min-width: 60px;
        """)
        selection_row.addWidget(with_label)
        
        # Second minigame selection
        self.mg2_combo = ComboBox()
        self.mg2_combo.setFixedWidth(200)
        self.mg2_combo.setStyleSheet("""
            QComboBox {
                font-size: 16px;
                font-weight: 600;
                padding: 8px 12px;
                border: 2px solid #555555;
                border-radius: 6px;
                background: #2A2A2A;
                color: white;
                min-height: 36px;
            }
            QComboBox:hover {
                border: 2px solid #4A90E2;
                background: #333333;
            }
            QComboBox:focus {
                border: 2px solid #4A90E2;
                background: #333333;
            }
            QComboBox::drop-down {
                border: none;
                width: 20px;
            }
            QComboBox::down-arrow {
                image: url(data:image/svg+xml;base64,PHN2ZyB3aWR0aD0iMTIiIGhlaWdodD0iOCIgdmlld0JveD0iMCAwIDEyIDgiIGZpbGw9Im5vbmUiIHhtbG5zPSJodHRwOi8vd3d3LnczLm9yZy8yMDAwL3N2ZyI+CjxwYXRoIGQ9Ik0xIDEuNUw2IDYuNUwxMSAxLjUiIHN0cm9rZT0iI0UwRTBFMCIgc3Ryb2tlLXdpZHRoPSIyIiBzdHJva2UtbGluZWNhcD0icm91bmQiIHN0cm9rZS1saW5lam9pbj0icm91bmQiLz4KPC9zdmc+);
            }
            QComboBox QAbstractItemView {
                background: #2A2A2A;
                border: 2px solid #4A90E2;
                border-radius: 6px;
                selection-background-color: #4A90E2;
                outline: none;
            }
        """)
        selection_row.addWidget(self.mg2_combo)
        
        selection_row.addStretch()
        group_layout.addLayout(selection_row)
        
        # Populate minigame lists based on game
        self.populate_minigame_lists()
        
        layout.addWidget(group)
        
        # Generate button
        # Generate button with reduced margins
        generate_btn = QPushButton("Generate Codes")
        generate_btn.setStyleSheet("""
            QPushButton {
                background: #4A90E2;
                color: white;
                border: none;
                border-radius: 8px;
                padding: 12px 24px;  /* Reduced from 16px 32px */
                font-size: 15px;  /* Reduced from 16px */
                font-weight: 700;
                margin: 8px 0;  /* Reduced from 16px */
                min-height: 44px;  /* Reduced from 52px */
            }
            QPushButton:hover {
                background: #5BA0F2;
            }
            QPushButton:pressed {
                background: #357ABD;
            }
        """)
        generate_btn.clicked.connect(self.generate_codes)
        layout.addWidget(generate_btn)
        
        # Add stretch to push everything up
        layout.addStretch()
        
        self.setLayout(layout)
    
    def populate_minigame_lists(self):
        """Populate minigame lists based on the current game"""
        if self.game_id == "marioParty1":
            minigames_list = [
                "Memory Match", "Slot Machine", "Buried Treasure", "Treasure Divers", 
                "Shell Game", "Slot Car Derby 1", "Hot Bob-omb", "Slot Car Derby 2", 
                "Pipe Maze", "Ghost Guess", "Musical Mushroom", "Pedal Power", 
                "Crazy Cutter", "Face Lift", "Whack-a-Plant", "Bash 'n' Cash", 
                "Bowl Over", "Ground Pound", "Balloon Burst", "Coin Block Blitz", 
                "Coin Block Bash", "Skateboard Scamper", "Box Mountain Mayhem", 
                "Platform Peril", "Teetering Towers", "Mushroom Mix-Up", 
                "Bumper Ball Maze 1", "Grab Bag", "Bobsled Run", "Bumper Balls", 
                "TightRope Treachery", "Knock Block Tower", "Tipsy Tourney", 
                "Bombs Away", "Crane Game", "Bumper Ball Maze 2", "Mario Bandstand", 
                "Desert Dash", "Shy Guy Says", "Limbo Dance", "Bombsketball", 
                "Cast Aways", "Key-pa-Way", "Running of the Bulb", "Hot Rope Jump", 
                "Handcar Havoc", "Deep Sea Divers", "Piranha's Pursuit", "Tug o' War", 
                "Paddle Battle", "Bumper Ball Maze 3", "Coin Shower Flower", "Hammer Drop"
            ]
        elif self.game_id == "marioParty2":
            minigames_list = [
                "BOWSER Slots", "Roll Out the Barrels", "Coffin Congestion", "Hammer Slammer",
                "Give Me a Brake!", "Mallet-Go Round", "Grab Bag", "Bumper Balloon Cars",
                "Rakin' 'em In", "Day at the Races", "Face Lift", "Crazy Cutters",
                "Hot BOB-OMB", "Bowl Over", "Rainbow Run", "Crane Game", "Move to the Music",
                "BOB-OMB Barrage", "Look Away", "Shock Drop or Roll", "Lights Out",
                "Filet Relay", "Archer-ival", "TOAD Bandstand", "Bobsled Run",
                "Handcar Havoc", "Balloon Burst", "Sky Pilots", "Speed Hockey",
                "Cake Factory", "Dungeon Dash", "Magnet Carta", "Lava Tile Isle",
                "Hot Rope Jump", "Shell Shocked", "TOAD in the Box", "Mecha-Marathon",
                "Roll Call", "Abandon Ship", "Platform Peril", "Totem Pole Pound",
                "Bumper Balls", "Bombs Away", "Tipsy Tourney", "Honeycomb Havoc",
                "Hexagon Heat", "Skateboard Scamper", "Slot Car Derby", "Shy Guy Says",
                "Sneak 'n' Snore", "Driver's Ed", "BOWSER's Big Blast", "Looney Lumberjacks",
                "Torpedo Targets", "Destruction Duet", "Dizzy Dancing", "Tile Driver",
                "Quicksand Cache", "Deep Sea Salvage"
            ]
        elif self.game_id == "marioParty3":
            minigames_list = [
                "Thwomp Pull", "River Raiders", "Tidal Toss", "Eatsa Pizza",
                "Baby Bowser Broadside", "Pump, Pump and Away", "Hyper Hydrants",
                "Picking Panic", "Treadmill Grill", "Toadstoll Titan", "Aces High",
                "Bounce 'n' Trounce", "Ice Rink Risk", "Locked Out", "Chip Shot Challenge",
                "Parasol Plummet", "Messy Memory", "Picture Imperfect", "Mario's Puzzle Party",
                "The Beat Goes On", "M. P. I. Q.", "Curtain Call", "Water Whirled",
                "Frigid Bridges", "Awful Tower", "Cheep Cheep Chase", "Pipe Cleaners",
                "Snowball Summit", "All Fired Up", "Stacked Deck", "Three Door Monty",
                "Rockin' Raceway", "Merry-Go-Chomp", "Slap Down", "Storm Chasers",
                "Eye Sore", "Vine With Me", "Popgun Pick-Off", "End of the Line",
                "Bowser Toss", "Baby Bowser Bonkers", "Motor Rooter", "Silly Screws",
                "Crowd Cover", "Tick Tock Hop", "Fowl Play", "Mecha-Marathon",
                "Hey, Batter, Batter!", "Bobbing Bow-loons", "Dorrie Dip",
                "Swinging with Sharks", "Swing 'n' Swipe", "Stardust Battle",
                "Game Guy's Roulette", "Game Guy's Lucky 7", "Game Guy's Magic Boxes",
                "Game Guy's Sweet Surprise", "Dizzy Dinghies", "Mario's Puzzle Party Pro"
            ]
        elif self.game_id == "marioParty4":
            minigames_list = [
                "Manta Rings", "Slime Time", "Booksquirm", "Trace Race", "Mario Medley",
                "Avalanche!", "Domination", "Paratrooper Plunge", "Toad's Quick Draw",
                "Three Throw", "Photo Finish", "Mr. Blizzard's Brigade", "Bob-omb Breakers",
                "Long Claw of the Law", "Stamp Out!", "Candlelight Fright", "Makin' Waves",
                "Hide and Go BOOM!", "Tree Stomp", "Fish n' Drips", "Hop or Pop",
                "Money Belts", "GOOOOOOAL!!", "Blame it on the Crane", "The Great Deflate",
                "Revers-a-Bomb", "Right Oar Left?", "Cliffhangers", "Team Treasure Trek",
                "Pair-a-sailing", "Order Up", "Dungeon Duos", "Beach Volley Folley",
                "Cheep Cheep Sweep", "Darts of Doom", "Fruits of Doom", "Balloon of Doom",
                "Chain Chomp Fever", "Paths of Peril", "Bowser's Bigger Blast",
                "Butterfly Blitz", "Barrel Baron", "Mario Speedwagons", "Bowser Bop",
                "Mystic Match 'Em", "Archaeologuess", "Goomba's Chip Flip",
                "Kareening Koopas", "The Final Battle!", "Rumble Fishing",
                "Take a Breather", "Bowser Wrestling", "Panels of Doom"
            ]
        elif self.game_id == "marioParty5":
            minigames_list = [
                "Coney Island", "Ground Pound Down", "Chimp Chase", "Chomp Romp",
                "Pushy Penguins", "Leaf Leap", "Night Light Fright", "Pop-Star Piranhas",
                "Mazed & Confused", "Dinger Derby", "Hydrostars", "Later Skater",
                "Will Flower", "Triple Jump", "Hotel Goomba", "Coin Cache", "Flatiator",
                "Squared Away", "Mario Mechs", "Revolving Fire", "Clock Stoppers",
                "Heat Stroke", "Beam Team", "Vicious Vending", "Big Top Drop",
                "Defuse or Lose", "ID UFO", "Mario Can-Can", "Handy Hoppers",
                "Berry Basket", "Bus Buffer", "Rumble Ready", "Submarathon",
                "Manic Mallets", "Astro-Logical", "Bill Blasters", "Tug-o-Dorrie",
                "Twist 'n' Out", "Lucky Lineup", "Random Ride", "Shock Absorbers",
                "Countdown Pound", "Whomp Maze", "Shy Guy Showdown", "Button Mashers",
                "Get a Rope", "Pump 'n' Jump", "Head Waiter", "Blown Away",
                "Merry Poppings", "Pound Peril", "Piece Out", "Bound of Music",
                "Wind Wavers", "Sky Survivor", "Cage-in Cookin'", "Rain of Fire",
                "Scaldin' Cauldron", "Frightmare", "Flower Shower", "Dodge Bomb",
                "Fish Upon a Star", "Rumble Fumble", "Quilt for Speed",
                "Tube It or Lose It", "Mathletes", "Fight Cards", "Banana Punch",
                "Da Vine Climb", "Mass A-peel", "Panic Pinball", "Banking Coins",
                "Frozen Frenzy", "Curvy Curbs", "Beach Volleyball", "Fish Sticks",
                "Ice Hockey"
            ]
        elif self.game_id == "marioParty6":
            minigames_list = [
                "Catchy Tunes", "Bubble Brawl", "Track & Yield", "Fun Run",
                "Cointagious", "Snow Ride", "Picture This", "Ghost in the Hall",
                "Big Dripper", "Target Tag", "Pokey Pummel", "Take Me Ohm",
                "Kart Wheeled", "Balloon Busters", "Clock Watchers", "Dart Attack",
                "Oil Crisis", "La Bomba", "Spray Anything", "Balloonatic",
                "Spinner Cell", "Think Tank", "Flashfright", "Coin-op Bop",
                "Easy Pickings", "Wheel of Woe", "Boxing Day", "Be My Chum!",
                "StratosFEAR!", "Pogo-a-go-go", "Buzzstormer", "Tile and Error",
                "Battery Ram", "Cardinal Rule", "Ice Moves", "Bumper Crop",
                "Hop-O-Matic 4000", "Wingin' It", "Sphere Factor", "Herbicidal Maniac",
                "Pyramid Scheme", "World Piece", "Warp Pipe Dreams", "Weight for It",
                "Helipopper", "Monty's Revenge", "Deck Hands", "Mad Props",
                "Gimme a Sign", "Bridge Work", "Spin Doctor", "Hip Hop Drop",
                "Air Farce", "The Final Countdown", "Royal Rumpus", "Light Speed",
                "Apes of Wrath", "Fish & Cheeps", "Camp Ukiki", "Funstacle Course!",
                "Funderwall!", "Magmagical Journey!", "Tunnel of Lava!",
                "Treasure Dome!", "Slot-O-Whirl!", "Peel Out", "Bananas Faster",
                "Stump Change", "Jump, Man", "Vine Country", "A Bridge Too Short",
                "Spider Stomp", "Stick and Spin", "Bowser's Lovely Lift!"
            ]
        elif self.game_id == "marioParty7":
            minigames_list = [
                "Catchy Tunes", "Bubble Brawl", "Track & Yield", "Fun Run",
                "Cointagious", "Snow Ride", "Picture This", "Ghost in the Hall",
                "Big Dripper", "Target Tag", "Pokey Pummel", "Take Me Ohm",
                "Kart Wheeled", "Balloon Busters", "Clock Watchers", "Dart Attack",
                "Oil Crisis", "La Bomba", "Spray Anything", "Balloonatic",
                "Spinner Cell", "Think Tank", "Flashfright", "Coin-op Bop",
                "Easy Pickings", "Wheel of Woe", "Boxing Day", "Be My Chum!",
                "StratosFEAR!", "Pogo-a-go-go", "Buzzstormer", "Tile and Error",
                "Battery Ram", "Cardinal Rule", "Ice Moves", "Bumper Crop",
                "Hop-O-Matic 4000", "Wingin' It", "Sphere Factor", "Herbicidal Maniac",
                "Pyramid Scheme", "World Piece", "Warp Pipe Dreams", "Weight for It",
                "Helipopper", "Monty's Revenge", "Deck Hands", "Mad Props",
                "Gimme a Sign", "Bridge Work", "Spin Doctor", "Hip Hop Drop",
                "Air Farce", "The Final Countdown", "Royal Rumpus", "Light Speed",
                "Apes of Wrath", "Fish & Cheeps", "Camp Ukiki", "Funstacle Course!",
                "Funderwall!", "Magmagical Journey!", "Tunnel of Lava!",
                "Treasure Dome!", "Slot-O-Whirl!", "Peel Out", "Bananas Faster",
                "Stump Change", "Jump, Man", "Vine Country", "A Bridge Too Short",
                "Spider Stomp", "Stick and Spin", "Bowser's Lovely Lift!"
            ]
        elif self.game_id == "marioParty8":
            minigames_list = [
                "Speedy Graffiti", "Swing Kings", "Water Ski Spree", "Punch-a-Bunch",
                "Crank to Rank", "At the Chomp Wash", "Mosh-Pit Playroom", "Mario Matrix",
                "Hammer de Pokari", "Grabby Giridion", "Lava or Leave 'Em", "Kartastrophe",
                "Ribbon Game", "Aim of the Game", "Rudder Madness", "Gun the Runner",
                "Grabbin' Gold", "Power Trip", "Bob-ombs Away", "Swervin' Skies",
                "Picture Perfect", "Snow Way Out", "Thrash 'n' Crash", "Chump Rope",
                "Sick and Twisted", "Bumper Balloons", "Rowed to Victory", "Winner or Dinner",
                "Paint Misbehavin'", "Sugar Rush", "King of the Thrill", "Shake It Up",
                "Lean, Mean Ravine", "Boo-ting Gallery", "Crops 'n' Robbers",
                "In the Nick of Time", "Cut from the Team", "Snipe for the Picking",
                "Saucer Swarm", "Glacial Meltdown", "Attention Grabber", "Blazing Lassos",
                "Wing and a Scare", "Lob to Rob", "Pumper Cars", "Cosmic Slalom",
                "Lava Lobbers", "Loco Motives", "Specter Inspector", "Frozen Assets",
                "Breakneck Building", "Surf's Way Up", "Bull Riding", "Balancing Act",
                "Ion the Prize", "You're the Bob-omb", "Scooter Pursuit", "Cardiators",
                "Rotation Station", "Eyebrawl", "Table Menace", "Flagging Rights",
                "Trial by Tile", "Star Carnival Bowling", "Puzzle Pillars",
                "Canyon Cruisers", "Settle It in Court", "Moped Mayhem", "Flip the Chimp",
                "Pour to Score", "Fruit Picker", "Stampede", "Superstar Showdown",
                "Alpine Assault", "Treacherous Tightrope"
            ]
        elif self.game_id == "marioParty9":
            minigames_list = [
                "Ruins Rumble", "Hazard Hold", "Line in the Sand", "Block and Roll",
                "Tackle Takedown", "Weird Wheels", "Spike-n-Span", "Hole Hogs",
                "Pix Fix", "Mob Sleds", "Mecha March", "Bowser Pop", "Double Pounder",
                "Zoom Room", "Cage Match", "Crossfire Caverns", "Bumper Sparks",
                "Sand Trap", "Pair of Aces", "Pedal to the Paddle", "Urn It",
                "Billistics", "Snow Go", "Skyjinks", "Player Conveyor", "Fungi Frenzy",
                "Jigsaw Jumble", "Twist Ending", "Peak Precision", "Speeding Bullets",
                "Launch Break", "Polar Extreme", "Logger Heads", "Smash Compactor",
                "Goomba Bowling", "Pianta Pool", "Bumper Bubbles", "Buddy Bounce",
                "Pizza Me, Mario", "Chain Event", "Pit or Platter", "Skipping Class",
                "Flinger Painting", "Goomba Spotting", "Thwomper Room", "Ballistic Beach",
                "Plunder Ground", "Tumble Temple", "Tuber Tug", "Piranha Patch",
                "Upward Mobility", "Manor of Escape", "Toad and Go Seek", "Goomba Village",
                "Growing Up", "Card Smarts", "Bomb Barge", "Ring Leader", "Magma Mayhem",
                "Don't Look", "Pinball Fall", "Pier Pressure", "10 to Win", "Mecha Choice",
                "Sock It to Lakitu", "Whomp Stomp", "Deck Dry Bones", "Cheep Cheep Shot",
                "Spike Strike", "Bowser Jr. Breakdown", "Diddy's Banana Blast",
                "Wiggler Bounce", "Bombard King Bob-omb", "King Boo's Puzzle Attack",
                "Blooper Barrage", "Chain Chomp Romp", "Bowser's Block Battle",
                "DK's Banana Bonus"
            ]
        elif self.game_id == "marioPartyDS":
            minigames_list = [
                "Goomba Wrangler", "Rail Riders", "Dress for Success", "Camera Shy",
                "Hedge Honcho", "Study Fall", "Domino Effect", "Cherry-Go-Round",
                "Trace Cadets", "Soccer Survival", "Hot Shots", "Call of the Goomba",
                "Pedal Pushers", "Roller Coasters", "Get the Lead Out", "Shortcut Circuit",
                "Big Blowout", "Trash Landing", "Cheep Cheep Chance", "Whomp-a-thon",
                "Twist and Route", "Crater Crawl", "Boogie Beam", "Parachutin' Gallery",
                "Boo Tag", "Dust Buddies", "Cyber Scamper", "Soap Surfers",
                "Sweet Sleuth", "Tidal Fools", "Raft Riot", "All Geared Up",
                "Power Washer", "Peek-a-Boo", "Fast Food Frenzy", "Track Star",
                "Shuffleboard Showdown", "Flash and Dash", "Rubber Ducky Rodeo",
                "Plush Crush", "Rotisserie Rampage", "Nothing to Luge", "Penny Pinchers",
                "Gusty Blizzard", "Soil Toil", "Double Vision", "Memory Mash",
                "Cube Crushers", "Mole Thrill", "Sprinkler Scalers", "Cucumberjacks",
                "Hanger Management", "Book It!", "Airbrushers", "Toppling Terror",
                "Crazy Crosshairs", "Shorty Scorers", "Cheep Chump", "Star Catchers",
                "Short Fuse", "Globe Gunners", "Chips and Dips", "Feed and Seed",
                "Hammer Chime", "Hexoskeleton", "Book Bash", "Bowser's Block Party",
                "Mario's Puzzle Party", "Bob-omb Breakers", "Piece Out", "Block Star",
                "Stick & Spin", "Triangle Twister"
            ]
        else:
            # Default minigame list for unsupported games
            minigames_list = ["Minigame 1", "Minigame 2", "Minigame 3", "Minigame 4"]
        
        # Populate both combo boxes
        self.mg1_combo.addItems(minigames_list)
        self.mg2_combo.addItems(minigames_list)
        
        # Set default selections
        if len(minigames_list) > 0:
            self.mg1_combo.setCurrentText(minigames_list[0])
            if len(minigames_list) > 1:
                self.mg2_combo.setCurrentText(minigames_list[1])
    
    def generate_codes(self):
        """Generate codes for the current game"""
        # Get selected minigames
        minigame1 = self.mg1_combo.currentText()
        minigame2 = self.mg2_combo.currentText()
        
        # Validate selection
        if minigame1 == minigame2:
            main_window = QApplication.instance().activeWindow()
            InfoBar.error(
                title="Invalid Selection",
                content="Please select different minigames for replacement.",
                orient=Qt.Horizontal,
                isClosable=True,
                position=InfoBarPosition.TOP_RIGHT,
                duration=2500,
                parent=main_window
            )
            return
        
        try:
            # Call appropriate minigame replacement function based on game
            if self.game_id == "marioParty1":
                if 'mgReplaceEvent_mp1' in globals():
                    mgReplaceEvent_mp1(self.mg1_combo, self.mg2_combo, 
                                     [self.mg1_combo.itemText(i) for i in range(self.mg1_combo.count())])
                else:
                    self.show_error("Mario Party 1 minigame replacement not available")
            elif self.game_id == "marioParty2":
                if 'mgReplaceEvent_mp2' in globals():
                    mgReplaceEvent_mp2(self.mg1_combo, self.mg2_combo, 
                                     [self.mg1_combo.itemText(i) for i in range(self.mg1_combo.count())])
                else:
                    self.show_error("Mario Party 2 minigame replacement not available")
            elif self.game_id == "marioParty3":
                if 'mgReplaceEvent_mp3' in globals():
                    mgReplaceEvent_mp3(self.mg1_combo, self.mg2_combo, 
                                     [self.mg1_combo.itemText(i) for i in range(self.mg1_combo.count())])
                else:
                    self.show_error("Mario Party 3 minigame replacement not available")
            elif self.game_id == "marioParty4":
                if 'mgReplaceEvent_mp4' in globals():
                    mgReplaceEvent_mp4(self.mg1_combo, self.mg2_combo, 
                                     [self.mg1_combo.itemText(i) for i in range(self.mg1_combo.count())])
                else:
                    self.show_error("Mario Party 4 minigame replacement not available")
            elif self.game_id == "marioParty5":
                if 'mgReplaceEvent_mp5' in globals():
                    mgReplaceEvent_mp5(self.mg1_combo, self.mg2_combo, 
                                     [self.mg1_combo.itemText(i) for i in range(self.mg1_combo.count())])
                else:
                    self.show_error("Mario Party 5 minigame replacement not available")
            elif self.game_id == "marioParty6":
                if 'mgReplaceEvent_mp6' in globals():
                    mgReplaceEvent_mp6(self.mg1_combo, self.mg2_combo, 
                                     [self.mg1_combo.itemText(i) for i in range(self.mg1_combo.count())])
                else:
                    self.show_error("Mario Party 6 minigame replacement not available")
            elif self.game_id == "marioParty7":
                if 'mgReplaceEvent_mp7' in globals():
                    mgReplaceEvent_mp7(self.mg1_combo, self.mg2_combo, 
                                     [self.mg1_combo.itemText(i) for i in range(self.mg1_combo.count())])
                else:
                    self.show_error("Mario Party 7 minigame replacement not available")
            elif self.game_id == "marioParty8":
                if 'mgReplaceEvent_mp8' in globals():
                    mgReplaceEvent_mp8(self.mg1_combo, self.mg2_combo, 
                                     [self.mg1_combo.itemText(i) for i in range(self.mg1_combo.count())])
                else:
                    self.show_error("Mario Party 8 minigame replacement not available")
            elif self.game_id == "marioParty9":
                if 'mgReplaceEvent_mp9' in globals():
                    mgReplaceEvent_mp9(self.mg1_combo, self.mg2_combo, 
                                     [self.mg1_combo.itemText(i) for i in range(self.mg1_combo.count())])
                else:
                    self.show_error("Mario Party 9 minigame replacement not available")
            elif self.game_id == "marioPartyDS":
                if 'mgReplaceEvent_mpDS' in globals():
                    mgReplaceEvent_mpDS(self.mg1_combo, self.mg2_combo, 
                                      [self.mg1_combo.itemText(i) for i in range(self.mg1_combo.count())])
                else:
                    self.show_error("Mario Party DS minigame replacement not available")
            else:
                self.show_error(f"Minigame replacement not supported for {self.game_id}")
                
        except Exception as e:
            self.show_error(f"Error generating codes: {str(e)}")
    
    def show_error(self, message):
        """Show error message to user"""
        QMessageBox.critical(self, "Error", message)
