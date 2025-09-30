# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (tabitha@tabs.gay)
# Date: 5/12/2024
# License: MIT
# ============================================

from functions import *
from codes.marioParty5 import *
import pyperclip
def coinsEvent_mp5(blueEntry, redEntry, mgEntry, starEntry, wigglerEntry, chompStarEntry, chompWeightEntry, koopaEntry, initialEntry):
    if not any((blueEntry.get(), redEntry.get(), starEntry.get(), mgEntry.get(), wigglerEntry.get(), chompWeightEntry.get(), chompStarEntry.get(), koopaEntry.get(), initialEntry.get())):
        createDialog("Error", "error", "Please fill out at least one box.", None)
        return
    
    blueSpaceAmountFive = hex(int(blueEntry.get()))[2:].zfill(4).upper() if blueEntry.get() else "DUMMY"
    redSpaceAmountNegativeFive = format(-int(redEntry.get()) & 0xFFFFFFFFFFFFFFFF, 'X')[12:] if redEntry.get() else "DUMMY"
    mgSpaceAmountFive = hex(int(mgEntry.get()))[2:].zfill(4).upper() if mgEntry.get() else "DUMMY"
    koopaAmountFive = hex(int(koopaEntry.get()))[2:].zfill(4).upper() if koopaEntry.get() else "DUMMY"
    starSpaceAmountFive = hex(int(starEntry.get()))[2:].zfill(4).upper() if starEntry.get() else "DUMMY"
    starSpaceAmountNegativeFive = format(-int(starEntry.get()) & 0xFFFFFFFFFFFFFFFF, 'X')[12:] if starEntry.get() else "DUMMY"
    wigglerSpaceAmountFive = hex(int(wigglerEntry.get()))[2:].zfill(4).upper() if wigglerEntry.get() else "DUMMY"
    wigglerSpaceAmountNegativeFive = format(-int(wigglerEntry.get()) & 0xFFFFFFFFFFFFFFFF, 'X')[12:] if wigglerEntry.get() else "DUMMY"
    chompWeightBaseAmountFive = hex(int(chompWeightEntry.get()))[2:].zfill(4).upper() if chompWeightEntry.get() else "DUMMY"
    chompSpaceAmountFive = hex(int(chompWeightEntry.get()))[2:].zfill(4).upper() if chompWeightEntry.get() else "DUMMY"
    chompSpaceAmountNegativeFive = format(-int(chompWeightEntry.get()) & 0xFFFFFFFFFFFFFFFF, 'X')[12:] if chompWeightEntry.get() else "DUMMY"
    chompStarStealFive = hex(int(chompStarEntry.get()))[2:].zfill(4).upper() if chompStarEntry.get() else "DUMMY"
    chompStarStealNegBase = -int(chompStarEntry.get()) if chompStarEntry.get() else "DUMMY"
    chompSpaceAmountNegativeFive = format(chompStarStealNegBase & 0xFFFFFFFFFFFFFFFF, 'X')[12:] if chompStarEntry.get() else "DUMMY"
    initialCoins = hex(int(initialEntry.get()))[2:].zfill(4).upper() if initialEntry.get() else "DUMMY"

    marioPartyFiveStarSpace = getStarSpaceCodeFive(starSpaceAmountFive, starSpaceAmountNegativeFive, starEntry.get()) if starSpaceAmountFive != "DUMMY" else ""
    marioPartyFiveWigglerSpace = getWigglerSpaceCodeFive(wigglerSpaceAmountFive, wigglerSpaceAmountNegativeFive, wigglerEntry.get()) if wigglerSpaceAmountFive != "DUMMY" else ""
    marioPartyFiveChompSpace = getChompSpaceCodeFive(chompStarStealFive, chompSpaceAmountNegativeFive, chompStarEntry.get()) if chompStarStealFive != "DUMMY" else ""
    marioPartyFiveChompBase = getCoinStealBaseFive(chompSpaceAmountFive, chompWeightEntry.get()) if chompSpaceAmountFive != "DUMMY" else ""
    marioPartyFiveBlueSpace = getBlueSpaceCodeFive(blueSpaceAmountFive, blueEntry.get()) if blueSpaceAmountFive != "DUMMY" else ""
    marioPartyFiveRedSpace = getRedSpaceCodeFive(redSpaceAmountNegativeFive, redEntry.get()) if redSpaceAmountNegativeFive != "DUMMY" else ""
    marioPartyFiveMiniGame = getMinigameCodeFive(mgSpaceAmountFive, mgEntry.get()) if mgSpaceAmountFive != "DUMMY" else ""
    marioPartyFiveKoopaBank = getKoopaBankFive(koopaAmountFive, koopaEntry.get()) if koopaAmountFive != "DUMMY" else ""
    marioPartyFourInitialCoins = initialCoinsMod5(initialCoins, initialEntry.get()) if initialCoins != "DUMMY" else ""

    generatedCode = marioPartyFiveBlueSpace + marioPartyFiveRedSpace + marioPartyFiveKoopaBank + marioPartyFiveMiniGame + marioPartyFiveStarSpace + marioPartyFiveWigglerSpace + marioPartyFiveChompSpace + marioPartyFiveChompBase + marioPartyFourInitialCoins
    generatedCode = generatedCode.strip()

    pyperclip.copy(generatedCode)

    print("Generated codes copied to the clipboard.")
    createDialog("Operation Successful", "success", "Generated codes copied to clipboard!", None)