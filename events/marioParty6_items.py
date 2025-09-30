# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (tabitha@tabs.gay)
# Date: 5/12/2024
# License: MIT
# ============================================

from codes.marioParty6 import *
from functions import *

import csv
import math
import pyperclip

def itemsEvent_mp6(warpPipeCapsuleWeight6, warpPipeCapsulePrice6, mushroomCapsuleWeight6, goldenMushroomCapsulePrice6, goldenMushroomCapsuleWeight6, slowMushroomCapsulePrice6, slowMushroomCapsuleWeight6, metalMushroomCapsulePrice6, metalMushroomCapsuleWeight6, bulletBillCapsulePrice6, bulletBillCapsuleWeight6, flutterCapsulePrice6, flutterCapsuleWeight6, cursedMushroomCapsulePrice6, cursedMushroomCapsuleWeight6, spinyCapsulePrice6, spinyCapsuleWeight6, goombaCapsulePrice6, goombaCapsuleWeight6, plantCapsulePrice6, plantCapsuleWeight6, kleptoCapsulePrice6, kleptoCapsuleWeight6, toadyCapsulePrice6, toadyCapsuleWeight6, kamekCapsulePrice6, kamekCapsuleWeight6, blizzardCapsulePrice6, blizzardCapsuleWeight6, podobooCapsulePrice6, podobooCapsuleWeight6, zapCapsulePrice6, zapCapsuleWeight6, tweesterCapsulePrice6, tweesterCapsuleWeight6, thwompCapsulePrice6, thwompCapsuleWeight6, bombCapsulePrice6, bombCapsuleWeight6, paraTroopaCapsulePrice6, paraTroopaCapsuleWeight6, snackCapsulePrice6, snackCapsuleWeight6, gaddLightCapsulePrice6, gaddLightCapsuleWeight6, pinkBooCapsulePrice6, pinkBooCapsuleWeight6, chanceTimeCapsulePrice6, chanceTimeCapsuleWeight6, bowserCapsulePrice6, bowserCapsuleWeight6, dkCapsulePrice6, dkCapsuleWeight6, duelCapsulePrice6, duelCapsuleWeight6):
    if not metalMushroomCapsulePrice6.get() or not metalMushroomCapsuleWeight6.get() or not mushroomCapsuleWeight6.get() or not goldenMushroomCapsulePrice6.get() or not goldenMushroomCapsuleWeight6.get() or not slowMushroomCapsulePrice6.get() or not slowMushroomCapsuleWeight6.get() or not bulletBillCapsulePrice6.get() or not bulletBillCapsuleWeight6.get() or not warpPipeCapsulePrice6.get() or not warpPipeCapsuleWeight6.get() or not flutterCapsulePrice6.get() or not flutterCapsuleWeight6.get() or not cursedMushroomCapsulePrice6.get() or not cursedMushroomCapsuleWeight6.get() or not spinyCapsulePrice6.get() or not spinyCapsuleWeight6.get() or not goombaCapsuleWeight6.get() or not goombaCapsulePrice6.get() or not plantCapsulePrice6.get() or not plantCapsuleWeight6.get() or not kleptoCapsuleWeight6.get() or not kleptoCapsulePrice6.get() or not kamekCapsuleWeight6.get() or not kamekCapsulePrice6.get() or not toadyCapsuleWeight6.get() or not toadyCapsulePrice6.get() or not blizzardCapsuleWeight6.get() or not blizzardCapsulePrice6.get() or not podobooCapsulePrice6.get() or not podobooCapsuleWeight6.get() or not paraTroopaCapsuleWeight6.get() or not paraTroopaCapsulePrice6.get() or not snackCapsulePrice6.get() or not snackCapsuleWeight6.get() or not zapCapsulePrice6.get() or not zapCapsuleWeight6.get() or not tweesterCapsulePrice6.get() or not tweesterCapsuleWeight6.get() or not thwompCapsulePrice6.get() or not thwompCapsuleWeight6.get() or not warpPipeCapsulePrice6.get() or not warpPipeCapsuleWeight6.get() or not bombCapsulePrice6.get() or not bombCapsuleWeight6.get() or not gaddLightCapsulePrice6.get() or not gaddLightCapsuleWeight6.get():
        createDialog("Error", "error", "Please fill out all the boxes.", None)
        return
    
    mushroomCapsuleWeight6 = mushroomCapsuleWeight6.get()
    
    goldenMushroomCapsulePrice6 = goldenMushroomCapsulePrice6.get()
    goldenMushroomCapsuleWeight6 = goldenMushroomCapsuleWeight6.get()

    slowMushroomCapsulePrice6 = slowMushroomCapsulePrice6.get()
    slowMushroomCapsuleWeight6 = slowMushroomCapsuleWeight6.get()

    metalMushroomCapsulePrice6 = metalMushroomCapsulePrice6.get()
    metalMushroomCapsuleWeight6 = metalMushroomCapsuleWeight6.get()

    bulletBillCapsulePrice6 = bulletBillCapsulePrice6.get()
    bulletBillCapsuleWeight6 = bulletBillCapsuleWeight6.get()

    flutterCapsulePrice6 = flutterCapsulePrice6.get()
    flutterCapsuleWeight6 = flutterCapsuleWeight6.get()

    cursedMushroomCapsulePrice6 = cursedMushroomCapsulePrice6.get()
    cursedMushroomCapsuleWeight6 = cursedMushroomCapsuleWeight6.get()

    spinyCapsulePrice6 = spinyCapsulePrice6.get()
    spinyCapsuleWeight6 = spinyCapsuleWeight6.get()

    goombaCapsulePrice6 = goombaCapsulePrice6.get()
    goombaCapsuleWeight6 = goombaCapsuleWeight6.get()

    plantCapsulePrice6 = plantCapsulePrice6.get()
    plantCapsuleWeight6 = plantCapsuleWeight6.get()

    kleptoCapsulePrice6 = kleptoCapsulePrice6.get()
    kleptoCapsuleWeight6 = kleptoCapsuleWeight6.get()

    kamekCapsulePrice6 = kamekCapsulePrice6.get()
    kamekCapsuleWeight6 = kamekCapsuleWeight6.get()

    toadyCapsulePrice6 = toadyCapsulePrice6.get()
    toadyCapsuleWeight6 = toadyCapsuleWeight6.get()

    blizzardCapsulePrice6 = blizzardCapsulePrice6.get()
    blizzardCapsuleWeight6 = blizzardCapsuleWeight6.get()

    podobooCapsulePrice6 = podobooCapsulePrice6.get()
    podobooCapsuleWeight6 = podobooCapsuleWeight6.get()

    paraTroopaCapsulePrice6 = paraTroopaCapsulePrice6.get()
    paraTroopaCapsuleWeight6 = paraTroopaCapsuleWeight6.get()

    snackCapsulePrice6 = snackCapsulePrice6.get()
    snackCapsuleWeight6 = snackCapsuleWeight6.get()

    zapCapsulePrice6 = zapCapsulePrice6.get()
    zapCapsuleWeight6 = zapCapsuleWeight6.get()

    tweesterCapsulePrice6 = tweesterCapsulePrice6.get()
    tweesterCapsuleWeight6 = tweesterCapsuleWeight6.get()

    thwompCapsulePrice6 = thwompCapsulePrice6.get()
    thwompCapsuleWeight6 = thwompCapsuleWeight6.get()

    warpPipeCapsulePrice6 = warpPipeCapsulePrice6.get()
    warpPipeCapsuleWeight6 = warpPipeCapsuleWeight6.get()

    bombCapsulePrice6 = bombCapsulePrice6.get()
    bombCapsuleWeight6 = bombCapsuleWeight6.get()

    gaddLightCapsulePrice6 = gaddLightCapsulePrice6.get()
    gaddLightCapsuleWeight6 = gaddLightCapsuleWeight6.get()

    try:
        pinkBooCapsulePrice6 = pinkBooCapsulePrice6.get()
    except:
        pinkBooCapsulePrice6 = 0

    try:
        pinkBooCapsuleWeight6 = pinkBooCapsuleWeight6.get()
    except:
        pinkBooCapsuleWeight6 = 0

    try:
        chanceTimeCapsulePrice6 = chanceTimeCapsulePrice6.get()
    except:
        chanceTimeCapsulePrice6 = 0

    try:
        chanceTimeCapsuleWeight6 = chanceTimeCapsuleWeight6.get()
    except:
        chanceTimeCapsuleWeight6 = 0

    try:
        bowserCapsulePrice6 = bowserCapsulePrice6.get()
    except:
        bowserCapsulePrice6 = 0

    try:
        bowserCapsuleWeight6 = bowserCapsuleWeight6.get()
    except:
        bowserCapsuleWeight6 = 0

    try:
        dkCapsulePrice6 = dkCapsulePrice6.get()
    except:
        dkCapsulePrice6 = 0

    try:
        dkCapsuleWeight6 = dkCapsuleWeight6.get()
    except:
        dkCapsuleWeight6 = 0

    try:
        duelCapsulePrice6 = duelCapsulePrice6.get()
    except:
        duelCapsulePrice6 = 0

    try:
        duelCapsuleWeight6 = duelCapsuleWeight6.get()
    except:
        duelCapsuleWeight6 = 0


    orbWeightTotal = int(mushroomCapsuleWeight6) + int(goldenMushroomCapsuleWeight6) + int(bulletBillCapsuleWeight6) + int(slowMushroomCapsuleWeight6) + int(warpPipeCapsuleWeight6) + int(flutterCapsuleWeight6) + int(cursedMushroomCapsuleWeight6) + int(spinyCapsuleWeight6) + int(goombaCapsuleWeight6) + int(plantCapsuleWeight6) + int(kleptoCapsuleWeight6) + int(kamekCapsuleWeight6) + int(toadyCapsuleWeight6) + int(blizzardCapsuleWeight6) + int(podobooCapsuleWeight6) + int(paraTroopaCapsuleWeight6) + int(snackCapsuleWeight6) + int(zapCapsuleWeight6) + int(tweesterCapsuleWeight6) + int(thwompCapsuleWeight6) + int(warpPipeCapsuleWeight6) + int(bombCapsuleWeight6) + int(gaddLightCapsuleWeight6) + int(pinkBooCapsuleWeight6) + int(chanceTimeCapsuleWeight6) + int(bowserCapsuleWeight6) + int(dkCapsuleWeight6) + int(metalMushroomCapsuleWeight6) + int(duelCapsuleWeight6)

    def calculateWeight(weight):
        if orbWeightTotal < 100:
            percentage = int(weight)
            return percentage
        else:
            percentage = (int(weight) / orbWeightTotal) * 100
            if 0< percentage < 1:
                return math.ceil(percentage)
            return round(percentage)

    mushroomCapsuleWeight6 = calculateWeight(mushroomCapsuleWeight6)
    goldenMushroomCapsuleWeight6 = calculateWeight(goldenMushroomCapsuleWeight6)
    bulletBillCapsuleWeight6 = calculateWeight(bulletBillCapsuleWeight6)
    slowMushroomCapsuleWeight6 = calculateWeight(slowMushroomCapsuleWeight6)
    warpPipeCapsuleWeight6 = calculateWeight(warpPipeCapsuleWeight6)
    flutterCapsuleWeight6 = calculateWeight(flutterCapsuleWeight6)
    cursedMushroomCapsuleWeight6 = calculateWeight(cursedMushroomCapsuleWeight6)
    spinyCapsuleWeight6 = calculateWeight(spinyCapsuleWeight6)
    goombaCapsuleWeight6 = calculateWeight(goombaCapsuleWeight6)
    plantCapsuleWeight6 = calculateWeight(plantCapsuleWeight6)
    kleptoCapsuleWeight6 = calculateWeight(kleptoCapsuleWeight6)
    kamekCapsuleWeight6 = calculateWeight(kamekCapsuleWeight6)
    toadyCapsuleWeight6 = calculateWeight(toadyCapsuleWeight6)
    blizzardCapsuleWeight6 = calculateWeight(blizzardCapsuleWeight6)
    podobooCapsuleWeight6 = calculateWeight(podobooCapsuleWeight6)
    paraTroopaCapsuleWeight6 = calculateWeight(paraTroopaCapsuleWeight6)
    snackCapsuleWeight6 = calculateWeight(snackCapsuleWeight6)
    zapCapsuleWeight6 = calculateWeight(zapCapsuleWeight6)
    tweesterCapsuleWeight6 = calculateWeight(tweesterCapsuleWeight6)
    thwompCapsuleWeight6 = calculateWeight(thwompCapsuleWeight6)
    warpPipeCapsuleWeight6 = calculateWeight(warpPipeCapsuleWeight6)
    bombCapsuleWeight6 = calculateWeight(bombCapsuleWeight6)
    gaddLightCapsuleWeight6 = calculateWeight(gaddLightCapsuleWeight6)
    pinkBooCapsuleWeight6 = calculateWeight(pinkBooCapsuleWeight6)
    chanceTimeCapsuleWeight6 = calculateWeight(chanceTimeCapsuleWeight6)
    bowserCapsuleWeight6 = calculateWeight(bowserCapsuleWeight6)
    dkCapsuleWeight6 = calculateWeight(dkCapsuleWeight6)
    metalMushroomCapsuleWeight6 = calculateWeight(metalMushroomCapsuleWeight6)
    duelCapsuleWeight6 = calculateWeight(duelCapsuleWeight6)

    orbWeightTotal = mushroomCapsuleWeight6 + goldenMushroomCapsuleWeight6 + bulletBillCapsuleWeight6 + slowMushroomCapsuleWeight6 + warpPipeCapsuleWeight6 + flutterCapsuleWeight6 + cursedMushroomCapsuleWeight6 + spinyCapsuleWeight6 + goombaCapsuleWeight6 + plantCapsuleWeight6 + kleptoCapsuleWeight6 + kamekCapsuleWeight6 + toadyCapsuleWeight6 + blizzardCapsuleWeight6 + podobooCapsuleWeight6 + paraTroopaCapsuleWeight6 + snackCapsuleWeight6 + zapCapsuleWeight6 + tweesterCapsuleWeight6 + thwompCapsuleWeight6 + warpPipeCapsuleWeight6 + bombCapsuleWeight6 + gaddLightCapsuleWeight6 + pinkBooCapsuleWeight6 + chanceTimeCapsuleWeight6 + bowserCapsuleWeight6 + dkCapsuleWeight6 + metalMushroomCapsuleWeight6 + duelCapsuleWeight6

    if orbWeightTotal < 100:
        var_names = ['mushroomCapsuleWeight6', 'goldenMushroomCapsuleWeight6', 'bulletBillCapsuleWeight6', 'slowMushroomCapsuleWeight6', 'warpPipeCapsuleWeight6', 'flutterCapsuleWeight6', 'cursedMushroomCapsuleWeight6', 'spinyCapsuleWeight6', 'goombaCapsuleWeight6', 'plantCapsuleWeight6', 'kleptoCapsuleWeight6', 'kamekCapsuleWeight6', 'toadyCapsuleWeight6', 'blizzardCapsuleWeight6', 'podobooCapsuleWeight6', 'paraTroopaCapsuleWeight6', 'snackCapsuleWeight6', 'zapCapsuleWeight6', 'tweesterCapsuleWeight6', 'thwompCapsuleWeight6', 'warpPipeCapsuleWeight6', 'bombCapsuleWeight6', 'gaddLightCapsuleWeight6', 'pinkBooCapsuleWeight6', 'chanceTimeCapsuleWeight6', 'bowserCapsuleWeight6', 'dkCapsuleWeight6', 'metalMushroomCapsuleWeight6', 'duelCapsuleWeight6']
        max_var = max(zip(var_names, (map(eval, var_names))), key=lambda tuple: tuple[1])[0]

        if max_var == 'mushroomCapsuleWeight6':
            mushroomCapsuleWeight6 += (100 - orbWeightTotal)

        if max_var == 'goldenMushroomCapsuleWeight6':
            goldenMushroomCapsuleWeight6 += (100 - orbWeightTotal)

        if max_var == 'bulletBillCapsuleWeight6':
            bulletBillCapsuleWeight6 += (100 - orbWeightTotal)

        if max_var == 'slowMushroomCapsuleWeight6':
            slowMushroomCapsuleWeight6 += (100 - orbWeightTotal)

        if max_var == 'warpPipeCapsuleWeight6':
            warpPipeCapsuleWeight6 += (100 - orbWeightTotal)

        if max_var == 'flutterCapsuleWeight6':
            flutterCapsuleWeight6 += (100 - orbWeightTotal)

        if max_var == 'cursedMushroomCapsuleWeight6':
            cursedMushroomCapsuleWeight6 += (100 - orbWeightTotal)

        if max_var == 'spinyCapsuleWeight6':
            spinyCapsuleWeight6 += (100 - orbWeightTotal)

        if max_var == 'goombaCapsuleWeight6':
            goombaCapsuleWeight6 += (100 - orbWeightTotal)

        if max_var == 'plantCapsuleWeight6':
            plantCapsuleWeight6 += (100 - orbWeightTotal)

        if max_var == 'kleptoCapsuleWeight6':
            kleptoCapsuleWeight6 += (100 - orbWeightTotal)

        if max_var == 'kamekCapsuleWeight6':
            kamekCapsuleWeight6 += (100 - orbWeightTotal)

        if max_var == 'toadyCapsuleWeight6':
            toadyCapsuleWeight6 += (100 - orbWeightTotal)

        if max_var == 'blizzardCapsuleWeight6':
            blizzardCapsuleWeight6 += (100 - orbWeightTotal)

        if max_var == 'podobooCapsuleWeight6':
            podobooCapsuleWeight6 += (100 - orbWeightTotal)

        if max_var == 'paraTroopaCapsuleWeight6':
            paraTroopaCapsuleWeight6 += (100 - orbWeightTotal)

        if max_var == 'snackCapsuleWeight6':
            snackCapsuleWeight6 += (100 - orbWeightTotal)

        if max_var == 'zapCapsuleWeight6':
            zapCapsuleWeight6 += (100 - orbWeightTotal)

        if max_var == 'tweesterCapsuleWeight6':
            tweesterCapsuleWeight6 += (100 - orbWeightTotal)

        if max_var == 'thwompCapsuleWeight6':
            thwompCapsuleWeight6 += (100 - orbWeightTotal)

        if max_var == 'warpPipeCapsuleWeight6':
            warpPipeCapsuleWeight6 += (100 - orbWeightTotal)

        if max_var == 'bombCapsuleWeight6':
            bombCapsuleWeight6 += (100 - orbWeightTotal)

        if max_var == 'gaddLightCapsuleWeight6':
            gaddLightCapsuleWeight6 += (100 - orbWeightTotal)

        if max_var == 'pinkBooCapsulePrice6':
            pinkBooCapsulePrice6 += (100 - orbWeightTotal)

        if max_var == 'chanceTimeCapsuleWeight6':
            chanceTimeCapsuleWeight6 += (100 - orbWeightTotal)

        if max_var == 'bowserCapsuleWeight6':
            bowserCapsuleWeight6 += (100 - orbWeightTotal)

        if max_var == 'dkCapsuleWeight6':
            dkCapsuleWeight6 += (100 - orbWeightTotal)

        if max_var == 'metalMushroomCapsuleWeight6':
            metalMushroomCapsuleWeight6 += (100 - orbWeightTotal)

        if max_var == 'duelCapsuleWeight6':
            duelCapsuleWeight6 += (100 - orbWeightTotal)
    
    mushroomCapsuleWeight6 = str(mushroomCapsuleWeight6)
    goldenMushroomCapsuleWeight6 = str(goldenMushroomCapsuleWeight6)
    bulletBillCapsuleWeight6 = str(bulletBillCapsuleWeight6)
    slowMushroomCapsuleWeight6 = str(slowMushroomCapsuleWeight6)
    warpPipeCapsuleWeight6 = str(warpPipeCapsuleWeight6)
    flutterCapsuleWeight6 = str(flutterCapsuleWeight6)
    cursedMushroomCapsuleWeight6 = str(cursedMushroomCapsuleWeight6)
    spinyCapsuleWeight6 = str(spinyCapsuleWeight6)
    goombaCapsuleWeight6 = str(goombaCapsuleWeight6)
    plantCapsuleWeight6 = str(plantCapsuleWeight6)
    kleptoCapsuleWeight6 = str(kleptoCapsuleWeight6)
    kamekCapsuleWeight6 = str(kamekCapsuleWeight6)
    toadyCapsuleWeight6 = str(toadyCapsuleWeight6)
    blizzardCapsuleWeight6 = str(blizzardCapsuleWeight6)
    podobooCapsuleWeight6 = str(podobooCapsuleWeight6)
    paraTroopaCapsuleWeight6 = str(paraTroopaCapsuleWeight6)
    snackCapsuleWeight6 = str(snackCapsuleWeight6)
    zapCapsuleWeight6 = str(zapCapsuleWeight6)
    tweesterCapsuleWeight6 = str(tweesterCapsuleWeight6)
    thwompCapsuleWeight6 = str(thwompCapsuleWeight6)
    warpPipeCapsuleWeight6 = str(warpPipeCapsuleWeight6)
    bombCapsuleWeight6 = str(bombCapsuleWeight6)
    gaddLightCapsuleWeight6 = str(gaddLightCapsuleWeight6)
    pinkBooCapsuleWeight6 = str(pinkBooCapsuleWeight6)
    chanceTimeCapsuleWeight6 = str(chanceTimeCapsuleWeight6)
    bowserCapsuleWeight6 = str(bowserCapsuleWeight6)
    dkCapsuleWeight6 = str(dkCapsuleWeight6)
    metalMushroomCapsuleWeight6 = str(metalMushroomCapsuleWeight6)
    duelCapsuleWeight6 = str(duelCapsuleWeight6)

    try:
        mushroomCapsuleWeight6 = hex(int(mushroomCapsuleWeight6))
        if len(mushroomCapsuleWeight6) == 4:
            mushroomCapsuleWeight6 = mushroomCapsuleWeight6[2:]
        elif len(mushroomCapsuleWeight6) == 3:
            mushroomCapsuleWeight6 = "0" + mushroomCapsuleWeight6[2:]
    except:
        mushroomCapsuleWeight6 = "00"

    try:
        goldenMushroomCapsuleWeight6 = hex(int(goldenMushroomCapsuleWeight6))
        if len(goldenMushroomCapsuleWeight6) == 4:
            goldenMushroomCapsuleWeight6 = goldenMushroomCapsuleWeight6[2:]
        elif len(goldenMushroomCapsuleWeight6) == 3:
            goldenMushroomCapsuleWeight6 = "0" + goldenMushroomCapsuleWeight6[2:]
    except:
        goldenMushroomCapsuleWeight6 = "00"

    try:
        goldenMushroomCapsulePrice6 = hex(int(goldenMushroomCapsulePrice6))
        if len(goldenMushroomCapsulePrice6) == 4:
            goldenMushroomCapsulePrice6 = goldenMushroomCapsulePrice6[2:]
        elif len(goldenMushroomCapsulePrice6) == 3:
            goldenMushroomCapsulePrice6 = "0" + goldenMushroomCapsulePrice6[2:]
    except:
        goldenMushroomCapsulePrice6 = "00"
    
    try:
        slowMushroomCapsuleWeight6 = hex(int(slowMushroomCapsuleWeight6))
        if len(slowMushroomCapsuleWeight6) == 4:
            slowMushroomCapsuleWeight6 = slowMushroomCapsuleWeight6[2:]
        elif len(slowMushroomCapsuleWeight6) == 3:
            slowMushroomCapsuleWeight6 = "0" + slowMushroomCapsuleWeight6[2:]
    except:
        slowMushroomCapsuleWeight6 = "00"

    try:
        slowMushroomCapsulePrice6 = hex(int(slowMushroomCapsulePrice6))
        if len(slowMushroomCapsulePrice6) == 4:
            slowMushroomCapsulePrice6 = slowMushroomCapsulePrice6[2:]
        elif len(slowMushroomCapsulePrice6) == 3:
            slowMushroomCapsulePrice6 = "0" + slowMushroomCapsulePrice6[2:]
    except:
        slowMushroomCapsulePrice6 = "00"

    try:
        bulletBillCapsuleWeight6 = hex(int(bulletBillCapsuleWeight6))
        if len(bulletBillCapsuleWeight6) == 4:
            bulletBillCapsuleWeight6 = bulletBillCapsuleWeight6[2:]
        elif len(bulletBillCapsuleWeight6) == 3:
            bulletBillCapsuleWeight6 = "0" + bulletBillCapsuleWeight6[2:]
    except:
        bulletBillCapsuleWeight6 = "00"

    try:
        bulletBillCapsulePrice6 = hex(int(bulletBillCapsulePrice6))
        if len(bulletBillCapsulePrice6) == 4:
            bulletBillCapsulePrice6 = bulletBillCapsulePrice6[2:]
        elif len(bulletBillCapsulePrice6) == 3:
            bulletBillCapsulePrice6 = "0" + bulletBillCapsulePrice6[2:]
    except:
        bulletBillCapsulePrice6 = "00"

    try:
        warpPipeCapsuleWeight6 = hex(int(warpPipeCapsuleWeight6))
        if len(warpPipeCapsuleWeight6) == 4:
            warpPipeCapsuleWeight6 = warpPipeCapsuleWeight6[2:]
        elif len(warpPipeCapsuleWeight6) == 3:
            warpPipeCapsuleWeight6 = "0" + warpPipeCapsuleWeight6[2:]
    except:
        warpPipeCapsuleWeight6 = "00"

    try:
        warpPipeCapsulePrice6 = hex(int(warpPipeCapsulePrice6))
        if len(warpPipeCapsulePrice6) == 4:
            warpPipeCapsulePrice6 = warpPipeCapsulePrice6[2:]
        elif len(warpPipeCapsulePrice6) == 3:
            warpPipeCapsulePrice6 = "0" + warpPipeCapsulePrice6[2:]
    except:
        warpPipeCapsulePrice6 = "00"

    try:
        flutterCapsuleWeight6 = hex(int(flutterCapsuleWeight6))
        if len(flutterCapsuleWeight6) == 4:
            flutterCapsuleWeight6 = flutterCapsuleWeight6[2:]
        elif len(flutterCapsuleWeight6) == 3:
            flutterCapsuleWeight6 = "0" + flutterCapsuleWeight6[2:]
    except:
        flutterCapsuleWeight6 = "00"

    try:
        flutterCapsulePrice6 = hex(int(flutterCapsulePrice6))
        if len(flutterCapsulePrice6) == 4:
            flutterCapsulePrice6 = flutterCapsulePrice6[2:]
        elif len(flutterCapsulePrice6) == 3:
            flutterCapsulePrice6 = "0" + flutterCapsulePrice6[2:]
    except:
        flutterCapsulePrice6 = "00"

    try:
        cursedMushroomCapsuleWeight6 = hex(int(cursedMushroomCapsuleWeight6))
        if len(cursedMushroomCapsuleWeight6) == 4:
            cursedMushroomCapsuleWeight6 = cursedMushroomCapsuleWeight6[2:]
        elif len(cursedMushroomCapsuleWeight6) == 3:
            cursedMushroomCapsuleWeight6 = "0" + cursedMushroomCapsuleWeight6[2:]
    except:
        cursedMushroomCapsuleWeight6 = "00"

    try:
        cursedMushroomCapsulePrice6 = hex(int(cursedMushroomCapsulePrice6))
        if len(cursedMushroomCapsulePrice6) == 4:
            cursedMushroomCapsulePrice6 = cursedMushroomCapsulePrice6[2:]
        elif len(cursedMushroomCapsulePrice6) == 3:
            cursedMushroomCapsulePrice6 = "0" + cursedMushroomCapsulePrice6[2:]
    except:
        cursedMushroomCapsulePrice6 = "00"

    try:
        spinyCapsuleWeight6 = hex(int(spinyCapsuleWeight6))
        if len(spinyCapsuleWeight6) == 4:
            spinyCapsuleWeight6 = spinyCapsuleWeight6[2:]
        elif len(spinyCapsuleWeight6) == 3:
            spinyCapsuleWeight6 = "0" + spinyCapsuleWeight6[2:]
    except:
        spinyCapsuleWeight6 = "00"

    try:
        spinyCapsulePrice6 = hex(int(spinyCapsulePrice6))
        if len(spinyCapsulePrice6) == 4:
            spinyCapsulePrice6 = spinyCapsulePrice6[2:]
        elif len(spinyCapsulePrice6) == 3:
            spinyCapsulePrice6 = "0" + spinyCapsulePrice6[2:]
    except:
        spinyCapsulePrice6 = "00"

    try:
        goombaCapsuleWeight6 = hex(int(goombaCapsuleWeight6))
        if len(goombaCapsuleWeight6) == 4:
            goombaCapsuleWeight6 = goombaCapsuleWeight6[2:]
        elif len(goombaCapsuleWeight6) == 3:
            goombaCapsuleWeight6 = "0" + goombaCapsuleWeight6[2:]
    except:
        goombaCapsuleWeight6 = "00"

    try:
        goombaCapsulePrice6 = hex(int(goombaCapsulePrice6))
        if len(goombaCapsulePrice6) == 4:
            goombaCapsulePrice6 = goombaCapsulePrice6[2:]
        elif len(goombaCapsulePrice6) == 3:
            goombaCapsulePrice6 = "0" + goombaCapsulePrice6[2:]
    except:
        goombaCapsulePrice6 = "00"

    try:
        plantCapsuleWeight6 = hex(int(plantCapsuleWeight6))
        if len(plantCapsuleWeight6) == 4:
            plantCapsuleWeight6 = plantCapsuleWeight6[2:]
        elif len(plantCapsuleWeight6) == 3:
            plantCapsuleWeight6 = "0" + plantCapsuleWeight6[2:]
    except:
        plantCapsuleWeight6 = "00"

    try:
        plantCapsulePrice6 = hex(int(plantCapsulePrice6))
        if len(plantCapsulePrice6) == 4:
            plantCapsulePrice6 = plantCapsulePrice6[2:]
        elif len(plantCapsulePrice6) == 3:
            plantCapsulePrice6 = "0" + plantCapsulePrice6[2:]
    except:
        plantCapsulePrice6 = "00"

    try:
        kleptoCapsuleWeight6 = hex(int(kleptoCapsuleWeight6))
        if len(kleptoCapsuleWeight6) == 4:
            kleptoCapsuleWeight6 = kleptoCapsuleWeight6[2:]
        elif len(kleptoCapsuleWeight6) == 3:
            kleptoCapsuleWeight6 = "0" + kleptoCapsuleWeight6[2:]
    except:
        kleptoCapsuleWeight6 = "00"

    try:
        kleptoCapsulePrice6 = hex(int(kleptoCapsulePrice6))
        if len(kleptoCapsulePrice6) == 4:
            kleptoCapsulePrice6 = kleptoCapsulePrice6[2:]
        elif len(kleptoCapsulePrice6) == 3:
            kleptoCapsulePrice6 = "0" + kleptoCapsulePrice6[2:]
    except:
        kleptoCapsulePrice6 = "00"

    try:
        kamekCapsuleWeight6 = hex(int(kamekCapsuleWeight6))
        if len(kamekCapsuleWeight6) == 4:
            kamekCapsuleWeight6 = kamekCapsuleWeight6[2:]
        elif len(kamekCapsuleWeight6) == 3:
            kamekCapsuleWeight6 = "0" + kamekCapsuleWeight6[2:]
    except:
        kamekCapsuleWeight6 = "00"

    try:
        kamekCapsulePrice6 = hex(int(kamekCapsulePrice6))
        if len(kamekCapsulePrice6) == 4:
            kamekCapsulePrice6 = kamekCapsulePrice6[2:]
        elif len(kamekCapsulePrice6) == 3:
            kamekCapsulePrice6 = "0" + kamekCapsulePrice6[2:]
    except:
        kamekCapsulePrice6 = "00"

    try:
        toadyCapsuleWeight6 = hex(int(toadyCapsuleWeight6))
        if len(toadyCapsuleWeight6) == 4:
            toadyCapsuleWeight6 = toadyCapsuleWeight6[2:]
        elif len(toadyCapsuleWeight6) == 3:
            toadyCapsuleWeight6 = "0" + toadyCapsuleWeight6[2:]
    except:
        toadyCapsuleWeight6 = "00"

    try:
        toadyCapsulePrice6 = hex(int(toadyCapsulePrice6))
        if len(toadyCapsulePrice6) == 4:
            toadyCapsulePrice6 = toadyCapsulePrice6[2:]
        elif len(toadyCapsulePrice6) == 3:
            toadyCapsulePrice6 = "0" + toadyCapsulePrice6[2:]
    except:
        toadyCapsulePrice6 = "00"

    try:
        blizzardCapsuleWeight6 = hex(int(blizzardCapsuleWeight6))
        if len(blizzardCapsuleWeight6) == 4:
            blizzardCapsuleWeight6 = blizzardCapsuleWeight6[2:]
        elif len(blizzardCapsuleWeight6) == 3:
            blizzardCapsuleWeight6 = "0" + blizzardCapsuleWeight6[2:]
    except:
        blizzardCapsuleWeight6 = "00"

    try:
        blizzardCapsulePrice6 = hex(int(blizzardCapsulePrice6))
        if len(blizzardCapsulePrice6) == 4:
            blizzardCapsulePrice6 = blizzardCapsulePrice6[2:]
        elif len(blizzardCapsulePrice6) == 3:
            blizzardCapsulePrice6 = "0" + blizzardCapsulePrice6[2:]
    except:
        blizzardCapsulePrice6 = "00"

    try:
        podobooCapsuleWeight6 = hex(int(podobooCapsuleWeight6))
        if len(podobooCapsuleWeight6) == 4:
            podobooCapsuleWeight6 = podobooCapsuleWeight6[2:]
        elif len(podobooCapsuleWeight6) == 3:
            podobooCapsuleWeight6 = "0" + podobooCapsuleWeight6[2:]
    except:
        podobooCapsuleWeight6 = "00"

    try:
        podobooCapsulePrice6 = hex(int(podobooCapsulePrice6))
        if len(podobooCapsulePrice6) == 4:
            podobooCapsulePrice6 = podobooCapsulePrice6[2:]
        elif len(podobooCapsulePrice6) == 3:
            podobooCapsulePrice6 = "0" + podobooCapsulePrice6[2:]
    except:
        podobooCapsulePrice6 = "00"

    try:
        paraTroopaCapsuleWeight6 = hex(int(paraTroopaCapsuleWeight6))
        if len(paraTroopaCapsuleWeight6) == 4:
            paraTroopaCapsuleWeight6 = paraTroopaCapsuleWeight6[2:]
        elif len(paraTroopaCapsuleWeight6) == 3:
            paraTroopaCapsuleWeight6 = "0" + paraTroopaCapsuleWeight6[2:]
    except:
        paraTroopaCapsuleWeight6 = "00"

    try:
        paraTroopaCapsulePrice6 = hex(int(paraTroopaCapsulePrice6))
        if len(paraTroopaCapsulePrice6) == 4:
            paraTroopaCapsulePrice6 = paraTroopaCapsulePrice6[2:]
        elif len(paraTroopaCapsulePrice6) == 3:
            paraTroopaCapsulePrice6 = "0" + paraTroopaCapsulePrice6[2:]
    except:
        paraTroopaCapsulePrice6 = "00"

    try:
        snackCapsuleWeight6 = hex(int(snackCapsuleWeight6))
        if len(snackCapsuleWeight6) == 4:
            snackCapsuleWeight6 = snackCapsuleWeight6[2:]
        elif len(snackCapsuleWeight6) == 3:
            snackCapsuleWeight6 = "0" + snackCapsuleWeight6[2:]
    except:
        snackCapsuleWeight6 = "00"

    try:
        snackCapsulePrice6 = hex(int(snackCapsulePrice6))
        if len(snackCapsulePrice6) == 4:
            snackCapsulePrice6 = snackCapsulePrice6[2:]
        elif len(snackCapsulePrice6) == 3:
            snackCapsulePrice6 = "0" + snackCapsulePrice6[2:]
    except:
        snackCapsulePrice6 = "00"

    try:
        zapCapsuleWeight6 = hex(int(zapCapsuleWeight6))
        if len(zapCapsuleWeight6) == 4:
            zapCapsuleWeight6 = zapCapsuleWeight6[2:]
        elif len(zapCapsuleWeight6) == 3:
            zapCapsuleWeight6 = "0" + zapCapsuleWeight6[2:]
    except:
        zapCapsuleWeight6 = "00"

    try:
        zapCapsulePrice6 = hex(int(zapCapsulePrice6))
        if len(zapCapsulePrice6) == 4:
            zapCapsulePrice6 = zapCapsulePrice6[2:]
        elif len(zapCapsulePrice6) == 3:
            zapCapsulePrice6 = "0" + zapCapsulePrice6[2:]
    except:
        zapCapsulePrice6 = "00"

    try:
        tweesterCapsuleWeight6 = hex(int(tweesterCapsuleWeight6))
        if len(tweesterCapsuleWeight6) == 4:
            tweesterCapsuleWeight6 = tweesterCapsuleWeight6[2:]
        elif len(tweesterCapsuleWeight6) == 3:
            tweesterCapsuleWeight6 = "0" + tweesterCapsuleWeight6[2:]
    except:
        tweesterCapsuleWeight6 = "00"

    try:
        tweesterCapsulePrice6 = hex(int(tweesterCapsulePrice6))
        if len(tweesterCapsulePrice6) == 4:
            tweesterCapsulePrice6 = tweesterCapsulePrice6[2:]
        elif len(tweesterCapsulePrice6) == 3:
            tweesterCapsulePrice6 = "0" + tweesterCapsulePrice6[2:]
    except:
        tweesterCapsulePrice6 = "00"

    try:
        thwompCapsuleWeight6 = hex(int(thwompCapsuleWeight6))
        if len(thwompCapsuleWeight6) == 4:
            thwompCapsuleWeight6 = thwompCapsuleWeight6[2:]
        elif len(thwompCapsuleWeight6) == 3:
            thwompCapsuleWeight6 = "0" + thwompCapsuleWeight6[2:]
    except:
        thwompCapsuleWeight6 = "00"

    try:
        thwompCapsulePrice6 = hex(int(thwompCapsulePrice6))
        if len(thwompCapsulePrice6) == 4:
            thwompCapsulePrice6 = thwompCapsulePrice6[2:]
        elif len(thwompCapsulePrice6) == 3:
            thwompCapsulePrice6 = "0" + thwompCapsulePrice6[2:]
    except:
        thwompCapsulePrice6 = "00"


    try:
        warpPipeCapsuleWeight6 = hex(int(warpPipeCapsuleWeight6))
        if len(warpPipeCapsuleWeight6) == 4:
            warpPipeCapsuleWeight6 = warpPipeCapsuleWeight6[2:]
        elif len(warpPipeCapsuleWeight6) == 3:
            warpPipeCapsuleWeight6 = "0" + warpPipeCapsuleWeight6[2:]
    except:
        warpPipeCapsuleWeight6 = "00"

    try:
        warpPipeCapsulePrice6 = hex(int(warpPipeCapsulePrice6))
        if len(warpPipeCapsulePrice6) == 4:
            warpPipeCapsulePrice6 = warpPipeCapsulePrice6[2:]
        elif len(warpPipeCapsulePrice6) == 3:
            warpPipeCapsulePrice6 = "0" + warpPipeCapsulePrice6[2:]
    except:
        warpPipeCapsulePrice6 = "00"

    try:
        bombCapsuleWeight6 = hex(int(bombCapsuleWeight6))
        if len(bombCapsuleWeight6) == 4:
            bombCapsuleWeight6 = bombCapsuleWeight6[2:]
        elif len(bombCapsuleWeight6) == 3:
            bombCapsuleWeight6 = "0" + bombCapsuleWeight6[2:]
    except:
        bombCapsuleWeight6 = "00"

    try:
        bombCapsulePrice6 = hex(int(bombCapsulePrice6))
        if len(bombCapsulePrice6) == 4:
            bombCapsulePrice6 = bombCapsulePrice6[2:]
        elif len(bombCapsulePrice6) == 3:
            bombCapsulePrice6 = "0" + bombCapsulePrice6[2:]
    except:
        bombCapsulePrice6 = "00"

    try:
        gaddLightCapsuleWeight6 = hex(int(gaddLightCapsuleWeight6))
        if len(gaddLightCapsuleWeight6) == 4:
            gaddLightCapsuleWeight6 = gaddLightCapsuleWeight6[2:]
        elif len(gaddLightCapsuleWeight6) == 3:
            gaddLightCapsuleWeight6 = "0" + gaddLightCapsuleWeight6[2:]
    except:
        gaddLightCapsuleWeight6 = "00"

    try:
        gaddLightCapsulePrice6 = hex(int(gaddLightCapsulePrice6))
        if len(gaddLightCapsulePrice6) == 4:
            gaddLightCapsulePrice6 = gaddLightCapsulePrice6[2:]
        elif len(gaddLightCapsulePrice6) == 3:
            gaddLightCapsulePrice6 = "0" + gaddLightCapsulePrice6[2:]
    except:
        gaddLightCapsulePrice6 = "00"

    try:
        pinkBooCapsuleWeight6 = hex(int(pinkBooCapsuleWeight6))
        if len(pinkBooCapsuleWeight6) == 4:
            pinkBooCapsuleWeight6 = pinkBooCapsuleWeight6[2:]
        elif len(pinkBooCapsuleWeight6) == 3:
            pinkBooCapsuleWeight6 = "0" + pinkBooCapsuleWeight6[2:]
    except:
        pinkBooCapsuleWeight6 = "00"

    try:
        pinkBooCapsulePrice6 = hex(int(pinkBooCapsulePrice6))
        if len(pinkBooCapsulePrice6) == 4:
            pinkBooCapsulePrice6 = pinkBooCapsulePrice6[2:]
        elif len(pinkBooCapsulePrice6) == 3:
            pinkBooCapsulePrice6 = "0" + pinkBooCapsulePrice6[2:]
    except:
        pinkBooCapsulePrice6 = "00"

    try:
        chanceTimeCapsuleWeight6 = hex(int(chanceTimeCapsuleWeight6))
        if len(chanceTimeCapsuleWeight6) == 4:
            chanceTimeCapsuleWeight6 = chanceTimeCapsuleWeight6[2:]
        elif len(chanceTimeCapsuleWeight6) == 3:
            chanceTimeCapsuleWeight6 = "0" + chanceTimeCapsuleWeight6[2:]
    except:
        chanceTimeCapsuleWeight6 = "00"

    try:
        chanceTimeCapsulePrice6 = hex(int(chanceTimeCapsulePrice6))
        if len(chanceTimeCapsulePrice6) == 4:
            chanceTimeCapsulePrice6 = chanceTimeCapsulePrice6[2:]
        elif len(chanceTimeCapsulePrice6) == 3:
            chanceTimeCapsulePrice6 = "0" + chanceTimeCapsulePrice6[2:]
    except:
        chanceTimeCapsulePrice6 = "00"

    try:
        bowserCapsuleWeight6 = hex(int(bowserCapsuleWeight6))
        if len(bowserCapsuleWeight6) == 4:
            bowserCapsuleWeight6 = bowserCapsuleWeight6[2:]
        elif len(bowserCapsuleWeight6) == 3:
            bowserCapsuleWeight6 = "0" + bowserCapsuleWeight6[2:]
    except:
        bowserCapsuleWeight6 = "00"

    try:
        bowserCapsulePrice6 = hex(int(bowserCapsulePrice6))
        if len(bowserCapsulePrice6) == 4:
            bowserCapsulePrice6 = bowserCapsulePrice6[2:]
        elif len(bowserCapsulePrice6) == 3:
            bowserCapsulePrice6 = "0" + bowserCapsulePrice6[2:]
    except:
        bowserCapsulePrice6 = "00"

    try:
        dkCapsuleWeight6 = hex(int(dkCapsuleWeight6))
        if len(dkCapsuleWeight6) == 4:
            dkCapsuleWeight6 = dkCapsuleWeight6[2:]
        elif len(dkCapsuleWeight6) == 3:
            dkCapsuleWeight6 = "0" + dkCapsuleWeight6[2:]
    except:
        dkCapsuleWeight6 = "00"

    try:
        dkCapsulePrice6 = hex(int(dkCapsulePrice6))
        if len(dkCapsulePrice6) == 4:
            dkCapsulePrice6 = dkCapsulePrice6[2:]
        elif len(dkCapsulePrice6) == 3:
            dkCapsulePrice6 = "0" + dkCapsulePrice6[2:]
    except:
        dkCapsulePrice6 = "00"

    try:
        metalMushroomCapsuleWeight6 = hex(int(metalMushroomCapsuleWeight6))
        if len(metalMushroomCapsuleWeight6) == 4:
            metalMushroomCapsuleWeight6 = metalMushroomCapsuleWeight6[2:]
        elif len(metalMushroomCapsuleWeight6) == 3:
            metalMushroomCapsuleWeight6 = "0" + metalMushroomCapsuleWeight6[2:]
    except:
        metalMushroomCapsuleWeight6 = "00"

    try:
        metalMushroomCapsulePrice6 = hex(int(metalMushroomCapsulePrice6))
        if len(metalMushroomCapsulePrice6) == 4:
            metalMushroomCapsulePrice6 = metalMushroomCapsulePrice6[2:]
        elif len(metalMushroomCapsulePrice6) == 3:
            metalMushroomCapsulePrice6 = "0" + metalMushroomCapsulePrice6[2:]
    except:
        metalMushroomCapsulePrice6 = "00"

    try:
        duelCapsuleWeight6 = hex(int(duelCapsuleWeight6))
        if len(duelCapsuleWeight6) == 4:
            duelCapsuleWeight6 = duelCapsuleWeight6[2:]
        elif len(duelCapsuleWeight6) == 3:
            duelCapsuleWeight6 = "0" + duelCapsuleWeight6[2:]
    except:
        duelCapsuleWeight6 = "00"

    try:
        duelCapsulePrice6 = hex(int(duelCapsulePrice6))
        if len(duelCapsulePrice6) == 4:
            duelCapsulePrice6 = duelCapsulePrice6[2:]
        elif len(duelCapsulePrice6) == 3:
            duelCapsulePrice6 = "0" + duelCapsulePrice6[2:]
    except:
        duelCapsulePrice6 = "00"

    generatedCode = getOrbModsSix(mushroomCapsuleWeight6, goldenMushroomCapsulePrice6, goldenMushroomCapsuleWeight6, slowMushroomCapsulePrice6, slowMushroomCapsuleWeight6, metalMushroomCapsulePrice6, metalMushroomCapsuleWeight6, bulletBillCapsulePrice6, bulletBillCapsuleWeight6, warpPipeCapsulePrice6, warpPipeCapsuleWeight6, flutterCapsulePrice6, flutterCapsuleWeight6, cursedMushroomCapsulePrice6, cursedMushroomCapsuleWeight6, spinyCapsulePrice6, spinyCapsuleWeight6, goombaCapsulePrice6, goombaCapsuleWeight6, plantCapsulePrice6, plantCapsuleWeight6, kleptoCapsulePrice6, kleptoCapsuleWeight6, toadyCapsulePrice6, toadyCapsuleWeight6, kamekCapsulePrice6, kamekCapsuleWeight6, blizzardCapsulePrice6, blizzardCapsuleWeight6, podobooCapsulePrice6, podobooCapsuleWeight6, zapCapsulePrice6, zapCapsuleWeight6, tweesterCapsulePrice6, tweesterCapsuleWeight6, thwompCapsulePrice6, thwompCapsuleWeight6, bombCapsulePrice6, bombCapsuleWeight6, paraTroopaCapsulePrice6, paraTroopaCapsuleWeight6, snackCapsulePrice6, snackCapsuleWeight6, gaddLightCapsulePrice6, gaddLightCapsuleWeight6, pinkBooCapsulePrice6, pinkBooCapsuleWeight6, chanceTimeCapsulePrice6, chanceTimeCapsuleWeight6, bowserCapsulePrice6, bowserCapsuleWeight6, dkCapsulePrice6, dkCapsuleWeight6, duelCapsulePrice6, duelCapsuleWeight6)
    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)

    print("Generated code copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

def savePresetItems6(warpPipeCapsuleWeight6, warpPipeCapsulePrice6, mushroomCapsuleWeight6, goldenMushroomCapsulePrice6, goldenMushroomCapsuleWeight6, slowMushroomCapsulePrice6, slowMushroomCapsuleWeight6, metalMushroomCapsulePrice6, metalMushroomCapsuleWeight6, bulletBillCapsulePrice6, bulletBillCapsuleWeight6, flutterCapsulePrice6, flutterCapsuleWeight6, cursedMushroomCapsulePrice6, cursedMushroomCapsuleWeight6, spinyCapsulePrice6, spinyCapsuleWeight6, goombaCapsulePrice6, goombaCapsuleWeight6, plantCapsulePrice6, plantCapsuleWeight6, kleptoCapsulePrice6, kleptoCapsuleWeight6, toadyCapsulePrice6, toadyCapsuleWeight6, kamekCapsulePrice6, kamekCapsuleWeight6, blizzardCapsulePrice6, blizzardCapsuleWeight6, podobooCapsulePrice6, podobooCapsuleWeight6, zapCapsulePrice6, zapCapsuleWeight6, tweesterCapsulePrice6, tweesterCapsuleWeight6, thwompCapsulePrice6, thwompCapsuleWeight6, bombCapsulePrice6, bombCapsuleWeight6, paraTroopaCapsulePrice6, paraTroopaCapsuleWeight6, snackCapsulePrice6, snackCapsuleWeight6, gaddLightCapsulePrice6, gaddLightCapsuleWeight6, pinkBooCapsulePrice6, pinkBooCapsuleWeight6, chanceTimeCapsulePrice6, chanceTimeCapsuleWeight6, bowserCapsulePrice6, bowserCapsuleWeight6, dkCapsulePrice6, dkCapsuleWeight6, duelCapsulePrice6, duelCapsuleWeight6):
    if not metalMushroomCapsulePrice6.get() or not metalMushroomCapsuleWeight6.get() or not mushroomCapsuleWeight6.get() or not goldenMushroomCapsulePrice6.get() or not goldenMushroomCapsuleWeight6.get() or not slowMushroomCapsulePrice6.get() or not slowMushroomCapsuleWeight6.get() or not bulletBillCapsulePrice6.get() or not bulletBillCapsuleWeight6.get() or not warpPipeCapsulePrice6.get() or not warpPipeCapsuleWeight6.get() or not flutterCapsulePrice6.get() or not flutterCapsuleWeight6.get() or not cursedMushroomCapsulePrice6.get() or not cursedMushroomCapsuleWeight6.get() or not spinyCapsulePrice6.get() or not spinyCapsuleWeight6.get() or not goombaCapsuleWeight6.get() or not goombaCapsulePrice6.get() or not plantCapsulePrice6.get() or not plantCapsuleWeight6.get() or not kleptoCapsuleWeight6.get() or not kleptoCapsulePrice6.get() or not kamekCapsuleWeight6.get() or not kamekCapsulePrice6.get() or not toadyCapsuleWeight6.get() or not toadyCapsulePrice6.get() or not blizzardCapsuleWeight6.get() or not blizzardCapsulePrice6.get() or not podobooCapsulePrice6.get() or not podobooCapsuleWeight6.get() or not paraTroopaCapsuleWeight6.get() or not paraTroopaCapsulePrice6.get() or not snackCapsulePrice6.get() or not snackCapsuleWeight6.get() or not zapCapsulePrice6.get() or not zapCapsuleWeight6.get() or not tweesterCapsulePrice6.get() or not tweesterCapsuleWeight6.get() or not thwompCapsulePrice6.get() or not thwompCapsuleWeight6.get() or not warpPipeCapsulePrice6.get() or not warpPipeCapsuleWeight6.get() or not bombCapsulePrice6.get() or not bombCapsuleWeight6.get() or not gaddLightCapsulePrice6.get() or not gaddLightCapsuleWeight6.get():
        createDialog("Error", "error", "Please fill out all the boxes.", None)
        return
    
    mushroomCapsuleWeight6 = mushroomCapsuleWeight6.get()
    
    goldenMushroomCapsulePrice6 = goldenMushroomCapsulePrice6.get()
    goldenMushroomCapsuleWeight6 = goldenMushroomCapsuleWeight6.get()
    slowMushroomCapsulePrice6 = slowMushroomCapsulePrice6.get()
    slowMushroomCapsuleWeight6 = slowMushroomCapsuleWeight6.get()
    metalMushroomCapsulePrice6 = metalMushroomCapsulePrice6.get()
    metalMushroomCapsuleWeight6 = metalMushroomCapsuleWeight6.get()
    bulletBillCapsulePrice6 = bulletBillCapsulePrice6.get()
    bulletBillCapsuleWeight6 = bulletBillCapsuleWeight6.get()
    flutterCapsulePrice6 = flutterCapsulePrice6.get()
    flutterCapsuleWeight6 = flutterCapsuleWeight6.get()
    cursedMushroomCapsulePrice6 = cursedMushroomCapsulePrice6.get()
    cursedMushroomCapsuleWeight6 = cursedMushroomCapsuleWeight6.get()
    spinyCapsulePrice6 = spinyCapsulePrice6.get()
    spinyCapsuleWeight6 = spinyCapsuleWeight6.get()
    goombaCapsulePrice6 = goombaCapsulePrice6.get()
    goombaCapsuleWeight6 = goombaCapsuleWeight6.get()
    plantCapsulePrice6 = plantCapsulePrice6.get()
    plantCapsuleWeight6 = plantCapsuleWeight6.get()
    kleptoCapsulePrice6 = kleptoCapsulePrice6.get()
    kleptoCapsuleWeight6 = kleptoCapsuleWeight6.get()
    kamekCapsulePrice6 = kamekCapsulePrice6.get()
    kamekCapsuleWeight6 = kamekCapsuleWeight6.get()
    toadyCapsulePrice6 = toadyCapsulePrice6.get()
    toadyCapsuleWeight6 = toadyCapsuleWeight6.get()
    blizzardCapsulePrice6 = blizzardCapsulePrice6.get()
    blizzardCapsuleWeight6 = blizzardCapsuleWeight6.get()
    podobooCapsulePrice6 = podobooCapsulePrice6.get()
    podobooCapsuleWeight6 = podobooCapsuleWeight6.get()
    paraTroopaCapsulePrice6 = paraTroopaCapsulePrice6.get()
    paraTroopaCapsuleWeight6 = paraTroopaCapsuleWeight6.get()
    snackCapsulePrice6 = snackCapsulePrice6.get()
    snackCapsuleWeight6 = snackCapsuleWeight6.get()
    zapCapsulePrice6 = zapCapsulePrice6.get()
    zapCapsuleWeight6 = zapCapsuleWeight6.get()
    tweesterCapsulePrice6 = tweesterCapsulePrice6.get()
    tweesterCapsuleWeight6 = tweesterCapsuleWeight6.get()
    thwompCapsulePrice6 = thwompCapsulePrice6.get()
    thwompCapsuleWeight6 = thwompCapsuleWeight6.get()
    warpPipeCapsulePrice6 = warpPipeCapsulePrice6.get()
    warpPipeCapsuleWeight6 = warpPipeCapsuleWeight6.get()
    bombCapsulePrice6 = bombCapsulePrice6.get()
    bombCapsuleWeight6 = bombCapsuleWeight6.get()
    gaddLightCapsulePrice6 = gaddLightCapsulePrice6.get()
    gaddLightCapsuleWeight6 = gaddLightCapsuleWeight6.get()
    
    try:
        pinkBooCapsulePrice6 = pinkBooCapsulePrice6.get()
    except:
        pinkBooCapsulePrice6 = 00

    try:
        pinkBooCapsuleWeight6 = pinkBooCapsuleWeight6.get()
    except:
        pinkBooCapsuleWeight6 = 00

    try:
        chanceTimeCapsulePrice6 = chanceTimeCapsulePrice6.get()
    except:
        chanceTimeCapsulePrice6 = 00

    try:
        chanceTimeCapsuleWeight6 = chanceTimeCapsuleWeight6.get()
    except:
        chanceTimeCapsuleWeight6 = 00

    try:
        bowserCapsulePrice6 = bowserCapsulePrice6.get()
    except:
        bowserCapsulePrice6 = 00

    try:
        bowserCapsuleWeight6 = bowserCapsuleWeight6.get()
    except:
        bowserCapsuleWeight6 = 00

    try:
        dkCapsulePrice6 = dkCapsulePrice6.get()
    except:
        dkCapsulePrice6 = 00

    try:
        dkCapsuleWeight6 = dkCapsuleWeight6.get()
    except:
        dkCapsuleWeight6 = 00

    try:
        duelCapsulePrice6 = duelCapsulePrice6.get()
    except:
        duelCapsulePrice6 = 00

    try:
        duelCapsuleWeight6 = duelCapsuleWeight6.get()
    except:
        duelCapsuleWeight6 = 00

    prices6 = ["5", goldenMushroomCapsulePrice6, slowMushroomCapsulePrice6, metalMushroomCapsulePrice6, bulletBillCapsulePrice6, flutterCapsulePrice6, cursedMushroomCapsulePrice6, spinyCapsulePrice6, goombaCapsulePrice6, plantCapsulePrice6, kleptoCapsulePrice6, kamekCapsulePrice6, toadyCapsulePrice6, blizzardCapsulePrice6, podobooCapsulePrice6, paraTroopaCapsulePrice6, snackCapsulePrice6, zapCapsulePrice6, tweesterCapsulePrice6, thwompCapsulePrice6, warpPipeCapsulePrice6, bombCapsulePrice6, gaddLightCapsulePrice6, pinkBooCapsulePrice6, chanceTimeCapsulePrice6, bowserCapsulePrice6, dkCapsulePrice6, duelCapsulePrice6]
    weights6 = [mushroomCapsuleWeight6, goldenMushroomCapsuleWeight6, slowMushroomCapsuleWeight6, metalMushroomCapsuleWeight6, bulletBillCapsuleWeight6, flutterCapsuleWeight6, cursedMushroomCapsuleWeight6, spinyCapsuleWeight6, goombaCapsuleWeight6, plantCapsuleWeight6, kleptoCapsuleWeight6, kamekCapsuleWeight6, toadyCapsuleWeight6, blizzardCapsuleWeight6, podobooCapsuleWeight6, paraTroopaCapsuleWeight6, snackCapsuleWeight6, zapCapsuleWeight6, tweesterCapsuleWeight6, thwompCapsuleWeight6, warpPipeCapsuleWeight6, bombCapsuleWeight6, gaddLightCapsuleWeight6, pinkBooCapsuleWeight6, chanceTimeCapsuleWeight6, bowserCapsuleWeight6, dkCapsuleWeight6, duelCapsuleWeight6]
    file_path = tkinter.filedialog.asksaveasfilename(defaultextension=".mpt", filetypes=[("MPT files", "*.mpt")])
    if file_path:
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Prices', 'Weights'])
            for price, weight in zip(prices6, weights6):
                writer.writerow([price, weight])
        print("MPT file saved successfully!")
        createDialog("Operation Sucessful", "success", "Presets file saved successfully!.", None)

def loadPresetItems6(warpPipeCapsuleWeight6, warpPipeCapsulePrice6, mushroomCapsuleWeight6, goldenMushroomCapsulePrice6, goldenMushroomCapsuleWeight6, slowMushroomCapsulePrice6, slowMushroomCapsuleWeight6, metalMushroomCapsulePrice6, metalMushroomCapsuleWeight6, bulletBillCapsulePrice6, bulletBillCapsuleWeight6, flutterCapsulePrice6, flutterCapsuleWeight6, cursedMushroomCapsulePrice6, cursedMushroomCapsuleWeight6, spinyCapsulePrice6, spinyCapsuleWeight6, goombaCapsulePrice6, goombaCapsuleWeight6, plantCapsulePrice6, plantCapsuleWeight6, kleptoCapsulePrice6, kleptoCapsuleWeight6, toadyCapsulePrice6, toadyCapsuleWeight6, kamekCapsulePrice6, kamekCapsuleWeight6, blizzardCapsulePrice6, blizzardCapsuleWeight6, podobooCapsulePrice6, podobooCapsuleWeight6, zapCapsulePrice6, zapCapsuleWeight6, tweesterCapsulePrice6, tweesterCapsuleWeight6, thwompCapsulePrice6, thwompCapsuleWeight6, bombCapsulePrice6, bombCapsuleWeight6, paraTroopaCapsulePrice6, paraTroopaCapsuleWeight6, snackCapsulePrice6, snackCapsuleWeight6, gaddLightCapsulePrice6, gaddLightCapsuleWeight6, pinkBooCapsulePrice6, pinkBooCapsuleWeight6, chanceTimeCapsulePrice6, chanceTimeCapsuleWeight6, bowserCapsulePrice6, bowserCapsuleWeight6, dkCapsulePrice6, dkCapsuleWeight6, duelCapsulePrice6, duelCapsuleWeight6):
    file_path = tkinter.filedialog.askopenfilename(defaultextension=".mpt", filetypes=[("MPT files", "*.mpt")])
    if file_path:
        prices6In = []
        weights6In = []
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                prices6In.append(float(row[0]))
                weights6In.append(float(row[1]))
        testVar = ""
        # Define a list of Entry widget attributes
        pricesNames6 = [testVar, goldenMushroomCapsulePrice6, slowMushroomCapsulePrice6, metalMushroomCapsulePrice6, bulletBillCapsulePrice6, flutterCapsulePrice6, cursedMushroomCapsulePrice6, spinyCapsulePrice6, goombaCapsulePrice6, plantCapsulePrice6, kleptoCapsulePrice6, kamekCapsulePrice6, toadyCapsulePrice6, blizzardCapsulePrice6, podobooCapsulePrice6, paraTroopaCapsulePrice6, snackCapsulePrice6, zapCapsulePrice6, tweesterCapsulePrice6, thwompCapsulePrice6, warpPipeCapsulePrice6, bombCapsulePrice6, gaddLightCapsulePrice6, pinkBooCapsulePrice6, chanceTimeCapsulePrice6, bowserCapsulePrice6, dkCapsulePrice6, duelCapsulePrice6]
        weightsNames6 = [mushroomCapsuleWeight6, goldenMushroomCapsuleWeight6, slowMushroomCapsuleWeight6, metalMushroomCapsuleWeight6, bulletBillCapsuleWeight6, flutterCapsuleWeight6, cursedMushroomCapsuleWeight6, spinyCapsuleWeight6, goombaCapsuleWeight6, plantCapsuleWeight6, kleptoCapsuleWeight6, kamekCapsuleWeight6, toadyCapsuleWeight6, blizzardCapsuleWeight6, podobooCapsuleWeight6, paraTroopaCapsuleWeight6, snackCapsuleWeight6, zapCapsuleWeight6, tweesterCapsuleWeight6, thwompCapsuleWeight6, warpPipeCapsuleWeight6, bombCapsuleWeight6, gaddLightCapsuleWeight6, pinkBooCapsuleWeight6, chanceTimeCapsuleWeight6, bowserCapsuleWeight6, dkCapsuleWeight6, duelCapsuleWeight6]

        # Update widgets with loaded values
        for index, widget in enumerate(pricesNames6):
            try:
                if widget and index < len(prices6In):
                    widget.delete(0, 'end')
                    widget.insert(0, int(prices6In[index]))
            except AttributeError:
                pricesNames6[index] = "0"
        
        for index, widget in enumerate(weightsNames6):
            try:
                if widget and index < len(weights6In):
                    widget.delete(0, 'end')
                    widget.insert(0, int(weights6In[index]))
            except AttributeError:
                weightsNames6[index] = "0"
        
        print("MPT file loaded successfully!")
        createDialog("Operation Successful", "success", "Presets file loaded successfully!", None)