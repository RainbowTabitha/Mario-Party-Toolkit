# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (tabitha@tabs.gay)
# Date: 7/32024
# License: MIT
# ============================================

from codes.marioPartyDS import *
from functions import *

import pyperclip


def mgReplaceEvent_mpDS(minigame1Name, minigame2Name, minigames_list):
    mingameSlot1 = minigame1Name.get()
    mingameSlot2 = minigame2Name.get()
    minigameHex = ["01", "02", "03", "04", "05", "06", "07", "08", "0A", "0B", "0C", "0D", "0E", "0F", "11", "12", "13", "14", "15", "16", "17", "18", "19", "1A", "1B", "1C", "1D", "1E", "1F", "20", "21", "22", "23", "24", "25", "26", "27", "28", "29", "2A", "2B", "2C", "2D", "2E", "2F", "30", "31", "32", "34", "35", "36", "37", "38", "39", "3A", "3B", "3C", "3D", "3E", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "4A", "4B", "4C", "4D"]
    minigameSlot1Num = minigames_list.index(mingameSlot1)
    minigameSlot1Hex = minigameHex[minigameSlot1Num]
    minigameSlot2Num = minigames_list.index(mingameSlot2)
    minigameSlot2Hex = minigameHex[minigameSlot2Num]
    code = getMinigameReplacementDS(minigameSlot1Hex, minigameSlot2Hex, mingameSlot1, mingameSlot2)
    code = code.strip()
    pyperclip.copy(code)
    print("Generated codes copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)
