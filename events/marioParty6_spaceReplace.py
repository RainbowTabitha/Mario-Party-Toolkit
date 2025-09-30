# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (tabitha@tabs.gay)
# Date: 5/12/2024
# License: MIT
# ============================================

from codes.marioParty6 import *
from functions import *

import pyperclip

def spaceReplaceEvent_mp6(spaceReplace411, spaceReplace421, spaceRep412, spaceRep422, spaces6):
    spaceSlot1 = spaceReplace411.get()
    spaceSlot2 = spaceRep412.get()

    spaceSlot3 = spaceReplace421.get()
    spaceSlot4 = spaceRep422.get()

    spaceHex = ["NONE", "00", "01", "02", "03", "04", "05", "06", "08"]

    spaceSlot1Num = spaces6.index(spaceSlot1)
    spaceSlot1Hex = spaceHex[spaceSlot1Num]

    spaceSlot2Num = spaces6.index(spaceSlot2)
    spaceSlot2Hex = spaceHex[spaceSlot2Num]

    spaceSlot3Num = spaces6.index(spaceSlot3)
    spaceSlot3Hex = spaceHex[spaceSlot3Num]

    spaceSlot4Num = spaces6.index(spaceSlot4)
    spaceSlot4Hex = spaceHex[spaceSlot4Num]

    mpSpace41 = getSpaceReplaceSix1(spaceSlot1Hex, spaceSlot2Hex, spaceSlot1, spaceSlot2)
    mpSpace42 = getSpaceReplaceSix2(spaceSlot3Hex, spaceSlot4Hex, spaceSlot3, spaceSlot4)
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
