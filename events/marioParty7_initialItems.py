# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

from codes.marioParty7 import *
from functions import *

import pyperclip

def initialItemsEvent_mp7(initalItem41, initalItem42, initalItem43, initalItem44, initalItem45, items7):
    itemSlot1 = initalItem41.get()
    itemSlot2 = initalItem42.get()
    itemSlot3 = initalItem43.get()
    itemSlot4 = initalItem44.get()
    itemSlot5 = initalItem45.get()
    itemHex = ["FF", "00", "01", "02", "03", "04", "05", "06", "07", "0A", "0B", "0C", "0D", "0E", "0F", "10", "11", "14", "15", "16", "17", "18", "19", "1E", "1F", "20", "21", "22", "23", "28"]
    
    itemSlot1Num = items7.index(itemSlot1)
    itemSlot1Hex = itemHex[itemSlot1Num]

    itemSlot2Num = items7.index(itemSlot2)
    itemSlot2Hex = itemHex[itemSlot2Num]

    itemSlot3Num = items7.index(itemSlot3)
    itemSlot3Hex = itemHex[itemSlot3Num]

    itemSlot4Num = items7.index(itemSlot4)
    itemSlot4Hex = itemHex[itemSlot4Num]

    itemSlot5Num = items7.index(itemSlot5)
    itemSlot5Hex = itemHex[itemSlot5Num]

    code = getInitialItemsSeven(itemSlot1Hex, itemSlot2Hex, itemSlot3Hex, itemSlot4Hex, itemSlot5Hex, itemSlot1, itemSlot2, itemSlot3, itemSlot4, itemSlot5)
    code = code.strip()
    pyperclip.copy(code)
    print("Generated codes copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)