# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (tabitha@tabs.gay)
# Date: 5/4/2024
# License: MIT
# ============================================

from functions import *
from codes.marioParty3 import *

import pyperclip

def coinsEvent_mp3(blueAmount, blueTick, redAmount, redTick, starAmount, booCoins, booStars, koopaBankAmount):
    if not blueAmount.get() and not redAmount.get() and not starAmount.get() and not koopaBankAmount.get() and not booStars.get() and not booCoins.get():
        createDialog("Error", "error", "Please fill out atleast one box.", None)
        return
    # Extract blue space information
    blueSpaceAmountBaseThree = blueAmount.get()
    blueSpaceAmountThree = hex(int(blueSpaceAmountBaseThree))[2:].zfill(4).upper() if blueSpaceAmountBaseThree else "DUMMY"
    blueSpaceSwitchThree = "1" if blueTick.get() else "0"

    # Extract red space information
    redSpaceAmountBaseThree = redAmount.get()
    redSpaceAmountThree = hex(int(redSpaceAmountBaseThree))[2:].zfill(4).upper() if redSpaceAmountBaseThree else "DUMMY"
    redSpaceSwitchThree = "1" if redTick.get() else "0"

    # Extract star space information
    starSpaceAmountBaseThree = starAmount.get()
    starSpaceAmountThree = hex(int(starSpaceAmountBaseThree))[2:].zfill(4).upper() if starSpaceAmountBaseThree else "DUMMY"
    negativeStarSpaceAmountBaseThree = -int(starSpaceAmountBaseThree) if starSpaceAmountBaseThree else "DUMMY" 
    starSpaceAmountNegativeThree = format(negativeStarSpaceAmountBaseThree & 0xFFFFFFFFFFFFFFFF, 'X')[12:] if starSpaceAmountBaseThree else "DUMMY"

    # Extract koopa bank information
    koopaBankAmountBaseThree = koopaBankAmount.get()
    koopaBankAmountThree = hex(int(koopaBankAmountBaseThree))[2:].zfill(4).upper() if koopaBankAmountBaseThree else "DUMMY"
    kbAmountNegativeBaseThree = -int(koopaBankAmountBaseThree) if koopaBankAmountBaseThree else "DUMMY"
    kbAmountNegativeBaseThree = format(kbAmountNegativeBaseThree & 0xFFFFFFFFFFFFFFFF, 'X')[12:] if koopaBankAmountBaseThree else "DUMMY"

    # Extract Boo Coins information
    booCoinsAmountBaseThree = booCoins.get()
    booCoinsAmountThree = hex(int(booCoinsAmountBaseThree))[2:].zfill(4).upper() if booCoinsAmountBaseThree else "DUMMY"
    negativeBooCoinsAmountBaseThree = -int(booCoinsAmountBaseThree) if booCoinsAmountBaseThree else "DUMMY" 
    booCoinsAmountNegativeThree = format(negativeBooCoinsAmountBaseThree & 0xFFFFFFFFFFFFFFFF, 'X')[12:] if booCoinsAmountBaseThree else "DUMMY"

    # Extract Boo Stars information
    booStarsAmountBaseThree = booStars.get()
    booStarsAmountThree = hex(int(booStarsAmountBaseThree))[2:].zfill(4).upper() if booStarsAmountBaseThree else "DUMMY"
    negativeBooStarsAmountBaseThree = -int(booStarsAmountBaseThree) if booStarsAmountBaseThree else "DUMMY" 
    booStarsAmountNegativeThree = format(negativeBooStarsAmountBaseThree & 0xFFFFFFFFFFFFFFFF, 'X')[12:] if booStarsAmountBaseThree else "DUMMY"


    # Generate codes for blue and red spaces
    if blueSpaceSwitchThree == "0":
        marioPartyThreeBlueSpace = getBlueSpaceCodeThree(blueSpaceAmountThree, blueSpaceSwitchThree, blueSpaceAmountBaseThree, "Doesn't Double on Last 5") if blueSpaceAmountThree != "DUMMY" else ""
    elif blueSpaceSwitchThree == "1":
        marioPartyThreeBlueSpace = getBlueSpaceCodeThree(blueSpaceAmountThree, blueSpaceSwitchThree, blueSpaceAmountBaseThree, "Doubles on Last 5") if blueSpaceAmountThree != "DUMMY" else ""

    if redSpaceSwitchThree == "0":
        marioPartyThreeRedSpace = getRedSpaceCodeThree(redSpaceAmountThree, redSpaceSwitchThree, redSpaceAmountBaseThree, "Doesn't Double on Last 5") if redSpaceAmountThree != "DUMMY" else ""
    elif redSpaceSwitchThree == "1":
        marioPartyThreeRedSpace = getRedSpaceCodeThree(redSpaceAmountThree, redSpaceSwitchThree, redSpaceAmountBaseThree, "Doubles on Last 5") if redSpaceAmountThree != "DUMMY" else ""

    marioPartyThreeStarSpace = getStarSpaceCodeThree(starSpaceAmountThree, starSpaceAmountNegativeThree, starSpaceAmountBaseThree) if starSpaceAmountThree != "DUMMY" else ""
    marioPartyThreeKoopaBank = getKoopaBankCodeThree(koopaBankAmountThree, kbAmountNegativeBaseThree, koopaBankAmountBaseThree) if koopaBankAmountThree != "DUMMY" else ""
    marioPartyThreeStarBoo = getBooStarPrice(booStarsAmountThree, booStarsAmountNegativeThree, booStarsAmountBaseThree) if booStarsAmountThree != "DUMMY" else ""
    marioPartyThreeCoinBoo = getBooCoinsPrice(booCoinsAmountThree, booCoinsAmountNegativeThree, booCoinsAmountBaseThree) if booCoinsAmountThree != "DUMMY" else ""

    # Replace placeholder in generated codes
    generatedCode = (marioPartyThreeBlueSpace + marioPartyThreeRedSpace + marioPartyThreeStarSpace + marioPartyThreeKoopaBank + marioPartyThreeCoinBoo + marioPartyThreeStarBoo).strip()

    # Copy generated codes to clipboard
    pyperclip.copy(generatedCode)

    # Notify user about successful operation
    print("Generated codes copied to the clipboard.")
    createDialog("Operation Successful", "success", "Generated codes copied to clipboard!", None)