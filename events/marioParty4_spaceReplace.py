# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

from codes.marioParty4 import *
from functions import *

import pyperclip

def spaceReplaceEvent_mp4(spaceRep411, spaceRep412, spaceRep421, spaceRep422, spaces4):
    spaceSlot1 = spaceRep411.get()
    spaceSlot2 = spaceRep412.get()

    spaceSlot3 = spaceRep421.get()
    spaceSlot4 = spaceRep422.get()

    spaceHex = ["NONE", "00", "01", "02", "03", "04", "05", "06", "07", "09"]

    spaceSlot1Num = spaces4.index(spaceSlot1)
    spaceSlot1Hex = spaceHex[spaceSlot1Num]

    spaceSlot2Num = spaces4.index(spaceSlot2)
    spaceSlot2Hex = spaceHex[spaceSlot2Num]

    spaceSlot3Num = spaces4.index(spaceSlot3)
    spaceSlot3Hex = spaceHex[spaceSlot3Num]

    spaceSlot4Num = spaces4.index(spaceSlot4)
    spaceSlot4Hex = spaceHex[spaceSlot4Num]

    mpSpace41 = getSpaceReplaceFour1(spaceSlot1Hex, spaceSlot2Hex, spaceSlot1, spaceSlot2)
    mpSpace42 = getSpaceReplaceFour2(spaceSlot3Hex, spaceSlot4Hex, spaceSlot3, spaceSlot4)
    if spaceSlot1Hex == "NONE":
        mpSpace41 = ""
    if spaceSlot2Hex == "NONE":
        mpSpace41 = ""
    if spaceSlot3Hex == "NONE":
        mpSpace42 = ""
    if spaceSlot4Hex == "NONE":
        mpSpace42 = ""
    
    generatedCode = mpSpace41 + mpSpace42

    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)

    print("Generated codes copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)
