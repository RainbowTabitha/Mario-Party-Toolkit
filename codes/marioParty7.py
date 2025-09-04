# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 2/21/2024
# License: MIT
# ============================================

def getBlueSpaceCodeSeven(amount, amountDec):
    return f'''
MP7 - Blue Spaces Give {amountDec} Coins
C2168578 00000001
60000000 00000000
C216857C 3880{amount}
60000000 00000000
'''

def getRedSpaceCodeSeven(amount, amountDec):
    return f'''
MP7 - Red Spaces Take Away {amountDec} Coins
C2168600 00000001
60000000 00000000
C2168604 3880{amount}
60000000 00000000
'''

def getCharacterSpaceCodeSeven(amount, amountDec):
    return f'''
MP7 - Character Spaces Give {amountDec} Coins
C21685B8 00000001
3880{amount} 00000000
'''

def getMinigameCodeSeven(amount, amountDec):
    return f'''
MP7 - Minigames Award {amountDec} Coins
C20098A4 00000012
3DC08029 61CE1559
89EE0000 2C0F0004
41820068 2C0F001A
41820060 2C0F002B
41820058 2C0F002F
41820050 2C0F0030
41820048 2C0F0031
41820040 2C0F0037
41820038 2C0F0038
41820030 3DC08029
61CE0CCA A1EE0000
2C0F0000 4182000C
39E0{amount} B1EE0000
39CE0110 3A100001
2C100003 4081FFE0
3800FFFF 39C00000
39E00000 3A000000
60000000 00000000
'''

def getStarSpaceCodeSeven(amount, amountDec, x2, x3, x4):
    return f'''
MP7 - Stars Cost {amountDec} Coins
C2188774 00000001
3B80{amount} 00000000
204E0640 38030001
C24E0644 00000001
1C00000A 00000000
C24E0574 00000001
3800{amount} 00000000
C24E08D8 00000001
3800{amount} 00000000
C24E09B8 00000001
1C00000A 00000000
C24E0BAC 00000001
38A0{amount} 00000000
C24E0C8C 00000001
1C60000A 00000000
E2000001 80008000
204F92AC 804F929D
044F9268 0000{amount}
044F926C 0000{x2}
044F9270 0000{x3}
044F9274 0000{x4}
E2000001 80008000
'''

def getStarSpaceCodeSevenLastFive(amount, amountDec):
    return f'''
MP7 - Stars Cost {amountDec} Coins During the Last 5 Turns Event
C218876C 00000001
3B80{amount} 00000000
'''

def getHammerBroSpaceCodeSeven(amount, negAmount, halfAmount, amountDec):
    return f'''
MP7 - Hammer Bro Takes {amountDec} Coins
C21A902C 00000002
3AC0{amount} 38A0{negAmount}
60000000 00000000
C21A973C 00000001
38000000 00000000
C21A9744 00000002
3800{halfAmount} 38000000
60000000 00000000
C21A9754 00000001
3800{halfAmount} 00000000
'''

def getZapSpaceCodeSeven(amount, amountDec):
    return f'''
MP7 - Zap Takes {amountDec} Coins
C21B652C 00000001
3880{amount} 00000000
'''

def getFlowerSpaceCodeSeven(amount, amountDec):
    return f'''
MP7 - Flower Gives {amountDec} Coins Per Space
C21C4F24 00000001
3B40{amount} 00000000
'''

def getVacuumSpaceCodeSeven(amount, amountDec):
    return f'''
MP7 - Vaccum Always Steals {amountDec} Coins
C21C8A34 00000001
3860{amount} 00000000
'''

def getFireballSpaceCodeSeven(amount, negAmount, amountDec):
    return f'''
MP7 - Fireball Takes {amountDec} Coins
C21C1464 00000001
3B80{amount} 00000000
C21C148C 00000001
38A0{negAmount} 00000000
'''

def getMinigameReplacement7(hexUno, hexDos, gameUno, gameDos):
    return f'''
MP7 - Minigame Replacement: {gameUno} ➜ {gameDos}
28291558 000000{hexUno}
02291558 000000{hexDos}
E2000001 80008000
'''

