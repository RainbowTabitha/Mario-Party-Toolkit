# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/12/2024
# License: MIT
# ============================================

from functions import *
from codes.marioParty7 import *
import pyperclip
def coinsEvent_mp7(blueEntry, redEntry, characterEntry, mgEntry, starEntry, startLast5, hammerBroEntry, zapEntry, fireballEntry, vacuumEntry, flowerEntry, initialEntry):
    if not any((blueEntry.get(), redEntry.get(), characterEntry.get(), mgEntry.get(), starEntry.get(), startLast5.get(), hammerBroEntry.get(), zapEntry.get(), fireballEntry.get(), vacuumEntry.get(), flowerEntry.get(), initialEntry.get())):
        createDialog("Error", "error", "Please fill out at least one box.", None)
        return
    
    blueSpaceAmountSeven = hex(int(blueEntry.get()))[2:].zfill(4).upper() if blueEntry.get() else "DUMMY"
    redSpaceAmountNegativeSeven = format(-int(redEntry.get()) & 0xFFFFFFFFFFFFFFFF, 'X')[12:] if redEntry.get() else "DUMMY"
    characterSpaceAmountSeven = hex(int(characterEntry.get()))[2:].zfill(4).upper() if characterEntry.get() else "DUMMY"
    mgSpaceAmountSeven = hex(int(mgEntry.get()))[2:].zfill(4).upper() if mgEntry.get() else "DUMMY"
    starSpaceAmountSeven = hex(int(starEntry.get()))[2:].zfill(4).upper() if starEntry.get() else "DUMMY"
    starSpaceAmountSevenLast5 = hex(int(startLast5.get()))[2:].zfill(4).upper() if startLast5.get() else "DUMMY"
    zapSeven = hex(int(zapEntry.get()))[2:].zfill(4).upper() if zapEntry.get() else "DUMMY"
    
    starSpacex2 = hex(int(starEntry.get()) * 2)[2:].zfill(4).upper() if starEntry.get() else "DUMMY"
    starSpacex3 = hex(int(starEntry.get()) * 3)[2:].zfill(4).upper() if starEntry.get() else "DUMMY"
    starSpacex4 = hex(int(starEntry.get()) * 4)[2:].zfill(4).upper() if starEntry.get() else "DUMMY"

    fireballSeven = hex(int(fireballEntry.get()))[2:].zfill(4).upper() if fireballEntry.get() else "DUMMY"
    fireballSevenNeg = format(-int(fireballEntry.get()) & 0xFFFFFFFFFFFFFFFF, 'X')[12:] if fireballEntry.get() else "DUMMY"
    
    flowerSeven = hex(int(flowerEntry.get()))[2:].zfill(4).upper() if flowerEntry.get() else "DUMMY"
    vacuumSeven = hex(int(vacuumEntry.get()))[2:].zfill(4).upper() if vacuumEntry.get() else "DUMMY"

    initialCoins = hex(int(initialEntry.get()))[2:].zfill(4).upper() if initialEntry.get() else "DUMMY"

    hammerBroSeven = hex(int(hammerBroEntry.get()))[2:].zfill(4).upper() if hammerBroEntry.get() else "DUMMY"
    hammerBroSevenNegative = format(-int(hammerBroEntry.get()) & 0xFFFFFFFFFFFFFFFF, 'X')[12:] if hammerBroEntry.get() else "DUMMY"
    hammerBroSevenHalf = format((-int(hammerBroEntry.get()) // 2) & 0xFFFFFFFFFFFFFFFF, 'X')[12:] if hammerBroEntry.get() else "DUMMY"

    marioPartySevenBlueSpace = getBlueSpaceCodeSeven(blueSpaceAmountSeven, blueEntry.get()) if blueSpaceAmountSeven != "DUMMY" else ""
    marioPartySevenRedSpace = getRedSpaceCodeSeven(redSpaceAmountNegativeSeven, redEntry.get()) if redSpaceAmountNegativeSeven != "DUMMY" else ""
    marioPartySevenCharSpace = getCharacterSpaceCodeSeven(characterSpaceAmountSeven, characterEntry.get()) if characterSpaceAmountSeven != "DUMMY" else ""
    marioPartySevenMiniGame = getMinigameCodeSeven(mgSpaceAmountSeven, mgEntry.get()) if mgSpaceAmountSeven != "DUMMY" else ""
    marioPartySevenStarSpace = getStarSpaceCodeSeven(starSpaceAmountSeven, starEntry.get(), starSpacex2, starSpacex3, starSpacex4) if starSpaceAmountSeven != "DUMMY" else ""
    marioPartySevenStarSpaceLast5 = getStarSpaceCodeSevenLastFive(starSpaceAmountSevenLast5, startLast5.get()) if starSpaceAmountSevenLast5 != "DUMMY" else ""
    marioPartySevenZap = getZapSpaceCodeSeven(zapSeven, zapEntry.get()) if zapSeven != "DUMMY" else ""
    marioPartySevenFireball = getFireballSpaceCodeSeven(fireballSeven, fireballSevenNeg, fireballEntry.get()) if fireballSeven != "DUMMY" else ""
    marioPartySevenFlower = getFlowerSpaceCodeSeven(flowerSeven, flowerEntry.get()) if flowerSeven != "DUMMY" else ""
    marioPartySevenVacuum = getVacuumSpaceCodeSeven(vacuumSeven, vacuumEntry.get()) if vacuumSeven != "DUMMY" else ""
    marioPartySevenHammerBro = getHammerBroSpaceCodeSeven(hammerBroSeven, hammerBroSevenNegative, hammerBroSevenHalf, hammerBroEntry.get()) if hammerBroSeven != "DUMMY" else ""
    marioPartyFourInitialCoins = initialCoinsMod7(initialCoins, initialEntry.get()) if initialCoins != "DUMMY" else ""

    generatedCode = marioPartySevenBlueSpace + marioPartySevenRedSpace + marioPartySevenCharSpace + marioPartySevenMiniGame + marioPartySevenStarSpace + marioPartySevenStarSpaceLast5 + marioPartySevenZap + marioPartySevenFireball + marioPartySevenFlower + marioPartySevenHammerBro + marioPartySevenVacuum + marioPartyFourInitialCoins
    generatedCode = generatedCode.strip()

    pyperclip.copy(generatedCode)

    print("Generated codes copied to the clipboard.")
    createDialog("Operation Successful", "success", "Generated codes copied to clipboard!", None)