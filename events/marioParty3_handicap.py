# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (tabitha@tabs.gay)
# Date: 5/16/2024
# License: MIT
# ============================================

from functions import *
from codes.marioParty3 import *

import pyperclip

def handicapEvent_mp3(p1, p2, p3, p4):
    if not p1.get() and not p2.get() and not p3.get() and not p4.get():
        createDialog("Error", "error", "Please fill out atleast one box.", None)
        return
    
    p1Handicap = hex(int(p1.get()))[2:].zfill(4).upper()
    p2Handicap = hex(int(p2.get()))[2:].zfill(4).upper()
    p3Handicap = hex(int(p3.get()))[2:].zfill(4).upper()
    p4Handicap = hex(int(p4.get()))[2:].zfill(4).upper()

    # Generate codes for blue and red spaces
    marioPartyThreeHandicap = getStarHandicap(p1Handicap, p2Handicap, p3Handicap, p4Handicap)

    # Replace placeholder in generated codes
    generatedCode = (marioPartyThreeHandicap).strip()

    # Copy generated codes to clipboard
    pyperclip.copy(generatedCode)

    # Notify user about successful operation
    print("Generated codes copied to the clipboard.")
    createDialog("Operation Successful", "success", "Generated codes copied to clipboard!", None)