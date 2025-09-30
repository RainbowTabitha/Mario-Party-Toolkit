# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

from codes.marioParty2 import *
from functions import *

import pyperclip

def itemReplace_mp2(spaceRep411, spaceRep412, spaces4):
    spaceSlot1 = spaceRep411.get()
    spaceSlot2 = spaceRep412.get()

    spaceHex = ["FF", "00", "01", "02", "03", "04", "05", "06", "07", "09"]

    spaceSlot1Num = spaces4.index(spaceSlot1)
    spaceSlot1Hex = spaceHex[spaceSlot1Num]

    spaceSlot2Num = spaces4.index(spaceSlot2)
    spaceSlot2Hex = spaceHex[spaceSlot2Num]

    mpSpace41 = getItemReplaceTwo(spaceSlot1Hex, spaceSlot2Hex, spaceSlot1, spaceSlot2)
    
    if spaceSlot1Hex == "NONE":
        mpSpace41 = ""
    if spaceSlot2Hex == "NONE":
        mpSpace41 = ""

    generatedCode = mpSpace41

    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)

    print("Generated codes copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)
