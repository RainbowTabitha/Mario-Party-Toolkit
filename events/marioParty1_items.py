# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (tabitha@tabs.gay)
# Date: 7/24/2024
# License: MIT
# ============================================

from codes.marioParty1 import *
from functions import *

import pyperclip


def itemsEvent_mp1(plus, minus, speed, slow, warp, stock):
    if not all([plus.text(), minus.text(), speed.text(), slow.text(), warp.text(), stock.text()]):
        createDialog("Error", "error", "Please fill out all the boxes.", None)
        return

    try:
        plusWeight = float(plus.text())
        minusWeight = float(minus.text())
        speedWeight = float(speed.text())
        slowWeight = float(slow.text())
        warpWeight = float(warp.text())
        stockWeight = float(stock.text())
    except ValueError:
        createDialog("Error", "error", "Please enter valid integers.", None)
        return

    total_weight = plusWeight + minusWeight + speedWeight + slowWeight + warpWeight + stockWeight

    # Normalize weights to ensure they sum to 100%
    if total_weight > 0:
        plusWeight = (plusWeight / total_weight) * 100
        minusWeight = (minusWeight / total_weight) * 100
        speedWeight = (speedWeight / total_weight) * 100
        slowWeight = (slowWeight / total_weight) * 100
        warpWeight = (warpWeight / total_weight) * 100
        stockWeight = (stockWeight / total_weight) * 100

    # Define cumulative weights
    cumulative_weights = [
        plusWeight,
        plusWeight + minusWeight,
        plusWeight + minusWeight + speedWeight,
        plusWeight + minusWeight + speedWeight + slowWeight,
        plusWeight + minusWeight + speedWeight + slowWeight + warpWeight,
        plusWeight + minusWeight + speedWeight + slowWeight + warpWeight + stockWeight,
    ]

    # Scale cumulative weights and ensure they do not exceed 255
    weights = [min(cumulative_weight * 2.56, 255) for cumulative_weight in cumulative_weights]

    # Ensure weights do not exceed 255
    if any(weight > 255 for weight in weights):
        createDialog("Error", "error", "One or more weight values exceed 255. Adjust inputs.", None)
        return

    hex_weights = []
    for weight in weights:
        hex_weight = hex(int(weight))[2:].zfill(2)  # Convert to hex and ensure two digits
        hex_weights.append(hex_weight.upper())  # Ensure uppercase for consistency


    code = getBlockWeights(*hex_weights).strip()
    pyperclip.copy(code)

    print("Generated code copied to the clipboard.")
    createDialog("Operation Successful", "success", "Generated codes copied to clipboard!", None)