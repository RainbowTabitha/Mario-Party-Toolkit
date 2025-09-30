# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

from codes.marioParty5 import *
from functions import *

import csv
import math
import pyperclip

def itemsEvent_mp5(bombCapsulePrice5 = "0", bombCapsuleWeight5 = "0", koopaBankCapsulePrice5 = "0", koopaBankCapsuleWeight5 = "0", bulletBillCapsulePrice5 = "0", bulletBillCapsuleWeight5 = "0", hammerBroCapsulePrice5 = "0", hammerBroCapsuleWeight5 = "0", coinBlockCapsulePrice5 = "0", coinBlockCapsuleWeight5 = "0", duelCapsulePrice5 = "0", duelCapsuleWeight5 = "0", mushroomCapsulePrice5 = "0", mushroomCapsuleWeight5 = "0", goldenMushroomCapsulePrice5 = "0", goldenMushroomCapsuleWeight5 = "0", cursedMushroomCapsulePrice5 = "0", cursedMushroomCapsuleWeight5 = "0", flutterCapsulePrice5 = "0", flutterCapsuleWeight5 = "0", spinyCapsulePrice5 = "0", spinyCapsuleWeight5 = "0", goombaCapsuleWeight5 = "0", goombaCapsulePrice5 = "0", plantCapsulePrice5 = "0", plantCapsuleWeight5 = "0", kleptoCapsuleWeight5 = "0", kleptoCapsulePrice5 = "0", kamekCapsuleWeight5 = "0", kamekCapsulePrice5 = "0", magiKoopaCapsuleWeight5 = "0", magiKoopaCapsulePrice5 = "0", blizzardCapsuleWeight5 = "0", blizzardCapsulePrice5 = "0", podobooCapsulePrice5 = "0", podobooCapsuleWeight5 = "0", paraTroopaCapsuleWeight5 = "0", paraTroopaCapsulePrice5 = "0", ukikiCapsulePrice5 = "0", ukikiCapsuleWeight5 = "0", tweesterCapsulePrice5 = "0", tweesterCapsuleWeight5 = "0", lakituCapsulePrice5 = "0", lakituCapsuleWeight5 = "0", warpPipeCapsulePrice5 = "0", warpPipeCapsuleWeight5 = "0", miracleCapsulePrice5 = "0", miracleCapsuleWeight5 = "0", boneCapsulePrice5 = "0", boneCapsuleWeight5 = "0", chanceCapsulePrice5 = "0", chanceCapsuleWeight5 = "0", chainChompCapsulePrice5 = "0", chainChompCapsuleWeight5 = "0", bowserCapsulePrice5 = "0", bowserCapsuleWeight5 = "0", dkCapsulePrice5 = "0", dkCapsuleWeight5 = "0"):

    mushroomCapsulePrice5 = mushroomCapsulePrice5.get()
    mushroomCapsuleWeight5 = mushroomCapsuleWeight5.get()

    kamekCapsuleWeight5 = kamekCapsuleWeight5.get()
    kamekCapsulePrice5 = kamekCapsulePrice5.get()
    
    goldenMushroomCapsulePrice5 = goldenMushroomCapsulePrice5.get()
    goldenMushroomCapsuleWeight5 = goldenMushroomCapsuleWeight5.get()

    cursedMushroomCapsulePrice5 = cursedMushroomCapsulePrice5.get()
    cursedMushroomCapsuleWeight5 = cursedMushroomCapsuleWeight5.get()

    goombaCapsulePrice5 = goombaCapsulePrice5.get()
    goombaCapsuleWeight5 = goombaCapsuleWeight5.get()

    kleptoCapsulePrice5 = kleptoCapsulePrice5.get()
    kleptoCapsuleWeight5 = kleptoCapsuleWeight5.get()

    flutterCapsulePrice5 = flutterCapsulePrice5.get()
    flutterCapsuleWeight5 = flutterCapsuleWeight5.get()

    podobooCapsulePrice5 = podobooCapsulePrice5.get()
    podobooCapsuleWeight5 = podobooCapsuleWeight5.get()

    spinyCapsulePrice5 = spinyCapsulePrice5.get()
    spinyCapsuleWeight5 = spinyCapsuleWeight5.get()

    coinBlockCapsulePrice5 = coinBlockCapsulePrice5.get()
    coinBlockCapsuleWeight5 = coinBlockCapsuleWeight5.get()

    plantCapsulePrice5 = plantCapsulePrice5.get()
    plantCapsuleWeight5 = plantCapsuleWeight5.get()

    hammerBroCapsulePrice5 = hammerBroCapsulePrice5.get()
    hammerBroCapsuleWeight5 = hammerBroCapsuleWeight5.get()

    bulletBillCapsulePrice5 = bulletBillCapsulePrice5.get()
    bulletBillCapsuleWeight5 = bulletBillCapsuleWeight5.get()

    blizzardCapsulePrice5 = blizzardCapsulePrice5.get()
    blizzardCapsuleWeight5 = blizzardCapsuleWeight5.get()

    paraTroopaCapsulePrice5 = paraTroopaCapsulePrice5.get()
    paraTroopaCapsuleWeight5 = paraTroopaCapsuleWeight5.get()

    magiKoopaCapsulePrice5 = magiKoopaCapsulePrice5.get()
    magiKoopaCapsuleWeight5 = magiKoopaCapsuleWeight5.get()

    ukikiCapsulePrice5 = ukikiCapsulePrice5.get()
    ukikiCapsuleWeight5 = ukikiCapsuleWeight5.get()

    tweesterCapsulePrice5 = tweesterCapsulePrice5.get()
    tweesterCapsuleWeight5 = tweesterCapsuleWeight5.get()

    lakituCapsulePrice5 = lakituCapsulePrice5.get()
    lakituCapsuleWeight5 = lakituCapsuleWeight5.get()

    warpPipeCapsulePrice5 = warpPipeCapsulePrice5.get()
    warpPipeCapsuleWeight5 = warpPipeCapsuleWeight5.get()

    miracleCapsulePrice5 = miracleCapsulePrice5.get()
    miracleCapsuleWeight5 = miracleCapsuleWeight5.get()

    boneCapsulePrice5 = boneCapsulePrice5.get()
    boneCapsuleWeight5 = boneCapsuleWeight5.get()

    chainChompCapsulePrice5 = chainChompCapsulePrice5.get()
    chainChompCapsuleWeight5 = chainChompCapsuleWeight5.get()

    chanceCapsulePrice5 = chanceCapsulePrice5.get()
    chanceCapsuleWeight5 = chanceCapsuleWeight5.get()

    bowserCapsulePrice5 = bowserCapsulePrice5.get()
    bowserCapsuleWeight5 = bowserCapsuleWeight5.get()

    dkCapsulePrice5 = dkCapsulePrice5.get()
    dkCapsuleWeight5 = dkCapsuleWeight5.get()

    duelCapsulePrice5 = duelCapsulePrice5.get()
    duelCapsuleWeight5 = duelCapsuleWeight5.get()

    koopaBankCapsulePrice5 = koopaBankCapsulePrice5.get()
    koopaBankCapsuleWeight5 = koopaBankCapsuleWeight5.get()

    bombCapsulePrice5 = bombCapsulePrice5.get()
    bombCapsuleWeight5 = bombCapsuleWeight5.get()

    orbWeightTotal = int(hammerBroCapsuleWeight5) + int(bulletBillCapsuleWeight5) + int(koopaBankCapsuleWeight5) + int(coinBlockCapsuleWeight5) + int(mushroomCapsuleWeight5) + int(goldenMushroomCapsuleWeight5) + int(cursedMushroomCapsuleWeight5) + int(warpPipeCapsuleWeight5) + int(flutterCapsuleWeight5) + int(spinyCapsuleWeight5) + int(goombaCapsuleWeight5) + int(plantCapsuleWeight5) + int(kleptoCapsuleWeight5) + int(kamekCapsuleWeight5) + int(blizzardCapsuleWeight5) + int(podobooCapsuleWeight5) + int(paraTroopaCapsuleWeight5) + int(magiKoopaCapsuleWeight5) + int(ukikiCapsuleWeight5) + int(tweesterCapsuleWeight5) + int(lakituCapsuleWeight5) + int(miracleCapsuleWeight5) + int(boneCapsuleWeight5) + int(chainChompCapsuleWeight5) + int(chanceCapsuleWeight5) + int(bowserCapsuleWeight5) + int(dkCapsuleWeight5) + int(duelCapsuleWeight5) + int(bombCapsuleWeight5)

    def calculateWeight(weight):
        if orbWeightTotal < 100:
            percentage = int(weight)
            return percentage
        else:
            percentage = (int(weight) / orbWeightTotal) * 100
            if 0< percentage < 1:
                return math.ceil(percentage)
            return round(percentage)
    
    mushroomCapsuleWeight5 = calculateWeight(mushroomCapsuleWeight5)
    goldenMushroomCapsuleWeight5 = calculateWeight(goldenMushroomCapsuleWeight5)
    warpPipeCapsuleWeight5 = calculateWeight(warpPipeCapsuleWeight5)
    flutterCapsuleWeight5 = calculateWeight(flutterCapsuleWeight5)
    cursedMushroomCapsuleWeight5 = calculateWeight(cursedMushroomCapsuleWeight5)
    spinyCapsuleWeight5 = calculateWeight(spinyCapsuleWeight5)
    goombaCapsuleWeight5 = calculateWeight(goombaCapsuleWeight5)
    plantCapsuleWeight5 = calculateWeight(plantCapsuleWeight5)
    kleptoCapsuleWeight5 = calculateWeight(kleptoCapsuleWeight5)
    kamekCapsuleWeight5 = calculateWeight(kamekCapsuleWeight5)
    blizzardCapsuleWeight5 = calculateWeight(blizzardCapsuleWeight5)
    podobooCapsuleWeight5 = calculateWeight(podobooCapsuleWeight5)
    paraTroopaCapsuleWeight5 = calculateWeight(paraTroopaCapsuleWeight5)
    magiKoopaCapsuleWeight5 = calculateWeight(magiKoopaCapsuleWeight5)
    ukikiCapsuleWeight5 = calculateWeight(ukikiCapsuleWeight5)
    tweesterCapsuleWeight5 = calculateWeight(tweesterCapsuleWeight5)
    lakituCapsuleWeight5 = calculateWeight(lakituCapsuleWeight5)
    miracleCapsuleWeight5 = calculateWeight(miracleCapsuleWeight5)
    boneCapsuleWeight5 = calculateWeight(boneCapsuleWeight5)
    chainChompCapsuleWeight5 = calculateWeight(chainChompCapsuleWeight5)
    chanceCapsuleWeight5 = calculateWeight(chanceCapsuleWeight5)
    bowserCapsuleWeight5 = calculateWeight(bowserCapsuleWeight5)
    dkCapsuleWeight5 = calculateWeight(dkCapsuleWeight5)
    duelCapsuleWeight5 = calculateWeight(duelCapsuleWeight5)
    hammerBroCapsuleWeight5 = calculateWeight(hammerBroCapsuleWeight5)
    bulletBillCapsuleWeight5 = calculateWeight(bulletBillCapsuleWeight5)
    koopaBankCapsuleWeight5 = calculateWeight(koopaBankCapsuleWeight5)
    coinBlockCapsuleWeight5 = calculateWeight(coinBlockCapsuleWeight5)
    bombCapsuleWeight5 = calculateWeight(bombCapsuleWeight5)

    orbWeightTotal = hammerBroCapsuleWeight5 + bulletBillCapsuleWeight5 + koopaBankCapsuleWeight5 + coinBlockCapsuleWeight5 + mushroomCapsuleWeight5 + goldenMushroomCapsuleWeight5 + cursedMushroomCapsuleWeight5 + warpPipeCapsuleWeight5 + flutterCapsuleWeight5 + spinyCapsuleWeight5 + goombaCapsuleWeight5 + plantCapsuleWeight5 + kleptoCapsuleWeight5 + kamekCapsuleWeight5 + blizzardCapsuleWeight5 + podobooCapsuleWeight5 + paraTroopaCapsuleWeight5 + magiKoopaCapsuleWeight5 + ukikiCapsuleWeight5 + tweesterCapsuleWeight5 + lakituCapsuleWeight5 + miracleCapsuleWeight5 + boneCapsuleWeight5 + chainChompCapsuleWeight5 + chanceCapsuleWeight5 + bowserCapsuleWeight5 + dkCapsuleWeight5 + duelCapsuleWeight5 + bombCapsuleWeight5
    
    if orbWeightTotal < 100:
        var_names = ['mushroomCapsuleWeight5', 'goldenMushroomCapsuleWeight5', 'warpPipeCapsuleWeight5', 'flutterCapsuleWeight5', 'cursedMushroomCapsuleWeight5', 'spinyCapsuleWeight5', 'goombaCapsuleWeight5', 'plantCapsuleWeight5', 'kleptoCapsuleWeight5', 'kamekCapsuleWeight5', 'blizzardCapsuleWeight5', 'podobooCapsuleWeight5', 'paraTroopaCapsuleWeight5', 'magiKoopaCapsuleWeight5', 'ukikiCapsuleWeight5', 'tweesterCapsuleWeight5', 'lakituCapsuleWeight5', 'miracleCapsuleWeight5', 'boneCapsuleWeight5', 'chainChompCapsuleWeight5', 'chanceCapsuleWeight5', 'bowserCapsuleWeight5', 'dkCapsuleWeight5', 'duelCapsuleWeight5', 'hammerBroCapsuleWeight5', 'bulletBillCapsuleWeight5', 'koopaBankCapsuleWeight5', 'coinBlockCapsuleWeight5', 'bombCapsuleWeight5']
        max_var = max(zip(var_names, (map(eval, var_names))), key=lambda tuple: tuple[1])[0]
        
        if max_var == 'mushroomCapsuleWeight5':
            mushroomCapsuleWeight5 += (100 - orbWeightTotal)

        if max_var == 'goldenMushroomCapsuleWeight5':
            goldenMushroomCapsuleWeight5 += (100 - orbWeightTotal)

        if max_var == 'warpPipeCapsuleWeight5':
            warpPipeCapsuleWeight5 += (100 - orbWeightTotal)

        if max_var == 'flutterCapsuleWeight5':
            flutterCapsuleWeight5 += (100 - orbWeightTotal)

        if max_var == 'cursedMushroomCapsuleWeight5':
            cursedMushroomCapsuleWeight5 += (100 - orbWeightTotal)

        if max_var == 'spinyCapsuleWeight5':
            spinyCapsuleWeight5 += (100 - orbWeightTotal)

        if max_var == 'goombaCapsuleWeight5':
            goombaCapsuleWeight5 += (100 - orbWeightTotal)

        if max_var == 'plantCapsuleWeight5':
            plantCapsuleWeight5 += (100 - orbWeightTotal)

        if max_var == 'kleptoCapsuleWeight5':
            kleptoCapsuleWeight5 += (100 - orbWeightTotal)

        if max_var == 'kamekCapsuleWeight5':
            kamekCapsuleWeight5 += (100 - orbWeightTotal)

        if max_var == 'blizzardCapsuleWeight5':
            blizzardCapsuleWeight5 += (100 - orbWeightTotal)

        if max_var == 'podobooCapsuleWeight5':
            podobooCapsuleWeight5 += (100 - orbWeightTotal)

        if max_var == 'paraTroopaCapsuleWeight5':
            paraTroopaCapsuleWeight5 += (100 - orbWeightTotal)

        if max_var == 'magiKoopaCapsuleWeight5':
            magiKoopaCapsuleWeight5 += (100 - orbWeightTotal)

        if max_var == 'ukikiCapsuleWeight5':
            ukikiCapsuleWeight5 += (100 - orbWeightTotal)

        if max_var == 'tweesterCapsuleWeight5':
            tweesterCapsuleWeight5 += (100 - orbWeightTotal)

        if max_var == 'lakituCapsuleWeight5':
            lakituCapsuleWeight5 += (100 - orbWeightTotal)

        if max_var == 'miracleCapsuleWeight5':
            miracleCapsuleWeight5 += (100 - orbWeightTotal)

        if max_var == 'boneCapsuleWeight5':
            boneCapsuleWeight5 += (100 - orbWeightTotal)

        if max_var == 'chainChompCapsuleWeight5':
            chainChompCapsuleWeight5 += (100 - orbWeightTotal)

        if max_var == 'chanceCapsuleWeight5':
            chanceCapsuleWeight5 += (100 - orbWeightTotal)

        if max_var == 'bowserCapsuleWeight5':
            bowserCapsuleWeight5 += (100 - orbWeightTotal)

        if max_var == 'dkCapsuleWeight5':
            dkCapsuleWeight5 += (100 - orbWeightTotal)

        if max_var == 'duelCapsuleWeight5':
            duelCapsuleWeight5 += (100 - orbWeightTotal)

        if max_var == 'hammerBroCapsuleWeight5':
            hammerBroCapsuleWeight5 += (100 - orbWeightTotal)

        if max_var == 'bulletBillCapsuleWeight5':
            bulletBillCapsuleWeight5 += (100 - orbWeightTotal)

        if max_var == 'koopaBankCapsuleWeight5':
            koopaBankCapsuleWeight5 += (100 - orbWeightTotal)

        if max_var == 'coinBlockCapsuleWeight5':
            coinBlockCapsuleWeight5 += (100 - orbWeightTotal)

        if max_var == 'bombCapsuleWeight5':
            bombCapsuleWeight5 += (100 - orbWeightTotal)

    mushroomCapsuleWeight5 = str(mushroomCapsuleWeight5)
    goldenMushroomCapsuleWeight5 = str(goldenMushroomCapsuleWeight5)
    warpPipeCapsuleWeight5 = str(warpPipeCapsuleWeight5)
    flutterCapsuleWeight5 = str(flutterCapsuleWeight5)
    cursedMushroomCapsuleWeight5 = str(cursedMushroomCapsuleWeight5)
    spinyCapsuleWeight5 = str(spinyCapsuleWeight5)
    goombaCapsuleWeight5 = str(goombaCapsuleWeight5)
    plantCapsuleWeight5 = str(plantCapsuleWeight5)
    kleptoCapsuleWeight5 = str(kleptoCapsuleWeight5)
    kamekCapsuleWeight5 = str(kamekCapsuleWeight5)
    blizzardCapsuleWeight5 = str(blizzardCapsuleWeight5)
    podobooCapsuleWeight5 = str(podobooCapsuleWeight5)
    paraTroopaCapsuleWeight5 = str(paraTroopaCapsuleWeight5)
    magiKoopaCapsuleWeight5 = str(magiKoopaCapsuleWeight5)
    ukikiCapsuleWeight5 = str(ukikiCapsuleWeight5)
    tweesterCapsuleWeight5 = str(tweesterCapsuleWeight5)
    lakituCapsuleWeight5 = str(lakituCapsuleWeight5)
    miracleCapsuleWeight5 = str(miracleCapsuleWeight5)
    boneCapsuleWeight5 = str(boneCapsuleWeight5)
    chainChompCapsuleWeight5 = str(chainChompCapsuleWeight5)
    chanceCapsuleWeight5 = str(chanceCapsuleWeight5)
    bowserCapsuleWeight5 = str(bowserCapsuleWeight5)
    dkCapsuleWeight5 = str(dkCapsuleWeight5)
    duelCapsuleWeight5 = str(duelCapsuleWeight5)
    hammerBroCapsuleWeight5 = str(hammerBroCapsuleWeight5)
    bulletBillCapsuleWeight5 = str(bulletBillCapsuleWeight5)
    koopaBankCapsuleWeight5 = str(koopaBankCapsuleWeight5)
    coinBlockCapsuleWeight5 = str(coinBlockCapsuleWeight5)
    bombCapsuleWeight5 = str(bombCapsuleWeight5)

    try:
        mushroomCapsuleWeight5 = hex(int(mushroomCapsuleWeight5))
        if len(mushroomCapsuleWeight5) == 4:
            mushroomCapsuleWeight5 = mushroomCapsuleWeight5[2:]
        elif len(mushroomCapsuleWeight5) == 3:
            mushroomCapsuleWeight5 = "0" + mushroomCapsuleWeight5[2:]
    except:
        mushroomCapsuleWeight5 = "00"

    try:
        mushroomCapsulePrice5 = hex(int(mushroomCapsulePrice5))
        if len(mushroomCapsulePrice5) == 4:
            mushroomCapsulePrice5 = mushroomCapsulePrice5[2:]
        elif len(mushroomCapsulePrice5) == 3:
            mushroomCapsulePrice5 = "0" + mushroomCapsulePrice5[2:]
    except:
        mushroomCapsulePrice5 = "00"

    try:
        hammerBroCapsuleWeight5 = hex(int(hammerBroCapsuleWeight5))
        if len(hammerBroCapsuleWeight5) == 4:
            hammerBroCapsuleWeight5 = hammerBroCapsuleWeight5[2:]
        elif len(hammerBroCapsuleWeight5) == 3:
            hammerBroCapsuleWeight5 = "0" + hammerBroCapsuleWeight5[2:]
    except:
        hammerBroCapsuleWeight5 = "00"

    try:
        hammerBroCapsulePrice5 = hex(int(hammerBroCapsulePrice5))
        if len(hammerBroCapsulePrice5) == 4:
            hammerBroCapsulePrice5 = hammerBroCapsulePrice5[2:]
        elif len(hammerBroCapsulePrice5) == 3:
            hammerBroCapsulePrice5 = "0" + hammerBroCapsulePrice5[2:]
    except:
        hammerBroCapsulePrice5 = "00"

    try:
        goldenMushroomCapsuleWeight5 = hex(int(goldenMushroomCapsuleWeight5))
        if len(goldenMushroomCapsuleWeight5) == 4:
            goldenMushroomCapsuleWeight5 = goldenMushroomCapsuleWeight5[2:]
        elif len(goldenMushroomCapsuleWeight5) == 3:
            goldenMushroomCapsuleWeight5 = "0" + goldenMushroomCapsuleWeight5[2:]
    except:
        goldenMushroomCapsuleWeight5 = "00"

    try:
        goldenMushroomCapsulePrice5 = hex(int(goldenMushroomCapsulePrice5))
        if len(goldenMushroomCapsulePrice5) == 4:
            goldenMushroomCapsulePrice5 = goldenMushroomCapsulePrice5[2:]
        elif len(goldenMushroomCapsulePrice5) == 3:
            goldenMushroomCapsulePrice5 = "0" + goldenMushroomCapsulePrice5[2:]
    except:
        goldenMushroomCapsulePrice5 = "00"
    
    try:
        cursedMushroomCapsuleWeight5 = hex(int(cursedMushroomCapsuleWeight5))
        if len(cursedMushroomCapsuleWeight5) == 4:
            cursedMushroomCapsuleWeight5 = cursedMushroomCapsuleWeight5[2:]
        elif len(cursedMushroomCapsuleWeight5) == 3:
            cursedMushroomCapsuleWeight5 = "0" + cursedMushroomCapsuleWeight5[2:]
    except:
        cursedMushroomCapsuleWeight5 = "00"

    try:
        cursedMushroomCapsulePrice5 = hex(int(cursedMushroomCapsulePrice5))
        if len(cursedMushroomCapsulePrice5) == 4:
            cursedMushroomCapsulePrice5 = cursedMushroomCapsulePrice5[2:]
        elif len(cursedMushroomCapsulePrice5) == 3:
            cursedMushroomCapsulePrice5 = "0" + cursedMushroomCapsulePrice5[2:]
    except:
        cursedMushroomCapsulePrice5 = "00"

    try:
        kleptoCapsuleWeight5 = hex(int(kleptoCapsuleWeight5))
        if len(kleptoCapsuleWeight5) == 4:
            kleptoCapsuleWeight5 = kleptoCapsuleWeight5[2:]
        elif len(kleptoCapsuleWeight5) == 3:
            kleptoCapsuleWeight5 = "0" + kleptoCapsuleWeight5[2:]
    except:
        kleptoCapsuleWeight5 = "00"

    try:
        kleptoCapsulePrice5 = hex(int(kleptoCapsulePrice5))
        if len(kleptoCapsulePrice5) == 4:
            kleptoCapsulePrice5 = kleptoCapsulePrice5[2:]
        elif len(kleptoCapsulePrice5) == 3:
            kleptoCapsulePrice5 = "0" + kleptoCapsulePrice5[2:]
    except:
        kleptoCapsulePrice5 = "00"

    try:
        warpPipeCapsuleWeight5 = hex(int(warpPipeCapsuleWeight5))
        if len(warpPipeCapsuleWeight5) == 4:
            warpPipeCapsuleWeight5 = warpPipeCapsuleWeight5[2:]
        elif len(warpPipeCapsuleWeight5) == 3:
            warpPipeCapsuleWeight5 = "0" + warpPipeCapsuleWeight5[2:]
    except:
        warpPipeCapsuleWeight5 = "00"

    try:
        warpPipeCapsulePrice5 = hex(int(warpPipeCapsulePrice5))
        if len(warpPipeCapsulePrice5) == 4:
            warpPipeCapsulePrice5 = warpPipeCapsulePrice5[2:]
        elif len(warpPipeCapsulePrice5) == 3:
            warpPipeCapsulePrice5 = "0" + warpPipeCapsulePrice5[2:]
    except:
        warpPipeCapsulePrice5 = "00"

    try:
        flutterCapsuleWeight5 = hex(int(flutterCapsuleWeight5))
        if len(flutterCapsuleWeight5) == 4:
            flutterCapsuleWeight5 = flutterCapsuleWeight5[2:]
        elif len(flutterCapsuleWeight5) == 3:
            flutterCapsuleWeight5 = "0" + flutterCapsuleWeight5[2:]
    except:
        flutterCapsuleWeight5 = "00"

    try:
        flutterCapsulePrice5 = hex(int(flutterCapsulePrice5))
        if len(flutterCapsulePrice5) == 4:
            flutterCapsulePrice5 = flutterCapsulePrice5[2:]
        elif len(flutterCapsulePrice5) == 3:
            flutterCapsulePrice5 = "0" + flutterCapsulePrice5[2:]
    except:
        flutterCapsulePrice5 = "00"

    try:
        cursedMushroomCapsulePrice5 = hex(int(cursedMushroomCapsulePrice5))
        if len(cursedMushroomCapsulePrice5) == 4:
            cursedMushroomCapsulePrice5 = cursedMushroomCapsulePrice5[2:]
        elif len(cursedMushroomCapsulePrice5) == 3:
            cursedMushroomCapsulePrice5 = "0" + cursedMushroomCapsulePrice5[2:]
    except:
        cursedMushroomCapsulePrice5 = "00"

    try:
        spinyCapsuleWeight5 = hex(int(spinyCapsuleWeight5))
        if len(spinyCapsuleWeight5) == 4:
            spinyCapsuleWeight5 = spinyCapsuleWeight5[2:]
        elif len(spinyCapsuleWeight5) == 3:
            spinyCapsuleWeight5 = "0" + spinyCapsuleWeight5[2:]
    except:
        spinyCapsuleWeight5 = "00"

    try:
        spinyCapsulePrice5 = hex(int(spinyCapsulePrice5))
        if len(spinyCapsulePrice5) == 4:
            spinyCapsulePrice5 = spinyCapsulePrice5[2:]
        elif len(spinyCapsulePrice5) == 3:
            spinyCapsulePrice5 = "0" + spinyCapsulePrice5[2:]
    except:
        spinyCapsulePrice5 = "00"

    try:
        goombaCapsuleWeight5 = hex(int(goombaCapsuleWeight5))
        if len(goombaCapsuleWeight5) == 4:
            goombaCapsuleWeight5 = goombaCapsuleWeight5[2:]
        elif len(goombaCapsuleWeight5) == 3:
            goombaCapsuleWeight5 = "0" + goombaCapsuleWeight5[2:]
    except:
        goombaCapsuleWeight5 = "00"

    try:
        goombaCapsulePrice5 = hex(int(goombaCapsulePrice5))
        if len(goombaCapsulePrice5) == 4:
            goombaCapsulePrice5 = goombaCapsulePrice5[2:]
        elif len(goombaCapsulePrice5) == 3:
            goombaCapsulePrice5 = "0" + goombaCapsulePrice5[2:]
    except:
        goombaCapsulePrice5 = "00"

    try:
        plantCapsuleWeight5 = hex(int(plantCapsuleWeight5))
        if len(plantCapsuleWeight5) == 4:
            plantCapsuleWeight5 = plantCapsuleWeight5[2:]
        elif len(plantCapsuleWeight5) == 3:
            plantCapsuleWeight5 = "0" + plantCapsuleWeight5[2:]
    except:
        plantCapsuleWeight5 = "00"

    try:
        plantCapsulePrice5 = hex(int(plantCapsulePrice5))
        if len(plantCapsulePrice5) == 4:
            plantCapsulePrice5 = plantCapsulePrice5[2:]
        elif len(plantCapsulePrice5) == 3:
            plantCapsulePrice5 = "0" + plantCapsulePrice5[2:]
    except:
        plantCapsulePrice5 = "00"

    try:
        kleptoCapsuleWeight5 = hex(int(kleptoCapsuleWeight5))
        if len(kleptoCapsuleWeight5) == 4:
            kleptoCapsuleWeight5 = kleptoCapsuleWeight5[2:]
        elif len(kleptoCapsuleWeight5) == 3:
            kleptoCapsuleWeight5 = "0" + kleptoCapsuleWeight5[2:]
    except:
        kleptoCapsuleWeight5 = "00"

    try:
        kleptoCapsulePrice5 = hex(int(kleptoCapsulePrice5))
        if len(kleptoCapsulePrice5) == 4:
            kleptoCapsulePrice5 = kleptoCapsulePrice5[2:]
        elif len(kleptoCapsulePrice5) == 3:
            kleptoCapsulePrice5 = "0" + kleptoCapsulePrice5[2:]
    except:
        kleptoCapsulePrice5 = "00"

    try:
        kamekCapsuleWeight5 = hex(int(kamekCapsuleWeight5))
        if len(kamekCapsuleWeight5) == 4:
            kamekCapsuleWeight5 = kamekCapsuleWeight5[2:]
        elif len(kamekCapsuleWeight5) == 3:
            kamekCapsuleWeight5 = "0" + kamekCapsuleWeight5[2:]
    except:
        kamekCapsuleWeight5 = "00"

    try:
        kamekCapsulePrice5 = hex(int(kamekCapsulePrice5))
        if len(kamekCapsulePrice5) == 4:
            kamekCapsulePrice5 = kamekCapsulePrice5[2:]
        elif len(kamekCapsulePrice5) == 3:
            kamekCapsulePrice5 = "0" + kamekCapsulePrice5[2:]
    except:
        kamekCapsulePrice5 = "00"

    try:
        magiKoopaCapsuleWeight5 = hex(int(magiKoopaCapsuleWeight5))
        if len(magiKoopaCapsuleWeight5) == 4:
            magiKoopaCapsuleWeight5 = magiKoopaCapsuleWeight5[2:]
        elif len(magiKoopaCapsuleWeight5) == 3:
            magiKoopaCapsuleWeight5 = "0" + magiKoopaCapsuleWeight5[2:]
    except:
        magiKoopaCapsuleWeight5 = "00"

    try:
        magiKoopaCapsulePrice5 = hex(int(magiKoopaCapsulePrice5))
        if len(magiKoopaCapsulePrice5) == 4:
            magiKoopaCapsulePrice5 = magiKoopaCapsulePrice5[2:]
        elif len(magiKoopaCapsulePrice5) == 3:
            magiKoopaCapsulePrice5 = "0" + magiKoopaCapsulePrice5[2:]
    except:
        magiKoopaCapsulePrice5 = "00"

    try:
        blizzardCapsuleWeight5 = hex(int(blizzardCapsuleWeight5))
        if len(blizzardCapsuleWeight5) == 4:
            blizzardCapsuleWeight5 = blizzardCapsuleWeight5[2:]
        elif len(blizzardCapsuleWeight5) == 3:
            blizzardCapsuleWeight5 = "0" + blizzardCapsuleWeight5[2:]
    except:
        blizzardCapsuleWeight5 = "00"

    try:
        blizzardCapsulePrice5 = hex(int(blizzardCapsulePrice5))
        if len(blizzardCapsulePrice5) == 4:
            blizzardCapsulePrice5 = blizzardCapsulePrice5[2:]
        elif len(blizzardCapsulePrice5) == 3:
            blizzardCapsulePrice5 = "0" + blizzardCapsulePrice5[2:]
    except:
        blizzardCapsulePrice5 = "00"

    try:
        podobooCapsuleWeight5 = hex(int(podobooCapsuleWeight5))
        if len(podobooCapsuleWeight5) == 4:
            podobooCapsuleWeight5 = podobooCapsuleWeight5[2:]
        elif len(podobooCapsuleWeight5) == 3:
            podobooCapsuleWeight5 = "0" + podobooCapsuleWeight5[2:]
    except:
        podobooCapsuleWeight5 = "00"

    try:
        podobooCapsulePrice5 = hex(int(podobooCapsulePrice5))
        if len(podobooCapsulePrice5) == 4:
            podobooCapsulePrice5 = podobooCapsulePrice5[2:]
        elif len(podobooCapsulePrice5) == 3:
            podobooCapsulePrice5 = "0" + podobooCapsulePrice5[2:]
    except:
        podobooCapsulePrice5 = "00"

    try:
        paraTroopaCapsuleWeight5 = hex(int(paraTroopaCapsuleWeight5))
        if len(paraTroopaCapsuleWeight5) == 4:
            paraTroopaCapsuleWeight5 = paraTroopaCapsuleWeight5[2:]
        elif len(paraTroopaCapsuleWeight5) == 3:
            paraTroopaCapsuleWeight5 = "0" + paraTroopaCapsuleWeight5[2:]
    except:
        paraTroopaCapsuleWeight5 = "00"

    try:
        paraTroopaCapsulePrice5 = hex(int(paraTroopaCapsulePrice5))
        if len(paraTroopaCapsulePrice5) == 4:
            paraTroopaCapsulePrice5 = paraTroopaCapsulePrice5[2:]
        elif len(paraTroopaCapsulePrice5) == 3:
            paraTroopaCapsulePrice5 = "0" + paraTroopaCapsulePrice5[2:]
    except:
        paraTroopaCapsulePrice5 = "00"

    try:
        magiKoopaCapsuleWeight5 = hex(int(magiKoopaCapsuleWeight5))
        if len(magiKoopaCapsuleWeight5) == 4:
            magiKoopaCapsuleWeight5 = magiKoopaCapsuleWeight5[2:]
        elif len(magiKoopaCapsuleWeight5) == 3:
            magiKoopaCapsuleWeight5 = "0" + magiKoopaCapsuleWeight5[2:]
    except:
        magiKoopaCapsuleWeight5 = "00"

    try:
        magiKoopaCapsulePrice5 = hex(int(magiKoopaCapsulePrice5))
        if len(magiKoopaCapsulePrice5) == 4:
            magiKoopaCapsulePrice5 = magiKoopaCapsulePrice5[2:]
        elif len(magiKoopaCapsulePrice5) == 3:
            magiKoopaCapsulePrice5 = "0" + magiKoopaCapsulePrice5[2:]
    except:
        magiKoopaCapsulePrice5 = "00"

    try:
        ukikiCapsuleWeight5 = hex(int(ukikiCapsuleWeight5))
        if len(ukikiCapsuleWeight5) == 4:
            ukikiCapsuleWeight5 = ukikiCapsuleWeight5[2:]
        elif len(ukikiCapsuleWeight5) == 3:
            ukikiCapsuleWeight5 = "0" + ukikiCapsuleWeight5[2:]
    except:
        ukikiCapsuleWeight5 = "00"

    try:
        ukikiCapsulePrice5 = hex(int(ukikiCapsulePrice5))
        if len(ukikiCapsulePrice5) == 4:
            ukikiCapsulePrice5 = ukikiCapsulePrice5[2:]
        elif len(ukikiCapsulePrice5) == 3:
            ukikiCapsulePrice5 = "0" + ukikiCapsulePrice5[2:]
    except:
        ukikiCapsulePrice5 = "00"

    try:
        tweesterCapsuleWeight5 = hex(int(tweesterCapsuleWeight5))
        if len(tweesterCapsuleWeight5) == 4:
            tweesterCapsuleWeight5 = tweesterCapsuleWeight5[2:]
        elif len(tweesterCapsuleWeight5) == 3:
            tweesterCapsuleWeight5 = "0" + tweesterCapsuleWeight5[2:]
    except:
        tweesterCapsuleWeight5 = "00"

    try:
        tweesterCapsulePrice5 = hex(int(tweesterCapsulePrice5))
        if len(tweesterCapsulePrice5) == 4:
            tweesterCapsulePrice5 = tweesterCapsulePrice5[2:]
        elif len(tweesterCapsulePrice5) == 3:
            tweesterCapsulePrice5 = "0" + tweesterCapsulePrice5[2:]
    except:
        tweesterCapsulePrice5 = "00"

    try:
        lakituCapsuleWeight5 = hex(int(lakituCapsuleWeight5))
        if len(lakituCapsuleWeight5) == 4:
            lakituCapsuleWeight5 = lakituCapsuleWeight5[2:]
        elif len(lakituCapsuleWeight5) == 3:
            lakituCapsuleWeight5 = "0" + lakituCapsuleWeight5[2:]
    except:
        lakituCapsuleWeight5 = "00"

    try:
        lakituCapsulePrice5 = hex(int(lakituCapsulePrice5))
        if len(lakituCapsulePrice5) == 4:
            lakituCapsulePrice5 = lakituCapsulePrice5[2:]
        elif len(lakituCapsulePrice5) == 3:
            lakituCapsulePrice5 = "0" + lakituCapsulePrice5[2:]
    except:
        lakituCapsulePrice5 = "00"

    try:
        miracleCapsuleWeight5 = hex(int(miracleCapsuleWeight5))
        if len(miracleCapsuleWeight5) == 4:
            miracleCapsuleWeight5 = miracleCapsuleWeight5[2:]
        elif len(miracleCapsuleWeight5) == 3:
            miracleCapsuleWeight5 = "0" + miracleCapsuleWeight5[2:]
    except:
        miracleCapsuleWeight5 = "00"

    try:
        miracleCapsulePrice5 = hex(int(miracleCapsulePrice5))
        if len(miracleCapsulePrice5) == 4:
            miracleCapsulePrice5 = miracleCapsulePrice5[2:]
        elif len(miracleCapsulePrice5) == 3:
            miracleCapsulePrice5 = "0" + miracleCapsulePrice5[2:]
    except:
        miracleCapsulePrice5 = "00"

    try:
        boneCapsuleWeight5 = hex(int(boneCapsuleWeight5))
        if len(boneCapsuleWeight5) == 4:
            boneCapsuleWeight5 = boneCapsuleWeight5[2:]
        elif len(boneCapsuleWeight5) == 3:
            boneCapsuleWeight5 = "0" + boneCapsuleWeight5[2:]
    except:
        boneCapsuleWeight5 = "00"

    try:
        boneCapsulePrice5 = hex(int(boneCapsulePrice5))
        if len(boneCapsulePrice5) == 4:
            boneCapsulePrice5 = boneCapsulePrice5[2:]
        elif len(boneCapsulePrice5) == 3:
            boneCapsulePrice5 = "0" + boneCapsulePrice5[2:]
    except:
        boneCapsulePrice5 = "00"

    try:
        chainChompCapsuleWeight5 = hex(int(chainChompCapsuleWeight5))
        if len(chainChompCapsuleWeight5) == 4:
            chainChompCapsuleWeight5 = chainChompCapsuleWeight5[2:]
        elif len(chainChompCapsuleWeight5) == 3:
            chainChompCapsuleWeight5 = "0" + chainChompCapsuleWeight5[2:]
    except:
        chainChompCapsuleWeight5 = "00"

    try:
        chainChompCapsulePrice5 = hex(int(chainChompCapsulePrice5))
        if len(chainChompCapsulePrice5) == 4:
            chainChompCapsulePrice5 = chainChompCapsulePrice5[2:]
        elif len(chainChompCapsulePrice5) == 3:
            chainChompCapsulePrice5 = "0" + chainChompCapsulePrice5[2:]
    except:
        chainChompCapsulePrice5 = "00"

    try:
        chanceCapsuleWeight5 = hex(int(chanceCapsuleWeight5))
        if len(chanceCapsuleWeight5) == 4:
            chanceCapsuleWeight5 = chanceCapsuleWeight5[2:]
        elif len(chanceCapsuleWeight5) == 3:
            chanceCapsuleWeight5 = "0" + chanceCapsuleWeight5[2:]
    except:
        chanceCapsuleWeight5 = "00"

    try:
        chanceCapsulePrice5 = hex(int(chanceCapsulePrice5))
        if len(chanceCapsulePrice5) == 4:
            chanceCapsulePrice5 = chanceCapsulePrice5[2:]
        elif len(chanceCapsulePrice5) == 3:
            chanceCapsulePrice5 = "0" + chanceCapsulePrice5[2:]
    except:
        chanceCapsulePrice5 = "00"

    try:
        bowserCapsuleWeight5 = hex(int(bowserCapsuleWeight5))
        if len(bowserCapsuleWeight5) == 4:
            bowserCapsuleWeight5 = bowserCapsuleWeight5[2:]
        elif len(bowserCapsuleWeight5) == 3:
            bowserCapsuleWeight5 = "0" + bowserCapsuleWeight5[2:]
    except:
        bowserCapsuleWeight5 = "00"

    try:
        bowserCapsulePrice5 = hex(int(bowserCapsulePrice5))
        if len(bowserCapsulePrice5) == 4:
            bowserCapsulePrice5 = bowserCapsulePrice5[2:]
        elif len(bowserCapsulePrice5) == 3:
            bowserCapsulePrice5 = "0" + bowserCapsulePrice5[2:]
    except:
        bowserCapsulePrice5 = "00"

    try:
        dkCapsuleWeight5 = hex(int(dkCapsuleWeight5))
        if len(dkCapsuleWeight5) == 4:
            dkCapsuleWeight5 = dkCapsuleWeight5[2:]
        elif len(dkCapsuleWeight5) == 3:
            dkCapsuleWeight5 = "0" + dkCapsuleWeight5[2:]
    except:
        dkCapsuleWeight5 = "00"

    try:
        dkCapsulePrice5 = hex(int(dkCapsulePrice5))
        if len(dkCapsulePrice5) == 4:
            dkCapsulePrice5 = dkCapsulePrice5[2:]
        elif len(dkCapsulePrice5) == 3:
            dkCapsulePrice5 = "0" + dkCapsulePrice5[2:]
    except:
        dkCapsulePrice5 = "00"

    try:
        warpPipeCapsuleWeight5 = hex(int(warpPipeCapsuleWeight5))
        if len(warpPipeCapsuleWeight5) == 4:
            warpPipeCapsuleWeight5 = warpPipeCapsuleWeight5[2:]
        elif len(warpPipeCapsuleWeight5) == 3:
            warpPipeCapsuleWeight5 = "0" + warpPipeCapsuleWeight5[2:]
    except:
        warpPipeCapsuleWeight5 = "00"

    try:
        warpPipeCapsulePrice5 = hex(int(warpPipeCapsulePrice5))
        if len(warpPipeCapsulePrice5) == 4:
            warpPipeCapsulePrice5 = warpPipeCapsulePrice5[2:]
        elif len(warpPipeCapsulePrice5) == 3:
            warpPipeCapsulePrice5 = "0" + warpPipeCapsulePrice5[2:]
    except:
        warpPipeCapsulePrice5 = "00"

    try:
        duelCapsuleWeight5 = hex(int(duelCapsuleWeight5))
        if len(duelCapsuleWeight5) == 4:
            duelCapsuleWeight5 = duelCapsuleWeight5[2:]
        elif len(duelCapsuleWeight5) == 3:
            duelCapsuleWeight5 = "0" + duelCapsuleWeight5[2:]
    except:
        duelCapsuleWeight5 = "00"

    try:
        duelCapsulePrice5 = hex(int(duelCapsulePrice5))
        if len(duelCapsulePrice5) == 4:
            duelCapsulePrice5 = duelCapsulePrice5[2:]
        elif len(duelCapsulePrice5) == 3:
            duelCapsulePrice5 = "0" + duelCapsulePrice5[2:]
    except:
        duelCapsulePrice5 = "00"

    try:
        coinBlockCapsuleWeight5 = hex(int(coinBlockCapsuleWeight5))
        if len(coinBlockCapsuleWeight5) == 4:
            coinBlockCapsuleWeight5 = coinBlockCapsuleWeight5[2:]
        elif len(coinBlockCapsuleWeight5) == 3:
            coinBlockCapsuleWeight5 = "0" + coinBlockCapsuleWeight5[2:]
    except:
        coinBlockCapsuleWeight5 = "00"

    try:
        coinBlockCapsulePrice5 = hex(int(coinBlockCapsulePrice5))
        if len(coinBlockCapsulePrice5) == 4:
            coinBlockCapsulePrice5 = coinBlockCapsulePrice5[2:]
        elif len(coinBlockCapsulePrice5) == 3:
            coinBlockCapsulePrice5 = "0" + coinBlockCapsulePrice5[2:]
    except:
        coinBlockCapsulePrice5 = "00"

    try:
        bombCapsuleWeight5 = hex(int(bombCapsuleWeight5))
        if len(bombCapsuleWeight5) == 4:
            bombCapsuleWeight5 = bombCapsuleWeight5[2:]
        elif len(bombCapsuleWeight5) == 3:
            bombCapsuleWeight5 = "0" + bombCapsuleWeight5[2:]
    except:
        bombCapsuleWeight5 = "00"

    try:
        bombCapsulePrice5 = hex(int(bombCapsulePrice5))
        if len(bombCapsulePrice5) == 4:
            bombCapsulePrice5 = bombCapsulePrice5[2:]
        elif len(bombCapsulePrice5) == 3:
            bombCapsulePrice5 = "0" + bombCapsulePrice5[2:]
    except:
        bombCapsulePrice5 = "00"

    try:
        koopaBankCapsuleWeight5 = hex(int(koopaBankCapsuleWeight5))
        if len(koopaBankCapsuleWeight5) == 4:
            koopaBankCapsuleWeight5 = koopaBankCapsuleWeight5[2:]
        elif len(koopaBankCapsuleWeight5) == 3:
            koopaBankCapsuleWeight5 = "0" + koopaBankCapsuleWeight5[2:]
    except:
        koopaBankCapsuleWeight5 = "00"

    try:
        koopaBankCapsulePrice5 = hex(int(koopaBankCapsulePrice5))
        if len(koopaBankCapsulePrice5) == 4:
            koopaBankCapsulePrice5 = koopaBankCapsulePrice5[2:]
        elif len(koopaBankCapsulePrice5) == 3:
            koopaBankCapsulePrice5 = "0" + koopaBankCapsulePrice5[2:]
    except:
        koopaBankCapsulePrice5 = "00"

    try:
        bulletBillCapsuleWeight5 = hex(int(bulletBillCapsuleWeight5))
        if len(bulletBillCapsuleWeight5) == 4:
            bulletBillCapsuleWeight5 = bulletBillCapsuleWeight5[2:]
        elif len(bulletBillCapsuleWeight5) == 3:
            bulletBillCapsuleWeight5 = "0" + bulletBillCapsuleWeight5[2:]
    except:
        bulletBillCapsuleWeight5 = "00"

    try:
        bulletBillCapsulePrice5 = hex(int(bulletBillCapsulePrice5))
        if len(bulletBillCapsulePrice5) == 4:
            bulletBillCapsulePrice5 = bulletBillCapsulePrice5[2:]
        elif len(bulletBillCapsulePrice5) == 3:
            bulletBillCapsulePrice5 = "0" + bulletBillCapsulePrice5[2:]
    except:
        bulletBillCapsulePrice5 = "00"

    generatedCode = getCapsuleModsFive(mushroomCapsulePrice5, mushroomCapsuleWeight5, goldenMushroomCapsulePrice5, goldenMushroomCapsuleWeight5, cursedMushroomCapsulePrice5, cursedMushroomCapsuleWeight5, warpPipeCapsulePrice5, warpPipeCapsuleWeight5, kleptoCapsulePrice5, kleptoCapsuleWeight5, podobooCapsulePrice5, podobooCapsuleWeight5, flutterCapsulePrice5, flutterCapsuleWeight5, hammerBroCapsulePrice5, hammerBroCapsuleWeight5, coinBlockCapsulePrice5, coinBlockCapsuleWeight5, spinyCapsulePrice5, spinyCapsuleWeight5, paraTroopaCapsulePrice5, paraTroopaCapsuleWeight5, bulletBillCapsulePrice5, bulletBillCapsuleWeight5, goombaCapsulePrice5, goombaCapsuleWeight5, bombCapsulePrice5, bombCapsuleWeight5, koopaBankCapsulePrice5, koopaBankCapsuleWeight5, kamekCapsulePrice5, kamekCapsuleWeight5, blizzardCapsulePrice5, blizzardCapsuleWeight5, plantCapsulePrice5, plantCapsuleWeight5, magiKoopaCapsulePrice5, magiKoopaCapsuleWeight5, ukikiCapsulePrice5, ukikiCapsuleWeight5, lakituCapsulePrice5, lakituCapsuleWeight5, tweesterCapsulePrice5, tweesterCapsuleWeight5, duelCapsulePrice5, duelCapsuleWeight5, chainChompCapsulePrice5, chainChompCapsuleWeight5, boneCapsulePrice5, boneCapsuleWeight5, bowserCapsulePrice5, bowserCapsuleWeight5, chanceCapsulePrice5, chanceCapsuleWeight5, miracleCapsulePrice5, miracleCapsuleWeight5, dkCapsulePrice5, dkCapsuleWeight5)
    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)

    print("Generated code copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

def savePresetItems5(bombCapsulePrice5, bombCapsuleWeight5, koopaBankCapsulePrice5, koopaBankCapsuleWeight5, bulletBillCapsulePrice5, bulletBillCapsuleWeight5, hammerBroCapsulePrice5, hammerBroCapsuleWeight5, coinBlockCapsulePrice5, coinBlockCapsuleWeight5, duelCapsulePrice5, duelCapsuleWeight5, mushroomCapsulePrice5, mushroomCapsuleWeight5, goldenMushroomCapsulePrice5, goldenMushroomCapsuleWeight5, cursedMushroomCapsulePrice5, cursedMushroomCapsuleWeight5, flutterCapsulePrice5, flutterCapsuleWeight5, spinyCapsulePrice5, spinyCapsuleWeight5, goombaCapsuleWeight5, goombaCapsulePrice5, plantCapsulePrice5, plantCapsuleWeight5, kleptoCapsuleWeight5, kleptoCapsulePrice5, kamekCapsuleWeight5, kamekCapsulePrice5, magiKoopaCapsuleWeight5, magiKoopaCapsulePrice5, blizzardCapsuleWeight5, blizzardCapsulePrice5, podobooCapsulePrice5, podobooCapsuleWeight5, paraTroopaCapsuleWeight5, paraTroopaCapsulePrice5, ukikiCapsulePrice5, ukikiCapsuleWeight5, tweesterCapsulePrice5, tweesterCapsuleWeight5, lakituCapsulePrice5, lakituCapsuleWeight5, warpPipeCapsulePrice5, warpPipeCapsuleWeight5, miracleCapsulePrice5, miracleCapsuleWeight5, boneCapsulePrice5, boneCapsuleWeight5, chanceCapsulePrice5, chanceCapsuleWeight5, chainChompCapsulePrice5, chainChompCapsuleWeight5, bowserCapsulePrice5, bowserCapsuleWeight5, dkCapsulePrice5, dkCapsuleWeight5):
    if not duelCapsulePrice5.get() or not duelCapsuleWeight5.get() or not warpPipeCapsulePrice5.get() or not warpPipeCapsuleWeight5.get() or not mushroomCapsulePrice5.get() or not mushroomCapsuleWeight5.get() or not goldenMushroomCapsulePrice5.get() or not goldenMushroomCapsuleWeight5.get() or not cursedMushroomCapsulePrice5.get() or not cursedMushroomCapsuleWeight5.get() or not kleptoCapsulePrice5.get() or not kleptoCapsuleWeight5.get() or not warpPipeCapsulePrice5.get() or not warpPipeCapsuleWeight5.get() or not flutterCapsulePrice5.get() or not flutterCapsuleWeight5.get() or not cursedMushroomCapsulePrice5.get() or not cursedMushroomCapsuleWeight5.get() or not spinyCapsulePrice5.get() or not spinyCapsuleWeight5.get() or not goombaCapsuleWeight5.get() or not goombaCapsulePrice5.get() or not plantCapsulePrice5.get() or not plantCapsuleWeight5.get() or not kleptoCapsuleWeight5.get() or not kleptoCapsulePrice5.get() or not kamekCapsuleWeight5.get() or not kamekCapsulePrice5.get() or not magiKoopaCapsuleWeight5.get() or not magiKoopaCapsulePrice5.get() or not blizzardCapsuleWeight5.get() or not blizzardCapsulePrice5.get() or not podobooCapsulePrice5.get() or not podobooCapsuleWeight5.get() or not paraTroopaCapsuleWeight5.get() or not paraTroopaCapsulePrice5.get() or not magiKoopaCapsulePrice5.get() or not magiKoopaCapsuleWeight5.get() or not ukikiCapsulePrice5.get() or not ukikiCapsuleWeight5.get() or not tweesterCapsulePrice5.get() or not tweesterCapsuleWeight5.get() or not lakituCapsulePrice5.get() or not lakituCapsuleWeight5.get() or not warpPipeCapsulePrice5.get() or not warpPipeCapsuleWeight5.get() or not miracleCapsulePrice5.get() or not miracleCapsuleWeight5.get() or not boneCapsulePrice5.get() or not boneCapsuleWeight5.get() or not chanceCapsulePrice5.get() or not chanceCapsuleWeight5.get() or not chainChompCapsulePrice5.get() or not chainChompCapsuleWeight5.get() or not bowserCapsulePrice5.get() or not bowserCapsuleWeight5.get() or not dkCapsulePrice5.get() or not dkCapsuleWeight5.get():
        createDialog("Error", "error", "Please fill out all the boxes.", None)
        return

    mushroomCapsulePrice5 = mushroomCapsulePrice5.get()
    mushroomCapsuleWeight5 = mushroomCapsuleWeight5.get()

    kamekCapsuleWeight5 = kamekCapsuleWeight5.get()
    kamekCapsulePrice5 = kamekCapsulePrice5.get()
    
    goldenMushroomCapsulePrice5 = goldenMushroomCapsulePrice5.get()
    goldenMushroomCapsuleWeight5 = goldenMushroomCapsuleWeight5.get()

    cursedMushroomCapsulePrice5 = cursedMushroomCapsulePrice5.get()
    cursedMushroomCapsuleWeight5 = cursedMushroomCapsuleWeight5.get()

    goombaCapsulePrice5 = goombaCapsulePrice5.get()
    goombaCapsuleWeight5 = goombaCapsuleWeight5.get()

    kleptoCapsulePrice5 = kleptoCapsulePrice5.get()
    kleptoCapsuleWeight5 = kleptoCapsuleWeight5.get()

    flutterCapsulePrice5 = flutterCapsulePrice5.get()
    flutterCapsuleWeight5 = flutterCapsuleWeight5.get()

    podobooCapsulePrice5 = podobooCapsulePrice5.get()
    podobooCapsuleWeight5 = podobooCapsuleWeight5.get()

    spinyCapsulePrice5 = spinyCapsulePrice5.get()
    spinyCapsuleWeight5 = spinyCapsuleWeight5.get()

    coinBlockCapsulePrice5 = coinBlockCapsulePrice5.get()
    coinBlockCapsuleWeight5 = coinBlockCapsuleWeight5.get()

    plantCapsulePrice5 = plantCapsulePrice5.get()
    plantCapsuleWeight5 = plantCapsuleWeight5.get()

    hammerBroCapsulePrice5 = hammerBroCapsulePrice5.get()
    hammerBroCapsuleWeight5 = hammerBroCapsuleWeight5.get()

    bulletBillCapsulePrice5 = bulletBillCapsulePrice5.get()
    bulletBillCapsuleWeight5 = bulletBillCapsuleWeight5.get()

    blizzardCapsulePrice5 = blizzardCapsulePrice5.get()
    blizzardCapsuleWeight5 = blizzardCapsuleWeight5.get()

    paraTroopaCapsulePrice5 = paraTroopaCapsulePrice5.get()
    paraTroopaCapsuleWeight5 = paraTroopaCapsuleWeight5.get()

    magiKoopaCapsulePrice5 = magiKoopaCapsulePrice5.get()
    magiKoopaCapsuleWeight5 = magiKoopaCapsuleWeight5.get()

    ukikiCapsulePrice5 = ukikiCapsulePrice5.get()
    ukikiCapsuleWeight5 = ukikiCapsuleWeight5.get()

    tweesterCapsulePrice5 = tweesterCapsulePrice5.get()
    tweesterCapsuleWeight5 = tweesterCapsuleWeight5.get()

    lakituCapsulePrice5 = lakituCapsulePrice5.get()
    lakituCapsuleWeight5 = lakituCapsuleWeight5.get()

    warpPipeCapsulePrice5 = warpPipeCapsulePrice5.get()
    warpPipeCapsuleWeight5 = warpPipeCapsuleWeight5.get()

    miracleCapsulePrice5 = miracleCapsulePrice5.get()
    miracleCapsuleWeight5 = miracleCapsuleWeight5.get()

    boneCapsulePrice5 = boneCapsulePrice5.get()
    boneCapsuleWeight5 = boneCapsuleWeight5.get()

    chainChompCapsulePrice5 = chainChompCapsulePrice5.get()
    chainChompCapsuleWeight5 = chainChompCapsuleWeight5.get()

    chanceCapsulePrice5 = chanceCapsulePrice5.get()
    chanceCapsuleWeight5 = chanceCapsuleWeight5.get()

    bowserCapsulePrice5 = bowserCapsulePrice5.get()
    bowserCapsuleWeight5 = bowserCapsuleWeight5.get()

    dkCapsulePrice5 = dkCapsulePrice5.get()
    dkCapsuleWeight5 = dkCapsuleWeight5.get()

    duelCapsulePrice5 = duelCapsulePrice5.get()
    duelCapsuleWeight5 = duelCapsuleWeight5.get()

    koopaBankCapsulePrice5 = koopaBankCapsulePrice5.get()
    koopaBankCapsuleWeight5 = koopaBankCapsuleWeight5.get()

    bombCapsulePrice5 = bombCapsulePrice5.get()
    bombCapsuleWeight5 = bombCapsuleWeight5.get()

    prices5 = [mushroomCapsulePrice5, kamekCapsulePrice5, goldenMushroomCapsulePrice5, cursedMushroomCapsulePrice5, goombaCapsulePrice5, kleptoCapsulePrice5, flutterCapsulePrice5, podobooCapsulePrice5, spinyCapsulePrice5, coinBlockCapsulePrice5, plantCapsulePrice5, hammerBroCapsulePrice5, bulletBillCapsulePrice5, blizzardCapsulePrice5, paraTroopaCapsulePrice5, magiKoopaCapsulePrice5, ukikiCapsulePrice5, tweesterCapsulePrice5, lakituCapsulePrice5, warpPipeCapsulePrice5, miracleCapsulePrice5, boneCapsulePrice5, chainChompCapsulePrice5, chanceCapsulePrice5, bowserCapsulePrice5, dkCapsulePrice5, duelCapsulePrice5, koopaBankCapsulePrice5, bombCapsulePrice5]
    weights5 = [mushroomCapsuleWeight5, kamekCapsuleWeight5, goldenMushroomCapsuleWeight5, cursedMushroomCapsuleWeight5, goombaCapsuleWeight5, kleptoCapsuleWeight5, flutterCapsuleWeight5, podobooCapsuleWeight5, spinyCapsuleWeight5, coinBlockCapsuleWeight5, plantCapsuleWeight5, hammerBroCapsuleWeight5, bulletBillCapsuleWeight5, blizzardCapsuleWeight5, paraTroopaCapsuleWeight5, magiKoopaCapsuleWeight5, ukikiCapsuleWeight5, tweesterCapsuleWeight5, lakituCapsuleWeight5, warpPipeCapsuleWeight5, miracleCapsuleWeight5, boneCapsuleWeight5, chainChompCapsuleWeight5, chanceCapsuleWeight5, bowserCapsuleWeight5, dkCapsuleWeight5, duelCapsuleWeight5, koopaBankCapsuleWeight5, bombCapsuleWeight5]

    file_path = tkinter.filedialog.asksaveasfilename(defaultextension=".mpt", filetypes=[("MPT files", "*.mpt")])
    if file_path:
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Prices', 'Weights'])
            for price, weight in zip(prices5, weights5):
                writer.writerow([price, weight])
        print("MPT file saved successfully!")
        createDialog("Operation Sucessful", "success", "Presets file saved successfully!.", None)

def loadPresetItems5(bombCapsulePrice5, bombCapsuleWeight5, koopaBankCapsulePrice5, koopaBankCapsuleWeight5, bulletBillCapsulePrice5, bulletBillCapsuleWeight5, hammerBroCapsulePrice5, hammerBroCapsuleWeight5, coinBlockCapsulePrice5, coinBlockCapsuleWeight5, duelCapsulePrice5, duelCapsuleWeight5, mushroomCapsulePrice5, mushroomCapsuleWeight5, goldenMushroomCapsulePrice5, goldenMushroomCapsuleWeight5, cursedMushroomCapsulePrice5, cursedMushroomCapsuleWeight5, flutterCapsulePrice5, flutterCapsuleWeight5, spinyCapsulePrice5, spinyCapsuleWeight5, goombaCapsuleWeight5, goombaCapsulePrice5, plantCapsulePrice5, plantCapsuleWeight5, kleptoCapsuleWeight5, kleptoCapsulePrice5, kamekCapsuleWeight5, kamekCapsulePrice5, magiKoopaCapsuleWeight5, magiKoopaCapsulePrice5, blizzardCapsuleWeight5, blizzardCapsulePrice5, podobooCapsulePrice5, podobooCapsuleWeight5, paraTroopaCapsuleWeight5, paraTroopaCapsulePrice5, ukikiCapsulePrice5, ukikiCapsuleWeight5, tweesterCapsulePrice5, tweesterCapsuleWeight5, lakituCapsulePrice5, lakituCapsuleWeight5, warpPipeCapsulePrice5, warpPipeCapsuleWeight5, miracleCapsulePrice5, miracleCapsuleWeight5, boneCapsulePrice5, boneCapsuleWeight5, chanceCapsulePrice5, chanceCapsuleWeight5, chainChompCapsulePrice5, chainChompCapsuleWeight5, bowserCapsulePrice5, bowserCapsuleWeight5, dkCapsulePrice5, dkCapsuleWeight5):
    file_path = tkinter.filedialog.askopenfilename(defaultextension=".mpt", filetypes=[("MPT files", "*.mpt")])
    if file_path:
        prices5In = []
        weights5In = []
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                prices5In.append(float(row[0]))
                weights5In.append(float(row[1]))
        # Define a list of Entry widget attributes
        pricesNames5 = [mushroomCapsulePrice5, kamekCapsulePrice5, goldenMushroomCapsulePrice5, cursedMushroomCapsulePrice5, goombaCapsulePrice5, kleptoCapsulePrice5, flutterCapsulePrice5, podobooCapsulePrice5, spinyCapsulePrice5, coinBlockCapsulePrice5, plantCapsulePrice5, hammerBroCapsulePrice5, bulletBillCapsulePrice5, blizzardCapsulePrice5, paraTroopaCapsulePrice5, magiKoopaCapsulePrice5, ukikiCapsulePrice5, tweesterCapsulePrice5, lakituCapsulePrice5, warpPipeCapsulePrice5, miracleCapsulePrice5, boneCapsulePrice5, chainChompCapsulePrice5, chanceCapsulePrice5, bowserCapsulePrice5, dkCapsulePrice5, duelCapsulePrice5, koopaBankCapsulePrice5, bombCapsulePrice5]
        weightsNames5 = [mushroomCapsuleWeight5, kamekCapsuleWeight5, goldenMushroomCapsuleWeight5, cursedMushroomCapsuleWeight5, goombaCapsuleWeight5, kleptoCapsuleWeight5, flutterCapsuleWeight5, podobooCapsuleWeight5, spinyCapsuleWeight5, coinBlockCapsuleWeight5, plantCapsuleWeight5, hammerBroCapsuleWeight5, bulletBillCapsuleWeight5, blizzardCapsuleWeight5, paraTroopaCapsuleWeight5, magiKoopaCapsuleWeight5, ukikiCapsuleWeight5, tweesterCapsuleWeight5, lakituCapsuleWeight5, warpPipeCapsuleWeight5, miracleCapsuleWeight5, boneCapsuleWeight5, chainChompCapsuleWeight5, chanceCapsuleWeight5, bowserCapsuleWeight5, dkCapsuleWeight5, duelCapsuleWeight5, koopaBankCapsuleWeight5, bombCapsuleWeight5]
        # Update widgets with loaded values
        for index, widget in enumerate(pricesNames5):
            if widget and index < len(prices5In):
                widget.delete(0, 'end')
                widget.insert(0, int(prices5In[index]))
        for index, widget in enumerate(weightsNames5):
            if widget and index < len(weights5In):
                widget.delete(0, 'end')
                widget.insert(0, int(weights5In[index]))
        print("MPT file laoded successfully!")
        createDialog("Operation Sucessful", "success", "Presets file saved successfully!.", None)

def fillViaCode5(top, codeText, bombCapsulePrice5, bombCapsuleWeight5, koopaBankCapsulePrice5, koopaBankCapsuleWeight5, bulletBillCapsulePrice5, bulletBillCapsuleWeight5, hammerBroCapsulePrice5, hammerBroCapsuleWeight5, coinBlockCapsulePrice5, coinBlockCapsuleWeight5, duelCapsulePrice5, duelCapsuleWeight5, mushroomCapsulePrice5, mushroomCapsuleWeight5, goldenMushroomCapsulePrice5, goldenMushroomCapsuleWeight5, cursedMushroomCapsulePrice5, cursedMushroomCapsuleWeight5, flutterCapsulePrice5, flutterCapsuleWeight5, spinyCapsulePrice5, spinyCapsuleWeight5, goombaCapsuleWeight5, goombaCapsulePrice5, plantCapsulePrice5, plantCapsuleWeight5, kleptoCapsuleWeight5, kleptoCapsulePrice5, kamekCapsuleWeight5, kamekCapsulePrice5, magiKoopaCapsuleWeight5, magiKoopaCapsulePrice5, blizzardCapsuleWeight5, blizzardCapsulePrice5, podobooCapsulePrice5, podobooCapsuleWeight5, paraTroopaCapsuleWeight5, paraTroopaCapsulePrice5, ukikiCapsulePrice5, ukikiCapsuleWeight5, tweesterCapsulePrice5, tweesterCapsuleWeight5, lakituCapsulePrice5, lakituCapsuleWeight5, warpPipeCapsulePrice5, warpPipeCapsuleWeight5, miracleCapsulePrice5, miracleCapsuleWeight5, boneCapsulePrice5, boneCapsuleWeight5, chanceCapsulePrice5, chanceCapsuleWeight5, chainChompCapsulePrice5, chainChompCapsuleWeight5, bowserCapsulePrice5, bowserCapsuleWeight5, dkCapsulePrice5, dkCapsuleWeight5):
    code5 = []
    code_single5 = []
    weight_code5 = []
    price_code5 = []
    weights5 = []
    weights5In = []
    prices5 = []
    prices5In = []
    names = ["Mushroom", "Super Mushroom", "Cursed Mushroom", "Warp Pipe", "Klepto", "Bubble", "Wiggler", "Hammer Brother", "Coin Block", "Spiny", "Paratroopa", "Bullet Bill", "Goomba", "Bomomb", "Koopa Bank", "Kamek", "Mr. Blizzard", "Piranha Plant", "Magikoopa", "Ukiki", "Lakitu", "Tweester", "Duel", "Chain Chomp", "Bone", "Bowser", "Chance", "Miracle", "Donkey Kong"]
    current_line5 = ""

    code5.append(codeText.get("1.0", "end"))
    
    try:
        for i in range(0, 21):
            current_line5 = current_line5 + code5[0][i]

        if current_line5 == "MP5 - Capsule Modifer":
            current_line5 = ""
            
            for i in range(22, 1210):
                if code5[0][i] != " " and code5[0][i] != "\n":
                    current_line5 = current_line5 + code5[0][i]
                else:
                    code_single5.append(current_line5)
                    current_line5 = ""
        else:
            current_line5 = ""
            
            for i in range(0, 1188):
                if code5[0][i] != " " and code5[0][i] != "\n":
                    current_line5 = current_line5 + code5[0][i]
                else:
                    code_single5.append(current_line5)
                    current_line5 = ""
    except IndexError:
        createDialog("Error", "error", "Invalid Code", None)
        return
    
    del code_single5[0:8]
    del code_single5[29:67]

    for i in range(30, 58):
        del code_single5[i]
    
    for i in range(29):
        weight_code5.append(code_single5[i])
    
    for i in range(29):
        price_code5.append(code_single5[i + 29])

    for line in weight_code5:
        weights5.append(line[2:4])
    
    for line in price_code5:
        prices5.append(line[6:8])
    
    for weight in weights5:
        weights5In.append(int(weight, 16))
    
    for price in prices5:
        prices5In.append(int(price, 16))

    weights5In.insert(1, weights5In.pop(15))
    weights5In.insert(4, weights5In.pop(13))
    weights5In.insert(5, weights5In.pop(6))
    weights5In.insert(6, weights5In.pop(8))
    weights5In.insert(7, weights5In.pop(8))
    weights5In.insert(8, weights5In.pop(11))
    weights5In.insert(9, weights5In.pop(11))
    weights5In.insert(10, weights5In.pop(17))
    weights5In.insert(11, weights5In.pop(12))
    weights5In.insert(12, weights5In.pop(14))
    weights5In.insert(13, weights5In.pop(17))
    weights5In.insert(14, weights5In.pop(15))
    weights5In.insert(15, weights5In.pop(18))
    weights5In.insert(16, weights5In.pop(19))
    weights5In.insert(17, weights5In.pop(21))
    weights5In.insert(18, weights5In.pop(21))
    weights5In.insert(20, weights5In.pop(27))
    weights5In.insert(21, weights5In.pop(25))
    weights5In.insert(22, weights5In.pop(25))
    weights5In.insert(23, weights5In.pop(27))
    weights5In.insert(24, weights5In.pop(27))
    weights5In.insert(25, weights5In.pop(28))
    weights5In.insert(26, weights5In.pop(28))
    weights5In.insert(27, weights5In.pop(28))

    prices5In.insert(1, prices5In.pop(15))
    prices5In.insert(4, prices5In.pop(13))
    prices5In.insert(5, prices5In.pop(6))
    prices5In.insert(6, prices5In.pop(8))
    prices5In.insert(7, prices5In.pop(8))
    prices5In.insert(8, prices5In.pop(11))
    prices5In.insert(9, prices5In.pop(11))
    prices5In.insert(10, prices5In.pop(17))
    prices5In.insert(11, prices5In.pop(12))
    prices5In.insert(12, prices5In.pop(14))
    prices5In.insert(13, prices5In.pop(17))
    prices5In.insert(14, prices5In.pop(15))
    prices5In.insert(15, prices5In.pop(18))
    prices5In.insert(16, prices5In.pop(19))
    prices5In.insert(17, prices5In.pop(21))
    prices5In.insert(18, prices5In.pop(21))
    prices5In.insert(20, prices5In.pop(27))
    prices5In.insert(21, prices5In.pop(25))
    prices5In.insert(22, prices5In.pop(25))
    prices5In.insert(23, prices5In.pop(27))
    prices5In.insert(24, prices5In.pop(27))
    prices5In.insert(25, prices5In.pop(28))
    prices5In.insert(26, prices5In.pop(28))
    prices5In.insert(27, prices5In.pop(28))
        
    # Define a list of Entry widget attributes
    pricesNames5 = [mushroomCapsulePrice5, kamekCapsulePrice5, goldenMushroomCapsulePrice5, cursedMushroomCapsulePrice5, goombaCapsulePrice5, kleptoCapsulePrice5, flutterCapsulePrice5, podobooCapsulePrice5, spinyCapsulePrice5, coinBlockCapsulePrice5, plantCapsulePrice5, hammerBroCapsulePrice5, bulletBillCapsulePrice5, blizzardCapsulePrice5, paraTroopaCapsulePrice5, magiKoopaCapsulePrice5, ukikiCapsulePrice5, tweesterCapsulePrice5, lakituCapsulePrice5, warpPipeCapsulePrice5, miracleCapsulePrice5, boneCapsulePrice5, chainChompCapsulePrice5, chanceCapsulePrice5, bowserCapsulePrice5, dkCapsulePrice5, duelCapsulePrice5, koopaBankCapsulePrice5, bombCapsulePrice5]
    weightsNames5 = [mushroomCapsuleWeight5, kamekCapsuleWeight5, goldenMushroomCapsuleWeight5, cursedMushroomCapsuleWeight5, goombaCapsuleWeight5, kleptoCapsuleWeight5, flutterCapsuleWeight5, podobooCapsuleWeight5, spinyCapsuleWeight5, coinBlockCapsuleWeight5, plantCapsuleWeight5, hammerBroCapsuleWeight5, bulletBillCapsuleWeight5, blizzardCapsuleWeight5, paraTroopaCapsuleWeight5, magiKoopaCapsuleWeight5, ukikiCapsuleWeight5, tweesterCapsuleWeight5, lakituCapsuleWeight5, warpPipeCapsuleWeight5, miracleCapsuleWeight5, boneCapsuleWeight5, chainChompCapsuleWeight5, chanceCapsuleWeight5, bowserCapsuleWeight5, dkCapsuleWeight5, duelCapsuleWeight5, koopaBankCapsuleWeight5, bombCapsuleWeight5]
    # Update widgets with loaded values
    for index, widget in enumerate(pricesNames5):
        if widget and index < len(prices5In):
            widget.delete(0, 'end')
            widget.insert(0, int(prices5In[index]))
    for index, widget in enumerate(weightsNames5):
        if widget and index < len(weights5In):
            widget.delete(0, 'end')
            widget.insert(0, int(weights5In[index]))
    print("Code loaded successfully!")
    
    top.destroy()

    createDialog("Operation Sucessful", "success", "Code loaded successfully!.", None)