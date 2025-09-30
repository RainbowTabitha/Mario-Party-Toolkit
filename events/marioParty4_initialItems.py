# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

from codes.marioParty4 import *
from functions import *

import pyperclip

def initialItemsEvent_mp4(initalItem41, initalItem42, initalItem43, items4):
    itemSlot1 = initalItem41.get()
    itemSlot2 = initalItem42.get()
    itemSlot3 = initalItem43.get()
    itemHex = ["FF", "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "0A", "0B", "0C", "0D"]
    itemSlot1Num = items4.index(itemSlot1)
    itemSlot1Hex = itemHex[itemSlot1Num]

    itemSlot2Num = items4.index(itemSlot2)
    itemSlot2Hex = itemHex[itemSlot2Num]

    itemSlot3Num = items4.index(itemSlot3)
    itemSlot3Hex = itemHex[itemSlot3Num]

    code = getInitialItemsFour(itemSlot1Hex, itemSlot2Hex, itemSlot3Hex, itemSlot1, itemSlot2, itemSlot3)
    code = code.strip()
    pyperclip.copy(code)
    print("Generated codes copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)