def getOrbModsSeven(mushroomCapsulePrice1, mushroomCapsulePrice2, mushroomCapsulePrice34, mushroomCapsuleShopOdds12, mushroomCapsuleShopOdds34, mushroomCapsuleSpaceOdds1,mushroomCapsuleSpaceOdds2, mushroomCapsuleSpaceOdds34, goldenMushroomCapsulePrice1, goldenMushroomCapsulePrice2, goldenMushroomCapsulePrice34, goldenMushroomCapsuleShopOdds12, goldenMushroomCapsuleShopOdds34, goldenMushroomCapsuleSpaceOdds1, goldenMushroomCapsuleSpaceOdds2, goldenMushroomCapsuleSpaceOdds34, slowMushroomCapsulePrice1, slowMushroomCapsulePrice2, slowMushroomCapsulePrice34, slowMushroomCapsuleShopOdds12, slowMushroomCapsuleShopOdds34, slowMushroomCapsuleSpaceOdds1, slowMushroomCapsuleSpaceOdds2, slowMushroomCapsuleSpaceOdds34, metalMushroomCapsulePrice1, metalMushroomCapsulePrice2, metalMushroomCapsulePrice34, metalMushroomCapsuleShopOdds12, metalMushroomCapsuleShopOdds34, metalMushroomCapsuleSpaceOdds1, metalMushroomCapsuleSpaceOdds2, metalMushroomCapsuleSpaceOdds34, flutterCapsulePrice1, flutterCapsulePrice2, flutterCapsulePrice34, flutterCapsuleShopOdds12, flutterCapsuleShopOdds34, flutterCapsuleSpaceOdds1, flutterCapsuleSpaceOdds2, flutterCapsuleSpaceOdds34, cannonCapsulePrice1, cannonCapsulePrice2, cannonCapsulePrice34, cannonCapsuleShopOdds12, cannonCapsuleShopOdds34, cannonCapsuleSpaceOdds1, cannonCapsuleSpaceOdds2, cannonCapsuleSpaceOdds34, snackCapsulePrice1, snackCapsulePrice2, snackCapsulePrice34, snackCapsuleShopOdds12, snackCapsuleShopOdds34, snackCapsuleSpaceOdds1, snackCapsuleSpaceOdds2, snackCapsuleSpaceOdds34, lakituCapsulePrice1, lakituCapsulePrice2, lakituCapsulePrice34, lakituCapsuleShopOdds12, lakituCapsuleShopOdds34, lakituCapsuleSpaceOdds1, lakituCapsuleSpaceOdds2, lakituCapsuleSpaceOdds34, hammerBroCapsulePrice1, hammerBroCapsulePrice2, hammerBroCapsulePrice34, hammerBroCapsuleShopOdds12, hammerBroCapsuleShopOdds34, hammerBroCapsuleSpaceOdds1, hammerBroCapsuleSpaceOdds2, hammerBroCapsuleSpaceOdds34, piranhaPlantCapsulePrice1, piranhaPlantCapsulePrice2, piranhaPlantCapsulePrice34, piranhaPlantCapsuleShopOdds12, piranhaPlantCapsuleShopOdds34, piranhaPlantCapsuleSpaceOdds1, piranhaPlantCapsuleSpaceOdds2, piranhaPlantCapsuleSpaceOdds34, spearGuyCapsulePrice1, spearGuyCapsulePrice2, spearGuyCapsulePrice34, spearGuyCapsuleShopOdds12, spearGuyCapsuleShopOdds34, spearGuyCapsuleSpaceOdds1, spearGuyCapsuleSpaceOdds2, spearGuyCapsuleSpaceOdds34, kamekCapsulePrice1, kamekCapsulePrice2, kamekCapsulePrice34, kamekCapsuleShopOdds12, kamekCapsuleShopOdds34, kamekCapsuleSpaceOdds1, kamekCapsuleSpaceOdds2, kamekCapsuleSpaceOdds34, toadyCapsulePrice1, toadyCapsulePrice2, toadyCapsulePrice34, toadyCapsuleShopOdds12, toadyCapsuleShopOdds34, toadyCapsuleSpaceOdds1, toadyCapsuleSpaceOdds2, toadyCapsuleSpaceOdds34, mrBlizzardCapsulePrice1, mrBlizzardCapsulePrice2, mrBlizzardCapsulePrice34, mrBlizzardCapsuleShopOdds12, mrBlizzardCapsuleShopOdds34, mrBlizzardCapsuleSpaceOdds1, mrBlizzardCapsuleSpaceOdds2, mrBlizzardCapsuleSpaceOdds34, banditCapsulePrice1, banditCapsulePrice2, banditCapsulePrice34, banditCapsuleShopOdds12, banditCapsuleShopOdds34, banditCapsuleSpaceOdds1, banditCapsuleSpaceOdds2, banditCapsuleSpaceOdds34, pinkBooCapsulePrice1, pinkBooCapsulePrice2, pinkBooCapsulePrice34, pinkBooCapsuleShopOdds12, pinkBooCapsuleShopOdds34, pinkBooCapsuleSpaceOdds1, pinkBooCapsuleSpaceOdds2, pinkBooCapsuleSpaceOdds34, spinyCapsulePrice1, spinyCapsulePrice2, spinyCapsulePrice34, spinyCapsuleShopOdds12, spinyCapsuleShopOdds34, spinyCapsuleSpaceOdds1, spinyCapsuleSpaceOdds2, spinyCapsuleSpaceOdds34, zapCapsulePrice1, zapCapsulePrice2, zapCapsulePrice34, zapCapsuleShopOdds12, zapCapsuleShopOdds34, zapCapsuleSpaceOdds1, zapCapsuleSpaceOdds2, zapCapsuleSpaceOdds34, tweesterCapsulePrice1, tweesterCapsulePrice2, tweesterCapsulePrice34, tweesterCapsuleShopOdds12, tweesterCapsuleShopOdds34, tweesterCapsuleSpaceOdds1, tweesterCapsuleSpaceOdds2, tweesterCapsuleSpaceOdds34, thwompCapsulePrice1, thwompCapsulePrice2, thwompCapsulePrice34, thwompCapsuleShopOdds12, thwompCapsuleShopOdds34, thwompCapsuleSpaceOdds1, thwompCapsuleSpaceOdds2, thwompCapsuleSpaceOdds34, warpCapsulePrice1, warpCapsulePrice2, warpCapsulePrice34, warpCapsuleShopOdds12, warpCapsuleShopOdds34, warpCapsuleSpaceOdds1, warpCapsuleSpaceOdds2, warpCapsuleSpaceOdds34, bombCapsulePrice1, bombCapsulePrice2, bombCapsulePrice34, bombCapsuleShopOdds12, bombCapsuleShopOdds34, bombCapsuleSpaceOdds1, bombCapsuleSpaceOdds2, bombCapsuleSpaceOdds34, fireballCapsulePrice1, fireballCapsulePrice2, fireballCapsulePrice34, fireballCapsuleShopOdds12, fireballCapsuleShopOdds34, fireballCapsuleSpaceOdds1, fireballCapsuleSpaceOdds2, fireballCapsuleSpaceOdds34, flowerCapsulePrice1, flowerCapsulePrice2, flowerCapsulePrice34, flowerCapsuleShopOdds12, flowerCapsuleShopOdds34, flowerCapsuleSpaceOdds1, flowerCapsuleSpaceOdds2, flowerCapsuleSpaceOdds34, eggCapsulePrice1, eggCapsulePrice2, eggCapsulePrice34, eggCapsuleShopOdds12, eggCapsuleShopOdds34, eggCapsuleSpaceOdds1, eggCapsuleSpaceOdds2, eggCapsuleSpaceOdds34, vacuumCapsulePrice1, vacuumCapsulePrice2, vacuumCapsulePrice34, vacuumCapsuleShopOdds12, vacuumCapsuleShopOdds34, vacuumCapsuleSpaceOdds1, vacuumCapsuleSpaceOdds2, vacuumCapsuleSpaceOdds34, magicCapsulePrice1, magicCapsulePrice2, magicCapsulePrice34, magicCapsuleShopOdds12, magicCapsuleShopOdds34, magicCapsuleSpaceOdds1, magicCapsuleSpaceOdds2, magicCapsuleSpaceOdds34, tripleCapsulePrice1, tripleCapsulePrice2, tripleCapsulePrice34, tripleCapsuleShopOdds12, tripleCapsuleShopOdds34, tripleCapsuleSpaceOdds1, tripleCapsuleSpaceOdds2, tripleCapsuleSpaceOdds34, koopaCapsulePrice1, koopaCapsulePrice2, koopaCapsulePrice34, koopaCapsuleShopOdds12, koopaCapsuleShopOdds34, koopaCapsuleSpaceOdds1, koopaCapsuleSpaceOdds2, koopaCapsuleSpaceOdds34, poisonMushroomPrice1, poisonMushroomPrice2, poisonMushroomPrice34, poisonMushroomShopOdds12, poisonMushroomShopOdds34, poisonMushroomSpaceOdds1, poisonMushroomSpaceOdds2, poisonMushroomSpaceOdds34, orbBagCapsulePrice1, orbBagCapsulePrice2, orbBagCapsulePrice34, orbBagCapsuleShopOdds12, orbBagCapsuleShopOdds34, orbBagCapsuleSpaceOdds1, orbBagCapsuleSpaceOdds2, orbBagCapsuleSpaceOdds34, mysteryCapsulePrice1, mysteryCapsulePrice2, mysteryCapsulePrice34, mysteryCapsuleShopOdds12, mysteryCapsuleShopOdds34, mysteryCapsuleSpaceOdds1, mysteryCapsuleSpaceOdds2, mysteryCapsuleSpaceOdds34, dkCapsulePrice1, dkCapsulePrice2, dkCapsulePrice34, dkCapsuleShopOdds12, dkCapsuleShopOdds34, dkCapsuleSpaceOdds1, dkCapsuleSpaceOdds2, dkCapsuleSpaceOdds34, duelCapsulePrice1, duelCapsulePrice2, duelCapsulePrice34, duelCapsuleShopOdds12, duelCapsuleShopOdds34, duelCapsuleSpaceOdds1, duelCapsuleSpaceOdds2, duelCapsuleSpaceOdds34):
    return f'''
MP7 - Orb Modifer
042EF588 00{mushroomCapsulePrice1}{mushroomCapsulePrice2}{mushroomCapsulePrice34}
042EF58C {mushroomCapsuleSpaceOdds1}{mushroomCapsuleSpaceOdds2}{mushroomCapsuleSpaceOdds34}{mushroomCapsuleSpaceOdds34}
042EF590 {mushroomCapsuleSpaceOdds1}{mushroomCapsuleSpaceOdds2}{mushroomCapsuleSpaceOdds34}{mushroomCapsuleSpaceOdds34}
042EF594 {mushroomCapsuleShopOdds12}{mushroomCapsuleShopOdds34}0000
042EF598 01{goldenMushroomCapsulePrice1}{goldenMushroomCapsulePrice2}{goldenMushroomCapsulePrice34}
042EF59C {goldenMushroomCapsuleSpaceOdds1}{goldenMushroomCapsuleSpaceOdds2}{goldenMushroomCapsuleSpaceOdds34}{goldenMushroomCapsuleSpaceOdds34}
042EF5A0 {goldenMushroomCapsuleSpaceOdds1}{goldenMushroomCapsuleSpaceOdds2}{goldenMushroomCapsuleSpaceOdds34}{goldenMushroomCapsuleSpaceOdds34}
042EF5A4 {goldenMushroomCapsuleShopOdds12}{goldenMushroomCapsuleShopOdds34}0000
042EF5A8 02{slowMushroomCapsulePrice1}{slowMushroomCapsulePrice2}{slowMushroomCapsulePrice34}
042EF5AC {slowMushroomCapsuleSpaceOdds1}{slowMushroomCapsuleSpaceOdds2}{slowMushroomCapsuleSpaceOdds34}{slowMushroomCapsuleSpaceOdds34}
042EF5B0 {slowMushroomCapsuleSpaceOdds1}{slowMushroomCapsuleSpaceOdds2}{slowMushroomCapsuleSpaceOdds34}{slowMushroomCapsuleSpaceOdds34}
042EF5B4 {slowMushroomCapsuleShopOdds12}{slowMushroomCapsuleShopOdds34}0000
042EF5B8 03{metalMushroomCapsulePrice1}{metalMushroomCapsulePrice2}{metalMushroomCapsulePrice34}
042EF5BC {metalMushroomCapsuleSpaceOdds1}{metalMushroomCapsuleSpaceOdds2}{metalMushroomCapsuleSpaceOdds34}{metalMushroomCapsuleSpaceOdds34}
042EF5C0 {metalMushroomCapsuleSpaceOdds1}{metalMushroomCapsuleSpaceOdds2}{metalMushroomCapsuleSpaceOdds34}{metalMushroomCapsuleSpaceOdds34}
042EF5C4 {metalMushroomCapsuleShopOdds12}{metalMushroomCapsuleShopOdds34}0000
042EF5C8 04{flutterCapsulePrice1}{flutterCapsulePrice2}{flutterCapsulePrice34}
042EF5CC {flutterCapsuleSpaceOdds1}{flutterCapsuleSpaceOdds2}{flutterCapsuleSpaceOdds34}{flutterCapsuleSpaceOdds34}
042EF5D0 {flutterCapsuleSpaceOdds1}{flutterCapsuleSpaceOdds2}{flutterCapsuleSpaceOdds34}{flutterCapsuleSpaceOdds34}
042EF5D4 {flutterCapsuleShopOdds12}{flutterCapsuleShopOdds34}0000
042EF5D8 05{cannonCapsulePrice1}{cannonCapsulePrice2}{cannonCapsulePrice34}
042EF5DC {cannonCapsuleSpaceOdds1}{cannonCapsuleSpaceOdds2}{cannonCapsuleSpaceOdds34}{cannonCapsuleSpaceOdds34}
042EF5E0 {cannonCapsuleSpaceOdds1}{cannonCapsuleSpaceOdds2}{cannonCapsuleSpaceOdds34}{cannonCapsuleSpaceOdds34}
042EF5E4 {cannonCapsuleShopOdds12}{cannonCapsuleShopOdds34}0000
042EF5E8 06{snackCapsulePrice1}{snackCapsulePrice2}{snackCapsulePrice34}
042EF5EC {snackCapsuleSpaceOdds1}{snackCapsuleSpaceOdds2}{snackCapsuleSpaceOdds34}{snackCapsuleSpaceOdds34}
042EF5F0 {snackCapsuleSpaceOdds1}{snackCapsuleSpaceOdds2}{snackCapsuleSpaceOdds34}{snackCapsuleSpaceOdds34}
042EF5F4 {snackCapsuleShopOdds12}{snackCapsuleShopOdds34}0000
042EF5F8 07{lakituCapsulePrice1}{lakituCapsulePrice2}{lakituCapsulePrice34}
042EF5FC {lakituCapsuleSpaceOdds1}{lakituCapsuleSpaceOdds2}{lakituCapsuleSpaceOdds34}{lakituCapsuleSpaceOdds34}
042EF600 {lakituCapsuleSpaceOdds1}{lakituCapsuleSpaceOdds2}{lakituCapsuleSpaceOdds34}{lakituCapsuleSpaceOdds34}
042EF604 {lakituCapsuleShopOdds12}{lakituCapsuleShopOdds34}0000
042EF608 0A{hammerBroCapsulePrice1}{hammerBroCapsulePrice2}{hammerBroCapsulePrice34}
042EF60C {hammerBroCapsuleSpaceOdds1}{hammerBroCapsuleSpaceOdds2}{hammerBroCapsuleSpaceOdds34}{hammerBroCapsuleSpaceOdds34}
042EF610 {hammerBroCapsuleSpaceOdds1}{hammerBroCapsuleSpaceOdds2}{hammerBroCapsuleSpaceOdds34}{hammerBroCapsuleSpaceOdds34}
042EF614 {hammerBroCapsuleShopOdds12}{hammerBroCapsuleShopOdds34}0000
042EF618 0B{piranhaPlantCapsulePrice1}{piranhaPlantCapsulePrice2}{piranhaPlantCapsulePrice34}
042EF61C {piranhaPlantCapsuleSpaceOdds1}{piranhaPlantCapsuleSpaceOdds2}{piranhaPlantCapsuleSpaceOdds34}{piranhaPlantCapsuleSpaceOdds34}
042EF620 {piranhaPlantCapsuleSpaceOdds1}{piranhaPlantCapsuleSpaceOdds2}{piranhaPlantCapsuleSpaceOdds34}{piranhaPlantCapsuleSpaceOdds34}
042EF624 {piranhaPlantCapsuleShopOdds12}{piranhaPlantCapsuleShopOdds34}0000
042EF628 0C{spearGuyCapsulePrice1}{spearGuyCapsulePrice2}{spearGuyCapsulePrice34}
042EF62C {spearGuyCapsuleSpaceOdds1}{spearGuyCapsuleSpaceOdds2}{spearGuyCapsuleSpaceOdds34}{spearGuyCapsuleSpaceOdds34}
042EF630 {spearGuyCapsuleSpaceOdds1}{spearGuyCapsuleSpaceOdds2}{spearGuyCapsuleSpaceOdds34}{spearGuyCapsuleSpaceOdds34}
042EF634 {spearGuyCapsuleShopOdds12}{spearGuyCapsuleShopOdds34}0000
042EF638 0D{kamekCapsulePrice1}{kamekCapsulePrice2}{kamekCapsulePrice34}
042EF63C {kamekCapsuleSpaceOdds1}{kamekCapsuleSpaceOdds2}{kamekCapsuleSpaceOdds34}{kamekCapsuleSpaceOdds34}
042EF640 {kamekCapsuleSpaceOdds1}{kamekCapsuleSpaceOdds2}{kamekCapsuleSpaceOdds34}{kamekCapsuleSpaceOdds34}
042EF644 {kamekCapsuleShopOdds12}{kamekCapsuleShopOdds34}0000
042EF648 0E{toadyCapsulePrice1}{toadyCapsulePrice2}{toadyCapsulePrice34}
042EF64C {toadyCapsuleSpaceOdds1}{toadyCapsuleSpaceOdds2}{toadyCapsuleSpaceOdds34}{toadyCapsuleSpaceOdds34}
042EF650 {toadyCapsuleSpaceOdds1}{toadyCapsuleSpaceOdds2}{toadyCapsuleSpaceOdds34}{toadyCapsuleSpaceOdds34}
042EF654 {toadyCapsuleShopOdds12}{toadyCapsuleShopOdds34}0000
042EF658 0F{mrBlizzardCapsulePrice1}{mrBlizzardCapsulePrice2}{mrBlizzardCapsulePrice34}
042EF65C {mrBlizzardCapsuleSpaceOdds1}{mrBlizzardCapsuleSpaceOdds2}{mrBlizzardCapsuleSpaceOdds34}{mrBlizzardCapsuleSpaceOdds34}
042EF660 {mrBlizzardCapsuleSpaceOdds1}{mrBlizzardCapsuleSpaceOdds2}{mrBlizzardCapsuleSpaceOdds34}{mrBlizzardCapsuleSpaceOdds34}
042EF664 {mrBlizzardCapsuleShopOdds12}{mrBlizzardCapsuleShopOdds34}0000
042EF668 10{banditCapsulePrice1}{banditCapsulePrice2}{banditCapsulePrice34}
042EF66C {banditCapsuleSpaceOdds1}{banditCapsuleSpaceOdds2}{banditCapsuleSpaceOdds34}{banditCapsuleSpaceOdds34}
042EF670 {banditCapsuleSpaceOdds1}{banditCapsuleSpaceOdds2}{banditCapsuleSpaceOdds34}{banditCapsuleSpaceOdds34}
042EF674 {banditCapsuleShopOdds12}{banditCapsuleShopOdds34}0000
042EF678 11{pinkBooCapsulePrice1}{pinkBooCapsulePrice2}{pinkBooCapsulePrice34}
042EF67C {pinkBooCapsuleSpaceOdds1}{pinkBooCapsuleSpaceOdds2}{pinkBooCapsuleSpaceOdds34}{pinkBooCapsuleSpaceOdds34}
042EF680 {pinkBooCapsuleSpaceOdds1}{pinkBooCapsuleSpaceOdds2}{pinkBooCapsuleSpaceOdds34}{pinkBooCapsuleSpaceOdds34}
042EF684 {pinkBooCapsuleShopOdds12}{pinkBooCapsuleShopOdds34}0000
042EF688 14{spinyCapsulePrice1}{spinyCapsulePrice2}{spinyCapsulePrice34}
042EF68C {spinyCapsuleSpaceOdds1}{spinyCapsuleSpaceOdds2}{spinyCapsuleSpaceOdds34}{spinyCapsuleSpaceOdds34}
042EF690 {spinyCapsuleSpaceOdds1}{spinyCapsuleSpaceOdds2}{spinyCapsuleSpaceOdds34}{spinyCapsuleSpaceOdds34}
042EF694 {spinyCapsuleShopOdds12}{spinyCapsuleShopOdds34}0000
042EF698 15{zapCapsulePrice1}{zapCapsulePrice2}{zapCapsulePrice34}
042EF69C {zapCapsuleSpaceOdds1}{zapCapsuleSpaceOdds2}{zapCapsuleSpaceOdds34}{zapCapsuleSpaceOdds34}
042EF6A0 {zapCapsuleSpaceOdds1}{zapCapsuleSpaceOdds2}{zapCapsuleSpaceOdds34}{zapCapsuleSpaceOdds34}
042EF6A4 {zapCapsuleShopOdds12}{zapCapsuleShopOdds34}0000
042EF6A8 16{tweesterCapsulePrice1}{tweesterCapsulePrice2}{tweesterCapsulePrice34}
042EF6AC {tweesterCapsuleSpaceOdds1}{tweesterCapsuleSpaceOdds2}{tweesterCapsuleSpaceOdds34}{tweesterCapsuleSpaceOdds34}
042EF6B0 {tweesterCapsuleSpaceOdds1}{tweesterCapsuleSpaceOdds2}{tweesterCapsuleSpaceOdds34}{tweesterCapsuleSpaceOdds34}
042EF6B4 {tweesterCapsuleShopOdds12}{tweesterCapsuleShopOdds34}0000
042EF6B8 17{thwompCapsulePrice1}{thwompCapsulePrice2}{thwompCapsulePrice34}
042EF6BC {thwompCapsuleSpaceOdds1}{thwompCapsuleSpaceOdds2}{thwompCapsuleSpaceOdds34}{thwompCapsuleSpaceOdds34}
042EF6C0 {thwompCapsuleSpaceOdds1}{thwompCapsuleSpaceOdds2}{thwompCapsuleSpaceOdds34}{thwompCapsuleSpaceOdds34}
042EF6C4 {thwompCapsuleShopOdds12}{thwompCapsuleShopOdds34}0000
042EF6C8 18{warpCapsulePrice1}{warpCapsulePrice2}{warpCapsulePrice34}
042EF6CC {warpCapsuleSpaceOdds1}{warpCapsuleSpaceOdds2}{warpCapsuleSpaceOdds34}{warpCapsuleSpaceOdds34}
042EF6D0 {warpCapsuleSpaceOdds1}{warpCapsuleSpaceOdds2}{warpCapsuleSpaceOdds34}{warpCapsuleSpaceOdds34}
042EF6D4 {warpCapsuleShopOdds12}{warpCapsuleShopOdds34}0000
042EF6D8 19{bombCapsulePrice1}{bombCapsulePrice2}{bombCapsulePrice34}
042EF6DC {bombCapsuleSpaceOdds1}{bombCapsuleSpaceOdds2}{bombCapsuleSpaceOdds34}{bombCapsuleSpaceOdds34}
042EF6E0 {bombCapsuleSpaceOdds1}{bombCapsuleSpaceOdds2}{bombCapsuleSpaceOdds34}{bombCapsuleSpaceOdds34}
042EF6E4 {bombCapsuleShopOdds12}{bombCapsuleShopOdds34}0000
042EF6E8 1E{fireballCapsulePrice1}{fireballCapsulePrice2}{fireballCapsulePrice34}
042EF6EC {fireballCapsuleSpaceOdds1}{fireballCapsuleSpaceOdds2}{fireballCapsuleSpaceOdds34}{fireballCapsuleSpaceOdds34}
042EF6F0 {fireballCapsuleSpaceOdds1}{fireballCapsuleSpaceOdds2}{fireballCapsuleSpaceOdds34}{fireballCapsuleSpaceOdds34}
042EF6F4 {fireballCapsuleShopOdds12}{fireballCapsuleShopOdds34}0000
042EF6F8 1F{flowerCapsulePrice1}{flowerCapsulePrice2}{flowerCapsulePrice34}
042EF6FC {flowerCapsuleSpaceOdds1}{flowerCapsuleSpaceOdds2}{flowerCapsuleSpaceOdds34}{flowerCapsuleSpaceOdds34}
042EF700 {flowerCapsuleSpaceOdds1}{flowerCapsuleSpaceOdds2}{flowerCapsuleSpaceOdds34}{flowerCapsuleSpaceOdds34}
042EF704 {flowerCapsuleShopOdds12}{flowerCapsuleShopOdds34}0000
042EF708 20{eggCapsulePrice1}{eggCapsulePrice2}{eggCapsulePrice34}
042EF70C {eggCapsuleSpaceOdds1}{eggCapsuleSpaceOdds2}{eggCapsuleSpaceOdds34}{eggCapsuleSpaceOdds34}
042EF710 {eggCapsuleSpaceOdds1}{eggCapsuleSpaceOdds2}{eggCapsuleSpaceOdds34}{eggCapsuleSpaceOdds34}
042EF714 {eggCapsuleShopOdds12}{eggCapsuleShopOdds34}0000
042EF718 21{vacuumCapsulePrice1}{vacuumCapsulePrice2}{vacuumCapsulePrice34}
042EF71C {vacuumCapsuleSpaceOdds1}{vacuumCapsuleSpaceOdds2}{vacuumCapsuleSpaceOdds34}{vacuumCapsuleSpaceOdds34}
042EF720 {vacuumCapsuleSpaceOdds1}{vacuumCapsuleSpaceOdds2}{vacuumCapsuleSpaceOdds34}{vacuumCapsuleSpaceOdds34}
042EF724 {vacuumCapsuleShopOdds12}{vacuumCapsuleShopOdds34}0000
042EF728 22{magicCapsulePrice1}{magicCapsulePrice2}{magicCapsulePrice34}
042EF72C {magicCapsuleSpaceOdds1}{magicCapsuleSpaceOdds2}{magicCapsuleSpaceOdds34}{magicCapsuleSpaceOdds34}
042EF730 {magicCapsuleSpaceOdds1}{magicCapsuleSpaceOdds2}{magicCapsuleSpaceOdds34}{magicCapsuleSpaceOdds34}
042EF734 {magicCapsuleShopOdds12}{magicCapsuleShopOdds34}0000
042EF738 23{tripleCapsulePrice1}{tripleCapsulePrice2}{tripleCapsulePrice34}
042EF73C {tripleCapsuleSpaceOdds1}{tripleCapsuleSpaceOdds2}{tripleCapsuleSpaceOdds34}{tripleCapsuleSpaceOdds34}
042EF740 {tripleCapsuleSpaceOdds1}{tripleCapsuleSpaceOdds2}{tripleCapsuleSpaceOdds34}{tripleCapsuleSpaceOdds34}
042EF744 {tripleCapsuleShopOdds12}{tripleCapsuleShopOdds34}0000
042EF748 28{koopaCapsulePrice1}{koopaCapsulePrice2}{koopaCapsulePrice34}
042EF74C {koopaCapsuleSpaceOdds1}{koopaCapsuleSpaceOdds2}{koopaCapsuleSpaceOdds34}{koopaCapsuleSpaceOdds34}
042EF750 {koopaCapsuleSpaceOdds1}{koopaCapsuleSpaceOdds2}{koopaCapsuleSpaceOdds34}{koopaCapsuleSpaceOdds34}
042EF754 {koopaCapsuleShopOdds12}{koopaCapsuleShopOdds34}0000
042EF758 08{duelCapsulePrice1}{duelCapsulePrice2}{duelCapsulePrice34}
042EF75C {duelCapsuleSpaceOdds1}{duelCapsuleSpaceOdds2}{duelCapsuleSpaceOdds34}{duelCapsuleSpaceOdds34}
042EF760 {duelCapsuleSpaceOdds1}{duelCapsuleSpaceOdds2}{duelCapsuleSpaceOdds34}{duelCapsuleSpaceOdds34}
042EF764 {duelCapsuleShopOdds12}{duelCapsuleShopOdds34}0000
042EF768 09{dkCapsulePrice1}{dkCapsulePrice2}{dkCapsulePrice34}
042EF76C {dkCapsuleSpaceOdds1}{dkCapsuleSpaceOdds2}{dkCapsuleSpaceOdds34}{dkCapsuleSpaceOdds34}
042EF770 {dkCapsuleSpaceOdds1}{dkCapsuleSpaceOdds2}{dkCapsuleSpaceOdds34}{dkCapsuleSpaceOdds34}
042EF774 {dkCapsuleShopOdds12}{dkCapsuleShopOdds34}0000
042EF778 32{poisonMushroomPrice1}{poisonMushroomPrice2}{poisonMushroomPrice34}
042EF78C {poisonMushroomSpaceOdds1}{poisonMushroomSpaceOdds2}{poisonMushroomSpaceOdds34}{poisonMushroomSpaceOdds34}
042EF790 {poisonMushroomSpaceOdds1}{poisonMushroomSpaceOdds2}{poisonMushroomSpaceOdds34}{poisonMushroomSpaceOdds34}
042EF794 {poisonMushroomShopOdds12}{poisonMushroomShopOdds34}0000
042EF798 33{orbBagCapsulePrice1}{orbBagCapsulePrice2}{orbBagCapsulePrice34}
042EF79C {orbBagCapsuleSpaceOdds1}{orbBagCapsuleSpaceOdds2}{orbBagCapsuleSpaceOdds34}{orbBagCapsuleSpaceOdds34}
042EF7A0 {orbBagCapsuleSpaceOdds1}{orbBagCapsuleSpaceOdds2}{orbBagCapsuleSpaceOdds34}{orbBagCapsuleSpaceOdds34}
042EF7A4 {orbBagCapsuleShopOdds12}{orbBagCapsuleShopOdds34}0000
042EF7A8 35{mysteryCapsulePrice1}{mysteryCapsulePrice2}{mysteryCapsulePrice34}
042EF7AC {mysteryCapsuleSpaceOdds1}{mysteryCapsuleSpaceOdds2}{mysteryCapsuleSpaceOdds34}{mysteryCapsuleSpaceOdds34}
042EF7B0 {mysteryCapsuleSpaceOdds1}{mysteryCapsuleSpaceOdds2}{mysteryCapsuleSpaceOdds34}{mysteryCapsuleSpaceOdds34}
042EF7B4 {mysteryCapsuleShopOdds12}{mysteryCapsuleShopOdds34}0000
042EF7B8 FF000000
042EF7BC 00000000
042EF7C0 00000000
042EF7C4 00000000
'''

