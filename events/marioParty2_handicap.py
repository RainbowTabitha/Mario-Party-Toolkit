# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

from functions import *
from codes.marioParty2 import *

import pyperclip

def handicapEvent_mp2(p1, p2, p3, p4):
    if not p1.get() and not p2.get() and not p3.get() and not p4.get():
        createDialog("Error", "error", "Please fill out atleast one box.", None)
        return
    
    p1Handicap = hex(int(p1.get()))[2:].zfill(4).upper() if p1.get() else "DUMMY"
    p2Handicap = hex(int(p2.get()))[2:].zfill(4).upper() if p2.get() else "DUMMY"
    p3Handicap = hex(int(p3.get()))[2:].zfill(4).upper() if p3.get() else "DUMMY"
    p4Handicap = hex(int(p4.get()))[2:].zfill(4).upper() if p4.get() else "DUMMY"

    # Generate codes for blue and red spaces
    marioPartyThreeHandicap = getStarHandicapP1(p1Handicap, p2Handicap, p3Handicap, p4Handicap)

    # Replace placeholder in generated codes
    generatedCode = (marioPartyThreeHandicap).strip()

    # Copy generated codes to clipboard
    pyperclip.copy(generatedCode)

    # Notify user about successful operation
    print("Generated codes copied to the clipboard.")
    createDialog("Operation Successful", "success", "Generated codes copied to clipboard!", None)