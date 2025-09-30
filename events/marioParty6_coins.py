# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

from functions import *
from codes.marioParty6 import *
import pyperclip

def coinsEvent_mp6(blueEntry, redEntry, characterEntry, mgEntry, starEntry, pinkBooCoinsEntry, pinkBooMinEntry, pinkBooStarEntry, initialEntry, zapEntry):
    if not any((blueEntry.get(), redEntry.get(), characterEntry.get(), starEntry.get(), mgEntry.get(), pinkBooCoinsEntry.get(), pinkBooMinEntry.get(), pinkBooStarEntry.get(), initialEntry.get(), zapEntry.get())):
        createDialog("Error", "error", "Please fill out at least one box.", None)
        return
    
    blueSpaceAmountSix = hex(int(blueEntry.get()))[2:].zfill(4).upper() if blueEntry.get() else "DUMMY"
    redSpaceAmountNegativeSix = format(-int(redEntry.get()) & 0xFFFFFFFFFFFFFFFF, 'X')[12:] if redEntry.get() else "DUMMY"
    mgSpaceAmountSix = hex(int(mgEntry.get()))[2:].zfill(4).upper() if mgEntry.get() else "DUMMY"
    starSpaceAmountSix = hex(int(starEntry.get()))[2:].zfill(4).upper() if starEntry.get() else "DUMMY"
    starSpaceAmountNegativeSix = format(-int(starEntry.get()) & 0xFFFFFFFFFFFFFFFF, 'X')[12:] if starEntry.get() else "DUMMY"
    
    starSpacex2 = hex(int(starEntry.get()) * 2)[2:].zfill(4).upper() if starEntry.get() else "DUMMY"
    starSpacex4 = hex(int(starEntry.get()) * 4)[2:].zfill(4).upper() if starEntry.get() else "DUMMY"
    starSpacey2 = hex(int(starEntry.get()) // 2)[2:].zfill(4).upper() if starEntry.get() else "DUMMY"
    starSpacey4 = hex(int(starEntry.get()) // 4)[2:].zfill(4).upper() if starEntry.get() else "DUMMY"

    characterSpaceAmountSix = hex(int(characterEntry.get()))[2:].zfill(4).upper() if characterEntry.get() else "DUMMY"
    
    pinkBooCoinsSix = hex(int(pinkBooCoinsEntry.get()))[2:].zfill(4).upper() if pinkBooCoinsEntry.get() else "DUMMY"
    pinkBooCoinsSixNeg = format(-int(pinkBooCoinsEntry.get()) & 0xFFFFFFFFFFFFFFFF, 'X')[12:] if pinkBooCoinsEntry.get() else "DUMMY"
    
    pinkBooStarsSix = hex(int(pinkBooStarEntry.get()))[2:].zfill(4).upper() if pinkBooStarEntry.get() else "DUMMY"
    pinkBooStarsSixNeg = format(-int(pinkBooStarEntry.get()) & 0xFFFFFFFFFFFFFFFF, 'X')[12:] if pinkBooStarEntry.get() else "DUMMY"
    
    pinkBooCoinsMinSix = hex(int(pinkBooMinEntry.get())+ 2)[2:].zfill(4).upper() if pinkBooMinEntry.get() else "DUMMY"
    
    initialCoins = hex(int(initialEntry.get()))[2:].zfill(4).upper() if initialEntry.get() else "DUMMY"
    
    zap = hex(int(zapEntry.get()))[2:].zfill(4).upper() if zapEntry.get() else "DUMMY"

    marioPartySixBlueSpace = getBlueSpaceCodeSix(blueSpaceAmountSix, blueEntry.get()) if blueSpaceAmountSix != "DUMMY" else ""
    marioPartySixRedSpace = getRedSpaceCodeSix(redSpaceAmountNegativeSix, redEntry.get()) if redSpaceAmountNegativeSix != "DUMMY" else ""
    marioPartySixCharSpace = getCharacterSpaceCodeSix(characterSpaceAmountSix, characterEntry.get()) if characterSpaceAmountSix != "DUMMY" else ""
    marioPartySixMiniGame = getMinigameCodeSix(mgSpaceAmountSix, mgEntry.get()) if mgSpaceAmountSix != "DUMMY" else ""
    marioPartySixStarSpace = getStarSpaceCodeSix(starSpaceAmountSix, starSpaceAmountNegativeSix, starEntry.get(), starSpacey4, starSpacey2, starSpacex2, starSpacex4) if starSpaceAmountSix != "DUMMY" else ""
    marioPartySixChompCoins = getPinkBooCoinsSpaceCodeSix(pinkBooCoinsSix, pinkBooCoinsSixNeg, pinkBooCoinsEntry.get()) if pinkBooCoinsSix != "DUMMY" else ""
    marioPartySixChompStars = getPinkBooSpaceCodeSix(pinkBooStarsSix, pinkBooStarsSixNeg, pinkBooStarEntry.get()) if pinkBooStarsSix != "DUMMY" else ""
    marioPartySixChompBase = getCoinStealBaseSix(pinkBooCoinsMinSix, pinkBooMinEntry.get()) if pinkBooCoinsMinSix != "DUMMY" else ""
    marioPartySixInitialCoins = initialCoinsMod6(initialCoins, initialEntry.get()) if initialCoins != "DUMMY" else ""
    marioPartySixZap = getZapOrb6(zap, zapEntry.get()) if zap != "DUMMY" else ""

    generatedCode = marioPartySixBlueSpace + marioPartySixRedSpace + marioPartySixCharSpace + marioPartySixMiniGame + marioPartySixStarSpace + marioPartySixChompCoins + marioPartySixChompStars + marioPartySixChompBase + marioPartySixInitialCoins + marioPartySixZap
    generatedCode = generatedCode.strip()

    pyperclip.copy(generatedCode)

    print("Generated codes copied to the clipboard.")
    createDialog("Operation Successful", "success", "Generated codes copied to clipboard!", None)