def getInitialItemsSeven(one, two, three, four, five, oneItem, twoItem, threeItem, fourItem, fiveItem):
    return f'''
MP7 - Start with {oneItem}, {twoItem}, and {threeItem}
06003620 00000030
3D808000 618C363C
1C060005 7C005A14
7C8C00AE 98830006
48164338 {one}{two}{three}{four}
{five}{one}{two}{three} {four}{five}{one}{two}
{three}{four}{five}{one} {two}{three}{four}{five}
0416796C 4BE9BCB4
'''

def getSpaceReplaceSeven1(spaceHex1, spaceHex2, spaceName, spaceName2):
    return f'''
MP7 - Replace {spaceName} with {spaceName2} (Slot A)
C217942C 00000005
A01F0030 280000{spaceHex1}
40820018 A09F0032
2804FFFF 4082000C
380000{spaceHex2} B01F0030
60000000 00000000
'''

def getSpaceReplaceSeven2(spaceHex1, spaceHex2, spaceName, spaceName2):
    return f'''
MP7 - Replace {spaceName} with {spaceName2} (Slot B)
C2179430 00000005
280000{spaceHex1} 40820018
A09F0032 2804FFFF
4082000C 380000{spaceHex2}
B01F0030 5404083C
60000000 00000000
'''

