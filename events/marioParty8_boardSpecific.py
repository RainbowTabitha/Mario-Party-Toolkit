# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/12/2024
# License: MIT
# ============================================

from functions import *
from codes.marioParty8 import *
import pyperclip

def hotelMaxInvestEvent_mp8(hotelEntry):
    if not hotelEntry.get():
        createDialog("Error", "error", "Please fill out the hotel max investment amount.", None)
        return
    
    hotelEight = hex(int(hotelEntry.get()))[2:].zfill(4).upper()
    marioPartyEightHotel = hotelMaxInvest(hotelEight, hotelEntry.get())

    generatedCode = marioPartyEightHotel.strip()

    pyperclip.copy(generatedCode)

    print("Generated codes copied to the clipboard.")
    createDialog("Operation Successful", "success", "Generated codes copied to clipboard!", None)
