# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (tabitha@tabs.gay)
# Date: 5/12/2024
# License: MIT
# ============================================

from codes.marioParty7 import *
from functions import *

import csv
import math
import pyperclip

def itemsEvent_mp7(mushroomCapsuleShopOdds12 = "0", mushroomCapsuleShopOdds34 = "0", mushroomCapsuleSpaceOdds1 = "0", mushroomCapsuleSpaceOdds2 = "0", mushroomCapsuleSpaceOdds34 = "0", goldenMushroomCapsulePrice1 = "0", goldenMushroomCapsulePrice2 = "0", goldenMushroomCapsulePrice34 = "0", goldenMushroomCapsuleShopOdds12 = "0", goldenMushroomCapsuleShopOdds34 = "0", goldenMushroomCapsuleSpaceOdds1 = "0", goldenMushroomCapsuleSpaceOdds2 = "0", goldenMushroomCapsuleSpaceOdds34 = "0", slowMushroomCapsulePrice1 = "0", slowMushroomCapsulePrice2 = "0", slowMushroomCapsulePrice34 = "0", slowMushroomCapsuleShopOdds12 = "0", slowMushroomCapsuleShopOdds34 = "0", slowMushroomCapsuleSpaceOdds1 = "0", slowMushroomCapsuleSpaceOdds2 = "0", slowMushroomCapsuleSpaceOdds34 = "0", metalMushroomCapsulePrice1 = "0", metalMushroomCapsulePrice2 = "0", metalMushroomCapsulePrice34 = "0", metalMushroomCapsuleShopOdds12 = "0", metalMushroomCapsuleShopOdds34 = "0", metalMushroomCapsuleSpaceOdds1 = "0", metalMushroomCapsuleSpaceOdds2 = "0", metalMushroomCapsuleSpaceOdds34 = "0", flutterCapsulePrice1 = "0", flutterCapsulePrice2 = "0", flutterCapsulePrice34 = "0", flutterCapsuleShopOdds12 = "0", flutterCapsuleShopOdds34 = "0", flutterCapsuleSpaceOdds1 = "0", flutterCapsuleSpaceOdds2 = "0", flutterCapsuleSpaceOdds34 = "0", cannonCapsulePrice1 = "0", cannonCapsulePrice2 = "0", cannonCapsulePrice34 = "0", cannonCapsuleShopOdds12 = "0", cannonCapsuleShopOdds34 = "0", cannonCapsuleSpaceOdds1 = "0", cannonCapsuleSpaceOdds2 = "0", cannonCapsuleSpaceOdds34 = "0", snackCapsulePrice1 = "0", snackCapsulePrice2 = "0", snackCapsulePrice34 = "0", snackCapsuleShopOdds12 = "0", snackCapsuleShopOdds34 = "0", snackCapsuleSpaceOdds1 = "0", snackCapsuleSpaceOdds2 = "0", snackCapsuleSpaceOdds34 = "0", lakituCapsulePrice1 = "0", lakituCapsulePrice2 = "0", lakituCapsulePrice34 = "0", lakituCapsuleShopOdds12 = "0", lakituCapsuleShopOdds34 = "0", lakituCapsuleSpaceOdds1 = "0", lakituCapsuleSpaceOdds2 = "0", lakituCapsuleSpaceOdds34 = "0", hammerBroCapsulePrice1 = "0", hammerBroCapsulePrice2 = "0", hammerBroCapsulePrice34 = "0", hammerBroCapsuleShopOdds12 = "0", hammerBroCapsuleShopOdds34 = "0", hammerBroCapsuleSpaceOdds1 = "0", hammerBroCapsuleSpaceOdds2 = "0", hammerBroCapsuleSpaceOdds34 = "0", piranhaPlantCapsulePrice1 = "0", piranhaPlantCapsulePrice2 = "0", piranhaPlantCapsulePrice34 = "0", piranhaPlantCapsuleShopOdds12 = "0", piranhaPlantCapsuleShopOdds34 = "0", piranhaPlantCapsuleSpaceOdds1 = "0", piranhaPlantCapsuleSpaceOdds2 = "0", piranhaPlantCapsuleSpaceOdds34 = "0", spearGuyCapsulePrice1 = "0", spearGuyCapsulePrice2 = "0", spearGuyCapsulePrice34 = "0", spearGuyCapsuleShopOdds12 = "0", spearGuyCapsuleShopOdds34 = "0", spearGuyCapsuleSpaceOdds1 = "0", spearGuyCapsuleSpaceOdds2 = "0", spearGuyCapsuleSpaceOdds34 = "0", kamekCapsulePrice1 = "0", kamekCapsulePrice2 = "0", kamekCapsulePrice34 = "0", kamekCapsuleShopOdds12 = "0", kamekCapsuleShopOdds34 = "0", kamekCapsuleSpaceOdds1 = "0", kamekCapsuleSpaceOdds2 = "0", kamekCapsuleSpaceOdds34 = "0", toadyCapsulePrice1 = "0", toadyCapsulePrice2 = "0", toadyCapsulePrice34 = "0", toadyCapsuleShopOdds12 = "0", toadyCapsuleShopOdds34 = "0", toadyCapsuleSpaceOdds1 = "0", toadyCapsuleSpaceOdds2 = "0", toadyCapsuleSpaceOdds34 = "0", mrBlizzardCapsulePrice1 = "0", mrBlizzardCapsulePrice2 = "0", mrBlizzardCapsulePrice34 = "0", mrBlizzardCapsuleShopOdds12 = "0", mrBlizzardCapsuleShopOdds34 = "0", mrBlizzardCapsuleSpaceOdds1 = "0", mrBlizzardCapsuleSpaceOdds2 = "0", mrBlizzardCapsuleSpaceOdds34 = "0", banditCapsulePrice1 = "0", banditCapsulePrice2 = "0", banditCapsulePrice34 = "0", banditCapsuleShopOdds12 = "0", banditCapsuleShopOdds34 = "0", banditCapsuleSpaceOdds1 = "0", banditCapsuleSpaceOdds2 = "0", banditCapsuleSpaceOdds34 = "0", pinkBooCapsulePrice1 = "0", pinkBooCapsulePrice2 = "0", pinkBooCapsulePrice34 = "0", pinkBooCapsuleShopOdds12 = "0", pinkBooCapsuleShopOdds34 = "0", pinkBooCapsuleSpaceOdds1 = "0", pinkBooCapsuleSpaceOdds2 = "0", pinkBooCapsuleSpaceOdds34 = "0", spinyCapsulePrice1 = "0", spinyCapsulePrice2 = "0", spinyCapsulePrice34 = "0", spinyCapsuleShopOdds12 = "0", spinyCapsuleShopOdds34 = "0", spinyCapsuleSpaceOdds1 = "0", spinyCapsuleSpaceOdds2 = "0", spinyCapsuleSpaceOdds34 = "0", zapCapsulePrice1 = "0", zapCapsulePrice2 = "0", zapCapsulePrice34 = "0", zapCapsuleShopOdds12 = "0", zapCapsuleShopOdds34 = "0", zapCapsuleSpaceOdds1 = "0", zapCapsuleSpaceOdds2 = "0", zapCapsuleSpaceOdds34 = "0", tweesterCapsulePrice1 = "0", tweesterCapsulePrice2 = "0", tweesterCapsulePrice34 = "0", tweesterCapsuleShopOdds12 = "0", tweesterCapsuleShopOdds34 = "0", tweesterCapsuleSpaceOdds1 = "0", tweesterCapsuleSpaceOdds2 = "0", tweesterCapsuleSpaceOdds34 = "0", thwompCapsulePrice1 = "0", thwompCapsulePrice2 = "0", thwompCapsulePrice34 = "0", thwompCapsuleShopOdds12 = "0", thwompCapsuleShopOdds34 = "0", thwompCapsuleSpaceOdds1 = "0", thwompCapsuleSpaceOdds2 = "0", thwompCapsuleSpaceOdds34 = "0", warpCapsulePrice1 = "0", warpCapsulePrice2 = "0", warpCapsulePrice34 = "0", warpCapsuleShopOdds12 = "0", warpCapsuleShopOdds34 = "0", warpCapsuleSpaceOdds1 = "0", warpCapsuleSpaceOdds2 = "0", warpCapsuleSpaceOdds34 = "0", bombCapsulePrice1 = "0", bombCapsulePrice2 = "0", bombCapsulePrice34 = "0", bombCapsuleShopOdds12 = "0", bombCapsuleShopOdds34 = "0", bombCapsuleSpaceOdds1 = "0", bombCapsuleSpaceOdds2 = "0", bombCapsuleSpaceOdds34 = "0", fireballCapsulePrice1 = "0", fireballCapsulePrice2 = "0", fireballCapsulePrice34 = "0", fireballCapsuleShopOdds12 = "0", fireballCapsuleShopOdds34 = "0", fireballCapsuleSpaceOdds1 = "0", fireballCapsuleSpaceOdds2 = "0", fireballCapsuleSpaceOdds34 = "0", flowerCapsulePrice1 = "0", flowerCapsulePrice2 = "0", flowerCapsulePrice34 = "0", flowerCapsuleShopOdds12 = "0", flowerCapsuleShopOdds34 = "0", flowerCapsuleSpaceOdds1 = "0", flowerCapsuleSpaceOdds2 = "0", flowerCapsuleSpaceOdds34 = "0", eggCapsulePrice1 = "0", eggCapsulePrice2 = "0", eggCapsulePrice34 = "0", eggCapsuleShopOdds12 = "0", eggCapsuleShopOdds34 = "0", eggCapsuleSpaceOdds1 = "0", eggCapsuleSpaceOdds2 = "0", eggCapsuleSpaceOdds34 = "0", vacuumCapsulePrice1 = "0", vacuumCapsulePrice2 = "0", vacuumCapsulePrice34 = "0", vacuumCapsuleShopOdds12 = "0", vacuumCapsuleShopOdds34 = "0", vacuumCapsuleSpaceOdds1 = "0", vacuumCapsuleSpaceOdds2 = "0", vacuumCapsuleSpaceOdds34 = "0", magicCapsulePrice1 = "0", magicCapsulePrice2 = "0", magicCapsulePrice34 = "0", magicCapsuleShopOdds12 = "0", magicCapsuleShopOdds34 = "0", magicCapsuleSpaceOdds1 = "0", magicCapsuleSpaceOdds2 = "0", magicCapsuleSpaceOdds34 = "0", tripleCapsulePrice1 = "0", tripleCapsulePrice2 = "0", tripleCapsulePrice34 = "0", tripleCapsuleShopOdds12 = "0", tripleCapsuleShopOdds34 = "0", tripleCapsuleSpaceOdds1 = "0", tripleCapsuleSpaceOdds2 = "0", tripleCapsuleSpaceOdds34 = "0", koopaCapsulePrice1 = "0", koopaCapsulePrice2 = "0", koopaCapsulePrice34 = "0", koopaCapsuleShopOdds12 = "0", koopaCapsuleShopOdds34 = "0", koopaCapsuleSpaceOdds1 = "0", koopaCapsuleSpaceOdds2 = "0", koopaCapsuleSpaceOdds34 = "0", poisonMushroomPrice1 = "0", poisonMushroomPrice2 = "0", poisonMushroomPrice34 = "0", poisonMushroomShopOdds12 = "0", poisonMushroomShopOdds34 = "0", poisonMushroomSpaceOdds1 = "0", poisonMushroomSpaceOdds2 = "0", poisonMushroomSpaceOdds34 = "0", orbBagCapsulePrice1 = "0", orbBagCapsulePrice2 = "0", orbBagCapsulePrice34 = "0", orbBagCapsuleShopOdds12 = "0", orbBagCapsuleShopOdds34 = "0", orbBagCapsuleSpaceOdds1 = "0", orbBagCapsuleSpaceOdds2 = "0", orbBagCapsuleSpaceOdds34 = "0", mysteryCapsulePrice1 = "0", mysteryCapsulePrice2 = "0", mysteryCapsulePrice34 = "0", mysteryCapsuleShopOdds12 = "0", mysteryCapsuleShopOdds34 = "0", mysteryCapsuleSpaceOdds1 = "0", mysteryCapsuleSpaceOdds2 = "0", mysteryCapsuleSpaceOdds34 = "0", dkCapsulePrice1 = "0", dkCapsulePrice2 = "0", dkCapsulePrice34 = "0", dkCapsuleShopOdds12 = "0", dkCapsuleShopOdds34 = "0", dkCapsuleSpaceOdds1 = "0", dkCapsuleSpaceOdds2 = "0", dkCapsuleSpaceOdds34 = "0", duelCapsulePrice1 = "0", duelCapsulePrice2 = "0", duelCapsulePrice34 = "0", duelCapsuleShopOdds12 = "0", duelCapsuleShopOdds34 = "0", duelCapsuleSpaceOdds1 = "0", duelCapsuleSpaceOdds2 = "0", duelCapsuleSpaceOdds34 = "0"):
    def get_capsule_value(capsule):
        try:
            return capsule.get()
        except:
            return 0

    mushroomCapsulePrice1 = "05"
    mushroomCapsulePrice2 = "05"
    mushroomCapsulePrice34 = "05"
    mushroomCapsuleShopOdds12 = get_capsule_value(mushroomCapsuleShopOdds12)
    mushroomCapsuleShopOdds34 = get_capsule_value(mushroomCapsuleShopOdds34)
    mushroomCapsuleSpaceOdds1 = get_capsule_value(mushroomCapsuleSpaceOdds1)
    mushroomCapsuleSpaceOdds2 = get_capsule_value(mushroomCapsuleSpaceOdds2)
    mushroomCapsuleSpaceOdds34 = get_capsule_value(mushroomCapsuleSpaceOdds34)

    goldenMushroomCapsulePrice1 = get_capsule_value(goldenMushroomCapsulePrice1)
    goldenMushroomCapsulePrice2 = get_capsule_value(goldenMushroomCapsulePrice2)
    goldenMushroomCapsulePrice34 = get_capsule_value(goldenMushroomCapsulePrice34)
    goldenMushroomCapsuleShopOdds12 = get_capsule_value(goldenMushroomCapsuleShopOdds12)
    goldenMushroomCapsuleShopOdds34 = get_capsule_value(goldenMushroomCapsuleShopOdds34)
    goldenMushroomCapsuleSpaceOdds1 = get_capsule_value(goldenMushroomCapsuleSpaceOdds1)
    goldenMushroomCapsuleSpaceOdds2 = get_capsule_value(goldenMushroomCapsuleSpaceOdds2)
    goldenMushroomCapsuleSpaceOdds34 = get_capsule_value(goldenMushroomCapsuleSpaceOdds34)


    slowMushroomCapsulePrice1 = get_capsule_value(slowMushroomCapsulePrice1)
    slowMushroomCapsulePrice2 = get_capsule_value(slowMushroomCapsulePrice2)
    slowMushroomCapsulePrice34 = get_capsule_value(slowMushroomCapsulePrice34)
    slowMushroomCapsuleShopOdds12 = get_capsule_value(slowMushroomCapsuleShopOdds12)
    slowMushroomCapsuleShopOdds34 = get_capsule_value(slowMushroomCapsuleShopOdds34)
    slowMushroomCapsuleSpaceOdds1 = get_capsule_value(slowMushroomCapsuleSpaceOdds1)
    slowMushroomCapsuleSpaceOdds2 = get_capsule_value(slowMushroomCapsuleSpaceOdds2)
    slowMushroomCapsuleSpaceOdds34 = get_capsule_value(slowMushroomCapsuleSpaceOdds34)

    metalMushroomCapsulePrice1 = get_capsule_value(metalMushroomCapsulePrice1)
    metalMushroomCapsulePrice2 = get_capsule_value(metalMushroomCapsulePrice2)
    metalMushroomCapsulePrice34 = get_capsule_value(metalMushroomCapsulePrice34)
    metalMushroomCapsuleShopOdds12 = get_capsule_value(metalMushroomCapsuleShopOdds12)
    metalMushroomCapsuleShopOdds34 = get_capsule_value(metalMushroomCapsuleShopOdds34)
    metalMushroomCapsuleSpaceOdds1 = get_capsule_value(metalMushroomCapsuleSpaceOdds1)
    metalMushroomCapsuleSpaceOdds2 = get_capsule_value(metalMushroomCapsuleSpaceOdds2)
    metalMushroomCapsuleSpaceOdds34 = get_capsule_value(metalMushroomCapsuleSpaceOdds34)

    flutterCapsulePrice1 = get_capsule_value(flutterCapsulePrice1)
    flutterCapsulePrice2 = get_capsule_value(flutterCapsulePrice2)
    flutterCapsulePrice34 = get_capsule_value(flutterCapsulePrice34)
    flutterCapsuleShopOdds12 = get_capsule_value(flutterCapsuleShopOdds12)
    flutterCapsuleShopOdds34 = get_capsule_value(flutterCapsuleShopOdds34)
    flutterCapsuleSpaceOdds1 = get_capsule_value(flutterCapsuleSpaceOdds1)
    flutterCapsuleSpaceOdds2 = get_capsule_value(flutterCapsuleSpaceOdds2)
    flutterCapsuleSpaceOdds34 = get_capsule_value(flutterCapsuleSpaceOdds34)

    cannonCapsulePrice1 = get_capsule_value(cannonCapsulePrice1)
    cannonCapsulePrice2 = get_capsule_value(cannonCapsulePrice2)
    cannonCapsulePrice34 = get_capsule_value(cannonCapsulePrice34)
    cannonCapsuleShopOdds12 = get_capsule_value(cannonCapsuleShopOdds12)
    cannonCapsuleShopOdds34 = get_capsule_value(cannonCapsuleShopOdds34)
    cannonCapsuleSpaceOdds1 = get_capsule_value(cannonCapsuleSpaceOdds1)
    cannonCapsuleSpaceOdds2 = get_capsule_value(cannonCapsuleSpaceOdds2)
    cannonCapsuleSpaceOdds34 = get_capsule_value(cannonCapsuleSpaceOdds34)

    snackCapsulePrice1 = get_capsule_value(snackCapsulePrice1)
    snackCapsulePrice2 = get_capsule_value(snackCapsulePrice2)
    snackCapsulePrice34 = get_capsule_value(snackCapsulePrice34)
    snackCapsuleShopOdds12 = get_capsule_value(snackCapsuleShopOdds12)
    snackCapsuleShopOdds34 = get_capsule_value(snackCapsuleShopOdds34)
    snackCapsuleSpaceOdds1 = get_capsule_value(snackCapsuleSpaceOdds1)
    snackCapsuleSpaceOdds2 = get_capsule_value(snackCapsuleSpaceOdds2)
    snackCapsuleSpaceOdds34 = get_capsule_value(snackCapsuleSpaceOdds34)

    lakituCapsulePrice1 = get_capsule_value(lakituCapsulePrice1)
    lakituCapsulePrice2 = get_capsule_value(lakituCapsulePrice2)
    lakituCapsulePrice34 = get_capsule_value(lakituCapsulePrice34)
    lakituCapsuleShopOdds12 = get_capsule_value(lakituCapsuleShopOdds12)
    lakituCapsuleShopOdds34 = get_capsule_value(lakituCapsuleShopOdds34)
    lakituCapsuleSpaceOdds1 = get_capsule_value(lakituCapsuleSpaceOdds1)
    lakituCapsuleSpaceOdds2 = get_capsule_value(lakituCapsuleSpaceOdds2)
    lakituCapsuleSpaceOdds34 = get_capsule_value(lakituCapsuleSpaceOdds34)

    hammerBroCapsulePrice1 = get_capsule_value(hammerBroCapsulePrice1)
    hammerBroCapsulePrice2 = get_capsule_value(hammerBroCapsulePrice2)
    hammerBroCapsulePrice34 = get_capsule_value(hammerBroCapsulePrice34)
    hammerBroCapsuleShopOdds12 = get_capsule_value(hammerBroCapsuleShopOdds12)
    hammerBroCapsuleShopOdds34 = get_capsule_value(hammerBroCapsuleShopOdds34)
    hammerBroCapsuleSpaceOdds1 = get_capsule_value(hammerBroCapsuleSpaceOdds1)
    hammerBroCapsuleSpaceOdds2 = get_capsule_value(hammerBroCapsuleSpaceOdds2)
    hammerBroCapsuleSpaceOdds34 = get_capsule_value(hammerBroCapsuleSpaceOdds34)

    piranhaPlantCapsulePrice1 = get_capsule_value(piranhaPlantCapsulePrice1)
    piranhaPlantCapsulePrice2 = get_capsule_value(piranhaPlantCapsulePrice2)
    piranhaPlantCapsulePrice34 = get_capsule_value(piranhaPlantCapsulePrice34)
    piranhaPlantCapsuleShopOdds12 = get_capsule_value(piranhaPlantCapsuleShopOdds12)
    piranhaPlantCapsuleShopOdds34 = get_capsule_value(piranhaPlantCapsuleShopOdds34)
    piranhaPlantCapsuleSpaceOdds1 = get_capsule_value(piranhaPlantCapsuleSpaceOdds1)
    piranhaPlantCapsuleSpaceOdds2 = get_capsule_value(piranhaPlantCapsuleSpaceOdds2)
    piranhaPlantCapsuleSpaceOdds34 = get_capsule_value(piranhaPlantCapsuleSpaceOdds34)

    spearGuyCapsulePrice1 = get_capsule_value(spearGuyCapsulePrice1)
    spearGuyCapsulePrice2 = get_capsule_value(spearGuyCapsulePrice2)
    spearGuyCapsulePrice34 = get_capsule_value(spearGuyCapsulePrice34)
    spearGuyCapsuleShopOdds12 = get_capsule_value(spearGuyCapsuleShopOdds12)
    spearGuyCapsuleShopOdds34 = get_capsule_value(spearGuyCapsuleShopOdds34)
    spearGuyCapsuleSpaceOdds1 = get_capsule_value(spearGuyCapsuleSpaceOdds1)
    spearGuyCapsuleSpaceOdds2 = get_capsule_value(spearGuyCapsuleSpaceOdds2)
    spearGuyCapsuleSpaceOdds34 = get_capsule_value(spearGuyCapsuleSpaceOdds34)

    kamekCapsulePrice1 = get_capsule_value(kamekCapsulePrice1)
    kamekCapsulePrice2 = get_capsule_value(kamekCapsulePrice2)
    kamekCapsulePrice34 = get_capsule_value(kamekCapsulePrice34)
    kamekCapsuleShopOdds12 = get_capsule_value(kamekCapsuleShopOdds12)
    kamekCapsuleShopOdds34 = get_capsule_value(kamekCapsuleShopOdds34)
    kamekCapsuleSpaceOdds1 = get_capsule_value(kamekCapsuleSpaceOdds1)
    kamekCapsuleSpaceOdds2 = get_capsule_value(kamekCapsuleSpaceOdds2)
    kamekCapsuleSpaceOdds34 = get_capsule_value(kamekCapsuleSpaceOdds34)

    toadyCapsulePrice1 = get_capsule_value(toadyCapsulePrice1)
    toadyCapsulePrice2 = get_capsule_value(toadyCapsulePrice2)
    toadyCapsulePrice34 = get_capsule_value(toadyCapsulePrice34)
    toadyCapsuleShopOdds12 = get_capsule_value(toadyCapsuleShopOdds12)
    toadyCapsuleShopOdds34 = get_capsule_value(toadyCapsuleShopOdds34)
    toadyCapsuleSpaceOdds1 = get_capsule_value(toadyCapsuleSpaceOdds1)
    toadyCapsuleSpaceOdds2 = get_capsule_value(toadyCapsuleSpaceOdds2)
    toadyCapsuleSpaceOdds34 = get_capsule_value(toadyCapsuleSpaceOdds34)

    mrBlizzardCapsulePrice1 = get_capsule_value(mrBlizzardCapsulePrice1)
    mrBlizzardCapsulePrice2 = get_capsule_value(mrBlizzardCapsulePrice2)
    mrBlizzardCapsulePrice34 = get_capsule_value(mrBlizzardCapsulePrice34)
    mrBlizzardCapsuleShopOdds12 = get_capsule_value(mrBlizzardCapsuleShopOdds12)
    mrBlizzardCapsuleShopOdds34 = get_capsule_value(mrBlizzardCapsuleShopOdds34)
    mrBlizzardCapsuleSpaceOdds1 = get_capsule_value(mrBlizzardCapsuleSpaceOdds1)
    mrBlizzardCapsuleSpaceOdds2 = get_capsule_value(mrBlizzardCapsuleSpaceOdds2)
    mrBlizzardCapsuleSpaceOdds34 = get_capsule_value(mrBlizzardCapsuleSpaceOdds34)

    banditCapsulePrice1 = get_capsule_value(banditCapsulePrice1)
    banditCapsulePrice2 = get_capsule_value(banditCapsulePrice2)
    banditCapsulePrice34 = get_capsule_value(banditCapsulePrice34)
    banditCapsuleShopOdds12 = get_capsule_value(banditCapsuleShopOdds12)
    banditCapsuleShopOdds34 = get_capsule_value(banditCapsuleShopOdds34)
    banditCapsuleSpaceOdds1 = get_capsule_value(banditCapsuleSpaceOdds1)
    banditCapsuleSpaceOdds2 = get_capsule_value(banditCapsuleSpaceOdds2)
    banditCapsuleSpaceOdds34 = get_capsule_value(banditCapsuleSpaceOdds34)

    pinkBooCapsulePrice1 = get_capsule_value(pinkBooCapsulePrice1)
    pinkBooCapsulePrice2 = get_capsule_value(pinkBooCapsulePrice2)
    pinkBooCapsulePrice34 = get_capsule_value(pinkBooCapsulePrice34)
    pinkBooCapsuleShopOdds12 = get_capsule_value(pinkBooCapsuleShopOdds12)
    pinkBooCapsuleShopOdds34 = get_capsule_value(pinkBooCapsuleShopOdds34)
    pinkBooCapsuleSpaceOdds1 = get_capsule_value(pinkBooCapsuleSpaceOdds1)
    pinkBooCapsuleSpaceOdds2 = get_capsule_value(pinkBooCapsuleSpaceOdds2)
    pinkBooCapsuleSpaceOdds34 = get_capsule_value(pinkBooCapsuleSpaceOdds34)

    spinyCapsulePrice1 = get_capsule_value(spinyCapsulePrice1)
    spinyCapsulePrice2 = get_capsule_value(spinyCapsulePrice2)
    spinyCapsulePrice34 = get_capsule_value(spinyCapsulePrice34)
    spinyCapsuleShopOdds12 = get_capsule_value(spinyCapsuleShopOdds12)
    spinyCapsuleShopOdds34 = get_capsule_value(spinyCapsuleShopOdds34)
    spinyCapsuleSpaceOdds1 = get_capsule_value(spinyCapsuleSpaceOdds1)
    spinyCapsuleSpaceOdds2 = get_capsule_value(spinyCapsuleSpaceOdds2)
    spinyCapsuleSpaceOdds34 = get_capsule_value(spinyCapsuleSpaceOdds34)

    zapCapsulePrice1 = get_capsule_value(zapCapsulePrice1)
    zapCapsulePrice2 = get_capsule_value(zapCapsulePrice2)
    zapCapsulePrice34 = get_capsule_value(zapCapsulePrice34)
    zapCapsuleShopOdds12 = get_capsule_value(zapCapsuleShopOdds12)
    zapCapsuleShopOdds34 = get_capsule_value(zapCapsuleShopOdds34)
    zapCapsuleSpaceOdds1 = get_capsule_value(zapCapsuleSpaceOdds1)
    zapCapsuleSpaceOdds2 = get_capsule_value(zapCapsuleSpaceOdds2)
    zapCapsuleSpaceOdds34 = get_capsule_value(zapCapsuleSpaceOdds34)

    tweesterCapsulePrice1 = get_capsule_value(tweesterCapsulePrice1)
    tweesterCapsulePrice2 = get_capsule_value(tweesterCapsulePrice2)
    tweesterCapsulePrice34 = get_capsule_value(tweesterCapsulePrice34)
    tweesterCapsuleShopOdds12 = get_capsule_value(tweesterCapsuleShopOdds12)
    tweesterCapsuleShopOdds34 = get_capsule_value(tweesterCapsuleShopOdds34)
    tweesterCapsuleSpaceOdds1 = get_capsule_value(tweesterCapsuleSpaceOdds1)
    tweesterCapsuleSpaceOdds2 = get_capsule_value(tweesterCapsuleSpaceOdds2)
    tweesterCapsuleSpaceOdds34 = get_capsule_value(tweesterCapsuleSpaceOdds34)

    thwompCapsulePrice1 = get_capsule_value(thwompCapsulePrice1)
    thwompCapsulePrice2 = get_capsule_value(thwompCapsulePrice2)
    thwompCapsulePrice34 = get_capsule_value(thwompCapsulePrice34)
    thwompCapsuleShopOdds12 = get_capsule_value(thwompCapsuleShopOdds12)
    thwompCapsuleShopOdds34 = get_capsule_value(thwompCapsuleShopOdds34)
    thwompCapsuleSpaceOdds1 = get_capsule_value(thwompCapsuleSpaceOdds1)
    thwompCapsuleSpaceOdds2 = get_capsule_value(thwompCapsuleSpaceOdds2)
    thwompCapsuleSpaceOdds34 = get_capsule_value(thwompCapsuleSpaceOdds34)

    warpCapsulePrice1 = get_capsule_value(warpCapsulePrice1)
    warpCapsulePrice2 = get_capsule_value(warpCapsulePrice2)
    warpCapsulePrice34 = get_capsule_value(warpCapsulePrice34)
    warpCapsuleShopOdds12 = get_capsule_value(warpCapsuleShopOdds12)
    warpCapsuleShopOdds34 = get_capsule_value(warpCapsuleShopOdds34)
    warpCapsuleSpaceOdds1 = get_capsule_value(warpCapsuleSpaceOdds1)
    warpCapsuleSpaceOdds2 = get_capsule_value(warpCapsuleSpaceOdds2)
    warpCapsuleSpaceOdds34 = get_capsule_value(warpCapsuleSpaceOdds34)

    bombCapsulePrice1 = get_capsule_value(bombCapsulePrice1)
    bombCapsulePrice2 = get_capsule_value(bombCapsulePrice2)
    bombCapsulePrice34 = get_capsule_value(bombCapsulePrice34)
    bombCapsuleShopOdds12 = get_capsule_value(bombCapsuleShopOdds12)
    bombCapsuleShopOdds34 = get_capsule_value(bombCapsuleShopOdds34)
    bombCapsuleSpaceOdds1 = get_capsule_value(bombCapsuleSpaceOdds1)
    bombCapsuleSpaceOdds2 = get_capsule_value(bombCapsuleSpaceOdds2)
    bombCapsuleSpaceOdds34 = get_capsule_value(bombCapsuleSpaceOdds34)

    fireballCapsulePrice1 = get_capsule_value(fireballCapsulePrice1)
    fireballCapsulePrice2 = get_capsule_value(fireballCapsulePrice2)
    fireballCapsulePrice34 = get_capsule_value(fireballCapsulePrice34)
    fireballCapsuleShopOdds12 = get_capsule_value(fireballCapsuleShopOdds12)
    fireballCapsuleShopOdds34 = get_capsule_value(fireballCapsuleShopOdds34)
    fireballCapsuleSpaceOdds1 = get_capsule_value(fireballCapsuleSpaceOdds1)
    fireballCapsuleSpaceOdds2 = get_capsule_value(fireballCapsuleSpaceOdds2)
    fireballCapsuleSpaceOdds34 = get_capsule_value(fireballCapsuleSpaceOdds34)

    flowerCapsulePrice1 = get_capsule_value(flowerCapsulePrice1)
    flowerCapsulePrice2 = get_capsule_value(flowerCapsulePrice2)
    flowerCapsulePrice34 = get_capsule_value(flowerCapsulePrice34)
    flowerCapsuleShopOdds12 = get_capsule_value(flowerCapsuleShopOdds12)
    flowerCapsuleShopOdds34 = get_capsule_value(flowerCapsuleShopOdds34)
    flowerCapsuleSpaceOdds1 = get_capsule_value(flowerCapsuleSpaceOdds1)
    flowerCapsuleSpaceOdds2 = get_capsule_value(flowerCapsuleSpaceOdds2)
    flowerCapsuleSpaceOdds34 = get_capsule_value(flowerCapsuleSpaceOdds34)

    eggCapsulePrice1 = get_capsule_value(eggCapsulePrice1)
    eggCapsulePrice2 = get_capsule_value(eggCapsulePrice2)
    eggCapsulePrice34 = get_capsule_value(eggCapsulePrice34)
    eggCapsuleShopOdds12 = get_capsule_value(eggCapsuleShopOdds12)
    eggCapsuleShopOdds34 = get_capsule_value(eggCapsuleShopOdds34)
    eggCapsuleSpaceOdds1 = get_capsule_value(eggCapsuleSpaceOdds1)
    eggCapsuleSpaceOdds2 = get_capsule_value(eggCapsuleSpaceOdds2)
    eggCapsuleSpaceOdds34 = get_capsule_value(eggCapsuleSpaceOdds34)

    vacuumCapsulePrice1 = get_capsule_value(vacuumCapsulePrice1)
    vacuumCapsulePrice2 = get_capsule_value(vacuumCapsulePrice2)
    vacuumCapsulePrice34 = get_capsule_value(vacuumCapsulePrice34)
    vacuumCapsuleShopOdds12 = get_capsule_value(vacuumCapsuleShopOdds12)
    vacuumCapsuleShopOdds34 = get_capsule_value(vacuumCapsuleShopOdds34)
    vacuumCapsuleSpaceOdds1 = get_capsule_value(vacuumCapsuleSpaceOdds1)
    vacuumCapsuleSpaceOdds2 = get_capsule_value(vacuumCapsuleSpaceOdds2)
    vacuumCapsuleSpaceOdds34 = get_capsule_value(vacuumCapsuleSpaceOdds34)

    magicCapsulePrice1 = get_capsule_value(magicCapsulePrice1)
    magicCapsulePrice2 = get_capsule_value(magicCapsulePrice2)
    magicCapsulePrice34 = get_capsule_value(magicCapsulePrice34)
    magicCapsuleShopOdds12 = get_capsule_value(magicCapsuleShopOdds12)
    magicCapsuleShopOdds34 = get_capsule_value(magicCapsuleShopOdds34)
    magicCapsuleSpaceOdds1 = get_capsule_value(magicCapsuleSpaceOdds1)
    magicCapsuleSpaceOdds2 = get_capsule_value(magicCapsuleSpaceOdds2)
    magicCapsuleSpaceOdds34 = get_capsule_value(magicCapsuleSpaceOdds34)

    tripleCapsulePrice1 = get_capsule_value(tripleCapsulePrice1)
    tripleCapsulePrice2 = get_capsule_value(tripleCapsulePrice2)
    tripleCapsulePrice34 = get_capsule_value(tripleCapsulePrice34)
    tripleCapsuleShopOdds12 = get_capsule_value(tripleCapsuleShopOdds12)
    tripleCapsuleShopOdds34 = get_capsule_value(tripleCapsuleShopOdds34)
    tripleCapsuleSpaceOdds1 = get_capsule_value(tripleCapsuleSpaceOdds1)
    tripleCapsuleSpaceOdds2 = get_capsule_value(tripleCapsuleSpaceOdds2)
    tripleCapsuleSpaceOdds34 = get_capsule_value(tripleCapsuleSpaceOdds34)

    koopaCapsulePrice1 = get_capsule_value(koopaCapsulePrice1)
    koopaCapsulePrice2 = get_capsule_value(koopaCapsulePrice2)
    koopaCapsulePrice34 = get_capsule_value(koopaCapsulePrice34)
    koopaCapsuleShopOdds12 = get_capsule_value(koopaCapsuleShopOdds12)
    koopaCapsuleShopOdds34 = get_capsule_value(koopaCapsuleShopOdds34)
    koopaCapsuleSpaceOdds1 = get_capsule_value(koopaCapsuleSpaceOdds1)
    koopaCapsuleSpaceOdds2 = get_capsule_value(koopaCapsuleSpaceOdds2)
    koopaCapsuleSpaceOdds34 = get_capsule_value(koopaCapsuleSpaceOdds34)

    poisonMushroomPrice1 = get_capsule_value(poisonMushroomPrice1)
    poisonMushroomPrice2 = get_capsule_value(poisonMushroomPrice2)
    poisonMushroomPrice34 = get_capsule_value(poisonMushroomPrice34)
    poisonMushroomShopOdds12 = get_capsule_value(poisonMushroomShopOdds12)
    poisonMushroomShopOdds34 = get_capsule_value(poisonMushroomShopOdds34)
    poisonMushroomSpaceOdds1 = get_capsule_value(poisonMushroomSpaceOdds1)
    poisonMushroomSpaceOdds2 = get_capsule_value(poisonMushroomSpaceOdds2)
    poisonMushroomSpaceOdds34 = get_capsule_value(poisonMushroomSpaceOdds34)

    orbBagCapsulePrice1 = get_capsule_value(orbBagCapsulePrice1)
    orbBagCapsulePrice2 = get_capsule_value(orbBagCapsulePrice2)
    orbBagCapsulePrice34 = get_capsule_value(orbBagCapsulePrice34)
    orbBagCapsuleShopOdds12 = get_capsule_value(orbBagCapsuleShopOdds12)
    orbBagCapsuleShopOdds34 = get_capsule_value(orbBagCapsuleShopOdds34)
    orbBagCapsuleSpaceOdds1 = get_capsule_value(orbBagCapsuleSpaceOdds1)
    orbBagCapsuleSpaceOdds2 = get_capsule_value(orbBagCapsuleSpaceOdds2)
    orbBagCapsuleSpaceOdds34 = get_capsule_value(orbBagCapsuleSpaceOdds34)

    mysteryCapsulePrice1 = get_capsule_value(mysteryCapsulePrice1)
    mysteryCapsulePrice2 = get_capsule_value(mysteryCapsulePrice2)
    mysteryCapsulePrice34 = get_capsule_value(mysteryCapsulePrice34)
    mysteryCapsuleShopOdds12 = get_capsule_value(mysteryCapsuleShopOdds12)
    mysteryCapsuleShopOdds34 = get_capsule_value(mysteryCapsuleShopOdds34)
    mysteryCapsuleSpaceOdds1 = get_capsule_value(mysteryCapsuleSpaceOdds1)
    mysteryCapsuleSpaceOdds2 = get_capsule_value(mysteryCapsuleSpaceOdds2)
    mysteryCapsuleSpaceOdds34 = get_capsule_value(mysteryCapsuleSpaceOdds34)

    dkCapsulePrice1 = get_capsule_value(dkCapsulePrice1)
    dkCapsulePrice2 = get_capsule_value(dkCapsulePrice2)
    dkCapsulePrice34 = get_capsule_value(dkCapsulePrice34)
    dkCapsuleShopOdds12 = get_capsule_value(dkCapsuleShopOdds12)
    dkCapsuleShopOdds34 = get_capsule_value(dkCapsuleShopOdds34)
    dkCapsuleSpaceOdds1 = get_capsule_value(dkCapsuleSpaceOdds1)
    dkCapsuleSpaceOdds2 = get_capsule_value(dkCapsuleSpaceOdds2)
    dkCapsuleSpaceOdds34 = get_capsule_value(dkCapsuleSpaceOdds34)

    duelCapsulePrice1 = get_capsule_value(duelCapsulePrice1)
    duelCapsulePrice2 = get_capsule_value(duelCapsulePrice2)
    duelCapsulePrice34 = get_capsule_value(duelCapsulePrice34)
    duelCapsuleShopOdds12 = get_capsule_value(duelCapsuleShopOdds12)
    duelCapsuleShopOdds34 = get_capsule_value(duelCapsuleShopOdds34)
    duelCapsuleSpaceOdds1 = get_capsule_value(duelCapsuleSpaceOdds1)
    duelCapsuleSpaceOdds2 = get_capsule_value(duelCapsuleSpaceOdds2)
    duelCapsuleSpaceOdds34 = get_capsule_value(duelCapsuleSpaceOdds34)

    # Weights lists
    shopOdds12 = [
        mushroomCapsuleShopOdds12, goldenMushroomCapsuleShopOdds12, metalMushroomCapsuleShopOdds12,
        slowMushroomCapsuleShopOdds12, flutterCapsuleShopOdds12, cannonCapsuleShopOdds12,
        snackCapsuleShopOdds12, lakituCapsuleShopOdds12, hammerBroCapsuleShopOdds12,
        piranhaPlantCapsuleShopOdds12, spearGuyCapsuleShopOdds12, kamekCapsuleShopOdds12,
        toadyCapsuleShopOdds12, mrBlizzardCapsuleShopOdds12, banditCapsuleShopOdds12,
        pinkBooCapsuleShopOdds12, spinyCapsuleShopOdds12, zapCapsuleShopOdds12,
        tweesterCapsuleShopOdds12, thwompCapsuleShopOdds12, warpCapsuleShopOdds12,
        bombCapsuleShopOdds12, fireballCapsuleShopOdds12, flowerCapsuleShopOdds12,
        eggCapsuleShopOdds12, vacuumCapsuleShopOdds12, magicCapsuleShopOdds12,
        tripleCapsuleShopOdds12, koopaCapsuleShopOdds12, mysteryCapsuleShopOdds12,
        duelCapsuleShopOdds12, dkCapsuleShopOdds12, orbBagCapsuleShopOdds12
    ]

    shopOdds34 = [
        mushroomCapsuleShopOdds34, goldenMushroomCapsuleShopOdds34, metalMushroomCapsuleShopOdds34,
        slowMushroomCapsuleShopOdds34, flutterCapsuleShopOdds34, cannonCapsuleShopOdds34,
        snackCapsuleShopOdds34, lakituCapsuleShopOdds34, hammerBroCapsuleShopOdds34,
        piranhaPlantCapsuleShopOdds34, spearGuyCapsuleShopOdds34, kamekCapsuleShopOdds34,
        toadyCapsuleShopOdds34, mrBlizzardCapsuleShopOdds34, banditCapsuleShopOdds34,
        pinkBooCapsuleShopOdds34, spinyCapsuleShopOdds34, zapCapsuleShopOdds34,
        tweesterCapsuleShopOdds34, thwompCapsuleShopOdds34, warpCapsuleShopOdds34,
        bombCapsuleShopOdds34, fireballCapsuleShopOdds34, flowerCapsuleShopOdds34,
        eggCapsuleShopOdds34, vacuumCapsuleShopOdds34, magicCapsuleShopOdds34,
        tripleCapsuleShopOdds34, koopaCapsuleShopOdds34, mysteryCapsuleShopOdds34,
        duelCapsuleShopOdds34, dkCapsuleShopOdds34, orbBagCapsuleShopOdds34
    ]

    spaceOdds1 = [
        mushroomCapsuleSpaceOdds1, goldenMushroomCapsuleSpaceOdds1, metalMushroomCapsuleSpaceOdds1,
        slowMushroomCapsuleSpaceOdds1, flutterCapsuleSpaceOdds1, cannonCapsuleSpaceOdds1,
        snackCapsuleSpaceOdds1, lakituCapsuleSpaceOdds1, hammerBroCapsuleSpaceOdds1,
        piranhaPlantCapsuleSpaceOdds1, spearGuyCapsuleSpaceOdds1, kamekCapsuleSpaceOdds1,
        toadyCapsuleSpaceOdds1, mrBlizzardCapsuleSpaceOdds1, banditCapsuleSpaceOdds1,
        pinkBooCapsuleSpaceOdds1, spinyCapsuleSpaceOdds1, zapCapsuleSpaceOdds1,
        tweesterCapsuleSpaceOdds1, thwompCapsuleSpaceOdds1, warpCapsuleSpaceOdds1,
        bombCapsuleSpaceOdds1, fireballCapsuleSpaceOdds1, flowerCapsuleSpaceOdds1,
        eggCapsuleSpaceOdds1, vacuumCapsuleSpaceOdds1, magicCapsuleSpaceOdds1,
        tripleCapsuleSpaceOdds1, koopaCapsuleSpaceOdds1, mysteryCapsuleSpaceOdds1,
        duelCapsuleSpaceOdds1, dkCapsuleSpaceOdds1, orbBagCapsuleSpaceOdds1
    ]

    spaceOdds2 = [
        mushroomCapsuleSpaceOdds2, goldenMushroomCapsuleSpaceOdds2, metalMushroomCapsuleSpaceOdds2,
        slowMushroomCapsuleSpaceOdds2, flutterCapsuleSpaceOdds2, cannonCapsuleSpaceOdds2,
        snackCapsuleSpaceOdds2, lakituCapsuleSpaceOdds2, hammerBroCapsuleSpaceOdds2,
        piranhaPlantCapsuleSpaceOdds2, spearGuyCapsuleSpaceOdds2, kamekCapsuleSpaceOdds2,
        toadyCapsuleSpaceOdds2, mrBlizzardCapsuleSpaceOdds2, banditCapsuleSpaceOdds2,
        pinkBooCapsuleSpaceOdds2, spinyCapsuleSpaceOdds2, zapCapsuleSpaceOdds2,
        tweesterCapsuleSpaceOdds2, thwompCapsuleSpaceOdds2, warpCapsuleSpaceOdds2,
        bombCapsuleSpaceOdds2, fireballCapsuleSpaceOdds2, flowerCapsuleSpaceOdds2,
        eggCapsuleSpaceOdds2, vacuumCapsuleSpaceOdds2, magicCapsuleSpaceOdds2,
        tripleCapsuleSpaceOdds2, koopaCapsuleSpaceOdds2, mysteryCapsuleSpaceOdds2,
        duelCapsuleSpaceOdds2, dkCapsuleSpaceOdds2, orbBagCapsuleSpaceOdds2
    ]
    
    spaceOdds34 = [
        mushroomCapsuleSpaceOdds34, goldenMushroomCapsuleSpaceOdds34, metalMushroomCapsuleSpaceOdds34,
        slowMushroomCapsuleSpaceOdds34, flutterCapsuleSpaceOdds34, cannonCapsuleSpaceOdds34,
        snackCapsuleSpaceOdds34, lakituCapsuleSpaceOdds34, hammerBroCapsuleSpaceOdds34,
        piranhaPlantCapsuleSpaceOdds34, spearGuyCapsuleSpaceOdds34, kamekCapsuleSpaceOdds34,
        toadyCapsuleSpaceOdds34, mrBlizzardCapsuleSpaceOdds34, banditCapsuleSpaceOdds34,
        pinkBooCapsuleSpaceOdds34, spinyCapsuleSpaceOdds34, zapCapsuleSpaceOdds34,
        tweesterCapsuleSpaceOdds34, thwompCapsuleSpaceOdds34, warpCapsuleSpaceOdds34,
        bombCapsuleSpaceOdds34, fireballCapsuleSpaceOdds34, flowerCapsuleSpaceOdds34,
        eggCapsuleSpaceOdds34, vacuumCapsuleSpaceOdds34, magicCapsuleSpaceOdds34,
        tripleCapsuleSpaceOdds34, koopaCapsuleSpaceOdds34, mysteryCapsuleSpaceOdds34,
        duelCapsuleSpaceOdds34, dkCapsuleSpaceOdds34, orbBagCapsuleSpaceOdds34
    ]

    shopOdds12Weights = sum(int(weight) if weight else 0 for weight in shopOdds12)
    shopOdds34Weights = sum(int(weight) if weight else 0 for weight in shopOdds34)
    spaceOdds1Weights = sum(int(weight) if weight else 0 for weight in spaceOdds1)
    spaceOdds2Weights = sum(int(weight) if weight else 0 for weight in spaceOdds2)
    spaceOdds34Weights = sum(int(weight) if weight else 0 for weight in spaceOdds34)

    def calculateWeight(weight, total):
        # Convert weight to int, default to 0 if empty or None
        weight = int(weight) if weight else 0
        # Check for total being zero to avoid division by zero
        if total <= 0:
            return 0  # Return 0 if total is zero or negative
        if total < 100:
            return weight  # Return the weight directly if total is less than 100
        else:
            percentage = (weight / total) * 100
            if 0 < percentage < 1:
                return math.ceil(percentage)
            return round(percentage)

    # Calculate weights for shop odds 12
    mushroomCapsuleShopOdds12 = calculateWeight(mushroomCapsuleShopOdds12, shopOdds12Weights)
    goldenMushroomCapsuleShopOdds12 = calculateWeight(goldenMushroomCapsuleShopOdds12, shopOdds12Weights)
    metalMushroomCapsuleShopOdds12 = calculateWeight(metalMushroomCapsuleShopOdds12, shopOdds12Weights)
    slowMushroomCapsuleShopOdds12 = calculateWeight(slowMushroomCapsuleShopOdds12, shopOdds12Weights)
    flutterCapsuleShopOdds12 = calculateWeight(flutterCapsuleShopOdds12, shopOdds12Weights)
    cannonCapsuleShopOdds12 = calculateWeight(cannonCapsuleShopOdds12, shopOdds12Weights)
    snackCapsuleShopOdds12 = calculateWeight(snackCapsuleShopOdds12, shopOdds12Weights)
    lakituCapsuleShopOdds12 = calculateWeight(lakituCapsuleShopOdds12, shopOdds12Weights)
    hammerBroCapsuleShopOdds12 = calculateWeight(hammerBroCapsuleShopOdds12, shopOdds12Weights)
    piranhaPlantCapsuleShopOdds12 = calculateWeight(piranhaPlantCapsuleShopOdds12, shopOdds12Weights)
    spearGuyCapsuleShopOdds12 = calculateWeight(spearGuyCapsuleShopOdds12, shopOdds12Weights)
    kamekCapsuleShopOdds12 = calculateWeight(kamekCapsuleShopOdds12, shopOdds12Weights)
    toadyCapsuleShopOdds12 = calculateWeight(toadyCapsuleShopOdds12, shopOdds12Weights)
    mrBlizzardCapsuleShopOdds12 = calculateWeight(mrBlizzardCapsuleShopOdds12, shopOdds12Weights)
    banditCapsuleShopOdds12 = calculateWeight(banditCapsuleShopOdds12, shopOdds12Weights)
    pinkBooCapsuleShopOdds12 = calculateWeight(pinkBooCapsuleShopOdds12, shopOdds12Weights)
    spinyCapsuleShopOdds12 = calculateWeight(spinyCapsuleShopOdds12, shopOdds12Weights)
    zapCapsuleShopOdds12 = calculateWeight(zapCapsuleShopOdds12, shopOdds12Weights)
    tweesterCapsuleShopOdds12 = calculateWeight(tweesterCapsuleShopOdds12, shopOdds12Weights)
    thwompCapsuleShopOdds12 = calculateWeight(thwompCapsuleShopOdds12, shopOdds12Weights)
    warpCapsuleShopOdds12 = calculateWeight(warpCapsuleShopOdds12, shopOdds12Weights)
    bombCapsuleShopOdds12 = calculateWeight(bombCapsuleShopOdds12, shopOdds12Weights)
    fireballCapsuleShopOdds12 = calculateWeight(fireballCapsuleShopOdds12, shopOdds12Weights)
    flowerCapsuleShopOdds12 = calculateWeight(flowerCapsuleShopOdds12, shopOdds12Weights)
    eggCapsuleShopOdds12 = calculateWeight(eggCapsuleShopOdds12, shopOdds12Weights)
    vacuumCapsuleShopOdds12 = calculateWeight(vacuumCapsuleShopOdds12, shopOdds12Weights)
    magicCapsuleShopOdds12 = calculateWeight(magicCapsuleShopOdds12, shopOdds12Weights)
    tripleCapsuleShopOdds12 = calculateWeight(tripleCapsuleShopOdds12, shopOdds12Weights)
    koopaCapsuleShopOdds12 = calculateWeight(koopaCapsuleShopOdds12, shopOdds12Weights)
    mysteryCapsuleShopOdds12 = calculateWeight(mysteryCapsuleShopOdds12, shopOdds12Weights)
    duelCapsuleShopOdds12 = calculateWeight(duelCapsuleShopOdds12, shopOdds12Weights)
    dkCapsuleShopOdds12 = calculateWeight(dkCapsuleShopOdds12, shopOdds12Weights)
    orbBagCapsuleShopOdds12 = calculateWeight(orbBagCapsuleShopOdds12, shopOdds12Weights)

    # Calculate weights for shop odds 34
    mushroomCapsuleShopOdds34 = calculateWeight(mushroomCapsuleShopOdds34, shopOdds34Weights)
    goldenMushroomCapsuleShopOdds34 = calculateWeight(goldenMushroomCapsuleShopOdds34, shopOdds34Weights)
    metalMushroomCapsuleShopOdds34 = calculateWeight(metalMushroomCapsuleShopOdds34, shopOdds34Weights)
    slowMushroomCapsuleShopOdds34 = calculateWeight(slowMushroomCapsuleShopOdds34, shopOdds34Weights)
    flutterCapsuleShopOdds34 = calculateWeight(flutterCapsuleShopOdds34, shopOdds34Weights)
    cannonCapsuleShopOdds34 = calculateWeight(cannonCapsuleShopOdds34, shopOdds34Weights)
    snackCapsuleShopOdds34 = calculateWeight(snackCapsuleShopOdds34, shopOdds34Weights)
    lakituCapsuleShopOdds34 = calculateWeight(lakituCapsuleShopOdds34, shopOdds34Weights)
    hammerBroCapsuleShopOdds34 = calculateWeight(hammerBroCapsuleShopOdds34, shopOdds34Weights)
    piranhaPlantCapsuleShopOdds34 = calculateWeight(piranhaPlantCapsuleShopOdds34, shopOdds34Weights)
    spearGuyCapsuleShopOdds34 = calculateWeight(spearGuyCapsuleShopOdds34, shopOdds34Weights)
    kamekCapsuleShopOdds34 = calculateWeight(kamekCapsuleShopOdds34, shopOdds34Weights)
    toadyCapsuleShopOdds34 = calculateWeight(toadyCapsuleShopOdds34, shopOdds34Weights)
    mrBlizzardCapsuleShopOdds34 = calculateWeight(mrBlizzardCapsuleShopOdds34, shopOdds34Weights)
    banditCapsuleShopOdds34 = calculateWeight(banditCapsuleShopOdds34, shopOdds34Weights)
    pinkBooCapsuleShopOdds34 = calculateWeight(pinkBooCapsuleShopOdds34, shopOdds34Weights)
    spinyCapsuleShopOdds34 = calculateWeight(spinyCapsuleShopOdds34, shopOdds34Weights)
    zapCapsuleShopOdds34 = calculateWeight(zapCapsuleShopOdds34, shopOdds34Weights)
    tweesterCapsuleShopOdds34 = calculateWeight(tweesterCapsuleShopOdds34, shopOdds34Weights)
    thwompCapsuleShopOdds34 = calculateWeight(thwompCapsuleShopOdds34, shopOdds34Weights)
    warpCapsuleShopOdds34 = calculateWeight(warpCapsuleShopOdds34, shopOdds34Weights)
    bombCapsuleShopOdds34 = calculateWeight(bombCapsuleShopOdds34, shopOdds34Weights)
    fireballCapsuleShopOdds34 = calculateWeight(fireballCapsuleShopOdds34, shopOdds34Weights)
    flowerCapsuleShopOdds34 = calculateWeight(flowerCapsuleShopOdds34, shopOdds34Weights)
    eggCapsuleShopOdds34 = calculateWeight(eggCapsuleShopOdds34, shopOdds34Weights)
    vacuumCapsuleShopOdds34 = calculateWeight(vacuumCapsuleShopOdds34, shopOdds34Weights)
    magicCapsuleShopOdds34 = calculateWeight(magicCapsuleShopOdds34, shopOdds34Weights)
    tripleCapsuleShopOdds34 = calculateWeight(tripleCapsuleShopOdds34, shopOdds34Weights)
    koopaCapsuleShopOdds34 = calculateWeight(koopaCapsuleShopOdds34, shopOdds34Weights)
    mysteryCapsuleShopOdds34 = calculateWeight(mysteryCapsuleShopOdds34, shopOdds34Weights)
    duelCapsuleShopOdds34 = calculateWeight(duelCapsuleShopOdds34, shopOdds34Weights)
    dkCapsuleShopOdds34 = calculateWeight(dkCapsuleShopOdds34, shopOdds34Weights)
    orbBagCapsuleShopOdds34 = calculateWeight(orbBagCapsuleShopOdds34, shopOdds34Weights)

    # Calculate weights for space odds 1
    mushroomCapsuleSpaceOdds1 = calculateWeight(mushroomCapsuleSpaceOdds1, spaceOdds1Weights)
    goldenMushroomCapsuleSpaceOdds1 = calculateWeight(goldenMushroomCapsuleSpaceOdds1, spaceOdds1Weights)
    metalMushroomCapsuleSpaceOdds1 = calculateWeight(metalMushroomCapsuleSpaceOdds1, spaceOdds1Weights)
    slowMushroomCapsuleSpaceOdds1 = calculateWeight(slowMushroomCapsuleSpaceOdds1, spaceOdds1Weights)
    flutterCapsuleSpaceOdds1 = calculateWeight(flutterCapsuleSpaceOdds1, spaceOdds1Weights)
    cannonCapsuleSpaceOdds1 = calculateWeight(cannonCapsuleSpaceOdds1, spaceOdds1Weights)
    snackCapsuleSpaceOdds1 = calculateWeight(snackCapsuleSpaceOdds1, spaceOdds1Weights)
    lakituCapsuleSpaceOdds1 = calculateWeight(lakituCapsuleSpaceOdds1, spaceOdds1Weights)
    hammerBroCapsuleSpaceOdds1 = calculateWeight(hammerBroCapsuleSpaceOdds1, spaceOdds1Weights)
    piranhaPlantCapsuleSpaceOdds1 = calculateWeight(piranhaPlantCapsuleSpaceOdds1, spaceOdds1Weights)
    spearGuyCapsuleSpaceOdds1 = calculateWeight(spearGuyCapsuleSpaceOdds1, spaceOdds1Weights)
    kamekCapsuleSpaceOdds1 = calculateWeight(kamekCapsuleSpaceOdds1, spaceOdds1Weights)
    toadyCapsuleSpaceOdds1 = calculateWeight(toadyCapsuleSpaceOdds1, spaceOdds1Weights)
    mrBlizzardCapsuleSpaceOdds1 = calculateWeight(mrBlizzardCapsuleSpaceOdds1, spaceOdds1Weights)
    banditCapsuleSpaceOdds1 = calculateWeight(banditCapsuleSpaceOdds1, spaceOdds1Weights)
    pinkBooCapsuleSpaceOdds1 = calculateWeight(pinkBooCapsuleSpaceOdds1, spaceOdds1Weights)
    spinyCapsuleSpaceOdds1 = calculateWeight(spinyCapsuleSpaceOdds1, spaceOdds1Weights)
    zapCapsuleSpaceOdds1 = calculateWeight(zapCapsuleSpaceOdds1, spaceOdds1Weights)
    tweesterCapsuleSpaceOdds1 = calculateWeight(tweesterCapsuleSpaceOdds1, spaceOdds1Weights)
    thwompCapsuleSpaceOdds1 = calculateWeight(thwompCapsuleSpaceOdds1, spaceOdds1Weights)
    warpCapsuleSpaceOdds1 = calculateWeight(warpCapsuleSpaceOdds1, spaceOdds1Weights)
    bombCapsuleSpaceOdds1 = calculateWeight(bombCapsuleSpaceOdds1, spaceOdds1Weights)
    fireballCapsuleSpaceOdds1 = calculateWeight(fireballCapsuleSpaceOdds1, spaceOdds1Weights)
    flowerCapsuleSpaceOdds1 = calculateWeight(flowerCapsuleSpaceOdds1, spaceOdds1Weights)
    eggCapsuleSpaceOdds1 = calculateWeight(eggCapsuleSpaceOdds1, spaceOdds1Weights)
    vacuumCapsuleSpaceOdds1 = calculateWeight(vacuumCapsuleSpaceOdds1, spaceOdds1Weights)
    magicCapsuleSpaceOdds1 = calculateWeight(magicCapsuleSpaceOdds1, spaceOdds1Weights)
    tripleCapsuleSpaceOdds1 = calculateWeight(tripleCapsuleSpaceOdds1, spaceOdds1Weights)
    koopaCapsuleSpaceOdds1 = calculateWeight(koopaCapsuleSpaceOdds1, spaceOdds1Weights)
    mysteryCapsuleSpaceOdds1 = calculateWeight(mysteryCapsuleSpaceOdds1, spaceOdds1Weights)
    duelCapsuleSpaceOdds1 = calculateWeight(duelCapsuleSpaceOdds1, spaceOdds1Weights)
    dkCapsuleSpaceOdds1 = calculateWeight(dkCapsuleSpaceOdds1, spaceOdds1Weights)
    orbBagCapsuleSpaceOdds1 = calculateWeight(orbBagCapsuleSpaceOdds1, spaceOdds1Weights)

    # Calculate weights for space odds 2
    mushroomCapsuleSpaceOdds2 = calculateWeight(mushroomCapsuleSpaceOdds2, spaceOdds2Weights)
    goldenMushroomCapsuleSpaceOdds2 = calculateWeight(goldenMushroomCapsuleSpaceOdds2, spaceOdds2Weights)
    metalMushroomCapsuleSpaceOdds2 = calculateWeight(metalMushroomCapsuleSpaceOdds2, spaceOdds2Weights)
    slowMushroomCapsuleSpaceOdds2 = calculateWeight(slowMushroomCapsuleSpaceOdds2, spaceOdds2Weights)
    flutterCapsuleSpaceOdds2 = calculateWeight(flutterCapsuleSpaceOdds2, spaceOdds2Weights)
    cannonCapsuleSpaceOdds2 = calculateWeight(cannonCapsuleSpaceOdds2, spaceOdds2Weights)
    snackCapsuleSpaceOdds2 = calculateWeight(snackCapsuleSpaceOdds2, spaceOdds2Weights)
    lakituCapsuleSpaceOdds2 = calculateWeight(lakituCapsuleSpaceOdds2, spaceOdds2Weights)
    hammerBroCapsuleSpaceOdds2 = calculateWeight(hammerBroCapsuleSpaceOdds2, spaceOdds2Weights)
    piranhaPlantCapsuleSpaceOdds2 = calculateWeight(piranhaPlantCapsuleSpaceOdds2, spaceOdds2Weights)
    spearGuyCapsuleSpaceOdds2 = calculateWeight(spearGuyCapsuleSpaceOdds2, spaceOdds2Weights)
    kamekCapsuleSpaceOdds2 = calculateWeight(kamekCapsuleSpaceOdds2, spaceOdds2Weights)
    toadyCapsuleSpaceOdds2 = calculateWeight(toadyCapsuleSpaceOdds2, spaceOdds2Weights)
    mrBlizzardCapsuleSpaceOdds2 = calculateWeight(mrBlizzardCapsuleSpaceOdds2, spaceOdds2Weights)
    banditCapsuleSpaceOdds2 = calculateWeight(banditCapsuleSpaceOdds2, spaceOdds2Weights)
    pinkBooCapsuleSpaceOdds2 = calculateWeight(pinkBooCapsuleSpaceOdds2, spaceOdds2Weights)
    spinyCapsuleSpaceOdds2 = calculateWeight(spinyCapsuleSpaceOdds2, spaceOdds2Weights)
    zapCapsuleSpaceOdds2 = calculateWeight(zapCapsuleSpaceOdds2, spaceOdds2Weights)
    tweesterCapsuleSpaceOdds2 = calculateWeight(tweesterCapsuleSpaceOdds2, spaceOdds2Weights)
    thwompCapsuleSpaceOdds2 = calculateWeight(thwompCapsuleSpaceOdds2, spaceOdds2Weights)
    warpCapsuleSpaceOdds2 = calculateWeight(warpCapsuleSpaceOdds2, spaceOdds2Weights)
    bombCapsuleSpaceOdds2 = calculateWeight(bombCapsuleSpaceOdds2, spaceOdds2Weights)
    fireballCapsuleSpaceOdds2 = calculateWeight(fireballCapsuleSpaceOdds2, spaceOdds2Weights)
    flowerCapsuleSpaceOdds2 = calculateWeight(flowerCapsuleSpaceOdds2, spaceOdds2Weights)
    eggCapsuleSpaceOdds2 = calculateWeight(eggCapsuleSpaceOdds2, spaceOdds2Weights)
    vacuumCapsuleSpaceOdds2 = calculateWeight(vacuumCapsuleSpaceOdds2, spaceOdds2Weights)
    magicCapsuleSpaceOdds2 = calculateWeight(magicCapsuleSpaceOdds2, spaceOdds2Weights)
    tripleCapsuleSpaceOdds2 = calculateWeight(tripleCapsuleSpaceOdds2, spaceOdds2Weights)
    koopaCapsuleSpaceOdds2 = calculateWeight(koopaCapsuleSpaceOdds2, spaceOdds2Weights)
    mysteryCapsuleSpaceOdds2 = calculateWeight(mysteryCapsuleSpaceOdds2, spaceOdds2Weights)
    duelCapsuleSpaceOdds2 = calculateWeight(duelCapsuleSpaceOdds2, spaceOdds2Weights)
    dkCapsuleSpaceOdds2 = calculateWeight(dkCapsuleSpaceOdds2, spaceOdds2Weights)
    orbBagCapsuleSpaceOdds2 = calculateWeight(orbBagCapsuleSpaceOdds2, spaceOdds2Weights)

    # Calculate weights for space odds 34
    mushroomCapsuleSpaceOdds34 = calculateWeight(mushroomCapsuleSpaceOdds34, spaceOdds34Weights)
    goldenMushroomCapsuleSpaceOdds34 = calculateWeight(goldenMushroomCapsuleSpaceOdds34, spaceOdds34Weights)
    metalMushroomCapsuleSpaceOdds34 = calculateWeight(metalMushroomCapsuleSpaceOdds34, spaceOdds34Weights)
    slowMushroomCapsuleSpaceOdds34 = calculateWeight(slowMushroomCapsuleSpaceOdds34, spaceOdds34Weights)
    flutterCapsuleSpaceOdds34 = calculateWeight(flutterCapsuleSpaceOdds34, spaceOdds34Weights)
    cannonCapsuleSpaceOdds34 = calculateWeight(cannonCapsuleSpaceOdds34, spaceOdds34Weights)
    snackCapsuleSpaceOdds34 = calculateWeight(snackCapsuleSpaceOdds34, spaceOdds34Weights)
    lakituCapsuleSpaceOdds34 = calculateWeight(lakituCapsuleSpaceOdds34, spaceOdds34Weights)
    hammerBroCapsuleSpaceOdds34 = calculateWeight(hammerBroCapsuleSpaceOdds34, spaceOdds34Weights)
    piranhaPlantCapsuleSpaceOdds34 = calculateWeight(piranhaPlantCapsuleSpaceOdds34, spaceOdds34Weights)
    spearGuyCapsuleSpaceOdds34 = calculateWeight(spearGuyCapsuleSpaceOdds34, spaceOdds34Weights)
    kamekCapsuleSpaceOdds34 = calculateWeight(kamekCapsuleSpaceOdds34, spaceOdds34Weights)
    toadyCapsuleSpaceOdds34 = calculateWeight(toadyCapsuleSpaceOdds34, spaceOdds34Weights)
    mrBlizzardCapsuleSpaceOdds34 = calculateWeight(mrBlizzardCapsuleSpaceOdds34, spaceOdds34Weights)
    banditCapsuleSpaceOdds34 = calculateWeight(banditCapsuleSpaceOdds34, spaceOdds34Weights)
    pinkBooCapsuleSpaceOdds34 = calculateWeight(pinkBooCapsuleSpaceOdds34, spaceOdds34Weights)
    spinyCapsuleSpaceOdds34 = calculateWeight(spinyCapsuleSpaceOdds34, spaceOdds34Weights)
    zapCapsuleSpaceOdds34 = calculateWeight(zapCapsuleSpaceOdds34, spaceOdds34Weights)
    tweesterCapsuleSpaceOdds34 = calculateWeight(tweesterCapsuleSpaceOdds34, spaceOdds34Weights)
    thwompCapsuleSpaceOdds34 = calculateWeight(thwompCapsuleSpaceOdds34, spaceOdds34Weights)
    warpCapsuleSpaceOdds34 = calculateWeight(warpCapsuleSpaceOdds34, spaceOdds34Weights)
    bombCapsuleSpaceOdds34 = calculateWeight(bombCapsuleSpaceOdds34, spaceOdds34Weights)
    fireballCapsuleSpaceOdds34 = calculateWeight(fireballCapsuleSpaceOdds34, spaceOdds34Weights)
    flowerCapsuleSpaceOdds34 = calculateWeight(flowerCapsuleSpaceOdds34, spaceOdds34Weights)
    eggCapsuleSpaceOdds34 = calculateWeight(eggCapsuleSpaceOdds34, spaceOdds34Weights)
    vacuumCapsuleSpaceOdds34 = calculateWeight(vacuumCapsuleSpaceOdds34, spaceOdds34Weights)
    magicCapsuleSpaceOdds34 = calculateWeight(magicCapsuleSpaceOdds34, spaceOdds34Weights)
    tripleCapsuleSpaceOdds34 = calculateWeight(tripleCapsuleSpaceOdds34, spaceOdds34Weights)
    koopaCapsuleSpaceOdds34 = calculateWeight(koopaCapsuleSpaceOdds34, spaceOdds34Weights)
    mysteryCapsuleSpaceOdds34 = calculateWeight(mysteryCapsuleSpaceOdds34, spaceOdds34Weights)
    duelCapsuleSpaceOdds34 = calculateWeight(duelCapsuleSpaceOdds34, spaceOdds34Weights)
    dkCapsuleSpaceOdds34 = calculateWeight(dkCapsuleSpaceOdds34, spaceOdds34Weights)
    orbBagCapsuleSpaceOdds34 = calculateWeight(orbBagCapsuleSpaceOdds34, spaceOdds34Weights)


    # Redefine Weights lists
    shopOdds12 = [
        mushroomCapsuleShopOdds12, goldenMushroomCapsuleShopOdds12, metalMushroomCapsuleShopOdds12,
        slowMushroomCapsuleShopOdds12, flutterCapsuleShopOdds12, cannonCapsuleShopOdds12,
        snackCapsuleShopOdds12, lakituCapsuleShopOdds12, hammerBroCapsuleShopOdds12,
        piranhaPlantCapsuleShopOdds12, spearGuyCapsuleShopOdds12, kamekCapsuleShopOdds12,
        toadyCapsuleShopOdds12, mrBlizzardCapsuleShopOdds12, banditCapsuleShopOdds12,
        pinkBooCapsuleShopOdds12, spinyCapsuleShopOdds12, zapCapsuleShopOdds12,
        tweesterCapsuleShopOdds12, thwompCapsuleShopOdds12, warpCapsuleShopOdds12,
        bombCapsuleShopOdds12, fireballCapsuleShopOdds12, flowerCapsuleShopOdds12,
        eggCapsuleShopOdds12, vacuumCapsuleShopOdds12, magicCapsuleShopOdds12,
        tripleCapsuleShopOdds12, koopaCapsuleShopOdds12, mysteryCapsuleShopOdds12,
        duelCapsuleShopOdds12, dkCapsuleShopOdds12, orbBagCapsuleShopOdds12
    ]

    shopOdds34 = [
        mushroomCapsuleShopOdds34, goldenMushroomCapsuleShopOdds34, metalMushroomCapsuleShopOdds34,
        slowMushroomCapsuleShopOdds34, flutterCapsuleShopOdds34, cannonCapsuleShopOdds34,
        snackCapsuleShopOdds34, lakituCapsuleShopOdds34, hammerBroCapsuleShopOdds34,
        piranhaPlantCapsuleShopOdds34, spearGuyCapsuleShopOdds34, kamekCapsuleShopOdds34,
        toadyCapsuleShopOdds34, mrBlizzardCapsuleShopOdds34, banditCapsuleShopOdds34,
        pinkBooCapsuleShopOdds34, spinyCapsuleShopOdds34, zapCapsuleShopOdds34,
        tweesterCapsuleShopOdds34, thwompCapsuleShopOdds34, warpCapsuleShopOdds34,
        bombCapsuleShopOdds34, fireballCapsuleShopOdds34, flowerCapsuleShopOdds34,
        eggCapsuleShopOdds34, vacuumCapsuleShopOdds34, magicCapsuleShopOdds34,
        tripleCapsuleShopOdds34, koopaCapsuleShopOdds34, mysteryCapsuleShopOdds34,
        duelCapsuleShopOdds34, dkCapsuleShopOdds34, orbBagCapsuleShopOdds34
    ]

    spaceOdds1 = [
        mushroomCapsuleSpaceOdds1, goldenMushroomCapsuleSpaceOdds1, metalMushroomCapsuleSpaceOdds1,
        slowMushroomCapsuleSpaceOdds1, flutterCapsuleSpaceOdds1, cannonCapsuleSpaceOdds1,
        snackCapsuleSpaceOdds1, lakituCapsuleSpaceOdds1, hammerBroCapsuleSpaceOdds1,
        piranhaPlantCapsuleSpaceOdds1, spearGuyCapsuleSpaceOdds1, kamekCapsuleSpaceOdds1,
        toadyCapsuleSpaceOdds1, mrBlizzardCapsuleSpaceOdds1, banditCapsuleSpaceOdds1,
        pinkBooCapsuleSpaceOdds1, spinyCapsuleSpaceOdds1, zapCapsuleSpaceOdds1,
        tweesterCapsuleSpaceOdds1, thwompCapsuleSpaceOdds1, warpCapsuleSpaceOdds1,
        bombCapsuleSpaceOdds1, fireballCapsuleSpaceOdds1, flowerCapsuleSpaceOdds1,
        eggCapsuleSpaceOdds1, vacuumCapsuleSpaceOdds1, magicCapsuleSpaceOdds1,
        tripleCapsuleSpaceOdds1, koopaCapsuleSpaceOdds1, mysteryCapsuleSpaceOdds1,
        duelCapsuleSpaceOdds1, dkCapsuleSpaceOdds1, orbBagCapsuleSpaceOdds1
    ]

    spaceOdds2 = [
        mushroomCapsuleSpaceOdds2, goldenMushroomCapsuleSpaceOdds2, metalMushroomCapsuleSpaceOdds2,
        slowMushroomCapsuleSpaceOdds2, flutterCapsuleSpaceOdds2, cannonCapsuleSpaceOdds2,
        snackCapsuleSpaceOdds2, lakituCapsuleSpaceOdds2, hammerBroCapsuleSpaceOdds2,
        piranhaPlantCapsuleSpaceOdds2, spearGuyCapsuleSpaceOdds2, kamekCapsuleSpaceOdds2,
        toadyCapsuleSpaceOdds2, mrBlizzardCapsuleSpaceOdds2, banditCapsuleSpaceOdds2,
        pinkBooCapsuleSpaceOdds2, spinyCapsuleSpaceOdds2, zapCapsuleSpaceOdds2,
        tweesterCapsuleSpaceOdds2, thwompCapsuleSpaceOdds2, warpCapsuleSpaceOdds2,
        bombCapsuleSpaceOdds2, fireballCapsuleSpaceOdds2, flowerCapsuleSpaceOdds2,
        eggCapsuleSpaceOdds2, vacuumCapsuleSpaceOdds2, magicCapsuleSpaceOdds2,
        tripleCapsuleSpaceOdds2, koopaCapsuleSpaceOdds2, mysteryCapsuleSpaceOdds2,
        duelCapsuleSpaceOdds2, dkCapsuleSpaceOdds2, orbBagCapsuleSpaceOdds2
    ]
    
    spaceOdds34 = [
        mushroomCapsuleSpaceOdds34, goldenMushroomCapsuleSpaceOdds34, metalMushroomCapsuleSpaceOdds34,
        slowMushroomCapsuleSpaceOdds34, flutterCapsuleSpaceOdds34, cannonCapsuleSpaceOdds34,
        snackCapsuleSpaceOdds34, lakituCapsuleSpaceOdds34, hammerBroCapsuleSpaceOdds34,
        piranhaPlantCapsuleSpaceOdds34, spearGuyCapsuleSpaceOdds34, kamekCapsuleSpaceOdds34,
        toadyCapsuleSpaceOdds34, mrBlizzardCapsuleSpaceOdds34, banditCapsuleSpaceOdds34,
        pinkBooCapsuleSpaceOdds34, spinyCapsuleSpaceOdds34, zapCapsuleSpaceOdds34,
        tweesterCapsuleSpaceOdds34, thwompCapsuleSpaceOdds34, warpCapsuleSpaceOdds34,
        bombCapsuleSpaceOdds34, fireballCapsuleSpaceOdds34, flowerCapsuleSpaceOdds34,
        eggCapsuleSpaceOdds34, vacuumCapsuleSpaceOdds34, magicCapsuleSpaceOdds34,
        tripleCapsuleSpaceOdds34, koopaCapsuleSpaceOdds34, mysteryCapsuleSpaceOdds34,
        duelCapsuleSpaceOdds34, dkCapsuleSpaceOdds34, orbBagCapsuleSpaceOdds34
    ]

    shopOdds12Weights = sum(weight for weight in shopOdds12)
    shopOdds34Weights = sum(weight for weight in shopOdds34)
    spaceOdds1Weights = sum(weight for weight in spaceOdds1)
    spaceOdds2Weights = sum(weight for weight in spaceOdds2)
    spaceOdds34Weights = sum(weight for weight in shopOdds34)

    if spaceOdds1Weights < 101:
        spaceOdds1Max = max(zip(spaceOdds1, spaceOdds1), key=lambda tuple: tuple[1])[0]

    if spaceOdds34Weights < 101:
        spaceOdds34Max = max(zip(spaceOdds34, spaceOdds34), key=lambda tuple: tuple[1])[0]

    if shopOdds12Weights < 101:
        shopOdds12Max = max(zip(shopOdds12, shopOdds12), key=lambda tuple: tuple[1])[0]

    if spaceOdds2Weights < 101:
        spaceOdds2Max = max(zip(spaceOdds2, spaceOdds2), key=lambda tuple: tuple[1])[0]

    if shopOdds34Weights < 101:
        shopOdds34Max = max(zip(shopOdds34, shopOdds34), key=lambda tuple: tuple[1])[0]

    if shopOdds12Max == 'mushroomCapsuleShopOdds12':
        mushroomCapsuleShopOdds12 += (100 - mushroomCapsuleShopOdds12)

    if shopOdds12Max == 'goldenMushroomCapsuleShopOdds12':
        goldenMushroomCapsuleShopOdds12 += (100 - goldenMushroomCapsuleShopOdds12)

    if shopOdds12Max == 'metalMushroomCapsuleShopOdds12':
        metalMushroomCapsuleShopOdds12 += (100 - metalMushroomCapsuleShopOdds12)

    if shopOdds12Max == 'slowMushroomCapsuleShopOdds12':
        slowMushroomCapsuleShopOdds12 += (100 - slowMushroomCapsuleShopOdds12)

    if shopOdds12Max == 'flutterCapsuleShopOdds12':
        flutterCapsuleShopOdds12 += (100 - flutterCapsuleShopOdds12)

    if shopOdds12Max == 'cannonCapsuleShopOdds12':
        cannonCapsuleShopOdds12 += (100 - cannonCapsuleShopOdds12)

    if shopOdds12Max == 'snackCapsuleShopOdds12':
        snackCapsuleShopOdds12 += (100 - snackCapsuleShopOdds12)

    if shopOdds12Max == 'lakituCapsuleShopOdds12':
        lakituCapsuleShopOdds12 += (100 - lakituCapsuleShopOdds12)

    if shopOdds12Max == 'hammerBroCapsuleShopOdds12':
        hammerBroCapsuleShopOdds12 += (100 - hammerBroCapsuleShopOdds12)

    if shopOdds12Max == 'piranhaPlantCapsuleShopOdds12':
        piranhaPlantCapsuleShopOdds12 += (100 - piranhaPlantCapsuleShopOdds12)

    if shopOdds12Max == 'spearGuyCapsuleShopOdds12':
        spearGuyCapsuleShopOdds12 += (100 - spearGuyCapsuleShopOdds12)

    if shopOdds12Max == 'kamekCapsuleShopOdds12':
        kamekCapsuleShopOdds12 += (100 - kamekCapsuleShopOdds12)

    if shopOdds12Max == 'toadyCapsuleShopOdds12':
        toadyCapsuleShopOdds12 += (100 - toadyCapsuleShopOdds12)

    if shopOdds12Max == 'mrBlizzardCapsuleShopOdds12':
        mrBlizzardCapsuleShopOdds12 += (100 - mrBlizzardCapsuleShopOdds12)

    if shopOdds12Max == 'banditCapsuleShopOdds12':
        banditCapsuleShopOdds12 += (100 - banditCapsuleShopOdds12)

    if shopOdds12Max == 'pinkBooCapsuleShopOdds12':
        pinkBooCapsuleShopOdds12 += (100 - pinkBooCapsuleShopOdds12)

    if shopOdds12Max == 'spinyCapsuleShopOdds12':
        spinyCapsuleShopOdds12 += (100 - spinyCapsuleShopOdds12)

    if shopOdds12Max == 'zapCapsuleShopOdds12':
        zapCapsuleShopOdds12 += (100 - zapCapsuleShopOdds12)

    if shopOdds12Max == 'tweesterCapsuleShopOdds12':
        tweesterCapsuleShopOdds12 += (100 - tweesterCapsuleShopOdds12)

    if shopOdds12Max == 'thwompCapsuleShopOdds12':
        thwompCapsuleShopOdds12 += (100 - thwompCapsuleShopOdds12)

    if shopOdds12Max == 'warpCapsuleShopOdds12':
        warpCapsuleShopOdds12 += (100 - warpCapsuleShopOdds12)

    if shopOdds12Max == 'bombCapsuleShopOdds12':
        bombCapsuleShopOdds12 += (100 - bombCapsuleShopOdds12)

    if shopOdds12Max == 'fireballCapsuleShopOdds12':
        fireballCapsuleShopOdds12 += (100 - fireballCapsuleShopOdds12)

    if shopOdds12Max == 'flowerCapsuleShopOdds12':
        flowerCapsuleShopOdds12 += (100 - flowerCapsuleShopOdds12)

    if shopOdds12Max == 'eggCapsuleShopOdds12':
        eggCapsuleShopOdds12 += (100 - eggCapsuleShopOdds12)

    if shopOdds12Max == 'vacuumCapsuleShopOdds12':
        vacuumCapsuleShopOdds12 += (100 - vacuumCapsuleShopOdds12)

    if shopOdds12Max == 'magicCapsuleShopOdds12':
        magicCapsuleShopOdds12 += (100 - magicCapsuleShopOdds12)

    if shopOdds12Max == 'tripleCapsuleShopOdds12':
        tripleCapsuleShopOdds12 += (100 - tripleCapsuleShopOdds12)

    if shopOdds12Max == 'koopaCapsuleShopOdds12':
        koopaCapsuleShopOdds12 += (100 - koopaCapsuleShopOdds12)

    if shopOdds12Max == 'mysteryCapsuleShopOdds12':
        mysteryCapsuleShopOdds12 += (100 - mysteryCapsuleShopOdds12)

    if shopOdds12Max == 'duelCapsuleShopOdds12':
        duelCapsuleShopOdds12 += (100 - duelCapsuleShopOdds12)

    if shopOdds12Max == 'dkCapsuleShopOdds12':
        dkCapsuleShopOdds12 += (100 - dkCapsuleShopOdds12)

    if shopOdds12Max == 'orbBagCapsuleShopOdds12':
        orbBagCapsuleShopOdds12 += (100 - orbBagCapsuleShopOdds12)

    if shopOdds34Max == 'mushroomCapsuleShopOdds34':
        mushroomCapsuleShopOdds34 += (100 - mushroomCapsuleShopOdds34)

    if shopOdds34Max == 'goldenMushroomCapsuleShopOdds34':
        goldenMushroomCapsuleShopOdds34 += (100 - goldenMushroomCapsuleShopOdds34)

    if shopOdds34Max == 'metalMushroomCapsuleShopOdds34':
        metalMushroomCapsuleShopOdds34 += (100 - metalMushroomCapsuleShopOdds34)

    if shopOdds34Max == 'slowMushroomCapsuleShopOdds34':
        slowMushroomCapsuleShopOdds34 += (100 - slowMushroomCapsuleShopOdds34)

    if shopOdds34Max == 'flutterCapsuleShopOdds34':
        flutterCapsuleShopOdds34 += (100 - flutterCapsuleShopOdds34)

    if shopOdds34Max == 'cannonCapsuleShopOdds34':
        cannonCapsuleShopOdds34 += (100 - cannonCapsuleShopOdds34)

    if shopOdds34Max == 'snackCapsuleShopOdds34':
        snackCapsuleShopOdds34 += (100 - snackCapsuleShopOdds34)

    if shopOdds34Max == 'lakituCapsuleShopOdds34':
        lakituCapsuleShopOdds34 += (100 - lakituCapsuleShopOdds34)

    if shopOdds34Max == 'hammerBroCapsuleShopOdds34':
        hammerBroCapsuleShopOdds34 += (100 - hammerBroCapsuleShopOdds34)

    if shopOdds34Max == 'piranhaPlantCapsuleShopOdds34':
        piranhaPlantCapsuleShopOdds34 += (100 - piranhaPlantCapsuleShopOdds34)

    if shopOdds34Max == 'spearGuyCapsuleShopOdds34':
        spearGuyCapsuleShopOdds34 += (100 - spearGuyCapsuleShopOdds34)

    if shopOdds34Max == 'kamekCapsuleShopOdds34':
        kamekCapsuleShopOdds34 += (100 - kamekCapsuleShopOdds34)

    if shopOdds34Max == 'toadyCapsuleShopOdds34':
        toadyCapsuleShopOdds34 += (100 - toadyCapsuleShopOdds34)

    if shopOdds34Max == 'mrBlizzardCapsuleShopOdds34':
        mrBlizzardCapsuleShopOdds34 += (100 - mrBlizzardCapsuleShopOdds34)

    if shopOdds34Max == 'banditCapsuleShopOdds34':
        banditCapsuleShopOdds34 += (100 - banditCapsuleShopOdds34)

    if shopOdds34Max == 'pinkBooCapsuleShopOdds34':
        pinkBooCapsuleShopOdds34 += (100 - pinkBooCapsuleShopOdds34)

    if shopOdds34Max == 'spinyCapsuleShopOdds34':
        spinyCapsuleShopOdds34 += (100 - spinyCapsuleShopOdds34)

    if shopOdds34Max == 'zapCapsuleShopOdds34':
        zapCapsuleShopOdds34 += (100 - zapCapsuleShopOdds34)

    if shopOdds34Max == 'tweesterCapsuleShopOdds34':
        tweesterCapsuleShopOdds34 += (100 - tweesterCapsuleShopOdds34)

    if shopOdds34Max == 'thwompCapsuleShopOdds34':
        thwompCapsuleShopOdds34 += (100 - thwompCapsuleShopOdds34)

    if shopOdds34Max == 'warpCapsuleShopOdds34':
        warpCapsuleShopOdds34 += (100 - warpCapsuleShopOdds34)

    if shopOdds34Max == 'bombCapsuleShopOdds34':
        bombCapsuleShopOdds34 += (100 - bombCapsuleShopOdds34)

    if shopOdds34Max == 'fireballCapsuleShopOdds34':
        fireballCapsuleShopOdds34 += (100 - fireballCapsuleShopOdds34)

    if shopOdds34Max == 'flowerCapsuleShopOdds34':
        flowerCapsuleShopOdds34 += (100 - flowerCapsuleShopOdds34)

    if shopOdds34Max == 'eggCapsuleShopOdds34':
        eggCapsuleShopOdds34 += (100 - eggCapsuleShopOdds34)

    if shopOdds34Max == 'vacuumCapsuleShopOdds34':
        vacuumCapsuleShopOdds34 += (100 - vacuumCapsuleShopOdds34)

    if shopOdds34Max == 'magicCapsuleShopOdds34':
        magicCapsuleShopOdds34 += (100 - magicCapsuleShopOdds34)

    if shopOdds34Max == 'tripleCapsuleShopOdds34':
        tripleCapsuleShopOdds34 += (100 - tripleCapsuleShopOdds34)

    if shopOdds34Max == 'koopaCapsuleShopOdds34':
        koopaCapsuleShopOdds34 += (100 - koopaCapsuleShopOdds34)

    if shopOdds34Max == 'mysteryCapsuleShopOdds34':
        mysteryCapsuleShopOdds34 += (100 - mysteryCapsuleShopOdds34)

    if shopOdds34Max == 'duelCapsuleShopOdds34':
        duelCapsuleShopOdds34 += (100 - duelCapsuleShopOdds34)

    if shopOdds34Max == 'dkCapsuleShopOdds34':
        dkCapsuleShopOdds34 += (100 - dkCapsuleShopOdds34)

    if shopOdds34Max == 'orbBagCapsuleShopOdds34':
        orbBagCapsuleShopOdds34 += (100 - orbBagCapsuleShopOdds34)

    if spaceOdds1Max == 'mushroomCapsuleSpaceOdds1':
        mushroomCapsuleSpaceOdds1 += (100 - mushroomCapsuleSpaceOdds1)

    if spaceOdds1Max == 'goldenMushroomCapsuleSpaceOdds1':
        goldenMushroomCapsuleSpaceOdds1 += (100 - goldenMushroomCapsuleSpaceOdds1)

    if spaceOdds1Max == 'metalMushroomCapsuleSpaceOdds1':
        metalMushroomCapsuleSpaceOdds1 += (100 - metalMushroomCapsuleSpaceOdds1)

    if spaceOdds1Max == 'slowMushroomCapsuleSpaceOdds1':
        slowMushroomCapsuleSpaceOdds1 += (100 - slowMushroomCapsuleSpaceOdds1)

    if spaceOdds1Max == 'flutterCapsuleSpaceOdds1':
        flutterCapsuleSpaceOdds1 += (100 - flutterCapsuleSpaceOdds1)

    if spaceOdds1Max == 'cannonCapsuleSpaceOdds1':
        cannonCapsuleSpaceOdds1 += (100 - cannonCapsuleSpaceOdds1)

    if spaceOdds1Max == 'snackCapsuleSpaceOdds1':
        snackCapsuleSpaceOdds1 += (100 - snackCapsuleSpaceOdds1)

    if spaceOdds1Max == 'lakituCapsuleSpaceOdds1':
        lakituCapsuleSpaceOdds1 += (100 - lakituCapsuleSpaceOdds1)

    if spaceOdds1Max == 'hammerBroCapsuleSpaceOdds1':
        hammerBroCapsuleSpaceOdds1 += (100 - hammerBroCapsuleSpaceOdds1)

    if spaceOdds1Max == 'piranhaPlantCapsuleSpaceOdds1':
        piranhaPlantCapsuleSpaceOdds1 += (100 - piranhaPlantCapsuleSpaceOdds1)

    if spaceOdds1Max == 'spearGuyCapsuleSpaceOdds1':
        spearGuyCapsuleSpaceOdds1 += (100 - spearGuyCapsuleSpaceOdds1)

    if spaceOdds1Max == 'kamekCapsuleSpaceOdds1':
        kamekCapsuleSpaceOdds1 += (100 - kamekCapsuleSpaceOdds1)

    if spaceOdds1Max == 'toadyCapsuleSpaceOdds1':
        toadyCapsuleSpaceOdds1 += (100 - toadyCapsuleSpaceOdds1)

    if spaceOdds1Max == 'mrBlizzardCapsuleSpaceOdds1':
        mrBlizzardCapsuleSpaceOdds1 += (100 - mrBlizzardCapsuleSpaceOdds1)

    if spaceOdds1Max == 'banditCapsuleSpaceOdds1':
        banditCapsuleSpaceOdds1 += (100 - banditCapsuleSpaceOdds1)

    if spaceOdds1Max == 'pinkBooCapsuleSpaceOdds1':
        pinkBooCapsuleSpaceOdds1 += (100 - pinkBooCapsuleSpaceOdds1)

    if spaceOdds1Max == 'spinyCapsuleSpaceOdds1':
        spinyCapsuleSpaceOdds1 += (100 - spinyCapsuleSpaceOdds1)

    if spaceOdds1Max == 'zapCapsuleSpaceOdds1':
        zapCapsuleSpaceOdds1 += (100 - zapCapsuleSpaceOdds1)

    if spaceOdds1Max == 'tweesterCapsuleSpaceOdds1':
        tweesterCapsuleSpaceOdds1 += (100 - tweesterCapsuleSpaceOdds1)

    if spaceOdds1Max == 'thwompCapsuleSpaceOdds1':
        thwompCapsuleSpaceOdds1 += (100 - thwompCapsuleSpaceOdds1)

    if spaceOdds1Max == 'warpCapsuleSpaceOdds1':
        warpCapsuleSpaceOdds1 += (100 - warpCapsuleSpaceOdds1)

    if spaceOdds1Max == 'bombCapsuleSpaceOdds1':
        bombCapsuleSpaceOdds1 += (100 - bombCapsuleSpaceOdds1)

    if spaceOdds1Max == 'fireballCapsuleSpaceOdds1':
        fireballCapsuleSpaceOdds1 += (100 - fireballCapsuleSpaceOdds1)

    if spaceOdds1Max == 'flowerCapsuleSpaceOdds1':
        flowerCapsuleSpaceOdds1 += (100 - flowerCapsuleSpaceOdds1)

    if spaceOdds1Max == 'eggCapsuleSpaceOdds1':
        eggCapsuleSpaceOdds1 += (100 - eggCapsuleSpaceOdds1)

    if spaceOdds1Max == 'vacuumCapsuleSpaceOdds1':
        vacuumCapsuleSpaceOdds1 += (100 - vacuumCapsuleSpaceOdds1)

    if spaceOdds1Max == 'magicCapsuleSpaceOdds1':
        magicCapsuleSpaceOdds1 += (100 - magicCapsuleSpaceOdds1)

    if spaceOdds1Max == 'tripleCapsuleSpaceOdds1':
        tripleCapsuleSpaceOdds1 += (100 - tripleCapsuleSpaceOdds1)

    if spaceOdds1Max == 'koopaCapsuleSpaceOdds1':
        koopaCapsuleSpaceOdds1 += (100 - koopaCapsuleSpaceOdds1)

    if spaceOdds1Max == 'mysteryCapsuleSpaceOdds1':
        mysteryCapsuleSpaceOdds1 += (100 - mysteryCapsuleSpaceOdds1)

    if spaceOdds1Max == 'duelCapsuleSpaceOdds1':
        duelCapsuleSpaceOdds1 += (100 - duelCapsuleSpaceOdds1)

    if spaceOdds1Max == 'dkCapsuleSpaceOdds1':
        dkCapsuleSpaceOdds1 += (100 - dkCapsuleSpaceOdds1)

    if spaceOdds1Max == 'orbBagCapsuleSpaceOdds1':
        orbBagCapsuleSpaceOdds1 += (100 - orbBagCapsuleSpaceOdds1)

    if spaceOdds2Max == 'mushroomCapsuleSpaceOdds2':
        mushroomCapsuleSpaceOdds2 += (100 - mushroomCapsuleSpaceOdds2)

    if spaceOdds2Max == 'goldenMushroomCapsuleSpaceOdds2':
        goldenMushroomCapsuleSpaceOdds2 += (100 - goldenMushroomCapsuleSpaceOdds2)

    if spaceOdds2Max == 'metalMushroomCapsuleSpaceOdds2':
        metalMushroomCapsuleSpaceOdds2 += (100 - metalMushroomCapsuleSpaceOdds2)

    if spaceOdds2Max == 'slowMushroomCapsuleSpaceOdds2':
        slowMushroomCapsuleSpaceOdds2 += (100 - slowMushroomCapsuleSpaceOdds2)

    if spaceOdds2Max == 'flutterCapsuleSpaceOdds2':
        flutterCapsuleSpaceOdds2 += (100 - flutterCapsuleSpaceOdds2)

    if spaceOdds2Max == 'cannonCapsuleSpaceOdds2':
        cannonCapsuleSpaceOdds2 += (100 - cannonCapsuleSpaceOdds2)

    if spaceOdds2Max == 'snackCapsuleSpaceOdds2':
        snackCapsuleSpaceOdds2 += (100 - snackCapsuleSpaceOdds2)

    if spaceOdds2Max == 'lakituCapsuleSpaceOdds2':
        lakituCapsuleSpaceOdds2 += (100 - lakituCapsuleSpaceOdds2)

    if spaceOdds2Max == 'hammerBroCapsuleSpaceOdds2':
        hammerBroCapsuleSpaceOdds2 += (100 - hammerBroCapsuleSpaceOdds2)

    if spaceOdds2Max == 'piranhaPlantCapsuleSpaceOdds2':
        piranhaPlantCapsuleSpaceOdds2 += (100 - piranhaPlantCapsuleSpaceOdds2)

    if spaceOdds2Max == 'spearGuyCapsuleSpaceOdds2':
        spearGuyCapsuleSpaceOdds2 += (100 - spearGuyCapsuleSpaceOdds2)

    if spaceOdds2Max == 'kamekCapsuleSpaceOdds2':
        kamekCapsuleSpaceOdds2 += (100 - kamekCapsuleSpaceOdds2)

    if spaceOdds2Max == 'toadyCapsuleSpaceOdds2':
        toadyCapsuleSpaceOdds2 += (100 - toadyCapsuleSpaceOdds2)

    if spaceOdds2Max == 'mrBlizzardCapsuleSpaceOdds2':
        mrBlizzardCapsuleSpaceOdds2 += (100 - mrBlizzardCapsuleSpaceOdds2)

    if spaceOdds2Max == 'banditCapsuleSpaceOdds2':
        banditCapsuleSpaceOdds2 += (100 - banditCapsuleSpaceOdds2)

    if spaceOdds2Max == 'pinkBooCapsuleSpaceOdds2':
        pinkBooCapsuleSpaceOdds2 += (100 - pinkBooCapsuleSpaceOdds2)

    if spaceOdds2Max == 'spinyCapsuleSpaceOdds2':
        spinyCapsuleSpaceOdds2 += (100 - spinyCapsuleSpaceOdds2)

    if spaceOdds2Max == 'zapCapsuleSpaceOdds2':
        zapCapsuleSpaceOdds2 += (100 - zapCapsuleSpaceOdds2)

    if spaceOdds2Max == 'tweesterCapsuleSpaceOdds2':
        tweesterCapsuleSpaceOdds2 += (100 - tweesterCapsuleSpaceOdds2)

    if spaceOdds2Max == 'thwompCapsuleSpaceOdds2':
        thwompCapsuleSpaceOdds2 += (100 - thwompCapsuleSpaceOdds2)

    if spaceOdds2Max == 'warpCapsuleSpaceOdds2':
        warpCapsuleSpaceOdds2 += (100 - warpCapsuleSpaceOdds2)

    if spaceOdds2Max == 'bombCapsuleSpaceOdds2':
        bombCapsuleSpaceOdds2 += (100 - bombCapsuleSpaceOdds2)

    if spaceOdds2Max == 'fireballCapsuleSpaceOdds2':
        fireballCapsuleSpaceOdds2 += (100 - fireballCapsuleSpaceOdds2)

    if spaceOdds2Max == 'flowerCapsuleSpaceOdds2':
        flowerCapsuleSpaceOdds2 += (100 - flowerCapsuleSpaceOdds2)

    if spaceOdds2Max == 'eggCapsuleSpaceOdds2':
        eggCapsuleSpaceOdds2 += (100 - eggCapsuleSpaceOdds2)

    if spaceOdds2Max == 'vacuumCapsuleSpaceOdds2':
        vacuumCapsuleSpaceOdds2 += (100 - vacuumCapsuleSpaceOdds2)

    if spaceOdds2Max == 'magicCapsuleSpaceOdds2':
        magicCapsuleSpaceOdds2 += (100 - magicCapsuleSpaceOdds2)

    if spaceOdds2Max == 'tripleCapsuleSpaceOdds2':
        tripleCapsuleSpaceOdds2 += (100 - tripleCapsuleSpaceOdds2)

    if spaceOdds2Max == 'koopaCapsuleSpaceOdds2':
        koopaCapsuleSpaceOdds2 += (100 - koopaCapsuleSpaceOdds2)

    if spaceOdds2Max == 'mysteryCapsuleSpaceOdds2':
        mysteryCapsuleSpaceOdds2 += (100 - mysteryCapsuleSpaceOdds2)

    if spaceOdds2Max == 'duelCapsuleSpaceOdds2':
        duelCapsuleSpaceOdds2 += (100 - duelCapsuleSpaceOdds2)

    if spaceOdds2Max == 'dkCapsuleSpaceOdds2':
        dkCapsuleSpaceOdds2 += (100 - dkCapsuleSpaceOdds2)

    if spaceOdds2Max == 'orbBagCapsuleSpaceOdds2':
        orbBagCapsuleSpaceOdds2 += (100 - orbBagCapsuleSpaceOdds2)

    if spaceOdds34Max == 'mushroomCapsuleSpaceOdds34':
        mushroomCapsuleSpaceOdds34 += (100 - mushroomCapsuleSpaceOdds34)

    if spaceOdds34Max == 'goldenMushroomCapsuleSpaceOdds34':
        goldenMushroomCapsuleSpaceOdds34 += (100 - goldenMushroomCapsuleSpaceOdds34)

    if spaceOdds34Max == 'metalMushroomCapsuleSpaceOdds34':
        metalMushroomCapsuleSpaceOdds34 += (100 - metalMushroomCapsuleSpaceOdds34)

    if spaceOdds34Max == 'slowMushroomCapsuleSpaceOdds34':
        slowMushroomCapsuleSpaceOdds34 += (100 - slowMushroomCapsuleSpaceOdds34)

    if spaceOdds34Max == 'flutterCapsuleSpaceOdds34':
        flutterCapsuleSpaceOdds34 += (100 - flutterCapsuleSpaceOdds34)

    if spaceOdds34Max == 'cannonCapsuleSpaceOdds34':
        cannonCapsuleSpaceOdds34 += (100 - cannonCapsuleSpaceOdds34)

    if spaceOdds34Max == 'snackCapsuleSpaceOdds34':
        snackCapsuleSpaceOdds34 += (100 - snackCapsuleSpaceOdds34)

    if spaceOdds34Max == 'lakituCapsuleSpaceOdds34':
        lakituCapsuleSpaceOdds34 += (100 - lakituCapsuleSpaceOdds34)

    if spaceOdds34Max == 'hammerBroCapsuleSpaceOdds34':
        hammerBroCapsuleSpaceOdds34 += (100 - hammerBroCapsuleSpaceOdds34)

    if spaceOdds34Max == 'piranhaPlantCapsuleSpaceOdds34':
        piranhaPlantCapsuleSpaceOdds34 += (100 - piranhaPlantCapsuleSpaceOdds34)

    if spaceOdds34Max == 'spearGuyCapsuleSpaceOdds34':
        spearGuyCapsuleSpaceOdds34 += (100 - spearGuyCapsuleSpaceOdds34)

    if spaceOdds34Max == 'kamekCapsuleSpaceOdds34':
        kamekCapsuleSpaceOdds34 += (100 - kamekCapsuleSpaceOdds34)

    if spaceOdds34Max == 'toadyCapsuleSpaceOdds34':
        toadyCapsuleSpaceOdds34 += (100 - toadyCapsuleSpaceOdds34)

    if spaceOdds34Max == 'mrBlizzardCapsuleSpaceOdds34':
        mrBlizzardCapsuleSpaceOdds34 += (100 - mrBlizzardCapsuleSpaceOdds34)

    if spaceOdds34Max == 'banditCapsuleSpaceOdds34':
        banditCapsuleSpaceOdds34 += (100 - banditCapsuleSpaceOdds34)

    if spaceOdds34Max == 'pinkBooCapsuleSpaceOdds34':
        pinkBooCapsuleSpaceOdds34 += (100 - pinkBooCapsuleSpaceOdds34)

    if spaceOdds34Max == 'spinyCapsuleSpaceOdds34':
        spinyCapsuleSpaceOdds34 += (100 - spinyCapsuleSpaceOdds34)

    if spaceOdds34Max == 'zapCapsuleSpaceOdds34':
        zapCapsuleSpaceOdds34 += (100 - zapCapsuleSpaceOdds34)

    if spaceOdds34Max == 'tweesterCapsuleSpaceOdds34':
        tweesterCapsuleSpaceOdds34 += (100 - tweesterCapsuleSpaceOdds34)

    if spaceOdds34Max == 'thwompCapsuleSpaceOdds34':
        thwompCapsuleSpaceOdds34 += (100 - thwompCapsuleSpaceOdds34)

    if spaceOdds34Max == 'warpCapsuleSpaceOdds34':
        warpCapsuleSpaceOdds34 += (100 - warpCapsuleSpaceOdds34)

    if spaceOdds34Max == 'bombCapsuleSpaceOdds34':
        bombCapsuleSpaceOdds34 += (100 - bombCapsuleSpaceOdds34)

    if spaceOdds34Max == 'fireballCapsuleSpaceOdds34':
        fireballCapsuleSpaceOdds34 += (100 - fireballCapsuleSpaceOdds34)

    if spaceOdds34Max == 'flowerCapsuleSpaceOdds34':
        flowerCapsuleSpaceOdds34 += (100 - flowerCapsuleSpaceOdds34)

    if spaceOdds34Max == 'eggCapsuleSpaceOdds34':
        eggCapsuleSpaceOdds34 += (100 - eggCapsuleSpaceOdds34)

    if spaceOdds34Max == 'vacuumCapsuleSpaceOdds34':
        vacuumCapsuleSpaceOdds34 += (100 - vacuumCapsuleSpaceOdds34)

    if spaceOdds34Max == 'magicCapsuleSpaceOdds34':
        magicCapsuleSpaceOdds34 += (100 - magicCapsuleSpaceOdds34)

    if spaceOdds34Max == 'tripleCapsuleSpaceOdds34':
        tripleCapsuleSpaceOdds34 += (100 - tripleCapsuleSpaceOdds34)

    if spaceOdds34Max == 'koopaCapsuleSpaceOdds34':
        koopaCapsuleSpaceOdds34 += (100 - koopaCapsuleSpaceOdds34)

    if spaceOdds34Max == 'mysteryCapsuleSpaceOdds34':
        mysteryCapsuleSpaceOdds34 += (100 - mysteryCapsuleSpaceOdds34)

    if spaceOdds34Max == 'duelCapsuleSpaceOdds34':
        duelCapsuleSpaceOdds34 += (100 - duelCapsuleSpaceOdds34)

    if spaceOdds34Max == 'dkCapsuleSpaceOdds34':
        dkCapsuleSpaceOdds34 += (100 - dkCapsuleSpaceOdds34)

    if spaceOdds34Max == 'orbBagCapsuleSpaceOdds34':
        orbBagCapsuleSpaceOdds34 += (100 - orbBagCapsuleSpaceOdds34)

    mushroomCapsuleShopOdds12 = str(mushroomCapsuleShopOdds12)
    mushroomCapsuleShopOdds34 = str(mushroomCapsuleShopOdds34)
    mushroomCapsuleSpaceOdds1 = str(mushroomCapsuleSpaceOdds1)
    mushroomCapsuleSpaceOdds2 = str(mushroomCapsuleSpaceOdds2)
    mushroomCapsuleSpaceOdds34 = str(mushroomCapsuleSpaceOdds34)

    goldenMushroomCapsuleShopOdds12 = str(goldenMushroomCapsuleShopOdds12)
    goldenMushroomCapsuleShopOdds34 = str(goldenMushroomCapsuleShopOdds34)
    goldenMushroomCapsuleSpaceOdds1 = str(goldenMushroomCapsuleSpaceOdds1)
    goldenMushroomCapsuleSpaceOdds2 = str(goldenMushroomCapsuleSpaceOdds2)
    goldenMushroomCapsuleSpaceOdds34 = str(goldenMushroomCapsuleSpaceOdds34)

    slowMushroomCapsuleShopOdds12 = str(slowMushroomCapsuleShopOdds12)
    slowMushroomCapsuleShopOdds34 = str(slowMushroomCapsuleShopOdds34)
    slowMushroomCapsuleSpaceOdds1 = str(slowMushroomCapsuleSpaceOdds1)
    slowMushroomCapsuleSpaceOdds2 = str(slowMushroomCapsuleSpaceOdds2)
    slowMushroomCapsuleSpaceOdds34 = str(slowMushroomCapsuleSpaceOdds34)

    metalMushroomCapsuleShopOdds12 = str(metalMushroomCapsuleShopOdds12)
    metalMushroomCapsuleShopOdds34 = str(metalMushroomCapsuleShopOdds34)
    metalMushroomCapsuleSpaceOdds1 = str(metalMushroomCapsuleSpaceOdds1)
    metalMushroomCapsuleSpaceOdds2 = str(metalMushroomCapsuleSpaceOdds2)
    metalMushroomCapsuleSpaceOdds34 = str(metalMushroomCapsuleSpaceOdds34)

    flutterCapsuleShopOdds12 = str(flutterCapsuleShopOdds12)
    flutterCapsuleShopOdds34 = str(flutterCapsuleShopOdds34)
    flutterCapsuleSpaceOdds1 = str(flutterCapsuleSpaceOdds1)
    flutterCapsuleSpaceOdds2 = str(flutterCapsuleSpaceOdds2)
    flutterCapsuleSpaceOdds34 = str(flutterCapsuleSpaceOdds34)

    cannonCapsuleShopOdds12 = str(cannonCapsuleShopOdds12)
    cannonCapsuleShopOdds34 = str(cannonCapsuleShopOdds34)
    cannonCapsuleSpaceOdds1 = str(cannonCapsuleSpaceOdds1)
    cannonCapsuleSpaceOdds2 = str(cannonCapsuleSpaceOdds2)
    cannonCapsuleSpaceOdds34 = str(cannonCapsuleSpaceOdds34)

    snackCapsuleShopOdds12 = str(snackCapsuleShopOdds12)
    snackCapsuleShopOdds34 = str(snackCapsuleShopOdds34)
    snackCapsuleSpaceOdds1 = str(snackCapsuleSpaceOdds1)
    snackCapsuleSpaceOdds2 = str(snackCapsuleSpaceOdds2)
    snackCapsuleSpaceOdds34 = str(snackCapsuleSpaceOdds34)

    lakituCapsuleShopOdds12 = str(lakituCapsuleShopOdds12)
    lakituCapsuleShopOdds34 = str(lakituCapsuleShopOdds34)
    lakituCapsuleSpaceOdds1 = str(lakituCapsuleSpaceOdds1)
    lakituCapsuleSpaceOdds2 = str(lakituCapsuleSpaceOdds2)
    lakituCapsuleSpaceOdds34 = str(lakituCapsuleSpaceOdds34)

    hammerBroCapsuleShopOdds12 = str(hammerBroCapsuleShopOdds12)
    hammerBroCapsuleShopOdds34 = str(hammerBroCapsuleShopOdds34)
    hammerBroCapsuleSpaceOdds1 = str(hammerBroCapsuleSpaceOdds1)
    hammerBroCapsuleSpaceOdds2 = str(hammerBroCapsuleSpaceOdds2)
    hammerBroCapsuleSpaceOdds34 = str(hammerBroCapsuleSpaceOdds34)

    piranhaPlantCapsuleShopOdds12 = str(piranhaPlantCapsuleShopOdds12)
    piranhaPlantCapsuleShopOdds34 = str(piranhaPlantCapsuleShopOdds34)
    piranhaPlantCapsuleSpaceOdds1 = str(piranhaPlantCapsuleSpaceOdds1)
    piranhaPlantCapsuleSpaceOdds2 = str(piranhaPlantCapsuleSpaceOdds2)
    piranhaPlantCapsuleSpaceOdds34 = str(piranhaPlantCapsuleSpaceOdds34)

    spearGuyCapsuleShopOdds12 = str(spearGuyCapsuleShopOdds12)
    spearGuyCapsuleShopOdds34 = str(spearGuyCapsuleShopOdds34)
    spearGuyCapsuleSpaceOdds1 = str(spearGuyCapsuleSpaceOdds1)
    spearGuyCapsuleSpaceOdds2 = str(spearGuyCapsuleSpaceOdds2)
    spearGuyCapsuleSpaceOdds34 = str(spearGuyCapsuleSpaceOdds34)

    kamekCapsuleShopOdds12 = str(kamekCapsuleShopOdds12)
    kamekCapsuleShopOdds34 = str(kamekCapsuleShopOdds34)
    kamekCapsuleSpaceOdds1 = str(kamekCapsuleSpaceOdds1)
    kamekCapsuleSpaceOdds2 = str(kamekCapsuleSpaceOdds2)
    kamekCapsuleSpaceOdds34 = str(kamekCapsuleSpaceOdds34)

    toadyCapsuleShopOdds12 = str(toadyCapsuleShopOdds12)
    toadyCapsuleShopOdds34 = str(toadyCapsuleShopOdds34)
    toadyCapsuleSpaceOdds1 = str(toadyCapsuleSpaceOdds1)
    toadyCapsuleSpaceOdds2 = str(toadyCapsuleSpaceOdds2)
    toadyCapsuleSpaceOdds34 = str(toadyCapsuleSpaceOdds34)

    mrBlizzardCapsuleShopOdds12 = str(mrBlizzardCapsuleShopOdds12)
    mrBlizzardCapsuleShopOdds34 = str(mrBlizzardCapsuleShopOdds34)
    mrBlizzardCapsuleSpaceOdds1 = str(mrBlizzardCapsuleSpaceOdds1)
    mrBlizzardCapsuleSpaceOdds2 = str(mrBlizzardCapsuleSpaceOdds2)
    mrBlizzardCapsuleSpaceOdds34 = str(mrBlizzardCapsuleSpaceOdds34)

    banditCapsuleShopOdds12 = str(banditCapsuleShopOdds12)
    banditCapsuleShopOdds34 = str(banditCapsuleShopOdds34)
    banditCapsuleSpaceOdds1 = str(banditCapsuleSpaceOdds1)
    banditCapsuleSpaceOdds2 = str(banditCapsuleSpaceOdds2)
    banditCapsuleSpaceOdds34 = str(banditCapsuleSpaceOdds34)

    pinkBooCapsuleShopOdds12 = str(pinkBooCapsuleShopOdds12)
    pinkBooCapsuleShopOdds34 = str(pinkBooCapsuleShopOdds34)
    pinkBooCapsuleSpaceOdds1 = str(pinkBooCapsuleSpaceOdds1)
    pinkBooCapsuleSpaceOdds2 = str(pinkBooCapsuleSpaceOdds2)
    pinkBooCapsuleSpaceOdds34 = str(pinkBooCapsuleSpaceOdds34)

    spinyCapsuleShopOdds12 = str(spinyCapsuleShopOdds12)
    spinyCapsuleShopOdds34 = str(spinyCapsuleShopOdds34)
    spinyCapsuleSpaceOdds1 = str(spinyCapsuleSpaceOdds1)
    spinyCapsuleSpaceOdds2 = str(spinyCapsuleSpaceOdds2)
    spinyCapsuleSpaceOdds34 = str(spinyCapsuleSpaceOdds34)

    zapCapsuleShopOdds12 = str(zapCapsuleShopOdds12)
    zapCapsuleShopOdds34 = str(zapCapsuleShopOdds34)
    zapCapsuleSpaceOdds1 = str(zapCapsuleSpaceOdds1)
    zapCapsuleSpaceOdds2 = str(zapCapsuleSpaceOdds2)
    zapCapsuleSpaceOdds34 = str(zapCapsuleSpaceOdds34)

    tweesterCapsuleShopOdds12 = str(tweesterCapsuleShopOdds12)
    tweesterCapsuleShopOdds34 = str(tweesterCapsuleShopOdds34)
    tweesterCapsuleSpaceOdds1 = str(tweesterCapsuleSpaceOdds1)
    tweesterCapsuleSpaceOdds2 = str(tweesterCapsuleSpaceOdds2)
    tweesterCapsuleSpaceOdds34 = str(tweesterCapsuleSpaceOdds34)

    thwompCapsuleShopOdds12 = str(thwompCapsuleShopOdds12)
    thwompCapsuleShopOdds34 = str(thwompCapsuleShopOdds34)
    thwompCapsuleSpaceOdds1 = str(thwompCapsuleSpaceOdds1)
    thwompCapsuleSpaceOdds2 = str(thwompCapsuleSpaceOdds2)
    thwompCapsuleSpaceOdds34 = str(thwompCapsuleSpaceOdds34)

    warpCapsuleShopOdds12 = str(warpCapsuleShopOdds12)
    warpCapsuleShopOdds34 = str(warpCapsuleShopOdds34)
    warpCapsuleSpaceOdds1 = str(warpCapsuleSpaceOdds1)
    warpCapsuleSpaceOdds2 = str(warpCapsuleSpaceOdds2)
    warpCapsuleSpaceOdds34 = str(warpCapsuleSpaceOdds34)

    bombCapsuleShopOdds12 = str(bombCapsuleShopOdds12)
    bombCapsuleShopOdds34 = str(bombCapsuleShopOdds34)
    bombCapsuleSpaceOdds1 = str(bombCapsuleSpaceOdds1)
    bombCapsuleSpaceOdds2 = str(bombCapsuleSpaceOdds2)
    bombCapsuleSpaceOdds34 = str(bombCapsuleSpaceOdds34)

    fireballCapsuleShopOdds12 = str(fireballCapsuleShopOdds12)
    fireballCapsuleShopOdds34 = str(fireballCapsuleShopOdds34)
    fireballCapsuleSpaceOdds1 = str(fireballCapsuleSpaceOdds1)
    fireballCapsuleSpaceOdds2 = str(fireballCapsuleSpaceOdds2)
    fireballCapsuleSpaceOdds34 = str(fireballCapsuleSpaceOdds34)

    flowerCapsuleShopOdds12 = str(flowerCapsuleShopOdds12)
    flowerCapsuleShopOdds34 = str(flowerCapsuleShopOdds34)
    flowerCapsuleSpaceOdds1 = str(flowerCapsuleSpaceOdds1)
    flowerCapsuleSpaceOdds2 = str(flowerCapsuleSpaceOdds2)
    flowerCapsuleSpaceOdds34 = str(flowerCapsuleSpaceOdds34)

    eggCapsuleShopOdds12 = str(eggCapsuleShopOdds12)
    eggCapsuleShopOdds34 = str(eggCapsuleShopOdds34)
    eggCapsuleSpaceOdds1 = str(eggCapsuleSpaceOdds1)
    eggCapsuleSpaceOdds2 = str(eggCapsuleSpaceOdds2)
    eggCapsuleSpaceOdds34 = str(eggCapsuleSpaceOdds34)

    vacuumCapsuleShopOdds12 = str(vacuumCapsuleShopOdds12)
    vacuumCapsuleShopOdds34 = str(vacuumCapsuleShopOdds34)
    vacuumCapsuleSpaceOdds1 = str(vacuumCapsuleSpaceOdds1)
    vacuumCapsuleSpaceOdds2 = str(vacuumCapsuleSpaceOdds2)
    vacuumCapsuleSpaceOdds34 = str(vacuumCapsuleSpaceOdds34)

    magicCapsuleShopOdds12 = str(magicCapsuleShopOdds12)
    magicCapsuleShopOdds34 = str(magicCapsuleShopOdds34)
    magicCapsuleSpaceOdds1 = str(magicCapsuleSpaceOdds1)
    magicCapsuleSpaceOdds2 = str(magicCapsuleSpaceOdds2)
    magicCapsuleSpaceOdds34 = str(magicCapsuleSpaceOdds34)

    tripleCapsuleShopOdds12 = str(tripleCapsuleShopOdds12)
    tripleCapsuleShopOdds34 = str(tripleCapsuleShopOdds34)
    tripleCapsuleSpaceOdds1 = str(tripleCapsuleSpaceOdds1)
    tripleCapsuleSpaceOdds2 = str(tripleCapsuleSpaceOdds2)
    tripleCapsuleSpaceOdds34 = str(tripleCapsuleSpaceOdds34)

    koopaCapsuleShopOdds12 = str(koopaCapsuleShopOdds12)
    koopaCapsuleShopOdds34 = str(koopaCapsuleShopOdds34)
    koopaCapsuleSpaceOdds1 = str(koopaCapsuleSpaceOdds1)
    koopaCapsuleSpaceOdds2 = str(koopaCapsuleSpaceOdds2)
    koopaCapsuleSpaceOdds34 = str(koopaCapsuleSpaceOdds34)

    poisonMushroomShopOdds12 = str(poisonMushroomShopOdds12)
    poisonMushroomShopOdds34 = str(poisonMushroomShopOdds34)
    poisonMushroomSpaceOdds1 = str(poisonMushroomSpaceOdds1)
    poisonMushroomSpaceOdds2 = str(poisonMushroomSpaceOdds2)
    poisonMushroomSpaceOdds34 = str(poisonMushroomSpaceOdds34)

    orbBagCapsuleShopOdds12 = str(orbBagCapsuleShopOdds12)
    orbBagCapsuleShopOdds34 = str(orbBagCapsuleShopOdds34)
    orbBagCapsuleSpaceOdds1 = str(orbBagCapsuleSpaceOdds1)
    orbBagCapsuleSpaceOdds2 = str(orbBagCapsuleSpaceOdds2)
    orbBagCapsuleSpaceOdds34 = str(orbBagCapsuleSpaceOdds34)

    mysteryCapsuleShopOdds12 = str(mysteryCapsuleShopOdds12)
    mysteryCapsuleShopOdds34 = str(mysteryCapsuleShopOdds34)
    mysteryCapsuleSpaceOdds1 = str(mysteryCapsuleSpaceOdds1)
    mysteryCapsuleSpaceOdds2 = str(mysteryCapsuleSpaceOdds2)
    mysteryCapsuleSpaceOdds34 = str(mysteryCapsuleSpaceOdds34)

    dkCapsuleShopOdds12 = str(dkCapsuleShopOdds12)
    dkCapsuleShopOdds34 = str(dkCapsuleShopOdds34)
    dkCapsuleSpaceOdds1 = str(dkCapsuleSpaceOdds1)
    dkCapsuleSpaceOdds2 = str(dkCapsuleSpaceOdds2)
    dkCapsuleSpaceOdds34 = str(dkCapsuleSpaceOdds34)

    duelCapsuleShopOdds12 = str(duelCapsuleShopOdds12)
    duelCapsuleShopOdds34 = str(duelCapsuleShopOdds34)
    duelCapsuleSpaceOdds1 = str(duelCapsuleSpaceOdds1)
    duelCapsuleSpaceOdds2 = str(duelCapsuleSpaceOdds2)
    duelCapsuleSpaceOdds34 = str(duelCapsuleSpaceOdds34)

    def convert_to_hex_weight(weight):
        try:
            weight_hex = hex(int(weight))
            if len(weight_hex) == 4:
                return weight_hex[2:]  # Remove '0x' prefix
            elif len(weight_hex) == 3:
                return "0" + weight_hex[2:]  # Add leading zero
            return weight_hex[2:]  # Return as is for other lengths
        except:
            return "00"  # Return default value on error

    # Usage
    mushroomCapsuleShopOdds12 = convert_to_hex_weight(mushroomCapsuleShopOdds12)
    mushroomCapsuleShopOdds34 = convert_to_hex_weight(mushroomCapsuleShopOdds34)
    mushroomCapsuleSpaceOdds1 = convert_to_hex_weight(mushroomCapsuleSpaceOdds1)
    mushroomCapsuleSpaceOdds2 = convert_to_hex_weight(mushroomCapsuleSpaceOdds2)
    mushroomCapsuleSpaceOdds34 = convert_to_hex_weight(mushroomCapsuleSpaceOdds34)

    goldenMushroomCapsulePrice1 = convert_to_hex_weight(goldenMushroomCapsulePrice1)
    goldenMushroomCapsulePrice2 = convert_to_hex_weight(goldenMushroomCapsulePrice2)
    goldenMushroomCapsulePrice34 = convert_to_hex_weight(goldenMushroomCapsulePrice34)
    goldenMushroomCapsuleShopOdds12 = convert_to_hex_weight(goldenMushroomCapsuleShopOdds12)
    goldenMushroomCapsuleShopOdds34 = convert_to_hex_weight(goldenMushroomCapsuleShopOdds34)
    goldenMushroomCapsuleSpaceOdds1 = convert_to_hex_weight(goldenMushroomCapsuleSpaceOdds1)
    goldenMushroomCapsuleSpaceOdds2 = convert_to_hex_weight(goldenMushroomCapsuleSpaceOdds2)
    goldenMushroomCapsuleSpaceOdds34 = convert_to_hex_weight(goldenMushroomCapsuleSpaceOdds34)

    slowMushroomCapsulePrice1 = convert_to_hex_weight(slowMushroomCapsulePrice1)
    slowMushroomCapsulePrice2 = convert_to_hex_weight(slowMushroomCapsulePrice2)
    slowMushroomCapsulePrice34 = convert_to_hex_weight(slowMushroomCapsulePrice34)
    slowMushroomCapsuleShopOdds12 = convert_to_hex_weight(slowMushroomCapsuleShopOdds12)
    slowMushroomCapsuleShopOdds34 = convert_to_hex_weight(slowMushroomCapsuleShopOdds34)
    slowMushroomCapsuleSpaceOdds1 = convert_to_hex_weight(slowMushroomCapsuleSpaceOdds1)
    slowMushroomCapsuleSpaceOdds2 = convert_to_hex_weight(slowMushroomCapsuleSpaceOdds2)
    slowMushroomCapsuleSpaceOdds34 = convert_to_hex_weight(slowMushroomCapsuleSpaceOdds34)

    metalMushroomCapsulePrice1 = convert_to_hex_weight(metalMushroomCapsulePrice1)
    metalMushroomCapsulePrice2 = convert_to_hex_weight(metalMushroomCapsulePrice2)
    metalMushroomCapsulePrice34 = convert_to_hex_weight(metalMushroomCapsulePrice34)
    metalMushroomCapsuleShopOdds12 = convert_to_hex_weight(metalMushroomCapsuleShopOdds12)
    metalMushroomCapsuleShopOdds34 = convert_to_hex_weight(metalMushroomCapsuleShopOdds34)
    metalMushroomCapsuleSpaceOdds1 = convert_to_hex_weight(metalMushroomCapsuleSpaceOdds1)
    metalMushroomCapsuleSpaceOdds2 = convert_to_hex_weight(metalMushroomCapsuleSpaceOdds2)
    metalMushroomCapsuleSpaceOdds34 = convert_to_hex_weight(metalMushroomCapsuleSpaceOdds34)

    flutterCapsulePrice1 = convert_to_hex_weight(flutterCapsulePrice1)
    flutterCapsulePrice2 = convert_to_hex_weight(flutterCapsulePrice2)
    flutterCapsulePrice34 = convert_to_hex_weight(flutterCapsulePrice34)
    flutterCapsuleShopOdds12 = convert_to_hex_weight(flutterCapsuleShopOdds12)
    flutterCapsuleShopOdds34 = convert_to_hex_weight(flutterCapsuleShopOdds34)
    flutterCapsuleSpaceOdds1 = convert_to_hex_weight(flutterCapsuleSpaceOdds1)
    flutterCapsuleSpaceOdds2 = convert_to_hex_weight(flutterCapsuleSpaceOdds2)
    flutterCapsuleSpaceOdds34 = convert_to_hex_weight(flutterCapsuleSpaceOdds34)

    cannonCapsulePrice1 = convert_to_hex_weight(cannonCapsulePrice1)
    cannonCapsulePrice2 = convert_to_hex_weight(cannonCapsulePrice2)
    cannonCapsulePrice34 = convert_to_hex_weight(cannonCapsulePrice34)
    cannonCapsuleShopOdds12 = convert_to_hex_weight(cannonCapsuleShopOdds12)
    cannonCapsuleShopOdds34 = convert_to_hex_weight(cannonCapsuleShopOdds34)
    cannonCapsuleSpaceOdds1 = convert_to_hex_weight(cannonCapsuleSpaceOdds1)
    cannonCapsuleSpaceOdds2 = convert_to_hex_weight(cannonCapsuleSpaceOdds2)
    cannonCapsuleSpaceOdds34 = convert_to_hex_weight(cannonCapsuleSpaceOdds34)

    snackCapsulePrice1 = convert_to_hex_weight(snackCapsulePrice1)
    snackCapsulePrice2 = convert_to_hex_weight(snackCapsulePrice2)
    snackCapsulePrice34 = convert_to_hex_weight(snackCapsulePrice34)
    snackCapsuleShopOdds12 = convert_to_hex_weight(snackCapsuleShopOdds12)
    snackCapsuleShopOdds34 = convert_to_hex_weight(snackCapsuleShopOdds34)
    snackCapsuleSpaceOdds1 = convert_to_hex_weight(snackCapsuleSpaceOdds1)
    snackCapsuleSpaceOdds2 = convert_to_hex_weight(snackCapsuleSpaceOdds2)
    snackCapsuleSpaceOdds34 = convert_to_hex_weight(snackCapsuleSpaceOdds34)

    lakituCapsulePrice1 = convert_to_hex_weight(lakituCapsulePrice1)
    lakituCapsulePrice2 = convert_to_hex_weight(lakituCapsulePrice2)
    lakituCapsulePrice34 = convert_to_hex_weight(lakituCapsulePrice34)
    lakituCapsuleShopOdds12 = convert_to_hex_weight(lakituCapsuleShopOdds12)
    lakituCapsuleShopOdds34 = convert_to_hex_weight(lakituCapsuleShopOdds34)
    lakituCapsuleSpaceOdds1 = convert_to_hex_weight(lakituCapsuleSpaceOdds1)
    lakituCapsuleSpaceOdds2 = convert_to_hex_weight(lakituCapsuleSpaceOdds2)
    lakituCapsuleSpaceOdds34 = convert_to_hex_weight(lakituCapsuleSpaceOdds34)

    hammerBroCapsulePrice1 = convert_to_hex_weight(hammerBroCapsulePrice1)
    hammerBroCapsulePrice2 = convert_to_hex_weight(hammerBroCapsulePrice2)
    hammerBroCapsulePrice34 = convert_to_hex_weight(hammerBroCapsulePrice34)
    hammerBroCapsuleShopOdds12 = convert_to_hex_weight(hammerBroCapsuleShopOdds12)
    hammerBroCapsuleShopOdds34 = convert_to_hex_weight(hammerBroCapsuleShopOdds34)
    hammerBroCapsuleSpaceOdds1 = convert_to_hex_weight(hammerBroCapsuleSpaceOdds1)
    hammerBroCapsuleSpaceOdds2 = convert_to_hex_weight(hammerBroCapsuleSpaceOdds2)
    hammerBroCapsuleSpaceOdds34 = convert_to_hex_weight(hammerBroCapsuleSpaceOdds34)

    piranhaPlantCapsulePrice1 = convert_to_hex_weight(piranhaPlantCapsulePrice1)
    piranhaPlantCapsulePrice2 = convert_to_hex_weight(piranhaPlantCapsulePrice2)
    piranhaPlantCapsulePrice34 = convert_to_hex_weight(piranhaPlantCapsulePrice34)
    piranhaPlantCapsuleShopOdds12 = convert_to_hex_weight(piranhaPlantCapsuleShopOdds12)
    piranhaPlantCapsuleShopOdds34 = convert_to_hex_weight(piranhaPlantCapsuleShopOdds34)
    piranhaPlantCapsuleSpaceOdds1 = convert_to_hex_weight(piranhaPlantCapsuleSpaceOdds1)
    piranhaPlantCapsuleSpaceOdds2 = convert_to_hex_weight(piranhaPlantCapsuleSpaceOdds2)
    piranhaPlantCapsuleSpaceOdds34 = convert_to_hex_weight(piranhaPlantCapsuleSpaceOdds34)

    spearGuyCapsulePrice1 = convert_to_hex_weight(spearGuyCapsulePrice1)
    spearGuyCapsulePrice2 = convert_to_hex_weight(spearGuyCapsulePrice2)
    spearGuyCapsulePrice34 = convert_to_hex_weight(spearGuyCapsulePrice34)
    spearGuyCapsuleShopOdds12 = convert_to_hex_weight(spearGuyCapsuleShopOdds12)
    spearGuyCapsuleShopOdds34 = convert_to_hex_weight(spearGuyCapsuleShopOdds34)
    spearGuyCapsuleSpaceOdds1 = convert_to_hex_weight(spearGuyCapsuleSpaceOdds1)
    spearGuyCapsuleSpaceOdds2 = convert_to_hex_weight(spearGuyCapsuleSpaceOdds2)
    spearGuyCapsuleSpaceOdds34 = convert_to_hex_weight(spearGuyCapsuleSpaceOdds34)

    kamekCapsulePrice1 = convert_to_hex_weight(kamekCapsulePrice1)
    kamekCapsulePrice2 = convert_to_hex_weight(kamekCapsulePrice2)
    kamekCapsulePrice34 = convert_to_hex_weight(kamekCapsulePrice34)
    kamekCapsuleShopOdds12 = convert_to_hex_weight(kamekCapsuleShopOdds12)
    kamekCapsuleShopOdds34 = convert_to_hex_weight(kamekCapsuleShopOdds34)
    kamekCapsuleSpaceOdds1 = convert_to_hex_weight(kamekCapsuleSpaceOdds1)
    kamekCapsuleSpaceOdds2 = convert_to_hex_weight(kamekCapsuleSpaceOdds2)
    kamekCapsuleSpaceOdds34 = convert_to_hex_weight(kamekCapsuleSpaceOdds34)

    toadyCapsulePrice1 = convert_to_hex_weight(toadyCapsulePrice1)
    toadyCapsulePrice2 = convert_to_hex_weight(toadyCapsulePrice2)
    toadyCapsulePrice34 = convert_to_hex_weight(toadyCapsulePrice34)
    toadyCapsuleShopOdds12 = convert_to_hex_weight(toadyCapsuleShopOdds12)
    toadyCapsuleShopOdds34 = convert_to_hex_weight(toadyCapsuleShopOdds34)
    toadyCapsuleSpaceOdds1 = convert_to_hex_weight(toadyCapsuleSpaceOdds1)
    toadyCapsuleSpaceOdds2 = convert_to_hex_weight(toadyCapsuleSpaceOdds2)
    toadyCapsuleSpaceOdds34 = convert_to_hex_weight(toadyCapsuleSpaceOdds34)

    mrBlizzardCapsulePrice1 = convert_to_hex_weight(mrBlizzardCapsulePrice1)
    mrBlizzardCapsulePrice2 = convert_to_hex_weight(mrBlizzardCapsulePrice2)
    mrBlizzardCapsulePrice34 = convert_to_hex_weight(mrBlizzardCapsulePrice34)
    mrBlizzardCapsuleShopOdds12 = convert_to_hex_weight(mrBlizzardCapsuleShopOdds12)
    mrBlizzardCapsuleShopOdds34 = convert_to_hex_weight(mrBlizzardCapsuleShopOdds34)
    mrBlizzardCapsuleSpaceOdds1 = convert_to_hex_weight(mrBlizzardCapsuleSpaceOdds1)
    mrBlizzardCapsuleSpaceOdds2 = convert_to_hex_weight(mrBlizzardCapsuleSpaceOdds2)
    mrBlizzardCapsuleSpaceOdds34 = convert_to_hex_weight(mrBlizzardCapsuleSpaceOdds34)

    banditCapsulePrice1 = convert_to_hex_weight(banditCapsulePrice1)
    banditCapsulePrice2 = convert_to_hex_weight(banditCapsulePrice2)
    banditCapsulePrice34 = convert_to_hex_weight(banditCapsulePrice34)
    banditCapsuleShopOdds12 = convert_to_hex_weight(banditCapsuleShopOdds12)
    banditCapsuleShopOdds34 = convert_to_hex_weight(banditCapsuleShopOdds34)
    banditCapsuleSpaceOdds1 = convert_to_hex_weight(banditCapsuleSpaceOdds1)
    banditCapsuleSpaceOdds2 = convert_to_hex_weight(banditCapsuleSpaceOdds2)
    banditCapsuleSpaceOdds34 = convert_to_hex_weight(banditCapsuleSpaceOdds34)

    pinkBooCapsulePrice1 = convert_to_hex_weight(pinkBooCapsulePrice1)
    pinkBooCapsulePrice2 = convert_to_hex_weight(pinkBooCapsulePrice2)
    pinkBooCapsulePrice34 = convert_to_hex_weight(pinkBooCapsulePrice34)
    pinkBooCapsuleShopOdds12 = convert_to_hex_weight(pinkBooCapsuleShopOdds12)
    pinkBooCapsuleShopOdds34 = convert_to_hex_weight(pinkBooCapsuleShopOdds34)
    pinkBooCapsuleSpaceOdds1 = convert_to_hex_weight(pinkBooCapsuleSpaceOdds1)
    pinkBooCapsuleSpaceOdds2 = convert_to_hex_weight(pinkBooCapsuleSpaceOdds2)
    pinkBooCapsuleSpaceOdds34 = convert_to_hex_weight(pinkBooCapsuleSpaceOdds34)

    spinyCapsulePrice1 = convert_to_hex_weight(spinyCapsulePrice1)
    spinyCapsulePrice2 = convert_to_hex_weight(spinyCapsulePrice2)
    spinyCapsulePrice34 = convert_to_hex_weight(spinyCapsulePrice34)
    spinyCapsuleShopOdds12 = convert_to_hex_weight(spinyCapsuleShopOdds12)
    spinyCapsuleShopOdds34 = convert_to_hex_weight(spinyCapsuleShopOdds34)
    spinyCapsuleSpaceOdds1 = convert_to_hex_weight(spinyCapsuleSpaceOdds1)
    spinyCapsuleSpaceOdds2 = convert_to_hex_weight(spinyCapsuleSpaceOdds2)
    spinyCapsuleSpaceOdds34 = convert_to_hex_weight(spinyCapsuleSpaceOdds34)

    zapCapsulePrice1 = convert_to_hex_weight(zapCapsulePrice1)
    zapCapsulePrice2 = convert_to_hex_weight(zapCapsulePrice2)
    zapCapsulePrice34 = convert_to_hex_weight(zapCapsulePrice34)
    zapCapsuleShopOdds12 = convert_to_hex_weight(zapCapsuleShopOdds12)
    zapCapsuleShopOdds34 = convert_to_hex_weight(zapCapsuleShopOdds34)
    zapCapsuleSpaceOdds1 = convert_to_hex_weight(zapCapsuleSpaceOdds1)
    zapCapsuleSpaceOdds2 = convert_to_hex_weight(zapCapsuleSpaceOdds2)
    zapCapsuleSpaceOdds34 = convert_to_hex_weight(zapCapsuleSpaceOdds34)

    tweesterCapsulePrice1 = convert_to_hex_weight(tweesterCapsulePrice1)
    tweesterCapsulePrice2 = convert_to_hex_weight(tweesterCapsulePrice2)
    tweesterCapsulePrice34 = convert_to_hex_weight(tweesterCapsulePrice34)
    tweesterCapsuleShopOdds12 = convert_to_hex_weight(tweesterCapsuleShopOdds12)
    tweesterCapsuleShopOdds34 = convert_to_hex_weight(tweesterCapsuleShopOdds34)
    tweesterCapsuleSpaceOdds1 = convert_to_hex_weight(tweesterCapsuleSpaceOdds1)
    tweesterCapsuleSpaceOdds2 = convert_to_hex_weight(tweesterCapsuleSpaceOdds2)
    tweesterCapsuleSpaceOdds34 = convert_to_hex_weight(tweesterCapsuleSpaceOdds34)

    thwompCapsulePrice1 = convert_to_hex_weight(thwompCapsulePrice1)
    thwompCapsulePrice2 = convert_to_hex_weight(thwompCapsulePrice2)
    thwompCapsulePrice34 = convert_to_hex_weight(thwompCapsulePrice34)
    thwompCapsuleShopOdds12 = convert_to_hex_weight(thwompCapsuleShopOdds12)
    thwompCapsuleShopOdds34 = convert_to_hex_weight(thwompCapsuleShopOdds34)
    thwompCapsuleSpaceOdds1 = convert_to_hex_weight(thwompCapsuleSpaceOdds1)
    thwompCapsuleSpaceOdds2 = convert_to_hex_weight(thwompCapsuleSpaceOdds2)
    thwompCapsuleSpaceOdds34 = convert_to_hex_weight(thwompCapsuleSpaceOdds34)

    warpCapsulePrice1 = convert_to_hex_weight(warpCapsulePrice1)
    warpCapsulePrice2 = convert_to_hex_weight(warpCapsulePrice2)
    warpCapsulePrice34 = convert_to_hex_weight(warpCapsulePrice34)
    warpCapsuleShopOdds12 = convert_to_hex_weight(warpCapsuleShopOdds12)
    warpCapsuleShopOdds34 = convert_to_hex_weight(warpCapsuleShopOdds34)
    warpCapsuleSpaceOdds1 = convert_to_hex_weight(warpCapsuleSpaceOdds1)
    warpCapsuleSpaceOdds2 = convert_to_hex_weight(warpCapsuleSpaceOdds2)
    warpCapsuleSpaceOdds34 = convert_to_hex_weight(warpCapsuleSpaceOdds34)

    bombCapsulePrice1 = convert_to_hex_weight(bombCapsulePrice1)
    bombCapsulePrice2 = convert_to_hex_weight(bombCapsulePrice2)
    bombCapsulePrice34 = convert_to_hex_weight(bombCapsulePrice34)
    bombCapsuleShopOdds12 = convert_to_hex_weight(bombCapsuleShopOdds12)
    bombCapsuleShopOdds34 = convert_to_hex_weight(bombCapsuleShopOdds34)
    bombCapsuleSpaceOdds1 = convert_to_hex_weight(bombCapsuleSpaceOdds1)
    bombCapsuleSpaceOdds2 = convert_to_hex_weight(bombCapsuleSpaceOdds2)
    bombCapsuleSpaceOdds34 = convert_to_hex_weight(bombCapsuleSpaceOdds34)

    fireballCapsulePrice1 = convert_to_hex_weight(fireballCapsulePrice1)
    fireballCapsulePrice2 = convert_to_hex_weight(fireballCapsulePrice2)
    fireballCapsulePrice34 = convert_to_hex_weight(fireballCapsulePrice34)
    fireballCapsuleShopOdds12 = convert_to_hex_weight(fireballCapsuleShopOdds12)
    fireballCapsuleShopOdds34 = convert_to_hex_weight(fireballCapsuleShopOdds34)
    fireballCapsuleSpaceOdds1 = convert_to_hex_weight(fireballCapsuleSpaceOdds1)
    fireballCapsuleSpaceOdds2 = convert_to_hex_weight(fireballCapsuleSpaceOdds2)
    fireballCapsuleSpaceOdds34 = convert_to_hex_weight(fireballCapsuleSpaceOdds34)

    flowerCapsulePrice1 = convert_to_hex_weight(flowerCapsulePrice1)
    flowerCapsulePrice2 = convert_to_hex_weight(flowerCapsulePrice2)
    flowerCapsulePrice34 = convert_to_hex_weight(flowerCapsulePrice34)
    flowerCapsuleShopOdds12 = convert_to_hex_weight(flowerCapsuleShopOdds12)
    flowerCapsuleShopOdds34 = convert_to_hex_weight(flowerCapsuleShopOdds34)
    flowerCapsuleSpaceOdds1 = convert_to_hex_weight(flowerCapsuleSpaceOdds1)
    flowerCapsuleSpaceOdds2 = convert_to_hex_weight(flowerCapsuleSpaceOdds2)
    flowerCapsuleSpaceOdds34 = convert_to_hex_weight(flowerCapsuleSpaceOdds34)

    eggCapsulePrice1 = convert_to_hex_weight(eggCapsulePrice1)
    eggCapsulePrice2 = convert_to_hex_weight(eggCapsulePrice2)
    eggCapsulePrice34 = convert_to_hex_weight(eggCapsulePrice34)
    eggCapsuleShopOdds12 = convert_to_hex_weight(eggCapsuleShopOdds12)
    eggCapsuleShopOdds34 = convert_to_hex_weight(eggCapsuleShopOdds34)
    eggCapsuleSpaceOdds1 = convert_to_hex_weight(eggCapsuleSpaceOdds1)
    eggCapsuleSpaceOdds2 = convert_to_hex_weight(eggCapsuleSpaceOdds2)
    eggCapsuleSpaceOdds34 = convert_to_hex_weight(eggCapsuleSpaceOdds34)

    vacuumCapsulePrice1 = convert_to_hex_weight(vacuumCapsulePrice1)
    vacuumCapsulePrice2 = convert_to_hex_weight(vacuumCapsulePrice2)
    vacuumCapsulePrice34 = convert_to_hex_weight(vacuumCapsulePrice34)
    vacuumCapsuleShopOdds12 = convert_to_hex_weight(vacuumCapsuleShopOdds12)
    vacuumCapsuleShopOdds34 = convert_to_hex_weight(vacuumCapsuleShopOdds34)
    vacuumCapsuleSpaceOdds1 = convert_to_hex_weight(vacuumCapsuleSpaceOdds1)
    vacuumCapsuleSpaceOdds2 = convert_to_hex_weight(vacuumCapsuleSpaceOdds2)
    vacuumCapsuleSpaceOdds34 = convert_to_hex_weight(vacuumCapsuleSpaceOdds34)

    magicCapsulePrice1 = convert_to_hex_weight(magicCapsulePrice1)
    magicCapsulePrice2 = convert_to_hex_weight(magicCapsulePrice2)
    magicCapsulePrice34 = convert_to_hex_weight(magicCapsulePrice34)
    magicCapsuleShopOdds12 = convert_to_hex_weight(magicCapsuleShopOdds12)
    magicCapsuleShopOdds34 = convert_to_hex_weight(magicCapsuleShopOdds34)
    magicCapsuleSpaceOdds1 = convert_to_hex_weight(magicCapsuleSpaceOdds1)
    magicCapsuleSpaceOdds2 = convert_to_hex_weight(magicCapsuleSpaceOdds2)
    magicCapsuleSpaceOdds34 = convert_to_hex_weight(magicCapsuleSpaceOdds34)

    tripleCapsulePrice1 = convert_to_hex_weight(tripleCapsulePrice1)
    tripleCapsulePrice2 = convert_to_hex_weight(tripleCapsulePrice2)
    tripleCapsulePrice34 = convert_to_hex_weight(tripleCapsulePrice34)
    tripleCapsuleShopOdds12 = convert_to_hex_weight(tripleCapsuleShopOdds12)
    tripleCapsuleShopOdds34 = convert_to_hex_weight(tripleCapsuleShopOdds34)
    tripleCapsuleSpaceOdds1 = convert_to_hex_weight(tripleCapsuleSpaceOdds1)
    tripleCapsuleSpaceOdds2 = convert_to_hex_weight(tripleCapsuleSpaceOdds2)
    tripleCapsuleSpaceOdds34 = convert_to_hex_weight(tripleCapsuleSpaceOdds34)

    koopaCapsulePrice1 = convert_to_hex_weight(koopaCapsulePrice1)
    koopaCapsulePrice2 = convert_to_hex_weight(koopaCapsulePrice2)
    koopaCapsulePrice34 = convert_to_hex_weight(koopaCapsulePrice34)
    koopaCapsuleShopOdds12 = convert_to_hex_weight(koopaCapsuleShopOdds12)
    koopaCapsuleShopOdds34 = convert_to_hex_weight(koopaCapsuleShopOdds34)
    koopaCapsuleSpaceOdds1 = convert_to_hex_weight(koopaCapsuleSpaceOdds1)
    koopaCapsuleSpaceOdds2 = convert_to_hex_weight(koopaCapsuleSpaceOdds2)
    koopaCapsuleSpaceOdds34 = convert_to_hex_weight(koopaCapsuleSpaceOdds34)

    poisonMushroomPrice1 = convert_to_hex_weight(poisonMushroomPrice1)
    poisonMushroomPrice2 = convert_to_hex_weight(poisonMushroomPrice2)
    poisonMushroomPrice34 = convert_to_hex_weight(poisonMushroomPrice34)
    poisonMushroomShopOdds12 = convert_to_hex_weight(poisonMushroomShopOdds12)
    poisonMushroomShopOdds34 = convert_to_hex_weight(poisonMushroomShopOdds34)
    poisonMushroomSpaceOdds1 = convert_to_hex_weight(poisonMushroomSpaceOdds1)
    poisonMushroomSpaceOdds2 = convert_to_hex_weight(poisonMushroomSpaceOdds2)
    poisonMushroomSpaceOdds34 = convert_to_hex_weight(poisonMushroomSpaceOdds34)

    orbBagCapsulePrice1 = convert_to_hex_weight(orbBagCapsulePrice1)
    orbBagCapsulePrice2 = convert_to_hex_weight(orbBagCapsulePrice2)
    orbBagCapsulePrice34 = convert_to_hex_weight(orbBagCapsulePrice34)
    orbBagCapsuleShopOdds12 = convert_to_hex_weight(orbBagCapsuleShopOdds12)
    orbBagCapsuleShopOdds34 = convert_to_hex_weight(orbBagCapsuleShopOdds34)
    orbBagCapsuleSpaceOdds1 = convert_to_hex_weight(orbBagCapsuleSpaceOdds1)
    orbBagCapsuleSpaceOdds2 = convert_to_hex_weight(orbBagCapsuleSpaceOdds2)
    orbBagCapsuleSpaceOdds34 = convert_to_hex_weight(orbBagCapsuleSpaceOdds34)

    mysteryCapsulePrice1 = convert_to_hex_weight(mysteryCapsulePrice1)
    mysteryCapsulePrice2 = convert_to_hex_weight(mysteryCapsulePrice2)
    mysteryCapsulePrice34 = convert_to_hex_weight(mysteryCapsulePrice34)
    mysteryCapsuleShopOdds12 = convert_to_hex_weight(mysteryCapsuleShopOdds12)
    mysteryCapsuleShopOdds34 = convert_to_hex_weight(mysteryCapsuleShopOdds34)
    mysteryCapsuleSpaceOdds1 = convert_to_hex_weight(mysteryCapsuleSpaceOdds1)
    mysteryCapsuleSpaceOdds2 = convert_to_hex_weight(mysteryCapsuleSpaceOdds2)
    mysteryCapsuleSpaceOdds34 = convert_to_hex_weight(mysteryCapsuleSpaceOdds34)

    dkCapsulePrice1 = convert_to_hex_weight(dkCapsulePrice1)
    dkCapsulePrice2 = convert_to_hex_weight(dkCapsulePrice2)
    dkCapsulePrice34 = convert_to_hex_weight(dkCapsulePrice34)
    dkCapsuleShopOdds12 = convert_to_hex_weight(dkCapsuleShopOdds12)
    dkCapsuleShopOdds34 = convert_to_hex_weight(dkCapsuleShopOdds34)
    dkCapsuleSpaceOdds1 = convert_to_hex_weight(dkCapsuleSpaceOdds1)
    dkCapsuleSpaceOdds2 = convert_to_hex_weight(dkCapsuleSpaceOdds2)
    dkCapsuleSpaceOdds34 = convert_to_hex_weight(dkCapsuleSpaceOdds34)

    duelCapsulePrice1 = convert_to_hex_weight(duelCapsulePrice1)
    duelCapsulePrice2 = convert_to_hex_weight(duelCapsulePrice2)
    duelCapsulePrice34 = convert_to_hex_weight(duelCapsulePrice34)
    duelCapsuleShopOdds12 = convert_to_hex_weight(duelCapsuleShopOdds12)
    duelCapsuleShopOdds34 = convert_to_hex_weight(duelCapsuleShopOdds34)
    duelCapsuleSpaceOdds1 = convert_to_hex_weight(duelCapsuleSpaceOdds1)
    duelCapsuleSpaceOdds2 = convert_to_hex_weight(duelCapsuleSpaceOdds2)
    duelCapsuleSpaceOdds34 = convert_to_hex_weight(duelCapsuleSpaceOdds34)

    generatedCode = getOrbModsSeven(mushroomCapsulePrice1, mushroomCapsulePrice2, mushroomCapsulePrice34, mushroomCapsuleShopOdds12, mushroomCapsuleShopOdds34, mushroomCapsuleSpaceOdds1,mushroomCapsuleSpaceOdds2, mushroomCapsuleSpaceOdds34, goldenMushroomCapsulePrice1, goldenMushroomCapsulePrice2, goldenMushroomCapsulePrice34, goldenMushroomCapsuleShopOdds12, goldenMushroomCapsuleShopOdds34, goldenMushroomCapsuleSpaceOdds1, goldenMushroomCapsuleSpaceOdds2, goldenMushroomCapsuleSpaceOdds34, slowMushroomCapsulePrice1, slowMushroomCapsulePrice2, slowMushroomCapsulePrice34, slowMushroomCapsuleShopOdds12, slowMushroomCapsuleShopOdds34, slowMushroomCapsuleSpaceOdds1, slowMushroomCapsuleSpaceOdds2, slowMushroomCapsuleSpaceOdds34, metalMushroomCapsulePrice1, metalMushroomCapsulePrice2, metalMushroomCapsulePrice34, metalMushroomCapsuleShopOdds12, metalMushroomCapsuleShopOdds34, metalMushroomCapsuleSpaceOdds1, metalMushroomCapsuleSpaceOdds2, metalMushroomCapsuleSpaceOdds34, flutterCapsulePrice1, flutterCapsulePrice2, flutterCapsulePrice34, flutterCapsuleShopOdds12, flutterCapsuleShopOdds34, flutterCapsuleSpaceOdds1, flutterCapsuleSpaceOdds2, flutterCapsuleSpaceOdds34, cannonCapsulePrice1, cannonCapsulePrice2, cannonCapsulePrice34, cannonCapsuleShopOdds12, cannonCapsuleShopOdds34, cannonCapsuleSpaceOdds1, cannonCapsuleSpaceOdds2, cannonCapsuleSpaceOdds34, snackCapsulePrice1, snackCapsulePrice2, snackCapsulePrice34, snackCapsuleShopOdds12, snackCapsuleShopOdds34, snackCapsuleSpaceOdds1, snackCapsuleSpaceOdds2, snackCapsuleSpaceOdds34, lakituCapsulePrice1, lakituCapsulePrice2, lakituCapsulePrice34, lakituCapsuleShopOdds12, lakituCapsuleShopOdds34, lakituCapsuleSpaceOdds1, lakituCapsuleSpaceOdds2, lakituCapsuleSpaceOdds34, hammerBroCapsulePrice1, hammerBroCapsulePrice2, hammerBroCapsulePrice34, hammerBroCapsuleShopOdds12, hammerBroCapsuleShopOdds34, hammerBroCapsuleSpaceOdds1, hammerBroCapsuleSpaceOdds2, hammerBroCapsuleSpaceOdds34, piranhaPlantCapsulePrice1, piranhaPlantCapsulePrice2, piranhaPlantCapsulePrice34, piranhaPlantCapsuleShopOdds12, piranhaPlantCapsuleShopOdds34, piranhaPlantCapsuleSpaceOdds1, piranhaPlantCapsuleSpaceOdds2, piranhaPlantCapsuleSpaceOdds34, spearGuyCapsulePrice1, spearGuyCapsulePrice2, spearGuyCapsulePrice34, spearGuyCapsuleShopOdds12, spearGuyCapsuleShopOdds34, spearGuyCapsuleSpaceOdds1, spearGuyCapsuleSpaceOdds2, spearGuyCapsuleSpaceOdds34, kamekCapsulePrice1, kamekCapsulePrice2, kamekCapsulePrice34, kamekCapsuleShopOdds12, kamekCapsuleShopOdds34, kamekCapsuleSpaceOdds1, kamekCapsuleSpaceOdds2, kamekCapsuleSpaceOdds34, toadyCapsulePrice1, toadyCapsulePrice2, toadyCapsulePrice34, toadyCapsuleShopOdds12, toadyCapsuleShopOdds34, toadyCapsuleSpaceOdds1, toadyCapsuleSpaceOdds2, toadyCapsuleSpaceOdds34, mrBlizzardCapsulePrice1, mrBlizzardCapsulePrice2, mrBlizzardCapsulePrice34, mrBlizzardCapsuleShopOdds12, mrBlizzardCapsuleShopOdds34, mrBlizzardCapsuleSpaceOdds1, mrBlizzardCapsuleSpaceOdds2, mrBlizzardCapsuleSpaceOdds34, banditCapsulePrice1, banditCapsulePrice2, banditCapsulePrice34, banditCapsuleShopOdds12, banditCapsuleShopOdds34, banditCapsuleSpaceOdds1, banditCapsuleSpaceOdds2, banditCapsuleSpaceOdds34, pinkBooCapsulePrice1, pinkBooCapsulePrice2, pinkBooCapsulePrice34, pinkBooCapsuleShopOdds12, pinkBooCapsuleShopOdds34, pinkBooCapsuleSpaceOdds1, pinkBooCapsuleSpaceOdds2, pinkBooCapsuleSpaceOdds34, spinyCapsulePrice1, spinyCapsulePrice2, spinyCapsulePrice34, spinyCapsuleShopOdds12, spinyCapsuleShopOdds34, spinyCapsuleSpaceOdds1, spinyCapsuleSpaceOdds2, spinyCapsuleSpaceOdds34, zapCapsulePrice1, zapCapsulePrice2, zapCapsulePrice34, zapCapsuleShopOdds12, zapCapsuleShopOdds34, zapCapsuleSpaceOdds1, zapCapsuleSpaceOdds2, zapCapsuleSpaceOdds34, tweesterCapsulePrice1, tweesterCapsulePrice2, tweesterCapsulePrice34, tweesterCapsuleShopOdds12, tweesterCapsuleShopOdds34, tweesterCapsuleSpaceOdds1, tweesterCapsuleSpaceOdds2, tweesterCapsuleSpaceOdds34, thwompCapsulePrice1, thwompCapsulePrice2, thwompCapsulePrice34, thwompCapsuleShopOdds12, thwompCapsuleShopOdds34, thwompCapsuleSpaceOdds1, thwompCapsuleSpaceOdds2, thwompCapsuleSpaceOdds34, warpCapsulePrice1, warpCapsulePrice2, warpCapsulePrice34, warpCapsuleShopOdds12, warpCapsuleShopOdds34, warpCapsuleSpaceOdds1, warpCapsuleSpaceOdds2, warpCapsuleSpaceOdds34, bombCapsulePrice1, bombCapsulePrice2, bombCapsulePrice34, bombCapsuleShopOdds12, bombCapsuleShopOdds34, bombCapsuleSpaceOdds1, bombCapsuleSpaceOdds2, bombCapsuleSpaceOdds34, fireballCapsulePrice1, fireballCapsulePrice2, fireballCapsulePrice34, fireballCapsuleShopOdds12, fireballCapsuleShopOdds34, fireballCapsuleSpaceOdds1, fireballCapsuleSpaceOdds2, fireballCapsuleSpaceOdds34, flowerCapsulePrice1, flowerCapsulePrice2, flowerCapsulePrice34, flowerCapsuleShopOdds12, flowerCapsuleShopOdds34, flowerCapsuleSpaceOdds1, flowerCapsuleSpaceOdds2, flowerCapsuleSpaceOdds34, eggCapsulePrice1, eggCapsulePrice2, eggCapsulePrice34, eggCapsuleShopOdds12, eggCapsuleShopOdds34, eggCapsuleSpaceOdds1, eggCapsuleSpaceOdds2, eggCapsuleSpaceOdds34, vacuumCapsulePrice1, vacuumCapsulePrice2, vacuumCapsulePrice34, vacuumCapsuleShopOdds12, vacuumCapsuleShopOdds34, vacuumCapsuleSpaceOdds1, vacuumCapsuleSpaceOdds2, vacuumCapsuleSpaceOdds34, magicCapsulePrice1, magicCapsulePrice2, magicCapsulePrice34, magicCapsuleShopOdds12, magicCapsuleShopOdds34, magicCapsuleSpaceOdds1, magicCapsuleSpaceOdds2, magicCapsuleSpaceOdds34, tripleCapsulePrice1, tripleCapsulePrice2, tripleCapsulePrice34, tripleCapsuleShopOdds12, tripleCapsuleShopOdds34, tripleCapsuleSpaceOdds1, tripleCapsuleSpaceOdds2, tripleCapsuleSpaceOdds34, koopaCapsulePrice1, koopaCapsulePrice2, koopaCapsulePrice34, koopaCapsuleShopOdds12, koopaCapsuleShopOdds34, koopaCapsuleSpaceOdds1, koopaCapsuleSpaceOdds2, koopaCapsuleSpaceOdds34, poisonMushroomPrice1, poisonMushroomPrice2, poisonMushroomPrice34, poisonMushroomShopOdds12, poisonMushroomShopOdds34, poisonMushroomSpaceOdds1, poisonMushroomSpaceOdds2, poisonMushroomSpaceOdds34, orbBagCapsulePrice1, orbBagCapsulePrice2, orbBagCapsulePrice34, orbBagCapsuleShopOdds12, orbBagCapsuleShopOdds34, orbBagCapsuleSpaceOdds1, orbBagCapsuleSpaceOdds2, orbBagCapsuleSpaceOdds34, mysteryCapsulePrice1, mysteryCapsulePrice2, mysteryCapsulePrice34, mysteryCapsuleShopOdds12, mysteryCapsuleShopOdds34, mysteryCapsuleSpaceOdds1, mysteryCapsuleSpaceOdds2, mysteryCapsuleSpaceOdds34, dkCapsulePrice1, dkCapsulePrice2, dkCapsulePrice34, dkCapsuleShopOdds12, dkCapsuleShopOdds34, dkCapsuleSpaceOdds1, dkCapsuleSpaceOdds2, dkCapsuleSpaceOdds34, duelCapsulePrice1, duelCapsulePrice2, duelCapsulePrice34, duelCapsuleShopOdds12, duelCapsuleShopOdds34, duelCapsuleSpaceOdds1, duelCapsuleSpaceOdds2, duelCapsuleSpaceOdds34)
    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)

    print("Generated code copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

def savePresetItems7(mushroomCapsuleShopOdds12 = "0", mushroomCapsuleShopOdds34 = "0", mushroomCapsuleSpaceOdds1 = "0", mushroomCapsuleSpaceOdds2 = "0", mushroomCapsuleSpaceOdds34 = "0", goldenMushroomCapsulePrice1 = "0", goldenMushroomCapsulePrice2 = "0", goldenMushroomCapsulePrice34 = "0", goldenMushroomCapsuleShopOdds12 = "0", goldenMushroomCapsuleShopOdds34 = "0", goldenMushroomCapsuleSpaceOdds1 = "0", goldenMushroomCapsuleSpaceOdds2 = "0", goldenMushroomCapsuleSpaceOdds34 = "0", slowMushroomCapsulePrice1 = "0", slowMushroomCapsulePrice2 = "0", slowMushroomCapsulePrice34 = "0", slowMushroomCapsuleShopOdds12 = "0", slowMushroomCapsuleShopOdds34 = "0", slowMushroomCapsuleSpaceOdds1 = "0", slowMushroomCapsuleSpaceOdds2 = "0", slowMushroomCapsuleSpaceOdds34 = "0", metalMushroomCapsulePrice1 = "0", metalMushroomCapsulePrice2 = "0", metalMushroomCapsulePrice34 = "0", metalMushroomCapsuleShopOdds12 = "0", metalMushroomCapsuleShopOdds34 = "0", metalMushroomCapsuleSpaceOdds1 = "0", metalMushroomCapsuleSpaceOdds2 = "0", metalMushroomCapsuleSpaceOdds34 = "0", flutterCapsulePrice1 = "0", flutterCapsulePrice2 = "0", flutterCapsulePrice34 = "0", flutterCapsuleShopOdds12 = "0", flutterCapsuleShopOdds34 = "0", flutterCapsuleSpaceOdds1 = "0", flutterCapsuleSpaceOdds2 = "0", flutterCapsuleSpaceOdds34 = "0", cannonCapsulePrice1 = "0", cannonCapsulePrice2 = "0", cannonCapsulePrice34 = "0", cannonCapsuleShopOdds12 = "0", cannonCapsuleShopOdds34 = "0", cannonCapsuleSpaceOdds1 = "0", cannonCapsuleSpaceOdds2 = "0", cannonCapsuleSpaceOdds34 = "0", snackCapsulePrice1 = "0", snackCapsulePrice2 = "0", snackCapsulePrice34 = "0", snackCapsuleShopOdds12 = "0", snackCapsuleShopOdds34 = "0", snackCapsuleSpaceOdds1 = "0", snackCapsuleSpaceOdds2 = "0", snackCapsuleSpaceOdds34 = "0", lakituCapsulePrice1 = "0", lakituCapsulePrice2 = "0", lakituCapsulePrice34 = "0", lakituCapsuleShopOdds12 = "0", lakituCapsuleShopOdds34 = "0", lakituCapsuleSpaceOdds1 = "0", lakituCapsuleSpaceOdds2 = "0", lakituCapsuleSpaceOdds34 = "0", hammerBroCapsulePrice1 = "0", hammerBroCapsulePrice2 = "0", hammerBroCapsulePrice34 = "0", hammerBroCapsuleShopOdds12 = "0", hammerBroCapsuleShopOdds34 = "0", hammerBroCapsuleSpaceOdds1 = "0", hammerBroCapsuleSpaceOdds2 = "0", hammerBroCapsuleSpaceOdds34 = "0", piranhaPlantCapsulePrice1 = "0", piranhaPlantCapsulePrice2 = "0", piranhaPlantCapsulePrice34 = "0", piranhaPlantCapsuleShopOdds12 = "0", piranhaPlantCapsuleShopOdds34 = "0", piranhaPlantCapsuleSpaceOdds1 = "0", piranhaPlantCapsuleSpaceOdds2 = "0", piranhaPlantCapsuleSpaceOdds34 = "0", spearGuyCapsulePrice1 = "0", spearGuyCapsulePrice2 = "0", spearGuyCapsulePrice34 = "0", spearGuyCapsuleShopOdds12 = "0", spearGuyCapsuleShopOdds34 = "0", spearGuyCapsuleSpaceOdds1 = "0", spearGuyCapsuleSpaceOdds2 = "0", spearGuyCapsuleSpaceOdds34 = "0", kamekCapsulePrice1 = "0", kamekCapsulePrice2 = "0", kamekCapsulePrice34 = "0", kamekCapsuleShopOdds12 = "0", kamekCapsuleShopOdds34 = "0", kamekCapsuleSpaceOdds1 = "0", kamekCapsuleSpaceOdds2 = "0", kamekCapsuleSpaceOdds34 = "0", toadyCapsulePrice1 = "0", toadyCapsulePrice2 = "0", toadyCapsulePrice34 = "0", toadyCapsuleShopOdds12 = "0", toadyCapsuleShopOdds34 = "0", toadyCapsuleSpaceOdds1 = "0", toadyCapsuleSpaceOdds2 = "0", toadyCapsuleSpaceOdds34 = "0", mrBlizzardCapsulePrice1 = "0", mrBlizzardCapsulePrice2 = "0", mrBlizzardCapsulePrice34 = "0", mrBlizzardCapsuleShopOdds12 = "0", mrBlizzardCapsuleShopOdds34 = "0", mrBlizzardCapsuleSpaceOdds1 = "0", mrBlizzardCapsuleSpaceOdds2 = "0", mrBlizzardCapsuleSpaceOdds34 = "0", banditCapsulePrice1 = "0", banditCapsulePrice2 = "0", banditCapsulePrice34 = "0", banditCapsuleShopOdds12 = "0", banditCapsuleShopOdds34 = "0", banditCapsuleSpaceOdds1 = "0", banditCapsuleSpaceOdds2 = "0", banditCapsuleSpaceOdds34 = "0", pinkBooCapsulePrice1 = "0", pinkBooCapsulePrice2 = "0", pinkBooCapsulePrice34 = "0", pinkBooCapsuleShopOdds12 = "0", pinkBooCapsuleShopOdds34 = "0", pinkBooCapsuleSpaceOdds1 = "0", pinkBooCapsuleSpaceOdds2 = "0", pinkBooCapsuleSpaceOdds34 = "0", spinyCapsulePrice1 = "0", spinyCapsulePrice2 = "0", spinyCapsulePrice34 = "0", spinyCapsuleShopOdds12 = "0", spinyCapsuleShopOdds34 = "0", spinyCapsuleSpaceOdds1 = "0", spinyCapsuleSpaceOdds2 = "0", spinyCapsuleSpaceOdds34 = "0", zapCapsulePrice1 = "0", zapCapsulePrice2 = "0", zapCapsulePrice34 = "0", zapCapsuleShopOdds12 = "0", zapCapsuleShopOdds34 = "0", zapCapsuleSpaceOdds1 = "0", zapCapsuleSpaceOdds2 = "0", zapCapsuleSpaceOdds34 = "0", tweesterCapsulePrice1 = "0", tweesterCapsulePrice2 = "0", tweesterCapsulePrice34 = "0", tweesterCapsuleShopOdds12 = "0", tweesterCapsuleShopOdds34 = "0", tweesterCapsuleSpaceOdds1 = "0", tweesterCapsuleSpaceOdds2 = "0", tweesterCapsuleSpaceOdds34 = "0", thwompCapsulePrice1 = "0", thwompCapsulePrice2 = "0", thwompCapsulePrice34 = "0", thwompCapsuleShopOdds12 = "0", thwompCapsuleShopOdds34 = "0", thwompCapsuleSpaceOdds1 = "0", thwompCapsuleSpaceOdds2 = "0", thwompCapsuleSpaceOdds34 = "0", warpCapsulePrice1 = "0", warpCapsulePrice2 = "0", warpCapsulePrice34 = "0", warpCapsuleShopOdds12 = "0", warpCapsuleShopOdds34 = "0", warpCapsuleSpaceOdds1 = "0", warpCapsuleSpaceOdds2 = "0", warpCapsuleSpaceOdds34 = "0", bombCapsulePrice1 = "0", bombCapsulePrice2 = "0", bombCapsulePrice34 = "0", bombCapsuleShopOdds12 = "0", bombCapsuleShopOdds34 = "0", bombCapsuleSpaceOdds1 = "0", bombCapsuleSpaceOdds2 = "0", bombCapsuleSpaceOdds34 = "0", fireballCapsulePrice1 = "0", fireballCapsulePrice2 = "0", fireballCapsulePrice34 = "0", fireballCapsuleShopOdds12 = "0", fireballCapsuleShopOdds34 = "0", fireballCapsuleSpaceOdds1 = "0", fireballCapsuleSpaceOdds2 = "0", fireballCapsuleSpaceOdds34 = "0", flowerCapsulePrice1 = "0", flowerCapsulePrice2 = "0", flowerCapsulePrice34 = "0", flowerCapsuleShopOdds12 = "0", flowerCapsuleShopOdds34 = "0", flowerCapsuleSpaceOdds1 = "0", flowerCapsuleSpaceOdds2 = "0", flowerCapsuleSpaceOdds34 = "0", eggCapsulePrice1 = "0", eggCapsulePrice2 = "0", eggCapsulePrice34 = "0", eggCapsuleShopOdds12 = "0", eggCapsuleShopOdds34 = "0", eggCapsuleSpaceOdds1 = "0", eggCapsuleSpaceOdds2 = "0", eggCapsuleSpaceOdds34 = "0", vacuumCapsulePrice1 = "0", vacuumCapsulePrice2 = "0", vacuumCapsulePrice34 = "0", vacuumCapsuleShopOdds12 = "0", vacuumCapsuleShopOdds34 = "0", vacuumCapsuleSpaceOdds1 = "0", vacuumCapsuleSpaceOdds2 = "0", vacuumCapsuleSpaceOdds34 = "0", magicCapsulePrice1 = "0", magicCapsulePrice2 = "0", magicCapsulePrice34 = "0", magicCapsuleShopOdds12 = "0", magicCapsuleShopOdds34 = "0", magicCapsuleSpaceOdds1 = "0", magicCapsuleSpaceOdds2 = "0", magicCapsuleSpaceOdds34 = "0", tripleCapsulePrice1 = "0", tripleCapsulePrice2 = "0", tripleCapsulePrice34 = "0", tripleCapsuleShopOdds12 = "0", tripleCapsuleShopOdds34 = "0", tripleCapsuleSpaceOdds1 = "0", tripleCapsuleSpaceOdds2 = "0", tripleCapsuleSpaceOdds34 = "0", koopaCapsulePrice1 = "0", koopaCapsulePrice2 = "0", koopaCapsulePrice34 = "0", koopaCapsuleShopOdds12 = "0", koopaCapsuleShopOdds34 = "0", koopaCapsuleSpaceOdds1 = "0", koopaCapsuleSpaceOdds2 = "0", koopaCapsuleSpaceOdds34 = "0", poisonMushroomPrice1 = "0", poisonMushroomPrice2 = "0", poisonMushroomPrice34 = "0", poisonMushroomShopOdds12 = "0", poisonMushroomShopOdds34 = "0", poisonMushroomSpaceOdds1 = "0", poisonMushroomSpaceOdds2 = "0", poisonMushroomSpaceOdds34 = "0", orbBagCapsulePrice1 = "0", orbBagCapsulePrice2 = "0", orbBagCapsulePrice34 = "0", orbBagCapsuleShopOdds12 = "0", orbBagCapsuleShopOdds34 = "0", orbBagCapsuleSpaceOdds1 = "0", orbBagCapsuleSpaceOdds2 = "0", orbBagCapsuleSpaceOdds34 = "0", mysteryCapsulePrice1 = "0", mysteryCapsulePrice2 = "0", mysteryCapsulePrice34 = "0", mysteryCapsuleShopOdds12 = "0", mysteryCapsuleShopOdds34 = "0", mysteryCapsuleSpaceOdds1 = "0", mysteryCapsuleSpaceOdds2 = "0", mysteryCapsuleSpaceOdds34 = "0", dkCapsulePrice1 = "0", dkCapsulePrice2 = "0", dkCapsulePrice34 = "0", dkCapsuleShopOdds12 = "0", dkCapsuleShopOdds34 = "0", dkCapsuleSpaceOdds1 = "0", dkCapsuleSpaceOdds2 = "0", dkCapsuleSpaceOdds34 = "0", duelCapsulePrice1 = "0", duelCapsulePrice2 = "0", duelCapsulePrice34 = "0", duelCapsuleShopOdds12 = "0", duelCapsuleShopOdds34 = "0", duelCapsuleSpaceOdds1 = "0", duelCapsuleSpaceOdds2 = "0", duelCapsuleSpaceOdds34 = "0"):
    def get_capsule_value(capsule):
        try:
            return capsule.get()
        except:
            return 0

    mushroomCapsulePrice1 = "5"
    mushroomCapsulePrice2 = "5"
    mushroomCapsulePrice34 = "5"
    mushroomCapsuleShopOdds12 = get_capsule_value(mushroomCapsuleShopOdds12)
    mushroomCapsuleShopOdds34 = get_capsule_value(mushroomCapsuleShopOdds34)
    mushroomCapsuleSpaceOdds1 = get_capsule_value(mushroomCapsuleSpaceOdds1)
    mushroomCapsuleSpaceOdds2 = get_capsule_value(mushroomCapsuleSpaceOdds2)
    mushroomCapsuleSpaceOdds34 = get_capsule_value(mushroomCapsuleSpaceOdds34)

    goldenMushroomCapsulePrice1 = get_capsule_value(goldenMushroomCapsulePrice1)
    goldenMushroomCapsulePrice2 = get_capsule_value(goldenMushroomCapsulePrice2)
    goldenMushroomCapsulePrice34 = get_capsule_value(goldenMushroomCapsulePrice34)
    goldenMushroomCapsuleShopOdds12 = get_capsule_value(goldenMushroomCapsuleShopOdds12)
    goldenMushroomCapsuleShopOdds34 = get_capsule_value(goldenMushroomCapsuleShopOdds34)
    goldenMushroomCapsuleSpaceOdds1 = get_capsule_value(goldenMushroomCapsuleSpaceOdds1)
    goldenMushroomCapsuleSpaceOdds2 = get_capsule_value(goldenMushroomCapsuleSpaceOdds2)
    goldenMushroomCapsuleSpaceOdds34 = get_capsule_value(goldenMushroomCapsuleSpaceOdds34)


    slowMushroomCapsulePrice1 = get_capsule_value(slowMushroomCapsulePrice1)
    slowMushroomCapsulePrice2 = get_capsule_value(slowMushroomCapsulePrice2)
    slowMushroomCapsulePrice34 = get_capsule_value(slowMushroomCapsulePrice34)
    slowMushroomCapsuleShopOdds12 = get_capsule_value(slowMushroomCapsuleShopOdds12)
    slowMushroomCapsuleShopOdds34 = get_capsule_value(slowMushroomCapsuleShopOdds34)
    slowMushroomCapsuleSpaceOdds1 = get_capsule_value(slowMushroomCapsuleSpaceOdds1)
    slowMushroomCapsuleSpaceOdds2 = get_capsule_value(slowMushroomCapsuleSpaceOdds2)
    slowMushroomCapsuleSpaceOdds34 = get_capsule_value(slowMushroomCapsuleSpaceOdds34)

    metalMushroomCapsulePrice1 = get_capsule_value(metalMushroomCapsulePrice1)
    metalMushroomCapsulePrice2 = get_capsule_value(metalMushroomCapsulePrice2)
    metalMushroomCapsulePrice34 = get_capsule_value(metalMushroomCapsulePrice34)
    metalMushroomCapsuleShopOdds12 = get_capsule_value(metalMushroomCapsuleShopOdds12)
    metalMushroomCapsuleShopOdds34 = get_capsule_value(metalMushroomCapsuleShopOdds34)
    metalMushroomCapsuleSpaceOdds1 = get_capsule_value(metalMushroomCapsuleSpaceOdds1)
    metalMushroomCapsuleSpaceOdds2 = get_capsule_value(metalMushroomCapsuleSpaceOdds2)
    metalMushroomCapsuleSpaceOdds34 = get_capsule_value(metalMushroomCapsuleSpaceOdds34)

    flutterCapsulePrice1 = get_capsule_value(flutterCapsulePrice1)
    flutterCapsulePrice2 = get_capsule_value(flutterCapsulePrice2)
    flutterCapsulePrice34 = get_capsule_value(flutterCapsulePrice34)
    flutterCapsuleShopOdds12 = get_capsule_value(flutterCapsuleShopOdds12)
    flutterCapsuleShopOdds34 = get_capsule_value(flutterCapsuleShopOdds34)
    flutterCapsuleSpaceOdds1 = get_capsule_value(flutterCapsuleSpaceOdds1)
    flutterCapsuleSpaceOdds2 = get_capsule_value(flutterCapsuleSpaceOdds2)
    flutterCapsuleSpaceOdds34 = get_capsule_value(flutterCapsuleSpaceOdds34)

    cannonCapsulePrice1 = get_capsule_value(cannonCapsulePrice1)
    cannonCapsulePrice2 = get_capsule_value(cannonCapsulePrice2)
    cannonCapsulePrice34 = get_capsule_value(cannonCapsulePrice34)
    cannonCapsuleShopOdds12 = get_capsule_value(cannonCapsuleShopOdds12)
    cannonCapsuleShopOdds34 = get_capsule_value(cannonCapsuleShopOdds34)
    cannonCapsuleSpaceOdds1 = get_capsule_value(cannonCapsuleSpaceOdds1)
    cannonCapsuleSpaceOdds2 = get_capsule_value(cannonCapsuleSpaceOdds2)
    cannonCapsuleSpaceOdds34 = get_capsule_value(cannonCapsuleSpaceOdds34)

    snackCapsulePrice1 = get_capsule_value(snackCapsulePrice1)
    snackCapsulePrice2 = get_capsule_value(snackCapsulePrice2)
    snackCapsulePrice34 = get_capsule_value(snackCapsulePrice34)
    snackCapsuleShopOdds12 = get_capsule_value(snackCapsuleShopOdds12)
    snackCapsuleShopOdds34 = get_capsule_value(snackCapsuleShopOdds34)
    snackCapsuleSpaceOdds1 = get_capsule_value(snackCapsuleSpaceOdds1)
    snackCapsuleSpaceOdds2 = get_capsule_value(snackCapsuleSpaceOdds2)
    snackCapsuleSpaceOdds34 = get_capsule_value(snackCapsuleSpaceOdds34)

    lakituCapsulePrice1 = get_capsule_value(lakituCapsulePrice1)
    lakituCapsulePrice2 = get_capsule_value(lakituCapsulePrice2)
    lakituCapsulePrice34 = get_capsule_value(lakituCapsulePrice34)
    lakituCapsuleShopOdds12 = get_capsule_value(lakituCapsuleShopOdds12)
    lakituCapsuleShopOdds34 = get_capsule_value(lakituCapsuleShopOdds34)
    lakituCapsuleSpaceOdds1 = get_capsule_value(lakituCapsuleSpaceOdds1)
    lakituCapsuleSpaceOdds2 = get_capsule_value(lakituCapsuleSpaceOdds2)
    lakituCapsuleSpaceOdds34 = get_capsule_value(lakituCapsuleSpaceOdds34)

    hammerBroCapsulePrice1 = get_capsule_value(hammerBroCapsulePrice1)
    hammerBroCapsulePrice2 = get_capsule_value(hammerBroCapsulePrice2)
    hammerBroCapsulePrice34 = get_capsule_value(hammerBroCapsulePrice34)
    hammerBroCapsuleShopOdds12 = get_capsule_value(hammerBroCapsuleShopOdds12)
    hammerBroCapsuleShopOdds34 = get_capsule_value(hammerBroCapsuleShopOdds34)
    hammerBroCapsuleSpaceOdds1 = get_capsule_value(hammerBroCapsuleSpaceOdds1)
    hammerBroCapsuleSpaceOdds2 = get_capsule_value(hammerBroCapsuleSpaceOdds2)
    hammerBroCapsuleSpaceOdds34 = get_capsule_value(hammerBroCapsuleSpaceOdds34)

    piranhaPlantCapsulePrice1 = get_capsule_value(piranhaPlantCapsulePrice1)
    piranhaPlantCapsulePrice2 = get_capsule_value(piranhaPlantCapsulePrice2)
    piranhaPlantCapsulePrice34 = get_capsule_value(piranhaPlantCapsulePrice34)
    piranhaPlantCapsuleShopOdds12 = get_capsule_value(piranhaPlantCapsuleShopOdds12)
    piranhaPlantCapsuleShopOdds34 = get_capsule_value(piranhaPlantCapsuleShopOdds34)
    piranhaPlantCapsuleSpaceOdds1 = get_capsule_value(piranhaPlantCapsuleSpaceOdds1)
    piranhaPlantCapsuleSpaceOdds2 = get_capsule_value(piranhaPlantCapsuleSpaceOdds2)
    piranhaPlantCapsuleSpaceOdds34 = get_capsule_value(piranhaPlantCapsuleSpaceOdds34)

    spearGuyCapsulePrice1 = get_capsule_value(spearGuyCapsulePrice1)
    spearGuyCapsulePrice2 = get_capsule_value(spearGuyCapsulePrice2)
    spearGuyCapsulePrice34 = get_capsule_value(spearGuyCapsulePrice34)
    spearGuyCapsuleShopOdds12 = get_capsule_value(spearGuyCapsuleShopOdds12)
    spearGuyCapsuleShopOdds34 = get_capsule_value(spearGuyCapsuleShopOdds34)
    spearGuyCapsuleSpaceOdds1 = get_capsule_value(spearGuyCapsuleSpaceOdds1)
    spearGuyCapsuleSpaceOdds2 = get_capsule_value(spearGuyCapsuleSpaceOdds2)
    spearGuyCapsuleSpaceOdds34 = get_capsule_value(spearGuyCapsuleSpaceOdds34)

    kamekCapsulePrice1 = get_capsule_value(kamekCapsulePrice1)
    kamekCapsulePrice2 = get_capsule_value(kamekCapsulePrice2)
    kamekCapsulePrice34 = get_capsule_value(kamekCapsulePrice34)
    kamekCapsuleShopOdds12 = get_capsule_value(kamekCapsuleShopOdds12)
    kamekCapsuleShopOdds34 = get_capsule_value(kamekCapsuleShopOdds34)
    kamekCapsuleSpaceOdds1 = get_capsule_value(kamekCapsuleSpaceOdds1)
    kamekCapsuleSpaceOdds2 = get_capsule_value(kamekCapsuleSpaceOdds2)
    kamekCapsuleSpaceOdds34 = get_capsule_value(kamekCapsuleSpaceOdds34)

    toadyCapsulePrice1 = get_capsule_value(toadyCapsulePrice1)
    toadyCapsulePrice2 = get_capsule_value(toadyCapsulePrice2)
    toadyCapsulePrice34 = get_capsule_value(toadyCapsulePrice34)
    toadyCapsuleShopOdds12 = get_capsule_value(toadyCapsuleShopOdds12)
    toadyCapsuleShopOdds34 = get_capsule_value(toadyCapsuleShopOdds34)
    toadyCapsuleSpaceOdds1 = get_capsule_value(toadyCapsuleSpaceOdds1)
    toadyCapsuleSpaceOdds2 = get_capsule_value(toadyCapsuleSpaceOdds2)
    toadyCapsuleSpaceOdds34 = get_capsule_value(toadyCapsuleSpaceOdds34)

    mrBlizzardCapsulePrice1 = get_capsule_value(mrBlizzardCapsulePrice1)
    mrBlizzardCapsulePrice2 = get_capsule_value(mrBlizzardCapsulePrice2)
    mrBlizzardCapsulePrice34 = get_capsule_value(mrBlizzardCapsulePrice34)
    mrBlizzardCapsuleShopOdds12 = get_capsule_value(mrBlizzardCapsuleShopOdds12)
    mrBlizzardCapsuleShopOdds34 = get_capsule_value(mrBlizzardCapsuleShopOdds34)
    mrBlizzardCapsuleSpaceOdds1 = get_capsule_value(mrBlizzardCapsuleSpaceOdds1)
    mrBlizzardCapsuleSpaceOdds2 = get_capsule_value(mrBlizzardCapsuleSpaceOdds2)
    mrBlizzardCapsuleSpaceOdds34 = get_capsule_value(mrBlizzardCapsuleSpaceOdds34)

    banditCapsulePrice1 = get_capsule_value(banditCapsulePrice1)
    banditCapsulePrice2 = get_capsule_value(banditCapsulePrice2)
    banditCapsulePrice34 = get_capsule_value(banditCapsulePrice34)
    banditCapsuleShopOdds12 = get_capsule_value(banditCapsuleShopOdds12)
    banditCapsuleShopOdds34 = get_capsule_value(banditCapsuleShopOdds34)
    banditCapsuleSpaceOdds1 = get_capsule_value(banditCapsuleSpaceOdds1)
    banditCapsuleSpaceOdds2 = get_capsule_value(banditCapsuleSpaceOdds2)
    banditCapsuleSpaceOdds34 = get_capsule_value(banditCapsuleSpaceOdds34)

    pinkBooCapsulePrice1 = get_capsule_value(pinkBooCapsulePrice1)
    pinkBooCapsulePrice2 = get_capsule_value(pinkBooCapsulePrice2)
    pinkBooCapsulePrice34 = get_capsule_value(pinkBooCapsulePrice34)
    pinkBooCapsuleShopOdds12 = get_capsule_value(pinkBooCapsuleShopOdds12)
    pinkBooCapsuleShopOdds34 = get_capsule_value(pinkBooCapsuleShopOdds34)
    pinkBooCapsuleSpaceOdds1 = get_capsule_value(pinkBooCapsuleSpaceOdds1)
    pinkBooCapsuleSpaceOdds2 = get_capsule_value(pinkBooCapsuleSpaceOdds2)
    pinkBooCapsuleSpaceOdds34 = get_capsule_value(pinkBooCapsuleSpaceOdds34)

    spinyCapsulePrice1 = get_capsule_value(spinyCapsulePrice1)
    spinyCapsulePrice2 = get_capsule_value(spinyCapsulePrice2)
    spinyCapsulePrice34 = get_capsule_value(spinyCapsulePrice34)
    spinyCapsuleShopOdds12 = get_capsule_value(spinyCapsuleShopOdds12)
    spinyCapsuleShopOdds34 = get_capsule_value(spinyCapsuleShopOdds34)
    spinyCapsuleSpaceOdds1 = get_capsule_value(spinyCapsuleSpaceOdds1)
    spinyCapsuleSpaceOdds2 = get_capsule_value(spinyCapsuleSpaceOdds2)
    spinyCapsuleSpaceOdds34 = get_capsule_value(spinyCapsuleSpaceOdds34)

    zapCapsulePrice1 = get_capsule_value(zapCapsulePrice1)
    zapCapsulePrice2 = get_capsule_value(zapCapsulePrice2)
    zapCapsulePrice34 = get_capsule_value(zapCapsulePrice34)
    zapCapsuleShopOdds12 = get_capsule_value(zapCapsuleShopOdds12)
    zapCapsuleShopOdds34 = get_capsule_value(zapCapsuleShopOdds34)
    zapCapsuleSpaceOdds1 = get_capsule_value(zapCapsuleSpaceOdds1)
    zapCapsuleSpaceOdds2 = get_capsule_value(zapCapsuleSpaceOdds2)
    zapCapsuleSpaceOdds34 = get_capsule_value(zapCapsuleSpaceOdds34)

    tweesterCapsulePrice1 = get_capsule_value(tweesterCapsulePrice1)
    tweesterCapsulePrice2 = get_capsule_value(tweesterCapsulePrice2)
    tweesterCapsulePrice34 = get_capsule_value(tweesterCapsulePrice34)
    tweesterCapsuleShopOdds12 = get_capsule_value(tweesterCapsuleShopOdds12)
    tweesterCapsuleShopOdds34 = get_capsule_value(tweesterCapsuleShopOdds34)
    tweesterCapsuleSpaceOdds1 = get_capsule_value(tweesterCapsuleSpaceOdds1)
    tweesterCapsuleSpaceOdds2 = get_capsule_value(tweesterCapsuleSpaceOdds2)
    tweesterCapsuleSpaceOdds34 = get_capsule_value(tweesterCapsuleSpaceOdds34)

    thwompCapsulePrice1 = get_capsule_value(thwompCapsulePrice1)
    thwompCapsulePrice2 = get_capsule_value(thwompCapsulePrice2)
    thwompCapsulePrice34 = get_capsule_value(thwompCapsulePrice34)
    thwompCapsuleShopOdds12 = get_capsule_value(thwompCapsuleShopOdds12)
    thwompCapsuleShopOdds34 = get_capsule_value(thwompCapsuleShopOdds34)
    thwompCapsuleSpaceOdds1 = get_capsule_value(thwompCapsuleSpaceOdds1)
    thwompCapsuleSpaceOdds2 = get_capsule_value(thwompCapsuleSpaceOdds2)
    thwompCapsuleSpaceOdds34 = get_capsule_value(thwompCapsuleSpaceOdds34)

    warpCapsulePrice1 = get_capsule_value(warpCapsulePrice1)
    warpCapsulePrice2 = get_capsule_value(warpCapsulePrice2)
    warpCapsulePrice34 = get_capsule_value(warpCapsulePrice34)
    warpCapsuleShopOdds12 = get_capsule_value(warpCapsuleShopOdds12)
    warpCapsuleShopOdds34 = get_capsule_value(warpCapsuleShopOdds34)
    warpCapsuleSpaceOdds1 = get_capsule_value(warpCapsuleSpaceOdds1)
    warpCapsuleSpaceOdds2 = get_capsule_value(warpCapsuleSpaceOdds2)
    warpCapsuleSpaceOdds34 = get_capsule_value(warpCapsuleSpaceOdds34)

    bombCapsulePrice1 = get_capsule_value(bombCapsulePrice1)
    bombCapsulePrice2 = get_capsule_value(bombCapsulePrice2)
    bombCapsulePrice34 = get_capsule_value(bombCapsulePrice34)
    bombCapsuleShopOdds12 = get_capsule_value(bombCapsuleShopOdds12)
    bombCapsuleShopOdds34 = get_capsule_value(bombCapsuleShopOdds34)
    bombCapsuleSpaceOdds1 = get_capsule_value(bombCapsuleSpaceOdds1)
    bombCapsuleSpaceOdds2 = get_capsule_value(bombCapsuleSpaceOdds2)
    bombCapsuleSpaceOdds34 = get_capsule_value(bombCapsuleSpaceOdds34)

    fireballCapsulePrice1 = get_capsule_value(fireballCapsulePrice1)
    fireballCapsulePrice2 = get_capsule_value(fireballCapsulePrice2)
    fireballCapsulePrice34 = get_capsule_value(fireballCapsulePrice34)
    fireballCapsuleShopOdds12 = get_capsule_value(fireballCapsuleShopOdds12)
    fireballCapsuleShopOdds34 = get_capsule_value(fireballCapsuleShopOdds34)
    fireballCapsuleSpaceOdds1 = get_capsule_value(fireballCapsuleSpaceOdds1)
    fireballCapsuleSpaceOdds2 = get_capsule_value(fireballCapsuleSpaceOdds2)
    fireballCapsuleSpaceOdds34 = get_capsule_value(fireballCapsuleSpaceOdds34)

    flowerCapsulePrice1 = get_capsule_value(flowerCapsulePrice1)
    flowerCapsulePrice2 = get_capsule_value(flowerCapsulePrice2)
    flowerCapsulePrice34 = get_capsule_value(flowerCapsulePrice34)
    flowerCapsuleShopOdds12 = get_capsule_value(flowerCapsuleShopOdds12)
    flowerCapsuleShopOdds34 = get_capsule_value(flowerCapsuleShopOdds34)
    flowerCapsuleSpaceOdds1 = get_capsule_value(flowerCapsuleSpaceOdds1)
    flowerCapsuleSpaceOdds2 = get_capsule_value(flowerCapsuleSpaceOdds2)
    flowerCapsuleSpaceOdds34 = get_capsule_value(flowerCapsuleSpaceOdds34)

    eggCapsulePrice1 = get_capsule_value(eggCapsulePrice1)
    eggCapsulePrice2 = get_capsule_value(eggCapsulePrice2)
    eggCapsulePrice34 = get_capsule_value(eggCapsulePrice34)
    eggCapsuleShopOdds12 = get_capsule_value(eggCapsuleShopOdds12)
    eggCapsuleShopOdds34 = get_capsule_value(eggCapsuleShopOdds34)
    eggCapsuleSpaceOdds1 = get_capsule_value(eggCapsuleSpaceOdds1)
    eggCapsuleSpaceOdds2 = get_capsule_value(eggCapsuleSpaceOdds2)
    eggCapsuleSpaceOdds34 = get_capsule_value(eggCapsuleSpaceOdds34)

    vacuumCapsulePrice1 = get_capsule_value(vacuumCapsulePrice1)
    vacuumCapsulePrice2 = get_capsule_value(vacuumCapsulePrice2)
    vacuumCapsulePrice34 = get_capsule_value(vacuumCapsulePrice34)
    vacuumCapsuleShopOdds12 = get_capsule_value(vacuumCapsuleShopOdds12)
    vacuumCapsuleShopOdds34 = get_capsule_value(vacuumCapsuleShopOdds34)
    vacuumCapsuleSpaceOdds1 = get_capsule_value(vacuumCapsuleSpaceOdds1)
    vacuumCapsuleSpaceOdds2 = get_capsule_value(vacuumCapsuleSpaceOdds2)
    vacuumCapsuleSpaceOdds34 = get_capsule_value(vacuumCapsuleSpaceOdds34)

    magicCapsulePrice1 = get_capsule_value(magicCapsulePrice1)
    magicCapsulePrice2 = get_capsule_value(magicCapsulePrice2)
    magicCapsulePrice34 = get_capsule_value(magicCapsulePrice34)
    magicCapsuleShopOdds12 = get_capsule_value(magicCapsuleShopOdds12)
    magicCapsuleShopOdds34 = get_capsule_value(magicCapsuleShopOdds34)
    magicCapsuleSpaceOdds1 = get_capsule_value(magicCapsuleSpaceOdds1)
    magicCapsuleSpaceOdds2 = get_capsule_value(magicCapsuleSpaceOdds2)
    magicCapsuleSpaceOdds34 = get_capsule_value(magicCapsuleSpaceOdds34)

    tripleCapsulePrice1 = get_capsule_value(tripleCapsulePrice1)
    tripleCapsulePrice2 = get_capsule_value(tripleCapsulePrice2)
    tripleCapsulePrice34 = get_capsule_value(tripleCapsulePrice34)
    tripleCapsuleShopOdds12 = get_capsule_value(tripleCapsuleShopOdds12)
    tripleCapsuleShopOdds34 = get_capsule_value(tripleCapsuleShopOdds34)
    tripleCapsuleSpaceOdds1 = get_capsule_value(tripleCapsuleSpaceOdds1)
    tripleCapsuleSpaceOdds2 = get_capsule_value(tripleCapsuleSpaceOdds2)
    tripleCapsuleSpaceOdds34 = get_capsule_value(tripleCapsuleSpaceOdds34)

    koopaCapsulePrice1 = get_capsule_value(koopaCapsulePrice1)
    koopaCapsulePrice2 = get_capsule_value(koopaCapsulePrice2)
    koopaCapsulePrice34 = get_capsule_value(koopaCapsulePrice34)
    koopaCapsuleShopOdds12 = get_capsule_value(koopaCapsuleShopOdds12)
    koopaCapsuleShopOdds34 = get_capsule_value(koopaCapsuleShopOdds34)
    koopaCapsuleSpaceOdds1 = get_capsule_value(koopaCapsuleSpaceOdds1)
    koopaCapsuleSpaceOdds2 = get_capsule_value(koopaCapsuleSpaceOdds2)
    koopaCapsuleSpaceOdds34 = get_capsule_value(koopaCapsuleSpaceOdds34)

    poisonMushroomPrice1 = get_capsule_value(poisonMushroomPrice1)
    poisonMushroomPrice2 = get_capsule_value(poisonMushroomPrice2)
    poisonMushroomPrice34 = get_capsule_value(poisonMushroomPrice34)
    poisonMushroomShopOdds12 = get_capsule_value(poisonMushroomShopOdds12)
    poisonMushroomShopOdds34 = get_capsule_value(poisonMushroomShopOdds34)
    poisonMushroomSpaceOdds1 = get_capsule_value(poisonMushroomSpaceOdds1)
    poisonMushroomSpaceOdds2 = get_capsule_value(poisonMushroomSpaceOdds2)
    poisonMushroomSpaceOdds34 = get_capsule_value(poisonMushroomSpaceOdds34)

    orbBagCapsulePrice1 = get_capsule_value(orbBagCapsulePrice1)
    orbBagCapsulePrice2 = get_capsule_value(orbBagCapsulePrice2)
    orbBagCapsulePrice34 = get_capsule_value(orbBagCapsulePrice34)
    orbBagCapsuleShopOdds12 = get_capsule_value(orbBagCapsuleShopOdds12)
    orbBagCapsuleShopOdds34 = get_capsule_value(orbBagCapsuleShopOdds34)
    orbBagCapsuleSpaceOdds1 = get_capsule_value(orbBagCapsuleSpaceOdds1)
    orbBagCapsuleSpaceOdds2 = get_capsule_value(orbBagCapsuleSpaceOdds2)
    orbBagCapsuleSpaceOdds34 = get_capsule_value(orbBagCapsuleSpaceOdds34)

    mysteryCapsulePrice1 = get_capsule_value(mysteryCapsulePrice1)
    mysteryCapsulePrice2 = get_capsule_value(mysteryCapsulePrice2)
    mysteryCapsulePrice34 = get_capsule_value(mysteryCapsulePrice34)
    mysteryCapsuleShopOdds12 = get_capsule_value(mysteryCapsuleShopOdds12)
    mysteryCapsuleShopOdds34 = get_capsule_value(mysteryCapsuleShopOdds34)
    mysteryCapsuleSpaceOdds1 = get_capsule_value(mysteryCapsuleSpaceOdds1)
    mysteryCapsuleSpaceOdds2 = get_capsule_value(mysteryCapsuleSpaceOdds2)
    mysteryCapsuleSpaceOdds34 = get_capsule_value(mysteryCapsuleSpaceOdds34)

    dkCapsulePrice1 = get_capsule_value(dkCapsulePrice1)
    dkCapsulePrice2 = get_capsule_value(dkCapsulePrice2)
    dkCapsulePrice34 = get_capsule_value(dkCapsulePrice34)
    dkCapsuleShopOdds12 = get_capsule_value(dkCapsuleShopOdds12)
    dkCapsuleShopOdds34 = get_capsule_value(dkCapsuleShopOdds34)
    dkCapsuleSpaceOdds1 = get_capsule_value(dkCapsuleSpaceOdds1)
    dkCapsuleSpaceOdds2 = get_capsule_value(dkCapsuleSpaceOdds2)
    dkCapsuleSpaceOdds34 = get_capsule_value(dkCapsuleSpaceOdds34)

    duelCapsulePrice1 = get_capsule_value(duelCapsulePrice1)
    duelCapsulePrice2 = get_capsule_value(duelCapsulePrice2)
    duelCapsulePrice34 = get_capsule_value(duelCapsulePrice34)
    duelCapsuleShopOdds12 = get_capsule_value(duelCapsuleShopOdds12)
    duelCapsuleShopOdds34 = get_capsule_value(duelCapsuleShopOdds34)
    duelCapsuleSpaceOdds1 = get_capsule_value(duelCapsuleSpaceOdds1)
    duelCapsuleSpaceOdds2 = get_capsule_value(duelCapsuleSpaceOdds2)
    duelCapsuleSpaceOdds34 = get_capsule_value(duelCapsuleSpaceOdds34)

    mushroomCapsuleShopOdds12 = str(mushroomCapsuleShopOdds12)
    mushroomCapsuleShopOdds34 = str(mushroomCapsuleShopOdds34)
    mushroomCapsuleSpaceOdds12 = str(mushroomCapsuleSpaceOdds12)
    mushroomCapsuleSpaceOdds34 = str(mushroomCapsuleSpaceOdds34)
    goldenMushroomCapsulePrice12 = str(goldenMushroomCapsulePrice12)
    goldenMushroomCapsulePrice34 = str(goldenMushroomCapsulePrice34)
    goldenMushroomCapsuleShopOdds12 = str(goldenMushroomCapsuleShopOdds12)
    goldenMushroomCapsuleShopOdds34 = str(goldenMushroomCapsuleShopOdds34)
    goldenMushroomCapsuleSpaceOdds12 = str(goldenMushroomCapsuleSpaceOdds12)
    goldenMushroomCapsuleSpaceOdds34 = str(goldenMushroomCapsuleSpaceOdds34)
    slowMushroomCapsulePrice12 = str(slowMushroomCapsulePrice12)
    slowMushroomCapsulePrice34 = str(slowMushroomCapsulePrice34)
    slowMushroomCapsuleShopOdds12 = str(slowMushroomCapsuleShopOdds12)
    slowMushroomCapsuleShopOdds34 = str(slowMushroomCapsuleShopOdds34)
    slowMushroomCapsuleSpaceOdds12 = str(slowMushroomCapsuleSpaceOdds12)
    slowMushroomCapsuleSpaceOdds34 = str(slowMushroomCapsuleSpaceOdds34)
    metalMushroomCapsulePrice12 = str(metalMushroomCapsulePrice12)
    metalMushroomCapsulePrice34 = str(metalMushroomCapsulePrice34)
    metalMushroomCapsuleShopOdds12 = str(metalMushroomCapsuleShopOdds12)
    metalMushroomCapsuleShopOdds34 = str(metalMushroomCapsuleShopOdds34)
    metalMushroomCapsuleSpaceOdds12 = str(metalMushroomCapsuleSpaceOdds12)
    metalMushroomCapsuleSpaceOdds34 = str(metalMushroomCapsuleSpaceOdds34)
    flutterCapsulePrice12 = str(flutterCapsulePrice12)
    flutterCapsulePrice34 = str(flutterCapsulePrice34)
    flutterCapsuleShopOdds12 = str(flutterCapsuleShopOdds12)
    flutterCapsuleShopOdds34 = str(flutterCapsuleShopOdds34)
    flutterCapsuleSpaceOdds12 = str(flutterCapsuleSpaceOdds12)
    flutterCapsuleSpaceOdds34 = str(flutterCapsuleSpaceOdds34)
    cannonCapsulePrice12 = str(cannonCapsulePrice12)
    cannonCapsulePrice34 = str(cannonCapsulePrice34)
    cannonCapsuleShopOdds12 = str(cannonCapsuleShopOdds12)
    cannonCapsuleShopOdds34 = str(cannonCapsuleShopOdds34)
    cannonCapsuleSpaceOdds12 = str(cannonCapsuleSpaceOdds12)
    cannonCapsuleSpaceOdds34 = str(cannonCapsuleSpaceOdds34)
    snackCapsulePrice12 = str(snackCapsulePrice12)
    snackCapsulePrice34 = str(snackCapsulePrice34)
    snackCapsuleShopOdds12 = str(snackCapsuleShopOdds12)
    snackCapsuleShopOdds34 = str(snackCapsuleShopOdds34)
    snackCapsuleSpaceOdds12 = str(snackCapsuleSpaceOdds12)
    snackCapsuleSpaceOdds34 = str(snackCapsuleSpaceOdds34)
    lakituCapsulePrice12 = str(lakituCapsulePrice12)
    lakituCapsulePrice34 = str(lakituCapsulePrice34)
    lakituCapsuleShopOdds12 = str(lakituCapsuleShopOdds12)
    lakituCapsuleShopOdds34 = str(lakituCapsuleShopOdds34)
    lakituCapsuleSpaceOdds12 = str(lakituCapsuleSpaceOdds12)
    lakituCapsuleSpaceOdds34 = str(lakituCapsuleSpaceOdds34)
    hammerBroCapsulePrice12 = str(hammerBroCapsulePrice12)
    hammerBroCapsulePrice34 = str(hammerBroCapsulePrice34)
    hammerBroCapsuleShopOdds12 = str(hammerBroCapsuleShopOdds12)
    hammerBroCapsuleShopOdds34 = str(hammerBroCapsuleShopOdds34)
    hammerBroCapsuleSpaceOdds12 = str(hammerBroCapsuleSpaceOdds12)
    hammerBroCapsuleSpaceOdds34 = str(hammerBroCapsuleSpaceOdds34)
    piranhaPlantCapsulePrice12 = str(piranhaPlantCapsulePrice12)
    piranhaPlantCapsulePrice34 = str(piranhaPlantCapsulePrice34)
    piranhaPlantCapsuleShopOdds12 = str(piranhaPlantCapsuleShopOdds12)
    piranhaPlantCapsuleShopOdds34 = str(piranhaPlantCapsuleShopOdds34)
    piranhaPlantCapsuleSpaceOdds12 = str(piranhaPlantCapsuleSpaceOdds12)
    piranhaPlantCapsuleSpaceOdds34 = str(piranhaPlantCapsuleSpaceOdds34)
    spearGuyCapsulePrice12 = str(spearGuyCapsulePrice12)
    spearGuyCapsulePrice34 = str(spearGuyCapsulePrice34)
    spearGuyCapsuleShopOdds12 = str(spearGuyCapsuleShopOdds12)
    spearGuyCapsuleShopOdds34 = str(spearGuyCapsuleShopOdds34)
    spearGuyCapsuleSpaceOdds12 = str(spearGuyCapsuleSpaceOdds12)
    spearGuyCapsuleSpaceOdds34 = str(spearGuyCapsuleSpaceOdds34)
    kamekCapsulePrice12 = str(kamekCapsulePrice12)
    kamekCapsulePrice34 = str(kamekCapsulePrice34)
    kamekCapsuleShopOdds12 = str(kamekCapsuleShopOdds12)
    kamekCapsuleShopOdds34 = str(kamekCapsuleShopOdds34)
    kamekCapsuleSpaceOdds12 = str(kamekCapsuleSpaceOdds12)
    kamekCapsuleSpaceOdds34 = str(kamekCapsuleSpaceOdds34)
    toadyCapsulePrice12 = str(toadyCapsulePrice12)
    toadyCapsulePrice34 = str(toadyCapsulePrice34)
    toadyCapsuleShopOdds12 = str(toadyCapsuleShopOdds12)
    toadyCapsuleShopOdds34 = str(toadyCapsuleShopOdds34)
    toadyCapsuleSpaceOdds12 = str(toadyCapsuleSpaceOdds12)
    toadyCapsuleSpaceOdds34 = str(toadyCapsuleSpaceOdds34)
    mrBlizzardCapsulePrice12 = str(mrBlizzardCapsulePrice12)
    mrBlizzardCapsulePrice34 = str(mrBlizzardCapsulePrice34)
    mrBlizzardCapsuleShopOdds12 = str(mrBlizzardCapsuleShopOdds12)
    mrBlizzardCapsuleShopOdds34 = str(mrBlizzardCapsuleShopOdds34)
    mrBlizzardCapsuleSpaceOdds12 = str(mrBlizzardCapsuleSpaceOdds12)
    mrBlizzardCapsuleSpaceOdds34 = str(mrBlizzardCapsuleSpaceOdds34)
    banditCapsulePrice12 = str(banditCapsulePrice12)
    banditCapsulePrice34 = str(banditCapsulePrice34)
    banditCapsuleShopOdds12 = str(banditCapsuleShopOdds12)
    banditCapsuleShopOdds34 = str(banditCapsuleShopOdds34)
    banditCapsuleSpaceOdds12 = str(banditCapsuleSpaceOdds12)
    banditCapsuleSpaceOdds34 = str(banditCapsuleSpaceOdds34)
    pinkBooCapsulePrice12 = str(pinkBooCapsulePrice12)
    pinkBooCapsulePrice34 = str(pinkBooCapsulePrice34)
    pinkBooCapsuleShopOdds12 = str(pinkBooCapsuleShopOdds12)
    pinkBooCapsuleShopOdds34 = str(pinkBooCapsuleShopOdds34)
    pinkBooCapsuleSpaceOdds12 = str(pinkBooCapsuleSpaceOdds12)
    pinkBooCapsuleSpaceOdds34 = str(pinkBooCapsuleSpaceOdds34)
    spinyCapsulePrice12 = str(spinyCapsulePrice12)
    spinyCapsulePrice34 = str(spinyCapsulePrice34)
    spinyCapsuleShopOdds12 = str(spinyCapsuleShopOdds12)
    spinyCapsuleShopOdds34 = str(spinyCapsuleShopOdds34)
    spinyCapsuleSpaceOdds12 = str(spinyCapsuleSpaceOdds12)
    spinyCapsuleSpaceOdds34 = str(spinyCapsuleSpaceOdds34)
    zapCapsulePrice12 = str(zapCapsulePrice12)
    zapCapsulePrice34 = str(zapCapsulePrice34)
    zapCapsuleShopOdds12 = str(zapCapsuleShopOdds12)
    zapCapsuleShopOdds34 = str(zapCapsuleShopOdds34)
    zapCapsuleSpaceOdds12 = str(zapCapsuleSpaceOdds12)
    zapCapsuleSpaceOdds34 = str(zapCapsuleSpaceOdds34)
    tweesterCapsulePrice12 = str(tweesterCapsulePrice12)
    tweesterCapsulePrice34 = str(tweesterCapsulePrice34)
    tweesterCapsuleShopOdds12 = str(tweesterCapsuleShopOdds12)
    tweesterCapsuleShopOdds34 = str(tweesterCapsuleShopOdds34)
    tweesterCapsuleSpaceOdds12 = str(tweesterCapsuleSpaceOdds12)
    tweesterCapsuleSpaceOdds34 = str(tweesterCapsuleSpaceOdds34)
    thwompCapsulePrice12 = str(thwompCapsulePrice12)
    thwompCapsulePrice34 = str(thwompCapsulePrice34)
    thwompCapsuleShopOdds12 = str(thwompCapsuleShopOdds12)
    thwompCapsuleShopOdds34 = str(thwompCapsuleShopOdds34)
    thwompCapsuleSpaceOdds12 = str(thwompCapsuleSpaceOdds12)
    thwompCapsuleSpaceOdds34 = str(thwompCapsuleSpaceOdds34)
    warpCapsulePrice12 = str(warpCapsulePrice12)
    warpCapsulePrice34 = str(warpCapsulePrice34)
    warpCapsuleShopOdds12 = str(warpCapsuleShopOdds12)
    warpCapsuleShopOdds34 = str(warpCapsuleShopOdds34)
    warpCapsuleSpaceOdds12 = str(warpCapsuleSpaceOdds12)
    warpCapsuleSpaceOdds34 = str(warpCapsuleSpaceOdds34)
    bombCapsulePrice12 = str(bombCapsulePrice12)
    bombCapsulePrice34 = str(bombCapsulePrice34)
    bombCapsuleShopOdds12 = str(bombCapsuleShopOdds12)
    bombCapsuleShopOdds34 = str(bombCapsuleShopOdds34)
    bombCapsuleSpaceOdds12 = str(bombCapsuleSpaceOdds12)
    bombCapsuleSpaceOdds34 = str(bombCapsuleSpaceOdds34)
    fireballCapsulePrice12 = str(fireballCapsulePrice12)
    fireballCapsulePrice34 = str(fireballCapsulePrice34)
    fireballCapsuleShopOdds12 = str(fireballCapsuleShopOdds12)
    fireballCapsuleShopOdds34 = str(fireballCapsuleShopOdds34)
    fireballCapsuleSpaceOdds12 = str(fireballCapsuleSpaceOdds12)
    fireballCapsuleSpaceOdds34 = str(fireballCapsuleSpaceOdds34)
    flowerCapsulePrice12 = str(flowerCapsulePrice12)
    flowerCapsulePrice34 = str(flowerCapsulePrice34)
    flowerCapsuleShopOdds12 = str(flowerCapsuleShopOdds12)
    flowerCapsuleShopOdds34 = str(flowerCapsuleShopOdds34)
    flowerCapsuleSpaceOdds12 = str(flowerCapsuleSpaceOdds12)
    flowerCapsuleSpaceOdds34 = str(flowerCapsuleSpaceOdds34)
    eggCapsulePrice12 = str(eggCapsulePrice12)
    eggCapsulePrice34 = str(eggCapsulePrice34)
    eggCapsuleShopOdds12 = str(eggCapsuleShopOdds12)
    eggCapsuleShopOdds34 = str(eggCapsuleShopOdds34)
    eggCapsuleSpaceOdds12 = str(eggCapsuleSpaceOdds12)
    eggCapsuleSpaceOdds34 = str(eggCapsuleSpaceOdds34)
    vacuumCapsulePrice12 = str(vacuumCapsulePrice12)
    vacuumCapsulePrice34 = str(vacuumCapsulePrice34)
    vacuumCapsuleShopOdds12 = str(vacuumCapsuleShopOdds12)
    vacuumCapsuleShopOdds34 = str(vacuumCapsuleShopOdds34)
    vacuumCapsuleSpaceOdds12 = str(vacuumCapsuleSpaceOdds12)
    vacuumCapsuleSpaceOdds34 = str(vacuumCapsuleSpaceOdds34)
    magicCapsulePrice12 = str(magicCapsulePrice12)
    magicCapsulePrice34 = str(magicCapsulePrice34)
    magicCapsuleShopOdds12 = str(magicCapsuleShopOdds12)
    magicCapsuleShopOdds34 = str(magicCapsuleShopOdds34)
    magicCapsuleSpaceOdds12 = str(magicCapsuleSpaceOdds12)
    magicCapsuleSpaceOdds34 = str(magicCapsuleSpaceOdds34)
    tripleCapsulePrice12 = str(tripleCapsulePrice12)
    tripleCapsulePrice34 = str(tripleCapsulePrice34)
    tripleCapsuleShopOdds12 = str(tripleCapsuleShopOdds12)
    tripleCapsuleShopOdds34 = str(tripleCapsuleShopOdds34)
    tripleCapsuleSpaceOdds12 = str(tripleCapsuleSpaceOdds12)
    tripleCapsuleSpaceOdds34 = str(tripleCapsuleSpaceOdds34)
    koopaCapsulePrice12 = str(koopaCapsulePrice12)
    koopaCapsulePrice34 = str(koopaCapsulePrice34)
    koopaCapsuleShopOdds12 = str(koopaCapsuleShopOdds12)
    koopaCapsuleShopOdds34 = str(koopaCapsuleShopOdds34)
    koopaCapsuleSpaceOdds12 = str(koopaCapsuleSpaceOdds12)
    koopaCapsuleSpaceOdds34 = str(koopaCapsuleSpaceOdds34)
    poisonMushroomPrice12 = str(poisonMushroomPrice12)
    poisonMushroomPrice34 = str(poisonMushroomPrice34)
    poisonMushroomShopOdds12 = str(poisonMushroomShopOdds12)
    poisonMushroomShopOdds34 = str(poisonMushroomShopOdds34)
    poisonMushroomSpaceOdds12 = str(poisonMushroomSpaceOdds12)
    poisonMushroomSpaceOdds34 = str(poisonMushroomSpaceOdds34)
    orbBagCapsulePrice12 = str(orbBagCapsulePrice12)
    orbBagCapsulePrice34 = str(orbBagCapsulePrice34)
    orbBagCapsuleShopOdds12 = str(orbBagCapsuleShopOdds12)
    orbBagCapsuleShopOdds34 = str(orbBagCapsuleShopOdds34)
    orbBagCapsuleSpaceOdds12 = str(orbBagCapsuleSpaceOdds12)
    orbBagCapsuleSpaceOdds34 = str(orbBagCapsuleSpaceOdds34)
    mysteryCapsulePrice12 = str(mysteryCapsulePrice12)
    mysteryCapsulePrice34 = str(mysteryCapsulePrice34)
    mysteryCapsuleShopOdds12 = str(mysteryCapsuleShopOdds12)
    mysteryCapsuleShopOdds34 = str(mysteryCapsuleShopOdds34)
    mysteryCapsuleSpaceOdds12 = str(mysteryCapsuleSpaceOdds12)
    mysteryCapsuleSpaceOdds34 = str(mysteryCapsuleSpaceOdds34)
    dkCapsulePrice12 = str(dkCapsulePrice12)
    dkCapsulePrice34 = str(dkCapsulePrice34)
    dkCapsuleShopOdds12 = str(dkCapsuleShopOdds12)
    dkCapsuleShopOdds34 = str(dkCapsuleShopOdds34)
    dkCapsuleSpaceOdds12 = str(dkCapsuleSpaceOdds12)
    dkCapsuleSpaceOdds34 = str(dkCapsuleSpaceOdds34)
    duelCapsulePrice12 = str(duelCapsulePrice12)
    duelCapsulePrice34 = str(duelCapsulePrice34)
    duelCapsuleShopOdds12 = str(duelCapsuleShopOdds12)
    duelCapsuleShopOdds34 = str(duelCapsuleShopOdds34)
    duelCapsuleSpaceOdds12 = str(duelCapsuleSpaceOdds12)
    duelCapsuleSpaceOdds34 = str(duelCapsuleSpaceOdds34)

    shopOdds1 = [
        mushroomCapsuleShopOdds1, goldenMushroomCapsuleShopOdds1, metalMushroomCapsuleShopOdds1,
        slowMushroomCapsuleShopOdds1, flutterCapsuleShopOdds1, cannonCapsuleShopOdds1,
        snackCapsuleShopOdds1, lakituCapsuleShopOdds1, hammerBroCapsuleShopOdds1,
        piranhaPlantCapsuleShopOdds1, spearGuyCapsuleShopOdds1, kamekCapsuleShopOdds1,
        toadyCapsuleShopOdds1, mrBlizzardCapsuleShopOdds1, banditCapsuleShopOdds1,
        pinkBooCapsuleShopOdds1, spinyCapsuleShopOdds1, zapCapsuleShopOdds1,
        tweesterCapsuleShopOdds1, thwompCapsuleShopOdds1, warpCapsuleShopOdds1,
        bombCapsuleShopOdds1, fireballCapsuleShopOdds1, flowerCapsuleShopOdds1,
        eggCapsuleShopOdds1, vacuumCapsuleShopOdds1, magicCapsuleShopOdds1,
        tripleCapsuleShopOdds1, koopaCapsuleShopOdds1, mysteryCapsuleShopOdds1,
        duelCapsuleShopOdds1, dkCapsuleShopOdds1, orbBagCapsuleShopOdds1
    ]

    shopOdds2 = [
        mushroomCapsuleShopOdds2, goldenMushroomCapsuleShopOdds2, metalMushroomCapsuleShopOdds2,
        slowMushroomCapsuleShopOdds2, flutterCapsuleShopOdds2, cannonCapsuleShopOdds2,
        snackCapsuleShopOdds2, lakituCapsuleShopOdds2, hammerBroCapsuleShopOdds2,
        piranhaPlantCapsuleShopOdds2, spearGuyCapsuleShopOdds2, kamekCapsuleShopOdds2,
        toadyCapsuleShopOdds2, mrBlizzardCapsuleShopOdds2, banditCapsuleShopOdds2,
        pinkBooCapsuleShopOdds2, spinyCapsuleShopOdds2, zapCapsuleShopOdds2,
        tweesterCapsuleShopOdds2, thwompCapsuleShopOdds2, warpCapsuleShopOdds2,
        bombCapsuleShopOdds2, fireballCapsuleShopOdds2, flowerCapsuleShopOdds2,
        eggCapsuleShopOdds2, vacuumCapsuleShopOdds2, magicCapsuleShopOdds2,
        tripleCapsuleShopOdds2, koopaCapsuleShopOdds2, mysteryCapsuleShopOdds2,
        duelCapsuleShopOdds2, dkCapsuleShopOdds2, orbBagCapsuleShopOdds2
    ]

    shopOdds34 = [
        mushroomCapsuleShopOdds34, goldenMushroomCapsuleShopOdds34, metalMushroomCapsuleShopOdds34,
        slowMushroomCapsuleShopOdds34, flutterCapsuleShopOdds34, cannonCapsuleShopOdds34,
        snackCapsuleShopOdds34, lakituCapsuleShopOdds34, hammerBroCapsuleShopOdds34,
        piranhaPlantCapsuleShopOdds34, spearGuyCapsuleShopOdds34, kamekCapsuleShopOdds34,
        toadyCapsuleShopOdds34, mrBlizzardCapsuleShopOdds34, banditCapsuleShopOdds34,
        pinkBooCapsuleShopOdds34, spinyCapsuleShopOdds34, zapCapsuleShopOdds34,
        tweesterCapsuleShopOdds34, thwompCapsuleShopOdds34, warpCapsuleShopOdds34,
        bombCapsuleShopOdds34, fireballCapsuleShopOdds34, flowerCapsuleShopOdds34,
        eggCapsuleShopOdds34, vacuumCapsuleShopOdds34, magicCapsuleShopOdds34,
        tripleCapsuleShopOdds34, koopaCapsuleShopOdds34, mysteryCapsuleShopOdds34,
        duelCapsuleShopOdds34, dkCapsuleShopOdds34, orbBagCapsuleShopOdds34
    ]

    spaceOdds1 = [
        mushroomCapsuleSpaceOdds1, goldenMushroomCapsuleSpaceOdds1, metalMushroomCapsuleSpaceOdds1,
        slowMushroomCapsuleSpaceOdds1, flutterCapsuleSpaceOdds1, cannonCapsuleSpaceOdds1,
        snackCapsuleSpaceOdds1, lakituCapsuleSpaceOdds1, hammerBroCapsuleSpaceOdds1,
        piranhaPlantCapsuleSpaceOdds1, spearGuyCapsuleSpaceOdds1, kamekCapsuleSpaceOdds1,
        toadyCapsuleSpaceOdds1, mrBlizzardCapsuleSpaceOdds1, banditCapsuleSpaceOdds1,
        pinkBooCapsuleSpaceOdds1, spinyCapsuleSpaceOdds1, zapCapsuleSpaceOdds1,
        tweesterCapsuleSpaceOdds1, thwompCapsuleSpaceOdds1, warpCapsuleSpaceOdds1,
        bombCapsuleSpaceOdds1, fireballCapsuleSpaceOdds1, flowerCapsuleSpaceOdds1,
        eggCapsuleSpaceOdds1, vacuumCapsuleSpaceOdds1, magicCapsuleSpaceOdds1,
        tripleCapsuleSpaceOdds1, koopaCapsuleSpaceOdds1, mysteryCapsuleSpaceOdds1,
        duelCapsuleSpaceOdds1, dkCapsuleSpaceOdds1, orbBagCapsuleSpaceOdds1
    ]

    spaceOdds2 = [
        mushroomCapsuleSpaceOdds2, goldenMushroomCapsuleSpaceOdds2, metalMushroomCapsuleSpaceOdds2,
        slowMushroomCapsuleSpaceOdds2, flutterCapsuleSpaceOdds2, cannonCapsuleSpaceOdds2,
        snackCapsuleSpaceOdds2, lakituCapsuleSpaceOdds2, hammerBroCapsuleSpaceOdds2,
        piranhaPlantCapsuleSpaceOdds2, spearGuyCapsuleSpaceOdds2, kamekCapsuleSpaceOdds2,
        toadyCapsuleSpaceOdds2, mrBlizzardCapsuleSpaceOdds2, banditCapsuleSpaceOdds2,
        pinkBooCapsuleSpaceOdds2, spinyCapsuleSpaceOdds2, zapCapsuleSpaceOdds2,
        tweesterCapsuleSpaceOdds2, thwompCapsuleSpaceOdds2, warpCapsuleSpaceOdds2,
        bombCapsuleSpaceOdds2, fireballCapsuleSpaceOdds2, flowerCapsuleSpaceOdds2,
        eggCapsuleSpaceOdds2, vacuumCapsuleSpaceOdds2, magicCapsuleSpaceOdds2,
        tripleCapsuleSpaceOdds2, koopaCapsuleSpaceOdds2, mysteryCapsuleSpaceOdds2,
        duelCapsuleSpaceOdds2, dkCapsuleSpaceOdds2, orbBagCapsuleSpaceOdds2
    ]

    spaceOdds34 = [
        mushroomCapsuleSpaceOdds34, goldenMushroomCapsuleSpaceOdds34, metalMushroomCapsuleSpaceOdds34,
        slowMushroomCapsuleSpaceOdds34, flutterCapsuleSpaceOdds34, cannonCapsuleSpaceOdds34,
        snackCapsuleSpaceOdds34, lakituCapsuleSpaceOdds34, hammerBroCapsuleSpaceOdds34,
        piranhaPlantCapsuleSpaceOdds34, spearGuyCapsuleSpaceOdds34, kamekCapsuleSpaceOdds34,
        toadyCapsuleSpaceOdds34, mrBlizzardCapsuleSpaceOdds34, banditCapsuleSpaceOdds34,
        pinkBooCapsuleSpaceOdds34, spinyCapsuleSpaceOdds34, zapCapsuleSpaceOdds34,
        tweesterCapsuleSpaceOdds34, thwompCapsuleSpaceOdds34, warpCapsuleSpaceOdds34,
        bombCapsuleSpaceOdds34, fireballCapsuleSpaceOdds34, flowerCapsuleSpaceOdds34,
        eggCapsuleSpaceOdds34, vacuumCapsuleSpaceOdds34, magicCapsuleSpaceOdds34,
        tripleCapsuleSpaceOdds34, koopaCapsuleSpaceOdds34, mysteryCapsuleSpaceOdds34,
        duelCapsuleSpaceOdds34, dkCapsuleSpaceOdds34, orbBagCapsuleSpaceOdds34
    ]

    prices12 = [
        mushroomCapsulePrice12, goldenMushroomCapsulePrice12, metalMushroomCapsulePrice12,
        slowMushroomCapsulePrice12, flutterCapsulePrice12, cannonCapsulePrice12,
        snackCapsulePrice12, lakituCapsulePrice12, hammerBroCapsulePrice12,
        piranhaPlantCapsulePrice12, spearGuyCapsulePrice12, kamekCapsulePrice12,
        toadyCapsulePrice12, mrBlizzardCapsulePrice12, banditCapsulePrice12,
        pinkBooCapsulePrice12, spinyCapsulePrice12, zapCapsulePrice12,
        tweesterCapsulePrice12, thwompCapsulePrice12, warpCapsulePrice12,
        bombCapsulePrice12, fireballCapsulePrice12, flowerCapsulePrice12,
        eggCapsulePrice12, vacuumCapsulePrice12, magicCapsulePrice12,
        tripleCapsulePrice12, koopaCapsulePrice12, poisonMushroomPrice12,
        orbBagCapsulePrice12, mysteryCapsulePrice12, dkCapsulePrice12,
        duelCapsulePrice12
    ]

    prices34 = [
        mushroomCapsulePrice34, goldenMushroomCapsulePrice34, metalMushroomCapsulePrice34,
        slowMushroomCapsulePrice34, flutterCapsulePrice34, cannonCapsulePrice34,
        snackCapsulePrice34, lakituCapsulePrice34, hammerBroCapsulePrice34,
        piranhaPlantCapsulePrice34, spearGuyCapsulePrice34, kamekCapsulePrice34,
        toadyCapsulePrice34, mrBlizzardCapsulePrice34, banditCapsulePrice34,
        pinkBooCapsulePrice34, spinyCapsulePrice34, zapCapsulePrice34,
        tweesterCapsulePrice34, thwompCapsulePrice34, warpCapsulePrice34,
        bombCapsulePrice34, fireballCapsulePrice34, flowerCapsulePrice34,
        eggCapsulePrice34, vacuumCapsulePrice34, magicCapsulePrice34,
        tripleCapsulePrice34, koopaCapsulePrice34, poisonMushroomPrice34,
        orbBagCapsulePrice34, mysteryCapsulePrice34, dkCapsulePrice34,
        duelCapsulePrice34
    ]
    
    file_path = tkinter.filedialog.asksaveasfilename(defaultextension=".mpt", filetypes=[("MPT files", "*.mpt")])
    if file_path:
        with open(file_path, 'w', newline='') as csvfile:
            writer = csv.writer(csvfile)
            writer.writerow(['Prices1', 'Prices2', 'Prices34', "ShopOdds12", "ShopOdds34", "SpaceOdds1", "SpaceOdds2", "SpaceOdds34"])
            for prices1, prices2, prices34, shopOdds12, shopOdds34, spaceOdds1, spaceOdds2, spaceOdds34 in zip(prices1, prices2, prices34, shopOdds12, shopOdds34, spaceOdds1, spaceOdds2, spaceOdds34):
                writer.writerow([prices1, prices2, prices34, shopOdds12, shopOdds34, spaceOdds1, spaceOdds2, spaceOdds34])
        print("MPT file saved successfully!")
        createDialog("Operation Sucessful", "success", "Presets file saved successfully!.", None)

def loadPresetItems7(hide_custom, mushroomCapsuleShopOdds12, mushroomCapsuleShopOdds34, mushroomCapsuleSpaceOdds1,mushroomCapsuleSpaceOdds2, mushroomCapsuleSpaceOdds34, goldenMushroomCapsulePrice1, goldenMushroomCapsulePrice2, goldenMushroomCapsulePrice34, goldenMushroomCapsuleShopOdds12, goldenMushroomCapsuleShopOdds34, goldenMushroomCapsuleSpaceOdds1, goldenMushroomCapsuleSpaceOdds2, goldenMushroomCapsuleSpaceOdds34, slowMushroomCapsulePrice1, slowMushroomCapsulePrice2, slowMushroomCapsulePrice34, slowMushroomCapsuleShopOdds12, slowMushroomCapsuleShopOdds34, slowMushroomCapsuleSpaceOdds1, slowMushroomCapsuleSpaceOdds2, slowMushroomCapsuleSpaceOdds34, metalMushroomCapsulePrice1, metalMushroomCapsulePrice2, metalMushroomCapsulePrice34, metalMushroomCapsuleShopOdds12, metalMushroomCapsuleShopOdds34, metalMushroomCapsuleSpaceOdds1, metalMushroomCapsuleSpaceOdds2, metalMushroomCapsuleSpaceOdds34, flutterCapsulePrice1, flutterCapsulePrice2, flutterCapsulePrice34, flutterCapsuleShopOdds12, flutterCapsuleShopOdds34, flutterCapsuleSpaceOdds1, flutterCapsuleSpaceOdds2, flutterCapsuleSpaceOdds34, cannonCapsulePrice1, cannonCapsulePrice2, cannonCapsulePrice34, cannonCapsuleShopOdds12, cannonCapsuleShopOdds34, cannonCapsuleSpaceOdds1, cannonCapsuleSpaceOdds2, cannonCapsuleSpaceOdds34, snackCapsulePrice1, snackCapsulePrice2, snackCapsulePrice34, snackCapsuleShopOdds12, snackCapsuleShopOdds34, snackCapsuleSpaceOdds1, snackCapsuleSpaceOdds2, snackCapsuleSpaceOdds34, lakituCapsulePrice1, lakituCapsulePrice2, lakituCapsulePrice34, lakituCapsuleShopOdds12, lakituCapsuleShopOdds34, lakituCapsuleSpaceOdds1, lakituCapsuleSpaceOdds2, lakituCapsuleSpaceOdds34, hammerBroCapsulePrice1, hammerBroCapsulePrice2, hammerBroCapsulePrice34, hammerBroCapsuleShopOdds12, hammerBroCapsuleShopOdds34, hammerBroCapsuleSpaceOdds1, hammerBroCapsuleSpaceOdds2, hammerBroCapsuleSpaceOdds34, piranhaPlantCapsulePrice1, piranhaPlantCapsulePrice2, piranhaPlantCapsulePrice34, piranhaPlantCapsuleShopOdds12, piranhaPlantCapsuleShopOdds34, piranhaPlantCapsuleSpaceOdds1, piranhaPlantCapsuleSpaceOdds2, piranhaPlantCapsuleSpaceOdds34, spearGuyCapsulePrice1, spearGuyCapsulePrice2, spearGuyCapsulePrice34, spearGuyCapsuleShopOdds12, spearGuyCapsuleShopOdds34, spearGuyCapsuleSpaceOdds1, spearGuyCapsuleSpaceOdds2, spearGuyCapsuleSpaceOdds34, kamekCapsulePrice1, kamekCapsulePrice2, kamekCapsulePrice34, kamekCapsuleShopOdds12, kamekCapsuleShopOdds34, kamekCapsuleSpaceOdds1, kamekCapsuleSpaceOdds2, kamekCapsuleSpaceOdds34, toadyCapsulePrice1, toadyCapsulePrice2, toadyCapsulePrice34, toadyCapsuleShopOdds12, toadyCapsuleShopOdds34, toadyCapsuleSpaceOdds1, toadyCapsuleSpaceOdds2, toadyCapsuleSpaceOdds34, mrBlizzardCapsulePrice1, mrBlizzardCapsulePrice2, mrBlizzardCapsulePrice34, mrBlizzardCapsuleShopOdds12, mrBlizzardCapsuleShopOdds34, mrBlizzardCapsuleSpaceOdds1, mrBlizzardCapsuleSpaceOdds2, mrBlizzardCapsuleSpaceOdds34, banditCapsulePrice1, banditCapsulePrice2, banditCapsulePrice34, banditCapsuleShopOdds12, banditCapsuleShopOdds34, banditCapsuleSpaceOdds1, banditCapsuleSpaceOdds2, banditCapsuleSpaceOdds34, pinkBooCapsulePrice1, pinkBooCapsulePrice2, pinkBooCapsulePrice34, pinkBooCapsuleShopOdds12, pinkBooCapsuleShopOdds34, pinkBooCapsuleSpaceOdds1, pinkBooCapsuleSpaceOdds2, pinkBooCapsuleSpaceOdds34, spinyCapsulePrice1, spinyCapsulePrice2, spinyCapsulePrice34, spinyCapsuleShopOdds12, spinyCapsuleShopOdds34, spinyCapsuleSpaceOdds1, spinyCapsuleSpaceOdds2, spinyCapsuleSpaceOdds34, zapCapsulePrice1, zapCapsulePrice2, zapCapsulePrice34, zapCapsuleShopOdds12, zapCapsuleShopOdds34, zapCapsuleSpaceOdds1, zapCapsuleSpaceOdds2, zapCapsuleSpaceOdds34, tweesterCapsulePrice1, tweesterCapsulePrice2, tweesterCapsulePrice34, tweesterCapsuleShopOdds12, tweesterCapsuleShopOdds34, tweesterCapsuleSpaceOdds1, tweesterCapsuleSpaceOdds2, tweesterCapsuleSpaceOdds34, thwompCapsulePrice1, thwompCapsulePrice2, thwompCapsulePrice34, thwompCapsuleShopOdds12, thwompCapsuleShopOdds34, thwompCapsuleSpaceOdds1, thwompCapsuleSpaceOdds2, thwompCapsuleSpaceOdds34, warpCapsulePrice1, warpCapsulePrice2, warpCapsulePrice34, warpCapsuleShopOdds12, warpCapsuleShopOdds34, warpCapsuleSpaceOdds1, warpCapsuleSpaceOdds2, warpCapsuleSpaceOdds34, bombCapsulePrice1, bombCapsulePrice2, bombCapsulePrice34, bombCapsuleShopOdds12, bombCapsuleShopOdds34, bombCapsuleSpaceOdds1, bombCapsuleSpaceOdds2, bombCapsuleSpaceOdds34, fireballCapsulePrice1, fireballCapsulePrice2, fireballCapsulePrice34, fireballCapsuleShopOdds12, fireballCapsuleShopOdds34, fireballCapsuleSpaceOdds1, fireballCapsuleSpaceOdds2, fireballCapsuleSpaceOdds34, flowerCapsulePrice1, flowerCapsulePrice2, flowerCapsulePrice34, flowerCapsuleShopOdds12, flowerCapsuleShopOdds34, flowerCapsuleSpaceOdds1, flowerCapsuleSpaceOdds2, flowerCapsuleSpaceOdds34, eggCapsulePrice1, eggCapsulePrice2, eggCapsulePrice34, eggCapsuleShopOdds12, eggCapsuleShopOdds34, eggCapsuleSpaceOdds1, eggCapsuleSpaceOdds2, eggCapsuleSpaceOdds34, vacuumCapsulePrice1, vacuumCapsulePrice2, vacuumCapsulePrice34, vacuumCapsuleShopOdds12, vacuumCapsuleShopOdds34, vacuumCapsuleSpaceOdds1, vacuumCapsuleSpaceOdds2, vacuumCapsuleSpaceOdds34, magicCapsulePrice1, magicCapsulePrice2, magicCapsulePrice34, magicCapsuleShopOdds12, magicCapsuleShopOdds34, magicCapsuleSpaceOdds1, magicCapsuleSpaceOdds2, magicCapsuleSpaceOdds34, tripleCapsulePrice1, tripleCapsulePrice2, tripleCapsulePrice34, tripleCapsuleShopOdds12, tripleCapsuleShopOdds34, tripleCapsuleSpaceOdds1, tripleCapsuleSpaceOdds2, tripleCapsuleSpaceOdds34, koopaCapsulePrice1, koopaCapsulePrice2, koopaCapsulePrice34, koopaCapsuleShopOdds12, koopaCapsuleShopOdds34, koopaCapsuleSpaceOdds1, koopaCapsuleSpaceOdds2, koopaCapsuleSpaceOdds34, poisonMushroomPrice1, poisonMushroomPrice2, poisonMushroomPrice34, poisonMushroomShopOdds12, poisonMushroomShopOdds34, poisonMushroomSpaceOdds1, poisonMushroomSpaceOdds2, poisonMushroomSpaceOdds34, orbBagCapsulePrice1, orbBagCapsulePrice2, orbBagCapsulePrice34, orbBagCapsuleShopOdds12, orbBagCapsuleShopOdds34, orbBagCapsuleSpaceOdds1, orbBagCapsuleSpaceOdds2, orbBagCapsuleSpaceOdds34, mysteryCapsulePrice1, mysteryCapsulePrice2, mysteryCapsulePrice34, mysteryCapsuleShopOdds12, mysteryCapsuleShopOdds34, mysteryCapsuleSpaceOdds1, mysteryCapsuleSpaceOdds2, mysteryCapsuleSpaceOdds34, dkCapsulePrice1, dkCapsulePrice2, dkCapsulePrice34, dkCapsuleShopOdds12, dkCapsuleShopOdds34, dkCapsuleSpaceOdds1, dkCapsuleSpaceOdds2, dkCapsuleSpaceOdds34, duelCapsulePrice1, duelCapsulePrice2, duelCapsulePrice34, duelCapsuleShopOdds12, duelCapsuleShopOdds34, duelCapsuleSpaceOdds1, duelCapsuleSpaceOdds2, duelCapsuleSpaceOdds34):
    file_path = tkinter.filedialog.askopenfilename(defaultextension=".mpt", filetypes=[("MPT files", "*.mpt")])
    if file_path:
        prices1In = []
        prices2In = []
        prices34In = []
        shopOdds12In = []
        shopOdds34In = []
        spaceOdds1In = []
        spaceOdds2In = []
        spaceOdds34In = []
        with open(file_path, 'r', newline='') as csvfile:
            reader = csv.reader(csvfile)
            next(reader)
            for row in reader:
                prices1In.append(float(row[0]) if row[0] else 0)
                prices2In.append(float(row[1]) if row[1] else 0)
                prices34In.append(float(row[2]) if row[2] else 0)
                shopOdds12In.append(float(row[3]) if row[3] else 0)
                shopOdds34In.append(float(row[4]) if row[4] else 0)
                spaceOdds1In.append(float(row[5]) if row[5] else 0)
                spaceOdds2In.append(float(row[6]) if row[6] else 0)
                spaceOdds34In.append(float(row[7]) if row[7] else 0)

        mushroomCapsulePrice12 = ""
        mushroomCapsulePrice34 = ""
        # Define a list of Entry widget attributes
        shopOdds12 = [
            mushroomCapsuleShopOdds12, goldenMushroomCapsuleShopOdds12, metalMushroomCapsuleShopOdds12,
            slowMushroomCapsuleShopOdds12, flutterCapsuleShopOdds12, cannonCapsuleShopOdds12,
            snackCapsuleShopOdds12, lakituCapsuleShopOdds12, hammerBroCapsuleShopOdds12,
            piranhaPlantCapsuleShopOdds12, spearGuyCapsuleShopOdds12, kamekCapsuleShopOdds12,
            toadyCapsuleShopOdds12, mrBlizzardCapsuleShopOdds12, banditCapsuleShopOdds12,
            pinkBooCapsuleShopOdds12, spinyCapsuleShopOdds12, zapCapsuleShopOdds12,
            tweesterCapsuleShopOdds12, thwompCapsuleShopOdds12, warpCapsuleShopOdds12,
            bombCapsuleShopOdds12, fireballCapsuleShopOdds12, flowerCapsuleShopOdds12,
            eggCapsuleShopOdds12, vacuumCapsuleShopOdds12, magicCapsuleShopOdds12,
            tripleCapsuleShopOdds12, koopaCapsuleShopOdds12, mysteryCapsuleShopOdds12,
            duelCapsuleShopOdds12, dkCapsuleShopOdds12, orbBagCapsuleShopOdds12
        ]
    
        shopOdds34 = [
            mushroomCapsuleShopOdds34, goldenMushroomCapsuleShopOdds34, metalMushroomCapsuleShopOdds34,
            slowMushroomCapsuleShopOdds34, flutterCapsuleShopOdds34, cannonCapsuleShopOdds34,
            snackCapsuleShopOdds34, lakituCapsuleShopOdds34, hammerBroCapsuleShopOdds34,
            piranhaPlantCapsuleShopOdds34, spearGuyCapsuleShopOdds34, kamekCapsuleShopOdds34,
            toadyCapsuleShopOdds34, mrBlizzardCapsuleShopOdds34, banditCapsuleShopOdds34,
            pinkBooCapsuleShopOdds34, spinyCapsuleShopOdds34, zapCapsuleShopOdds34,
            tweesterCapsuleShopOdds34, thwompCapsuleShopOdds34, warpCapsuleShopOdds34,
            bombCapsuleShopOdds34, fireballCapsuleShopOdds34, flowerCapsuleShopOdds34,
            eggCapsuleShopOdds34, vacuumCapsuleShopOdds34, magicCapsuleShopOdds34,
            tripleCapsuleShopOdds34, koopaCapsuleShopOdds34, mysteryCapsuleShopOdds34,
            duelCapsuleShopOdds34, dkCapsuleShopOdds34, orbBagCapsuleShopOdds34
        ]
    
        spaceOdds12 = [
            mushroomCapsuleSpaceOdds12, goldenMushroomCapsuleSpaceOdds12, metalMushroomCapsuleSpaceOdds12,
            slowMushroomCapsuleSpaceOdds12, flutterCapsuleSpaceOdds12, cannonCapsuleSpaceOdds12,
            snackCapsuleSpaceOdds12, lakituCapsuleSpaceOdds12, hammerBroCapsuleSpaceOdds12,
            piranhaPlantCapsuleSpaceOdds12, spearGuyCapsuleSpaceOdds12, kamekCapsuleSpaceOdds12,
            toadyCapsuleSpaceOdds12, mrBlizzardCapsuleSpaceOdds12, banditCapsuleSpaceOdds12,
            pinkBooCapsuleSpaceOdds12, spinyCapsuleSpaceOdds12, zapCapsuleSpaceOdds12,
            tweesterCapsuleSpaceOdds12, thwompCapsuleSpaceOdds12, warpCapsuleSpaceOdds12,
            bombCapsuleSpaceOdds12, fireballCapsuleSpaceOdds12, flowerCapsuleSpaceOdds12,
            eggCapsuleSpaceOdds12, vacuumCapsuleSpaceOdds12, magicCapsuleSpaceOdds12,
            tripleCapsuleSpaceOdds12, koopaCapsuleSpaceOdds12, mysteryCapsuleSpaceOdds12,
            duelCapsuleSpaceOdds12, dkCapsuleSpaceOdds12, orbBagCapsuleSpaceOdds12
        ]
        
        spaceOdds34 = [
            mushroomCapsuleSpaceOdds34, goldenMushroomCapsuleSpaceOdds34, metalMushroomCapsuleSpaceOdds34,
            slowMushroomCapsuleSpaceOdds34, flutterCapsuleSpaceOdds34, cannonCapsuleSpaceOdds34,
            snackCapsuleSpaceOdds34, lakituCapsuleSpaceOdds34, hammerBroCapsuleSpaceOdds34,
            piranhaPlantCapsuleSpaceOdds34, spearGuyCapsuleSpaceOdds34, kamekCapsuleSpaceOdds34,
            toadyCapsuleSpaceOdds34, mrBlizzardCapsuleSpaceOdds34, banditCapsuleSpaceOdds34,
            pinkBooCapsuleSpaceOdds34, spinyCapsuleSpaceOdds34, zapCapsuleSpaceOdds34,
            tweesterCapsuleSpaceOdds34, thwompCapsuleSpaceOdds34, warpCapsuleSpaceOdds34,
            bombCapsuleSpaceOdds34, fireballCapsuleSpaceOdds34, flowerCapsuleSpaceOdds34,
            eggCapsuleSpaceOdds34, vacuumCapsuleSpaceOdds34, magicCapsuleSpaceOdds34,
            tripleCapsuleSpaceOdds34, koopaCapsuleSpaceOdds34, mysteryCapsuleSpaceOdds34,
            duelCapsuleSpaceOdds34, dkCapsuleSpaceOdds34, orbBagCapsuleSpaceOdds34
        ]
    
        prices12 = [
            None, mushroomCapsulePrice12, goldenMushroomCapsulePrice12, metalMushroomCapsulePrice12,
            slowMushroomCapsulePrice12, flutterCapsulePrice12, cannonCapsulePrice12,
            snackCapsulePrice12, lakituCapsulePrice12, hammerBroCapsulePrice12,
            piranhaPlantCapsulePrice12, spearGuyCapsulePrice12, kamekCapsulePrice12,
            toadyCapsulePrice12, mrBlizzardCapsulePrice12, banditCapsulePrice12,
            pinkBooCapsulePrice12, spinyCapsulePrice12, zapCapsulePrice12,
            tweesterCapsulePrice12, thwompCapsulePrice12, warpCapsulePrice12,
            bombCapsulePrice12, fireballCapsulePrice12, flowerCapsulePrice12,
            eggCapsulePrice12, vacuumCapsulePrice12, magicCapsulePrice12,
            tripleCapsulePrice12, koopaCapsulePrice12
        ]
    
        prices34 = [
            None, mushroomCapsulePrice34, goldenMushroomCapsulePrice34, metalMushroomCapsulePrice34,
            slowMushroomCapsulePrice34, flutterCapsulePrice34, cannonCapsulePrice34,
            snackCapsulePrice34, lakituCapsulePrice34, hammerBroCapsulePrice34,
            piranhaPlantCapsulePrice34, spearGuyCapsulePrice34, kamekCapsulePrice34,
            toadyCapsulePrice34, mrBlizzardCapsulePrice34, banditCapsulePrice34,
            pinkBooCapsulePrice34, spinyCapsulePrice34, zapCapsulePrice34,
            tweesterCapsulePrice34, thwompCapsulePrice34, warpCapsulePrice34,
            bombCapsulePrice34, fireballCapsulePrice34, flowerCapsulePrice34,
            eggCapsulePrice34, vacuumCapsulePrice34, magicCapsulePrice34,
            tripleCapsulePrice34, koopaCapsulePrice34
        ]

        if not hide_custom:
            prices1.extend([
                poisonMushroomPrice1,
                orbBagCapsulePrice1, 
                mysteryCapsulePrice1, 
                dkCapsulePrice1,
                duelCapsulePrice1
            ])
            prices2.extend([
                poisonMushroomPrice2,
                orbBagCapsulePrice2, 
                mysteryCapsulePrice2, 
                dkCapsulePrice2,
                duelCapsulePrice2
            ])
            prices34.extend([
                poisonMushroomPrice34,
                orbBagCapsulePrice34, 
                mysteryCapsulePrice34, 
                dkCapsulePrice34,
                duelCapsulePrice34
            ])
            shopOdds12.extend([
                poisonMushroomShopOdds12,
                orbBagCapsuleShopOdds12,
                mysteryCapsuleShopOdds12,
                dkCapsuleShopOdds12,
                duelCapsuleShopOdds12
            ])
            shopOdds34.extend([
                poisonMushroomShopOdds34,
                orbBagCapsuleShopOdds34,
                mysteryCapsuleShopOdds34,
                dkCapsuleShopOdds34,
                duelCapsuleShopOdds34
            ])
            spaceOdds1.extend([
                poisonMushroomSpaceOdds1,
                orbBagCapsuleSpaceOdds1,
                mysteryCapsuleSpaceOdds1,
                dkCapsuleSpaceOdds1,
                duelCapsuleSpaceOdds1
            ])
            spaceOdds2.extend([
                poisonMushroomSpaceOdds2,
                orbBagCapsuleSpaceOdds2,
                mysteryCapsuleSpaceOdds2,
                dkCapsuleSpaceOdds2,
                duelCapsuleSpaceOdds2
            ])
            spaceOdds34.extend([
                poisonMushroomSpaceOdds34,
                orbBagCapsuleSpaceOdds34,
                mysteryCapsuleSpaceOdds34,
                dkCapsuleSpaceOdds34,
                duelCapsuleSpaceOdds34
            ])

        # Update widgets with loaded values
        for index, widget in enumerate(prices1):
            if widget and index < len(prices1In):
                try:
                    widget.delete(0, 'end')
                except:
                    pass
                try:
                    widget.insert(0, int(prices1In[index]))
                except:
                    pass
        for index, widget in enumerate(prices2):
            if widget and index < len(prices2In):
                try:
                    widget.delete(0, 'end')
                except:
                    pass
                try:
                    widget.insert(0, int(prices2In[index]))
                except:
                    pass
        for index, widget in enumerate(prices34):
            if widget and index < len(prices34In):
                try:
                    widget.delete(0, 'end')
                except:
                    pass
                try:
                    widget.insert(0, int(prices34In[index]))
                except:
                    pass
        
        # Update widgets for shop odds
        for index, widget in enumerate(shopOdds12):
            if widget and index < len(shopOdds12In):
                try:
                    widget.delete(0, 'end')
                except:
                    pass
                try:
                    widget.insert(0, int(shopOdds12In[index]))
                except:
                    pass
        for index, widget in enumerate(shopOdds34):
            if widget and index < len(shopOdds34In):
                try:
                    widget.delete(0, 'end')
                except:
                    pass
                try:
                    widget.insert(0, int(shopOdds34In[index]))
                except:
                    pass

        for index, widget in enumerate(spaceOdds1):
            if widget and index < len(spaceOdds1In):
                try:
                    widget.delete(0, 'end')
                except:
                    pass
                try:
                    widget.insert(0, int(spaceOdds1In[index]))
                except:
                    pass

        for index, widget in enumerate(spaceOdds2):
            if widget and index < len(spaceOdds2In):
                try:
                    widget.delete(0, 'end')
                except:
                    pass
                try:
                    widget.insert(0, int(spaceOdds2In[index]))
                except:
                    pass

        for index, widget in enumerate(spaceOdds34):
            if widget and index < len(spaceOdds34In):
                try:
                    widget.delete(0, 'end')
                except:
                    pass
                try:
                    widget.insert(0, int(spaceOdds34In[index]))
                except:
                    pass

        print("MPT file laoded successfully!")
        createDialog("Operation Sucessful", "success", "Presets file saved successfully!.", None)