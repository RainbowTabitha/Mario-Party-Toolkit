# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (tabitha@tabs.gay)
# Date: 8/1/2024
# License: MIT
# ============================================

from codes.marioParty5 import *
from functions import *

import pyperclip


def underseaEvent_mp5(item, item_list):
    itemSlot = item.get()
    itemHex = ["00", "01", "02", "03", "04", "05", "06", "0A", "0B", "0C", "0D", "0F", "10", "11", "14", "15", "16", "17", "18", "19", "1E", "1F", "20", "21", "22", "23", "24", "25"]
    itemSlot1Num = item_list.index(itemSlot)
    itemSlot1Hex = itemHex[itemSlot1Num]
    code = getUnderseaShell(itemSlot1Hex, itemSlot)
    code = code.strip()
    pyperclip.copy(code)
    print("Generated codes copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)
