# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/4/2024
# License: MIT
# ============================================

from functions import *
from codes.marioParty1 import *

import pyperclip

def coinsEvent_mp1(blueAmount, blueTick, redAmount, redTick, starAmount):
    if not blueAmount.text() and not redAmount.text() and not starAmount.text():
        createDialog("Error", "error", "Please fill out atleast one box.", None)
        return
    
    # Extract blue space information
    blueSpaceAmountBaseOne = blueAmount.text()
    blueSpaceAmountOne = hex(int(blueSpaceAmountBaseOne))[2:].zfill(4).upper() if blueSpaceAmountBaseOne else "DUMMY"
    blueSpaceSwitchOne = "1" if blueTick.isChecked() else "0"

    # Extract red space information
    redSpaceAmountBaseOne = redAmount.text()
    redSpaceAmountOne = hex(int(redSpaceAmountBaseOne))[2:].zfill(4).upper() if redSpaceAmountBaseOne else "DUMMY"
    redSpaceSwitchOne = "1" if redTick.isChecked() else "0"

    # Extract star space information
    starSpaceAmountBaseOne = starAmount.text()
    starSpaceAmountOne = hex(int(starSpaceAmountBaseOne))[2:].zfill(4).upper() if starSpaceAmountBaseOne else "DUMMY"
    negativeStarSpaceAmountBaseOne = -int(starSpaceAmountBaseOne) if starSpaceAmountBaseOne else "DUMMY" 
    starSpaceAmountNegativeOne = format(negativeStarSpaceAmountBaseOne & 0xFFFFFFFFFFFFFFFF, 'X')[12:] if starSpaceAmountBaseOne else "DUMMY"

    # Generate codes for blue and red spaces
    if blueSpaceSwitchOne == "0":
        marioPartyOneBlueSpace = getBlueSpaceCodeOne(blueSpaceAmountOne, blueSpaceSwitchOne, blueSpaceAmountBaseOne, "Doesn't Double on Last 5") if blueSpaceAmountOne != "DUMMY" else ""
    elif blueSpaceSwitchOne == "1":
        marioPartyOneBlueSpace = getBlueSpaceCodeOne(blueSpaceAmountOne, blueSpaceSwitchOne, blueSpaceAmountBaseOne, "Doubles on Last 5") if blueSpaceAmountOne != "DUMMY" else ""

    if redSpaceSwitchOne == "0":
        marioPartyOneRedSpace = getRedSpaceCodeOne(redSpaceAmountOne, redSpaceSwitchOne, redSpaceAmountBaseOne, "Doesn't Double on Last 5") if redSpaceAmountOne != "DUMMY" else ""
    elif redSpaceSwitchOne == "1":
        marioPartyOneRedSpace = getRedSpaceCodeOne(redSpaceAmountOne, redSpaceSwitchOne, redSpaceAmountBaseOne, "Doubles on Last 5") if redSpaceAmountOne != "DUMMY" else ""

    marioPartyOneStarSpace = getStarSpaceCodeOne(starSpaceAmountOne, starSpaceAmountNegativeOne, starSpaceAmountBaseOne) if starSpaceAmountOne != "DUMMY" else ""

    # Replace placeholder in generated codes
    generatedCode = (marioPartyOneBlueSpace + marioPartyOneRedSpace + marioPartyOneStarSpace).strip()

    # Copy generated codes to clipboard
    try:
        pyperclip.copy(generatedCode)
    except Exception as e:
        print(f"Error copying to clipboard: {e}")

    # Notify user about successful operation
    print("Generated codes copied to the clipboard.")
    createDialog("Operation Successful", "success", "Generated codes copied to clipboard!", None)