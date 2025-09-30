# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (tabitha@tabs.gay)
# Date: 7/12/2024
# License: MIT
# ============================================

from codes.marioParty5 import *
from functions import *

import pyperclip

def customBonusStarEvent_mp5(star1, star2, star3, stars5):
    starSlot1 = star1.get()
    starSlot2 = star2.get()
    starSlot3 = star3.get()

    starHex = ["NONE", "881D0014", "881D0015", "881D0016", "881D0017", "881D0018", "881D0019", "A81D0020", "A81D0022", "A81D0026", "A81D0034"]

    starSlot1Num = stars5.index(starSlot1)
    starSlot1Hex = starHex[starSlot1Num]

    starSlot2Num = stars5.index(starSlot2)
    starSlot2Hex = starHex[starSlot2Num]

    starSlot3Num = stars5.index(starSlot3)
    starSlot3Hex = starHex[starSlot3Num]

    mpStar41 = getStarReplaceFive1(starSlot1Hex, starSlot1)
    mpStar42 = getStarReplaceFive2(starSlot2Hex, starSlot2)
    mpStar43 = getStarReplaceFive3(starSlot3Hex, starSlot3)

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
