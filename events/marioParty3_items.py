# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

from codes.marioParty3 import *
from functions import *
import pyperclip

def itemsEvent_mp3(mushroom, skeletonKey, poisonMushroom, reverseMushroom, goldenMushroom, magicLamp, warpBlock, cellularShopper, bowserPhone, duelingGlove, luckyLamp, bowserSuit, plunderChest, booBell, booRepellent, itemBag):
    if not all((mushroom.get(), skeletonKey.get(), poisonMushroom.get(), reverseMushroom.get(), goldenMushroom.get(), magicLamp.get(), warpBlock.get(), cellularShopper.get(), bowserPhone.get(), duelingGlove.get(), luckyLamp.get(), bowserSuit.get(), plunderChest.get(), booBell.get(), booRepellent.get(), itemBag.get())):
        createDialog("Error", "error", "Please fill out all the boxes.", None)
        return

    def to_hex(value):
        try:
            hex_value = hex(int(value))
            return hex_value[2:].zfill(2) if len(hex_value) < 4 else hex_value[2:]
        except:
            return "00"

    mushroom_hex = to_hex(mushroom.get())
    skeletonKey_hex = to_hex(skeletonKey.get())
    poisonMushroom_hex = to_hex(poisonMushroom.get())
    reverseMushroom_hex = to_hex(reverseMushroom.get())
    goldenMushroom_hex = to_hex(goldenMushroom.get())
    magicLamp_hex = to_hex(magicLamp.get())
    warpBlock_hex = to_hex(warpBlock.get())
    cellularShopper_hex = to_hex(cellularShopper.get())
    bowserPhone_hex = to_hex(bowserPhone.get())
    duelingGlove_hex = to_hex(duelingGlove.get())
    luckyLamp_hex = to_hex(luckyLamp.get())
    bowserSuit_hex = to_hex(bowserSuit.get())
    plunderChest_hex = to_hex(plunderChest.get())
    booBell_hex = to_hex(booBell.get())
    booRepellent_hex = to_hex(booRepellent.get())
    itemBag_hex = to_hex(itemBag.get())

    orbPriceMin = findLowestIntegerWithZero(int(mushroom.get()), int(skeletonKey.get()), int(plunderChest.get()), int(duelingGlove.get()), int(warpBlock.get()), int(goldenMushroom.get()), int(magicLamp.get()), int(cellularShopper.get()), int(itemBag.get()), int(poisonMushroom.get()), int(reverseMushroom.get()), int(booBell.get()), int(booRepellent.get()), int(luckyLamp.get()), int(bowserPhone.get()))
    orbPriceMin_hex = to_hex(orbPriceMin)

    code = getItems3(mushroom_hex.upper(), skeletonKey_hex.upper(), poisonMushroom_hex.upper(), reverseMushroom_hex.upper(), goldenMushroom_hex.upper(), magicLamp_hex.upper(), warpBlock_hex.upper(), cellularShopper_hex.upper(), bowserPhone_hex.upper(), duelingGlove_hex.upper(), luckyLamp_hex.upper(), bowserSuit_hex.upper(), plunderChest_hex.upper(), booBell_hex.upper(), booRepellent_hex.upper(), itemBag_hex.upper(), orbPriceMin_hex.upper()).strip()
    pyperclip.copy(code)

    print("Generated code copied to the clipboard.")
    createDialog("Operation Successful", "success", "Generated codes copied to clipboard!", None)