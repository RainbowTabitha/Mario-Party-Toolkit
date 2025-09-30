# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (tabitha@tabs.gay)
# Date: 5/12/2024
# License: MIT
# ============================================

from codes.marioParty6 import *
from functions import *

import pyperclip

def initialItemsEvent_mp6(initalItem41, initalItem42, initalItem43, items6):
    itemSlot1 = initalItem41.get()
    itemSlot2 = initalItem42.get()
    itemSlot3 = initalItem43.get()
    itemHex = ["FF", "00", "01", "02", "03", "04", "06", "07", "0A", "0B", "0C", "0D", "0F", "10", "11", "14", "15", "16", "17", "18", "19", "1E", "1F"]
    itemSlot1Num = items6.index(itemSlot1)
    itemSlot1Hex = itemHex[itemSlot1Num]

    itemSlot2Num = items6.index(itemSlot2)
    itemSlot2Hex = itemHex[itemSlot2Num]

    itemSlot3Num = items6.index(itemSlot3)
    itemSlot3Hex = itemHex[itemSlot3Num]

    code = getInitialItemsSix(itemSlot1Hex, itemSlot2Hex, itemSlot3Hex, itemSlot1, itemSlot2, itemSlot3)
    code = code.strip()
    pyperclip.copy(code)
    print("Generated codes copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)