# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (tabitha@tabs.gay)
# Date: 10/14/2024
# License: MIT
# ============================================

from codes.marioParty4 import *
from functions import *

import csv
import math
import pyperclip

def itemsEvent_mp4ShopDXPrices(miniMushroomEarlyPrice1 = "5", miniMushroomEarlyPrice2 = "5", miniMushroomEarlyPrice34 = "5", miniMushroomMidPrice1 = "5", miniMushroomMidPrice2 = "5", miniMushroomMidPrice34 = "5", miniMushroomLatePrice1 = "5", miniMushroomLatePrice2 = "5", miniMushroomLatePrice34 = "5", megaMushroomEarlyPrice1 = "5", megaMushroomEarlyPrice2 = "5", megaMushroomEarlyPrice34 = "5", megaMushroomMidPrice1 = "5", megaMushroomMidPrice2 = "5", megaMushroomMidPrice34 = "5", megaMushroomLatePrice1 = "5", megaMushroomLatePrice2 = "5", megaMushroomLatePrice34 = "5", superMiniMushroomEarlyPrice1 = "10", superMiniMushroomEarlyPrice2 = "10", superMiniMushroomEarlyPrice34 = "10", superMiniMushroomMidPrice1 = "10", superMiniMushroomMidPrice2 = "10", superMiniMushroomMidPrice34 = "10", superMiniMushroomLatePrice1 = "10", superMiniMushroomLatePrice2 = "10", superMiniMushroomLatePrice34 = "10", superMegaMushroomEarlyPrice1 = "15", superMegaMushroomEarlyPrice2 = "15", superMegaMushroomEarlyPrice34 = "15", superMegaMushroomMidPrice1 = "15", superMegaMushroomMidPrice2 = "15", superMegaMushroomMidPrice34 = "15", superMegaMushroomLatePrice1 = "15", superMegaMushroomLatePrice2 = "15", superMegaMushroomLatePrice34 = "15", miniMegaHammerEarlyPrice1 = "10", miniMegaHammerEarlyPrice2 = "10", miniMegaHammerEarlyPrice34 = "10", miniMegaHammerMidPrice1 = "10", miniMegaHammerMidPrice2 = "10", miniMegaHammerMidPrice34 = "10", miniMegaHammerLatePrice1 = "10", miniMegaHammerLatePrice2 = "10", miniMegaHammerLatePrice34 = "10", warpPipeEarlyPrice1 = "10", warpPipeEarlyPrice2 = "10", warpPipeEarlyPrice34 = "10", warpPipeMidPrice1 = "10", warpPipeMidPrice2 = "10", warpPipeMidPrice34 = "10", warpPipeLatePrice1 = "10", warpPipeLatePrice2 = "10", warpPipeLatePrice34 = "10", swapCardEarlyPrice1 = "15", swapCardEarlyPrice2 = "15", swapCardEarlyPrice34 = "15", swapCardMidPrice1 = "15", swapCardMidPrice2 = "15", swapCardMidPrice34 = "15", swapCardLatePrice1 = "15", swapCardLatePrice2 = "15", swapCardLatePrice34 = "15", sparkyStickerEarlyPrice1 = "5", sparkyStickerEarlyPrice2 = "5", sparkyStickerEarlyPrice34 = "5", sparkyStickerMidPrice1 = "5", sparkyStickerMidPrice2 = "5", sparkyStickerMidPrice34 = "5", sparkyStickerLatePrice1 = "5", sparkyStickerLatePrice2 = "5", sparkyStickerLatePrice34 = "5", gaddlightEarlyPrice1 = "15", gaddlightEarlyPrice2 = "15", gaddlightEarlyPrice34 = "15", gaddlightMidPrice1 = "15", gaddlightMidPrice2 = "15", gaddlightMidPrice34 = "15", gaddlightLatePrice1 = "15", gaddlightLatePrice2 = "15", gaddlightLatePrice34 = "10", chompCallEarlyPrice1 = "10", chompCallEarlyPrice2 = "10", chompCallEarlyPrice34 = "10", chompCallMidPrice1 = "10", chompCallMidPrice2 = "10", chompCallMidPrice34 = "10", chompCallLatePrice1 = "10", chompCallLatePrice2 = "10", chompCallLatePrice34 = "10", bowserSuitEarlyPrice1 = "12", bowserSuitEarlyPrice2 = "12", bowserSuitEarlyPrice34 = "12", bowserSuitMidPrice1 = "12", bowserSuitMidPrice2 = "12", bowserSuitMidPrice34 = "12", bowserSuitLatePrice1 = "12", bowserSuitLatePrice2 = "12", bowserSuitLatePrice34 = "12", crystalBallEarlyPrice1 = "25", crystalBallEarlyPrice2 = "25", crystalBallEarlyPrice34 = "25", crystalBallMidPrice1 = "25", crystalBallMidPrice2 = "25", crystalBallMidPrice34 = "25", crystalBallLatePrice1 = "25", crystalBallLatePrice2 = "25", crystalBallLatePrice34 = "25", magicLampEarlyPrice1 = "30", magicLampEarlyPrice2 = "30", magicLampEarlyPrice34 = "30", magicLampMidPrice1 = "30", magicLampMidPrice2 = "30", magicLampMidPrice34 = "30", magicLampLatePrice1 = "30", magicLampLatePrice2 = "30", magicLampLatePrice34 = "30", itemBagEarlyPrice1 = "30", itemBagEarlyPrice2 = "30", itemBagEarlyPrice34 = "30", itemBagMidPrice1 = "30", itemBagMidPrice2 = "30", itemBagMidPrice34 = "30", itemBagLatePrice1 = "30", itemBagLatePrice2 = "30", itemBagLatePrice34 = "30", mushroomEarlyPrice1 = "5", mushroomEarlyPrice2 = "5", mushroomEarlyPrice34 = "5", mushroomMidPrice1 = "5", mushroomMidPrice2 = "5", mushroomMidPrice34 = "5", mushroomLatePrice1 = "5", mushroomLatePrice2 = "5", mushroomLatePrice34 = "5", goldenMushroomEarlyPrice1 = "10", goldenMushroomEarlyPrice2 = "10", goldenMushroomEarlyPrice34 = "10", goldenMushroomMidPrice1 = "10", goldenMushroomMidPrice2 = "10", goldenMushroomMidPrice34 = "10", goldenMushroomLatePrice1 = "10", goldenMushroomLatePrice2 = "10", goldenMushroomLatePrice34 = "10", reverseMushroomEarlyPrice1 = "10", reverseMushroomEarlyPrice2 = "10", reverseMushroomEarlyPrice34 = "10", reverseMushroomMidPrice1 = "10", reverseMushroomMidPrice2 = "10", reverseMushroomMidPrice34 = "10", reverseMushroomLatePrice1 = "10", reverseMushroomLatePrice2 = "10", reverseMushroomLatePrice34 = "5", poisonMushroomEarlyPrice1 = "5", poisonMushroomEarlyPrice2 = "5", poisonMushroomEarlyPrice34 = "5", poisonMushroomMidPrice1 = "5", poisonMushroomMidPrice2 = "5", poisonMushroomMidPrice34 = "5", poisonMushroomLatePrice1 = "5", poisonMushroomLatePrice2 = "5", poisonMushroomLatePrice34 = "5", triplePoisonMushroomEarlyPrice1 = "15", triplePoisonMushroomEarlyPrice2 = "15", triplePoisonMushroomEarlyPrice34 = "15", triplePoisonMushroomMidPrice1 = "15", triplePoisonMushroomMidPrice2 = "15", triplePoisonMushroomMidPrice34 = "15", triplePoisonMushroomLatePrice1 = "15", triplePoisonMushroomLatePrice2 = "15", triplePoisonMushroomLatePrice34 = "15", celluarShopperEarlyPrice1 = "5", celluarShopperEarlyPrice2 = "5", celluarShopperEarlyPrice34 = "5", celluarShopperMidPrice1 = "5", celluarShopperMidPrice2 = "5", celluarShopperMidPrice34 = "5", celluarShopperLatePrice1 = "5", celluarShopperLatePrice2 = "5", celluarShopperLatePrice34 = "5", skeletonKeyEarlyPrice1 = "5", skeletonKeyEarlyPrice2 = "5", skeletonKeyEarlyPrice34 = "5", skeletonKeyMidPrice1 = "5", skeletonKeyMidPrice2 = "5", skeletonKeyMidPrice34 = "5", skeletonKeyLatePrice1 = "5", skeletonKeyLatePrice2 = "5", skeletonKeyLatePrice34 = "5", plunderChestEarlyPrice1 = "15", plunderChestEarlyPrice2 = "15", plunderChestEarlyPrice34 = "15", plunderChestMidPrice1 = "15", plunderChestMidPrice2 = "15", plunderChestMidPrice34 = "15", plunderChestLatePrice1 = "15", plunderChestLatePrice2 = "15", plunderChestLatePrice34 = "15", gaddbrushEarlyPrice1 = "15", gaddbrushEarlyPrice2 = "15", gaddbrushEarlyPrice34 = "15", gaddbrushMidPrice1 = "15", gaddbrushMidPrice2 = "15", gaddbrushMidPrice34 = "15", gaddbrushLatePrice1 = "15", gaddbrushLatePrice2 = "15", gaddbrushLatePrice34 = "15", warpBlockEarlyPrice1 = "5", warpBlockEarlyPrice2 = "5", warpBlockEarlyPrice34 = "5", warpBlockMidPrice1 = "5", warpBlockMidPrice2 = "5", warpBlockMidPrice34 = "5", warpBlockLatePrice1 = "5", warpBlockLatePrice2 = "5", warpBlockLatePrice34 = "5", flyGuyEarlyPrice1 = "12", flyGuyEarlyPrice2 = "12", flyGuyEarlyPrice34 = "12", flyGuyMidPrice1 = "12", flyGuyMidPrice2 = "12", flyGuyMidPrice34 = "12", flyGuyLatePrice1 = "12", flyGuyLatePrice2 = "12", flyGuyLatePrice34 = "12", plusBlockEarlyPrice1 = "10", plusBlockEarlyPrice2 = "10", plusBlockEarlyPrice34 = "10", plusBlockMidPrice1 = "10", plusBlockMidPrice2 = "10", plusBlockMidPrice34 = "10", plusBlockLatePrice1 = "10", plusBlockLatePrice2 = "10", plusBlockLatePrice34 = "10", minusBlockEarlyPrice1 = "10", minusBlockEarlyPrice2 = "10", minusBlockEarlyPrice34 = "10", minusBlockMidPrice1 = "10", minusBlockMidPrice2 = "10", minusBlockMidPrice34 = "10", minusBlockLatePrice1 = "10", minusBlockLatePrice2 = "10", minusBlockLatePrice34 = "10", speedBlockEarlyPrice1 = "12", speedBlockEarlyPrice2 = "12", speedBlockEarlyPrice34 = "12", speedBlockMidPrice1 = "12", speedBlockMidPrice2 = "12", speedBlockMidPrice34 = "12", speedBlockLatePrice1 = "12", speedBlockLatePrice2 = "12", speedBlockLatePrice34 = "12", slowBlockEarlyPrice1 = "12", slowBlockEarlyPrice2 = "12", slowBlockEarlyPrice34 = "12", slowBlockMidPrice1 = "12", slowBlockMidPrice2 = "12", slowBlockMidPrice34 = "12", slowBlockLatePrice1 = "12", slowBlockLatePrice2 = "12", slowBlockLatePrice34 = "12", bowserPhoneEarlyPrice1 = "10", bowserPhoneEarlyPrice2 = "10", bowserPhoneEarlyPrice34 = "10", bowserPhoneMidPrice1 = "10", bowserPhoneMidPrice2 = "10", bowserPhoneMidPrice34 = "10", bowserPhoneLatePrice1 = "10", bowserPhoneLatePrice2 = "10", bowserPhoneLatePrice34 = "10", doubleDipEarlyPrice1 = "12", doubleDipEarlyPrice2 = "12", doubleDipEarlyPrice34 = "12", doubleDipMidPrice1 = "12", doubleDipMidPrice2 = "12", doubleDipMidPrice34 = "12", doubleDipLatePrice1 = "12", doubleDipLatePrice2 = "12", doubleDipLatePrice34 = "12", hiddenBlockCardEarlyPrice1 = "40", hiddenBlockCardEarlyPrice2 = "40", hiddenBlockCardEarlyPrice34 = "40", hiddenBlockCardMidPrice1 = "40", hiddenBlockCardMidPrice2 = "40", hiddenBlockCardMidPrice34 = "40", hiddenBlockCardLatePrice1 = "40", hiddenBlockCardLatePrice2 = "40", hiddenBlockCardLatePrice34 = "40", barterBoxEarlyPrice1 = "40", barterBoxEarlyPrice2 = "40", barterBoxEarlyPrice34 = "40", barterBoxMidPrice1 = "40", barterBoxMidPrice2 = "40", barterBoxMidPrice34 = "40", barterBoxLatePrice1 = "40", barterBoxLatePrice2 = "40", barterBoxLatePrice34 = "40", superWarpPipeEarlyPrice1 = "40", superWarpPipeEarlyPrice2 = "40", superWarpPipeEarlyPrice34 = "40", superWarpPipeMidPrice1 = "40", superWarpPipeMidPrice2 = "40", superWarpPipeMidPrice34 = "40", superWarpPipeLatePrice1 = "40", superWarpPipeLatePrice2 = "40", superWarpPipeLatePrice34 = "40", chanceTimeCharmEarlyPrice1 = "40", chanceTimeCharmEarlyPrice2 = "40", chanceTimeCharmEarlyPrice34 = "40", chanceTimeCharmMidPrice1 = "40", chanceTimeCharmMidPrice2 = "40", chanceTimeCharmMidPrice34 = "40", chanceTimeCharmLatePrice1 = "40", chanceTimeCharmLatePrice2 = "40", chanceTimeCharmLatePrice34 = "40", wackyWatchEarlyPrice1 = "100", wackyWatchEarlyPrice2 = "100", wackyWatchEarlyPrice34 = "100", wackyWatchMidPrice1 = "100", wackyWatchMidPrice2 = "100", wackyWatchMidPrice34 = "100", wackyWatchLatePrice1 = "100", wackyWatchLatePrice2 = "100", wackyWatchLatePrice34 = "100"):

    # Mini Mushroom
    miniMushroomEarlyPrice1 = get_capsule_value(miniMushroomEarlyPrice1) or "5"
    miniMushroomEarlyPrice2 = get_capsule_value(miniMushroomEarlyPrice2) or "5"
    miniMushroomEarlyPrice34 = get_capsule_value(miniMushroomEarlyPrice34) or "5"
    miniMushroomMidPrice1 = get_capsule_value(miniMushroomMidPrice1) or "5"
    miniMushroomMidPrice2 = get_capsule_value(miniMushroomMidPrice2) or "5"
    miniMushroomMidPrice34 = get_capsule_value(miniMushroomMidPrice34) or "5"
    miniMushroomLatePrice1 = get_capsule_value(miniMushroomLatePrice1) or "5"
    miniMushroomLatePrice2 = get_capsule_value(miniMushroomLatePrice2) or "5"
    miniMushroomLatePrice34 = get_capsule_value(miniMushroomLatePrice34) or "5"
    
    # Mega Mushroom
    megaMushroomEarlyPrice1 = get_capsule_value(megaMushroomEarlyPrice1) or "5"
    megaMushroomEarlyPrice2 = get_capsule_value(megaMushroomEarlyPrice2) or "5"
    megaMushroomEarlyPrice34 = get_capsule_value(megaMushroomEarlyPrice34) or "5"
    megaMushroomMidPrice1 = get_capsule_value(megaMushroomMidPrice1) or "5"
    megaMushroomMidPrice2 = get_capsule_value(megaMushroomMidPrice2) or "5"
    megaMushroomMidPrice34 = get_capsule_value(megaMushroomMidPrice34) or "5"
    megaMushroomLatePrice1 = get_capsule_value(megaMushroomLatePrice1) or "5"
    megaMushroomLatePrice2 = get_capsule_value(megaMushroomLatePrice2) or "5"
    megaMushroomLatePrice34 = get_capsule_value(megaMushroomLatePrice34) or "5"

    # Super Mini Mushroom
    superMiniMushroomEarlyPrice1 = get_capsule_value(superMiniMushroomEarlyPrice1) or "10"
    superMiniMushroomEarlyPrice2 = get_capsule_value(superMiniMushroomEarlyPrice2) or "10"
    superMiniMushroomEarlyPrice34 = get_capsule_value(superMiniMushroomEarlyPrice34) or "10"
    superMiniMushroomMidPrice1 = get_capsule_value(superMiniMushroomMidPrice1) or "10"
    superMiniMushroomMidPrice2 = get_capsule_value(superMiniMushroomMidPrice2) or "10"
    superMiniMushroomMidPrice34 = get_capsule_value(superMiniMushroomMidPrice34) or "10"
    superMiniMushroomLatePrice1 = get_capsule_value(superMiniMushroomLatePrice1) or "10"
    superMiniMushroomLatePrice2 = get_capsule_value(superMiniMushroomLatePrice2) or "10"
    superMiniMushroomLatePrice34 = get_capsule_value(superMiniMushroomLatePrice34) or "10"

    # Super Mega Mushroom
    superMegaMushroomEarlyPrice1 = get_capsule_value(superMegaMushroomEarlyPrice1) or "15"
    superMegaMushroomEarlyPrice2 = get_capsule_value(superMegaMushroomEarlyPrice2) or "15"
    superMegaMushroomEarlyPrice34 = get_capsule_value(superMegaMushroomEarlyPrice34) or "15"
    superMegaMushroomMidPrice1 = get_capsule_value(superMegaMushroomMidPrice1) or "15"
    superMegaMushroomMidPrice2 = get_capsule_value(superMegaMushroomMidPrice2) or "15"
    superMegaMushroomMidPrice34 = get_capsule_value(superMegaMushroomMidPrice34) or "15"
    superMegaMushroomLatePrice1 = get_capsule_value(superMegaMushroomLatePrice1) or "15"
    superMegaMushroomLatePrice2 = get_capsule_value(superMegaMushroomLatePrice2) or "15"
    superMegaMushroomLatePrice34 = get_capsule_value(superMegaMushroomLatePrice34) or "15"

    # Mini Mega Hammer
    miniMegaHammerEarlyPrice1 = get_capsule_value(miniMegaHammerEarlyPrice1) or "10"
    miniMegaHammerEarlyPrice2 = get_capsule_value(miniMegaHammerEarlyPrice2) or "10"
    miniMegaHammerEarlyPrice34 = get_capsule_value(miniMegaHammerEarlyPrice34) or "10"
    miniMegaHammerMidPrice1 = get_capsule_value(miniMegaHammerMidPrice1) or "10"
    miniMegaHammerMidPrice2 = get_capsule_value(miniMegaHammerMidPrice2) or "10"
    miniMegaHammerMidPrice34 = get_capsule_value(miniMegaHammerMidPrice34) or "10"
    miniMegaHammerLatePrice1 = get_capsule_value(miniMegaHammerLatePrice1) or "10"
    miniMegaHammerLatePrice2 = get_capsule_value(miniMegaHammerLatePrice2) or "10"
    miniMegaHammerLatePrice34 = get_capsule_value(miniMegaHammerLatePrice34) or "10"

    # Warp Pipe
    warpPipeEarlyPrice1 = get_capsule_value(warpPipeEarlyPrice1) or "10"
    warpPipeEarlyPrice2 = get_capsule_value(warpPipeEarlyPrice2) or "10"
    warpPipeEarlyPrice34 = get_capsule_value(warpPipeEarlyPrice34) or "10"
    warpPipeMidPrice1 = get_capsule_value(warpPipeMidPrice1) or "10"
    warpPipeMidPrice2 = get_capsule_value(warpPipeMidPrice2) or "10"
    warpPipeMidPrice34 = get_capsule_value(warpPipeMidPrice34) or "10"
    warpPipeLatePrice1 = get_capsule_value(warpPipeLatePrice1) or "10"
    warpPipeLatePrice2 = get_capsule_value(warpPipeLatePrice2) or "10"
    warpPipeLatePrice34 = get_capsule_value(warpPipeLatePrice34) or "10"

    # Swap Card
    swapCardEarlyPrice1 = get_capsule_value(swapCardEarlyPrice1) or "15"
    swapCardEarlyPrice2 = get_capsule_value(swapCardEarlyPrice2) or "15"
    swapCardEarlyPrice34 = get_capsule_value(swapCardEarlyPrice34) or "15"
    swapCardMidPrice1 = get_capsule_value(swapCardMidPrice1) or "15"
    swapCardMidPrice2 = get_capsule_value(swapCardMidPrice2) or "15"
    swapCardMidPrice34 = get_capsule_value(swapCardMidPrice34) or "15"
    swapCardLatePrice1 = get_capsule_value(swapCardLatePrice1) or "15"
    swapCardLatePrice2 = get_capsule_value(swapCardLatePrice2) or "15"
    swapCardLatePrice34 = get_capsule_value(swapCardLatePrice34) or "15"

    # Sparky Sticker
    sparkyStickerEarlyPrice1 = get_capsule_value(sparkyStickerEarlyPrice1) or "5"
    sparkyStickerEarlyPrice2 = get_capsule_value(sparkyStickerEarlyPrice2) or "5"
    sparkyStickerEarlyPrice34 = get_capsule_value(sparkyStickerEarlyPrice34) or "5"
    sparkyStickerMidPrice1 = get_capsule_value(sparkyStickerMidPrice1) or "5"
    sparkyStickerMidPrice2 = get_capsule_value(sparkyStickerMidPrice2) or "5"
    sparkyStickerMidPrice34 = get_capsule_value(sparkyStickerMidPrice34) or "5"
    sparkyStickerLatePrice1 = get_capsule_value(sparkyStickerLatePrice1) or "5"
    sparkyStickerLatePrice2 = get_capsule_value(sparkyStickerLatePrice2) or "5"
    sparkyStickerLatePrice34 = get_capsule_value(sparkyStickerLatePrice34) or "5"

    # Gaddlight
    gaddlightEarlyPrice1 = get_capsule_value(gaddlightEarlyPrice1) or "15"
    gaddlightEarlyPrice2 = get_capsule_value(gaddlightEarlyPrice2) or "15"
    gaddlightEarlyPrice34 = get_capsule_value(gaddlightEarlyPrice34) or "15"
    gaddlightMidPrice1 = get_capsule_value(gaddlightMidPrice1) or "15"
    gaddlightMidPrice2 = get_capsule_value(gaddlightMidPrice2) or "15"
    gaddlightMidPrice34 = get_capsule_value(gaddlightMidPrice34) or "15"
    gaddlightLatePrice1 = get_capsule_value(gaddlightLatePrice1) or "15"
    gaddlightLatePrice2 = get_capsule_value(gaddlightLatePrice2) or "15"
    gaddlightLatePrice34 = get_capsule_value(gaddlightLatePrice34) or "15"

    # Chomp Call
    chompCallEarlyPrice1 = get_capsule_value(chompCallEarlyPrice1) or "10"
    chompCallEarlyPrice2 = get_capsule_value(chompCallEarlyPrice2) or "10"
    chompCallEarlyPrice34 = get_capsule_value(chompCallEarlyPrice34) or "10"
    chompCallMidPrice1 = get_capsule_value(chompCallMidPrice1) or "10"
    chompCallMidPrice2 = get_capsule_value(chompCallMidPrice2) or "10"
    chompCallMidPrice34 = get_capsule_value(chompCallMidPrice34) or "10"
    chompCallLatePrice1 = get_capsule_value(chompCallLatePrice1) or "10"
    chompCallLatePrice2 = get_capsule_value(chompCallLatePrice2) or "10"
    chompCallLatePrice34 = get_capsule_value(chompCallLatePrice34) or "10"

    # Bowser Suit
    bowserSuitEarlyPrice1 = get_capsule_value(bowserSuitEarlyPrice1) or "12"
    bowserSuitEarlyPrice2 = get_capsule_value(bowserSuitEarlyPrice2) or "12"
    bowserSuitEarlyPrice34 = get_capsule_value(bowserSuitEarlyPrice34) or "12"
    bowserSuitMidPrice1 = get_capsule_value(bowserSuitMidPrice1) or "12"
    bowserSuitMidPrice2 = get_capsule_value(bowserSuitMidPrice2) or "12"
    bowserSuitMidPrice34 = get_capsule_value(bowserSuitMidPrice34) or "12"
    bowserSuitLatePrice1 = get_capsule_value(bowserSuitLatePrice1) or "12"
    bowserSuitLatePrice2 = get_capsule_value(bowserSuitLatePrice2) or "12"
    bowserSuitLatePrice34 = get_capsule_value(bowserSuitLatePrice34) or "12"

    # Crystal Ball
    crystalBallEarlyPrice1 = get_capsule_value(crystalBallEarlyPrice1) or "25"
    crystalBallEarlyPrice2 = get_capsule_value(crystalBallEarlyPrice2) or "25"
    crystalBallEarlyPrice34 = get_capsule_value(crystalBallEarlyPrice34) or "25"
    crystalBallMidPrice1 = get_capsule_value(crystalBallMidPrice1) or "25"
    crystalBallMidPrice2 = get_capsule_value(crystalBallMidPrice2) or "25"
    crystalBallMidPrice34 = get_capsule_value(crystalBallMidPrice34) or "25"
    crystalBallLatePrice1 = get_capsule_value(crystalBallLatePrice1) or "25"
    crystalBallLatePrice2 = get_capsule_value(crystalBallLatePrice2) or "25"
    crystalBallLatePrice34 = get_capsule_value(crystalBallLatePrice34) or "25"

    # Magic Lamp
    magicLampEarlyPrice1 = get_capsule_value(magicLampEarlyPrice1) or "30"
    magicLampEarlyPrice2 = get_capsule_value(magicLampEarlyPrice2) or "30"
    magicLampEarlyPrice34 = get_capsule_value(magicLampEarlyPrice34) or "30"
    magicLampMidPrice1 = get_capsule_value(magicLampMidPrice1) or "30"
    magicLampMidPrice2 = get_capsule_value(magicLampMidPrice2) or "30"
    magicLampMidPrice34 = get_capsule_value(magicLampMidPrice34) or "30"
    magicLampLatePrice1 = get_capsule_value(magicLampLatePrice1) or "30"
    magicLampLatePrice2 = get_capsule_value(magicLampLatePrice2) or "30"
    magicLampLatePrice34 = get_capsule_value(magicLampLatePrice34) or "30"

    # Item Bag
    itemBagEarlyPrice1 = get_capsule_value(itemBagEarlyPrice1) or "30"
    itemBagEarlyPrice2 = get_capsule_value(itemBagEarlyPrice2) or "30"
    itemBagEarlyPrice34 = get_capsule_value(itemBagEarlyPrice34) or "30"
    itemBagMidPrice1 = get_capsule_value(itemBagMidPrice1) or "30"
    itemBagMidPrice2 = get_capsule_value(itemBagMidPrice2) or "30"
    itemBagMidPrice34 = get_capsule_value(itemBagMidPrice34) or "30"
    itemBagLatePrice1 = get_capsule_value(itemBagLatePrice1) or "30"
    itemBagLatePrice2 = get_capsule_value(itemBagLatePrice2) or "30"
    itemBagLatePrice34 = get_capsule_value(itemBagLatePrice34) or "30"

    # Mushroom: DX
    mushroomEarlyPrice1 = get_capsule_value(mushroomEarlyPrice1) or "5"
    mushroomEarlyPrice2 = get_capsule_value(mushroomEarlyPrice2) or "5"
    mushroomEarlyPrice34 = get_capsule_value(mushroomEarlyPrice34) or "5"
    mushroomMidPrice1 = get_capsule_value(mushroomMidPrice1) or "5"
    mushroomMidPrice2 = get_capsule_value(mushroomMidPrice2) or "5"
    mushroomMidPrice34 = get_capsule_value(mushroomMidPrice34) or "5"
    mushroomLatePrice1 = get_capsule_value(mushroomLatePrice1) or "5"
    mushroomLatePrice2 = get_capsule_value(mushroomLatePrice2) or "5"
    mushroomLatePrice34 = get_capsule_value(mushroomLatePrice34) or "5"

    # Golden Mushroom: DX
    goldenMushroomEarlyPrice1 = get_capsule_value(goldenMushroomEarlyPrice1) or "10"
    goldenMushroomEarlyPrice2 = get_capsule_value(goldenMushroomEarlyPrice2) or "10"
    goldenMushroomEarlyPrice34 = get_capsule_value(goldenMushroomEarlyPrice34) or "10"
    goldenMushroomMidPrice1 = get_capsule_value(goldenMushroomMidPrice1) or "10"
    goldenMushroomMidPrice2 = get_capsule_value(goldenMushroomMidPrice2) or "10"
    goldenMushroomMidPrice34 = get_capsule_value(goldenMushroomMidPrice34) or "10"
    goldenMushroomLatePrice1 = get_capsule_value(goldenMushroomLatePrice1) or "10"
    goldenMushroomLatePrice2 = get_capsule_value(goldenMushroomLatePrice2) or "10"
    goldenMushroomLatePrice34 = get_capsule_value(goldenMushroomLatePrice34) or "10"

    # Reverse Mushroom: DX
    reverseMushroomEarlyPrice1 = get_capsule_value(reverseMushroomEarlyPrice1) or "15"
    reverseMushroomEarlyPrice2 = get_capsule_value(reverseMushroomEarlyPrice2) or "15"
    reverseMushroomEarlyPrice34 = get_capsule_value(reverseMushroomEarlyPrice34) or "15"
    reverseMushroomMidPrice1 = get_capsule_value(reverseMushroomMidPrice1) or "15"
    reverseMushroomMidPrice2 = get_capsule_value(reverseMushroomMidPrice2) or "15"
    reverseMushroomMidPrice34 = get_capsule_value(reverseMushroomMidPrice34) or "15"
    reverseMushroomLatePrice1 = get_capsule_value(reverseMushroomLatePrice1) or "15"
    reverseMushroomLatePrice2 = get_capsule_value(reverseMushroomLatePrice2) or "15"
    reverseMushroomLatePrice34 = get_capsule_value(reverseMushroomLatePrice34) or "15"

    # Poison Mushroom: DX
    poisonMushroomEarlyPrice1 = get_capsule_value(poisonMushroomEarlyPrice1) or "5"
    poisonMushroomEarlyPrice2 = get_capsule_value(poisonMushroomEarlyPrice2) or "5"
    poisonMushroomEarlyPrice34 = get_capsule_value(poisonMushroomEarlyPrice34) or "5"
    poisonMushroomMidPrice1 = get_capsule_value(poisonMushroomMidPrice1) or "5"
    poisonMushroomMidPrice2 = get_capsule_value(poisonMushroomMidPrice2) or "5"
    poisonMushroomMidPrice34 = get_capsule_value(poisonMushroomMidPrice34) or "5"
    poisonMushroomLatePrice1 = get_capsule_value(poisonMushroomLatePrice1) or "5"
    poisonMushroomLatePrice2 = get_capsule_value(poisonMushroomLatePrice2) or "5"
    poisonMushroomLatePrice34 = get_capsule_value(poisonMushroomLatePrice34) or "5"
    
    # Bowser Phone: DX
    bowserPhoneEarlyPrice1 = get_capsule_value(bowserPhoneEarlyPrice1) or "10"
    bowserPhoneEarlyPrice2 = get_capsule_value(bowserPhoneEarlyPrice2) or "10"
    bowserPhoneEarlyPrice34 = get_capsule_value(bowserPhoneEarlyPrice34) or "10"
    bowserPhoneMidPrice1 = get_capsule_value(bowserPhoneMidPrice1) or "10"
    bowserPhoneMidPrice2 = get_capsule_value(bowserPhoneMidPrice2) or "10"
    bowserPhoneMidPrice34 = get_capsule_value(bowserPhoneMidPrice34) or "10"
    bowserPhoneLatePrice1 = get_capsule_value(bowserPhoneLatePrice1) or "10"
    bowserPhoneLatePrice2 = get_capsule_value(bowserPhoneLatePrice2) or "10"
    bowserPhoneLatePrice34 = get_capsule_value(bowserPhoneLatePrice34) or "10"

    # Triple Poison Mushroom: DX
    triplePoisonMushroomEarlyPrice1 = get_capsule_value(triplePoisonMushroomEarlyPrice1) or "15"
    triplePoisonMushroomEarlyPrice2 = get_capsule_value(triplePoisonMushroomEarlyPrice2) or "15"
    triplePoisonMushroomEarlyPrice34 = get_capsule_value(triplePoisonMushroomEarlyPrice34) or "15"
    triplePoisonMushroomMidPrice1 = get_capsule_value(triplePoisonMushroomMidPrice1) or "15"
    triplePoisonMushroomMidPrice2 = get_capsule_value(triplePoisonMushroomMidPrice2) or "15"
    triplePoisonMushroomMidPrice34 = get_capsule_value(triplePoisonMushroomMidPrice34) or "15"
    triplePoisonMushroomLatePrice1 = get_capsule_value(triplePoisonMushroomLatePrice1) or "15"
    triplePoisonMushroomLatePrice2 = get_capsule_value(triplePoisonMushroomLatePrice2) or "15"
    triplePoisonMushroomLatePrice34 = get_capsule_value(triplePoisonMushroomLatePrice34) or "15"

    # Celluar Shopper: DX
    celluarShopperEarlyPrice1 = get_capsule_value(celluarShopperEarlyPrice1) or "5"
    celluarShopperEarlyPrice2 = get_capsule_value(celluarShopperEarlyPrice2) or "5"
    celluarShopperEarlyPrice34 = get_capsule_value(celluarShopperEarlyPrice34) or "5"
    celluarShopperMidPrice1 = get_capsule_value(celluarShopperMidPrice1) or "5"
    celluarShopperMidPrice2 = get_capsule_value(celluarShopperMidPrice2) or "5"
    celluarShopperMidPrice34 = get_capsule_value(celluarShopperMidPrice34) or "5"
    celluarShopperLatePrice1 = get_capsule_value(celluarShopperLatePrice1) or "5"
    celluarShopperLatePrice2 = get_capsule_value(celluarShopperLatePrice2) or "5"
    celluarShopperLatePrice34 = get_capsule_value(celluarShopperLatePrice34) or "5"

    # Skeleton Key: DX
    skeletonKeyEarlyPrice1 = get_capsule_value(skeletonKeyEarlyPrice1) or "5"
    skeletonKeyEarlyPrice2 = get_capsule_value(skeletonKeyEarlyPrice2) or "5"
    skeletonKeyEarlyPrice34 = get_capsule_value(skeletonKeyEarlyPrice34) or "5"
    skeletonKeyMidPrice1 = get_capsule_value(skeletonKeyMidPrice1) or "5"
    skeletonKeyMidPrice2 = get_capsule_value(skeletonKeyMidPrice2) or "5"
    skeletonKeyMidPrice34 = get_capsule_value(skeletonKeyMidPrice34) or "5"
    skeletonKeyLatePrice1 = get_capsule_value(skeletonKeyLatePrice1) or "5"
    skeletonKeyLatePrice2 = get_capsule_value(skeletonKeyLatePrice2) or "5"
    skeletonKeyLatePrice34 = get_capsule_value(skeletonKeyLatePrice34) or "5"

    # Plunder Chest: DX
    plunderChestEarlyPrice1 = get_capsule_value(plunderChestEarlyPrice1) or "15"
    plunderChestEarlyPrice2 = get_capsule_value(plunderChestEarlyPrice2) or "15"
    plunderChestEarlyPrice34 = get_capsule_value(plunderChestEarlyPrice34) or "15"
    plunderChestMidPrice1 = get_capsule_value(plunderChestMidPrice1) or "15"
    plunderChestMidPrice2 = get_capsule_value(plunderChestMidPrice2) or "15"
    plunderChestMidPrice34 = get_capsule_value(plunderChestMidPrice34) or "15"
    plunderChestLatePrice1 = get_capsule_value(plunderChestLatePrice1) or "15"
    plunderChestLatePrice2 = get_capsule_value(plunderChestLatePrice2) or "15"
    plunderChestLatePrice34 = get_capsule_value(plunderChestLatePrice34) or "15"

    # Gaddbrush: DX
    gaddbrushEarlyPrice1 = get_capsule_value(gaddbrushEarlyPrice1) or "15"
    gaddbrushEarlyPrice2 = get_capsule_value(gaddbrushEarlyPrice2) or "15"
    gaddbrushEarlyPrice34 = get_capsule_value(gaddbrushEarlyPrice34) or "15"
    gaddbrushMidPrice1 = get_capsule_value(gaddbrushMidPrice1) or "15"
    gaddbrushMidPrice2 = get_capsule_value(gaddbrushMidPrice2) or "15"
    gaddbrushMidPrice34 = get_capsule_value(gaddbrushMidPrice34) or "15"
    gaddbrushLatePrice1 = get_capsule_value(gaddbrushLatePrice1) or "15"
    gaddbrushLatePrice2 = get_capsule_value(gaddbrushLatePrice2) or "15"
    gaddbrushLatePrice34 = get_capsule_value(gaddbrushLatePrice34) or "15"

    # Warp Block: DX
    warpBlockEarlyPrice1 = get_capsule_value(warpBlockEarlyPrice1) or "5"
    warpBlockEarlyPrice2 = get_capsule_value(warpBlockEarlyPrice2) or "5"
    warpBlockEarlyPrice34 = get_capsule_value(warpBlockEarlyPrice34) or "5"
    warpBlockMidPrice1 = get_capsule_value(warpBlockMidPrice1) or "5"
    warpBlockMidPrice2 = get_capsule_value(warpBlockMidPrice2) or "5"
    warpBlockMidPrice34 = get_capsule_value(warpBlockMidPrice34) or "5"
    warpBlockLatePrice1 = get_capsule_value(warpBlockLatePrice1) or "5"
    warpBlockLatePrice2 = get_capsule_value(warpBlockLatePrice2) or "5"
    warpBlockLatePrice34 = get_capsule_value(warpBlockLatePrice34) or "5"

    # Fly Guy: DX
    flyGuyEarlyPrice1 = get_capsule_value(flyGuyEarlyPrice1) or "12"
    flyGuyEarlyPrice2 = get_capsule_value(flyGuyEarlyPrice2) or "12"
    flyGuyEarlyPrice34 = get_capsule_value(flyGuyEarlyPrice34) or "12"
    flyGuyMidPrice1 = get_capsule_value(flyGuyMidPrice1) or "12"
    flyGuyMidPrice2 = get_capsule_value(flyGuyMidPrice2) or "12"
    flyGuyMidPrice34 = get_capsule_value(flyGuyMidPrice34) or "12"
    flyGuyLatePrice1 = get_capsule_value(flyGuyLatePrice1) or "12"
    flyGuyLatePrice2 = get_capsule_value(flyGuyLatePrice2) or "12"
    flyGuyLatePrice34 = get_capsule_value(flyGuyLatePrice34) or "12"

    # Plus Block: DX
    plusBlockEarlyPrice1 = get_capsule_value(plusBlockEarlyPrice1) or "10"
    plusBlockEarlyPrice2 = get_capsule_value(plusBlockEarlyPrice2) or "10"
    plusBlockEarlyPrice34 = get_capsule_value(plusBlockEarlyPrice34) or "10"
    plusBlockMidPrice1 = get_capsule_value(plusBlockMidPrice1) or "10"
    plusBlockMidPrice2 = get_capsule_value(plusBlockMidPrice2) or "10"
    plusBlockMidPrice34 = get_capsule_value(plusBlockMidPrice34) or "10"
    plusBlockLatePrice1 = get_capsule_value(plusBlockLatePrice1) or "10"
    plusBlockLatePrice2 = get_capsule_value(plusBlockLatePrice2) or "10"
    plusBlockLatePrice34 = get_capsule_value(plusBlockLatePrice34) or "10"

    # Minus Block: DX
    minusBlockEarlyPrice1 = get_capsule_value(minusBlockEarlyPrice1) or "10"
    minusBlockEarlyPrice2 = get_capsule_value(minusBlockEarlyPrice2) or "10"
    minusBlockEarlyPrice34 = get_capsule_value(minusBlockEarlyPrice34) or "10"
    minusBlockMidPrice1 = get_capsule_value(minusBlockMidPrice1) or "10"
    minusBlockMidPrice2 = get_capsule_value(minusBlockMidPrice2) or "10"
    minusBlockMidPrice34 = get_capsule_value(minusBlockMidPrice34) or "10"
    minusBlockLatePrice1 = get_capsule_value(minusBlockLatePrice1) or "10"
    minusBlockLatePrice2 = get_capsule_value(minusBlockLatePrice2) or "10"
    minusBlockLatePrice34 = get_capsule_value(minusBlockLatePrice34) or "10"

    # Speed Block: DX
    speedBlockEarlyPrice1 = get_capsule_value(speedBlockEarlyPrice1) or "12"
    speedBlockEarlyPrice2 = get_capsule_value(speedBlockEarlyPrice2) or "12"
    speedBlockEarlyPrice34 = get_capsule_value(speedBlockEarlyPrice34) or "12"
    speedBlockMidPrice1 = get_capsule_value(speedBlockMidPrice1) or "12"
    speedBlockMidPrice2 = get_capsule_value(speedBlockMidPrice2) or "12"
    speedBlockMidPrice34 = get_capsule_value(speedBlockMidPrice34) or "12"
    speedBlockLatePrice1 = get_capsule_value(speedBlockLatePrice1) or "12"
    speedBlockLatePrice2 = get_capsule_value(speedBlockLatePrice2) or "12"
    speedBlockLatePrice34 = get_capsule_value(speedBlockLatePrice34) or "12"

    # Slow Block: DX
    slowBlockEarlyPrice1 = get_capsule_value(slowBlockEarlyPrice1) or "12"
    slowBlockEarlyPrice2 = get_capsule_value(slowBlockEarlyPrice2) or "12"
    slowBlockEarlyPrice34 = get_capsule_value(slowBlockEarlyPrice34) or "12"
    slowBlockMidPrice1 = get_capsule_value(slowBlockMidPrice1) or "12"
    slowBlockMidPrice2 = get_capsule_value(slowBlockMidPrice2) or "12"
    slowBlockMidPrice34 = get_capsule_value(slowBlockMidPrice34) or "12"
    slowBlockLatePrice1 = get_capsule_value(slowBlockLatePrice1) or "12"
    slowBlockLatePrice2 = get_capsule_value(slowBlockLatePrice2) or "12"
    slowBlockLatePrice34 = get_capsule_value(slowBlockLatePrice34) or "12"

    # Hidden Block Card: DX
    hiddenBlockCardEarlyPrice1 = get_capsule_value(hiddenBlockCardEarlyPrice1) or "40"
    hiddenBlockCardEarlyPrice2 = get_capsule_value(hiddenBlockCardEarlyPrice2) or "40"
    hiddenBlockCardEarlyPrice34 = get_capsule_value(hiddenBlockCardEarlyPrice34) or "40"
    hiddenBlockCardMidPrice1 = get_capsule_value(hiddenBlockCardMidPrice1) or "40"
    hiddenBlockCardMidPrice2 = get_capsule_value(hiddenBlockCardMidPrice2) or "40"
    hiddenBlockCardMidPrice34 = get_capsule_value(hiddenBlockCardMidPrice34) or "40"
    hiddenBlockCardLatePrice1 = get_capsule_value(hiddenBlockCardLatePrice1) or "40"
    hiddenBlockCardLatePrice2 = get_capsule_value(hiddenBlockCardLatePrice2) or "40"
    hiddenBlockCardLatePrice34 = get_capsule_value(hiddenBlockCardLatePrice34) or "40"

    # Barter Box: DX
    barterBoxEarlyPrice1 = get_capsule_value(barterBoxEarlyPrice1) or "40"
    barterBoxEarlyPrice2 = get_capsule_value(barterBoxEarlyPrice2) or "40"
    barterBoxEarlyPrice34 = get_capsule_value(barterBoxEarlyPrice34) or "40"
    barterBoxMidPrice1 = get_capsule_value(barterBoxMidPrice1) or "40"
    barterBoxMidPrice2 = get_capsule_value(barterBoxMidPrice2) or "40"
    barterBoxMidPrice34 = get_capsule_value(barterBoxMidPrice34) or "40"
    barterBoxLatePrice1 = get_capsule_value(barterBoxLatePrice1) or "40"
    barterBoxLatePrice2 = get_capsule_value(barterBoxLatePrice2) or "40"
    barterBoxLatePrice34 = get_capsule_value(barterBoxLatePrice34) or "40"

    # Super Warp Pipe: DX
    superWarpPipeEarlyPrice1 = get_capsule_value(superWarpPipeEarlyPrice1) or "40"
    superWarpPipeEarlyPrice2 = get_capsule_value(superWarpPipeEarlyPrice2) or "40"
    superWarpPipeEarlyPrice34 = get_capsule_value(superWarpPipeEarlyPrice34) or "40"
    superWarpPipeMidPrice1 = get_capsule_value(superWarpPipeMidPrice1) or "40"
    superWarpPipeMidPrice2 = get_capsule_value(superWarpPipeMidPrice2) or "40"
    superWarpPipeMidPrice34 = get_capsule_value(superWarpPipeMidPrice34) or "40"
    superWarpPipeLatePrice1 = get_capsule_value(superWarpPipeLatePrice1) or "40"
    superWarpPipeLatePrice2 = get_capsule_value(superWarpPipeLatePrice2) or "40"
    superWarpPipeLatePrice34 = get_capsule_value(superWarpPipeLatePrice34) or "40"

    # Chance Time Charm: DX
    chanceTimeCharmEarlyPrice1 = get_capsule_value(chanceTimeCharmEarlyPrice1) or "40"
    chanceTimeCharmEarlyPrice2 = get_capsule_value(chanceTimeCharmEarlyPrice2) or "40"
    chanceTimeCharmEarlyPrice34 = get_capsule_value(chanceTimeCharmEarlyPrice34) or "40"
    chanceTimeCharmMidPrice1 = get_capsule_value(chanceTimeCharmMidPrice1) or "40"
    chanceTimeCharmMidPrice2 = get_capsule_value(chanceTimeCharmMidPrice2) or "40"
    chanceTimeCharmMidPrice34 = get_capsule_value(chanceTimeCharmMidPrice34) or "40"
    chanceTimeCharmLatePrice1 = get_capsule_value(chanceTimeCharmLatePrice1) or "40"
    chanceTimeCharmLatePrice2 = get_capsule_value(chanceTimeCharmLatePrice2) or "40"
    chanceTimeCharmLatePrice34 = get_capsule_value(chanceTimeCharmLatePrice34) or "40"

    # Wacky Watch: DX
    wackyWatchEarlyPrice1 = get_capsule_value(wackyWatchEarlyPrice1) or "100"
    wackyWatchEarlyPrice2 = get_capsule_value(wackyWatchEarlyPrice2) or "100"
    wackyWatchEarlyPrice34 = get_capsule_value(wackyWatchEarlyPrice34) or "100"
    wackyWatchMidPrice1 = get_capsule_value(wackyWatchMidPrice1) or "100"
    wackyWatchMidPrice2 = get_capsule_value(wackyWatchMidPrice2) or "100"
    wackyWatchMidPrice34 = get_capsule_value(wackyWatchMidPrice34) or "100"
    wackyWatchLatePrice1 = get_capsule_value(wackyWatchLatePrice1) or "100"
    wackyWatchLatePrice2 = get_capsule_value(wackyWatchLatePrice2) or "100"
    wackyWatchLatePrice34 = get_capsule_value(wackyWatchLatePrice34) or "100"
    
    # Double Dip: DX
    doubleDipEarlyPrice1 = get_capsule_value(doubleDipEarlyPrice1) or "12"
    doubleDipEarlyPrice2 = get_capsule_value(doubleDipEarlyPrice2) or "12"
    doubleDipEarlyPrice34 = get_capsule_value(doubleDipEarlyPrice34) or "12"
    doubleDipMidPrice1 = get_capsule_value(doubleDipMidPrice1) or "12"
    doubleDipMidPrice2 = get_capsule_value(doubleDipMidPrice2) or "12"
    doubleDipMidPrice34 = get_capsule_value(doubleDipMidPrice34) or "12"
    doubleDipLatePrice1 = get_capsule_value(doubleDipLatePrice1) or "12"
    doubleDipLatePrice2 = get_capsule_value(doubleDipLatePrice2) or "12"
    doubleDipLatePrice34 = get_capsule_value(doubleDipLatePrice34) or "12"

    minCoins = find_lowest_integer(*[
        int(miniMushroomEarlyPrice1), int(miniMushroomEarlyPrice2), int(miniMushroomEarlyPrice34), 
        int(miniMushroomMidPrice1), int(miniMushroomMidPrice2), int(miniMushroomMidPrice34),
        int(miniMushroomLatePrice1), int(miniMushroomLatePrice2), int(miniMushroomLatePrice34),
        int(megaMushroomEarlyPrice1), int(megaMushroomEarlyPrice2), int(megaMushroomEarlyPrice34), 
        int(megaMushroomMidPrice1), int(megaMushroomMidPrice2), int(megaMushroomMidPrice34),
        int(megaMushroomLatePrice1), int(megaMushroomLatePrice2), int(megaMushroomLatePrice34),
        int(superMiniMushroomEarlyPrice1), int(superMiniMushroomEarlyPrice2), int(superMiniMushroomEarlyPrice34),
        int(superMiniMushroomMidPrice1), int(superMiniMushroomMidPrice2), int(superMiniMushroomMidPrice34),
        int(superMiniMushroomLatePrice1), int(superMiniMushroomLatePrice2), int(superMiniMushroomLatePrice34),
        int(superMegaMushroomEarlyPrice1), int(superMegaMushroomEarlyPrice2), int(superMegaMushroomEarlyPrice34),
        int(superMegaMushroomMidPrice1), int(superMegaMushroomMidPrice2), int(superMegaMushroomMidPrice34),
        int(superMegaMushroomLatePrice1), int(superMegaMushroomLatePrice2), int(superMegaMushroomLatePrice34),
        int(miniMegaHammerEarlyPrice1), int(miniMegaHammerEarlyPrice2), int(miniMegaHammerEarlyPrice34),
        int(miniMegaHammerMidPrice1), int(miniMegaHammerMidPrice2), int(miniMegaHammerMidPrice34),
        int(miniMegaHammerLatePrice1), int(miniMegaHammerLatePrice2), int(miniMegaHammerLatePrice34),
        int(warpPipeEarlyPrice1), int(warpPipeEarlyPrice2), int(warpPipeEarlyPrice34),
        int(warpPipeMidPrice1), int(warpPipeMidPrice2), int(warpPipeMidPrice34),
        int(warpPipeLatePrice1), int(warpPipeLatePrice2), int(warpPipeLatePrice34),
        int(swapCardEarlyPrice1), int(swapCardEarlyPrice2), int(swapCardEarlyPrice34),
        int(swapCardMidPrice1), int(swapCardMidPrice2), int(swapCardMidPrice34),
        int(swapCardLatePrice1), int(swapCardLatePrice2), int(swapCardLatePrice34),
        int(sparkyStickerEarlyPrice1), int(sparkyStickerEarlyPrice2), int(sparkyStickerEarlyPrice34),
        int(sparkyStickerMidPrice1), int(sparkyStickerMidPrice2), int(sparkyStickerMidPrice34),
        int(sparkyStickerLatePrice1), int(sparkyStickerLatePrice2), int(sparkyStickerLatePrice34),
        int(gaddlightEarlyPrice1), int(gaddlightEarlyPrice2), int(gaddlightEarlyPrice34),
        int(gaddlightMidPrice1), int(gaddlightMidPrice2), int(gaddlightMidPrice34),
        int(gaddlightLatePrice1), int(gaddlightLatePrice2), int(gaddlightLatePrice34),
        int(chompCallEarlyPrice1), int(chompCallEarlyPrice2), int(chompCallEarlyPrice34),
        int(chompCallMidPrice1), int(chompCallMidPrice2), int(chompCallMidPrice34),
        int(chompCallLatePrice1), int(chompCallLatePrice2), int(chompCallLatePrice34),
        int(bowserSuitEarlyPrice1), int(bowserSuitEarlyPrice2), int(bowserSuitEarlyPrice34),
        int(bowserSuitMidPrice1), int(bowserSuitMidPrice2), int(bowserSuitMidPrice34),
        int(bowserSuitLatePrice1), int(bowserSuitLatePrice2), int(bowserSuitLatePrice34),
        int(crystalBallEarlyPrice1), int(crystalBallEarlyPrice2), int(crystalBallEarlyPrice34),
        int(crystalBallMidPrice1), int(crystalBallMidPrice2), int(crystalBallMidPrice34),
        int(crystalBallLatePrice1), int(crystalBallLatePrice2), int(crystalBallLatePrice34),
        int(magicLampEarlyPrice1), int(magicLampEarlyPrice2), int(magicLampEarlyPrice34),
        int(magicLampMidPrice1), int(magicLampMidPrice2), int(magicLampMidPrice34),
        int(magicLampLatePrice1), int(magicLampLatePrice2), int(magicLampLatePrice34),
        int(itemBagEarlyPrice1), int(itemBagEarlyPrice2), int(itemBagEarlyPrice34),
        int(itemBagMidPrice1), int(itemBagMidPrice2), int(itemBagMidPrice34),
        int(itemBagLatePrice1), int(itemBagLatePrice2), int(itemBagLatePrice34),
        int(mushroomEarlyPrice1), int(mushroomEarlyPrice2), int(mushroomEarlyPrice34),
        int(mushroomMidPrice1), int(mushroomMidPrice2), int(mushroomMidPrice34),
        int(mushroomLatePrice1), int(mushroomLatePrice2), int(mushroomLatePrice34),
        int(goldenMushroomEarlyPrice1), int(goldenMushroomEarlyPrice2), int(goldenMushroomEarlyPrice34),
        int(goldenMushroomMidPrice1), int(goldenMushroomMidPrice2), int(goldenMushroomMidPrice34),
        int(goldenMushroomLatePrice1), int(goldenMushroomLatePrice2), int(goldenMushroomLatePrice34),
        int(reverseMushroomEarlyPrice1), int(reverseMushroomEarlyPrice2), int(reverseMushroomEarlyPrice34),
        int(reverseMushroomMidPrice1), int(reverseMushroomMidPrice2), int(reverseMushroomMidPrice34),
        int(reverseMushroomLatePrice1), int(reverseMushroomLatePrice2), int(reverseMushroomLatePrice34),
        int(poisonMushroomEarlyPrice1), int(poisonMushroomEarlyPrice2), int(poisonMushroomEarlyPrice34),
        int(poisonMushroomMidPrice1), int(poisonMushroomMidPrice2), int(poisonMushroomMidPrice34),
        int(poisonMushroomLatePrice1), int(poisonMushroomLatePrice2), int(poisonMushroomLatePrice34),
        int(bowserPhoneEarlyPrice1), int(bowserPhoneEarlyPrice2), int(bowserPhoneEarlyPrice34),
        int(bowserPhoneMidPrice1), int(bowserPhoneMidPrice2), int(bowserPhoneMidPrice34),
        int(bowserPhoneLatePrice1), int(bowserPhoneLatePrice2), int(bowserPhoneLatePrice34),
        int(triplePoisonMushroomEarlyPrice1), int(triplePoisonMushroomEarlyPrice2), int(triplePoisonMushroomEarlyPrice34),
        int(triplePoisonMushroomMidPrice1), int(triplePoisonMushroomMidPrice2), int(triplePoisonMushroomMidPrice34),
        int(triplePoisonMushroomLatePrice1), int(triplePoisonMushroomLatePrice2), int(triplePoisonMushroomLatePrice34),
        int(celluarShopperEarlyPrice1), int(celluarShopperEarlyPrice2), int(celluarShopperEarlyPrice34),
        int(celluarShopperMidPrice1), int(celluarShopperMidPrice2), int(celluarShopperMidPrice34),
        int(celluarShopperLatePrice1), int(celluarShopperLatePrice2), int(celluarShopperLatePrice34),
        int(skeletonKeyEarlyPrice1), int(skeletonKeyEarlyPrice2), int(skeletonKeyEarlyPrice34),
        int(skeletonKeyMidPrice1), int(skeletonKeyMidPrice2), int(skeletonKeyMidPrice34),
        int(skeletonKeyLatePrice1), int(skeletonKeyLatePrice2), int(skeletonKeyLatePrice34),
        int(plunderChestEarlyPrice1), int(plunderChestEarlyPrice2), int(plunderChestEarlyPrice34),
        int(plunderChestMidPrice1), int(plunderChestMidPrice2), int(plunderChestMidPrice34),
        int(plunderChestLatePrice1), int(plunderChestLatePrice2), int(plunderChestLatePrice34),
        int(gaddbrushEarlyPrice1), int(gaddbrushEarlyPrice2), int(gaddbrushEarlyPrice34),
        int(gaddbrushMidPrice1), int(gaddbrushMidPrice2), int(gaddbrushMidPrice34),
        int(gaddbrushLatePrice1), int(gaddbrushLatePrice2), int(gaddbrushLatePrice34),
        int(warpBlockEarlyPrice1), int(warpBlockEarlyPrice2), int(warpBlockEarlyPrice34),
        int(warpBlockMidPrice1), int(warpBlockMidPrice2), int(warpBlockMidPrice34),
        int(warpBlockLatePrice1), int(warpBlockLatePrice2), int(warpBlockLatePrice34),
        int(flyGuyEarlyPrice1), int(flyGuyEarlyPrice2), int(flyGuyEarlyPrice34),
        int(flyGuyMidPrice1), int(flyGuyMidPrice2), int(flyGuyMidPrice34),
        int(flyGuyLatePrice1), int(flyGuyLatePrice2), int(flyGuyLatePrice34),
        int(plusBlockEarlyPrice1), int(plusBlockEarlyPrice2), int(plusBlockEarlyPrice34),
        int(plusBlockMidPrice1), int(plusBlockMidPrice2), int(plusBlockMidPrice34),
        int(plusBlockLatePrice1), int(plusBlockLatePrice2), int(plusBlockLatePrice34),
        int(minusBlockEarlyPrice1), int(minusBlockEarlyPrice2), int(minusBlockEarlyPrice34),
        int(minusBlockMidPrice1), int(minusBlockMidPrice2), int(minusBlockMidPrice34),
        int(minusBlockLatePrice1), int(minusBlockLatePrice2), int(minusBlockLatePrice34),
        int(speedBlockEarlyPrice1), int(speedBlockEarlyPrice2), int(speedBlockEarlyPrice34),
        int(speedBlockMidPrice1), int(speedBlockMidPrice2), int(speedBlockMidPrice34),
        int(speedBlockLatePrice1), int(speedBlockLatePrice2), int(speedBlockLatePrice34),
        int(slowBlockEarlyPrice1), int(slowBlockEarlyPrice2), int(slowBlockEarlyPrice34),
        int(slowBlockMidPrice1), int(slowBlockMidPrice2), int(slowBlockMidPrice34),
        int(slowBlockLatePrice1), int(slowBlockLatePrice2), int(slowBlockLatePrice34),
        int(hiddenBlockCardEarlyPrice1), int(hiddenBlockCardEarlyPrice2), int(hiddenBlockCardEarlyPrice34),
        int(hiddenBlockCardMidPrice1), int(hiddenBlockCardMidPrice2), int(hiddenBlockCardMidPrice34),
        int(hiddenBlockCardLatePrice1), int(hiddenBlockCardLatePrice2), int(hiddenBlockCardLatePrice34),
        int(barterBoxEarlyPrice1), int(barterBoxEarlyPrice2), int(barterBoxEarlyPrice34),
        int(barterBoxMidPrice1), int(barterBoxMidPrice2), int(barterBoxMidPrice34),
        int(barterBoxLatePrice1), int(barterBoxLatePrice2), int(barterBoxLatePrice34),
        int(superWarpPipeEarlyPrice1), int(superWarpPipeEarlyPrice2), int(superWarpPipeEarlyPrice34),
        int(superWarpPipeMidPrice1), int(superWarpPipeMidPrice2), int(superWarpPipeMidPrice34),
        int(superWarpPipeLatePrice1), int(superWarpPipeLatePrice2), int(superWarpPipeLatePrice34),
        int(chanceTimeCharmEarlyPrice1), int(chanceTimeCharmEarlyPrice2), int(chanceTimeCharmEarlyPrice34),
        int(chanceTimeCharmMidPrice1), int(chanceTimeCharmMidPrice2), int(chanceTimeCharmMidPrice34),
        int(chanceTimeCharmLatePrice1), int(chanceTimeCharmLatePrice2), int(chanceTimeCharmLatePrice34),
        int(wackyWatchEarlyPrice1), int(wackyWatchEarlyPrice2), int(wackyWatchEarlyPrice34),
        int(wackyWatchMidPrice1), int(wackyWatchMidPrice2), int(wackyWatchMidPrice34),
        int(wackyWatchLatePrice1), int(wackyWatchLatePrice2), int(wackyWatchLatePrice34),
        int(doubleDipEarlyPrice1), int(doubleDipEarlyPrice2), int(doubleDipEarlyPrice34),
        int(doubleDipMidPrice1), int(doubleDipMidPrice2), int(doubleDipMidPrice34),
        int(doubleDipLatePrice1), int(doubleDipLatePrice2), int(doubleDipLatePrice34)

    ])


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


    # Mini Mushroom
    miniMushroomEarlyPrice1 = convert_to_hex_weight(miniMushroomEarlyPrice1)
    miniMushroomEarlyPrice2 = convert_to_hex_weight(miniMushroomEarlyPrice2)
    miniMushroomEarlyPrice34 = convert_to_hex_weight(miniMushroomEarlyPrice34)
    miniMushroomMidPrice1 = convert_to_hex_weight(miniMushroomMidPrice1)
    miniMushroomMidPrice2 = convert_to_hex_weight(miniMushroomMidPrice2)
    miniMushroomMidPrice34 = convert_to_hex_weight(miniMushroomMidPrice34)
    miniMushroomLatePrice1 = convert_to_hex_weight(miniMushroomLatePrice1)
    miniMushroomLatePrice2 = convert_to_hex_weight(miniMushroomLatePrice2)
    miniMushroomLatePrice34 = convert_to_hex_weight(miniMushroomLatePrice34)
    
    # Mega Mushroom
    megaMushroomEarlyPrice1 = convert_to_hex_weight(megaMushroomEarlyPrice1)
    megaMushroomEarlyPrice2 = convert_to_hex_weight(megaMushroomEarlyPrice2)
    megaMushroomEarlyPrice34 = convert_to_hex_weight(megaMushroomEarlyPrice34)
    megaMushroomMidPrice1 = convert_to_hex_weight(megaMushroomMidPrice1)
    megaMushroomMidPrice2 = convert_to_hex_weight(megaMushroomMidPrice2)
    megaMushroomMidPrice34 = convert_to_hex_weight(megaMushroomMidPrice34)
    megaMushroomLatePrice1 = convert_to_hex_weight(megaMushroomLatePrice1)
    megaMushroomLatePrice2 = convert_to_hex_weight(megaMushroomLatePrice2)
    megaMushroomLatePrice34 = convert_to_hex_weight(megaMushroomLatePrice34)

    # Super Mini Mushroom
    superMiniMushroomEarlyPrice1 = convert_to_hex_weight(superMiniMushroomEarlyPrice1)
    superMiniMushroomEarlyPrice2 = convert_to_hex_weight(superMiniMushroomEarlyPrice2)
    superMiniMushroomEarlyPrice34 = convert_to_hex_weight(superMiniMushroomEarlyPrice34)
    superMiniMushroomMidPrice1 = convert_to_hex_weight(superMiniMushroomMidPrice1)
    superMiniMushroomMidPrice2 = convert_to_hex_weight(superMiniMushroomMidPrice2)
    superMiniMushroomMidPrice34 = convert_to_hex_weight(superMiniMushroomMidPrice34)
    superMiniMushroomLatePrice1 = convert_to_hex_weight(superMiniMushroomLatePrice1)
    superMiniMushroomLatePrice2 = convert_to_hex_weight(superMiniMushroomLatePrice2)
    superMiniMushroomLatePrice34 = convert_to_hex_weight(superMiniMushroomLatePrice34)

    # Super Mega Mushroom
    superMegaMushroomEarlyPrice1 = convert_to_hex_weight(superMegaMushroomEarlyPrice1)
    superMegaMushroomEarlyPrice2 = convert_to_hex_weight(superMegaMushroomEarlyPrice2)
    superMegaMushroomEarlyPrice34 = convert_to_hex_weight(superMegaMushroomEarlyPrice34)
    superMegaMushroomMidPrice1 = convert_to_hex_weight(superMegaMushroomMidPrice1)
    superMegaMushroomMidPrice2 = convert_to_hex_weight(superMegaMushroomMidPrice2)
    superMegaMushroomMidPrice34 = convert_to_hex_weight(superMegaMushroomMidPrice34)
    superMegaMushroomLatePrice1 = convert_to_hex_weight(superMegaMushroomLatePrice1)
    superMegaMushroomLatePrice2 = convert_to_hex_weight(superMegaMushroomLatePrice2)
    superMegaMushroomLatePrice34 = convert_to_hex_weight(superMegaMushroomLatePrice34)

    # Mini Mega Hammer
    miniMegaHammerEarlyPrice1 = convert_to_hex_weight(miniMegaHammerEarlyPrice1)
    miniMegaHammerEarlyPrice2 = convert_to_hex_weight(miniMegaHammerEarlyPrice2)
    miniMegaHammerEarlyPrice34 = convert_to_hex_weight(miniMegaHammerEarlyPrice34)
    miniMegaHammerMidPrice1 = convert_to_hex_weight(miniMegaHammerMidPrice1)
    miniMegaHammerMidPrice2 = convert_to_hex_weight(miniMegaHammerMidPrice2)
    miniMegaHammerMidPrice34 = convert_to_hex_weight(miniMegaHammerMidPrice34)
    miniMegaHammerLatePrice1 = convert_to_hex_weight(miniMegaHammerLatePrice1)
    miniMegaHammerLatePrice2 = convert_to_hex_weight(miniMegaHammerLatePrice2)
    miniMegaHammerLatePrice34 = convert_to_hex_weight(miniMegaHammerLatePrice34)

    # Warp Pipe
    warpPipeEarlyPrice1 = convert_to_hex_weight(warpPipeEarlyPrice1)
    warpPipeEarlyPrice2 = convert_to_hex_weight(warpPipeEarlyPrice2)
    warpPipeEarlyPrice34 = convert_to_hex_weight(warpPipeEarlyPrice34)
    warpPipeMidPrice1 = convert_to_hex_weight(warpPipeMidPrice1)
    warpPipeMidPrice2 = convert_to_hex_weight(warpPipeMidPrice2)
    warpPipeMidPrice34 = convert_to_hex_weight(warpPipeMidPrice34)
    warpPipeLatePrice1 = convert_to_hex_weight(warpPipeLatePrice1)
    warpPipeLatePrice2 = convert_to_hex_weight(warpPipeLatePrice2)
    warpPipeLatePrice34 = convert_to_hex_weight(warpPipeLatePrice34)

    # Swap Card
    swapCardEarlyPrice1 = convert_to_hex_weight(swapCardEarlyPrice1)
    swapCardEarlyPrice2 = convert_to_hex_weight(swapCardEarlyPrice2)
    swapCardEarlyPrice34 = convert_to_hex_weight(swapCardEarlyPrice34)
    swapCardMidPrice1 = convert_to_hex_weight(swapCardMidPrice1)
    swapCardMidPrice2 = convert_to_hex_weight(swapCardMidPrice2)
    swapCardMidPrice34 = convert_to_hex_weight(swapCardMidPrice34)
    swapCardLatePrice1 = convert_to_hex_weight(swapCardLatePrice1)
    swapCardLatePrice2 = convert_to_hex_weight(swapCardLatePrice2)
    swapCardLatePrice34 = convert_to_hex_weight(swapCardLatePrice34)

    # Sparky Sticker
    sparkyStickerEarlyPrice1 = convert_to_hex_weight(sparkyStickerEarlyPrice1)
    sparkyStickerEarlyPrice2 = convert_to_hex_weight(sparkyStickerEarlyPrice2)
    sparkyStickerEarlyPrice34 = convert_to_hex_weight(sparkyStickerEarlyPrice34)
    sparkyStickerMidPrice1 = convert_to_hex_weight(sparkyStickerMidPrice1)
    sparkyStickerMidPrice2 = convert_to_hex_weight(sparkyStickerMidPrice2)
    sparkyStickerMidPrice34 = convert_to_hex_weight(sparkyStickerMidPrice34)
    sparkyStickerLatePrice1 = convert_to_hex_weight(sparkyStickerLatePrice1)
    sparkyStickerLatePrice2 = convert_to_hex_weight(sparkyStickerLatePrice2)
    sparkyStickerLatePrice34 = convert_to_hex_weight(sparkyStickerLatePrice34)

    # Gaddlight
    gaddlightEarlyPrice1 = convert_to_hex_weight(gaddlightEarlyPrice1)
    gaddlightEarlyPrice2 = convert_to_hex_weight(gaddlightEarlyPrice2)
    gaddlightEarlyPrice34 = convert_to_hex_weight(gaddlightEarlyPrice34)
    gaddlightMidPrice1 = convert_to_hex_weight(gaddlightMidPrice1)
    gaddlightMidPrice2 = convert_to_hex_weight(gaddlightMidPrice2)
    gaddlightMidPrice34 = convert_to_hex_weight(gaddlightMidPrice34)
    gaddlightLatePrice1 = convert_to_hex_weight(gaddlightLatePrice1)
    gaddlightLatePrice2 = convert_to_hex_weight(gaddlightLatePrice2)
    gaddlightLatePrice34 = convert_to_hex_weight(gaddlightLatePrice34)

    # Chomp Call
    chompCallEarlyPrice1 = convert_to_hex_weight(chompCallEarlyPrice1)
    chompCallEarlyPrice2 = convert_to_hex_weight(chompCallEarlyPrice2)
    chompCallEarlyPrice34 = convert_to_hex_weight(chompCallEarlyPrice34)
    chompCallMidPrice1 = convert_to_hex_weight(chompCallMidPrice1)
    chompCallMidPrice2 = convert_to_hex_weight(chompCallMidPrice2)
    chompCallMidPrice34 = convert_to_hex_weight(chompCallMidPrice34)
    chompCallLatePrice1 = convert_to_hex_weight(chompCallLatePrice1)
    chompCallLatePrice2 = convert_to_hex_weight(chompCallLatePrice2)
    chompCallLatePrice34 = convert_to_hex_weight(chompCallLatePrice34)

    # Bowser Suit
    bowserSuitEarlyPrice1 = convert_to_hex_weight(bowserSuitEarlyPrice1)
    bowserSuitEarlyPrice2 = convert_to_hex_weight(bowserSuitEarlyPrice2)
    bowserSuitEarlyPrice34 = convert_to_hex_weight(bowserSuitEarlyPrice34)
    bowserSuitMidPrice1 = convert_to_hex_weight(bowserSuitMidPrice1)
    bowserSuitMidPrice2 = convert_to_hex_weight(bowserSuitMidPrice2)
    bowserSuitMidPrice34 = convert_to_hex_weight(bowserSuitMidPrice34)
    bowserSuitLatePrice1 = convert_to_hex_weight(bowserSuitLatePrice1)
    bowserSuitLatePrice2 = convert_to_hex_weight(bowserSuitLatePrice2)
    bowserSuitLatePrice34 = convert_to_hex_weight(bowserSuitLatePrice34)

    # Crystal Ball
    crystalBallEarlyPrice1 = convert_to_hex_weight(crystalBallEarlyPrice1)
    crystalBallEarlyPrice2 = convert_to_hex_weight(crystalBallEarlyPrice2)
    crystalBallEarlyPrice34 = convert_to_hex_weight(crystalBallEarlyPrice34)
    crystalBallMidPrice1 = convert_to_hex_weight(crystalBallMidPrice1)
    crystalBallMidPrice2 = convert_to_hex_weight(crystalBallMidPrice2)
    crystalBallMidPrice34 = convert_to_hex_weight(crystalBallMidPrice34)
    crystalBallLatePrice1 = convert_to_hex_weight(crystalBallLatePrice1)
    crystalBallLatePrice2 = convert_to_hex_weight(crystalBallLatePrice2)
    crystalBallLatePrice34 = convert_to_hex_weight(crystalBallLatePrice34)

    # Magic Lamp
    magicLampEarlyPrice1 = convert_to_hex_weight(magicLampEarlyPrice1)
    magicLampEarlyPrice2 = convert_to_hex_weight(magicLampEarlyPrice2)
    magicLampEarlyPrice34 = convert_to_hex_weight(magicLampEarlyPrice34)
    magicLampMidPrice1 = convert_to_hex_weight(magicLampMidPrice1)
    magicLampMidPrice2 = convert_to_hex_weight(magicLampMidPrice2)
    magicLampMidPrice34 = convert_to_hex_weight(magicLampMidPrice34)
    magicLampLatePrice1 = convert_to_hex_weight(magicLampLatePrice1)
    magicLampLatePrice2 = convert_to_hex_weight(magicLampLatePrice2)
    magicLampLatePrice34 = convert_to_hex_weight(magicLampLatePrice34)

    # Item Bag
    itemBagEarlyPrice1 = convert_to_hex_weight(itemBagEarlyPrice1)
    itemBagEarlyPrice2 = convert_to_hex_weight(itemBagEarlyPrice2)
    itemBagEarlyPrice34 = convert_to_hex_weight(itemBagEarlyPrice34)
    itemBagMidPrice1 = convert_to_hex_weight(itemBagMidPrice1)
    itemBagMidPrice2 = convert_to_hex_weight(itemBagMidPrice2)
    itemBagMidPrice34 = convert_to_hex_weight(itemBagMidPrice34)
    itemBagLatePrice1 = convert_to_hex_weight(itemBagLatePrice1)
    itemBagLatePrice2 = convert_to_hex_weight(itemBagLatePrice2)
    itemBagLatePrice34 = convert_to_hex_weight(itemBagLatePrice34)

    # Mushroom: DX
    mushroomEarlyPrice1 = convert_to_hex_weight(mushroomEarlyPrice1)
    mushroomEarlyPrice2 = convert_to_hex_weight(mushroomEarlyPrice2)
    mushroomEarlyPrice34 = convert_to_hex_weight(mushroomEarlyPrice34)
    mushroomMidPrice1 = convert_to_hex_weight(mushroomMidPrice1)
    mushroomMidPrice2 = convert_to_hex_weight(mushroomMidPrice2)
    mushroomMidPrice34 = convert_to_hex_weight(mushroomMidPrice34)
    mushroomLatePrice1 = convert_to_hex_weight(mushroomLatePrice1)
    mushroomLatePrice2 = convert_to_hex_weight(mushroomLatePrice2)
    mushroomLatePrice34 = convert_to_hex_weight(mushroomLatePrice34)

    # Golden Mushroom: DX
    goldenMushroomEarlyPrice1 = convert_to_hex_weight(goldenMushroomEarlyPrice1)
    goldenMushroomEarlyPrice2 = convert_to_hex_weight(goldenMushroomEarlyPrice2)
    goldenMushroomEarlyPrice34 = convert_to_hex_weight(goldenMushroomEarlyPrice34)
    goldenMushroomMidPrice1 = convert_to_hex_weight(goldenMushroomMidPrice1)
    goldenMushroomMidPrice2 = convert_to_hex_weight(goldenMushroomMidPrice2)
    goldenMushroomMidPrice34 = convert_to_hex_weight(goldenMushroomMidPrice34)
    goldenMushroomLatePrice1 = convert_to_hex_weight(goldenMushroomLatePrice1)
    goldenMushroomLatePrice2 = convert_to_hex_weight(goldenMushroomLatePrice2)
    goldenMushroomLatePrice34 = convert_to_hex_weight(goldenMushroomLatePrice34)

    # Reverse Mushroom: DX
    reverseMushroomEarlyPrice1 = convert_to_hex_weight(reverseMushroomEarlyPrice1)
    reverseMushroomEarlyPrice2 = convert_to_hex_weight(reverseMushroomEarlyPrice2)
    reverseMushroomEarlyPrice34 = convert_to_hex_weight(reverseMushroomEarlyPrice34)
    reverseMushroomMidPrice1 = convert_to_hex_weight(reverseMushroomMidPrice1)
    reverseMushroomMidPrice2 = convert_to_hex_weight(reverseMushroomMidPrice2)
    reverseMushroomMidPrice34 = convert_to_hex_weight(reverseMushroomMidPrice34)
    reverseMushroomLatePrice1 = convert_to_hex_weight(reverseMushroomLatePrice1)
    reverseMushroomLatePrice2 = convert_to_hex_weight(reverseMushroomLatePrice2)
    reverseMushroomLatePrice34 = convert_to_hex_weight(reverseMushroomLatePrice34)

    # Poison Mushroom: DX
    poisonMushroomEarlyPrice1 = convert_to_hex_weight(poisonMushroomEarlyPrice1)
    poisonMushroomEarlyPrice2 = convert_to_hex_weight(poisonMushroomEarlyPrice2)
    poisonMushroomEarlyPrice34 = convert_to_hex_weight(poisonMushroomEarlyPrice34)
    poisonMushroomMidPrice1 = convert_to_hex_weight(poisonMushroomMidPrice1)
    poisonMushroomMidPrice2 = convert_to_hex_weight(poisonMushroomMidPrice2)
    poisonMushroomMidPrice34 = convert_to_hex_weight(poisonMushroomMidPrice34)
    poisonMushroomLatePrice1 = convert_to_hex_weight(poisonMushroomLatePrice1)
    poisonMushroomLatePrice2 = convert_to_hex_weight(poisonMushroomLatePrice2)
    poisonMushroomLatePrice34 = convert_to_hex_weight(poisonMushroomLatePrice34)

    # Triple Poison Mushroom: DX
    triplePoisonMushroomEarlyPrice1 = convert_to_hex_weight(triplePoisonMushroomEarlyPrice1)
    triplePoisonMushroomEarlyPrice2 = convert_to_hex_weight(triplePoisonMushroomEarlyPrice2)
    triplePoisonMushroomEarlyPrice34 = convert_to_hex_weight(triplePoisonMushroomEarlyPrice34)
    triplePoisonMushroomMidPrice1 = convert_to_hex_weight(triplePoisonMushroomMidPrice1)
    triplePoisonMushroomMidPrice2 = convert_to_hex_weight(triplePoisonMushroomMidPrice2)
    triplePoisonMushroomMidPrice34 = convert_to_hex_weight(triplePoisonMushroomMidPrice34)
    triplePoisonMushroomLatePrice1 = convert_to_hex_weight(triplePoisonMushroomLatePrice1)
    triplePoisonMushroomLatePrice2 = convert_to_hex_weight(triplePoisonMushroomLatePrice2)
    triplePoisonMushroomLatePrice34 = convert_to_hex_weight(triplePoisonMushroomLatePrice34)

    # Celluar Shopper: DX
    celluarShopperEarlyPrice1 = convert_to_hex_weight(celluarShopperEarlyPrice1)
    celluarShopperEarlyPrice2 = convert_to_hex_weight(celluarShopperEarlyPrice2)
    celluarShopperEarlyPrice34 = convert_to_hex_weight(celluarShopperEarlyPrice34)
    celluarShopperMidPrice1 = convert_to_hex_weight(celluarShopperMidPrice1)
    celluarShopperMidPrice2 = convert_to_hex_weight(celluarShopperMidPrice2)
    celluarShopperMidPrice34 = convert_to_hex_weight(celluarShopperMidPrice34)
    celluarShopperLatePrice1 = convert_to_hex_weight(celluarShopperLatePrice1)
    celluarShopperLatePrice2 = convert_to_hex_weight(celluarShopperLatePrice2)
    celluarShopperLatePrice34 = convert_to_hex_weight(celluarShopperLatePrice34)

    # Skeleton Key: DX
    skeletonKeyEarlyPrice1 = convert_to_hex_weight(skeletonKeyEarlyPrice1)
    skeletonKeyEarlyPrice2 = convert_to_hex_weight(skeletonKeyEarlyPrice2)
    skeletonKeyEarlyPrice34 = convert_to_hex_weight(skeletonKeyEarlyPrice34)
    skeletonKeyMidPrice1 = convert_to_hex_weight(skeletonKeyMidPrice1)
    skeletonKeyMidPrice2 = convert_to_hex_weight(skeletonKeyMidPrice2)
    skeletonKeyMidPrice34 = convert_to_hex_weight(skeletonKeyMidPrice34)
    skeletonKeyLatePrice1 = convert_to_hex_weight(skeletonKeyLatePrice1)
    skeletonKeyLatePrice2 = convert_to_hex_weight(skeletonKeyLatePrice2)
    skeletonKeyLatePrice34 = convert_to_hex_weight(skeletonKeyLatePrice34)

    # Plunder Chest: DX
    plunderChestEarlyPrice1 = convert_to_hex_weight(plunderChestEarlyPrice1)
    plunderChestEarlyPrice2 = convert_to_hex_weight(plunderChestEarlyPrice2)
    plunderChestEarlyPrice34 = convert_to_hex_weight(plunderChestEarlyPrice34)
    plunderChestMidPrice1 = convert_to_hex_weight(plunderChestMidPrice1)
    plunderChestMidPrice2 = convert_to_hex_weight(plunderChestMidPrice2)
    plunderChestMidPrice34 = convert_to_hex_weight(plunderChestMidPrice34)
    plunderChestLatePrice1 = convert_to_hex_weight(plunderChestLatePrice1)
    plunderChestLatePrice2 = convert_to_hex_weight(plunderChestLatePrice2)
    plunderChestLatePrice34 = convert_to_hex_weight(plunderChestLatePrice34)

    # Gaddbrush: DX
    gaddbrushEarlyPrice1 = convert_to_hex_weight(gaddbrushEarlyPrice1)
    gaddbrushEarlyPrice2 = convert_to_hex_weight(gaddbrushEarlyPrice2)
    gaddbrushEarlyPrice34 = convert_to_hex_weight(gaddbrushEarlyPrice34)
    gaddbrushMidPrice1 = convert_to_hex_weight(gaddbrushMidPrice1)
    gaddbrushMidPrice2 = convert_to_hex_weight(gaddbrushMidPrice2)
    gaddbrushMidPrice34 = convert_to_hex_weight(gaddbrushMidPrice34)
    gaddbrushLatePrice1 = convert_to_hex_weight(gaddbrushLatePrice1)
    gaddbrushLatePrice2 = convert_to_hex_weight(gaddbrushLatePrice2)
    gaddbrushLatePrice34 = convert_to_hex_weight(gaddbrushLatePrice34)

    # Warp Block: DX
    warpBlockEarlyPrice1 = convert_to_hex_weight(warpBlockEarlyPrice1)
    warpBlockEarlyPrice2 = convert_to_hex_weight(warpBlockEarlyPrice2)
    warpBlockEarlyPrice34 = convert_to_hex_weight(warpBlockEarlyPrice34)
    warpBlockMidPrice1 = convert_to_hex_weight(warpBlockMidPrice1)
    warpBlockMidPrice2 = convert_to_hex_weight(warpBlockMidPrice2)
    warpBlockMidPrice34 = convert_to_hex_weight(warpBlockMidPrice34)
    warpBlockLatePrice1 = convert_to_hex_weight(warpBlockLatePrice1)
    warpBlockLatePrice2 = convert_to_hex_weight(warpBlockLatePrice2)
    warpBlockLatePrice34 = convert_to_hex_weight(warpBlockLatePrice34)

    # Fly Guy: DX
    flyGuyEarlyPrice1 = convert_to_hex_weight(flyGuyEarlyPrice1)
    flyGuyEarlyPrice2 = convert_to_hex_weight(flyGuyEarlyPrice2)
    flyGuyEarlyPrice34 = convert_to_hex_weight(flyGuyEarlyPrice34)
    flyGuyMidPrice1 = convert_to_hex_weight(flyGuyMidPrice1)
    flyGuyMidPrice2 = convert_to_hex_weight(flyGuyMidPrice2)
    flyGuyMidPrice34 = convert_to_hex_weight(flyGuyMidPrice34)
    flyGuyLatePrice1 = convert_to_hex_weight(flyGuyLatePrice1)
    flyGuyLatePrice2 = convert_to_hex_weight(flyGuyLatePrice2)
    flyGuyLatePrice34 = convert_to_hex_weight(flyGuyLatePrice34)

    # Plus Block: DX
    plusBlockEarlyPrice1 = convert_to_hex_weight(plusBlockEarlyPrice1)
    plusBlockEarlyPrice2 = convert_to_hex_weight(plusBlockEarlyPrice2)
    plusBlockEarlyPrice34 = convert_to_hex_weight(plusBlockEarlyPrice34)
    plusBlockMidPrice1 = convert_to_hex_weight(plusBlockMidPrice1)
    plusBlockMidPrice2 = convert_to_hex_weight(plusBlockMidPrice2)
    plusBlockMidPrice34 = convert_to_hex_weight(plusBlockMidPrice34)
    plusBlockLatePrice1 = convert_to_hex_weight(plusBlockLatePrice1)
    plusBlockLatePrice2 = convert_to_hex_weight(plusBlockLatePrice2)
    plusBlockLatePrice34 = convert_to_hex_weight(plusBlockLatePrice34)

    # Minus Block: DX
    minusBlockEarlyPrice1 = convert_to_hex_weight(minusBlockEarlyPrice1)
    minusBlockEarlyPrice2 = convert_to_hex_weight(minusBlockEarlyPrice2)
    minusBlockEarlyPrice34 = convert_to_hex_weight(minusBlockEarlyPrice34)
    minusBlockMidPrice1 = convert_to_hex_weight(minusBlockMidPrice1)
    minusBlockMidPrice2 = convert_to_hex_weight(minusBlockMidPrice2)
    minusBlockMidPrice34 = convert_to_hex_weight(minusBlockMidPrice34)
    minusBlockLatePrice1 = convert_to_hex_weight(minusBlockLatePrice1)
    minusBlockLatePrice2 = convert_to_hex_weight(minusBlockLatePrice2)
    minusBlockLatePrice34 = convert_to_hex_weight(minusBlockLatePrice34)

    # Speed Block: DX
    speedBlockEarlyPrice1 = convert_to_hex_weight(speedBlockEarlyPrice1)
    speedBlockEarlyPrice2 = convert_to_hex_weight(speedBlockEarlyPrice2)
    speedBlockEarlyPrice34 = convert_to_hex_weight(speedBlockEarlyPrice34)
    speedBlockMidPrice1 = convert_to_hex_weight(speedBlockMidPrice1)
    speedBlockMidPrice2 = convert_to_hex_weight(speedBlockMidPrice2)
    speedBlockMidPrice34 = convert_to_hex_weight(speedBlockMidPrice34)
    speedBlockLatePrice1 = convert_to_hex_weight(speedBlockLatePrice1)
    speedBlockLatePrice2 = convert_to_hex_weight(speedBlockLatePrice2)
    speedBlockLatePrice34 = convert_to_hex_weight(speedBlockLatePrice34)

    # Slow Block: DX
    slowBlockEarlyPrice1 = convert_to_hex_weight(slowBlockEarlyPrice1)
    slowBlockEarlyPrice2 = convert_to_hex_weight(slowBlockEarlyPrice2)
    slowBlockEarlyPrice34 = convert_to_hex_weight(slowBlockEarlyPrice34)
    slowBlockMidPrice1 = convert_to_hex_weight(slowBlockMidPrice1)
    slowBlockMidPrice2 = convert_to_hex_weight(slowBlockMidPrice2)
    slowBlockMidPrice34 = convert_to_hex_weight(slowBlockMidPrice34)
    slowBlockLatePrice1 = convert_to_hex_weight(slowBlockLatePrice1)
    slowBlockLatePrice2 = convert_to_hex_weight(slowBlockLatePrice2)
    slowBlockLatePrice34 = convert_to_hex_weight(slowBlockLatePrice34)

    # Hidden Block Card: DX
    hiddenBlockCardEarlyPrice1 = convert_to_hex_weight(hiddenBlockCardEarlyPrice1)
    hiddenBlockCardEarlyPrice2 = convert_to_hex_weight(hiddenBlockCardEarlyPrice2)
    hiddenBlockCardEarlyPrice34 = convert_to_hex_weight(hiddenBlockCardEarlyPrice34)
    hiddenBlockCardMidPrice1 = convert_to_hex_weight(hiddenBlockCardMidPrice1)
    hiddenBlockCardMidPrice2 = convert_to_hex_weight(hiddenBlockCardMidPrice2)
    hiddenBlockCardMidPrice34 = convert_to_hex_weight(hiddenBlockCardMidPrice34)
    hiddenBlockCardLatePrice1 = convert_to_hex_weight(hiddenBlockCardLatePrice1)
    hiddenBlockCardLatePrice2 = convert_to_hex_weight(hiddenBlockCardLatePrice2)
    hiddenBlockCardLatePrice34 = convert_to_hex_weight(hiddenBlockCardLatePrice34)

    # Barter Box: DX
    barterBoxEarlyPrice1 = convert_to_hex_weight(barterBoxEarlyPrice1)
    barterBoxEarlyPrice2 = convert_to_hex_weight(barterBoxEarlyPrice2)
    barterBoxEarlyPrice34 = convert_to_hex_weight(barterBoxEarlyPrice34)
    barterBoxMidPrice1 = convert_to_hex_weight(barterBoxMidPrice1)
    barterBoxMidPrice2 = convert_to_hex_weight(barterBoxMidPrice2)
    barterBoxMidPrice34 = convert_to_hex_weight(barterBoxMidPrice34)
    barterBoxLatePrice1 = convert_to_hex_weight(barterBoxLatePrice1)
    barterBoxLatePrice2 = convert_to_hex_weight(barterBoxLatePrice2)
    barterBoxLatePrice34 = convert_to_hex_weight(barterBoxLatePrice34)

    # Super Warp Pipe: DX
    superWarpPipeEarlyPrice1 = convert_to_hex_weight(superWarpPipeEarlyPrice1)
    superWarpPipeEarlyPrice2 = convert_to_hex_weight(superWarpPipeEarlyPrice2)
    superWarpPipeEarlyPrice34 = convert_to_hex_weight(superWarpPipeEarlyPrice34)
    superWarpPipeMidPrice1 = convert_to_hex_weight(superWarpPipeMidPrice1)
    superWarpPipeMidPrice2 = convert_to_hex_weight(superWarpPipeMidPrice2)
    superWarpPipeMidPrice34 = convert_to_hex_weight(superWarpPipeMidPrice34)
    superWarpPipeLatePrice1 = convert_to_hex_weight(superWarpPipeLatePrice1)
    superWarpPipeLatePrice2 = convert_to_hex_weight(superWarpPipeLatePrice2)
    superWarpPipeLatePrice34 = convert_to_hex_weight(superWarpPipeLatePrice34)

    # Chance Time Charm: DX
    chanceTimeCharmEarlyPrice1 = convert_to_hex_weight(chanceTimeCharmEarlyPrice1)
    chanceTimeCharmEarlyPrice2 = convert_to_hex_weight(chanceTimeCharmEarlyPrice2)
    chanceTimeCharmEarlyPrice34 = convert_to_hex_weight(chanceTimeCharmEarlyPrice34)
    chanceTimeCharmMidPrice1 = convert_to_hex_weight(chanceTimeCharmMidPrice1)
    chanceTimeCharmMidPrice2 = convert_to_hex_weight(chanceTimeCharmMidPrice2)
    chanceTimeCharmMidPrice34 = convert_to_hex_weight(chanceTimeCharmMidPrice34)
    chanceTimeCharmLatePrice1 = convert_to_hex_weight(chanceTimeCharmLatePrice1)
    chanceTimeCharmLatePrice2 = convert_to_hex_weight(chanceTimeCharmLatePrice2)
    chanceTimeCharmLatePrice34 = convert_to_hex_weight(chanceTimeCharmLatePrice34)

    # Wacky Watch: DX
    wackyWatchEarlyPrice1 = convert_to_hex_weight(wackyWatchEarlyPrice1)
    wackyWatchEarlyPrice2 = convert_to_hex_weight(wackyWatchEarlyPrice2)
    wackyWatchEarlyPrice34 = convert_to_hex_weight(wackyWatchEarlyPrice34)
    wackyWatchMidPrice1 = convert_to_hex_weight(wackyWatchMidPrice1)
    wackyWatchMidPrice2 = convert_to_hex_weight(wackyWatchMidPrice2)
    wackyWatchMidPrice34 = convert_to_hex_weight(wackyWatchMidPrice34)
    wackyWatchLatePrice1 = convert_to_hex_weight(wackyWatchLatePrice1)
    wackyWatchLatePrice2 = convert_to_hex_weight(wackyWatchLatePrice2)
    wackyWatchLatePrice34 = convert_to_hex_weight(wackyWatchLatePrice34)

    # Bowser Phone: DX
    bowserPhoneEarlyPrice1 = convert_to_hex_weight(bowserPhoneEarlyPrice1)
    bowserPhoneEarlyPrice2 = convert_to_hex_weight(bowserPhoneEarlyPrice2)
    bowserPhoneEarlyPrice34 = convert_to_hex_weight(bowserPhoneEarlyPrice34)
    bowserPhoneMidPrice1 = convert_to_hex_weight(bowserPhoneMidPrice1)
    bowserPhoneMidPrice2 = convert_to_hex_weight(bowserPhoneMidPrice2)
    bowserPhoneMidPrice34 = convert_to_hex_weight(bowserPhoneMidPrice34)
    bowserPhoneLatePrice1 = convert_to_hex_weight(bowserPhoneLatePrice1)
    bowserPhoneLatePrice2 = convert_to_hex_weight(bowserPhoneLatePrice2)
    bowserPhoneLatePrice34 = convert_to_hex_weight(bowserPhoneLatePrice34)

    # Double Dip: DX
    doubleDipEarlyPrice1 = convert_to_hex_weight(doubleDipEarlyPrice1)
    doubleDipEarlyPrice2 = convert_to_hex_weight(doubleDipEarlyPrice2)
    doubleDipEarlyPrice34 = convert_to_hex_weight(doubleDipEarlyPrice34)
    doubleDipMidPrice1 = convert_to_hex_weight(doubleDipMidPrice1)
    doubleDipMidPrice2 = convert_to_hex_weight(doubleDipMidPrice2)
    doubleDipMidPrice34 = convert_to_hex_weight(doubleDipMidPrice34)
    doubleDipLatePrice1 = convert_to_hex_weight(doubleDipLatePrice1)
    doubleDipLatePrice2 = convert_to_hex_weight(doubleDipLatePrice2)
    doubleDipLatePrice34 = convert_to_hex_weight(doubleDipLatePrice34)


    minCoins = convert_to_hex_weight(minCoins)

    generatedCode = getItemShopPricesFourDX(minCoins, miniMushroomEarlyPrice1, miniMushroomEarlyPrice2, miniMushroomEarlyPrice34, miniMushroomMidPrice1, miniMushroomMidPrice2, miniMushroomMidPrice34, miniMushroomLatePrice1, miniMushroomLatePrice2, miniMushroomLatePrice34, megaMushroomEarlyPrice1, megaMushroomEarlyPrice2, megaMushroomEarlyPrice34, megaMushroomMidPrice1, megaMushroomMidPrice2, megaMushroomMidPrice34, megaMushroomLatePrice1, megaMushroomLatePrice2, megaMushroomLatePrice34, superMiniMushroomEarlyPrice1, superMiniMushroomEarlyPrice2, superMiniMushroomEarlyPrice34, superMiniMushroomMidPrice1, superMiniMushroomMidPrice2, superMiniMushroomMidPrice34, superMiniMushroomLatePrice1, superMiniMushroomLatePrice2, superMiniMushroomLatePrice34, superMegaMushroomEarlyPrice1, superMegaMushroomEarlyPrice2, superMegaMushroomEarlyPrice34, superMegaMushroomMidPrice1, superMegaMushroomMidPrice2, superMegaMushroomMidPrice34, superMegaMushroomLatePrice1, superMegaMushroomLatePrice2, superMegaMushroomLatePrice34, miniMegaHammerEarlyPrice1, miniMegaHammerEarlyPrice2, miniMegaHammerEarlyPrice34, miniMegaHammerMidPrice1, miniMegaHammerMidPrice2, miniMegaHammerMidPrice34, miniMegaHammerLatePrice1, miniMegaHammerLatePrice2, miniMegaHammerLatePrice34, warpPipeEarlyPrice1, warpPipeEarlyPrice2, warpPipeEarlyPrice34, warpPipeMidPrice1, warpPipeMidPrice2, warpPipeMidPrice34, warpPipeLatePrice1, warpPipeLatePrice2, warpPipeLatePrice34, swapCardEarlyPrice1, swapCardEarlyPrice2, swapCardEarlyPrice34, swapCardMidPrice1, swapCardMidPrice2, swapCardMidPrice34, swapCardLatePrice1, swapCardLatePrice2, swapCardLatePrice34, sparkyStickerEarlyPrice1, sparkyStickerEarlyPrice2, sparkyStickerEarlyPrice34, sparkyStickerMidPrice1, sparkyStickerMidPrice2, sparkyStickerMidPrice34, sparkyStickerLatePrice1, sparkyStickerLatePrice2, sparkyStickerLatePrice34, gaddlightEarlyPrice1, gaddlightEarlyPrice2, gaddlightEarlyPrice34, gaddlightMidPrice1, gaddlightMidPrice2, gaddlightMidPrice34, gaddlightLatePrice1, gaddlightLatePrice2, gaddlightLatePrice34, chompCallEarlyPrice1, chompCallEarlyPrice2, chompCallEarlyPrice34, chompCallMidPrice1, chompCallMidPrice2, chompCallMidPrice34, chompCallLatePrice1, chompCallLatePrice2, chompCallLatePrice34, bowserSuitEarlyPrice1, bowserSuitEarlyPrice2, bowserSuitEarlyPrice34, bowserSuitMidPrice1, bowserSuitMidPrice2, bowserSuitMidPrice34, bowserSuitLatePrice1, bowserSuitLatePrice2, bowserSuitLatePrice34, crystalBallEarlyPrice1, crystalBallEarlyPrice2, crystalBallEarlyPrice34, crystalBallMidPrice1, crystalBallMidPrice2, crystalBallMidPrice34, crystalBallLatePrice1, crystalBallLatePrice2, crystalBallLatePrice34, magicLampEarlyPrice1, magicLampEarlyPrice2, magicLampEarlyPrice34, magicLampMidPrice1, magicLampMidPrice2, magicLampMidPrice34, magicLampLatePrice1, magicLampLatePrice2, magicLampLatePrice34, itemBagEarlyPrice1, itemBagEarlyPrice2, itemBagEarlyPrice34, itemBagMidPrice1, itemBagMidPrice2, itemBagMidPrice34, itemBagLatePrice1, itemBagLatePrice2, itemBagLatePrice34, mushroomEarlyPrice1, mushroomEarlyPrice2, mushroomEarlyPrice34, mushroomMidPrice1, mushroomMidPrice2, mushroomMidPrice34, mushroomLatePrice1, mushroomLatePrice2, mushroomLatePrice34, goldenMushroomEarlyPrice1, goldenMushroomEarlyPrice2, goldenMushroomEarlyPrice34, goldenMushroomMidPrice1, goldenMushroomMidPrice2, goldenMushroomMidPrice34, goldenMushroomLatePrice1, goldenMushroomLatePrice2, goldenMushroomLatePrice34, reverseMushroomEarlyPrice1, reverseMushroomEarlyPrice2, reverseMushroomEarlyPrice34, reverseMushroomMidPrice1, reverseMushroomMidPrice2, reverseMushroomMidPrice34, reverseMushroomLatePrice1, reverseMushroomLatePrice2, reverseMushroomLatePrice34, poisonMushroomEarlyPrice1, poisonMushroomEarlyPrice2, poisonMushroomEarlyPrice34, poisonMushroomMidPrice1, poisonMushroomMidPrice2, poisonMushroomMidPrice34, poisonMushroomLatePrice1, poisonMushroomLatePrice2, poisonMushroomLatePrice34, triplePoisonMushroomEarlyPrice1, triplePoisonMushroomEarlyPrice2, triplePoisonMushroomEarlyPrice34, triplePoisonMushroomMidPrice1, triplePoisonMushroomMidPrice2, triplePoisonMushroomMidPrice34, triplePoisonMushroomLatePrice1, triplePoisonMushroomLatePrice2, triplePoisonMushroomLatePrice34, celluarShopperEarlyPrice1, celluarShopperEarlyPrice2, celluarShopperEarlyPrice34, celluarShopperMidPrice1, celluarShopperMidPrice2, celluarShopperMidPrice34, celluarShopperLatePrice1, celluarShopperLatePrice2, celluarShopperLatePrice34, skeletonKeyEarlyPrice1, skeletonKeyEarlyPrice2, skeletonKeyEarlyPrice34, skeletonKeyMidPrice1, skeletonKeyMidPrice2, skeletonKeyMidPrice34, skeletonKeyLatePrice1, skeletonKeyLatePrice2, skeletonKeyLatePrice34, plunderChestEarlyPrice1, plunderChestEarlyPrice2, plunderChestEarlyPrice34, plunderChestMidPrice1, plunderChestMidPrice2, plunderChestMidPrice34, plunderChestLatePrice1, plunderChestLatePrice2, plunderChestLatePrice34, gaddbrushEarlyPrice1, gaddbrushEarlyPrice2, gaddbrushEarlyPrice34, gaddbrushMidPrice1, gaddbrushMidPrice2, gaddbrushMidPrice34, gaddbrushLatePrice1, gaddbrushLatePrice2, gaddbrushLatePrice34, warpBlockEarlyPrice1, warpBlockEarlyPrice2, warpBlockEarlyPrice34, warpBlockMidPrice1, warpBlockMidPrice2, warpBlockMidPrice34, warpBlockLatePrice1, warpBlockLatePrice2, warpBlockLatePrice34, flyGuyEarlyPrice1, flyGuyEarlyPrice2, flyGuyEarlyPrice34, flyGuyMidPrice1, flyGuyMidPrice2, flyGuyMidPrice34, flyGuyLatePrice1, flyGuyLatePrice2, flyGuyLatePrice34, plusBlockEarlyPrice1, plusBlockEarlyPrice2, plusBlockEarlyPrice34, plusBlockMidPrice1, plusBlockMidPrice2, plusBlockMidPrice34, plusBlockLatePrice1, plusBlockLatePrice2, plusBlockLatePrice34, minusBlockEarlyPrice1, minusBlockEarlyPrice2, minusBlockEarlyPrice34, minusBlockMidPrice1, minusBlockMidPrice2, minusBlockMidPrice34, minusBlockLatePrice1, minusBlockLatePrice2, minusBlockLatePrice34, speedBlockEarlyPrice1, speedBlockEarlyPrice2, speedBlockEarlyPrice34, speedBlockMidPrice1, speedBlockMidPrice2, speedBlockMidPrice34, speedBlockLatePrice1, speedBlockLatePrice2, speedBlockLatePrice34, slowBlockEarlyPrice1, slowBlockEarlyPrice2, slowBlockEarlyPrice34, slowBlockMidPrice1, slowBlockMidPrice2, slowBlockMidPrice34, slowBlockLatePrice1, slowBlockLatePrice2, slowBlockLatePrice34, bowserPhoneEarlyPrice1, bowserPhoneEarlyPrice2, bowserPhoneEarlyPrice34, bowserPhoneMidPrice1, bowserPhoneMidPrice2, bowserPhoneMidPrice34, bowserPhoneLatePrice1, bowserPhoneLatePrice2, bowserPhoneLatePrice34, doubleDipEarlyPrice1, doubleDipEarlyPrice2, doubleDipEarlyPrice34, doubleDipMidPrice1, doubleDipMidPrice2, doubleDipMidPrice34, doubleDipLatePrice1, doubleDipLatePrice2, doubleDipLatePrice34, hiddenBlockCardEarlyPrice1, hiddenBlockCardEarlyPrice2, hiddenBlockCardEarlyPrice34, hiddenBlockCardMidPrice1, hiddenBlockCardMidPrice2, hiddenBlockCardMidPrice34, hiddenBlockCardLatePrice1, hiddenBlockCardLatePrice2, hiddenBlockCardLatePrice34, barterBoxEarlyPrice1, barterBoxEarlyPrice2, barterBoxEarlyPrice34, barterBoxMidPrice1, barterBoxMidPrice2, barterBoxMidPrice34, barterBoxLatePrice1, barterBoxLatePrice2, barterBoxLatePrice34, superWarpPipeEarlyPrice1, superWarpPipeEarlyPrice2, superWarpPipeEarlyPrice34, superWarpPipeMidPrice1, superWarpPipeMidPrice2, superWarpPipeMidPrice34, superWarpPipeLatePrice1, superWarpPipeLatePrice2, superWarpPipeLatePrice34, chanceTimeCharmEarlyPrice1, chanceTimeCharmEarlyPrice2, chanceTimeCharmEarlyPrice34, chanceTimeCharmMidPrice1, chanceTimeCharmMidPrice2, chanceTimeCharmMidPrice34, chanceTimeCharmLatePrice1, chanceTimeCharmLatePrice2, chanceTimeCharmLatePrice34, wackyWatchEarlyPrice1, wackyWatchEarlyPrice2, wackyWatchEarlyPrice34, wackyWatchMidPrice1, wackyWatchMidPrice2, wackyWatchMidPrice34, wackyWatchLatePrice1, wackyWatchLatePrice2, wackyWatchLatePrice34)
    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)

    print("Generated code copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

def itemsEvent_mp4ShopPrices(miniMushroomEarlyPrice1 = "5", miniMushroomEarlyPrice2 = "5", miniMushroomEarlyPrice34 = "5", miniMushroomMidPrice1 = "5", miniMushroomMidPrice2 = "5", miniMushroomMidPrice34 = "5", miniMushroomLatePrice1 = "5", miniMushroomLatePrice2 = "5", miniMushroomLatePrice34 = "5", megaMushroomEarlyPrice1 = "5", megaMushroomEarlyPrice2 = "5", megaMushroomEarlyPrice34 = "5", megaMushroomMidPrice1 = "5", megaMushroomMidPrice2 = "5", megaMushroomMidPrice34 = "5", megaMushroomLatePrice1 = "5", megaMushroomLatePrice2 = "5", megaMushroomLatePrice34 = "5", superMiniMushroomEarlyPrice1 = "15", superMiniMushroomEarlyPrice2 = "15", superMiniMushroomEarlyPrice34 = "15", superMiniMushroomMidPrice1 = "15", superMiniMushroomMidPrice2 = "10", superMiniMushroomMidPrice34 = "15", superMiniMushroomLatePrice1 = "15", superMiniMushroomLatePrice2 = "15", superMiniMushroomLatePrice34 = "15", superMegaMushroomEarlyPrice1 = "15", superMegaMushroomEarlyPrice2 = "15", superMegaMushroomEarlyPrice34 = "15", superMegaMushroomMidPrice1 = "15", superMegaMushroomMidPrice2 = "15", superMegaMushroomMidPrice34 = "15", superMegaMushroomLatePrice1 = "15", superMegaMushroomLatePrice2 = "15", superMegaMushroomLatePrice34 = "15", miniMegaHammerEarlyPrice1 = "10", miniMegaHammerEarlyPrice2 = "10", miniMegaHammerEarlyPrice34 = "10", miniMegaHammerMidPrice1 = "10", miniMegaHammerMidPrice2 = "10", miniMegaHammerMidPrice34 = "10", miniMegaHammerLatePrice1 = "10", miniMegaHammerLatePrice2 = "10", miniMegaHammerLatePrice34 = "10", warpPipeEarlyPrice1 = "10", warpPipeEarlyPrice2 = "10", warpPipeEarlyPrice34 = "10", warpPipeMidPrice1 = "10", warpPipeMidPrice2 = "10", warpPipeMidPrice34 = "10", warpPipeLatePrice1 = "10", warpPipeLatePrice2 = "10", warpPipeLatePrice34 = "10", swapCardEarlyPrice1 = "15", swapCardEarlyPrice2 = "15", swapCardEarlyPrice34 = "15", swapCardMidPrice1 = "15", swapCardMidPrice2 = "15", swapCardMidPrice34 = "15", swapCardLatePrice1 = "15", swapCardLatePrice2 = "15", swapCardLatePrice34 = "15", sparkyStickerEarlyPrice1 = "15", sparkyStickerEarlyPrice2 = "15", sparkyStickerEarlyPrice34 = "15", sparkyStickerMidPrice1 = "15", sparkyStickerMidPrice2 = "15", sparkyStickerMidPrice34 = "5", sparkyStickerLatePrice1 = "15", sparkyStickerLatePrice2 = "15", sparkyStickerLatePrice34 = "15", gaddlightEarlyPrice1 = "15", gaddlightEarlyPrice2 = "15", gaddlightEarlyPrice34 = "15", gaddlightMidPrice1 = "15", gaddlightMidPrice2 = "15", gaddlightMidPrice34 = "15", gaddlightLatePrice1 = "15", gaddlightLatePrice2 = "15", gaddlightLatePrice34 = "10", chompCallEarlyPrice1 = "15", chompCallEarlyPrice2 = "15", chompCallEarlyPrice34 = "15", chompCallMidPrice1 = "15", chompCallMidPrice2 = "10", chompCallMidPrice34 = "15", chompCallLatePrice1 = "10", chompCallLatePrice2 = "15", chompCallLatePrice34 = "15", bowserSuitEarlyPrice1 = "0", bowserSuitEarlyPrice2 = "0", bowserSuitEarlyPrice34 = "0", bowserSuitMidPrice1 = "0", bowserSuitMidPrice2 = "0", bowserSuitMidPrice34 = "0", bowserSuitLatePrice1 = "0", bowserSuitLatePrice2 = "0", bowserSuitLatePrice34 = "12", crystalBallEarlyPrice1 = "25", crystalBallEarlyPrice2 = "25", crystalBallEarlyPrice34 = "25", crystalBallMidPrice1 = "25", crystalBallMidPrice2 = "25", crystalBallMidPrice34 = "25", crystalBallLatePrice1 = "25", crystalBallLatePrice2 = "25", crystalBallLatePrice34 = "25", magicLampEarlyPrice1 = "30", magicLampEarlyPrice2 = "30", magicLampEarlyPrice34 = "30", magicLampMidPrice1 = "30", magicLampMidPrice2 = "30", magicLampMidPrice34 = "30", magicLampLatePrice1 = "30", magicLampLatePrice2 = "30", magicLampLatePrice34 = "30", itemBagEarlyPrice1 = "30", itemBagEarlyPrice2 = "30", itemBagEarlyPrice34 = "30", itemBagMidPrice1 = "30", itemBagMidPrice2 = "30", itemBagMidPrice34 = "30", itemBagLatePrice1 = "30", itemBagLatePrice2 = "30", itemBagLatePrice34 = "30"):
    def get_capsule_value(capsule):
        try:
            return capsule.get()
        except:
            return 0

    # Mini Mushroom
    miniMushroomEarlyPrice1 = get_capsule_value(miniMushroomEarlyPrice1) or "5"
    miniMushroomEarlyPrice2 = get_capsule_value(miniMushroomEarlyPrice2) or "5"
    miniMushroomEarlyPrice34 = get_capsule_value(miniMushroomEarlyPrice34) or "5"
    miniMushroomMidPrice1 = get_capsule_value(miniMushroomMidPrice1) or "5"
    miniMushroomMidPrice2 = get_capsule_value(miniMushroomMidPrice2) or "5"
    miniMushroomMidPrice34 = get_capsule_value(miniMushroomMidPrice34) or "5"
    miniMushroomLatePrice1 = get_capsule_value(miniMushroomLatePrice1) or "5"
    miniMushroomLatePrice2 = get_capsule_value(miniMushroomLatePrice2) or "5"
    miniMushroomLatePrice34 = get_capsule_value(miniMushroomLatePrice34) or "5"
    
    # Mega Mushroom
    megaMushroomEarlyPrice1 = get_capsule_value(megaMushroomEarlyPrice1) or "5"
    megaMushroomEarlyPrice2 = get_capsule_value(megaMushroomEarlyPrice2) or "5"
    megaMushroomEarlyPrice34 = get_capsule_value(megaMushroomEarlyPrice34) or "5"
    megaMushroomMidPrice1 = get_capsule_value(megaMushroomMidPrice1) or "5"
    megaMushroomMidPrice2 = get_capsule_value(megaMushroomMidPrice2) or "5"
    megaMushroomMidPrice34 = get_capsule_value(megaMushroomMidPrice34) or "5"
    megaMushroomLatePrice1 = get_capsule_value(megaMushroomLatePrice1) or "5"
    megaMushroomLatePrice2 = get_capsule_value(megaMushroomLatePrice2) or "5"
    megaMushroomLatePrice34 = get_capsule_value(megaMushroomLatePrice34) or "5"

    # Super Mini Mushroom
    superMiniMushroomEarlyPrice1 = get_capsule_value(superMiniMushroomEarlyPrice1) or "15"
    superMiniMushroomEarlyPrice2 = get_capsule_value(superMiniMushroomEarlyPrice2) or "15"
    superMiniMushroomEarlyPrice34 = get_capsule_value(superMiniMushroomEarlyPrice34) or "15"
    superMiniMushroomMidPrice1 = get_capsule_value(superMiniMushroomMidPrice1) or "15"
    superMiniMushroomMidPrice2 = get_capsule_value(superMiniMushroomMidPrice2) or "15"
    superMiniMushroomMidPrice34 = get_capsule_value(superMiniMushroomMidPrice34) or "15"
    superMiniMushroomLatePrice1 = get_capsule_value(superMiniMushroomLatePrice1) or "15"
    superMiniMushroomLatePrice2 = get_capsule_value(superMiniMushroomLatePrice2) or "15"
    superMiniMushroomLatePrice34 = get_capsule_value(superMiniMushroomLatePrice34) or "15"

    # Super Mega Mushroom
    superMegaMushroomEarlyPrice1 = get_capsule_value(superMegaMushroomEarlyPrice1) or "15"
    superMegaMushroomEarlyPrice2 = get_capsule_value(superMegaMushroomEarlyPrice2) or "15"
    superMegaMushroomEarlyPrice34 = get_capsule_value(superMegaMushroomEarlyPrice34) or "15"
    superMegaMushroomMidPrice1 = get_capsule_value(superMegaMushroomMidPrice1) or "15"
    superMegaMushroomMidPrice2 = get_capsule_value(superMegaMushroomMidPrice2) or "15"
    superMegaMushroomMidPrice34 = get_capsule_value(superMegaMushroomMidPrice34) or "15"
    superMegaMushroomLatePrice1 = get_capsule_value(superMegaMushroomLatePrice1) or "15"
    superMegaMushroomLatePrice2 = get_capsule_value(superMegaMushroomLatePrice2) or "15"
    superMegaMushroomLatePrice34 = get_capsule_value(superMegaMushroomLatePrice34) or "15"

    # Mini Mega Hammer
    miniMegaHammerEarlyPrice1 = get_capsule_value(miniMegaHammerEarlyPrice1) or "10"
    miniMegaHammerEarlyPrice2 = get_capsule_value(miniMegaHammerEarlyPrice2) or "10"
    miniMegaHammerEarlyPrice34 = get_capsule_value(miniMegaHammerEarlyPrice34) or "10"
    miniMegaHammerMidPrice1 = get_capsule_value(miniMegaHammerMidPrice1) or "10"
    miniMegaHammerMidPrice2 = get_capsule_value(miniMegaHammerMidPrice2) or "10"
    miniMegaHammerMidPrice34 = get_capsule_value(miniMegaHammerMidPrice34) or "10"
    miniMegaHammerLatePrice1 = get_capsule_value(miniMegaHammerLatePrice1) or "10"
    miniMegaHammerLatePrice2 = get_capsule_value(miniMegaHammerLatePrice2) or "10"
    miniMegaHammerLatePrice34 = get_capsule_value(miniMegaHammerLatePrice34) or "10"

    # Warp Pipe
    warpPipeEarlyPrice1 = get_capsule_value(warpPipeEarlyPrice1) or "10"
    warpPipeEarlyPrice2 = get_capsule_value(warpPipeEarlyPrice2) or "10"
    warpPipeEarlyPrice34 = get_capsule_value(warpPipeEarlyPrice34) or "10"
    warpPipeMidPrice1 = get_capsule_value(warpPipeMidPrice1) or "10"
    warpPipeMidPrice2 = get_capsule_value(warpPipeMidPrice2) or "10"
    warpPipeMidPrice34 = get_capsule_value(warpPipeMidPrice34) or "10"
    warpPipeLatePrice1 = get_capsule_value(warpPipeLatePrice1) or "10"
    warpPipeLatePrice2 = get_capsule_value(warpPipeLatePrice2) or "10"
    warpPipeLatePrice34 = get_capsule_value(warpPipeLatePrice34) or "10"

    # Swap Card
    swapCardEarlyPrice1 = get_capsule_value(swapCardEarlyPrice1) or "15"
    swapCardEarlyPrice2 = get_capsule_value(swapCardEarlyPrice2) or "15"
    swapCardEarlyPrice34 = get_capsule_value(swapCardEarlyPrice34) or "15"
    swapCardMidPrice1 = get_capsule_value(swapCardMidPrice1) or "15"
    swapCardMidPrice2 = get_capsule_value(swapCardMidPrice2) or "15"
    swapCardMidPrice34 = get_capsule_value(swapCardMidPrice34) or "15"
    swapCardLatePrice1 = get_capsule_value(swapCardLatePrice1) or "15"
    swapCardLatePrice2 = get_capsule_value(swapCardLatePrice2) or "15"
    swapCardLatePrice34 = get_capsule_value(swapCardLatePrice34) or "15"

    # Sparky Sticker
    sparkyStickerEarlyPrice1 = get_capsule_value(sparkyStickerEarlyPrice1) or "15"
    sparkyStickerEarlyPrice2 = get_capsule_value(sparkyStickerEarlyPrice2) or "15"
    sparkyStickerEarlyPrice34 = get_capsule_value(sparkyStickerEarlyPrice34) or "15"
    sparkyStickerMidPrice1 = get_capsule_value(sparkyStickerMidPrice1) or "15"
    sparkyStickerMidPrice2 = get_capsule_value(sparkyStickerMidPrice2) or "15"
    sparkyStickerMidPrice34 = get_capsule_value(sparkyStickerMidPrice34) or "15"
    sparkyStickerLatePrice1 = get_capsule_value(sparkyStickerLatePrice1) or "15"
    sparkyStickerLatePrice2 = get_capsule_value(sparkyStickerLatePrice2) or "15"
    sparkyStickerLatePrice34 = get_capsule_value(sparkyStickerLatePrice34) or "15"

    # Gaddlight
    gaddlightEarlyPrice1 = get_capsule_value(gaddlightEarlyPrice1) or "15"
    gaddlightEarlyPrice2 = get_capsule_value(gaddlightEarlyPrice2) or "15"
    gaddlightEarlyPrice34 = get_capsule_value(gaddlightEarlyPrice34) or "15"
    gaddlightMidPrice1 = get_capsule_value(gaddlightMidPrice1) or "15"
    gaddlightMidPrice2 = get_capsule_value(gaddlightMidPrice2) or "15"
    gaddlightMidPrice34 = get_capsule_value(gaddlightMidPrice34) or "15"
    gaddlightLatePrice1 = get_capsule_value(gaddlightLatePrice1) or "15"
    gaddlightLatePrice2 = get_capsule_value(gaddlightLatePrice2) or "15"
    gaddlightLatePrice34 = get_capsule_value(gaddlightLatePrice34) or "15"

    # Chomp Call
    chompCallEarlyPrice1 = get_capsule_value(chompCallEarlyPrice1) or "15"
    chompCallEarlyPrice2 = get_capsule_value(chompCallEarlyPrice2) or "15"
    chompCallEarlyPrice34 = get_capsule_value(chompCallEarlyPrice34) or "15"
    chompCallMidPrice1 = get_capsule_value(chompCallMidPrice1) or "15"
    chompCallMidPrice2 = get_capsule_value(chompCallMidPrice2) or "15"
    chompCallMidPrice34 = get_capsule_value(chompCallMidPrice34) or "15"
    chompCallLatePrice1 = get_capsule_value(chompCallLatePrice1) or "15"
    chompCallLatePrice2 = get_capsule_value(chompCallLatePrice2) or "15"
    chompCallLatePrice34 = get_capsule_value(chompCallLatePrice34) or "15"

    # Bowser Suit
    bowserSuitEarlyPrice1 = get_capsule_value(bowserSuitEarlyPrice1) or "0"
    bowserSuitEarlyPrice2 = get_capsule_value(bowserSuitEarlyPrice2) or "0"
    bowserSuitEarlyPrice34 = get_capsule_value(bowserSuitEarlyPrice34) or "0"
    bowserSuitMidPrice1 = get_capsule_value(bowserSuitMidPrice1) or "0"
    bowserSuitMidPrice2 = get_capsule_value(bowserSuitMidPrice2) or "0"
    bowserSuitMidPrice34 = get_capsule_value(bowserSuitMidPrice34) or "0"
    bowserSuitLatePrice1 = get_capsule_value(bowserSuitLatePrice1) or "0"
    bowserSuitLatePrice2 = get_capsule_value(bowserSuitLatePrice2) or "0"
    bowserSuitLatePrice34 = get_capsule_value(bowserSuitLatePrice34) or "0"

    # Crystal Ball
    crystalBallEarlyPrice1 = get_capsule_value(crystalBallEarlyPrice1) or "25"
    crystalBallEarlyPrice2 = get_capsule_value(crystalBallEarlyPrice2) or "25"
    crystalBallEarlyPrice34 = get_capsule_value(crystalBallEarlyPrice34) or "25"
    crystalBallMidPrice1 = get_capsule_value(crystalBallMidPrice1) or "25"
    crystalBallMidPrice2 = get_capsule_value(crystalBallMidPrice2) or "25"
    crystalBallMidPrice34 = get_capsule_value(crystalBallMidPrice34) or "25"
    crystalBallLatePrice1 = get_capsule_value(crystalBallLatePrice1) or "25"
    crystalBallLatePrice2 = get_capsule_value(crystalBallLatePrice2) or "25"
    crystalBallLatePrice34 = get_capsule_value(crystalBallLatePrice34) or "25"

    # Magic Lamp
    magicLampEarlyPrice1 = get_capsule_value(magicLampEarlyPrice1) or "30"
    magicLampEarlyPrice2 = get_capsule_value(magicLampEarlyPrice2) or "30"
    magicLampEarlyPrice34 = get_capsule_value(magicLampEarlyPrice34) or "30"
    magicLampMidPrice1 = get_capsule_value(magicLampMidPrice1) or "30"
    magicLampMidPrice2 = get_capsule_value(magicLampMidPrice2) or "30"
    magicLampMidPrice34 = get_capsule_value(magicLampMidPrice34) or "30"
    magicLampLatePrice1 = get_capsule_value(magicLampLatePrice1) or "30"
    magicLampLatePrice2 = get_capsule_value(magicLampLatePrice2) or "30"
    magicLampLatePrice34 = get_capsule_value(magicLampLatePrice34) or "30"

    # Item Bag
    itemBagEarlyPrice1 = get_capsule_value(itemBagEarlyPrice1) or "30"
    itemBagEarlyPrice2 = get_capsule_value(itemBagEarlyPrice2) or "30"
    itemBagEarlyPrice34 = get_capsule_value(itemBagEarlyPrice34) or "30"
    itemBagMidPrice1 = get_capsule_value(itemBagMidPrice1) or "30"
    itemBagMidPrice2 = get_capsule_value(itemBagMidPrice2) or "30"
    itemBagMidPrice34 = get_capsule_value(itemBagMidPrice34) or "30"
    itemBagLatePrice1 = get_capsule_value(itemBagLatePrice1) or "30"
    itemBagLatePrice2 = get_capsule_value(itemBagLatePrice2) or "30"
    itemBagLatePrice34 = get_capsule_value(itemBagLatePrice34) or "30"

    minCoins = find_lowest_integer(*[
        int(miniMushroomEarlyPrice1), int(miniMushroomEarlyPrice2), int(miniMushroomEarlyPrice34), 
        int(miniMushroomMidPrice1), int(miniMushroomMidPrice2), int(miniMushroomMidPrice34),
        int(miniMushroomLatePrice1), int(miniMushroomLatePrice2), int(miniMushroomLatePrice34),
        int(megaMushroomEarlyPrice1), int(megaMushroomEarlyPrice2), int(megaMushroomEarlyPrice34), 
        int(megaMushroomMidPrice1), int(megaMushroomMidPrice2), int(megaMushroomMidPrice34),
        int(megaMushroomLatePrice1), int(megaMushroomLatePrice2), int(megaMushroomLatePrice34),
        int(superMiniMushroomEarlyPrice1), int(superMiniMushroomEarlyPrice2), int(superMiniMushroomEarlyPrice34),
        int(superMiniMushroomMidPrice1), int(superMiniMushroomMidPrice2), int(superMiniMushroomMidPrice34),
        int(superMiniMushroomLatePrice1), int(superMiniMushroomLatePrice2), int(superMiniMushroomLatePrice34),
        int(superMegaMushroomEarlyPrice1), int(superMegaMushroomEarlyPrice2), int(superMegaMushroomEarlyPrice34),
        int(superMegaMushroomMidPrice1), int(superMegaMushroomMidPrice2), int(superMegaMushroomMidPrice34),
        int(superMegaMushroomLatePrice1), int(superMegaMushroomLatePrice2), int(superMegaMushroomLatePrice34),
        int(miniMegaHammerEarlyPrice1), int(miniMegaHammerEarlyPrice2), int(miniMegaHammerEarlyPrice34),
        int(miniMegaHammerMidPrice1), int(miniMegaHammerMidPrice2), int(miniMegaHammerMidPrice34),
        int(miniMegaHammerLatePrice1), int(miniMegaHammerLatePrice2), int(miniMegaHammerLatePrice34),
        int(warpPipeEarlyPrice1), int(warpPipeEarlyPrice2), int(warpPipeEarlyPrice34),
        int(warpPipeMidPrice1), int(warpPipeMidPrice2), int(warpPipeMidPrice34),
        int(warpPipeLatePrice1), int(warpPipeLatePrice2), int(warpPipeLatePrice34),
        int(swapCardEarlyPrice1), int(swapCardEarlyPrice2), int(swapCardEarlyPrice34),
        int(swapCardMidPrice1), int(swapCardMidPrice2), int(swapCardMidPrice34),
        int(swapCardLatePrice1), int(swapCardLatePrice2), int(swapCardLatePrice34),
        int(sparkyStickerEarlyPrice1), int(sparkyStickerEarlyPrice2), int(sparkyStickerEarlyPrice34),
        int(sparkyStickerMidPrice1), int(sparkyStickerMidPrice2), int(sparkyStickerMidPrice34),
        int(sparkyStickerLatePrice1), int(sparkyStickerLatePrice2), int(sparkyStickerLatePrice34),
        int(gaddlightEarlyPrice1), int(gaddlightEarlyPrice2), int(gaddlightEarlyPrice34),
        int(gaddlightMidPrice1), int(gaddlightMidPrice2), int(gaddlightMidPrice34),
        int(gaddlightLatePrice1), int(gaddlightLatePrice2), int(gaddlightLatePrice34),
        int(chompCallEarlyPrice1), int(chompCallEarlyPrice2), int(chompCallEarlyPrice34),
        int(chompCallMidPrice1), int(chompCallMidPrice2), int(chompCallMidPrice34),
        int(chompCallLatePrice1), int(chompCallLatePrice2), int(chompCallLatePrice34),
        int(bowserSuitEarlyPrice1), int(bowserSuitEarlyPrice2), int(bowserSuitEarlyPrice34),
        int(bowserSuitMidPrice1), int(bowserSuitMidPrice2), int(bowserSuitMidPrice34),
        int(bowserSuitLatePrice1), int(bowserSuitLatePrice2), int(bowserSuitLatePrice34),
        int(crystalBallEarlyPrice1), int(crystalBallEarlyPrice2), int(crystalBallEarlyPrice34),
        int(crystalBallMidPrice1), int(crystalBallMidPrice2), int(crystalBallMidPrice34),
        int(crystalBallLatePrice1), int(crystalBallLatePrice2), int(crystalBallLatePrice34),
        int(magicLampEarlyPrice1), int(magicLampEarlyPrice2), int(magicLampEarlyPrice34),
        int(magicLampMidPrice1), int(magicLampMidPrice2), int(magicLampMidPrice34),
        int(magicLampLatePrice1), int(magicLampLatePrice2), int(magicLampLatePrice34),
        int(itemBagEarlyPrice1), int(itemBagEarlyPrice2), int(itemBagEarlyPrice34),
        int(itemBagMidPrice1), int(itemBagMidPrice2), int(itemBagMidPrice34),
        int(itemBagLatePrice1), int(itemBagLatePrice2), int(itemBagLatePrice34)
    ])


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


    # Mini Mushroom
    miniMushroomEarlyPrice1 = convert_to_hex_weight(miniMushroomEarlyPrice1)
    miniMushroomEarlyPrice2 = convert_to_hex_weight(miniMushroomEarlyPrice2)
    miniMushroomEarlyPrice34 = convert_to_hex_weight(miniMushroomEarlyPrice34)
    miniMushroomMidPrice1 = convert_to_hex_weight(miniMushroomMidPrice1)
    miniMushroomMidPrice2 = convert_to_hex_weight(miniMushroomMidPrice2)
    miniMushroomMidPrice34 = convert_to_hex_weight(miniMushroomMidPrice34)
    miniMushroomLatePrice1 = convert_to_hex_weight(miniMushroomLatePrice1)
    miniMushroomLatePrice2 = convert_to_hex_weight(miniMushroomLatePrice2)
    miniMushroomLatePrice34 = convert_to_hex_weight(miniMushroomLatePrice34)
    
    # Mega Mushroom
    megaMushroomEarlyPrice1 = convert_to_hex_weight(megaMushroomEarlyPrice1)
    megaMushroomEarlyPrice2 = convert_to_hex_weight(megaMushroomEarlyPrice2)
    megaMushroomEarlyPrice34 = convert_to_hex_weight(megaMushroomEarlyPrice34)
    megaMushroomMidPrice1 = convert_to_hex_weight(megaMushroomMidPrice1)
    megaMushroomMidPrice2 = convert_to_hex_weight(megaMushroomMidPrice2)
    megaMushroomMidPrice34 = convert_to_hex_weight(megaMushroomMidPrice34)
    megaMushroomLatePrice1 = convert_to_hex_weight(megaMushroomLatePrice1)
    megaMushroomLatePrice2 = convert_to_hex_weight(megaMushroomLatePrice2)
    megaMushroomLatePrice34 = convert_to_hex_weight(megaMushroomLatePrice34)

    # Super Mini Mushroom
    superMiniMushroomEarlyPrice1 = convert_to_hex_weight(superMiniMushroomEarlyPrice1)
    superMiniMushroomEarlyPrice2 = convert_to_hex_weight(superMiniMushroomEarlyPrice2)
    superMiniMushroomEarlyPrice34 = convert_to_hex_weight(superMiniMushroomEarlyPrice34)
    superMiniMushroomMidPrice1 = convert_to_hex_weight(superMiniMushroomMidPrice1)
    superMiniMushroomMidPrice2 = convert_to_hex_weight(superMiniMushroomMidPrice2)
    superMiniMushroomMidPrice34 = convert_to_hex_weight(superMiniMushroomMidPrice34)
    superMiniMushroomLatePrice1 = convert_to_hex_weight(superMiniMushroomLatePrice1)
    superMiniMushroomLatePrice2 = convert_to_hex_weight(superMiniMushroomLatePrice2)
    superMiniMushroomLatePrice34 = convert_to_hex_weight(superMiniMushroomLatePrice34)

    # Super Mega Mushroom
    superMegaMushroomEarlyPrice1 = convert_to_hex_weight(superMegaMushroomEarlyPrice1)
    superMegaMushroomEarlyPrice2 = convert_to_hex_weight(superMegaMushroomEarlyPrice2)
    superMegaMushroomEarlyPrice34 = convert_to_hex_weight(superMegaMushroomEarlyPrice34)
    superMegaMushroomMidPrice1 = convert_to_hex_weight(superMegaMushroomMidPrice1)
    superMegaMushroomMidPrice2 = convert_to_hex_weight(superMegaMushroomMidPrice2)
    superMegaMushroomMidPrice34 = convert_to_hex_weight(superMegaMushroomMidPrice34)
    superMegaMushroomLatePrice1 = convert_to_hex_weight(superMegaMushroomLatePrice1)
    superMegaMushroomLatePrice2 = convert_to_hex_weight(superMegaMushroomLatePrice2)
    superMegaMushroomLatePrice34 = convert_to_hex_weight(superMegaMushroomLatePrice34)

    # Mini Mega Hammer
    miniMegaHammerEarlyPrice1 = convert_to_hex_weight(miniMegaHammerEarlyPrice1)
    miniMegaHammerEarlyPrice2 = convert_to_hex_weight(miniMegaHammerEarlyPrice2)
    miniMegaHammerEarlyPrice34 = convert_to_hex_weight(miniMegaHammerEarlyPrice34)
    miniMegaHammerMidPrice1 = convert_to_hex_weight(miniMegaHammerMidPrice1)
    miniMegaHammerMidPrice2 = convert_to_hex_weight(miniMegaHammerMidPrice2)
    miniMegaHammerMidPrice34 = convert_to_hex_weight(miniMegaHammerMidPrice34)
    miniMegaHammerLatePrice1 = convert_to_hex_weight(miniMegaHammerLatePrice1)
    miniMegaHammerLatePrice2 = convert_to_hex_weight(miniMegaHammerLatePrice2)
    miniMegaHammerLatePrice34 = convert_to_hex_weight(miniMegaHammerLatePrice34)

    # Warp Pipe
    warpPipeEarlyPrice1 = convert_to_hex_weight(warpPipeEarlyPrice1)
    warpPipeEarlyPrice2 = convert_to_hex_weight(warpPipeEarlyPrice2)
    warpPipeEarlyPrice34 = convert_to_hex_weight(warpPipeEarlyPrice34)
    warpPipeMidPrice1 = convert_to_hex_weight(warpPipeMidPrice1)
    warpPipeMidPrice2 = convert_to_hex_weight(warpPipeMidPrice2)
    warpPipeMidPrice34 = convert_to_hex_weight(warpPipeMidPrice34)
    warpPipeLatePrice1 = convert_to_hex_weight(warpPipeLatePrice1)
    warpPipeLatePrice2 = convert_to_hex_weight(warpPipeLatePrice2)
    warpPipeLatePrice34 = convert_to_hex_weight(warpPipeLatePrice34)

    # Swap Card
    swapCardEarlyPrice1 = convert_to_hex_weight(swapCardEarlyPrice1)
    swapCardEarlyPrice2 = convert_to_hex_weight(swapCardEarlyPrice2)
    swapCardEarlyPrice34 = convert_to_hex_weight(swapCardEarlyPrice34)
    swapCardMidPrice1 = convert_to_hex_weight(swapCardMidPrice1)
    swapCardMidPrice2 = convert_to_hex_weight(swapCardMidPrice2)
    swapCardMidPrice34 = convert_to_hex_weight(swapCardMidPrice34)
    swapCardLatePrice1 = convert_to_hex_weight(swapCardLatePrice1)
    swapCardLatePrice2 = convert_to_hex_weight(swapCardLatePrice2)
    swapCardLatePrice34 = convert_to_hex_weight(swapCardLatePrice34)

    # Sparky Sticker
    sparkyStickerEarlyPrice1 = convert_to_hex_weight(sparkyStickerEarlyPrice1)
    sparkyStickerEarlyPrice2 = convert_to_hex_weight(sparkyStickerEarlyPrice2)
    sparkyStickerEarlyPrice34 = convert_to_hex_weight(sparkyStickerEarlyPrice34)
    sparkyStickerMidPrice1 = convert_to_hex_weight(sparkyStickerMidPrice1)
    sparkyStickerMidPrice2 = convert_to_hex_weight(sparkyStickerMidPrice2)
    sparkyStickerMidPrice34 = convert_to_hex_weight(sparkyStickerMidPrice34)
    sparkyStickerLatePrice1 = convert_to_hex_weight(sparkyStickerLatePrice1)
    sparkyStickerLatePrice2 = convert_to_hex_weight(sparkyStickerLatePrice2)
    sparkyStickerLatePrice34 = convert_to_hex_weight(sparkyStickerLatePrice34)

    # Gaddlight
    gaddlightEarlyPrice1 = convert_to_hex_weight(gaddlightEarlyPrice1)
    gaddlightEarlyPrice2 = convert_to_hex_weight(gaddlightEarlyPrice2)
    gaddlightEarlyPrice34 = convert_to_hex_weight(gaddlightEarlyPrice34)
    gaddlightMidPrice1 = convert_to_hex_weight(gaddlightMidPrice1)
    gaddlightMidPrice2 = convert_to_hex_weight(gaddlightMidPrice2)
    gaddlightMidPrice34 = convert_to_hex_weight(gaddlightMidPrice34)
    gaddlightLatePrice1 = convert_to_hex_weight(gaddlightLatePrice1)
    gaddlightLatePrice2 = convert_to_hex_weight(gaddlightLatePrice2)
    gaddlightLatePrice34 = convert_to_hex_weight(gaddlightLatePrice34)

    # Chomp Call
    chompCallEarlyPrice1 = convert_to_hex_weight(chompCallEarlyPrice1)
    chompCallEarlyPrice2 = convert_to_hex_weight(chompCallEarlyPrice2)
    chompCallEarlyPrice34 = convert_to_hex_weight(chompCallEarlyPrice34)
    chompCallMidPrice1 = convert_to_hex_weight(chompCallMidPrice1)
    chompCallMidPrice2 = convert_to_hex_weight(chompCallMidPrice2)
    chompCallMidPrice34 = convert_to_hex_weight(chompCallMidPrice34)
    chompCallLatePrice1 = convert_to_hex_weight(chompCallLatePrice1)
    chompCallLatePrice2 = convert_to_hex_weight(chompCallLatePrice2)
    chompCallLatePrice34 = convert_to_hex_weight(chompCallLatePrice34)

    # Bowser Suit
    bowserSuitEarlyPrice1 = convert_to_hex_weight(bowserSuitEarlyPrice1)
    bowserSuitEarlyPrice2 = convert_to_hex_weight(bowserSuitEarlyPrice2)
    bowserSuitEarlyPrice34 = convert_to_hex_weight(bowserSuitEarlyPrice34)
    bowserSuitMidPrice1 = convert_to_hex_weight(bowserSuitMidPrice1)
    bowserSuitMidPrice2 = convert_to_hex_weight(bowserSuitMidPrice2)
    bowserSuitMidPrice34 = convert_to_hex_weight(bowserSuitMidPrice34)
    bowserSuitLatePrice1 = convert_to_hex_weight(bowserSuitLatePrice1)
    bowserSuitLatePrice2 = convert_to_hex_weight(bowserSuitLatePrice2)
    bowserSuitLatePrice34 = convert_to_hex_weight(bowserSuitLatePrice34)

    # Crystal Ball
    crystalBallEarlyPrice1 = convert_to_hex_weight(crystalBallEarlyPrice1)
    crystalBallEarlyPrice2 = convert_to_hex_weight(crystalBallEarlyPrice2)
    crystalBallEarlyPrice34 = convert_to_hex_weight(crystalBallEarlyPrice34)
    crystalBallMidPrice1 = convert_to_hex_weight(crystalBallMidPrice1)
    crystalBallMidPrice2 = convert_to_hex_weight(crystalBallMidPrice2)
    crystalBallMidPrice34 = convert_to_hex_weight(crystalBallMidPrice34)
    crystalBallLatePrice1 = convert_to_hex_weight(crystalBallLatePrice1)
    crystalBallLatePrice2 = convert_to_hex_weight(crystalBallLatePrice2)
    crystalBallLatePrice34 = convert_to_hex_weight(crystalBallLatePrice34)

    # Magic Lamp
    magicLampEarlyPrice1 = convert_to_hex_weight(magicLampEarlyPrice1)
    magicLampEarlyPrice2 = convert_to_hex_weight(magicLampEarlyPrice2)
    magicLampEarlyPrice34 = convert_to_hex_weight(magicLampEarlyPrice34)
    magicLampMidPrice1 = convert_to_hex_weight(magicLampMidPrice1)
    magicLampMidPrice2 = convert_to_hex_weight(magicLampMidPrice2)
    magicLampMidPrice34 = convert_to_hex_weight(magicLampMidPrice34)
    magicLampLatePrice1 = convert_to_hex_weight(magicLampLatePrice1)
    magicLampLatePrice2 = convert_to_hex_weight(magicLampLatePrice2)
    magicLampLatePrice34 = convert_to_hex_weight(magicLampLatePrice34)

    # Item Bag
    itemBagEarlyPrice1 = convert_to_hex_weight(itemBagEarlyPrice1)
    itemBagEarlyPrice2 = convert_to_hex_weight(itemBagEarlyPrice2)
    itemBagEarlyPrice34 = convert_to_hex_weight(itemBagEarlyPrice34)
    itemBagMidPrice1 = convert_to_hex_weight(itemBagMidPrice1)
    itemBagMidPrice2 = convert_to_hex_weight(itemBagMidPrice2)
    itemBagMidPrice34 = convert_to_hex_weight(itemBagMidPrice34)
    itemBagLatePrice1 = convert_to_hex_weight(itemBagLatePrice1)
    itemBagLatePrice2 = convert_to_hex_weight(itemBagLatePrice2)
    itemBagLatePrice34 = convert_to_hex_weight(itemBagLatePrice34)

    minCoins = convert_to_hex_weight(minCoins)

    generatedCode = getItemShopPricesFour(minCoins, miniMushroomEarlyPrice1, miniMushroomEarlyPrice2, miniMushroomEarlyPrice34, miniMushroomMidPrice1, miniMushroomMidPrice2, miniMushroomMidPrice34, miniMushroomLatePrice1, miniMushroomLatePrice2, miniMushroomLatePrice34, megaMushroomEarlyPrice1, megaMushroomEarlyPrice2, megaMushroomEarlyPrice34, megaMushroomMidPrice1, megaMushroomMidPrice2, megaMushroomMidPrice34, megaMushroomLatePrice1, megaMushroomLatePrice2, megaMushroomLatePrice34, superMiniMushroomEarlyPrice1, superMiniMushroomEarlyPrice2, superMiniMushroomEarlyPrice34, superMiniMushroomMidPrice1, superMiniMushroomMidPrice2, superMiniMushroomMidPrice34, superMiniMushroomLatePrice1, superMiniMushroomLatePrice2, superMiniMushroomLatePrice34, superMegaMushroomEarlyPrice1, superMegaMushroomEarlyPrice2, superMegaMushroomEarlyPrice34, superMegaMushroomMidPrice1, superMegaMushroomMidPrice2, superMegaMushroomMidPrice34, superMegaMushroomLatePrice1, superMegaMushroomLatePrice2, superMegaMushroomLatePrice34, miniMegaHammerEarlyPrice1, miniMegaHammerEarlyPrice2, miniMegaHammerEarlyPrice34, miniMegaHammerMidPrice1, miniMegaHammerMidPrice2, miniMegaHammerMidPrice34, miniMegaHammerLatePrice1, miniMegaHammerLatePrice2, miniMegaHammerLatePrice34, warpPipeEarlyPrice1, warpPipeEarlyPrice2, warpPipeEarlyPrice34, warpPipeMidPrice1, warpPipeMidPrice2, warpPipeMidPrice34, warpPipeLatePrice1, warpPipeLatePrice2, warpPipeLatePrice34, swapCardEarlyPrice1, swapCardEarlyPrice2, swapCardEarlyPrice34, swapCardMidPrice1, swapCardMidPrice2, swapCardMidPrice34, swapCardLatePrice1, swapCardLatePrice2, swapCardLatePrice34, sparkyStickerEarlyPrice1, sparkyStickerEarlyPrice2, sparkyStickerEarlyPrice34, sparkyStickerMidPrice1, sparkyStickerMidPrice2, sparkyStickerMidPrice34, sparkyStickerLatePrice1, sparkyStickerLatePrice2, sparkyStickerLatePrice34, gaddlightEarlyPrice1, gaddlightEarlyPrice2, gaddlightEarlyPrice34, gaddlightMidPrice1, gaddlightMidPrice2, gaddlightMidPrice34, gaddlightLatePrice1, gaddlightLatePrice2, gaddlightLatePrice34, chompCallEarlyPrice1, chompCallEarlyPrice2, chompCallEarlyPrice34, chompCallMidPrice1, chompCallMidPrice2, chompCallMidPrice34, chompCallLatePrice1, chompCallLatePrice2, chompCallLatePrice34, bowserSuitEarlyPrice1, bowserSuitEarlyPrice2, bowserSuitEarlyPrice34, bowserSuitMidPrice1, bowserSuitMidPrice2, bowserSuitMidPrice34, bowserSuitLatePrice1, bowserSuitLatePrice2, bowserSuitLatePrice34, crystalBallEarlyPrice1, crystalBallEarlyPrice2, crystalBallEarlyPrice34, crystalBallMidPrice1, crystalBallMidPrice2, crystalBallMidPrice34, crystalBallLatePrice1, crystalBallLatePrice2, crystalBallLatePrice34, magicLampEarlyPrice1, magicLampEarlyPrice2, magicLampEarlyPrice34, magicLampMidPrice1, magicLampMidPrice2, magicLampMidPrice34, magicLampLatePrice1, magicLampLatePrice2, magicLampLatePrice34, itemBagEarlyPrice1, itemBagEarlyPrice2, itemBagEarlyPrice34, itemBagMidPrice1, itemBagMidPrice2, itemBagMidPrice34, itemBagLatePrice1, itemBagLatePrice2, itemBagLatePrice34)
    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)

    print("Generated code copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)