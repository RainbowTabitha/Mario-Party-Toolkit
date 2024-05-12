# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/7/2024
# License: MIT
# ============================================

from codes.marioParty4 import *
from functions import *

import pyperclip

def initialItemsEvent_mp4(lotteryPrizeA, lotteryPrizeB, lotteryPrizeC, lotteryPrizeD, items4):
    itemSlot1 = lotteryPrizeC.get()
    itemSlot2 = lotteryPrizeD.get()
    itemHex = ["FF", "00", "01", "02", "03", "04", "05", "06", "07", "08", "09", "0A", "0B", "0C", "0D"]
    itemSlot1Num = items4.index(itemSlot1)
    itemSlot1Hex = itemHex[itemSlot1Num]

    itemSlot2Num = items4.index(itemSlot2)
    itemSlot2Hex = itemHex[itemSlot2Num]

    code = getInitialItemsFour(itemSlot1Hex, itemSlot2Hex, itemSlot1, itemSlot2)
    code = code.strip()
    pyperclip.copy(code)
    print("Generated codes copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)