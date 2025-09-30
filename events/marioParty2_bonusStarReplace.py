# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (tabitha@tabs.gay)
# Date: 7/12/2024
# License: MIT
# ============================================

from codes.marioParty2 import *
from functions import *

import pyperclip

def customBonusStarEvent_mp2(star1, star2, star3, stars2):
    starSlot1 = star1.get()
    starSlot2 = star2.get()
    starSlot3 = star3.get()

    starHex = ["NONE", "E8", "EA", "EC", "ED", "EE", "EF", "F0", "F1", "F2", "F3"]

    starSlot1Num = stars2.index(starSlot1)
    starSlot1Hex = starHex[starSlot1Num]

    starSlot2Num = stars2.index(starSlot2)
    starSlot2Hex = starHex[starSlot2Num]

    starSlot3Num = stars2.index(starSlot3)
    starSlot3Hex = starHex[starSlot3Num]

    mpStar21 = getStarReplaceTwo1(starSlot1Hex, starSlot1)
    mpStar22 = getStarReplaceTwo2(starSlot2Hex, starSlot2)
    mpStar23 = getStarReplaceTwo3(starSlot3Hex, starSlot3)

    if starSlot1Hex == "NONE":
        mpStar21 = ""
    if starSlot2Hex == "NONE":
        mpStar22 = ""
    if starSlot3Hex == "NONE":
        mpStar23 = ""

    generatedCode = mpStar21 + mpStar22 + mpStar23

    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)

    print("Generated codes copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)
