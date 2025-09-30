# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

from codes.marioParty6 import *
from functions import *

import pyperclip

def customBonusStarEvent_mp6(star1, star2, star3, stars6):
    starSlot1 = star1.get()
    starSlot2 = star2.get()
    starSlot3 = star3.get()

    starHex1 = ["NONE", "88830014", "88830015", "88830016", "88830017", "88830018", "88830019", "8883001A", "8883001B", "A883001C", "A883001E", "A8830022", "A8830030", "A8830034"]
    starHex2 = ["NONE", "88C70014", "88C70015", "88C70016", "88C70017", "88C70018", "88C70019", "88C7001A", "88C7001B", "A8C7001C", "A8C7001E", "A8C70022", "A8C70030", "A8C70234"]
    starHex3 = ["NONE", "88040014", "88040015", "88040016", "88040017", "88040018", "88040019", "8804001A", "8804001B", "A804001C", "A804001E", "A8040022", "A8040030", "A8040234"]

    starSlot1Num = stars6.index(starSlot1)
    starSlot1Hex = starHex1[starSlot1Num]

    starSlot2Num = stars6.index(starSlot2)
    starSlot2Hex = starHex2[starSlot2Num]

    starSlot3Num = stars6.index(starSlot3)
    starSlot3Hex = starHex3[starSlot3Num]

    mpStar41 = getStarReplaceSix1(starSlot1Hex, starSlot1)
    mpStar42 = getStarReplaceSix2(starSlot2Hex, starSlot2)
    mpStar43 = getStarReplaceSix3(starSlot3Hex, starSlot3)

    if starSlot1Hex == "NONE":
        mpStar41 = ""
    if starSlot2Hex == "NONE":
        mpStar42 = ""
    if starSlot3Hex == "NONE":
        mpStar43 = ""

    generatedCode = mpStar41 + mpStar42 + mpStar43

    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)

    print("Generated codes copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)