def getWindmillMaxSeven(amount, amountDec):
    return f'''
MP7 - Windmillville: Invest Up To {amountDec}
204E4C7C 2C040064
C24E4C7C 00000001
2C04{amount} 00000000
E2000001 80008000
204E4CCC 2C040064
C24E4CCC 00000001
2C04{amount} 00000000
E2000001 80008000
'''

def getStarHandicap(p1, p2, p3, p4):
    return f'''
MP7 - Star Handicap
20290CC4 00000000
02290CD0 0000{p1}
02290DE0 0000{p2}
02290EF0 0000{p3}
02291000 0000{p4}
E2000001 80008000
'''

def getSpinxEvent(a, b):
    return f'''
MP7 - Pyramid Park: Spinx Event is Always {b}
282F2F3E 0000007C
28290CA8 0000004D
28291522 00000023
0052449F 000000{a}
E2000002 80008000
28290DB8 0000004D
28291522 00000123
0052449F 000000{a}
E2000002 80008000
28290EC8 0000004D
28291522 00000223
0052449F 000000{a}
E2000002 80008000
28290FD8 0000004D
28291522 00000323
0052449F 000000{a}
E2000003 80008000
'''

def getGliderEvent(a, b):
    return f'''
MP7 - Windmillvlle: Flower Glider Always Goes To
282F2F3E 0000007E
28290CA8 00000031
28291522 0000001A
026370B2 000000{a}
E2000002 80008000
28290DB8 00000031
28291522 0000011A
026370B2 000000{a}
E2000002 80008000
28290EC8 00000031
28291522 0000021A
026370B2 000000{a}
E2000002 80008000
28290FD8 00000031
28291522 0000031A
026370B2 000000{a}
E2000003 80008000
'''

