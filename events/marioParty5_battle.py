# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (tabitha@tabs.gay)
# Date: 5/16/2024
# License: MIT
# ============================================

from functions import *
from codes.marioParty5 import *

import pyperclip

def battleCoins_mp5(p1, p2, p3, p4, p5):
    if not p1.get() and not p2.get() and not p3.get() and not p4.get() and not p5.get():
        createDialog("Error", "error", "Please fill out atleast one box.", None)
        return
    
    p1Handicap = hex(int(p1.get()))[2:].zfill(4).upper() if p1.get() else "0005"
    p2Handicap = hex(int(p2.get()))[2:].zfill(4).upper() if p2.get() else "000A"
    p3Handicap = hex(int(p3.get()))[2:].zfill(4).upper() if p3.get() else "0014"
    p4Handicap = hex(int(p4.get()))[2:].zfill(4).upper() if p4.get() else "001F"
    p5Handicap = hex(int(p5.get()))[2:].zfill(4).upper() if p5.get() else "0032"

    p1String = p1.get() if p1.get() != "" else "5"
    p2String = p2.get() if p2.get() != "" else "10"
    p3String = p3.get() if p3.get() != "" else "20"
    p4String = p4.get() if p4.get() != "" else "30"
    p5String = p5.get() if p5.get() != "" else "50"

    # Generate codes for blue and red spaces
    marioPartyFive = getBattleGame5(p1Handicap, p2Handicap, p3Handicap, p4Handicap, p5Handicap, p1String, p2String, p3String, p4String, p5String)

    # Replace placeholder in generated codes
    generatedCode = (marioPartyFive).strip()

    # Copy generated codes to clipboard
    pyperclip.copy(generatedCode)

    # Notify user about successful operation
    print("Generated codes copied to the clipboard.")
    createDialog("Operation Successful", "success", "Generated codes copied to clipboard!", None)