# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

from functions import *
from codes.marioParty4 import *
import pyperclip

def coinsEvent_mp4(blueEntry, redEntry, mgEntry, starEntry, megaEntry, booStarEntry, booCoinsEntry, lotteryEntry, booCoinsMinimum, bowserEntry, initialEntry):
    if not any((booCoinsMinimum.get(), blueEntry.get(), redEntry.get(), starEntry.get(), mgEntry.get(), megaEntry.get(), booStarEntry.get(), booCoinsEntry.get(), lotteryEntry.get(), bowserEntry.get(), initialEntry.get())):
        createDialog("Error", "error", "Please fill out at least one box.", None)
        return
    
    blueSpaceAmountFour = hex(int(blueEntry.get()))[2:].zfill(4).upper() if blueEntry.get() else "DUMMY"
    redSpaceAmountFour = hex(int(redEntry.get()))[2:].zfill(4).upper() if redEntry.get() else "DUMMY"
    mgSpaceAmountFour = hex(int(mgEntry.get()))[2:].zfill(4).upper() if mgEntry.get() else "DUMMY"
    starSpaceAmountFour = hex(int(starEntry.get()))[2:].zfill(4).upper() if starEntry.get() else "DUMMY"
    lotterySpaceAmountFour = hex(int(lotteryEntry.get()))[2:].zfill(4).upper() if lotteryEntry.get() else "DUMMY"
    booStarSpaceAmountFour = hex(int(booStarEntry.get()))[2:].zfill(4).upper() if booStarEntry.get() else "DUMMY"
    booCoinsSpaceAmountFour = hex(int(booCoinsEntry.get()))[2:].zfill(4).upper() if booCoinsEntry.get() else "DUMMY"
    megaAmountFour = hex(int(megaEntry.get()))[2:].zfill(4).upper() if megaEntry.get() else "DUMMY"
    booMinimumFour = hex(int(booCoinsMinimum.get()) + 5)[2:].zfill(4).upper() if booCoinsMinimum.get() else "DUMMY"
    bowserAmountFour = hex(int(bowserEntry.get()))[2:].zfill(4).upper() if bowserEntry.get() else "DUMMY"
    initialCoinsAmountFour = hex(int(initialEntry.get()))[2:].zfill(4).upper() if initialEntry.get() else "DUMMY"

    marioPartyFourBlueSpace = getBlueSpaceCodeFour(blueSpaceAmountFour, blueEntry.get()) if blueSpaceAmountFour != "DUMMY" else ""
    marioPartyFourRedSpace = getRedSpaceCodeFour(redSpaceAmountFour, redEntry.get()) if redSpaceAmountFour != "DUMMY" else ""
    marioPartyFourStarSpace = getStarSpaceCodeFour(starSpaceAmountFour, starEntry.get()) if starSpaceAmountFour != "DUMMY" else ""
    marioPartyFourLotterySpace = getLotterySpaceCodeFour(lotterySpaceAmountFour, lotteryEntry.get()) if lotterySpaceAmountFour != "DUMMY" else ""
    marioPartyFourMGSpace = getMinigameCodeFour(mgSpaceAmountFour, mgEntry.get()) if mgSpaceAmountFour != "DUMMY" else ""
    marioPartyFourBooStar = getBooSpaceStarFour(booStarSpaceAmountFour, booStarEntry.get()) if booStarSpaceAmountFour != "DUMMY" else ""
    marioPartyFourBooCoins = getBooSpaceCoinsFour(booCoinsSpaceAmountFour, booCoinsEntry.get()) if booCoinsSpaceAmountFour != "DUMMY" else ""
    marioPartyFourSquish = getSquishCodeFour(megaAmountFour, megaEntry.get()) if megaAmountFour != "DUMMY" else ""
    marioPartyFourBooMinimumCoins = getBooHouseMinimum(booMinimumFour, booCoinsMinimum.get()) if booMinimumFour != "DUMMY" else ""
    marioPartyFourBowser = getBowserSuitCodeFour(bowserAmountFour, bowserEntry.get()) if bowserAmountFour != "DUMMY" else ""
    marioPartyFourInitialCoins = initialCoinsMod4(initialCoinsAmountFour, initialEntry.get()) if initialCoinsAmountFour != "DUMMY" else ""

    generatedCode = (marioPartyFourBlueSpace + marioPartyFourRedSpace + marioPartyFourInitialCoins + marioPartyFourMGSpace + marioPartyFourStarSpace + marioPartyFourSquish + marioPartyFourBowser + marioPartyFourBooStar + marioPartyFourBooCoins + marioPartyFourBooMinimumCoins +  marioPartyFourLotterySpace).strip()

    pyperclip.copy(generatedCode)

    print("Generated codes copied to the clipboard.")
    createDialog("Operation Successful", "success", "Generated codes copied to clipboard!", None)