def getGliderCostEvent(a, b, c):
    return f'''
MP7 - Windmillville: Flower Glider Costs {c}
282F2F3E 0000007E
284E73AE 0000000A
024E73AE 0000{a}
E2000001 80008000
284E7D12 0000FFF6
024E7D12 0000{b}
E2000002 80008000
'''

def getBlackChomp(a, b):
    return f'''
MP7 - Pyramid Park: Standard Chomp Costs {b}
282F2F3E 0000007C
28511722 0000000A
02511722 0000{a}
E2000002 80008000
'''

def getRedChomp(a, b):
    return f'''
MP7 - Pyramid Park: Red Chomp Costs {b}
282F2F3E 0000007C
28511726 0000000A
02511726 0000{a}
E2000002 80008000
'''

def initialCoinsMod7(hex, hexDec):
    return f'''
MP7 - Gain {hexDec} Coins at the Start of the Game
02196D12 0000{hex}
02151DEA 0000{hex}
'''

def getBattleGame7(p1, p2, p3, p4, p5, s1, s2, s3, s4, s5):
    return f'''
MP7 - Battle Minigames Bounties are {s1}, {s2}, {s3}, {s4}, and {s5}
04276F34 0000{p1}
04276F38 0000{p2}
04276F3C 0000{p3}
04276F40 0000{p4}
04276F44 0000{p5}
04276F48 0000{p5}
042215E0 60000000
'''

