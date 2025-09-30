# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (tabitha@tabs.gay)
# Date: 9/6/2024
# License: MIT
# ============================================

from codes.marioParty7 import *
from functions import *

import pyperclip

def customBonusStarEvent_mp7(star1, star2, star3, star4, star5, star6, stars7):
    starSlot1 = star1.get()
    starSlot2 = star2.get()
    starSlot3 = star3.get()
    starSlot4 = star4.get()
    starSlot5 = star5.get()
    starSlot6 = star6.get()

    starHex1 = ["NONE", "88A7001C", "88A7001D", "88A7001E", "88A7001F", "88A70023", "88A70021", "88A70020", "88A70024", "A8A70028", "A8A7002C", "88A7003B", "A8A7003C", "A8A7003E", "A8A70018"]
    starHex2 = ["NONE", "88C3001C", "88C3001D", "88C3001E", "88C3001F", "88C30023", "88C30021", "88C30020", "88C30024", "A8C30028", "A8C3002C", "88C3003B", "A8C3003C", "A8C3003E", "A8C30018"]
    starHex3 = ["NONE", "8803001C", "8803001D", "8803001E", "8803001F", "88030023", "88030021", "88030020", "88030024", "A8030028", "A803002C", "8803003B", "A803003C", "A803003E", "A8030018"]
    starHex4 = ["NONE", "8885001C", "8885001D", "8885001E", "8885001F", "88850023", "88850021", "88850020", "88850024", "A8850028", "A885002C", "8885003B", "A885003C", "A885003E", "A8850018"]
    starHex5 = ["NONE", "88C4001C", "88C4001D", "88C4001E", "88C4001F", "88C40023", "88C40021", "88C40020", "88C40024", "A8C40028", "A8C4002C", "88C4003B", "A8C4003C", "A8C4003E", "A8C40018"]
    starHex6 = ["NONE", "8804001C", "8804001D", "8804001E", "8804001F", "88040023", "88040021", "88040020", "88040024", "A8040028", "A804002C", "8804003B", "A804003C", "A804003E", "A8040018"]

    starSlot1Num = stars7.index(starSlot1)
    starSlot1Hex = starHex1[starSlot1Num]

    starSlot2Num = stars7.index(starSlot2)
    starSlot2Hex = starHex2[starSlot2Num]

    starSlot3Num = stars7.index(starSlot3)
    starSlot3Hex = starHex3[starSlot3Num]

    starSlot4Num = stars7.index(starSlot4)
    starSlot4Hex = starHex4[starSlot4Num]

    starSlot5Num = stars7.index(starSlot5)
    starSlot5Hex = starHex5[starSlot5Num]

    starSlot6Num = stars7.index(starSlot6)
    starSlot6Hex = starHex6[starSlot6Num]

    mpStar41 = getStarReplaceSeven1(starSlot1Hex, starSlot1)
    mpStar42 = getStarReplaceSeven2(starSlot2Hex, starSlot2)
    mpStar43 = getStarReplaceSeven3(starSlot3Hex, starSlot3)
    mpStar44 = getStarReplaceSeven4(starSlot4Hex, starSlot4)
    mpStar45 = getStarReplaceSeven5(starSlot5Hex, starSlot5)
    mpStar46 = getStarReplaceSeven6(starSlot6Hex, starSlot6)

    if starSlot1Hex == "NONE":
        mpStar41 = ""
    if starSlot2Hex == "NONE":
        mpStar42 = ""
    if starSlot3Hex == "NONE":
        mpStar43 = ""
    if starSlot4Hex == "NONE":
        mpStar44 = ""
    if starSlot5Hex == "NONE":
        mpStar45 = ""
    if starSlot6Hex == "NONE":
        mpStar46 = ""

    generatedCode = mpStar41 + mpStar42 + mpStar43 + mpStar44 + mpStar45 + mpStar46

    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)

    print("Generated codes copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)
