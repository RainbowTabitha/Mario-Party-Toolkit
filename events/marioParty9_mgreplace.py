# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (tabitha@tabs.gay)
# Date: 7/3/2024
# License: MIT
# ============================================

from codes.marioParty9 import *
from functions import *

import pyperclip


def mgReplaceEvent_mp9(minigame1Name, minigame2Name, minigames_list):
    mingameSlot1 = minigame1Name.get()
    mingameSlot2 = minigame2Name.get()
    minigameHex = ["313031", "313032", "313033", "313034", "313035", "313036", "313037", "313038", "313039", "313130", "323031", "323032", "323033", "323034", "323035", "323036", "323037", "323038", "323039", "323130", "343031", "343032", "343033", "343034", "343035", "343036", "343037", "343038", "343039", "343130", "343131", "343132", "343133", "343134", "343135", "343136", "343137", "343138", "343139", "343230", "343231", "343232", "343233", "343234", "343235", "343236", "343237", "343238", "343239", "343330", "343331", "343332", "343333", "343334", "343335", "343336", "343337", "343338", "343339", "343430", "343431", "343432", "343433", "343434", "363031", "363032", "363033", "363034", "363035", "363036", "363037", "373031", "373032", "373033", "373034", "373035", "373036", "37303"]
    minigameSlot1Num = minigames_list.index(mingameSlot1)
    minigameSlot1Hex = minigameHex[minigameSlot1Num]
    minigameSlot2Num = minigames_list.index(mingameSlot2)
    minigameSlot2Hex = minigameHex[minigameSlot2Num]
    code = getMinigameReplacement9(minigameSlot1Hex, minigameSlot2Hex, mingameSlot1, mingameSlot2)
    code = code.strip()
    pyperclip.copy(code)
    print("Generated codes copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)
