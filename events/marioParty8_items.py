# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

from codes.marioParty8 import *
from functions import *

import csv
import math
import pyperclip

def itemsEvent_mp8(board, twiceWeight4, thricePrice4, thriceWeight4, slowgoPrice4, slowgoWeight4, springoPrice4, springoWeight4, cashzapPrice4, cashzapWeight4, vampirePrice4, vampireWeight4, bitsizePrice4, bitsizeWeight4, blowayPrice4, blowayWeight4, bowloPrice4, bowloWeight4, weeglePrice4, weegleWeight4, thwompPrice4, thwompWeight4, bulletPrice4, bulletWeight4, bowserPrice4, bowserWeight4, dueloPrice4, dueloWeight4):
    if not twiceWeight4.get() or not thricePrice4.get() or not thriceWeight4.get() or not springoPrice4.get() or not springoWeight4.get() or not slowgoPrice4.get() or not slowgoWeight4.get() or not cashzapPrice4.get() or not cashzapWeight4.get() or not bitsizePrice4.get() or not bitsizeWeight4.get() or not blowayPrice4.get() or not blowayWeight4.get() or not vampirePrice4.get() or not vampireWeight4.get() or not bowloPrice4.get() or not bowloWeight4.get() or not weeglePrice4.get() or not weegleWeight4.get() or not bowserPrice4.get() or not bowserWeight4.get() or not bulletPrice4.get() or not bulletWeight4.get() or not thwompPrice4.get() or not thwompWeight4.get() or not dueloPrice4.get()  or not dueloWeight4.get():
        createDialog("Error", "error", "Please fill out all the boxes.", None)
        return
    
    board = board.get()

    thricePrice4 = thricePrice4.get()
    thriceWeight4 = thriceWeight4.get()
    slowgoPrice4 = slowgoPrice4.get()
    slowgoWeight4 = slowgoWeight4.get()
    springoPrice4 = springoPrice4.get()
    springoWeight4 = springoWeight4.get()
    cashzapPrice4 = cashzapPrice4.get()
    cashzapWeight4 = cashzapWeight4.get()
    bitsizePrice4 = bitsizePrice4.get()
    bitsizeWeight4 = bitsizeWeight4.get()
    blowayPrice4 = blowayPrice4.get()
    blowayWeight4 = blowayWeight4.get()
    vampirePrice4 = vampirePrice4.get()
    vampireWeight4 = vampireWeight4.get()
    weeglePrice4 = weeglePrice4.get()
    weegleWeight4 = weegleWeight4.get()
    bowserPrice4 = bowserPrice4.get()
    bowserWeight4 = bowserWeight4.get()
    bowloPrice4 = bowloPrice4.get()
    bowloWeight4 = bowloWeight4.get()
    bulletPrice4 = bulletPrice4.get()
    bulletWeight4 = bulletWeight4.get()
    thwompPrice4 = thwompPrice4.get()
    thwompWeight4 = thwompWeight4.get()
    dueloPrice4 = dueloPrice4.get()
    dueloWeight4 = dueloWeight4.get()
    twiceWeight4 = twiceWeight4.get()

    orbWeightTotal = int(twiceWeight4) + int(thriceWeight4) + int(slowgoWeight4) + int(springoWeight4) + int(cashzapWeight4) + int(bitsizeWeight4) + int(blowayWeight4) + int(vampireWeight4) + int(weegleWeight4) + int(bowserWeight4) + int(bowloWeight4) + int(bulletWeight4) + int(thwompWeight4) + int(dueloWeight4)
    
    def calculateWeight(weight):
        if orbWeightTotal < 100:
            percentage = int(weight)
            return percentage
        else:
            percentage = (int(weight) / orbWeightTotal) * 100
            if 0< percentage < 1:
                return math.ceil(percentage)
            return round(percentage)

    thriceWeight4 = calculateWeight(thriceWeight4)
    slowgoWeight4 = calculateWeight(slowgoWeight4)
    springoWeight4 = calculateWeight(springoWeight4)
    cashzapWeight4 = calculateWeight(cashzapWeight4)
    bitsizeWeight4 = calculateWeight(bitsizeWeight4)
    blowayWeight4 = calculateWeight(blowayWeight4)
    vampireWeight4 = calculateWeight(vampireWeight4)
    weegleWeight4 = calculateWeight(weegleWeight4)
    bowserWeight4 = calculateWeight(bowserWeight4)
    bowloWeight4 = calculateWeight(bowloWeight4)
    bulletWeight4 = calculateWeight(bulletWeight4)
    thwompWeight4 = calculateWeight(thwompWeight4)
    dueloWeight4 = calculateWeight(dueloWeight4)
    twiceWeight4 = calculateWeight(twiceWeight4)

    orbWeightTotal = twiceWeight4 + thriceWeight4 + springoWeight4 + slowgoWeight4 + cashzapWeight4 + bitsizeWeight4 + blowayWeight4 + vampireWeight4 + weegleWeight4 + bowserWeight4 + bowloWeight4 + bulletWeight4 + thwompWeight4 + dueloWeight4

    if orbWeightTotal < 100:
        var_names = ['twiceWeight4', 'thriceWeight4', 'slowgoWeight4', 'springoWeight4', 'cashzapWeight4', 'bitsizeWeight4', 'blowayWeight4', 'vampireWeight4', 'weegleWeight4', 'bowserWeight4', 'bowloWeight4', 'bulletWeight4', 'thwompWeight4', 'dueloWeight4']
        max_var = max(zip(var_names, (map(eval, var_names))), key=lambda tuple: tuple[1])[0]

        if max_var == 'thriceWeight4':
            thriceWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'slowgoWeight4':
            slowgoWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'springoWeight4':
            springoWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'cashzapWeight4':
            cashzapWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'bitsizeWeight4':
            bitsizeWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'blowayWeight4':
            blowayWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'vampireWeight4':
            vampireWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'weegleWeight4':
            weegleWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'bowserWeight4':
            bowserWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'bowloWeight4':
            bowloWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'bulletWeight4':
            bulletWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'thwompWeight4':
            thwompWeight4 += (100 - orbWeightTotal)
        
        if max_var == 'dueloWeight4':
            dueloWeight4 += (100 - orbWeightTotal)

        if max_var == 'twiceWeight4':
            twiceWeight4 += (100 - orbWeightTotal)

    thriceWeight4 = str(thriceWeight4)
    slowgoWeight4 = str(slowgoWeight4)
    springoWeight4 = str(springoWeight4)
    cashzapWeight4 = str(cashzapWeight4)
    bitsizeWeight4 = str(bitsizeWeight4)
    blowayWeight4 = str(blowayWeight4)
    vampireWeight4 = str(vampireWeight4)
    weegleWeight4 = str(weegleWeight4)
    bowserWeight4 = str(bowserWeight4)
    bowloWeight4 = str(bowloWeight4)
    bulletWeight4 = str(bulletWeight4)
    thwompWeight4 = str(thwompWeight4)
    dueloWeight4 = str(dueloWeight4)
    twiceWeight4 = str(twiceWeight4)

    try:
        thriceWeight4 = hex(int(thriceWeight4))
        if len(thriceWeight4) == 4:
            thriceWeight4 = thriceWeight4[2:]
        elif len(thriceWeight4) == 3:
            thriceWeight4 = "0" + thriceWeight4[2:]
    except:
        thriceWeight4 = "00"
    try:
        thricePrice4 = hex(int(thricePrice4))
        if len(thricePrice4) == 4:
            thricePrice4 = thricePrice4[2:]
        elif len(thricePrice4) == 3:
            thricePrice4 = "0" + thricePrice4[2:]
    except:
        thricePrice4 = "00"
    try:
        springoWeight4 = hex(int(springoWeight4))
        if len(springoWeight4) == 4:
            springoWeight4 = springoWeight4[2:]
        elif len(springoWeight4) == 3:
            springoWeight4 = "0" + springoWeight4[2:]
    except:
        springoWeight4 = "00"
    try:
        slowgoPrice4 = hex(int(slowgoPrice4))
        if len(slowgoPrice4) == 4:
            slowgoPrice4 = slowgoPrice4[2:]
        elif len(slowgoPrice4) == 3:
            slowgoPrice4 = "0" + slowgoPrice4[2:]
    except:
        slowgoPrice4 = "00"
    try:
        slowgoWeight4 = hex(int(slowgoWeight4))
        if len(slowgoWeight4) == 4:
            slowgoWeight4 = slowgoWeight4[2:]
        elif len(slowgoWeight4) == 3:
            slowgoWeight4 = "0" + slowgoWeight4[2:]
    except:
        slowgoWeight4 = "00"
    try:
        springoPrice4 = hex(int(springoPrice4))
        if len(springoPrice4) == 4:
            springoPrice4 = springoPrice4[2:]
        elif len(springoPrice4) == 3:
            springoPrice4 = "0" + springoPrice4[2:]
    except:
        springoPrice4 = "00"
    try:
        cashzapWeight4 = hex(int(cashzapWeight4))
        if len(cashzapWeight4) == 4:
            cashzapWeight4 = cashzapWeight4[2:]
        elif len(cashzapWeight4) == 3:
            cashzapWeight4 = "0" + cashzapWeight4[2:]
    except:
        cashzapWeight4 = "00"
    try:
        cashzapPrice4 = hex(int(cashzapPrice4))
        if len(cashzapPrice4) == 4:
            cashzapPrice4 = cashzapPrice4[2:]
        elif len(cashzapPrice4) == 3:
            cashzapPrice4 = "0" + cashzapPrice4[2:]
    except:
        cashzapPrice4 = "00"
    try:
        bitsizeWeight4 = hex(int(bitsizeWeight4))
        if len(bitsizeWeight4) == 4:
            bitsizeWeight4 = bitsizeWeight4[2:]
        elif len(bitsizeWeight4) == 3:
            bitsizeWeight4 = "0" + bitsizeWeight4[2:]
    except:
        bitsizeWeight4 = "00"
    try:
        vampirePrice4 = hex(int(vampirePrice4))
        if len(vampirePrice4) == 4:
            vampirePrice4 = vampirePrice4[2:]
        elif len(vampirePrice4) == 3:
            vampirePrice4 = "0" + vampirePrice4[2:]
    except:
        vampirePrice4 = "00"
    try:
        blowayWeight4 = hex(int(blowayWeight4))
        if len(blowayWeight4) == 4:
            blowayWeight4 = blowayWeight4[2:]
        elif len(blowayWeight4) == 3:
            blowayWeight4 = "0" + blowayWeight4[2:]
    except:
        blowayWeight4 = "00"
    try:
        bitsizePrice4 = hex(int(bitsizePrice4))
        if len(bitsizePrice4) == 4:
            bitsizePrice4 = bitsizePrice4[2:]
        elif len(bitsizePrice4) == 3:
            bitsizePrice4 = "0" + bitsizePrice4[2:]
    except:
        bitsizePrice4 = "00"
    try:
        vampireWeight4 = hex(int(vampireWeight4))
        if len(vampireWeight4) == 4:
            vampireWeight4 = vampireWeight4[2:]
        elif len(vampireWeight4) == 3:
            vampireWeight4 = "0" + vampireWeight4[2:]
    except:
        vampireWeight4 = "00"
    try:
        blowayPrice4 = hex(int(blowayPrice4))
        if len(blowayPrice4) == 4:
            blowayPrice4 = blowayPrice4[2:]
        elif len(blowayPrice4) == 3:
            blowayPrice4 = "0" + blowayPrice4[2:]
    except:
        blowayPrice4 = "00"
    try:
        weegleWeight4 = hex(int(weegleWeight4))
        if len(weegleWeight4) == 4:
            weegleWeight4 = weegleWeight4[2:]
        elif len(weegleWeight4) == 3:
            weegleWeight4 = "0" + weegleWeight4[2:]
    except:
        weegleWeight4 = "00"
    try:
        bowloPrice4 = hex(int(bowloPrice4))
        if len(bowloPrice4) == 4:
            bowloPrice4 = bowloPrice4[2:]
        elif len(bowloPrice4) == 3:
            bowloPrice4 = "0" + bowloPrice4[2:]
    except:
        bowloPrice4 = "00"
    try:
        bowserWeight4 = hex(int(bowserWeight4))
        if len(bowserWeight4) == 4:
            bowserWeight4 = bowserWeight4[2:]
        elif len(bowserWeight4) == 3:
            bowserWeight4 = "0" + bowserWeight4[2:]
    except:
        bowserWeight4 = "00"
    try:
        weeglePrice4 = hex(int(weeglePrice4))
        if len(weeglePrice4) == 4:
            weeglePrice4 = weeglePrice4[2:]
        elif len(weeglePrice4) == 3:
            weeglePrice4 = "0" + weeglePrice4[2:]
    except:
        weeglePrice4 = "00"
    try:
        bowloWeight4 = hex(int(bowloWeight4))
        if len(bowloWeight4) == 4:
            bowloWeight4 = bowloWeight4[2:]
        elif len(bowloWeight4) == 3:
            bowloWeight4 = "0" + bowloWeight4[2:]
    except:
        bowloWeight4 = "00"
    try:
        thwompPrice4 = hex(int(thwompPrice4))
        if len(thwompPrice4) == 4:
            thwompPrice4 = thwompPrice4[2:]
        elif len(thwompPrice4) == 3:
            thwompPrice4 = "0" + thwompPrice4[2:]
    except:
        thwompPrice4 = "00"
    try:
        bulletWeight4 = hex(int(bulletWeight4))
        if len(bulletWeight4) == 4:
            bulletWeight4 = bulletWeight4[2:]
        elif len(bulletWeight4) == 3:
            bulletWeight4 = "0" + bulletWeight4[2:]
    except:
        bulletWeight4 = "00"
    try:
        bulletPrice4 = hex(int(bulletPrice4))
        if len(bulletPrice4) == 4:
            bulletPrice4 = bulletPrice4[2:]
        elif len(bulletPrice4) == 3:
            bulletPrice4 = "0" + bulletPrice4[2:]
    except:
        bulletPrice4 = "00"
    try:
        thwompWeight4 = hex(int(thwompWeight4))
        if len(thwompWeight4) == 4:
            thwompWeight4 = thwompWeight4[2:]
        elif len(thwompWeight4) == 3:
            thwompWeight4 = "0" + thwompWeight4[2:]
    except:
        thwompWeight4 = "00"
    try:
        bowserPrice4 = hex(int(bowserPrice4))
        if len(bowserPrice4) == 4:
            bowserPrice4 = bowserPrice4[2:]
        elif len(bowserPrice4) == 3:
            bowserPrice4 = "0" + bowserPrice4[2:]
    except:
        bowserPrice4 = "00"
    try:
        dueloWeight4 = hex(int(dueloWeight4))
        if len(dueloWeight4) == 4:
            dueloWeight4 = dueloWeight4[2:]
        elif len(dueloWeight4) == 3:
            dueloWeight4 = "0" + dueloWeight4[2:]
    except:
        dueloWeight4 = "00"
    try:
        dueloPrice4 = hex(int(dueloPrice4))
        if len(dueloPrice4) == 4:
            dueloPrice4 = dueloPrice4[2:]
        elif len(dueloPrice4) == 3:
            dueloPrice4 = "0" + dueloPrice4[2:]
    except:
        dueloPrice4 = "00"

    try:
        twiceWeight4 = hex(int(twiceWeight4))
        if len(twiceWeight4) == 4:
            twiceWeight4 = twiceWeight4[2:]
        elif len(twiceWeight4) == 3:
            twiceWeight4 = "0" + twiceWeight4[2:]
    except:
        twiceWeight4 = "00"

    if board == "DK's Treetop Temple":
        generatedCode = getCandyCodeDK(twiceWeight4, thricePrice4, thriceWeight4, slowgoPrice4, slowgoWeight4, springoPrice4, springoWeight4, cashzapPrice4, cashzapWeight4, vampirePrice4, vampireWeight4, bitsizePrice4, bitsizeWeight4, blowayPrice4, blowayWeight4, bowloPrice4, bowloWeight4, weeglePrice4, weegleWeight4, thwompPrice4, thwompWeight4, bulletPrice4, bulletWeight4, bowserPrice4, bowserWeight4, dueloPrice4, dueloWeight4)
    elif board == "Goomba's Booty Boardwalk":
        generatedCode = getCandyCodeGoomba(twiceWeight4, thricePrice4, thriceWeight4, slowgoPrice4, slowgoWeight4, springoPrice4, springoWeight4, cashzapPrice4, cashzapWeight4, vampirePrice4, vampireWeight4, bitsizePrice4, bitsizeWeight4, blowayPrice4, blowayWeight4, bowloPrice4, bowloWeight4, weeglePrice4, weegleWeight4, thwompPrice4, thwompWeight4, bulletPrice4, bulletWeight4, bowserPrice4, bowserWeight4, dueloPrice4, dueloWeight4)
    elif board == "King Boo's Haunted Hideaway":
        generatedCode = getCandyCodeBoo(twiceWeight4, thricePrice4, thriceWeight4, slowgoPrice4, slowgoWeight4, springoPrice4, springoWeight4, cashzapPrice4, cashzapWeight4, vampirePrice4, vampireWeight4, bitsizePrice4, bitsizeWeight4, blowayPrice4, blowayWeight4, bowloPrice4, bowloWeight4, weeglePrice4, weegleWeight4, thwompPrice4, thwompWeight4, bulletPrice4, bulletWeight4, bowserPrice4, bowserWeight4, dueloPrice4, dueloWeight4)
    elif board == "Shy Guy's Perplex Express":
        generatedCode = getCandyCodeShyGuy(twiceWeight4, thricePrice4, thriceWeight4, slowgoPrice4, slowgoWeight4, springoPrice4, springoWeight4, cashzapPrice4, cashzapWeight4, vampirePrice4, vampireWeight4, bitsizePrice4, bitsizeWeight4, blowayPrice4, blowayWeight4, bowloPrice4, bowloWeight4, weeglePrice4, weegleWeight4, thwompPrice4, thwompWeight4, bulletPrice4, bulletWeight4, bowserPrice4, bowserWeight4, dueloPrice4, dueloWeight4)
    elif board == "Koopa's Tycoon Town":
        generatedCode = getCandyCodeKoopa(twiceWeight4, thricePrice4, thriceWeight4, slowgoPrice4, slowgoWeight4, springoPrice4, springoWeight4, cashzapPrice4, cashzapWeight4, vampirePrice4, vampireWeight4, bitsizePrice4, bitsizeWeight4, blowayPrice4, blowayWeight4, bowloPrice4, bowloWeight4, weeglePrice4, weegleWeight4, thwompPrice4, thwompWeight4, bulletPrice4, bulletWeight4, bowserPrice4, bowserWeight4, dueloPrice4, dueloWeight4)
    elif board == "Bowser's Warped Orbit":
        generatedCode = getCandyCodBowser(twiceWeight4, thricePrice4, thriceWeight4, slowgoPrice4, slowgoWeight4, springoPrice4, springoWeight4, cashzapPrice4, cashzapWeight4, vampirePrice4, vampireWeight4, bitsizePrice4, bitsizeWeight4, blowayPrice4, blowayWeight4, bowloPrice4, bowloWeight4, weeglePrice4, weegleWeight4, thwompPrice4, thwompWeight4, bulletPrice4, bulletWeight4, bowserPrice4, bowserWeight4, dueloPrice4, dueloWeight4)

    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)
    print("Generated code copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

def savePresetItems8(twiceWeight4, thricePrice4, thriceWeight4, slowgoPrice4, slowgoWeight4, springoPrice4, springoWeight4, cashzapPrice4, cashzapWeight4, vampirePrice4, vampireWeight4, bitsizePrice4, bitsizeWeight4, blowayPrice4, blowayWeight4, bowloPrice4, bowloWeight4, weegleePrice4, weegleeWeight4, thwompPrice4, thwompWeight4, bulletPrice4, bulletWeight4, bowserPrice4, bowserWeight4, dueloPrice4, dueloWeight4):
    if not twiceWeight4.get() or not thricePrice4.get() or not twiceWeight4.get() or not thricePrice4.get() or not thriceWeight4.get() or not slowgoPrice4.get() or not slowgoWeight4.get() or not springoPrice4.get() or not springoWeight4.get() or not cashzapPrice4.get() or not cashzapWeight4.get() or not vampirePrice4.get() or not vampireWeight4.get() or not bitsizePrice4.get() or not bitsizeWeight4.get() or not blowayPrice4.get() or not blowayWeight4.get() or not bowloPrice4.get() or not bowloWeight4.get() or not weegleePrice4.get() or not weegleeWeight4.get() or not thwompPrice4.get() or not thwompWeight4.get() or not bulletPrice4.get() or not bulletWeight4.get() or not bowserPrice4.get() or not bowserWeight4.get() or not dueloPrice4.get() or not dueloWeight4.get():
        if sys.platform == "darwin":
            createDialog("Error", "error", "Please fill out all the boxes.", None)
        else:
            createDialog("Error", "error", "Please fill out all the boxes.", None)
        return
    
    twiceWeight4 = twiceWeight4.get()
    
    thricePrice4 = thricePrice4.get()
    thriceWeight4 = thriceWeight4.get()
    slowgoPrice4 = slowgoPrice4.get()
    slowgoWeight4 = slowgoWeight4.get()
    springoPrice4 = springoPrice4.get()
    springoWeight4 = springoWeight4.get()
    cashzapPrice4 = cashzapPrice4.get()
    cashzapWeight4 = cashzapWeight4.get()
    vampirePrice4 = vampirePrice4.get()
    vampireWeight4 = vampireWeight4.get()
    bitsizePrice4 = bitsizePrice4.get()
    bitsizeWeight4 = bitsizeWeight4.get()
    blowayPrice4 = blowayPrice4.get()
    blowayWeight4 = blowayWeight4.get()
    bowloPrice4 = bowloPrice4.get()
    bowloWeight4 = bowloWeight4.get()
    weegleePrice4 = weegleePrice4.get()
    weegleeWeight4 = weegleeWeight4.get()
    thwompPrice4 = thwompPrice4.get()
    thwompWeight4 = thwompWeight4.get()
    bulletPrice4 = bulletPrice4.get()
    bulletWeight4 = bulletWeight4.get()
    bowserPrice4 = bowserPrice4.get()
    bowserWeight4 = bowserWeight4.get()
    dueloPrice4 = dueloPrice4.get()
    dueloWeight4 = dueloWeight4.get()
    prices8 = ["5", thricePrice4, slowgoPrice4, springoPrice4, cashzapPrice4, vampirePrice4, bitsizePrice4, blowayPrice4, bowloPrice4, weegleePrice4, thwompPrice4, bulletPrice4, bowserPrice4, dueloPrice4]
    weights8 = [twiceWeight4, thriceWeight4, slowgoWeight4, springoWeight4, cashzapWeight4, vampireWeight4, bitsizeWeight4, blowayWeight4, bowloWeight4, weegleeWeight4, thwompWeight4, bulletWeight4, bowserWeight4, dueloWeight4]
    file_path = tkinter.filedialog.asksaveasfilename(defaultextension=".mpt", filetypes=[("MPT files", "*.mpt")])
    if file_path:
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Prices', 'Weights'])
            for price, weight in zip(prices8, weights8):
                writer.writerow([price, weight])
        print("MPT file saved successfully!")
        createDialog("Operation Sucessful", "success", "Presets file saved successfully!.", None)

def loadPresetItems8(twiceWeight4, thricePrice4, thriceWeight4, slowgoPrice4, slowgoWeight4, springoPrice4, springoWeight4, cashzapPrice4, cashzapWeight4, vampirePrice4, vampireWeight4, bitsizePrice4, bitsizeWeight4, blowayPrice4, blowayWeight4, bowloPrice4, bowloWeight4, weegleePrice4, weegleeWeight4, thwompPrice4, thwompWeight4, bulletPrice4, bulletWeight4, bowserPrice4, bowserWeight4, dueloPrice4, dueloWeight4):
    file_path = tkinter.filedialog.askopenfilename(defaultextension=".mpt", filetypes=[("MPT files", "*.mpt")])
    if file_path:
        prices8In = []
        weights8In = []
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                prices8In.append(float(row[0]))
                weights8In.append(float(row[1]))
        
        testVar = ""
        # Define a list of Entry widget attributes
        
        pricesNames8 = [testVar, thricePrice4, slowgoPrice4, springoPrice4, cashzapPrice4, vampirePrice4, bitsizePrice4, blowayPrice4, bowloPrice4, weegleePrice4, thwompPrice4, bulletPrice4, bowserPrice4, dueloPrice4]
        weightsNames8 = [twiceWeight4, thriceWeight4, slowgoWeight4, springoWeight4, cashzapWeight4, vampireWeight4, bitsizeWeight4, blowayWeight4, bowloWeight4, weegleeWeight4, thwompWeight4, bulletWeight4, bowserWeight4, dueloWeight4]
        # Update widgets with loaded values
        for index, widget in enumerate(pricesNames8):
            if widget and index < len(prices8In):
                widget.delete(0, 'end')
                widget.insert(0, int(prices8In[index]))
        for index, widget in enumerate(weightsNames8):
            if widget and index < len(weights8In):
                widget.delete(0, 'end')
                widget.insert(0, int(weights8In[index]))
        print("MPT file laoded successfully!")
        createDialog("Operation Sucessful", "success", "Presets file saved successfully!.", None)