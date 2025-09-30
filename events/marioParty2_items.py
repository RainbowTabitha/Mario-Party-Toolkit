# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (tabitha@tabs.gay)
# Date: 5/4/2024
# License: MIT
# ============================================

from codes.marioParty2 import *
from functions import *

import pyperclip


def itemsEvent_mp2(mushroom2, skeletonKey2, plunderChest2, duelingGlove2, warpBlock2, goldenMushroom2, magicLamp2):
    if not mushroom2.get() or not skeletonKey2.get() or not plunderChest2.get() or not duelingGlove2.get() or not warpBlock2.get() or not goldenMushroom2.get() or not magicLamp2.get():
        createDialog("Error", "error", "Please fill out all the boxes.", None)
        return

    mushroom2 = mushroom2.get()
    skeletonKey2 = skeletonKey2.get()
    plunderChest2 = plunderChest2.get()
    duelingGlove2 = duelingGlove2.get()
    warpBlock2 = warpBlock2.get()
    goldenMushroom2 = goldenMushroom2.get()
    magicLamp2 = magicLamp2.get()

    try:
        mushroom2 = hex(int(mushroom2))
        if len(mushroom2) == 4:
            mushroom2 = mushroom2[2:]
        elif len(mushroom2) == 3:
            mushroom2 = "0" + mushroom2[2:]
    except:
        mushroom2 = "00"

    try:
        skeletonKey2 = hex(int(skeletonKey2))
        if len(skeletonKey2) == 4:
            skeletonKey2 = skeletonKey2[2:]
        elif len(skeletonKey2) == 3:
            skeletonKey2 = "0" + skeletonKey2[2:]
    except:
        skeletonKey2 = "00"

    try:
        plunderChest2 = hex(int(plunderChest2))
        if len(plunderChest2) == 4:
            plunderChest2 = plunderChest2[2:]
        elif len(plunderChest2) == 3:
            plunderChest2 = "0" + plunderChest2[2:]
    except:
        plunderChest2 = "00"

    try:
        duelingGlove2 = hex(int(duelingGlove2))
        if len(duelingGlove2) == 4:
            duelingGlove2 = duelingGlove2[2:]
        elif len(duelingGlove2) == 3:
            duelingGlove2 = "0" + duelingGlove2[2:]
    except:
        duelingGlove2 = "00"

    try:
        warpBlock2 = hex(int(warpBlock2))
        if len(warpBlock2) == 4:
            warpBlock2 = warpBlock2[2:]
        elif len(warpBlock2) == 3:
            warpBlock2 = "0" + warpBlock2[2:]
    except:
        warpBlock2 = "00"

    try:
        goldenMushroom2 = hex(int(goldenMushroom2))
        if len(goldenMushroom2) == 4:
            goldenMushroom2 = goldenMushroom2[2:]
        elif len(goldenMushroom2) == 3:
            goldenMushroom2 = "0" + goldenMushroom2[2:]
    except:
        goldenMushroom2 = "00"

    try:
        magicLamp2 = hex(int(magicLamp2))
        if len(magicLamp2) == 4:
            magicLamp2 = magicLamp2[2:]
        elif len(magicLamp2) == 3:
            magicLamp2 = "0" + magicLamp2[2:]
    except:
        magicLamp2 = "00"

    code = getItems2(mushroom2.upper(), skeletonKey2.upper(), plunderChest2.upper(), duelingGlove2.upper(), warpBlock2.upper(), goldenMushroom2.upper(), magicLamp2.upper())
    code = code.strip()
    pyperclip.copy(code)

    print("Generated code copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)