# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

from codes.marioParty7 import *
from functions import *

import pyperclip


def spinxEvent_mp7(spinx, spinx_list):
    spinxSlot = spinx.get()
    spinxHex = ["03", "00", "01", "02"]
    spinxSlot1Num = spinx_list.index(spinxSlot)
    spinxSlot1Hex = spinxHex[spinxSlot1Num]
    code = getSpinxEvent(spinxSlot1Hex, spinxSlot)
    code = code.strip()
    pyperclip.copy(code)
    print("Generated codes copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

def gliderEvent_mp7(spinx, spinx_list):
    spinxSlot = spinx.get()
    spinxHex = ["02", "00", "01"]
    spinxSlot1Num = spinx_list.index(spinxSlot)
    spinxSlot1Hex = spinxHex[spinxSlot1Num]
    code = getGliderEvent(spinxSlot1Hex, spinxSlot)
    code = code.strip()
    pyperclip.copy(code)
    print("Generated codes copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

def chompEvent_mp7(coin):
    if not coin.get():
        createDialog("Error", "error", "Please fill out the box.", None)
        return
    coin2 = hex(int(coin.get()))[2:].zfill(4).upper() if coin.get() else "DUMMY"
    mpChompEventBlack = getBlackChomp(coin2, coin.get()) if coin2 != "DUMMY" else ""
    generatedCode = (mpChompEventBlack).strip()
    pyperclip.copy(generatedCode)
    print("Generated codes copied to the clipboard.")
    createDialog("Operation Successful", "success", "Generated codes copied to clipboard!", None)


def redChompEvent_mp7(coin):
    if not coin.get():
        createDialog("Error", "error", "Please fill out the box.", None)
        return
    coin3 = hex(int(coin.get()))[2:].zfill(4).upper() if coin.get() else "DUMMY"
    mpChompEventRed = getRedChomp(coin3, coin.get()) if coin3 != "DUMMY" else ""
    generatedCode = (mpChompEventRed).strip()
    pyperclip.copy(generatedCode)
    print("Generated codes copied to the clipboard.")
    createDialog("Operation Successful", "success", "Generated codes copied to clipboard!", None)

def gliderCostEvent_mp7(coin):
    if not coin.get():
        createDialog("Error", "error", "Please fill out the box.", None)
        return
    coin2 = hex(int(coin.get()))[2:].zfill(4).upper() if coin.get() else "DUMMY"
    coinNegBase = -int(coin.get()) if coin.get() else "DUMMY" 
    coinNeg = format(coinNegBase & 0xFFFFFFFFFFFFFFFF, 'X')[12:] if coin.get() else "DUMMY"

    mpChompEventBlack = getGliderCostEvent(coin2, coinNeg, coin.get()) if coin2 != "DUMMY" else ""
    generatedCode = (mpChompEventBlack).strip()
    pyperclip.copy(generatedCode)
    print("Generated codes copied to the clipboard.")
    createDialog("Operation Successful", "success", "Generated codes copied to clipboard!", None)

def windmillEvent_mp7(coin):
    if not coin.get():
        createDialog("Error", "error", "Please fill out the box.", None)
        return
    coin3 = hex(int(coin.get()))[2:].zfill(4).upper() if coin.get() else "DUMMY"
    mpChompEventRed = getWindmillMaxSeven(coin3, coin.get()) if coin3 != "DUMMY" else ""
    generatedCode = (mpChompEventRed).strip()
    pyperclip.copy(generatedCode)
    print("Generated codes copied to the clipboard.")
    createDialog("Operation Successful", "success", "Generated codes copied to clipboard!", None)