def getStarReplaceSeven1(amount, amountDec):
    return f'''
MP7 - Replace Minigame Star with {amountDec}
204E185C A8A70028
C24E185C 00000001
{amount} 00000000
E2000001 80008000
'''

def getStarReplaceSeven2(amount, amountDec):
    return f'''
MP7 - Replace Orb Star with {amountDec}
204E18D4 A8C3003C
C24E18D4 00000001
{amount} 00000000
E2000001 80008000
'''

def getStarReplaceSeven3(amount, amountDec):
    return f'''
MP7 - Replace Happening Star with {amountDec}
204E1A0C 8903001F
C24E1A0C 00000002
{amount} 7D064378
60000000 00000000
E2000001 80008000
'''

def getStarReplaceSeven4(amount, amountDec):
    return f'''
MP7 - Replace Shopping Star with {amountDec}
204E1898 A885003E
C24E1898 00000001
{amount} 00000000
E2000001 80008000
'''

def getStarReplaceSeven5(amount, amountDec):
    return f'''
MP7 - Replace Running Star with {amountDec}
204E1910 A8C40018
C24E1910 00000001
{amount} 00000000
E2000001 80008000
'''

def getStarReplaceSeven6(amount, amountDec):
    return f'''
MP7 - Replace Red Star with {amountDec}
204E198C 8904001D
C24E198C 00000002
{amount} 7D064378
60000000 00000000
E2000001 80008000
'''
