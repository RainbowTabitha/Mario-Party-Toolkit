# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

from codes.marioParty4 import *
from functions import *

import csv
import math
import pyperclip

def itemsEvent_mp4ShopOddsDX(miniMushroomEarlyOdds1 = "0", miniMushroomEarlyOdds2 = "0", miniMushroomEarlyOdds34 = "0", miniMushroomMidOdds1 = "0", miniMushroomMidOdds2 = "0", miniMushroomMidOdds34 = "0", miniMushroomLateOdds1 = "0", miniMushroomLateOdds2 = "0", miniMushroomLateOdds34 = "0", megaMushroomEarlyOdds1 = "0", megaMushroomEarlyOdds2 = "0", megaMushroomEarlyOdds34 = "0", megaMushroomMidOdds1 = "0", megaMushroomMidOdds2 = "0", megaMushroomMidOdds34 = "0", megaMushroomLateOdds1 = "0", megaMushroomLateOdds2 = "0", megaMushroomLateOdds34 = "0", superMiniMushroomEarlyOdds1 = "0", superMiniMushroomEarlyOdds2 = "0", superMiniMushroomEarlyOdds34 = "0", superMiniMushroomMidOdds1 = "0", superMiniMushroomMidOdds2 = "0", superMiniMushroomMidOdds34 = "0", superMiniMushroomLateOdds1 = "0", superMiniMushroomLateOdds2 = "0", superMiniMushroomLateOdds34 = "0", superMegaMushroomEarlyOdds1 = "0", superMegaMushroomEarlyOdds2 = "0", superMegaMushroomEarlyOdds34 = "0", superMegaMushroomMidOdds1 = "0", superMegaMushroomMidOdds2 = "0", superMegaMushroomMidOdds34 = "0", superMegaMushroomLateOdds1 = "0", superMegaMushroomLateOdds2 = "0", superMegaMushroomLateOdds34 = "0", miniMegaHammerEarlyOdds1 = "0", miniMegaHammerEarlyOdds2 = "0", miniMegaHammerEarlyOdds34 = "0", miniMegaHammerMidOdds1 = "0", miniMegaHammerMidOdds2 = "0", miniMegaHammerMidOdds34 = "0", miniMegaHammerLateOdds1 = "0", miniMegaHammerLateOdds2 = "0", miniMegaHammerLateOdds34 = "0", warpPipeEarlyOdds1 = "0", warpPipeEarlyOdds2 = "0", warpPipeEarlyOdds34 = "0", warpPipeMidOdds1 = "0", warpPipeMidOdds2 = "0", warpPipeMidOdds34 = "0", warpPipeLateOdds1 = "0", warpPipeLateOdds2 = "0", warpPipeLateOdds34 = "0", swapCardEarlyOdds1 = "0", swapCardEarlyOdds2 = "0", swapCardEarlyOdds34 = "0", swapCardMidOdds1 = "0", swapCardMidOdds2 = "0", swapCardMidOdds34 = "0", swapCardLateOdds1 = "0", swapCardLateOdds2 = "0", swapCardLateOdds34 = "0", sparkyStickerEarlyOdds1 = "0", sparkyStickerEarlyOdds2 = "0", sparkyStickerEarlyOdds34 = "0", sparkyStickerMidOdds1 = "0", sparkyStickerMidOdds2 = "0", sparkyStickerMidOdds34 = "0", sparkyStickerLateOdds1 = "0", sparkyStickerLateOdds2 = "0", sparkyStickerLateOdds34 = "0", gaddlightEarlyOdds1 = "0", gaddlightEarlyOdds2 = "0", gaddlightEarlyOdds34 = "0", gaddlightMidOdds1 = "0", gaddlightMidOdds2 = "0", gaddlightMidOdds34 = "0", gaddlightLateOdds1 = "0", gaddlightLateOdds2 = "0", gaddlightLateOdds34 = "0", chompCallEarlyOdds1 = "0", chompCallEarlyOdds2 = "0", chompCallEarlyOdds34 = "0", chompCallMidOdds1 = "0", chompCallMidOdds2 = "0", chompCallMidOdds34 = "0", chompCallLateOdds1 = "0", chompCallLateOdds2 = "0", chompCallLateOdds34 = "0", bowserSuitEarlyOdds1 = "0", bowserSuitEarlyOdds2 = "0", bowserSuitEarlyOdds34 = "0", bowserSuitMidOdds1 = "0", bowserSuitMidOdds2 = "0", bowserSuitMidOdds34 = "0", bowserSuitLateOdds1 = "0", bowserSuitLateOdds2 = "0", bowserSuitLateOdds34 = "0", crystalBallEarlyOdds1 = "0", crystalBallEarlyOdds2 = "0", crystalBallEarlyOdds34 = "0", crystalBallMidOdds1 = "0", crystalBallMidOdds2 = "0", crystalBallMidOdds34 = "0", crystalBallLateOdds1 = "0", crystalBallLateOdds2 = "0", crystalBallLateOdds34 = "0", magicLampEarlyOdds1 = "0", magicLampEarlyOdds2 = "0", magicLampEarlyOdds34 = "0", magicLampMidOdds1 = "0", magicLampMidOdds2 = "0", magicLampMidOdds34 = "0", magicLampLateOdds1 = "0", magicLampLateOdds2 = "0", magicLampLateOdds34 = "0", itemBagEarlyOdds1 = "0", itemBagEarlyOdds2 = "0", itemBagEarlyOdds34 = "0", itemBagMidOdds1 = "0", itemBagMidOdds2 = "0", itemBagMidOdds34 = "0", itemBagLateOdds1 = "0", itemBagLateOdds2 = "0", itemBagLateOdds34 = "0", mushroomEarlyOdds1 = "0", mushroomEarlyOdds2 = "0", mushroomEarlyOdds34 = "0", mushroomMidOdds1 = "0", mushroomMidOdds2 = "0", mushroomMidOdds34 = "0", mushroomLateOdds1 = "0", mushroomLateOdds2 = "0", mushroomLateOdds34 = "0", goldenMushroomEarlyOdds1 = "0", goldenMushroomEarlyOdds2 = "0", goldenMushroomEarlyOdds34 = "0", goldenMushroomMidOdds1 = "0", goldenMushroomMidOdds2 = "0", goldenMushroomMidOdds34 = "0", goldenMushroomLateOdds1 = "0", goldenMushroomLateOdds2 = "0", goldenMushroomLateOdds34 = "0", reverseMushroomEarlyOdds1 = "0", reverseMushroomEarlyOdds2 = "0", reverseMushroomEarlyOdds34 = "0", reverseMushroomMidOdds1 = "0", reverseMushroomMidOdds2 = "0", reverseMushroomMidOdds34 = "0", reverseMushroomLateOdds1 = "0", reverseMushroomLateOdds2 = "0", reverseMushroomLateOdds34 = "0", poisonMushroomEarlyOdds1 = "0", poisonMushroomEarlyOdds2 = "0", poisonMushroomEarlyOdds34 = "0", poisonMushroomMidOdds1 = "0", poisonMushroomMidOdds2 = "0", poisonMushroomMidOdds34 = "0", poisonMushroomLateOdds1 = "0", poisonMushroomLateOdds2 = "0", poisonMushroomLateOdds34 = "0", triplePoisonMushroomEarlyOdds1 = "0", triplePoisonMushroomEarlyOdds2 = "0", triplePoisonMushroomEarlyOdds34 = "0", triplePoisonMushroomMidOdds1 = "0", triplePoisonMushroomMidOdds2 = "0", triplePoisonMushroomMidOdds34 = "0", triplePoisonMushroomLateOdds1 = "0", triplePoisonMushroomLateOdds2 = "0", triplePoisonMushroomLateOdds34 = "0", celluarShopperEarlyOdds1 = "0", celluarShopperEarlyOdds2 = "0", celluarShopperEarlyOdds34 = "0", celluarShopperMidOdds1 = "0", celluarShopperMidOdds2 = "0", celluarShopperMidOdds34 = "0", celluarShopperLateOdds1 = "0", celluarShopperLateOdds2 = "0", celluarShopperLateOdds34 = "0", skeletonKeyEarlyOdds1 = "0", skeletonKeyEarlyOdds2 = "0", skeletonKeyEarlyOdds34 = "0", skeletonKeyMidOdds1 = "0", skeletonKeyMidOdds2 = "0", skeletonKeyMidOdds34 = "0", skeletonKeyLateOdds1 = "0", skeletonKeyLateOdds2 = "0", skeletonKeyLateOdds34 = "0", plunderChestEarlyOdds1 = "0", plunderChestEarlyOdds2 = "0", plunderChestEarlyOdds34 = "0", plunderChestMidOdds1 = "0", plunderChestMidOdds2 = "0", plunderChestMidOdds34 = "0", plunderChestLateOdds1 = "0", plunderChestLateOdds2 = "0", plunderChestLateOdds34 = "0", gaddbrushEarlyOdds1 = "0", gaddbrushEarlyOdds2 = "0", gaddbrushEarlyOdds34 = "0", gaddbrushMidOdds1 = "0", gaddbrushMidOdds2 = "0", gaddbrushMidOdds34 = "0", gaddbrushLateOdds1 = "0", gaddbrushLateOdds2 = "0", gaddbrushLateOdds34 = "0", warpBlockEarlyOdds1 = "0", warpBlockEarlyOdds2 = "0", warpBlockEarlyOdds34 = "0", warpBlockMidOdds1 = "0", warpBlockMidOdds2 = "0", warpBlockMidOdds34 = "0", warpBlockLateOdds1 = "0", warpBlockLateOdds2 = "0", warpBlockLateOdds34 = "0", flyGuyEarlyOdds1 = "0", flyGuyEarlyOdds2 = "0", flyGuyEarlyOdds34 = "0", flyGuyMidOdds1 = "0", flyGuyMidOdds2 = "0", flyGuyMidOdds34 = "0", flyGuyLateOdds1 = "0", flyGuyLateOdds2 = "0", flyGuyLateOdds34 = "0", plusBlockEarlyOdds1 = "0", plusBlockEarlyOdds2 = "0", plusBlockEarlyOdds34 = "0", plusBlockMidOdds1 = "0", plusBlockMidOdds2 = "0", plusBlockMidOdds34 = "0", plusBlockLateOdds1 = "0", plusBlockLateOdds2 = "0", plusBlockLateOdds34 = "0", minusBlockEarlyOdds1 = "0", minusBlockEarlyOdds2 = "0", minusBlockEarlyOdds34 = "0", minusBlockMidOdds1 = "0", minusBlockMidOdds2 = "0", minusBlockMidOdds34 = "0", minusBlockLateOdds1 = "0", minusBlockLateOdds2 = "0", minusBlockLateOdds34 = "0", speedBlockEarlyOdds1 = "0", speedBlockEarlyOdds2 = "0", speedBlockEarlyOdds34 = "0", speedBlockMidOdds1 = "0", speedBlockMidOdds2 = "0", speedBlockMidOdds34 = "0", speedBlockLateOdds1 = "0", speedBlockLateOdds2 = "0", speedBlockLateOdds34 = "0", slowBlockEarlyOdds1 = "0", slowBlockEarlyOdds2 = "0", slowBlockEarlyOdds34 = "0", slowBlockMidOdds1 = "0", slowBlockMidOdds2 = "0", slowBlockMidOdds34 = "0", slowBlockLateOdds1 = "0", slowBlockLateOdds2 = "0", slowBlockLateOdds34 = "0", bowserPhoneEarlyOdds1 = "0", bowserPhoneEarlyOdds2 = "0", bowserPhoneEarlyOdds34 = "0", bowserPhoneMidOdds1 = "0", bowserPhoneMidOdds2 = "0", bowserPhoneMidOdds34 = "0", bowserPhoneLateOdds1 = "0", bowserPhoneLateOdds2 = "0", bowserPhoneLateOdds34 = "0", doubleDipEarlyOdds1 = "0", doubleDipEarlyOdds2 = "0", doubleDipEarlyOdds34 = "0", doubleDipMidOdds1 = "0", doubleDipMidOdds2 = "0", doubleDipMidOdds34 = "0", doubleDipLateOdds1 = "0", doubleDipLateOdds2 = "0", doubleDipLateOdds34 = "0", hiddenBlockCardEarlyOdds1 = "0", hiddenBlockCardEarlyOdds2 = "0", hiddenBlockCardEarlyOdds34 = "0", hiddenBlockCardMidOdds1 = "0", hiddenBlockCardMidOdds2 = "0", hiddenBlockCardMidOdds34 = "0", hiddenBlockCardLateOdds1 = "0", hiddenBlockCardLateOdds2 = "0", hiddenBlockCardLateOdds34 = "0", barterBoxEarlyOdds1 = "0", barterBoxEarlyOdds2 = "0", barterBoxEarlyOdds34 = "0", barterBoxMidOdds1 = "0", barterBoxMidOdds2 = "0", barterBoxMidOdds34 = "0", barterBoxLateOdds1 = "0", barterBoxLateOdds2 = "0", barterBoxLateOdds34 = "0", superWarpPipeEarlyOdds1 = "0", superWarpPipeEarlyOdds2 = "0", superWarpPipeEarlyOdds34 = "0", superWarpPipeMidOdds1 = "0", superWarpPipeMidOdds2 = "0", superWarpPipeMidOdds34 = "0", superWarpPipeLateOdds1 = "0", superWarpPipeLateOdds2 = "0", superWarpPipeLateOdds34 = "0", chanceTimeCharmEarlyOdds1 = "0", chanceTimeCharmEarlyOdds2 = "0", chanceTimeCharmEarlyOdds34 = "0", chanceTimeCharmMidOdds1 = "0", chanceTimeCharmMidOdds2 = "0", chanceTimeCharmMidOdds34 = "0", chanceTimeCharmLateOdds1 = "0", chanceTimeCharmLateOdds2 = "0", chanceTimeCharmLateOdds34 = "0", wackyWatchEarlyOdds1 = "0", wackyWatchEarlyOdds2 = "0", wackyWatchEarlyOdds34 = "0", wackyWatchMidOdds1 = "0", wackyWatchMidOdds2 = "0", wackyWatchMidOdds34 = "0", wackyWatchLateOdds1 = "0", wackyWatchLateOdds2 = "0", wackyWatchLateOdds34 = "0"):
    # Mini Mushroom
    miniMushroomEarlyOdds1 = get_capsule_value(miniMushroomEarlyOdds1)
    miniMushroomEarlyOdds2 = get_capsule_value(miniMushroomEarlyOdds2)
    miniMushroomEarlyOdds34 = get_capsule_value(miniMushroomEarlyOdds34)
    miniMushroomMidOdds1 = get_capsule_value(miniMushroomMidOdds1)
    miniMushroomMidOdds2 = get_capsule_value(miniMushroomMidOdds2)
    miniMushroomMidOdds34 = get_capsule_value(miniMushroomMidOdds34)
    miniMushroomLateOdds1 = get_capsule_value(miniMushroomLateOdds1)
    miniMushroomLateOdds2 = get_capsule_value(miniMushroomLateOdds2)
    miniMushroomLateOdds34 = get_capsule_value(miniMushroomLateOdds34)
    
    # Mega Mushroom
    megaMushroomEarlyOdds1 = get_capsule_value(megaMushroomEarlyOdds1)
    megaMushroomEarlyOdds2 = get_capsule_value(megaMushroomEarlyOdds2)
    megaMushroomEarlyOdds34 = get_capsule_value(megaMushroomEarlyOdds34)
    megaMushroomMidOdds1 = get_capsule_value(megaMushroomMidOdds1)
    megaMushroomMidOdds2 = get_capsule_value(megaMushroomMidOdds2)
    megaMushroomMidOdds34 = get_capsule_value(megaMushroomMidOdds34)
    megaMushroomLateOdds1 = get_capsule_value(megaMushroomLateOdds1)
    megaMushroomLateOdds2 = get_capsule_value(megaMushroomLateOdds2)
    megaMushroomLateOdds34 = get_capsule_value(megaMushroomLateOdds34)

    # Super Mini Mushroom
    superMiniMushroomEarlyOdds1 = get_capsule_value(superMiniMushroomEarlyOdds1)
    superMiniMushroomEarlyOdds2 = get_capsule_value(superMiniMushroomEarlyOdds2)
    superMiniMushroomEarlyOdds34 = get_capsule_value(superMiniMushroomEarlyOdds34)
    superMiniMushroomMidOdds1 = get_capsule_value(superMiniMushroomMidOdds1)
    superMiniMushroomMidOdds2 = get_capsule_value(superMiniMushroomMidOdds2)
    superMiniMushroomMidOdds34 = get_capsule_value(superMiniMushroomMidOdds34)
    superMiniMushroomLateOdds1 = get_capsule_value(superMiniMushroomLateOdds1)
    superMiniMushroomLateOdds2 = get_capsule_value(superMiniMushroomLateOdds2)
    superMiniMushroomLateOdds34 = get_capsule_value(superMiniMushroomLateOdds34)

    # Super Mega Mushroom
    superMegaMushroomEarlyOdds1 = get_capsule_value(superMegaMushroomEarlyOdds1)
    superMegaMushroomEarlyOdds2 = get_capsule_value(superMegaMushroomEarlyOdds2)
    superMegaMushroomEarlyOdds34 = get_capsule_value(superMegaMushroomEarlyOdds34)
    superMegaMushroomMidOdds1 = get_capsule_value(superMegaMushroomMidOdds1)
    superMegaMushroomMidOdds2 = get_capsule_value(superMegaMushroomMidOdds2)
    superMegaMushroomMidOdds34 = get_capsule_value(superMegaMushroomMidOdds34)
    superMegaMushroomLateOdds1 = get_capsule_value(superMegaMushroomLateOdds1)
    superMegaMushroomLateOdds2 = get_capsule_value(superMegaMushroomLateOdds2)
    superMegaMushroomLateOdds34 = get_capsule_value(superMegaMushroomLateOdds34)

    # Mini Mega Hammer
    miniMegaHammerEarlyOdds1 = get_capsule_value(miniMegaHammerEarlyOdds1)
    miniMegaHammerEarlyOdds2 = get_capsule_value(miniMegaHammerEarlyOdds2)
    miniMegaHammerEarlyOdds34 = get_capsule_value(miniMegaHammerEarlyOdds34)
    miniMegaHammerMidOdds1 = get_capsule_value(miniMegaHammerMidOdds1)
    miniMegaHammerMidOdds2 = get_capsule_value(miniMegaHammerMidOdds2)
    miniMegaHammerMidOdds34 = get_capsule_value(miniMegaHammerMidOdds34)
    miniMegaHammerLateOdds1 = get_capsule_value(miniMegaHammerLateOdds1)
    miniMegaHammerLateOdds2 = get_capsule_value(miniMegaHammerLateOdds2)
    miniMegaHammerLateOdds34 = get_capsule_value(miniMegaHammerLateOdds34)

    # Warp Pipe
    warpPipeEarlyOdds1 = get_capsule_value(warpPipeEarlyOdds1)
    warpPipeEarlyOdds2 = get_capsule_value(warpPipeEarlyOdds2)
    warpPipeEarlyOdds34 = get_capsule_value(warpPipeEarlyOdds34)
    warpPipeMidOdds1 = get_capsule_value(warpPipeMidOdds1)
    warpPipeMidOdds2 = get_capsule_value(warpPipeMidOdds2)
    warpPipeMidOdds34 = get_capsule_value(warpPipeMidOdds34)
    warpPipeLateOdds1 = get_capsule_value(warpPipeLateOdds1)
    warpPipeLateOdds2 = get_capsule_value(warpPipeLateOdds2)
    warpPipeLateOdds34 = get_capsule_value(warpPipeLateOdds34)

    # Swap Card
    swapCardEarlyOdds1 = get_capsule_value(swapCardEarlyOdds1)
    swapCardEarlyOdds2 = get_capsule_value(swapCardEarlyOdds2)
    swapCardEarlyOdds34 = get_capsule_value(swapCardEarlyOdds34)
    swapCardMidOdds1 = get_capsule_value(swapCardMidOdds1)
    swapCardMidOdds2 = get_capsule_value(swapCardMidOdds2)
    swapCardMidOdds34 = get_capsule_value(swapCardMidOdds34)
    swapCardLateOdds1 = get_capsule_value(swapCardLateOdds1)
    swapCardLateOdds2 = get_capsule_value(swapCardLateOdds2)
    swapCardLateOdds34 = get_capsule_value(swapCardLateOdds34)

    # Sparky Sticker
    sparkyStickerEarlyOdds1 = get_capsule_value(sparkyStickerEarlyOdds1)
    sparkyStickerEarlyOdds2 = get_capsule_value(sparkyStickerEarlyOdds2)
    sparkyStickerEarlyOdds34 = get_capsule_value(sparkyStickerEarlyOdds34)
    sparkyStickerMidOdds1 = get_capsule_value(sparkyStickerMidOdds1)
    sparkyStickerMidOdds2 = get_capsule_value(sparkyStickerMidOdds2)
    sparkyStickerMidOdds34 = get_capsule_value(sparkyStickerMidOdds34)
    sparkyStickerLateOdds1 = get_capsule_value(sparkyStickerLateOdds1)
    sparkyStickerLateOdds2 = get_capsule_value(sparkyStickerLateOdds2)
    sparkyStickerLateOdds34 = get_capsule_value(sparkyStickerLateOdds34)

    # Gaddlight
    gaddlightEarlyOdds1 = get_capsule_value(gaddlightEarlyOdds1)
    gaddlightEarlyOdds2 = get_capsule_value(gaddlightEarlyOdds2)
    gaddlightEarlyOdds34 = get_capsule_value(gaddlightEarlyOdds34)
    gaddlightMidOdds1 = get_capsule_value(gaddlightMidOdds1)
    gaddlightMidOdds2 = get_capsule_value(gaddlightMidOdds2)
    gaddlightMidOdds34 = get_capsule_value(gaddlightMidOdds34)
    gaddlightLateOdds1 = get_capsule_value(gaddlightLateOdds1)
    gaddlightLateOdds2 = get_capsule_value(gaddlightLateOdds2)
    gaddlightLateOdds34 = get_capsule_value(gaddlightLateOdds34)

    # Chomp Call
    chompCallEarlyOdds1 = get_capsule_value(chompCallEarlyOdds1)
    chompCallEarlyOdds2 = get_capsule_value(chompCallEarlyOdds2)
    chompCallEarlyOdds34 = get_capsule_value(chompCallEarlyOdds34)
    chompCallMidOdds1 = get_capsule_value(chompCallMidOdds1)
    chompCallMidOdds2 = get_capsule_value(chompCallMidOdds2)
    chompCallMidOdds34 = get_capsule_value(chompCallMidOdds34)
    chompCallLateOdds1 = get_capsule_value(chompCallLateOdds1)
    chompCallLateOdds2 = get_capsule_value(chompCallLateOdds2)
    chompCallLateOdds34 = get_capsule_value(chompCallLateOdds34)

    # Bowser Suit
    bowserSuitEarlyOdds1 = get_capsule_value(bowserSuitEarlyOdds1)
    bowserSuitEarlyOdds2 = get_capsule_value(bowserSuitEarlyOdds2)
    bowserSuitEarlyOdds34 = get_capsule_value(bowserSuitEarlyOdds34)
    bowserSuitMidOdds1 = get_capsule_value(bowserSuitMidOdds1)
    bowserSuitMidOdds2 = get_capsule_value(bowserSuitMidOdds2)
    bowserSuitMidOdds34 = get_capsule_value(bowserSuitMidOdds34)
    bowserSuitLateOdds1 = get_capsule_value(bowserSuitLateOdds1)
    bowserSuitLateOdds2 = get_capsule_value(bowserSuitLateOdds2)
    bowserSuitLateOdds34 = get_capsule_value(bowserSuitLateOdds34)

    # Crystal Ball
    crystalBallEarlyOdds1 = get_capsule_value(crystalBallEarlyOdds1)
    crystalBallEarlyOdds2 = get_capsule_value(crystalBallEarlyOdds2)
    crystalBallEarlyOdds34 = get_capsule_value(crystalBallEarlyOdds34)
    crystalBallMidOdds1 = get_capsule_value(crystalBallMidOdds1)
    crystalBallMidOdds2 = get_capsule_value(crystalBallMidOdds2)
    crystalBallMidOdds34 = get_capsule_value(crystalBallMidOdds34)
    crystalBallLateOdds1 = get_capsule_value(crystalBallLateOdds1)
    crystalBallLateOdds2 = get_capsule_value(crystalBallLateOdds2)
    crystalBallLateOdds34 = get_capsule_value(crystalBallLateOdds34)

    # Magic Lamp
    magicLampEarlyOdds1 = get_capsule_value(magicLampEarlyOdds1)
    magicLampEarlyOdds2 = get_capsule_value(magicLampEarlyOdds2)
    magicLampEarlyOdds34 = get_capsule_value(magicLampEarlyOdds34)
    magicLampMidOdds1 = get_capsule_value(magicLampMidOdds1)
    magicLampMidOdds2 = get_capsule_value(magicLampMidOdds2)
    magicLampMidOdds34 = get_capsule_value(magicLampMidOdds34)
    magicLampLateOdds1 = get_capsule_value(magicLampLateOdds1)
    magicLampLateOdds2 = get_capsule_value(magicLampLateOdds2)
    magicLampLateOdds34 = get_capsule_value(magicLampLateOdds34)

    # Item Bag
    itemBagEarlyOdds1 = get_capsule_value(itemBagEarlyOdds1)
    itemBagEarlyOdds2 = get_capsule_value(itemBagEarlyOdds2)
    itemBagEarlyOdds34 = get_capsule_value(itemBagEarlyOdds34)
    itemBagMidOdds1 = get_capsule_value(itemBagMidOdds1)
    itemBagMidOdds2 = get_capsule_value(itemBagMidOdds2)
    itemBagMidOdds34 = get_capsule_value(itemBagMidOdds34)
    itemBagLateOdds1 = get_capsule_value(itemBagLateOdds1)
    itemBagLateOdds2 = get_capsule_value(itemBagLateOdds2)
    itemBagLateOdds34 = get_capsule_value(itemBagLateOdds34)

    # Mushroom: DX
    mushroomEarlyOdds1 = get_capsule_value(mushroomEarlyOdds1)
    mushroomEarlyOdds2 = get_capsule_value(mushroomEarlyOdds2)
    mushroomEarlyOdds34 = get_capsule_value(mushroomEarlyOdds34)
    mushroomMidOdds1 = get_capsule_value(mushroomMidOdds1)
    mushroomMidOdds2 = get_capsule_value(mushroomMidOdds2)
    mushroomMidOdds34 = get_capsule_value(mushroomMidOdds34)
    mushroomLateOdds1 = get_capsule_value(mushroomLateOdds1)
    mushroomLateOdds2 = get_capsule_value(mushroomLateOdds2)
    mushroomLateOdds34 = get_capsule_value(mushroomLateOdds34)

    # Golden Mushroom: DX
    goldenMushroomEarlyOdds1 = get_capsule_value(goldenMushroomEarlyOdds1)
    goldenMushroomEarlyOdds2 = get_capsule_value(goldenMushroomEarlyOdds2)
    goldenMushroomEarlyOdds34 = get_capsule_value(goldenMushroomEarlyOdds34)
    goldenMushroomMidOdds1 = get_capsule_value(goldenMushroomMidOdds1)
    goldenMushroomMidOdds2 = get_capsule_value(goldenMushroomMidOdds2)
    goldenMushroomMidOdds34 = get_capsule_value(goldenMushroomMidOdds34)
    goldenMushroomLateOdds1 = get_capsule_value(goldenMushroomLateOdds1)
    goldenMushroomLateOdds2 = get_capsule_value(goldenMushroomLateOdds2)
    goldenMushroomLateOdds34 = get_capsule_value(goldenMushroomLateOdds34)

    # Reverse Mushroom: DX
    reverseMushroomEarlyOdds1 = get_capsule_value(reverseMushroomEarlyOdds1)
    reverseMushroomEarlyOdds2 = get_capsule_value(reverseMushroomEarlyOdds2)
    reverseMushroomEarlyOdds34 = get_capsule_value(reverseMushroomEarlyOdds34)
    reverseMushroomMidOdds1 = get_capsule_value(reverseMushroomMidOdds1)
    reverseMushroomMidOdds2 = get_capsule_value(reverseMushroomMidOdds2)
    reverseMushroomMidOdds34 = get_capsule_value(reverseMushroomMidOdds34)
    reverseMushroomLateOdds1 = get_capsule_value(reverseMushroomLateOdds1)
    reverseMushroomLateOdds2 = get_capsule_value(reverseMushroomLateOdds2)
    reverseMushroomLateOdds34 = get_capsule_value(reverseMushroomLateOdds34)

    # Poison Mushroom: DX
    poisonMushroomEarlyOdds1 = get_capsule_value(poisonMushroomEarlyOdds1)
    poisonMushroomEarlyOdds2 = get_capsule_value(poisonMushroomEarlyOdds2)
    poisonMushroomEarlyOdds34 = get_capsule_value(poisonMushroomEarlyOdds34)
    poisonMushroomMidOdds1 = get_capsule_value(poisonMushroomMidOdds1)
    poisonMushroomMidOdds2 = get_capsule_value(poisonMushroomMidOdds2)
    poisonMushroomMidOdds34 = get_capsule_value(poisonMushroomMidOdds34)
    poisonMushroomLateOdds1 = get_capsule_value(poisonMushroomLateOdds1)
    poisonMushroomLateOdds2 = get_capsule_value(poisonMushroomLateOdds2)
    poisonMushroomLateOdds34 = get_capsule_value(poisonMushroomLateOdds34)
    
    # Bowser Phone: DX
    bowserPhoneEarlyOdds1 = get_capsule_value(bowserPhoneEarlyOdds1)
    bowserPhoneEarlyOdds2 = get_capsule_value(bowserPhoneEarlyOdds2)
    bowserPhoneEarlyOdds34 = get_capsule_value(bowserPhoneEarlyOdds34)
    bowserPhoneMidOdds1 = get_capsule_value(bowserPhoneMidOdds1)
    bowserPhoneMidOdds2 = get_capsule_value(bowserPhoneMidOdds2)
    bowserPhoneMidOdds34 = get_capsule_value(bowserPhoneMidOdds34)
    bowserPhoneLateOdds1 = get_capsule_value(bowserPhoneLateOdds1)
    bowserPhoneLateOdds2 = get_capsule_value(bowserPhoneLateOdds2)
    bowserPhoneLateOdds34 = get_capsule_value(bowserPhoneLateOdds34)

    # Triple Poison Mushroom: DX
    triplePoisonMushroomEarlyOdds1 = get_capsule_value(triplePoisonMushroomEarlyOdds1)
    triplePoisonMushroomEarlyOdds2 = get_capsule_value(triplePoisonMushroomEarlyOdds2)
    triplePoisonMushroomEarlyOdds34 = get_capsule_value(triplePoisonMushroomEarlyOdds34)
    triplePoisonMushroomMidOdds1 = get_capsule_value(triplePoisonMushroomMidOdds1)
    triplePoisonMushroomMidOdds2 = get_capsule_value(triplePoisonMushroomMidOdds2)
    triplePoisonMushroomMidOdds34 = get_capsule_value(triplePoisonMushroomMidOdds34)
    triplePoisonMushroomLateOdds1 = get_capsule_value(triplePoisonMushroomLateOdds1)
    triplePoisonMushroomLateOdds2 = get_capsule_value(triplePoisonMushroomLateOdds2)
    triplePoisonMushroomLateOdds34 = get_capsule_value(triplePoisonMushroomLateOdds34)

    # Celluar Shopper: DX
    celluarShopperEarlyOdds1 = get_capsule_value(celluarShopperEarlyOdds1)
    celluarShopperEarlyOdds2 = get_capsule_value(celluarShopperEarlyOdds2)
    celluarShopperEarlyOdds34 = get_capsule_value(celluarShopperEarlyOdds34)
    celluarShopperMidOdds1 = get_capsule_value(celluarShopperMidOdds1)
    celluarShopperMidOdds2 = get_capsule_value(celluarShopperMidOdds2)
    celluarShopperMidOdds34 = get_capsule_value(celluarShopperMidOdds34)
    celluarShopperLateOdds1 = get_capsule_value(celluarShopperLateOdds1)
    celluarShopperLateOdds2 = get_capsule_value(celluarShopperLateOdds2)
    celluarShopperLateOdds34 = get_capsule_value(celluarShopperLateOdds34)

    # Skeleton Key: DX
    skeletonKeyEarlyOdds1 = get_capsule_value(skeletonKeyEarlyOdds1)
    skeletonKeyEarlyOdds2 = get_capsule_value(skeletonKeyEarlyOdds2)
    skeletonKeyEarlyOdds34 = get_capsule_value(skeletonKeyEarlyOdds34)
    skeletonKeyMidOdds1 = get_capsule_value(skeletonKeyMidOdds1)
    skeletonKeyMidOdds2 = get_capsule_value(skeletonKeyMidOdds2)
    skeletonKeyMidOdds34 = get_capsule_value(skeletonKeyMidOdds34)
    skeletonKeyLateOdds1 = get_capsule_value(skeletonKeyLateOdds1)
    skeletonKeyLateOdds2 = get_capsule_value(skeletonKeyLateOdds2)
    skeletonKeyLateOdds34 = get_capsule_value(skeletonKeyLateOdds34)

    # Plunder Chest: DX
    plunderChestEarlyOdds1 = get_capsule_value(plunderChestEarlyOdds1)
    plunderChestEarlyOdds2 = get_capsule_value(plunderChestEarlyOdds2)
    plunderChestEarlyOdds34 = get_capsule_value(plunderChestEarlyOdds34)
    plunderChestMidOdds1 = get_capsule_value(plunderChestMidOdds1)
    plunderChestMidOdds2 = get_capsule_value(plunderChestMidOdds2)
    plunderChestMidOdds34 = get_capsule_value(plunderChestMidOdds34)
    plunderChestLateOdds1 = get_capsule_value(plunderChestLateOdds1)
    plunderChestLateOdds2 = get_capsule_value(plunderChestLateOdds2)
    plunderChestLateOdds34 = get_capsule_value(plunderChestLateOdds34)

    # Double Dip: DX
    doubleDipEarlyOdds1 = get_capsule_value(doubleDipEarlyOdds1)
    doubleDipEarlyOdds2 = get_capsule_value(doubleDipEarlyOdds2)
    doubleDipEarlyOdds34 = get_capsule_value(doubleDipEarlyOdds34)
    doubleDipMidOdds1 = get_capsule_value(doubleDipMidOdds1)
    doubleDipMidOdds2 = get_capsule_value(doubleDipMidOdds2)
    doubleDipMidOdds34 = get_capsule_value(doubleDipMidOdds34)
    doubleDipLateOdds1 = get_capsule_value(doubleDipLateOdds1)
    doubleDipLateOdds2 = get_capsule_value(doubleDipLateOdds2)
    doubleDipLateOdds34 = get_capsule_value(plunderChestLateOdds34)

    # Gaddbrush: DX
    gaddbrushEarlyOdds1 = get_capsule_value(gaddbrushEarlyOdds1)
    gaddbrushEarlyOdds2 = get_capsule_value(gaddbrushEarlyOdds2)
    gaddbrushEarlyOdds34 = get_capsule_value(gaddbrushEarlyOdds34)
    gaddbrushMidOdds1 = get_capsule_value(gaddbrushMidOdds1)
    gaddbrushMidOdds2 = get_capsule_value(gaddbrushMidOdds2)
    gaddbrushMidOdds34 = get_capsule_value(gaddbrushMidOdds34)
    gaddbrushLateOdds1 = get_capsule_value(gaddbrushLateOdds1)
    gaddbrushLateOdds2 = get_capsule_value(gaddbrushLateOdds2)
    gaddbrushLateOdds34 = get_capsule_value(gaddbrushLateOdds34)

    # Warp Block: DX
    warpBlockEarlyOdds1 = get_capsule_value(warpBlockEarlyOdds1)
    warpBlockEarlyOdds2 = get_capsule_value(warpBlockEarlyOdds2)
    warpBlockEarlyOdds34 = get_capsule_value(warpBlockEarlyOdds34)
    warpBlockMidOdds1 = get_capsule_value(warpBlockMidOdds1)
    warpBlockMidOdds2 = get_capsule_value(warpBlockMidOdds2)
    warpBlockMidOdds34 = get_capsule_value(warpBlockMidOdds34)
    warpBlockLateOdds1 = get_capsule_value(warpBlockLateOdds1)
    warpBlockLateOdds2 = get_capsule_value(warpBlockLateOdds2)
    warpBlockLateOdds34 = get_capsule_value(warpBlockLateOdds34)

    # Fly Guy: DX
    flyGuyEarlyOdds1 = get_capsule_value(flyGuyEarlyOdds1)
    flyGuyEarlyOdds2 = get_capsule_value(flyGuyEarlyOdds2)
    flyGuyEarlyOdds34 = get_capsule_value(flyGuyEarlyOdds34)
    flyGuyMidOdds1 = get_capsule_value(flyGuyMidOdds1)
    flyGuyMidOdds2 = get_capsule_value(flyGuyMidOdds2)
    flyGuyMidOdds34 = get_capsule_value(flyGuyMidOdds34)
    flyGuyLateOdds1 = get_capsule_value(flyGuyLateOdds1)
    flyGuyLateOdds2 = get_capsule_value(flyGuyLateOdds2)
    flyGuyLateOdds34 = get_capsule_value(flyGuyLateOdds34)

    # Plus Block: DX
    plusBlockEarlyOdds1 = get_capsule_value(plusBlockEarlyOdds1)
    plusBlockEarlyOdds2 = get_capsule_value(plusBlockEarlyOdds2)
    plusBlockEarlyOdds34 = get_capsule_value(plusBlockEarlyOdds34)
    plusBlockMidOdds1 = get_capsule_value(plusBlockMidOdds1)
    plusBlockMidOdds2 = get_capsule_value(plusBlockMidOdds2)
    plusBlockMidOdds34 = get_capsule_value(plusBlockMidOdds34)
    plusBlockLateOdds1 = get_capsule_value(plusBlockLateOdds1)
    plusBlockLateOdds2 = get_capsule_value(plusBlockLateOdds2)
    plusBlockLateOdds34 = get_capsule_value(plusBlockLateOdds34)

    # Minus Block: DX
    minusBlockEarlyOdds1 = get_capsule_value(minusBlockEarlyOdds1)
    minusBlockEarlyOdds2 = get_capsule_value(minusBlockEarlyOdds2)
    minusBlockEarlyOdds34 = get_capsule_value(minusBlockEarlyOdds34)
    minusBlockMidOdds1 = get_capsule_value(minusBlockMidOdds1)
    minusBlockMidOdds2 = get_capsule_value(minusBlockMidOdds2)
    minusBlockMidOdds34 = get_capsule_value(minusBlockMidOdds34)
    minusBlockLateOdds1 = get_capsule_value(minusBlockLateOdds1)
    minusBlockLateOdds2 = get_capsule_value(minusBlockLateOdds2)
    minusBlockLateOdds34 = get_capsule_value(minusBlockLateOdds34)

    # Speed Block: DX
    speedBlockEarlyOdds1 = get_capsule_value(speedBlockEarlyOdds1)
    speedBlockEarlyOdds2 = get_capsule_value(speedBlockEarlyOdds2)
    speedBlockEarlyOdds34 = get_capsule_value(speedBlockEarlyOdds34)
    speedBlockMidOdds1 = get_capsule_value(speedBlockMidOdds1)
    speedBlockMidOdds2 = get_capsule_value(speedBlockMidOdds2)
    speedBlockMidOdds34 = get_capsule_value(speedBlockMidOdds34)
    speedBlockLateOdds1 = get_capsule_value(speedBlockLateOdds1)
    speedBlockLateOdds2 = get_capsule_value(speedBlockLateOdds2)
    speedBlockLateOdds34 = get_capsule_value(speedBlockLateOdds34)

    # Slow Block: DX
    slowBlockEarlyOdds1 = get_capsule_value(slowBlockEarlyOdds1)
    slowBlockEarlyOdds2 = get_capsule_value(slowBlockEarlyOdds2)
    slowBlockEarlyOdds34 = get_capsule_value(slowBlockEarlyOdds34)
    slowBlockMidOdds1 = get_capsule_value(slowBlockMidOdds1)
    slowBlockMidOdds2 = get_capsule_value(slowBlockMidOdds2)
    slowBlockMidOdds34 = get_capsule_value(slowBlockMidOdds34)
    slowBlockLateOdds1 = get_capsule_value(slowBlockLateOdds1)
    slowBlockLateOdds2 = get_capsule_value(slowBlockLateOdds2)
    slowBlockLateOdds34 = get_capsule_value(slowBlockLateOdds34)

    # Hidden Block Card: DX
    hiddenBlockCardEarlyOdds1 = get_capsule_value(hiddenBlockCardEarlyOdds1)
    hiddenBlockCardEarlyOdds2 = get_capsule_value(hiddenBlockCardEarlyOdds2)
    hiddenBlockCardEarlyOdds34 = get_capsule_value(hiddenBlockCardEarlyOdds34)
    hiddenBlockCardMidOdds1 = get_capsule_value(hiddenBlockCardMidOdds1)
    hiddenBlockCardMidOdds2 = get_capsule_value(hiddenBlockCardMidOdds2)
    hiddenBlockCardMidOdds34 = get_capsule_value(hiddenBlockCardMidOdds34)
    hiddenBlockCardLateOdds1 = get_capsule_value(hiddenBlockCardLateOdds1)
    hiddenBlockCardLateOdds2 = get_capsule_value(hiddenBlockCardLateOdds2)
    hiddenBlockCardLateOdds34 = get_capsule_value(hiddenBlockCardLateOdds34)

    # Barter Box: DX
    barterBoxEarlyOdds1 = get_capsule_value(barterBoxEarlyOdds1)
    barterBoxEarlyOdds2 = get_capsule_value(barterBoxEarlyOdds2)
    barterBoxEarlyOdds34 = get_capsule_value(barterBoxEarlyOdds34)
    barterBoxMidOdds1 = get_capsule_value(barterBoxMidOdds1)
    barterBoxMidOdds2 = get_capsule_value(barterBoxMidOdds2)
    barterBoxMidOdds34 = get_capsule_value(barterBoxMidOdds34)
    barterBoxLateOdds1 = get_capsule_value(barterBoxLateOdds1)
    barterBoxLateOdds2 = get_capsule_value(barterBoxLateOdds2)
    barterBoxLateOdds34 = get_capsule_value(barterBoxLateOdds34)

    # Super Warp Pipe: DX
    superWarpPipeEarlyOdds1 = get_capsule_value(superWarpPipeEarlyOdds1)
    superWarpPipeEarlyOdds2 = get_capsule_value(superWarpPipeEarlyOdds2)
    superWarpPipeEarlyOdds34 = get_capsule_value(superWarpPipeEarlyOdds34)
    superWarpPipeMidOdds1 = get_capsule_value(superWarpPipeMidOdds1)
    superWarpPipeMidOdds2 = get_capsule_value(superWarpPipeMidOdds2)
    superWarpPipeMidOdds34 = get_capsule_value(superWarpPipeMidOdds34)
    superWarpPipeLateOdds1 = get_capsule_value(superWarpPipeLateOdds1)
    superWarpPipeLateOdds2 = get_capsule_value(superWarpPipeLateOdds2)
    superWarpPipeLateOdds34 = get_capsule_value(superWarpPipeLateOdds34)

    # Chance Time Charm: DX
    chanceTimeCharmEarlyOdds1 = get_capsule_value(chanceTimeCharmEarlyOdds1)
    chanceTimeCharmEarlyOdds2 = get_capsule_value(chanceTimeCharmEarlyOdds2)
    chanceTimeCharmEarlyOdds34 = get_capsule_value(chanceTimeCharmEarlyOdds34)
    chanceTimeCharmMidOdds1 = get_capsule_value(chanceTimeCharmMidOdds1)
    chanceTimeCharmMidOdds2 = get_capsule_value(chanceTimeCharmMidOdds2)
    chanceTimeCharmMidOdds34 = get_capsule_value(chanceTimeCharmMidOdds34)
    chanceTimeCharmLateOdds1 = get_capsule_value(chanceTimeCharmLateOdds1)
    chanceTimeCharmLateOdds2 = get_capsule_value(chanceTimeCharmLateOdds2)
    chanceTimeCharmLateOdds34 = get_capsule_value(chanceTimeCharmLateOdds34)

    # Wacky Watch: DX
    wackyWatchEarlyOdds1 = get_capsule_value(wackyWatchEarlyOdds1)
    wackyWatchEarlyOdds2 = get_capsule_value(wackyWatchEarlyOdds2)
    wackyWatchEarlyOdds34 = get_capsule_value(wackyWatchEarlyOdds34)
    wackyWatchMidOdds1 = get_capsule_value(wackyWatchMidOdds1)
    wackyWatchMidOdds2 = get_capsule_value(wackyWatchMidOdds2)
    wackyWatchMidOdds34 = get_capsule_value(wackyWatchMidOdds34)
    wackyWatchLateOdds1 = get_capsule_value(wackyWatchLateOdds1)
    wackyWatchLateOdds2 = get_capsule_value(wackyWatchLateOdds2)
    wackyWatchLateOdds34 = get_capsule_value(wackyWatchLateOdds34)

    earlyOdds1 = [
        miniMushroomEarlyOdds1,
        megaMushroomEarlyOdds1,
        superMiniMushroomEarlyOdds1,
        superMegaMushroomEarlyOdds1,
        miniMegaHammerEarlyOdds1,
        warpPipeEarlyOdds1,
        swapCardEarlyOdds1,
        sparkyStickerEarlyOdds1,
        gaddlightEarlyOdds1,
        chompCallEarlyOdds1,
        bowserSuitEarlyOdds1,
        crystalBallEarlyOdds1,
        magicLampEarlyOdds1,
        itemBagEarlyOdds1,
        mushroomEarlyOdds1,
        goldenMushroomEarlyOdds1,
        reverseMushroomEarlyOdds1,
        poisonMushroomEarlyOdds1,
        triplePoisonMushroomEarlyOdds1,
        celluarShopperEarlyOdds1,
        skeletonKeyEarlyOdds1,
        plunderChestEarlyOdds1,
        gaddbrushEarlyOdds1,
        warpBlockEarlyOdds1,
        flyGuyEarlyOdds1,
        plusBlockEarlyOdds1,
        minusBlockEarlyOdds1,
        speedBlockEarlyOdds1,
        slowBlockEarlyOdds1,
        bowserPhoneEarlyOdds1,
        doubleDipEarlyOdds1,
        hiddenBlockCardEarlyOdds1,
        barterBoxEarlyOdds1,
        superWarpPipeEarlyOdds1,
        chanceTimeCharmEarlyOdds1,
        wackyWatchEarlyOdds1,
    ]
    
    earlyOdds2 = [
        miniMushroomEarlyOdds2,
        megaMushroomEarlyOdds2,
        superMiniMushroomEarlyOdds2,
        superMegaMushroomEarlyOdds2,
        miniMegaHammerEarlyOdds2,
        warpPipeEarlyOdds2,
        swapCardEarlyOdds2,
        sparkyStickerEarlyOdds2,
        gaddlightEarlyOdds2,
        chompCallEarlyOdds2,
        bowserSuitEarlyOdds2,
        crystalBallEarlyOdds2,
        magicLampEarlyOdds2,
        itemBagEarlyOdds2,
        mushroomEarlyOdds2,
        goldenMushroomEarlyOdds2,
        reverseMushroomEarlyOdds2,
        poisonMushroomEarlyOdds2,
        triplePoisonMushroomEarlyOdds2,
        celluarShopperEarlyOdds2,
        skeletonKeyEarlyOdds2,
        plunderChestEarlyOdds2,
        gaddbrushEarlyOdds2,
        warpBlockEarlyOdds2,
        flyGuyEarlyOdds2,
        plusBlockEarlyOdds2,
        minusBlockEarlyOdds2,
        speedBlockEarlyOdds2,
        slowBlockEarlyOdds2,
        bowserPhoneEarlyOdds2,
        doubleDipEarlyOdds2,
        hiddenBlockCardEarlyOdds2,
        barterBoxEarlyOdds2,
        superWarpPipeEarlyOdds2,
        chanceTimeCharmEarlyOdds2,
        wackyWatchEarlyOdds2,
    ]

    earlyOdds34 = [
        miniMushroomEarlyOdds34,
        megaMushroomEarlyOdds34,
        superMiniMushroomEarlyOdds34,
        superMegaMushroomEarlyOdds34,
        miniMegaHammerEarlyOdds34,
        warpPipeEarlyOdds34,
        swapCardEarlyOdds34,
        sparkyStickerEarlyOdds34,
        gaddlightEarlyOdds34,
        chompCallEarlyOdds34,
        bowserSuitEarlyOdds34,
        crystalBallEarlyOdds34,
        magicLampEarlyOdds34,
        itemBagEarlyOdds34,
        mushroomEarlyOdds34,
        goldenMushroomEarlyOdds34,
        reverseMushroomEarlyOdds34,
        poisonMushroomEarlyOdds34,
        triplePoisonMushroomEarlyOdds34,
        celluarShopperEarlyOdds34,
        skeletonKeyEarlyOdds34,
        plunderChestEarlyOdds34,
        gaddbrushEarlyOdds34,
        warpBlockEarlyOdds34,
        flyGuyEarlyOdds34,
        plusBlockEarlyOdds34,
        minusBlockEarlyOdds34,
        speedBlockEarlyOdds34,
        slowBlockEarlyOdds34,
        bowserPhoneEarlyOdds34,
        doubleDipEarlyOdds34,
        hiddenBlockCardEarlyOdds34,
        barterBoxEarlyOdds34,
        superWarpPipeEarlyOdds34,
        chanceTimeCharmEarlyOdds34,
        wackyWatchEarlyOdds34,
    ]
    
    midOdds1 = [
        miniMushroomMidOdds1,
        megaMushroomMidOdds1,
        superMiniMushroomMidOdds1,
        superMegaMushroomMidOdds1,
        miniMegaHammerMidOdds1,
        warpPipeMidOdds1,
        swapCardMidOdds1,
        sparkyStickerMidOdds1,
        gaddlightMidOdds1,
        chompCallMidOdds1,
        bowserSuitMidOdds1,
        crystalBallMidOdds1,
        magicLampMidOdds1,
        itemBagMidOdds1,
        mushroomMidOdds1,
        goldenMushroomMidOdds1,
        reverseMushroomMidOdds1,
        poisonMushroomMidOdds1,
        triplePoisonMushroomMidOdds1,
        celluarShopperMidOdds1,
        skeletonKeyMidOdds1,
        plunderChestMidOdds1,
        gaddbrushMidOdds1,
        warpBlockMidOdds1,
        flyGuyMidOdds1,
        plusBlockMidOdds1,
        minusBlockMidOdds1,
        speedBlockMidOdds1,
        slowBlockMidOdds1,
        bowserPhoneMidOdds1,
        doubleDipMidOdds1,
        hiddenBlockCardMidOdds1,
        barterBoxMidOdds1,
        superWarpPipeMidOdds1,
        chanceTimeCharmMidOdds1,
        wackyWatchMidOdds1,
    ]

    midOdds2 = [
        miniMushroomMidOdds2,
        megaMushroomMidOdds2,
        superMiniMushroomMidOdds2,
        superMegaMushroomMidOdds2,
        miniMegaHammerMidOdds2,
        warpPipeMidOdds2,
        swapCardMidOdds2,
        sparkyStickerMidOdds2,
        gaddlightMidOdds2,
        chompCallMidOdds2,
        bowserSuitMidOdds2,
        crystalBallMidOdds2,
        magicLampMidOdds2,
        itemBagMidOdds2,
        mushroomMidOdds2,
        goldenMushroomMidOdds2,
        reverseMushroomMidOdds2,
        poisonMushroomMidOdds2,
        triplePoisonMushroomMidOdds2,
        celluarShopperMidOdds2,
        skeletonKeyMidOdds2,
        plunderChestMidOdds2,
        gaddbrushMidOdds2,
        warpBlockMidOdds2,
        flyGuyMidOdds2,
        plusBlockMidOdds2,
        minusBlockMidOdds2,
        speedBlockMidOdds2,
        slowBlockMidOdds2,
        bowserPhoneMidOdds2,
        doubleDipMidOdds2,
        hiddenBlockCardMidOdds2,
        barterBoxMidOdds2,
        superWarpPipeMidOdds2,
        chanceTimeCharmMidOdds2,
        wackyWatchMidOdds2,
    ]

    midOdds34 = [
        miniMushroomMidOdds34,
        megaMushroomMidOdds34,
        superMiniMushroomMidOdds34,
        superMegaMushroomMidOdds34,
        miniMegaHammerMidOdds34,
        warpPipeMidOdds34,
        swapCardMidOdds34,
        sparkyStickerMidOdds34,
        gaddlightMidOdds34,
        chompCallMidOdds34,
        bowserSuitMidOdds34,
        crystalBallMidOdds34,
        magicLampMidOdds34,
        itemBagMidOdds34,
        mushroomMidOdds34,
        goldenMushroomMidOdds34,
        reverseMushroomMidOdds34,
        poisonMushroomMidOdds34,
        triplePoisonMushroomMidOdds34,
        celluarShopperMidOdds34,
        skeletonKeyMidOdds34,
        plunderChestMidOdds34,
        gaddbrushMidOdds34,
        warpBlockMidOdds34,
        flyGuyMidOdds34,
        plusBlockMidOdds34,
        minusBlockMidOdds34,
        speedBlockMidOdds34,
        slowBlockMidOdds34,
        bowserPhoneMidOdds34,
        doubleDipMidOdds34,
        hiddenBlockCardMidOdds34,
        barterBoxMidOdds34,
        superWarpPipeMidOdds34,
        chanceTimeCharmMidOdds34,
        wackyWatchMidOdds34,
    ]

    lateOdds1 = [
        miniMushroomLateOdds1,
        megaMushroomLateOdds1,
        superMiniMushroomLateOdds1,
        superMegaMushroomLateOdds1,
        miniMegaHammerLateOdds1,
        warpPipeLateOdds1,
        swapCardLateOdds1,
        sparkyStickerLateOdds1,
        gaddlightLateOdds1,
        chompCallLateOdds1,
        bowserSuitLateOdds1,
        crystalBallLateOdds1,
        magicLampLateOdds1,
        itemBagLateOdds1,
        mushroomLateOdds1,
        goldenMushroomLateOdds1,
        reverseMushroomLateOdds1,
        poisonMushroomLateOdds1,
        triplePoisonMushroomLateOdds1,
        celluarShopperLateOdds1,
        skeletonKeyLateOdds1,
        plunderChestLateOdds1,
        gaddbrushLateOdds1,
        warpBlockLateOdds1,
        flyGuyLateOdds1,
        plusBlockLateOdds1,
        minusBlockLateOdds1,
        speedBlockLateOdds1,
        slowBlockLateOdds1,
        bowserPhoneLateOdds1,
        doubleDipLateOdds1,
        hiddenBlockCardLateOdds1,
        barterBoxLateOdds1,
        superWarpPipeLateOdds1,
        chanceTimeCharmLateOdds1,
        wackyWatchLateOdds1,
    ]

    lateOdds2 = [
        miniMushroomLateOdds2,
        megaMushroomLateOdds2,
        superMiniMushroomLateOdds2,
        superMegaMushroomLateOdds2,
        miniMegaHammerLateOdds2,
        warpPipeLateOdds2,
        swapCardLateOdds2,
        sparkyStickerLateOdds2,
        gaddlightLateOdds2,
        chompCallLateOdds2,
        bowserSuitLateOdds2,
        crystalBallLateOdds2,
        magicLampLateOdds2,
        itemBagLateOdds2,
        mushroomLateOdds2,
        goldenMushroomLateOdds2,
        reverseMushroomLateOdds2,
        poisonMushroomLateOdds2,
        triplePoisonMushroomLateOdds2,
        celluarShopperLateOdds2,
        skeletonKeyLateOdds2,
        plunderChestLateOdds2,
        gaddbrushLateOdds2,
        warpBlockLateOdds2,
        flyGuyLateOdds2,
        plusBlockLateOdds2,
        minusBlockLateOdds2,
        speedBlockLateOdds2,
        slowBlockLateOdds2,
        bowserPhoneLateOdds2,
        doubleDipLateOdds2,
        hiddenBlockCardLateOdds2,
        barterBoxLateOdds2,
        superWarpPipeLateOdds2,
        chanceTimeCharmLateOdds2,
        wackyWatchLateOdds2,
    ]

    lateOdds34 = [
        miniMushroomLateOdds34,
        megaMushroomLateOdds34,
        superMiniMushroomLateOdds34,
        superMegaMushroomLateOdds34,
        miniMegaHammerLateOdds34,
        warpPipeLateOdds34,
        swapCardLateOdds34,
        sparkyStickerLateOdds34,
        gaddlightLateOdds34,
        chompCallLateOdds34,
        bowserSuitLateOdds34,
        crystalBallLateOdds34,
        magicLampLateOdds34,
        itemBagLateOdds34,
        mushroomLateOdds34,
        goldenMushroomLateOdds34,
        reverseMushroomLateOdds34,
        poisonMushroomLateOdds34,
        triplePoisonMushroomLateOdds34,
        celluarShopperLateOdds34,
        skeletonKeyLateOdds34,
        plunderChestLateOdds34,
        gaddbrushLateOdds34,
        warpBlockLateOdds34,
        flyGuyLateOdds34,
        plusBlockLateOdds34,
        minusBlockLateOdds34,
        speedBlockLateOdds34,
        slowBlockLateOdds34,
        bowserPhoneLateOdds34,
        doubleDipLateOdds34,
        hiddenBlockCardLateOdds34,
        barterBoxLateOdds34,
        superWarpPipeLateOdds34,
        chanceTimeCharmLateOdds34,
        wackyWatchLateOdds34,
    ]

    earlyOdds1Weights = sum(int(weight) if weight else 0 for weight in earlyOdds1)
    earlyOdds2Weights = sum(int(weight) if weight else 0 for weight in earlyOdds2)
    earlyOdds34Weights = sum(int(weight) if weight else 0 for weight in earlyOdds34)
    midOdds1Weights = sum(int(weight) if weight else 0 for weight in midOdds1)
    midOdds2Weights = sum(int(weight) if weight else 0 for weight in midOdds2)
    midOdds34Weights = sum(int(weight) if weight else 0 for weight in midOdds34)
    lateOdds1Weights = sum(int(weight) if weight else 0 for weight in lateOdds1)
    lateOdds2Weights = sum(int(weight) if weight else 0 for weight in lateOdds2)
    lateOdds34Weights = sum(int(weight) if weight else 0 for weight in lateOdds34)

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

    # Mini Mushroom
    miniMushroomEarlyOdds1 = calculateWeight(miniMushroomEarlyOdds1, earlyOdds1Weights)
    miniMushroomEarlyOdds2 = calculateWeight(miniMushroomEarlyOdds2, earlyOdds2Weights)
    miniMushroomEarlyOdds34 = calculateWeight(miniMushroomEarlyOdds34, earlyOdds34Weights)
    miniMushroomMidOdds1 = calculateWeight(miniMushroomMidOdds1, midOdds1Weights)
    miniMushroomMidOdds2 = calculateWeight(miniMushroomMidOdds2, midOdds2Weights)
    miniMushroomMidOdds34 = calculateWeight(miniMushroomMidOdds34, midOdds34Weights)
    miniMushroomLateOdds1 = calculateWeight(miniMushroomLateOdds1, lateOdds1Weights)
    miniMushroomLateOdds2 = calculateWeight(miniMushroomLateOdds2, lateOdds2Weights)
    miniMushroomLateOdds34 = calculateWeight(miniMushroomLateOdds34, lateOdds34Weights)

    # Mega Mushroom
    megaMushroomEarlyOdds1 = calculateWeight(megaMushroomEarlyOdds1, earlyOdds1Weights)
    megaMushroomEarlyOdds2 = calculateWeight(megaMushroomEarlyOdds2, earlyOdds2Weights)
    megaMushroomEarlyOdds34 = calculateWeight(megaMushroomEarlyOdds34, earlyOdds34Weights)
    megaMushroomMidOdds1 = calculateWeight(megaMushroomMidOdds1, midOdds1Weights)
    megaMushroomMidOdds2 = calculateWeight(megaMushroomMidOdds2, midOdds2Weights)
    megaMushroomMidOdds34 = calculateWeight(megaMushroomMidOdds34, midOdds34Weights)
    megaMushroomLateOdds1 = calculateWeight(megaMushroomLateOdds1, lateOdds1Weights)
    megaMushroomLateOdds2 = calculateWeight(megaMushroomLateOdds2, lateOdds2Weights)
    megaMushroomLateOdds34 = calculateWeight(megaMushroomLateOdds34, lateOdds34Weights)

    # Super Mini Mushroom
    superMiniMushroomEarlyOdds1 = calculateWeight(superMiniMushroomEarlyOdds1, earlyOdds1Weights)
    superMiniMushroomEarlyOdds2 = calculateWeight(superMiniMushroomEarlyOdds2, earlyOdds2Weights)
    superMiniMushroomEarlyOdds34 = calculateWeight(superMiniMushroomEarlyOdds34, earlyOdds34Weights)
    superMiniMushroomMidOdds1 = calculateWeight(superMiniMushroomMidOdds1, midOdds1Weights)
    superMiniMushroomMidOdds2 = calculateWeight(superMiniMushroomMidOdds2, midOdds2Weights)
    superMiniMushroomMidOdds34 = calculateWeight(superMiniMushroomMidOdds34, midOdds34Weights)
    superMiniMushroomLateOdds1 = calculateWeight(superMiniMushroomLateOdds1, lateOdds1Weights)
    superMiniMushroomLateOdds2 = calculateWeight(superMiniMushroomLateOdds2, lateOdds2Weights)
    superMiniMushroomLateOdds34 = calculateWeight(superMiniMushroomLateOdds34, lateOdds34Weights)

    # Super Mega Mushroom
    superMegaMushroomEarlyOdds1 = calculateWeight(superMegaMushroomEarlyOdds1, earlyOdds1Weights)
    superMegaMushroomEarlyOdds2 = calculateWeight(superMegaMushroomEarlyOdds2, earlyOdds2Weights)
    superMegaMushroomEarlyOdds34 = calculateWeight(superMegaMushroomEarlyOdds34, earlyOdds34Weights)
    superMegaMushroomMidOdds1 = calculateWeight(superMegaMushroomMidOdds1, midOdds1Weights)
    superMegaMushroomMidOdds2 = calculateWeight(superMegaMushroomMidOdds2, midOdds2Weights)
    superMegaMushroomMidOdds34 = calculateWeight(superMegaMushroomMidOdds34, midOdds34Weights)
    superMegaMushroomLateOdds1 = calculateWeight(superMegaMushroomLateOdds1, lateOdds1Weights)
    superMegaMushroomLateOdds2 = calculateWeight(superMegaMushroomLateOdds2, lateOdds2Weights)
    superMegaMushroomLateOdds34 = calculateWeight(superMegaMushroomLateOdds34, lateOdds34Weights)

    # Mini Mega Hammer
    miniMegaHammerEarlyOdds1 = calculateWeight(miniMegaHammerEarlyOdds1, earlyOdds1Weights)
    miniMegaHammerEarlyOdds2 = calculateWeight(miniMegaHammerEarlyOdds2, earlyOdds2Weights)
    miniMegaHammerEarlyOdds34 = calculateWeight(miniMegaHammerEarlyOdds34, earlyOdds34Weights)
    miniMegaHammerMidOdds1 = calculateWeight(miniMegaHammerMidOdds1, midOdds1Weights)
    miniMegaHammerMidOdds2 = calculateWeight(miniMegaHammerMidOdds2, midOdds2Weights)
    miniMegaHammerMidOdds34 = calculateWeight(miniMegaHammerMidOdds34, midOdds34Weights)
    miniMegaHammerLateOdds1 = calculateWeight(miniMegaHammerLateOdds1, lateOdds1Weights)
    miniMegaHammerLateOdds2 = calculateWeight(miniMegaHammerLateOdds2, lateOdds2Weights)
    miniMegaHammerLateOdds34 = calculateWeight(miniMegaHammerLateOdds34, lateOdds34Weights)

    # Warp Pipe
    warpPipeEarlyOdds1 = calculateWeight(warpPipeEarlyOdds1, earlyOdds1Weights)
    warpPipeEarlyOdds2 = calculateWeight(warpPipeEarlyOdds2, earlyOdds2Weights)
    warpPipeEarlyOdds34 = calculateWeight(warpPipeEarlyOdds34, earlyOdds34Weights)
    warpPipeMidOdds1 = calculateWeight(warpPipeMidOdds1, midOdds1Weights)
    warpPipeMidOdds2 = calculateWeight(warpPipeMidOdds2, midOdds2Weights)
    warpPipeMidOdds34 = calculateWeight(warpPipeMidOdds34, midOdds34Weights)
    warpPipeLateOdds1 = calculateWeight(warpPipeLateOdds1, lateOdds1Weights)
    warpPipeLateOdds2 = calculateWeight(warpPipeLateOdds2, lateOdds2Weights)
    warpPipeLateOdds34 = calculateWeight(warpPipeLateOdds34, lateOdds34Weights)

    # Swap Card
    swapCardEarlyOdds1 = calculateWeight(swapCardEarlyOdds1, earlyOdds1Weights)
    swapCardEarlyOdds2 = calculateWeight(swapCardEarlyOdds2, earlyOdds2Weights)
    swapCardEarlyOdds34 = calculateWeight(swapCardEarlyOdds34, earlyOdds34Weights)
    swapCardMidOdds1 = calculateWeight(swapCardMidOdds1, midOdds1Weights)
    swapCardMidOdds2 = calculateWeight(swapCardMidOdds2, midOdds2Weights)
    swapCardMidOdds34 = calculateWeight(swapCardMidOdds34, midOdds34Weights)
    swapCardLateOdds1 = calculateWeight(swapCardLateOdds1, lateOdds1Weights)
    swapCardLateOdds2 = calculateWeight(swapCardLateOdds2, lateOdds2Weights)
    swapCardLateOdds34 = calculateWeight(swapCardLateOdds34, lateOdds34Weights)

    # Sparky Sticker
    sparkyStickerEarlyOdds1 = calculateWeight(sparkyStickerEarlyOdds1, earlyOdds1Weights)
    sparkyStickerEarlyOdds2 = calculateWeight(sparkyStickerEarlyOdds2, earlyOdds2Weights)
    sparkyStickerEarlyOdds34 = calculateWeight(sparkyStickerEarlyOdds34, earlyOdds34Weights)
    sparkyStickerMidOdds1 = calculateWeight(sparkyStickerMidOdds1, midOdds1Weights)
    sparkyStickerMidOdds2 = calculateWeight(sparkyStickerMidOdds2, midOdds2Weights)
    sparkyStickerMidOdds34 = calculateWeight(sparkyStickerMidOdds34, midOdds34Weights)
    sparkyStickerLateOdds1 = calculateWeight(sparkyStickerLateOdds1, lateOdds1Weights)
    sparkyStickerLateOdds2 = calculateWeight(sparkyStickerLateOdds2, lateOdds2Weights)
    sparkyStickerLateOdds34 = calculateWeight(sparkyStickerLateOdds34, lateOdds34Weights)

    # Gaddlight
    gaddlightEarlyOdds1 = calculateWeight(gaddlightEarlyOdds1, earlyOdds1Weights)
    gaddlightEarlyOdds2 = calculateWeight(gaddlightEarlyOdds2, earlyOdds2Weights)
    gaddlightEarlyOdds34 = calculateWeight(gaddlightEarlyOdds34, earlyOdds34Weights)
    gaddlightMidOdds1 = calculateWeight(gaddlightMidOdds1, midOdds1Weights)
    gaddlightMidOdds2 = calculateWeight(gaddlightMidOdds2, midOdds2Weights)
    gaddlightMidOdds34 = calculateWeight(gaddlightMidOdds34, midOdds34Weights)
    gaddlightLateOdds1 = calculateWeight(gaddlightLateOdds1, lateOdds1Weights)
    gaddlightLateOdds2 = calculateWeight(gaddlightLateOdds2, lateOdds2Weights)
    gaddlightLateOdds34 = calculateWeight(gaddlightLateOdds34, lateOdds34Weights)

    # Chomp Call
    chompCallEarlyOdds1 = calculateWeight(chompCallEarlyOdds1, earlyOdds1Weights)
    chompCallEarlyOdds2 = calculateWeight(chompCallEarlyOdds2, earlyOdds2Weights)
    chompCallEarlyOdds34 = calculateWeight(chompCallEarlyOdds34, earlyOdds34Weights)
    chompCallMidOdds1 = calculateWeight(chompCallMidOdds1, midOdds1Weights)
    chompCallMidOdds2 = calculateWeight(chompCallMidOdds2, midOdds2Weights)
    chompCallMidOdds34 = calculateWeight(chompCallMidOdds34, midOdds34Weights)
    chompCallLateOdds1 = calculateWeight(chompCallLateOdds1, lateOdds1Weights)
    chompCallLateOdds2 = calculateWeight(chompCallLateOdds2, lateOdds2Weights)
    chompCallLateOdds34 = calculateWeight(chompCallLateOdds34, lateOdds34Weights)

    # Bowser Suit
    bowserSuitEarlyOdds1 = calculateWeight(bowserSuitEarlyOdds1, earlyOdds1Weights)
    bowserSuitEarlyOdds2 = calculateWeight(bowserSuitEarlyOdds2, earlyOdds2Weights)
    bowserSuitEarlyOdds34 = calculateWeight(bowserSuitEarlyOdds34, earlyOdds34Weights)
    bowserSuitMidOdds1 = calculateWeight(bowserSuitMidOdds1, midOdds1Weights)
    bowserSuitMidOdds2 = calculateWeight(bowserSuitMidOdds2, midOdds2Weights)
    bowserSuitMidOdds34 = calculateWeight(bowserSuitMidOdds34, midOdds34Weights)
    bowserSuitLateOdds1 = calculateWeight(bowserSuitLateOdds1, lateOdds1Weights)
    bowserSuitLateOdds2 = calculateWeight(bowserSuitLateOdds2, lateOdds2Weights)
    bowserSuitLateOdds34 = calculateWeight(bowserSuitLateOdds34, lateOdds34Weights)

    # Crystal Ball
    crystalBallEarlyOdds1 = calculateWeight(crystalBallEarlyOdds1, earlyOdds1Weights)
    crystalBallEarlyOdds2 = calculateWeight(crystalBallEarlyOdds2, earlyOdds2Weights)
    crystalBallEarlyOdds34 = calculateWeight(crystalBallEarlyOdds34, earlyOdds34Weights)
    crystalBallMidOdds1 = calculateWeight(crystalBallMidOdds1, midOdds1Weights)
    crystalBallMidOdds2 = calculateWeight(crystalBallMidOdds2, midOdds2Weights)
    crystalBallMidOdds34 = calculateWeight(crystalBallMidOdds34, midOdds34Weights)
    crystalBallLateOdds1 = calculateWeight(crystalBallLateOdds1, lateOdds1Weights)
    crystalBallLateOdds2 = calculateWeight(crystalBallLateOdds2, lateOdds2Weights)
    crystalBallLateOdds34 = calculateWeight(crystalBallLateOdds34, lateOdds34Weights)

    # Magic Lamp
    magicLampEarlyOdds1 = calculateWeight(magicLampEarlyOdds1, earlyOdds1Weights)
    magicLampEarlyOdds2 = calculateWeight(magicLampEarlyOdds2, earlyOdds2Weights)
    magicLampEarlyOdds34 = calculateWeight(magicLampEarlyOdds34, earlyOdds34Weights)
    magicLampMidOdds1 = calculateWeight(magicLampMidOdds1, midOdds1Weights)
    magicLampMidOdds2 = calculateWeight(magicLampMidOdds2, midOdds2Weights)
    magicLampMidOdds34 = calculateWeight(magicLampMidOdds34, midOdds34Weights)
    magicLampLateOdds1 = calculateWeight(magicLampLateOdds1, lateOdds1Weights)
    magicLampLateOdds2 = calculateWeight(magicLampLateOdds2, lateOdds2Weights)
    magicLampLateOdds34 = calculateWeight(magicLampLateOdds34, lateOdds34Weights)

    # Item Bag
    itemBagEarlyOdds1 = calculateWeight(itemBagEarlyOdds1, earlyOdds1Weights)
    itemBagEarlyOdds2 = calculateWeight(itemBagEarlyOdds2, earlyOdds2Weights)
    itemBagEarlyOdds34 = calculateWeight(itemBagEarlyOdds34, earlyOdds34Weights)
    itemBagMidOdds1 = calculateWeight(itemBagMidOdds1, midOdds1Weights)
    itemBagMidOdds2 = calculateWeight(itemBagMidOdds2, midOdds2Weights)
    itemBagMidOdds34 = calculateWeight(itemBagMidOdds34, midOdds34Weights)
    itemBagLateOdds1 = calculateWeight(itemBagLateOdds1, lateOdds1Weights)
    itemBagLateOdds2 = calculateWeight(itemBagLateOdds2, lateOdds2Weights)
    itemBagLateOdds34 = calculateWeight(itemBagLateOdds34, lateOdds34Weights)

    # Mushroom: DX
    mushroomEarlyOdds1 = calculateWeight(mushroomEarlyOdds1, earlyOdds1Weights)
    mushroomEarlyOdds2 = calculateWeight(mushroomEarlyOdds2, earlyOdds2Weights)
    mushroomEarlyOdds34 = calculateWeight(mushroomEarlyOdds34, earlyOdds34Weights)
    mushroomMidOdds1 = calculateWeight(mushroomMidOdds1, midOdds1Weights)
    mushroomMidOdds2 = calculateWeight(mushroomMidOdds2, midOdds2Weights)
    mushroomMidOdds34 = calculateWeight(mushroomMidOdds34, midOdds34Weights)
    mushroomLateOdds1 = calculateWeight(mushroomLateOdds1, lateOdds1Weights)
    mushroomLateOdds2 = calculateWeight(mushroomLateOdds2, lateOdds2Weights)
    mushroomLateOdds34 = calculateWeight(mushroomLateOdds34, lateOdds34Weights)

    # Golden Mushroom: DX
    goldenMushroomEarlyOdds1 = calculateWeight(goldenMushroomEarlyOdds1, earlyOdds1Weights)
    goldenMushroomEarlyOdds2 = calculateWeight(goldenMushroomEarlyOdds2, earlyOdds2Weights)
    goldenMushroomEarlyOdds34 = calculateWeight(goldenMushroomEarlyOdds34, earlyOdds34Weights)
    goldenMushroomMidOdds1 = calculateWeight(goldenMushroomMidOdds1, midOdds1Weights)
    goldenMushroomMidOdds2 = calculateWeight(goldenMushroomMidOdds2, midOdds2Weights)
    goldenMushroomMidOdds34 = calculateWeight(goldenMushroomMidOdds34, midOdds34Weights)
    goldenMushroomLateOdds1 = calculateWeight(goldenMushroomLateOdds1, lateOdds1Weights)
    goldenMushroomLateOdds2 = calculateWeight(goldenMushroomLateOdds2, lateOdds2Weights)
    goldenMushroomLateOdds34 = calculateWeight(goldenMushroomLateOdds34, lateOdds34Weights)

    # Reverse Mushroom: DX
    reverseMushroomEarlyOdds1 = calculateWeight(reverseMushroomEarlyOdds1, earlyOdds1Weights)
    reverseMushroomEarlyOdds2 = calculateWeight(reverseMushroomEarlyOdds2, earlyOdds2Weights)
    reverseMushroomEarlyOdds34 = calculateWeight(reverseMushroomEarlyOdds34, earlyOdds34Weights)
    reverseMushroomMidOdds1 = calculateWeight(reverseMushroomMidOdds1, midOdds1Weights)
    reverseMushroomMidOdds2 = calculateWeight(reverseMushroomMidOdds2, midOdds2Weights)
    reverseMushroomMidOdds34 = calculateWeight(reverseMushroomMidOdds34, midOdds34Weights)
    reverseMushroomLateOdds1 = calculateWeight(reverseMushroomLateOdds1, lateOdds1Weights)
    reverseMushroomLateOdds2 = calculateWeight(reverseMushroomLateOdds2, lateOdds2Weights)
    reverseMushroomLateOdds34 = calculateWeight(reverseMushroomLateOdds34, lateOdds34Weights)

    # Poison Mushroom: DX
    poisonMushroomEarlyOdds1 = calculateWeight(poisonMushroomEarlyOdds1, earlyOdds1Weights)
    poisonMushroomEarlyOdds2 = calculateWeight(poisonMushroomEarlyOdds2, earlyOdds2Weights)
    poisonMushroomEarlyOdds34 = calculateWeight(poisonMushroomEarlyOdds34, earlyOdds34Weights)
    poisonMushroomMidOdds1 = calculateWeight(poisonMushroomMidOdds1, midOdds1Weights)
    poisonMushroomMidOdds2 = calculateWeight(poisonMushroomMidOdds2, midOdds2Weights)
    poisonMushroomMidOdds34 = calculateWeight(poisonMushroomMidOdds34, midOdds34Weights)
    poisonMushroomLateOdds1 = calculateWeight(poisonMushroomLateOdds1, lateOdds1Weights)
    poisonMushroomLateOdds2 = calculateWeight(poisonMushroomLateOdds2, lateOdds2Weights)
    poisonMushroomLateOdds34 = calculateWeight(poisonMushroomLateOdds34, lateOdds34Weights)

    # Triple Poison Mushroom: DX
    triplePoisonMushroomEarlyOdds1 = calculateWeight(triplePoisonMushroomEarlyOdds1, earlyOdds1Weights)
    triplePoisonMushroomEarlyOdds2 = calculateWeight(triplePoisonMushroomEarlyOdds2, earlyOdds2Weights)
    triplePoisonMushroomEarlyOdds34 = calculateWeight(triplePoisonMushroomEarlyOdds34, earlyOdds34Weights)
    triplePoisonMushroomMidOdds1 = calculateWeight(triplePoisonMushroomMidOdds1, midOdds1Weights)
    triplePoisonMushroomMidOdds2 = calculateWeight(triplePoisonMushroomMidOdds2, midOdds2Weights)
    triplePoisonMushroomMidOdds34 = calculateWeight(triplePoisonMushroomMidOdds34, midOdds34Weights)
    triplePoisonMushroomLateOdds1 = calculateWeight(triplePoisonMushroomLateOdds1, lateOdds1Weights)
    triplePoisonMushroomLateOdds2 = calculateWeight(triplePoisonMushroomLateOdds2, lateOdds2Weights)
    triplePoisonMushroomLateOdds34 = calculateWeight(triplePoisonMushroomLateOdds34, lateOdds34Weights)

    # Celluar Shopper: DX
    celluarShopperEarlyOdds1 = calculateWeight(celluarShopperEarlyOdds1, earlyOdds1Weights)
    celluarShopperEarlyOdds2 = calculateWeight(celluarShopperEarlyOdds2, earlyOdds2Weights)
    celluarShopperEarlyOdds34 = calculateWeight(celluarShopperEarlyOdds34, earlyOdds34Weights)
    celluarShopperMidOdds1 = calculateWeight(celluarShopperMidOdds1, midOdds1Weights)
    celluarShopperMidOdds2 = calculateWeight(celluarShopperMidOdds2, midOdds2Weights)
    celluarShopperMidOdds34 = calculateWeight(celluarShopperMidOdds34, midOdds34Weights)
    celluarShopperLateOdds1 = calculateWeight(celluarShopperLateOdds1, lateOdds1Weights)
    celluarShopperLateOdds2 = calculateWeight(celluarShopperLateOdds2, lateOdds2Weights)
    celluarShopperLateOdds34 = calculateWeight(celluarShopperLateOdds34, lateOdds34Weights)

    # Skeleton Key: DX
    skeletonKeyEarlyOdds1 = calculateWeight(skeletonKeyEarlyOdds1, earlyOdds1Weights)
    skeletonKeyEarlyOdds2 = calculateWeight(skeletonKeyEarlyOdds2, earlyOdds2Weights)
    skeletonKeyEarlyOdds34 = calculateWeight(skeletonKeyEarlyOdds34, earlyOdds34Weights)
    skeletonKeyMidOdds1 = calculateWeight(skeletonKeyMidOdds1, midOdds1Weights)
    skeletonKeyMidOdds2 = calculateWeight(skeletonKeyMidOdds2, midOdds2Weights)
    skeletonKeyMidOdds34 = calculateWeight(skeletonKeyMidOdds34, midOdds34Weights)
    skeletonKeyLateOdds1 = calculateWeight(skeletonKeyLateOdds1, lateOdds1Weights)
    skeletonKeyLateOdds2 = calculateWeight(skeletonKeyLateOdds2, lateOdds2Weights)
    skeletonKeyLateOdds34 = calculateWeight(skeletonKeyLateOdds34, lateOdds34Weights)

    # Plunder Chest: DX
    plunderChestEarlyOdds1 = calculateWeight(plunderChestEarlyOdds1, earlyOdds1Weights)
    plunderChestEarlyOdds2 = calculateWeight(plunderChestEarlyOdds2, earlyOdds2Weights)
    plunderChestEarlyOdds34 = calculateWeight(plunderChestEarlyOdds34, earlyOdds34Weights)
    plunderChestMidOdds1 = calculateWeight(plunderChestMidOdds1, midOdds1Weights)
    plunderChestMidOdds2 = calculateWeight(plunderChestMidOdds2, midOdds2Weights)
    plunderChestMidOdds34 = calculateWeight(plunderChestMidOdds34, midOdds34Weights)
    plunderChestLateOdds1 = calculateWeight(plunderChestLateOdds1, lateOdds1Weights)
    plunderChestLateOdds2 = calculateWeight(plunderChestLateOdds2, lateOdds2Weights)
    plunderChestLateOdds34 = calculateWeight(plunderChestLateOdds34, lateOdds34Weights)

    # Gaddbrush: DX
    gaddbrushEarlyOdds1 = calculateWeight(gaddbrushEarlyOdds1, earlyOdds1Weights)
    gaddbrushEarlyOdds2 = calculateWeight(gaddbrushEarlyOdds2, earlyOdds2Weights)
    gaddbrushEarlyOdds34 = calculateWeight(gaddbrushEarlyOdds34, earlyOdds34Weights)
    gaddbrushMidOdds1 = calculateWeight(gaddbrushMidOdds1, midOdds1Weights)
    gaddbrushMidOdds2 = calculateWeight(gaddbrushMidOdds2, midOdds2Weights)
    gaddbrushMidOdds34 = calculateWeight(gaddbrushMidOdds34, midOdds34Weights)
    gaddbrushLateOdds1 = calculateWeight(gaddbrushLateOdds1, lateOdds1Weights)
    gaddbrushLateOdds2 = calculateWeight(gaddbrushLateOdds2, lateOdds2Weights)
    gaddbrushLateOdds34 = calculateWeight(gaddbrushLateOdds34, lateOdds34Weights)

    # Double Dip: DX
    doubleDipEarlyOdds1 = calculateWeight(doubleDipEarlyOdds1, earlyOdds1Weights)
    doubleDipEarlyOdds2 = calculateWeight(doubleDipEarlyOdds2, earlyOdds2Weights)
    doubleDipEarlyOdds34 = calculateWeight(doubleDipEarlyOdds34, earlyOdds34Weights)
    doubleDipMidOdds1 = calculateWeight(doubleDipMidOdds1, midOdds1Weights)
    doubleDipMidOdds2 = calculateWeight(doubleDipMidOdds2, midOdds2Weights)
    doubleDipMidOdds34 = calculateWeight(doubleDipMidOdds34, midOdds34Weights)
    doubleDipLateOdds1 = calculateWeight(doubleDipLateOdds1, lateOdds1Weights)
    doubleDipLateOdds2 = calculateWeight(doubleDipLateOdds2, lateOdds2Weights)
    doubleDipLateOdds34 = calculateWeight(poisonMushroomLateOdds34, lateOdds34Weights)

    # Bowser Phone
    bowserPhoneEarlyOdds1 = calculateWeight(bowserPhoneEarlyOdds1, earlyOdds1Weights)
    bowserPhoneEarlyOdds2 = calculateWeight(bowserPhoneEarlyOdds2, earlyOdds2Weights)
    bowserPhoneEarlyOdds34 = calculateWeight(bowserPhoneEarlyOdds34, earlyOdds34Weights)
    bowserPhoneMidOdds1 = calculateWeight(bowserPhoneMidOdds1, midOdds1Weights)
    bowserPhoneMidOdds2 = calculateWeight(bowserPhoneMidOdds2, midOdds2Weights)
    bowserPhoneMidOdds34 = calculateWeight(bowserPhoneMidOdds34, midOdds34Weights)
    bowserPhoneLateOdds1 = calculateWeight(bowserPhoneLateOdds1, lateOdds1Weights)
    bowserPhoneLateOdds2 = calculateWeight(bowserPhoneLateOdds2, lateOdds2Weights)
    bowserPhoneLateOdds34 = calculateWeight(bowserPhoneLateOdds34, lateOdds34Weights)

    # Hidden Block Card
    hiddenBlockCardEarlyOdds1 = calculateWeight(hiddenBlockCardEarlyOdds1, earlyOdds1Weights)
    hiddenBlockCardEarlyOdds2 = calculateWeight(hiddenBlockCardEarlyOdds2, earlyOdds2Weights)
    hiddenBlockCardEarlyOdds34 = calculateWeight(hiddenBlockCardEarlyOdds34, earlyOdds34Weights)
    hiddenBlockCardMidOdds1 = calculateWeight(hiddenBlockCardMidOdds1, midOdds1Weights)
    hiddenBlockCardMidOdds2 = calculateWeight(hiddenBlockCardMidOdds2, midOdds2Weights)
    hiddenBlockCardMidOdds34 = calculateWeight(hiddenBlockCardMidOdds34, midOdds34Weights)
    hiddenBlockCardLateOdds1 = calculateWeight(hiddenBlockCardLateOdds1, lateOdds1Weights)
    hiddenBlockCardLateOdds2 = calculateWeight(hiddenBlockCardLateOdds2, lateOdds2Weights)
    hiddenBlockCardLateOdds34 = calculateWeight(hiddenBlockCardLateOdds34, lateOdds34Weights)

    # Barter Box
    barterBoxEarlyOdds1 = calculateWeight(barterBoxEarlyOdds1, earlyOdds1Weights)
    barterBoxEarlyOdds2 = calculateWeight(barterBoxEarlyOdds2, earlyOdds2Weights)
    barterBoxEarlyOdds34 = calculateWeight(barterBoxEarlyOdds34, earlyOdds34Weights)
    barterBoxMidOdds1 = calculateWeight(barterBoxMidOdds1, midOdds1Weights)
    barterBoxMidOdds2 = calculateWeight(barterBoxMidOdds2, midOdds2Weights)
    barterBoxMidOdds34 = calculateWeight(barterBoxMidOdds34, midOdds34Weights)
    barterBoxLateOdds1 = calculateWeight(barterBoxLateOdds1, lateOdds1Weights)
    barterBoxLateOdds2 = calculateWeight(barterBoxLateOdds2, lateOdds2Weights)
    barterBoxLateOdds34 = calculateWeight(barterBoxLateOdds34, lateOdds34Weights)

    # Super Warp Pipe
    superWarpPipeEarlyOdds1 = calculateWeight(superWarpPipeEarlyOdds1, earlyOdds1Weights)
    superWarpPipeEarlyOdds2 = calculateWeight(superWarpPipeEarlyOdds2, earlyOdds2Weights)
    superWarpPipeEarlyOdds34 = calculateWeight(superWarpPipeEarlyOdds34, earlyOdds34Weights)
    superWarpPipeMidOdds1 = calculateWeight(superWarpPipeMidOdds1, midOdds1Weights)
    superWarpPipeMidOdds2 = calculateWeight(superWarpPipeMidOdds2, midOdds2Weights)
    superWarpPipeMidOdds34 = calculateWeight(superWarpPipeMidOdds34, midOdds34Weights)
    superWarpPipeLateOdds1 = calculateWeight(superWarpPipeLateOdds1, lateOdds1Weights)
    superWarpPipeLateOdds2 = calculateWeight(superWarpPipeLateOdds2, lateOdds2Weights)
    superWarpPipeLateOdds34 = calculateWeight(superWarpPipeLateOdds34, lateOdds34Weights)

    # Chance Time Charm
    chanceTimeCharmEarlyOdds1 = calculateWeight(chanceTimeCharmEarlyOdds1, earlyOdds1Weights)
    chanceTimeCharmEarlyOdds2 = calculateWeight(chanceTimeCharmEarlyOdds2, earlyOdds2Weights)
    chanceTimeCharmEarlyOdds34 = calculateWeight(chanceTimeCharmEarlyOdds34, earlyOdds34Weights)
    chanceTimeCharmMidOdds1 = calculateWeight(chanceTimeCharmMidOdds1, midOdds1Weights)
    chanceTimeCharmMidOdds2 = calculateWeight(chanceTimeCharmMidOdds2, midOdds2Weights)
    chanceTimeCharmMidOdds34 = calculateWeight(chanceTimeCharmMidOdds34, midOdds34Weights)
    chanceTimeCharmLateOdds1 = calculateWeight(chanceTimeCharmLateOdds1, lateOdds1Weights)
    chanceTimeCharmLateOdds2 = calculateWeight(chanceTimeCharmLateOdds2, lateOdds2Weights)
    chanceTimeCharmLateOdds34 = calculateWeight(chanceTimeCharmLateOdds34, lateOdds34Weights)

    # Wacky Watch
    wackyWatchEarlyOdds1 = calculateWeight(wackyWatchEarlyOdds1, earlyOdds1Weights)
    wackyWatchEarlyOdds2 = calculateWeight(wackyWatchEarlyOdds2, earlyOdds2Weights)
    wackyWatchEarlyOdds34 = calculateWeight(wackyWatchEarlyOdds34, earlyOdds34Weights)
    wackyWatchMidOdds1 = calculateWeight(wackyWatchMidOdds1, midOdds1Weights)
    wackyWatchMidOdds2 = calculateWeight(wackyWatchMidOdds2, midOdds2Weights)
    wackyWatchMidOdds34 = calculateWeight(wackyWatchMidOdds34, midOdds34Weights)
    wackyWatchLateOdds1 = calculateWeight(wackyWatchLateOdds1, lateOdds1Weights)
    wackyWatchLateOdds2 = calculateWeight(wackyWatchLateOdds2, lateOdds2Weights)
    wackyWatchLateOdds34 = calculateWeight(wackyWatchLateOdds34, lateOdds34Weights)

    # Warp Block
    warpBlockEarlyOdds1 = calculateWeight(warpBlockEarlyOdds1, earlyOdds1Weights)
    warpBlockEarlyOdds2 = calculateWeight(warpBlockEarlyOdds2, earlyOdds2Weights)
    warpBlockEarlyOdds34 = calculateWeight(warpBlockEarlyOdds34, earlyOdds34Weights)
    warpBlockMidOdds1 = calculateWeight(warpBlockMidOdds1, midOdds1Weights)
    warpBlockMidOdds2 = calculateWeight(warpBlockMidOdds2, midOdds2Weights)
    warpBlockMidOdds34 = calculateWeight(warpBlockMidOdds34, midOdds34Weights)
    warpBlockLateOdds1 = calculateWeight(warpBlockLateOdds1, lateOdds1Weights)
    warpBlockLateOdds2 = calculateWeight(warpBlockLateOdds2, lateOdds2Weights)
    warpBlockLateOdds34 = calculateWeight(warpBlockLateOdds34, lateOdds34Weights)

    # Fly Guy
    flyGuyEarlyOdds1 = calculateWeight(flyGuyEarlyOdds1, earlyOdds1Weights)
    flyGuyEarlyOdds2 = calculateWeight(flyGuyEarlyOdds2, earlyOdds2Weights)
    flyGuyEarlyOdds34 = calculateWeight(flyGuyEarlyOdds34, earlyOdds34Weights)
    flyGuyMidOdds1 = calculateWeight(flyGuyMidOdds1, midOdds1Weights)
    flyGuyMidOdds2 = calculateWeight(flyGuyMidOdds2, midOdds2Weights)
    flyGuyMidOdds34 = calculateWeight(flyGuyMidOdds34, midOdds34Weights)
    flyGuyLateOdds1 = calculateWeight(flyGuyLateOdds1, lateOdds1Weights)
    flyGuyLateOdds2 = calculateWeight(flyGuyLateOdds2, lateOdds2Weights)
    flyGuyLateOdds34 = calculateWeight(flyGuyLateOdds34, lateOdds34Weights)

    # Plus Block
    plusBlockEarlyOdds1 = calculateWeight(plusBlockEarlyOdds1, earlyOdds1Weights)
    plusBlockEarlyOdds2 = calculateWeight(plusBlockEarlyOdds2, earlyOdds2Weights)
    plusBlockEarlyOdds34 = calculateWeight(plusBlockEarlyOdds34, earlyOdds34Weights)
    plusBlockMidOdds1 = calculateWeight(plusBlockMidOdds1, midOdds1Weights)
    plusBlockMidOdds2 = calculateWeight(plusBlockMidOdds2, midOdds2Weights)
    plusBlockMidOdds34 = calculateWeight(plusBlockMidOdds34, midOdds34Weights)
    plusBlockLateOdds1 = calculateWeight(plusBlockLateOdds1, lateOdds1Weights)
    plusBlockLateOdds2 = calculateWeight(plusBlockLateOdds2, lateOdds2Weights)
    plusBlockLateOdds34 = calculateWeight(plusBlockLateOdds34, lateOdds34Weights)

    # Minus Block
    minusBlockEarlyOdds1 = calculateWeight(minusBlockEarlyOdds1, earlyOdds1Weights)
    minusBlockEarlyOdds2 = calculateWeight(minusBlockEarlyOdds2, earlyOdds2Weights)
    minusBlockEarlyOdds34 = calculateWeight(minusBlockEarlyOdds34, earlyOdds34Weights)
    minusBlockMidOdds1 = calculateWeight(minusBlockMidOdds1, midOdds1Weights)
    minusBlockMidOdds2 = calculateWeight(minusBlockMidOdds2, midOdds2Weights)
    minusBlockMidOdds34 = calculateWeight(minusBlockMidOdds34, midOdds34Weights)
    minusBlockLateOdds1 = calculateWeight(minusBlockLateOdds1, lateOdds1Weights)
    minusBlockLateOdds2 = calculateWeight(minusBlockLateOdds2, lateOdds2Weights)
    minusBlockLateOdds34 = calculateWeight(minusBlockLateOdds34, lateOdds34Weights)

    # Speed Block
    speedBlockEarlyOdds1 = calculateWeight(speedBlockEarlyOdds1, earlyOdds1Weights)
    speedBlockEarlyOdds2 = calculateWeight(speedBlockEarlyOdds2, earlyOdds2Weights)
    speedBlockEarlyOdds34 = calculateWeight(speedBlockEarlyOdds34, earlyOdds34Weights)
    speedBlockMidOdds1 = calculateWeight(speedBlockMidOdds1, midOdds1Weights)
    speedBlockMidOdds2 = calculateWeight(speedBlockMidOdds2, midOdds2Weights)
    speedBlockMidOdds34 = calculateWeight(speedBlockMidOdds34, midOdds34Weights)
    speedBlockLateOdds1 = calculateWeight(speedBlockLateOdds1, lateOdds1Weights)
    speedBlockLateOdds2 = calculateWeight(speedBlockLateOdds2, lateOdds2Weights)
    speedBlockLateOdds34 = calculateWeight(speedBlockLateOdds34, lateOdds34Weights)

    # Slow Block
    slowBlockEarlyOdds1 = calculateWeight(slowBlockEarlyOdds1, earlyOdds1Weights)
    slowBlockEarlyOdds2 = calculateWeight(slowBlockEarlyOdds2, earlyOdds2Weights)
    slowBlockEarlyOdds34 = calculateWeight(slowBlockEarlyOdds34, earlyOdds34Weights)
    slowBlockMidOdds1 = calculateWeight(slowBlockMidOdds1, midOdds1Weights)
    slowBlockMidOdds2 = calculateWeight(slowBlockMidOdds2, midOdds2Weights)
    slowBlockMidOdds34 = calculateWeight(slowBlockMidOdds34, midOdds34Weights)
    slowBlockLateOdds1 = calculateWeight(slowBlockLateOdds1, lateOdds1Weights)
    slowBlockLateOdds2 = calculateWeight(slowBlockLateOdds2, lateOdds2Weights)
    slowBlockLateOdds34 = calculateWeight(slowBlockLateOdds34, lateOdds34Weights)

    earlyOdds1 = [
        miniMushroomEarlyOdds1,
        megaMushroomEarlyOdds1,
        superMiniMushroomEarlyOdds1,
        superMegaMushroomEarlyOdds1,
        miniMegaHammerEarlyOdds1,
        warpPipeEarlyOdds1,
        swapCardEarlyOdds1,
        sparkyStickerEarlyOdds1,
        gaddlightEarlyOdds1,
        chompCallEarlyOdds1,
        bowserSuitEarlyOdds1,
        crystalBallEarlyOdds1,
        magicLampEarlyOdds1,
        itemBagEarlyOdds1,
        mushroomEarlyOdds1,
        goldenMushroomEarlyOdds1,
        reverseMushroomEarlyOdds1,
        poisonMushroomEarlyOdds1,
        triplePoisonMushroomEarlyOdds1,
        celluarShopperEarlyOdds1,
        skeletonKeyEarlyOdds1,
        plunderChestEarlyOdds1,
        gaddbrushEarlyOdds1,
        warpBlockEarlyOdds1,
        flyGuyEarlyOdds1,
        plusBlockEarlyOdds1,
        minusBlockEarlyOdds1,
        speedBlockEarlyOdds1,
        slowBlockEarlyOdds1,
        bowserPhoneEarlyOdds1,
        doubleDipEarlyOdds1,
        hiddenBlockCardEarlyOdds1,
        barterBoxEarlyOdds1,
        superWarpPipeEarlyOdds1,
        chanceTimeCharmEarlyOdds1,
        wackyWatchEarlyOdds1,
    ]

    earlyOdds2 = [
        miniMushroomEarlyOdds2,
        megaMushroomEarlyOdds2,
        superMiniMushroomEarlyOdds2,
        superMegaMushroomEarlyOdds2,
        miniMegaHammerEarlyOdds2,
        warpPipeEarlyOdds2,
        swapCardEarlyOdds2,
        sparkyStickerEarlyOdds2,
        gaddlightEarlyOdds2,
        chompCallEarlyOdds2,
        bowserSuitEarlyOdds2,
        crystalBallEarlyOdds2,
        magicLampEarlyOdds2,
        itemBagEarlyOdds2,
        mushroomEarlyOdds2,
        goldenMushroomEarlyOdds2,
        reverseMushroomEarlyOdds2,
        poisonMushroomEarlyOdds2,
        triplePoisonMushroomEarlyOdds2,
        celluarShopperEarlyOdds2,
        skeletonKeyEarlyOdds2,
        plunderChestEarlyOdds2,
        gaddbrushEarlyOdds2,
        warpBlockEarlyOdds2,
        flyGuyEarlyOdds2,
        plusBlockEarlyOdds2,
        minusBlockEarlyOdds2,
        speedBlockEarlyOdds2,
        slowBlockEarlyOdds2,
        bowserPhoneEarlyOdds2,
        doubleDipEarlyOdds2,
        hiddenBlockCardEarlyOdds2,
        barterBoxEarlyOdds2,
        superWarpPipeEarlyOdds2,
        chanceTimeCharmEarlyOdds2,
        wackyWatchEarlyOdds2,
    ]

    earlyOdds34 = [
        miniMushroomEarlyOdds34,
        megaMushroomEarlyOdds34,
        superMiniMushroomEarlyOdds34,
        superMegaMushroomEarlyOdds34,
        miniMegaHammerEarlyOdds34,
        warpPipeEarlyOdds34,
        swapCardEarlyOdds34,
        sparkyStickerEarlyOdds34,
        gaddlightEarlyOdds34,
        chompCallEarlyOdds34,
        bowserSuitEarlyOdds34,
        crystalBallEarlyOdds34,
        magicLampEarlyOdds34,
        itemBagEarlyOdds34,
        mushroomEarlyOdds34,
        goldenMushroomEarlyOdds34,
        reverseMushroomEarlyOdds34,
        poisonMushroomEarlyOdds34,
        triplePoisonMushroomEarlyOdds34,
        celluarShopperEarlyOdds34,
        skeletonKeyEarlyOdds34,
        plunderChestEarlyOdds34,
        gaddbrushEarlyOdds34,
        warpBlockEarlyOdds34,
        flyGuyEarlyOdds34,
        plusBlockEarlyOdds34,
        minusBlockEarlyOdds34,
        speedBlockEarlyOdds34,
        slowBlockEarlyOdds34,
        bowserPhoneEarlyOdds34,
        doubleDipEarlyOdds34,
        hiddenBlockCardEarlyOdds34,
        barterBoxEarlyOdds34,
        superWarpPipeEarlyOdds34,
        chanceTimeCharmEarlyOdds34,
        wackyWatchEarlyOdds34,
    ]
    
    midOdds1 = [
        miniMushroomMidOdds1,
        megaMushroomMidOdds1,
        superMiniMushroomMidOdds1,
        superMegaMushroomMidOdds1,
        miniMegaHammerMidOdds1,
        warpPipeMidOdds1,
        swapCardMidOdds1,
        sparkyStickerMidOdds1,
        gaddlightMidOdds1,
        chompCallMidOdds1,
        bowserSuitMidOdds1,
        crystalBallMidOdds1,
        magicLampMidOdds1,
        itemBagMidOdds1,
        mushroomMidOdds1,
        goldenMushroomMidOdds1,
        reverseMushroomMidOdds1,
        poisonMushroomMidOdds1,
        triplePoisonMushroomMidOdds1,
        celluarShopperMidOdds1,
        skeletonKeyMidOdds1,
        plunderChestMidOdds1,
        gaddbrushMidOdds1,
        warpBlockMidOdds1,
        flyGuyMidOdds1,
        plusBlockMidOdds1,
        minusBlockMidOdds1,
        speedBlockMidOdds1,
        slowBlockMidOdds1,
        bowserPhoneMidOdds1,
        doubleDipMidOdds1,
        hiddenBlockCardMidOdds1,
        barterBoxMidOdds1,
        superWarpPipeMidOdds1,
        chanceTimeCharmMidOdds1,
        wackyWatchMidOdds1,
    ]

    midOdds2 = [
        miniMushroomMidOdds2,
        megaMushroomMidOdds2,
        superMiniMushroomMidOdds2,
        superMegaMushroomMidOdds2,
        miniMegaHammerMidOdds2,
        warpPipeMidOdds2,
        swapCardMidOdds2,
        sparkyStickerMidOdds2,
        gaddlightMidOdds2,
        chompCallMidOdds2,
        bowserSuitMidOdds2,
        crystalBallMidOdds2,
        magicLampMidOdds2,
        itemBagMidOdds2,
        mushroomMidOdds2,
        goldenMushroomMidOdds2,
        reverseMushroomMidOdds2,
        poisonMushroomMidOdds2,
        triplePoisonMushroomMidOdds2,
        celluarShopperMidOdds2,
        skeletonKeyMidOdds2,
        plunderChestMidOdds2,
        gaddbrushMidOdds2,
        warpBlockMidOdds2,
        flyGuyMidOdds2,
        plusBlockMidOdds2,
        minusBlockMidOdds2,
        speedBlockMidOdds2,
        slowBlockMidOdds2,
        bowserPhoneMidOdds2,
        doubleDipMidOdds2,
        hiddenBlockCardMidOdds2,
        barterBoxMidOdds2,
        superWarpPipeMidOdds2,
        chanceTimeCharmMidOdds2,
        wackyWatchMidOdds2,
    ]

    midOdds34 = [
        miniMushroomMidOdds34,
        megaMushroomMidOdds34,
        superMiniMushroomMidOdds34,
        superMegaMushroomMidOdds34,
        miniMegaHammerMidOdds34,
        warpPipeMidOdds34,
        swapCardMidOdds34,
        sparkyStickerMidOdds34,
        gaddlightMidOdds34,
        chompCallMidOdds34,
        bowserSuitMidOdds34,
        crystalBallMidOdds34,
        magicLampMidOdds34,
        itemBagMidOdds34,
        mushroomMidOdds34,
        goldenMushroomMidOdds34,
        reverseMushroomMidOdds34,
        poisonMushroomMidOdds34,
        triplePoisonMushroomMidOdds34,
        celluarShopperMidOdds34,
        skeletonKeyMidOdds34,
        plunderChestMidOdds34,
        gaddbrushMidOdds34,
        warpBlockMidOdds34,
        flyGuyMidOdds34,
        plusBlockMidOdds34,
        minusBlockMidOdds34,
        speedBlockMidOdds34,
        slowBlockMidOdds34,
        bowserPhoneMidOdds34,
        doubleDipMidOdds34,
        hiddenBlockCardMidOdds34,
        barterBoxMidOdds34,
        superWarpPipeMidOdds34,
        chanceTimeCharmMidOdds34,
        wackyWatchMidOdds34,
    ]

    lateOdds1 = [
        miniMushroomLateOdds1,
        megaMushroomLateOdds1,
        superMiniMushroomLateOdds1,
        superMegaMushroomLateOdds1,
        miniMegaHammerLateOdds1,
        warpPipeLateOdds1,
        swapCardLateOdds1,
        sparkyStickerLateOdds1,
        gaddlightLateOdds1,
        chompCallLateOdds1,
        bowserSuitLateOdds1,
        crystalBallLateOdds1,
        magicLampLateOdds1,
        itemBagLateOdds1,
        mushroomLateOdds1,
        goldenMushroomLateOdds1,
        reverseMushroomLateOdds1,
        poisonMushroomLateOdds1,
        triplePoisonMushroomLateOdds1,
        celluarShopperLateOdds1,
        skeletonKeyLateOdds1,
        plunderChestLateOdds1,
        gaddbrushLateOdds1,
        warpBlockLateOdds1,
        flyGuyLateOdds1,
        plusBlockLateOdds1,
        minusBlockLateOdds1,
        speedBlockLateOdds1,
        slowBlockLateOdds1,
        bowserPhoneLateOdds1,
        doubleDipLateOdds1,
        hiddenBlockCardLateOdds1,
        barterBoxLateOdds1,
        superWarpPipeLateOdds1,
        chanceTimeCharmLateOdds1,
        wackyWatchLateOdds1,
    ]

    lateOdds2 = [
        miniMushroomLateOdds2,
        megaMushroomLateOdds2,
        superMiniMushroomLateOdds2,
        superMegaMushroomLateOdds2,
        miniMegaHammerLateOdds2,
        warpPipeLateOdds2,
        swapCardLateOdds2,
        sparkyStickerLateOdds2,
        gaddlightLateOdds2,
        chompCallLateOdds2,
        bowserSuitLateOdds2,
        crystalBallLateOdds2,
        magicLampLateOdds2,
        itemBagLateOdds2,
        mushroomLateOdds2,
        goldenMushroomLateOdds2,
        reverseMushroomLateOdds2,
        poisonMushroomLateOdds2,
        triplePoisonMushroomLateOdds2,
        celluarShopperLateOdds2,
        skeletonKeyLateOdds2,
        plunderChestLateOdds2,
        gaddbrushLateOdds2,
        warpBlockLateOdds2,
        flyGuyLateOdds2,
        plusBlockLateOdds2,
        minusBlockLateOdds2,
        speedBlockLateOdds2,
        slowBlockLateOdds2,
        bowserPhoneLateOdds2,
        doubleDipLateOdds2,
        hiddenBlockCardLateOdds2,
        barterBoxLateOdds2,
        superWarpPipeLateOdds2,
        chanceTimeCharmLateOdds2,
        wackyWatchLateOdds2,
    ]

    lateOdds34 = [
        miniMushroomLateOdds34,
        megaMushroomLateOdds34,
        superMiniMushroomLateOdds34,
        superMegaMushroomLateOdds34,
        miniMegaHammerLateOdds34,
        warpPipeLateOdds34,
        swapCardLateOdds34,
        sparkyStickerLateOdds34,
        gaddlightLateOdds34,
        chompCallLateOdds34,
        bowserSuitLateOdds34,
        crystalBallLateOdds34,
        magicLampLateOdds34,
        itemBagLateOdds34,
        mushroomLateOdds34,
        goldenMushroomLateOdds34,
        reverseMushroomLateOdds34,
        poisonMushroomLateOdds34,
        triplePoisonMushroomLateOdds34,
        celluarShopperLateOdds34,
        skeletonKeyLateOdds34,
        plunderChestLateOdds34,
        gaddbrushLateOdds34,
        warpBlockLateOdds34,
        flyGuyLateOdds34,
        plusBlockLateOdds34,
        minusBlockLateOdds34,
        speedBlockLateOdds34,
        slowBlockLateOdds34,
        bowserPhoneLateOdds34,
        doubleDipLateOdds34,
        hiddenBlockCardLateOdds34,
        barterBoxLateOdds34,
        superWarpPipeLateOdds34,
        chanceTimeCharmLateOdds34,
        wackyWatchLateOdds34,
    ]

    earlyOdds1Weights = sum(int(weight) for weight in earlyOdds1)
    earlyOdds2Weights = sum(int(weight) for weight in earlyOdds2)
    earlyOdds34Weights = sum(int(weight) for weight in earlyOdds34)
    midOdds1Weights = sum(int(weight) for weight in midOdds1)
    midOdds2Weights = sum(int(weight) for weight in midOdds2)
    midOdds34Weights = sum(int(weight) for weight in midOdds34)
    lateOdds1Weights = sum(int(weight) for weight in lateOdds1)
    lateOdds2Weights = sum(int(weight) for weight in lateOdds2)
    lateOdds34Weights = sum(int(weight) for weight in lateOdds34)

    earlyOdds1Max = max(zip(earlyOdds1, earlyOdds1), key=lambda tuple: int(tuple[1]))[0]
    earlyOdds2Max = max(zip(earlyOdds2, earlyOdds2), key=lambda tuple: int(tuple[1]))[0]
    earlyOdds34Max = max(zip(earlyOdds34, earlyOdds34), key=lambda tuple: int(tuple[1]))[0]
    midOdds1Max = max(zip(midOdds1, midOdds1), key=lambda tuple: int(tuple[1]))[0]
    midOdds2Max = max(zip(midOdds2, midOdds2), key=lambda tuple: int(tuple[1]))[0]
    midOdds34Max = max(zip(midOdds34, midOdds34), key=lambda tuple: int(tuple[1]))[0]
    lateOdds1Max = max(zip(lateOdds1, lateOdds1), key=lambda tuple: int(tuple[1]))[0]
    lateOdds2Max = max(zip(lateOdds2, lateOdds2), key=lambda tuple: int(tuple[1]))[0]
    lateOdds34Max = max(zip(lateOdds34, lateOdds34), key=lambda tuple: int(tuple[1]))[0]

    # Mini Mushroom
    if earlyOdds1Max == 'miniMushroomEarlyOdds1':
        miniMushroomEarlyOdds1 += (100 - miniMushroomEarlyOdds1)
    if earlyOdds2Max == 'miniMushroomEarlyOdds2':
        miniMushroomEarlyOdds2 += (100 - miniMushroomEarlyOdds2)
    if earlyOdds34Max == 'miniMushroomEarlyOdds34':
        miniMushroomEarlyOdds34 += (100 - miniMushroomEarlyOdds34)
    if midOdds1Max == 'miniMushroomMidOdds1':
        miniMushroomMidOdds1 += (100 - miniMushroomMidOdds1)
    if midOdds2Max == 'miniMushroomMidOdds2':
        miniMushroomMidOdds2 += (100 - miniMushroomMidOdds2)
    if midOdds34Max == 'miniMushroomMidOdds34':
        miniMushroomMidOdds34 += (100 - miniMushroomMidOdds34)
    if lateOdds1Max == 'miniMushroomLateOdds1':
        miniMushroomLateOdds1 += (100 - miniMushroomLateOdds1)
    if lateOdds2Max == 'miniMushroomLateOdds2':
        miniMushroomLateOdds2 += (100 - miniMushroomLateOdds2)
    if lateOdds34Max == 'miniMushroomLateOdds34':
        miniMushroomLateOdds34 += (100 - miniMushroomLateOdds34)

    # Mega Mushroom
    if earlyOdds1Max == 'megaMushroomEarlyOdds1':
        megaMushroomEarlyOdds1 += (100 - megaMushroomEarlyOdds1)
    if earlyOdds2Max == 'megaMushroomEarlyOdds2':
        megaMushroomEarlyOdds2 += (100 - megaMushroomEarlyOdds2)
    if earlyOdds34Max == 'megaMushroomEarlyOdds34':
        megaMushroomEarlyOdds34 += (100 - megaMushroomEarlyOdds34)
    if midOdds1Max == 'megaMushroomMidOdds1':
        megaMushroomMidOdds1 += (100 - megaMushroomMidOdds1)
    if midOdds2Max == 'megaMushroomMidOdds2':
        megaMushroomMidOdds2 += (100 - megaMushroomMidOdds2)
    if midOdds34Max == 'megaMushroomMidOdds34':
        megaMushroomMidOdds34 += (100 - megaMushroomMidOdds34)
    if lateOdds1Max == 'megaMushroomLateOdds1':
        megaMushroomLateOdds1 += (100 - megaMushroomLateOdds1)
    if lateOdds2Max == 'megaMushroomLateOdds2':
        megaMushroomLateOdds2 += (100 - megaMushroomLateOdds2)
    if lateOdds34Max == 'megaMushroomLateOdds34':
        megaMushroomLateOdds34 += (100 - megaMushroomLateOdds34)

    # Super Mini Mushroom
    if earlyOdds1Max == 'superMiniMushroomEarlyOdds1':
        superMiniMushroomEarlyOdds1 += (100 - superMiniMushroomEarlyOdds1)
    if earlyOdds2Max == 'superMiniMushroomEarlyOdds2':
        superMiniMushroomEarlyOdds2 += (100 - superMiniMushroomEarlyOdds2)
    if earlyOdds34Max == 'superMiniMushroomEarlyOdds34':
        superMiniMushroomEarlyOdds34 += (100 - superMiniMushroomEarlyOdds34)
    if midOdds1Max == 'superMiniMushroomMidOdds1':
        superMiniMushroomMidOdds1 += (100 - superMiniMushroomMidOdds1)
    if midOdds2Max == 'superMiniMushroomMidOdds2':
        superMiniMushroomMidOdds2 += (100 - superMiniMushroomMidOdds2)
    if midOdds34Max == 'superMiniMushroomMidOdds34':
        superMiniMushroomMidOdds34 += (100 - superMiniMushroomMidOdds34)
    if lateOdds1Max == 'superMiniMushroomLateOdds1':
        superMiniMushroomLateOdds1 += (100 - superMiniMushroomLateOdds1)
    if lateOdds2Max == 'superMiniMushroomLateOdds2':
        superMiniMushroomLateOdds2 += (100 - superMiniMushroomLateOdds2)
    if lateOdds34Max == 'superMiniMushroomLateOdds34':
        superMiniMushroomLateOdds34 += (100 - superMiniMushroomLateOdds34)

    # Super Mega Mushroom
    if earlyOdds1Max == 'superMegaMushroomEarlyOdds1':
        superMegaMushroomEarlyOdds1 += (100 - superMegaMushroomEarlyOdds1)
    if earlyOdds2Max == 'superMegaMushroomEarlyOdds2':
        superMegaMushroomEarlyOdds2 += (100 - superMegaMushroomEarlyOdds2)
    if earlyOdds34Max == 'superMegaMushroomEarlyOdds34':
        superMegaMushroomEarlyOdds34 += (100 - superMegaMushroomEarlyOdds34)
    if midOdds1Max == 'superMegaMushroomMidOdds1':
        superMegaMushroomMidOdds1 += (100 - superMegaMushroomMidOdds1)
    if midOdds2Max == 'superMegaMushroomMidOdds2':
        superMegaMushroomMidOdds2 += (100 - superMegaMushroomMidOdds2)
    if midOdds34Max == 'superMegaMushroomMidOdds34':
        superMegaMushroomMidOdds34 += (100 - superMegaMushroomMidOdds34)
    if lateOdds1Max == 'superMegaMushroomLateOdds1':
        superMegaMushroomLateOdds1 += (100 - superMegaMushroomLateOdds1)
    if lateOdds2Max == 'superMegaMushroomLateOdds2':
        superMegaMushroomLateOdds2 += (100 - superMegaMushroomLateOdds2)
    if lateOdds34Max == 'superMegaMushroomLateOdds34':
        superMegaMushroomLateOdds34 += (100 - superMegaMushroomLateOdds34)

    # Mini Mega Hammer
    if earlyOdds1Max == 'miniMegaHammerEarlyOdds1':
        miniMegaHammerEarlyOdds1 += (100 - miniMegaHammerEarlyOdds1)
    if earlyOdds2Max == 'miniMegaHammerEarlyOdds2':
        miniMegaHammerEarlyOdds2 += (100 - miniMegaHammerEarlyOdds2)
    if earlyOdds34Max == 'miniMegaHammerEarlyOdds34':
        miniMegaHammerEarlyOdds34 += (100 - miniMegaHammerEarlyOdds34)
    if midOdds1Max == 'miniMegaHammerMidOdds1':
        miniMegaHammerMidOdds1 += (100 - miniMegaHammerMidOdds1)
    if midOdds2Max == 'miniMegaHammerMidOdds2':
        miniMegaHammerMidOdds2 += (100 - miniMegaHammerMidOdds2)
    if midOdds34Max == 'miniMegaHammerMidOdds34':
        miniMegaHammerMidOdds34 += (100 - miniMegaHammerMidOdds34)
    if lateOdds1Max == 'miniMegaHammerLateOdds1':
        miniMegaHammerLateOdds1 += (100 - miniMegaHammerLateOdds1)
    if lateOdds2Max == 'miniMegaHammerLateOdds2':
        miniMegaHammerLateOdds2 += (100 - miniMegaHammerLateOdds2)
    if lateOdds34Max == 'miniMegaHammerLateOdds34':
        miniMegaHammerLateOdds34 += (100 - miniMegaHammerLateOdds34)

    # Warp Pipe
    if earlyOdds1Max == 'warpPipeEarlyOdds1':
        warpPipeEarlyOdds1 += (100 - warpPipeEarlyOdds1)
    if earlyOdds2Max == 'warpPipeEarlyOdds2':
        warpPipeEarlyOdds2 += (100 - warpPipeEarlyOdds2)
    if earlyOdds34Max == 'warpPipeEarlyOdds34':
        warpPipeEarlyOdds34 += (100 - warpPipeEarlyOdds34)
    if midOdds1Max == 'warpPipeMidOdds1':
        warpPipeMidOdds1 += (100 - warpPipeMidOdds1)
    if midOdds2Max == 'warpPipeMidOdds2':
        warpPipeMidOdds2 += (100 - warpPipeMidOdds2)
    if midOdds34Max == 'warpPipeMidOdds34':
        warpPipeMidOdds34 += (100 - warpPipeMidOdds34)
    if lateOdds1Max == 'warpPipeLateOdds1':
        warpPipeLateOdds1 += (100 - warpPipeLateOdds1)
    if lateOdds2Max == 'warpPipeLateOdds2':
        warpPipeLateOdds2 += (100 - warpPipeLateOdds2)
    if lateOdds34Max == 'warpPipeLateOdds34':
        warpPipeLateOdds34 += (100 - warpPipeLateOdds34)

    # Swap Card
    if earlyOdds1Max == 'swapCardEarlyOdds1':
        swapCardEarlyOdds1 += (100 - swapCardEarlyOdds1)
    if earlyOdds2Max == 'swapCardEarlyOdds2':
        swapCardEarlyOdds2 += (100 - swapCardEarlyOdds2)
    if earlyOdds34Max == 'swapCardEarlyOdds34':
        swapCardEarlyOdds34 += (100 - swapCardEarlyOdds34)
    if midOdds1Max == 'swapCardMidOdds1':
        swapCardMidOdds1 += (100 - swapCardMidOdds1)
    if midOdds2Max == 'swapCardMidOdds2':
        swapCardMidOdds2 += (100 - swapCardMidOdds2)
    if midOdds34Max == 'swapCardMidOdds34':
        swapCardMidOdds34 += (100 - swapCardMidOdds34)
    if lateOdds1Max == 'swapCardLateOdds1':
        swapCardLateOdds1 += (100 - swapCardLateOdds1)
    if lateOdds2Max == 'swapCardLateOdds2':
        swapCardLateOdds2 += (100 - swapCardLateOdds2)
    if lateOdds34Max == 'swapCardLateOdds34':
        swapCardLateOdds34 += (100 - swapCardLateOdds34)

    # Sparky Sticker
    if earlyOdds1Max == 'sparkyStickerEarlyOdds1':
        sparkyStickerEarlyOdds1 += (100 - sparkyStickerEarlyOdds1)
    if earlyOdds2Max == 'sparkyStickerEarlyOdds2':
        sparkyStickerEarlyOdds2 += (100 - sparkyStickerEarlyOdds2)
    if earlyOdds34Max == 'sparkyStickerEarlyOdds34':
        sparkyStickerEarlyOdds34 += (100 - sparkyStickerEarlyOdds34)
    if midOdds1Max == 'sparkyStickerMidOdds1':
        sparkyStickerMidOdds1 += (100 - sparkyStickerMidOdds1)
    if midOdds2Max == 'sparkyStickerMidOdds2':
        sparkyStickerMidOdds2 += (100 - sparkyStickerMidOdds2)
    if midOdds34Max == 'sparkyStickerMidOdds34':
        sparkyStickerMidOdds34 += (100 - sparkyStickerMidOdds34)
    if lateOdds1Max == 'sparkyStickerLateOdds1':
        sparkyStickerLateOdds1 += (100 - sparkyStickerLateOdds1)
    if lateOdds2Max == 'sparkyStickerLateOdds2':
        sparkyStickerLateOdds2 += (100 - sparkyStickerLateOdds2)
    if lateOdds34Max == 'sparkyStickerLateOdds34':
        sparkyStickerLateOdds34 += (100 - sparkyStickerLateOdds34)

    # Gaddlight
    if earlyOdds1Max == 'gaddlightEarlyOdds1':
        gaddlightEarlyOdds1 += (100 - gaddlightEarlyOdds1)
    if earlyOdds2Max == 'gaddlightEarlyOdds2':
        gaddlightEarlyOdds2 += (100 - gaddlightEarlyOdds2)
    if earlyOdds34Max == 'gaddlightEarlyOdds34':
        gaddlightEarlyOdds34 += (100 - gaddlightEarlyOdds34)
    if midOdds1Max == 'gaddlightMidOdds1':
        gaddlightMidOdds1 += (100 - gaddlightMidOdds1)
    if midOdds2Max == 'gaddlightMidOdds2':
        gaddlightMidOdds2 += (100 - gaddlightMidOdds2)
    if midOdds34Max == 'gaddlightMidOdds34':
        gaddlightMidOdds34 += (100 - gaddlightMidOdds34)
    if lateOdds1Max == 'gaddlightLateOdds1':
        gaddlightLateOdds1 += (100 - gaddlightLateOdds1)
    if lateOdds2Max == 'gaddlightLateOdds2':
        gaddlightLateOdds2 += (100 - gaddlightLateOdds2)
    if lateOdds34Max == 'gaddlightLateOdds34':
        gaddlightLateOdds34 += (100 - gaddlightLateOdds34)

    # Chomp Call
    if earlyOdds1Max == 'chompCallEarlyOdds1':
        chompCallEarlyOdds1 += (100 - chompCallEarlyOdds1)
    if earlyOdds2Max == 'chompCallEarlyOdds2':
        chompCallEarlyOdds2 += (100 - chompCallEarlyOdds2)
    if earlyOdds34Max == 'chompCallEarlyOdds34':
        chompCallEarlyOdds34 += (100 - chompCallEarlyOdds34)
    if midOdds1Max == 'chompCallMidOdds1':
        chompCallMidOdds1 += (100 - chompCallMidOdds1)
    if midOdds2Max == 'chompCallMidOdds2':
        chompCallMidOdds2 += (100 - chompCallMidOdds2)
    if midOdds34Max == 'chompCallMidOdds34':
        chompCallMidOdds34 += (100 - chompCallMidOdds34)
    if lateOdds1Max == 'chompCallLateOdds1':
        chompCallLateOdds1 += (100 - chompCallLateOdds1)
    if lateOdds2Max == 'chompCallLateOdds2':
        chompCallLateOdds2 += (100 - chompCallLateOdds2)
    if lateOdds34Max == 'chompCallLateOdds34':
        chompCallLateOdds34 += (100 - chompCallLateOdds34)

    # Bowser Suit
    if earlyOdds1Max == 'bowserSuitEarlyOdds1':
        bowserSuitEarlyOdds1 += (100 - bowserSuitEarlyOdds1)
    if earlyOdds2Max == 'bowserSuitEarlyOdds2':
        bowserSuitEarlyOdds2 += (100 - bowserSuitEarlyOdds2)
    if earlyOdds34Max == 'bowserSuitEarlyOdds34':
        bowserSuitEarlyOdds34 += (100 - bowserSuitEarlyOdds34)
    if midOdds1Max == 'bowserSuitMidOdds1':
        bowserSuitMidOdds1 += (100 - bowserSuitMidOdds1)
    if midOdds2Max == 'bowserSuitMidOdds2':
        bowserSuitMidOdds2 += (100 - bowserSuitMidOdds2)
    if midOdds34Max == 'bowserSuitMidOdds34':
        bowserSuitMidOdds34 += (100 - bowserSuitMidOdds34)
    if lateOdds1Max == 'bowserSuitLateOdds1':
        bowserSuitLateOdds1 += (100 - bowserSuitLateOdds1)
    if lateOdds2Max == 'bowserSuitLateOdds2':
        bowserSuitLateOdds2 += (100 - bowserSuitLateOdds2)
    if lateOdds34Max == 'bowserSuitLateOdds34':
        bowserSuitLateOdds34 += (100 - bowserSuitLateOdds34)

    # Crystal Ball
    if earlyOdds1Max == 'crystalBallEarlyOdds1':
        crystalBallEarlyOdds1 += (100 - crystalBallEarlyOdds1)
    if earlyOdds2Max == 'crystalBallEarlyOdds2':
        crystalBallEarlyOdds2 += (100 - crystalBallEarlyOdds2)
    if earlyOdds34Max == 'crystalBallEarlyOdds34':
        crystalBallEarlyOdds34 += (100 - crystalBallEarlyOdds34)
    if midOdds1Max == 'crystalBallMidOdds1':
        crystalBallMidOdds1 += (100 - crystalBallMidOdds1)
    if midOdds2Max == 'crystalBallMidOdds2':
        crystalBallMidOdds2 += (100 - crystalBallMidOdds2)
    if midOdds34Max == 'crystalBallMidOdds34':
        crystalBallMidOdds34 += (100 - crystalBallMidOdds34)
    if lateOdds1Max == 'crystalBallLateOdds1':
        crystalBallLateOdds1 += (100 - crystalBallLateOdds1)
    if lateOdds2Max == 'crystalBallLateOdds2':
        crystalBallLateOdds2 += (100 - crystalBallLateOdds2)
    if lateOdds34Max == 'crystalBallLateOdds34':
        crystalBallLateOdds34 += (100 - crystalBallLateOdds34)

    # Magic Lamp
    if earlyOdds1Max == 'magicLampEarlyOdds1':
        magicLampEarlyOdds1 += (100 - magicLampEarlyOdds1)
    if earlyOdds2Max == 'magicLampEarlyOdds2':
        magicLampEarlyOdds2 += (100 - magicLampEarlyOdds2)
    if earlyOdds34Max == 'magicLampEarlyOdds34':
        magicLampEarlyOdds34 += (100 - magicLampEarlyOdds34)
    if midOdds1Max == 'magicLampMidOdds1':
        magicLampMidOdds1 += (100 - magicLampMidOdds1)
    if midOdds2Max == 'magicLampMidOdds2':
        magicLampMidOdds2 += (100 - magicLampMidOdds2)
    if midOdds34Max == 'magicLampMidOdds34':
        magicLampMidOdds34 += (100 - magicLampMidOdds34)
    if lateOdds1Max == 'magicLampLateOdds1':
        magicLampLateOdds1 += (100 - magicLampLateOdds1)
    if lateOdds2Max == 'magicLampLateOdds2':
        magicLampLateOdds2 += (100 - magicLampLateOdds2)
    if lateOdds34Max == 'magicLampLateOdds34':
        magicLampLateOdds34 += (100 - magicLampLateOdds34)

    # Item Bag
    if earlyOdds1Max == 'itemBagEarlyOdds1':
        itemBagEarlyOdds1 += (100 - itemBagEarlyOdds1)
    if earlyOdds2Max == 'itemBagEarlyOdds2':
        itemBagEarlyOdds2 += (100 - itemBagEarlyOdds2)
    if earlyOdds34Max == 'itemBagEarlyOdds34':
        itemBagEarlyOdds34 += (100 - itemBagEarlyOdds34)
    if midOdds1Max == 'itemBagMidOdds1':
        itemBagMidOdds1 += (100 - itemBagMidOdds1)
    if midOdds2Max == 'itemBagMidOdds2':
        itemBagMidOdds2 += (100 - itemBagMidOdds2)
    if midOdds34Max == 'itemBagMidOdds34':
        itemBagMidOdds34 += (100 - itemBagMidOdds34)
    if lateOdds1Max == 'itemBagLateOdds1':
        itemBagLateOdds1 += (100 - itemBagLateOdds1)
    if lateOdds2Max == 'itemBagLateOdds2':
        itemBagLateOdds2 += (100 - itemBagLateOdds2)
    if lateOdds34Max == 'itemBagLateOdds34':
        itemBagLateOdds34 += (100 - itemBagLateOdds34)

    # Mushroom: DX
    if earlyOdds1Max == 'mushroomEarlyOdds1':
        mushroomEarlyOdds1 += (100 - mushroomEarlyOdds1)
    if earlyOdds2Max == 'mushroomEarlyOdds2':
        mushroomEarlyOdds2 += (100 - mushroomEarlyOdds2)
    if earlyOdds34Max == 'mushroomEarlyOdds34':
        mushroomEarlyOdds34 += (100 - mushroomEarlyOdds34)
    if midOdds1Max == 'mushroomMidOdds1':
        mushroomMidOdds1 += (100 - mushroomMidOdds1)
    if midOdds2Max == 'mushroomMidOdds2':
        mushroomMidOdds2 += (100 - mushroomMidOdds2)
    if midOdds34Max == 'mushroomMidOdds34':
        mushroomMidOdds34 += (100 - mushroomMidOdds34)
    if lateOdds1Max == 'mushroomLateOdds1':
        mushroomLateOdds1 += (100 - mushroomLateOdds1)
    if lateOdds2Max == 'mushroomLateOdds2':
        mushroomLateOdds2 += (100 - mushroomLateOdds2)
    if lateOdds34Max == 'mushroomLateOdds34':
        mushroomLateOdds34 += (100 - mushroomLateOdds34)

    # Golden Mushroom: DX
    if earlyOdds1Max == 'goldenMushroomEarlyOdds1':
        goldenMushroomEarlyOdds1 += (100 - goldenMushroomEarlyOdds1)
    if earlyOdds2Max == 'goldenMushroomEarlyOdds2':
        goldenMushroomEarlyOdds2 += (100 - goldenMushroomEarlyOdds2)
    if earlyOdds34Max == 'goldenMushroomEarlyOdds34':
        goldenMushroomEarlyOdds34 += (100 - goldenMushroomEarlyOdds34)
    if midOdds1Max == 'goldenMushroomMidOdds1':
        goldenMushroomMidOdds1 += (100 - goldenMushroomMidOdds1)
    if midOdds2Max == 'goldenMushroomMidOdds2':
        goldenMushroomMidOdds2 += (100 - goldenMushroomMidOdds2)
    if midOdds34Max == 'goldenMushroomMidOdds34':
        goldenMushroomMidOdds34 += (100 - goldenMushroomMidOdds34)
    if lateOdds1Max == 'goldenMushroomLateOdds1':
        goldenMushroomLateOdds1 += (100 - goldenMushroomLateOdds1)
    if lateOdds2Max == 'goldenMushroomLateOdds2':
        goldenMushroomLateOdds2 += (100 - goldenMushroomLateOdds2)
    if lateOdds34Max == 'goldenMushroomLateOdds34':
        goldenMushroomLateOdds34 += (100 - goldenMushroomLateOdds34)

    # Reverse Mushroom: DX
    if earlyOdds1Max == 'reverseMushroomEarlyOdds1':
        reverseMushroomEarlyOdds1 += (100 - reverseMushroomEarlyOdds1)
    if earlyOdds2Max == 'reverseMushroomEarlyOdds2':
        reverseMushroomEarlyOdds2 += (100 - reverseMushroomEarlyOdds2)
    if earlyOdds34Max == 'reverseMushroomEarlyOdds34':
        reverseMushroomEarlyOdds34 += (100 - reverseMushroomEarlyOdds34)
    if midOdds1Max == 'reverseMushroomMidOdds1':
        reverseMushroomMidOdds1 += (100 - reverseMushroomMidOdds1)
    if midOdds2Max == 'reverseMushroomMidOdds2':
        reverseMushroomMidOdds2 += (100 - reverseMushroomMidOdds2)
    if midOdds34Max == 'reverseMushroomMidOdds34':
        reverseMushroomMidOdds34 += (100 - reverseMushroomMidOdds34)
    if lateOdds1Max == 'reverseMushroomLateOdds1':
        reverseMushroomLateOdds1 += (100 - reverseMushroomLateOdds1)
    if lateOdds2Max == 'reverseMushroomLateOdds2':
        reverseMushroomLateOdds2 += (100 - reverseMushroomLateOdds2)
    if lateOdds34Max == 'reverseMushroomLateOdds34':
        reverseMushroomLateOdds34 += (100 - reverseMushroomLateOdds34)

    # Poison Mushroom: DX
    if earlyOdds1Max == 'poisonMushroomEarlyOdds1':
        poisonMushroomEarlyOdds1 += (100 - poisonMushroomEarlyOdds1)
    if earlyOdds2Max == 'poisonMushroomEarlyOdds2':
        poisonMushroomEarlyOdds2 += (100 - poisonMushroomEarlyOdds2)
    if earlyOdds34Max == 'poisonMushroomEarlyOdds34':
        poisonMushroomEarlyOdds34 += (100 - poisonMushroomEarlyOdds34)
    if midOdds1Max == 'poisonMushroomMidOdds1':
        poisonMushroomMidOdds1 += (100 - poisonMushroomMidOdds1)
    if midOdds2Max == 'poisonMushroomMidOdds2':
        poisonMushroomMidOdds2 += (100 - poisonMushroomMidOdds2)
    if midOdds34Max == 'poisonMushroomMidOdds34':
        poisonMushroomMidOdds34 += (100 - poisonMushroomMidOdds34)
    if lateOdds1Max == 'poisonMushroomLateOdds1':
        poisonMushroomLateOdds1 += (100 - poisonMushroomLateOdds1)
    if lateOdds2Max == 'poisonMushroomLateOdds2':
        poisonMushroomLateOdds2 += (100 - poisonMushroomLateOdds2)
    if lateOdds34Max == 'poisonMushroomLateOdds34':
        poisonMushroomLateOdds34 += (100 - poisonMushroomLateOdds34)

    # Triple Poison Mushroom: DX
    if earlyOdds1Max == 'triplePoisonMushroomEarlyOdds1':
        triplePoisonMushroomEarlyOdds1 += (100 - triplePoisonMushroomEarlyOdds1)
    if earlyOdds2Max == 'triplePoisonMushroomEarlyOdds2':
        triplePoisonMushroomEarlyOdds2 += (100 - triplePoisonMushroomEarlyOdds2)
    if earlyOdds34Max == 'triplePoisonMushroomEarlyOdds34':
        triplePoisonMushroomEarlyOdds34 += (100 - triplePoisonMushroomEarlyOdds34)
    if midOdds1Max == 'triplePoisonMushroomMidOdds1':
        triplePoisonMushroomMidOdds1 += (100 - triplePoisonMushroomMidOdds1)
    if midOdds2Max == 'triplePoisonMushroomMidOdds2':
        triplePoisonMushroomMidOdds2 += (100 - triplePoisonMushroomMidOdds2)
    if midOdds34Max == 'triplePoisonMushroomMidOdds34':
        triplePoisonMushroomMidOdds34 += (100 - triplePoisonMushroomMidOdds34)
    if lateOdds1Max == 'triplePoisonMushroomLateOdds1':
        triplePoisonMushroomLateOdds1 += (100 - triplePoisonMushroomLateOdds1)
    if lateOdds2Max == 'triplePoisonMushroomLateOdds2':
        triplePoisonMushroomLateOdds2 += (100 - triplePoisonMushroomLateOdds2)
    if lateOdds34Max == 'triplePoisonMushroomLateOdds34':
        triplePoisonMushroomLateOdds34 += (100 - triplePoisonMushroomLateOdds34)

    # Celluar Shopper: DX
    if earlyOdds1Max == 'celluarShopperEarlyOdds1':
        celluarShopperEarlyOdds1 += (100 - celluarShopperEarlyOdds1)
    if earlyOdds2Max == 'celluarShopperEarlyOdds2':
        celluarShopperEarlyOdds2 += (100 - celluarShopperEarlyOdds2)
    if earlyOdds34Max == 'celluarShopperEarlyOdds34':
        celluarShopperEarlyOdds34 += (100 - celluarShopperEarlyOdds34)
    if midOdds1Max == 'celluarShopperMidOdds1':
        celluarShopperMidOdds1 += (100 - celluarShopperMidOdds1)
    if midOdds2Max == 'celluarShopperMidOdds2':
        celluarShopperMidOdds2 += (100 - celluarShopperMidOdds2)
    if midOdds34Max == 'celluarShopperMidOdds34':
        celluarShopperMidOdds34 += (100 - celluarShopperMidOdds34)
    if lateOdds1Max == 'celluarShopperLateOdds1':
        celluarShopperLateOdds1 += (100 - celluarShopperLateOdds1)
    if lateOdds2Max == 'celluarShopperLateOdds2':
        celluarShopperLateOdds2 += (100 - celluarShopperLateOdds2)
    if lateOdds34Max == 'celluarShopperLateOdds34':
        celluarShopperLateOdds34 += (100 - celluarShopperLateOdds34)

    # Skeleton Key: DX
    if earlyOdds1Max == 'skeletonKeyEarlyOdds1':
        skeletonKeyEarlyOdds1 += (100 - skeletonKeyEarlyOdds1)
    if earlyOdds2Max == 'skeletonKeyEarlyOdds2':
        skeletonKeyEarlyOdds2 += (100 - skeletonKeyEarlyOdds2)
    if earlyOdds34Max == 'skeletonKeyEarlyOdds34':
        skeletonKeyEarlyOdds34 += (100 - skeletonKeyEarlyOdds34)
    if midOdds1Max == 'skeletonKeyMidOdds1':
        skeletonKeyMidOdds1 += (100 - skeletonKeyMidOdds1)
    if midOdds2Max == 'skeletonKeyMidOdds2':
        skeletonKeyMidOdds2 += (100 - skeletonKeyMidOdds2)
    if midOdds34Max == 'skeletonKeyMidOdds34':
        skeletonKeyMidOdds34 += (100 - skeletonKeyMidOdds34)
    if lateOdds1Max == 'skeletonKeyLateOdds1':
        skeletonKeyLateOdds1 += (100 - skeletonKeyLateOdds1)
    if lateOdds2Max == 'skeletonKeyLateOdds2':
        skeletonKeyLateOdds2 += (100 - skeletonKeyLateOdds2)
    if lateOdds34Max == 'skeletonKeyLateOdds34':
        skeletonKeyLateOdds34 += (100 - skeletonKeyLateOdds34)

    # Plunder Chest: DX
    if earlyOdds1Max == 'plunderChestEarlyOdds1':
        plunderChestEarlyOdds1 += (100 - plunderChestEarlyOdds1)
    if earlyOdds2Max == 'plunderChestEarlyOdds2':
        plunderChestEarlyOdds2 += (100 - plunderChestEarlyOdds2)
    if earlyOdds34Max == 'plunderChestEarlyOdds34':
        plunderChestEarlyOdds34 += (100 - plunderChestEarlyOdds34)
    if midOdds1Max == 'plunderChestMidOdds1':
        plunderChestMidOdds1 += (100 - plunderChestMidOdds1)
    if midOdds2Max == 'plunderChestMidOdds2':
        plunderChestMidOdds2 += (100 - plunderChestMidOdds2)
    if midOdds34Max == 'plunderChestMidOdds34':
        plunderChestMidOdds34 += (100 - plunderChestMidOdds34)
    if lateOdds1Max == 'plunderChestLateOdds1':
        plunderChestLateOdds1 += (100 - plunderChestLateOdds1)
    if lateOdds2Max == 'plunderChestLateOdds2':
        plunderChestLateOdds2 += (100 - plunderChestLateOdds2)
    if lateOdds34Max == 'plunderChestLateOdds34':
        plunderChestLateOdds34 += (100 - plunderChestLateOdds34)

    # Gaddbrush: DX
    if earlyOdds1Max == 'gaddbrushEarlyOdds1':
        gaddbrushEarlyOdds1 += (100 - gaddbrushEarlyOdds1)
    if earlyOdds2Max == 'gaddbrushEarlyOdds2':
        gaddbrushEarlyOdds2 += (100 - gaddbrushEarlyOdds2)
    if earlyOdds34Max == 'gaddbrushEarlyOdds34':
        gaddbrushEarlyOdds34 += (100 - gaddbrushEarlyOdds34)
    if midOdds1Max == 'gaddbrushMidOdds1':
        gaddbrushMidOdds1 += (100 - gaddbrushMidOdds1)
    if midOdds2Max == 'gaddbrushMidOdds2':
        gaddbrushMidOdds2 += (100 - gaddbrushMidOdds2)
    if midOdds34Max == 'gaddbrushMidOdds34':
        gaddbrushMidOdds34 += (100 - gaddbrushMidOdds34)
    if lateOdds1Max == 'gaddbrushLateOdds1':
        gaddbrushLateOdds1 += (100 - gaddbrushLateOdds1)
    if lateOdds2Max == 'gaddbrushLateOdds2':
        gaddbrushLateOdds2 += (100 - gaddbrushLateOdds2)
    if lateOdds34Max == 'gaddbrushLateOdds34':
        gaddbrushLateOdds34 += (100 - gaddbrushLateOdds34)

    # Warp Block: DX
    if earlyOdds1Max == 'warpBlockEarlyOdds1':
        warpBlockEarlyOdds1 += (100 - warpBlockEarlyOdds1)
    if earlyOdds2Max == 'warpBlockEarlyOdds2':
        warpBlockEarlyOdds2 += (100 - warpBlockEarlyOdds2)
    if earlyOdds34Max == 'warpBlockEarlyOdds34':
        warpBlockEarlyOdds34 += (100 - warpBlockEarlyOdds34)
    if midOdds1Max == 'warpBlockMidOdds1':
        warpBlockMidOdds1 += (100 - warpBlockMidOdds1)
    if midOdds2Max == 'warpBlockMidOdds2':
        warpBlockMidOdds2 += (100 - warpBlockMidOdds2)
    if midOdds34Max == 'warpBlockMidOdds34':
        warpBlockMidOdds34 += (100 - warpBlockMidOdds34)
    if lateOdds1Max == 'warpBlockLateOdds1':
        warpBlockLateOdds1 += (100 - warpBlockLateOdds1)
    if lateOdds2Max == 'warpBlockLateOdds2':
        warpBlockLateOdds2 += (100 - warpBlockLateOdds2)
    if lateOdds34Max == 'warpBlockLateOdds34':
        warpBlockLateOdds34 += (100 - warpBlockLateOdds34)

    # Fly Guy: DX
    if earlyOdds1Max == 'flyGuyEarlyOdds1':
        flyGuyEarlyOdds1 += (100 - flyGuyEarlyOdds1)
    if earlyOdds2Max == 'flyGuyEarlyOdds2':
        flyGuyEarlyOdds2 += (100 - flyGuyEarlyOdds2)
    if earlyOdds34Max == 'flyGuyEarlyOdds34':
        flyGuyEarlyOdds34 += (100 - flyGuyEarlyOdds34)
    if midOdds1Max == 'flyGuyMidOdds1':
        flyGuyMidOdds1 += (100 - flyGuyMidOdds1)
    if midOdds2Max == 'flyGuyMidOdds2':
        flyGuyMidOdds2 += (100 - flyGuyMidOdds2)
    if midOdds34Max == 'flyGuyMidOdds34':
        flyGuyMidOdds34 += (100 - flyGuyMidOdds34)
    if lateOdds1Max == 'flyGuyLateOdds1':
        flyGuyLateOdds1 += (100 - flyGuyLateOdds1)
    if lateOdds2Max == 'flyGuyLateOdds2':
        flyGuyLateOdds2 += (100 - flyGuyLateOdds2)
    if lateOdds34Max == 'flyGuyLateOdds34':
        flyGuyLateOdds34 += (100 - flyGuyLateOdds34)

    # Plus Block: DX
    if earlyOdds1Max == 'plusBlockEarlyOdds1':
        plusBlockEarlyOdds1 += (100 - plusBlockEarlyOdds1)
    if earlyOdds2Max == 'plusBlockEarlyOdds2':
        plusBlockEarlyOdds2 += (100 - plusBlockEarlyOdds2)
    if earlyOdds34Max == 'plusBlockEarlyOdds34':
        plusBlockEarlyOdds34 += (100 - plusBlockEarlyOdds34)
    if midOdds1Max == 'plusBlockMidOdds1':
        plusBlockMidOdds1 += (100 - plusBlockMidOdds1)
    if midOdds2Max == 'plusBlockMidOdds2':
        plusBlockMidOdds2 += (100 - plusBlockMidOdds2)
    if midOdds34Max == 'plusBlockMidOdds34':
        plusBlockMidOdds34 += (100 - plusBlockMidOdds34)
    if lateOdds1Max == 'plusBlockLateOdds1':
        plusBlockLateOdds1 += (100 - plusBlockLateOdds1)
    if lateOdds2Max == 'plusBlockLateOdds2':
        plusBlockLateOdds2 += (100 - plusBlockLateOdds2)
    if lateOdds34Max == 'plusBlockLateOdds34':
        plusBlockLateOdds34 += (100 - plusBlockLateOdds34)

    # Minus Block: DX
    if earlyOdds1Max == 'minusBlockEarlyOdds1':
        minusBlockEarlyOdds1 += (100 - minusBlockEarlyOdds1)
    if earlyOdds2Max == 'minusBlockEarlyOdds2':
        minusBlockEarlyOdds2 += (100 - minusBlockEarlyOdds2)
    if earlyOdds34Max == 'minusBlockEarlyOdds34':
        minusBlockEarlyOdds34 += (100 - minusBlockEarlyOdds34)
    if midOdds1Max == 'minusBlockMidOdds1':
        minusBlockMidOdds1 += (100 - minusBlockMidOdds1)
    if midOdds2Max == 'minusBlockMidOdds2':
        minusBlockMidOdds2 += (100 - minusBlockMidOdds2)
    if midOdds34Max == 'minusBlockMidOdds34':
        minusBlockMidOdds34 += (100 - minusBlockMidOdds34)
    if lateOdds1Max == 'minusBlockLateOdds1':
        minusBlockLateOdds1 += (100 - minusBlockLateOdds1)
    if lateOdds2Max == 'minusBlockLateOdds2':
        minusBlockLateOdds2 += (100 - minusBlockLateOdds2)
    if lateOdds34Max == 'minusBlockLateOdds34':
        minusBlockLateOdds34 += (100 - minusBlockLateOdds34)

    # Speed Block: DX
    if earlyOdds1Max == 'speedBlockEarlyOdds1':
        speedBlockEarlyOdds1 += (100 - speedBlockEarlyOdds1)
    if earlyOdds2Max == 'speedBlockEarlyOdds2':
        speedBlockEarlyOdds2 += (100 - speedBlockEarlyOdds2)
    if earlyOdds34Max == 'speedBlockEarlyOdds34':
        speedBlockEarlyOdds34 += (100 - speedBlockEarlyOdds34)
    if midOdds1Max == 'speedBlockMidOdds1':
        speedBlockMidOdds1 += (100 - speedBlockMidOdds1)
    if midOdds2Max == 'speedBlockMidOdds2':
        speedBlockMidOdds2 += (100 - speedBlockMidOdds2)
    if midOdds34Max == 'speedBlockMidOdds34':
        speedBlockMidOdds34 += (100 - speedBlockMidOdds34)
    if lateOdds1Max == 'speedBlockLateOdds1':
        speedBlockLateOdds1 += (100 - speedBlockLateOdds1)
    if lateOdds2Max == 'speedBlockLateOdds2':
        speedBlockLateOdds2 += (100 - speedBlockLateOdds2)
    if lateOdds34Max == 'speedBlockLateOdds34':
        speedBlockLateOdds34 += (100 - speedBlockLateOdds34)

    # Slow Block: DX
    if earlyOdds1Max == 'slowBlockEarlyOdds1':
        slowBlockEarlyOdds1 += (100 - slowBlockEarlyOdds1)
    if earlyOdds2Max == 'slowBlockEarlyOdds2':
        slowBlockEarlyOdds2 += (100 - slowBlockEarlyOdds2)
    if earlyOdds34Max == 'slowBlockEarlyOdds34':
        slowBlockEarlyOdds34 += (100 - slowBlockEarlyOdds34)
    if midOdds1Max == 'slowBlockMidOdds1':
        slowBlockMidOdds1 += (100 - slowBlockMidOdds1)
    if midOdds2Max == 'slowBlockMidOdds2':
        slowBlockMidOdds2 += (100 - slowBlockMidOdds2)
    if midOdds34Max == 'slowBlockMidOdds34':
        slowBlockMidOdds34 += (100 - slowBlockMidOdds34)
    if lateOdds1Max == 'slowBlockLateOdds1':
        slowBlockLateOdds1 += (100 - slowBlockLateOdds1)
    if lateOdds2Max == 'slowBlockLateOdds2':
        slowBlockLateOdds2 += (100 - slowBlockLateOdds2)
    if lateOdds34Max == 'slowBlockLateOdds34':
        slowBlockLateOdds34 += (100 - slowBlockLateOdds34)

    # Hidden Block Card: DX
    if earlyOdds1Max == 'hiddenBlockCardEarlyOdds1':
        hiddenBlockCardEarlyOdds1 += (100 - hiddenBlockCardEarlyOdds1)
    if earlyOdds2Max == 'hiddenBlockCardEarlyOdds2':
        hiddenBlockCardEarlyOdds2 += (100 - hiddenBlockCardEarlyOdds2)
    if earlyOdds34Max == 'hiddenBlockCardEarlyOdds34':
        hiddenBlockCardEarlyOdds34 += (100 - hiddenBlockCardEarlyOdds34)
    if midOdds1Max == 'hiddenBlockCardMidOdds1':
        hiddenBlockCardMidOdds1 += (100 - hiddenBlockCardMidOdds1)
    if midOdds2Max == 'hiddenBlockCardMidOdds2':
        hiddenBlockCardMidOdds2 += (100 - hiddenBlockCardMidOdds2)
    if midOdds34Max == 'hiddenBlockCardMidOdds34':
        hiddenBlockCardMidOdds34 += (100 - hiddenBlockCardMidOdds34)
    if lateOdds1Max == 'hiddenBlockCardLateOdds1':
        hiddenBlockCardLateOdds1 += (100 - hiddenBlockCardLateOdds1)
    if lateOdds2Max == 'hiddenBlockCardLateOdds2':
        hiddenBlockCardLateOdds2 += (100 - hiddenBlockCardLateOdds2)
    if lateOdds34Max == 'hiddenBlockCardLateOdds34':
        hiddenBlockCardLateOdds34 += (100 - hiddenBlockCardLateOdds34)

    # Barter Box: DX
    if earlyOdds1Max == 'barterBoxEarlyOdds1':
        barterBoxEarlyOdds1 += (100 - barterBoxEarlyOdds1)
    if earlyOdds2Max == 'barterBoxEarlyOdds2':
        barterBoxEarlyOdds2 += (100 - barterBoxEarlyOdds2)
    if earlyOdds34Max == 'barterBoxEarlyOdds34':
        barterBoxEarlyOdds34 += (100 - barterBoxEarlyOdds34)
    if midOdds1Max == 'barterBoxMidOdds1':
        barterBoxMidOdds1 += (100 - barterBoxMidOdds1)
    if midOdds2Max == 'barterBoxMidOdds2':
        barterBoxMidOdds2 += (100 - barterBoxMidOdds2)
    if midOdds34Max == 'barterBoxMidOdds34':
        barterBoxMidOdds34 += (100 - barterBoxMidOdds34)
    if lateOdds1Max == 'barterBoxLateOdds1':
        barterBoxLateOdds1 += (100 - barterBoxLateOdds1)
    if lateOdds2Max == 'barterBoxLateOdds2':
        barterBoxLateOdds2 += (100 - barterBoxLateOdds2)
    if lateOdds34Max == 'barterBoxLateOdds34':
        barterBoxLateOdds34 += (100 - barterBoxLateOdds34)

    # Super Warp Pipe: DX
    if earlyOdds1Max == 'superWarpPipeEarlyOdds1':
        superWarpPipeEarlyOdds1 += (100 - superWarpPipeEarlyOdds1)
    if earlyOdds2Max == 'superWarpPipeEarlyOdds2':
        superWarpPipeEarlyOdds2 += (100 - superWarpPipeEarlyOdds2)
    if earlyOdds34Max == 'superWarpPipeEarlyOdds34':
        superWarpPipeEarlyOdds34 += (100 - superWarpPipeEarlyOdds34)
    if midOdds1Max == 'superWarpPipeMidOdds1':
        superWarpPipeMidOdds1 += (100 - superWarpPipeMidOdds1)
    if midOdds2Max == 'superWarpPipeMidOdds2':
        superWarpPipeMidOdds2 += (100 - superWarpPipeMidOdds2)
    if midOdds34Max == 'superWarpPipeMidOdds34':
        superWarpPipeMidOdds34 += (100 - superWarpPipeMidOdds34)
    if lateOdds1Max == 'superWarpPipeLateOdds1':
        superWarpPipeLateOdds1 += (100 - superWarpPipeLateOdds1)
    if lateOdds2Max == 'superWarpPipeLateOdds2':
        superWarpPipeLateOdds2 += (100 - superWarpPipeLateOdds2)
    if lateOdds34Max == 'superWarpPipeLateOdds34':
        superWarpPipeLateOdds34 += (100 - superWarpPipeLateOdds34)

    # Chance Time Charm: DX
    if earlyOdds1Max == 'chanceTimeCharmEarlyOdds1':
        chanceTimeCharmEarlyOdds1 += (100 - chanceTimeCharmEarlyOdds1)
    if earlyOdds2Max == 'chanceTimeCharmEarlyOdds2':
        chanceTimeCharmEarlyOdds2 += (100 - chanceTimeCharmEarlyOdds2)
    if earlyOdds34Max == 'chanceTimeCharmEarlyOdds34':
        chanceTimeCharmEarlyOdds34 += (100 - chanceTimeCharmEarlyOdds34)
    if midOdds1Max == 'chanceTimeCharmMidOdds1':
        chanceTimeCharmMidOdds1 += (100 - chanceTimeCharmMidOdds1)
    if midOdds2Max == 'chanceTimeCharmMidOdds2':
        chanceTimeCharmMidOdds2 += (100 - chanceTimeCharmMidOdds2)
    if midOdds34Max == 'chanceTimeCharmMidOdds34':
        chanceTimeCharmMidOdds34 += (100 - chanceTimeCharmMidOdds34)
    if lateOdds1Max == 'chanceTimeCharmLateOdds1':
        chanceTimeCharmLateOdds1 += (100 - chanceTimeCharmLateOdds1)
    if lateOdds2Max == 'chanceTimeCharmLateOdds2':
        chanceTimeCharmLateOdds2 += (100 - chanceTimeCharmLateOdds2)
    if lateOdds34Max == 'chanceTimeCharmLateOdds34':
        chanceTimeCharmLateOdds34 += (100 - chanceTimeCharmLateOdds34)

    # Wacky Watch: DX
    if earlyOdds1Max == 'wackyWatchEarlyOdds1':
        wackyWatchEarlyOdds1 += (100 - wackyWatchEarlyOdds1)
    if earlyOdds2Max == 'wackyWatchEarlyOdds2':
        wackyWatchEarlyOdds2 += (100 - wackyWatchEarlyOdds2)
    if earlyOdds34Max == 'wackyWatchEarlyOdds34':
        wackyWatchEarlyOdds34 += (100 - wackyWatchEarlyOdds34)
    if midOdds1Max == 'wackyWatchMidOdds1':
        wackyWatchMidOdds1 += (100 - wackyWatchMidOdds1)
    if midOdds2Max == 'wackyWatchMidOdds2':
        wackyWatchMidOdds2 += (100 - wackyWatchMidOdds2)
    if midOdds34Max == 'wackyWatchMidOdds34':
        wackyWatchMidOdds34 += (100 - wackyWatchMidOdds34)
    if lateOdds1Max == 'wackyWatchLateOdds1':
        wackyWatchLateOdds1 += (100 - wackyWatchLateOdds1)
    if lateOdds2Max == 'wackyWatchLateOdds2':
        wackyWatchLateOdds2 += (100 - wackyWatchLateOdds2)
    if lateOdds34Max == 'wackyWatchLateOdds34':
        wackyWatchLateOdds34 += (100 - wackyWatchLateOdds34)


    # Double Dip: DX
    if earlyOdds1Max == 'doubleDipEarlyOdds1':
        doubleDipEarlyOdds1 += (100 - doubleDipEarlyOdds1)
    if earlyOdds2Max == 'doubleDipEarlyOdds2':
        doubleDipEarlyOdds2 += (100 - doubleDipEarlyOdds2)
    if earlyOdds34Max == 'doubleDipEarlyOdds34':
        doubleDipEarlyOdds34 += (100 - doubleDipEarlyOdds34)
    if midOdds1Max == 'doubleDipMidOdds1':
        doubleDipMidOdds1 += (100 - doubleDipMidOdds1)
    if midOdds2Max == 'doubleDipMidOdds2':
        doubleDipMidOdds2 += (100 - doubleDipMidOdds2)
    if midOdds34Max == 'doubleDipMidOdds34':
        doubleDipMidOdds34 += (100 - doubleDipMidOdds34)
    if lateOdds1Max == 'doubleDipLateOdds1':
        doubleDipLateOdds1 += (100 - doubleDipLateOdds1)
    if lateOdds2Max == 'doubleDipLateOdds2':
        doubleDipLateOdds2 += (100 - doubleDipLateOdds2)
    if lateOdds34Max == 'doubleDipLateOdds34':
        doubleDipLateOdds34 += (100 - doubleDipLateOdds34)


    # Mini Mushroom
    miniMushroomEarlyOdds1 = str(miniMushroomEarlyOdds1)
    miniMushroomEarlyOdds2 = str(miniMushroomEarlyOdds2)
    miniMushroomEarlyOdds34 = str(miniMushroomEarlyOdds34)
    miniMushroomMidOdds1 = str(miniMushroomMidOdds1)
    miniMushroomMidOdds2 = str(miniMushroomMidOdds2)
    miniMushroomMidOdds34 = str(miniMushroomMidOdds34)
    miniMushroomLateOdds1 = str(miniMushroomLateOdds1)
    miniMushroomLateOdds2 = str(miniMushroomLateOdds2)
    miniMushroomLateOdds34 = str(miniMushroomLateOdds34)
    
    # Mega Mushroom
    megaMushroomEarlyOdds1 = str(megaMushroomEarlyOdds1)
    megaMushroomEarlyOdds2 = str(megaMushroomEarlyOdds2)
    megaMushroomEarlyOdds34 = str(megaMushroomEarlyOdds34)
    megaMushroomMidOdds1 = str(megaMushroomMidOdds1)
    megaMushroomMidOdds2 = str(megaMushroomMidOdds2)
    megaMushroomMidOdds34 = str(megaMushroomMidOdds34)
    megaMushroomLateOdds1 = str(megaMushroomLateOdds1)
    megaMushroomLateOdds2 = str(megaMushroomLateOdds2)
    megaMushroomLateOdds34 = str(megaMushroomLateOdds34)

    # Super Mini Mushroom
    superMiniMushroomEarlyOdds1 = str(superMiniMushroomEarlyOdds1)
    superMiniMushroomEarlyOdds2 = str(superMiniMushroomEarlyOdds2)
    superMiniMushroomEarlyOdds34 = str(superMiniMushroomEarlyOdds34)
    superMiniMushroomMidOdds1 = str(superMiniMushroomMidOdds1)
    superMiniMushroomMidOdds2 = str(superMiniMushroomMidOdds2)
    superMiniMushroomMidOdds34 = str(superMiniMushroomMidOdds34)
    superMiniMushroomLateOdds1 = str(superMiniMushroomLateOdds1)
    superMiniMushroomLateOdds2 = str(superMiniMushroomLateOdds2)
    superMiniMushroomLateOdds34 = str(superMiniMushroomLateOdds34)

    # Super Mega Mushroom
    superMegaMushroomEarlyOdds1 = str(superMegaMushroomEarlyOdds1)
    superMegaMushroomEarlyOdds2 = str(superMegaMushroomEarlyOdds2)
    superMegaMushroomEarlyOdds34 = str(superMegaMushroomEarlyOdds34)
    superMegaMushroomMidOdds1 = str(superMegaMushroomMidOdds1)
    superMegaMushroomMidOdds2 = str(superMegaMushroomMidOdds2)
    superMegaMushroomMidOdds34 = str(superMegaMushroomMidOdds34)
    superMegaMushroomLateOdds1 = str(superMegaMushroomLateOdds1)
    superMegaMushroomLateOdds2 = str(superMegaMushroomLateOdds2)
    superMegaMushroomLateOdds34 = str(superMegaMushroomLateOdds34)

    # Mini Mega Hammer
    miniMegaHammerEarlyOdds1 = str(miniMegaHammerEarlyOdds1)
    miniMegaHammerEarlyOdds2 = str(miniMegaHammerEarlyOdds2)
    miniMegaHammerEarlyOdds34 = str(miniMegaHammerEarlyOdds34)
    miniMegaHammerMidOdds1 = str(miniMegaHammerMidOdds1)
    miniMegaHammerMidOdds2 = str(miniMegaHammerMidOdds2)
    miniMegaHammerMidOdds34 = str(miniMegaHammerMidOdds34)
    miniMegaHammerLateOdds1 = str(miniMegaHammerLateOdds1)
    miniMegaHammerLateOdds2 = str(miniMegaHammerLateOdds2)
    miniMegaHammerLateOdds34 = str(miniMegaHammerLateOdds34)

    # Warp Pipe
    warpPipeEarlyOdds1 = str(warpPipeEarlyOdds1)
    warpPipeEarlyOdds2 = str(warpPipeEarlyOdds2)
    warpPipeEarlyOdds34 = str(warpPipeEarlyOdds34)
    warpPipeMidOdds1 = str(warpPipeMidOdds1)
    warpPipeMidOdds2 = str(warpPipeMidOdds2)
    warpPipeMidOdds34 = str(warpPipeMidOdds34)
    warpPipeLateOdds1 = str(warpPipeLateOdds1)
    warpPipeLateOdds2 = str(warpPipeLateOdds2)
    warpPipeLateOdds34 = str(warpPipeLateOdds34)

    # Swap Card
    swapCardEarlyOdds1 = str(swapCardEarlyOdds1)
    swapCardEarlyOdds2 = str(swapCardEarlyOdds2)
    swapCardEarlyOdds34 = str(swapCardEarlyOdds34)
    swapCardMidOdds1 = str(swapCardMidOdds1)
    swapCardMidOdds2 = str(swapCardMidOdds2)
    swapCardMidOdds34 = str(swapCardMidOdds34)
    swapCardLateOdds1 = str(swapCardLateOdds1)
    swapCardLateOdds2 = str(swapCardLateOdds2)
    swapCardLateOdds34 = str(swapCardLateOdds34)

    # Sparky Sticker
    sparkyStickerEarlyOdds1 = str(sparkyStickerEarlyOdds1)
    sparkyStickerEarlyOdds2 = str(sparkyStickerEarlyOdds2)
    sparkyStickerEarlyOdds34 = str(sparkyStickerEarlyOdds34)
    sparkyStickerMidOdds1 = str(sparkyStickerMidOdds1)
    sparkyStickerMidOdds2 = str(sparkyStickerMidOdds2)
    sparkyStickerMidOdds34 = str(sparkyStickerMidOdds34)
    sparkyStickerLateOdds1 = str(sparkyStickerLateOdds1)
    sparkyStickerLateOdds2 = str(sparkyStickerLateOdds2)
    sparkyStickerLateOdds34 = str(sparkyStickerLateOdds34)

    # Gaddlight
    gaddlightEarlyOdds1 = str(gaddlightEarlyOdds1)
    gaddlightEarlyOdds2 = str(gaddlightEarlyOdds2)
    gaddlightEarlyOdds34 = str(gaddlightEarlyOdds34)
    gaddlightMidOdds1 = str(gaddlightMidOdds1)
    gaddlightMidOdds2 = str(gaddlightMidOdds2)
    gaddlightMidOdds34 = str(gaddlightMidOdds34)
    gaddlightLateOdds1 = str(gaddlightLateOdds1)
    gaddlightLateOdds2 = str(gaddlightLateOdds2)
    gaddlightLateOdds34 = str(gaddlightLateOdds34)

    # Chomp Call
    chompCallEarlyOdds1 = str(chompCallEarlyOdds1)
    chompCallEarlyOdds2 = str(chompCallEarlyOdds2)
    chompCallEarlyOdds34 = str(chompCallEarlyOdds34)
    chompCallMidOdds1 = str(chompCallMidOdds1)
    chompCallMidOdds2 = str(chompCallMidOdds2)
    chompCallMidOdds34 = str(chompCallMidOdds34)
    chompCallLateOdds1 = str(chompCallLateOdds1)
    chompCallLateOdds2 = str(chompCallLateOdds2)
    chompCallLateOdds34 = str(chompCallLateOdds34)

    # Bowser Suit
    bowserSuitEarlyOdds1 = str(bowserSuitEarlyOdds1)
    bowserSuitEarlyOdds2 = str(bowserSuitEarlyOdds2)
    bowserSuitEarlyOdds34 = str(bowserSuitEarlyOdds34)
    bowserSuitMidOdds1 = str(bowserSuitMidOdds1)
    bowserSuitMidOdds2 = str(bowserSuitMidOdds2)
    bowserSuitMidOdds34 = str(bowserSuitMidOdds34)
    bowserSuitLateOdds1 = str(bowserSuitLateOdds1)
    bowserSuitLateOdds2 = str(bowserSuitLateOdds2)
    bowserSuitLateOdds34 = str(bowserSuitLateOdds34)

    # Crystal Ball
    crystalBallEarlyOdds1 = str(crystalBallEarlyOdds1)
    crystalBallEarlyOdds2 = str(crystalBallEarlyOdds2)
    crystalBallEarlyOdds34 = str(crystalBallEarlyOdds34)
    crystalBallMidOdds1 = str(crystalBallMidOdds1)
    crystalBallMidOdds2 = str(crystalBallMidOdds2)
    crystalBallMidOdds34 = str(crystalBallMidOdds34)
    crystalBallLateOdds1 = str(crystalBallLateOdds1)
    crystalBallLateOdds2 = str(crystalBallLateOdds2)
    crystalBallLateOdds34 = str(crystalBallLateOdds34)

    # Magic Lamp
    magicLampEarlyOdds1 = str(magicLampEarlyOdds1)
    magicLampEarlyOdds2 = str(magicLampEarlyOdds2)
    magicLampEarlyOdds34 = str(magicLampEarlyOdds34)
    magicLampMidOdds1 = str(magicLampMidOdds1)
    magicLampMidOdds2 = str(magicLampMidOdds2)
    magicLampMidOdds34 = str(magicLampMidOdds34)
    magicLampLateOdds1 = str(magicLampLateOdds1)
    magicLampLateOdds2 = str(magicLampLateOdds2)
    magicLampLateOdds34 = str(magicLampLateOdds34)

    # Item Bag
    itemBagEarlyOdds1 = str(itemBagEarlyOdds1)
    itemBagEarlyOdds2 = str(itemBagEarlyOdds2)
    itemBagEarlyOdds34 = str(itemBagEarlyOdds34)
    itemBagMidOdds1 = str(itemBagMidOdds1)
    itemBagMidOdds2 = str(itemBagMidOdds2)
    itemBagMidOdds34 = str(itemBagMidOdds34)
    itemBagLateOdds1 = str(itemBagLateOdds1)
    itemBagLateOdds2 = str(itemBagLateOdds2)
    itemBagLateOdds34 = str(itemBagLateOdds34)

    # Mushroom: DX
    mushroomEarlyOdds1 = str(mushroomEarlyOdds1)
    mushroomEarlyOdds2 = str(mushroomEarlyOdds2)
    mushroomEarlyOdds34 = str(mushroomEarlyOdds34)
    mushroomMidOdds1 = str(mushroomMidOdds1)
    mushroomMidOdds2 = str(mushroomMidOdds2)
    mushroomMidOdds34 = str(mushroomMidOdds34)
    mushroomLateOdds1 = str(mushroomLateOdds1)
    mushroomLateOdds2 = str(mushroomLateOdds2)
    mushroomLateOdds34 = str(mushroomLateOdds34)

    # Golden Mushroom: DX
    goldenMushroomEarlyOdds1 = str(goldenMushroomEarlyOdds1)
    goldenMushroomEarlyOdds2 = str(goldenMushroomEarlyOdds2)
    goldenMushroomEarlyOdds34 = str(goldenMushroomEarlyOdds34)
    goldenMushroomMidOdds1 = str(goldenMushroomMidOdds1)
    goldenMushroomMidOdds2 = str(goldenMushroomMidOdds2)
    goldenMushroomMidOdds34 = str(goldenMushroomMidOdds34)
    goldenMushroomLateOdds1 = str(goldenMushroomLateOdds1)
    goldenMushroomLateOdds2 = str(goldenMushroomLateOdds2)
    goldenMushroomLateOdds34 = str(goldenMushroomLateOdds34)

    # Reverse Mushroom: DX
    reverseMushroomEarlyOdds1 = str(reverseMushroomEarlyOdds1)
    reverseMushroomEarlyOdds2 = str(reverseMushroomEarlyOdds2)
    reverseMushroomEarlyOdds34 = str(reverseMushroomEarlyOdds34)
    reverseMushroomMidOdds1 = str(reverseMushroomMidOdds1)
    reverseMushroomMidOdds2 = str(reverseMushroomMidOdds2)
    reverseMushroomMidOdds34 = str(reverseMushroomMidOdds34)
    reverseMushroomLateOdds1 = str(reverseMushroomLateOdds1)
    reverseMushroomLateOdds2 = str(reverseMushroomLateOdds2)
    reverseMushroomLateOdds34 = str(reverseMushroomLateOdds34)

    # Poison Mushroom: DX
    poisonMushroomEarlyOdds1 = str(poisonMushroomEarlyOdds1)
    poisonMushroomEarlyOdds2 = str(poisonMushroomEarlyOdds2)
    poisonMushroomEarlyOdds34 = str(poisonMushroomEarlyOdds34)
    poisonMushroomMidOdds1 = str(poisonMushroomMidOdds1)
    poisonMushroomMidOdds2 = str(poisonMushroomMidOdds2)
    poisonMushroomMidOdds34 = str(poisonMushroomMidOdds34)
    poisonMushroomLateOdds1 = str(poisonMushroomLateOdds1)
    poisonMushroomLateOdds2 = str(poisonMushroomLateOdds2)
    poisonMushroomLateOdds34 = str(poisonMushroomLateOdds34)

    # Triple Poison Mushroom: DX
    triplePoisonMushroomEarlyOdds1 = str(triplePoisonMushroomEarlyOdds1)
    triplePoisonMushroomEarlyOdds2 = str(triplePoisonMushroomEarlyOdds2)
    triplePoisonMushroomEarlyOdds34 = str(triplePoisonMushroomEarlyOdds34)
    triplePoisonMushroomMidOdds1 = str(triplePoisonMushroomMidOdds1)
    triplePoisonMushroomMidOdds2 = str(triplePoisonMushroomMidOdds2)
    triplePoisonMushroomMidOdds34 = str(triplePoisonMushroomMidOdds34)
    triplePoisonMushroomLateOdds1 = str(triplePoisonMushroomLateOdds1)
    triplePoisonMushroomLateOdds2 = str(triplePoisonMushroomLateOdds2)
    triplePoisonMushroomLateOdds34 = str(triplePoisonMushroomLateOdds34)

    # Celluar Shopper: DX
    celluarShopperEarlyOdds1 = str(celluarShopperEarlyOdds1)
    celluarShopperEarlyOdds2 = str(celluarShopperEarlyOdds2)
    celluarShopperEarlyOdds34 = str(celluarShopperEarlyOdds34)
    celluarShopperMidOdds1 = str(celluarShopperMidOdds1)
    celluarShopperMidOdds2 = str(celluarShopperMidOdds2)
    celluarShopperMidOdds34 = str(celluarShopperMidOdds34)
    celluarShopperLateOdds1 = str(celluarShopperLateOdds1)
    celluarShopperLateOdds2 = str(celluarShopperLateOdds2)
    celluarShopperLateOdds34 = str(celluarShopperLateOdds34)

    # Skeleton Key: DX
    skeletonKeyEarlyOdds1 = str(skeletonKeyEarlyOdds1)
    skeletonKeyEarlyOdds2 = str(skeletonKeyEarlyOdds2)
    skeletonKeyEarlyOdds34 = str(skeletonKeyEarlyOdds34)
    skeletonKeyMidOdds1 = str(skeletonKeyMidOdds1)
    skeletonKeyMidOdds2 = str(skeletonKeyMidOdds2)
    skeletonKeyMidOdds34 = str(skeletonKeyMidOdds34)
    skeletonKeyLateOdds1 = str(skeletonKeyLateOdds1)
    skeletonKeyLateOdds2 = str(skeletonKeyLateOdds2)
    skeletonKeyLateOdds34 = str(skeletonKeyLateOdds34)

    # Plunder Chest: DX
    plunderChestEarlyOdds1 = str(plunderChestEarlyOdds1)
    plunderChestEarlyOdds2 = str(plunderChestEarlyOdds2)
    plunderChestEarlyOdds34 = str(plunderChestEarlyOdds34)
    plunderChestMidOdds1 = str(plunderChestMidOdds1)
    plunderChestMidOdds2 = str(plunderChestMidOdds2)
    plunderChestMidOdds34 = str(plunderChestMidOdds34)
    plunderChestLateOdds1 = str(plunderChestLateOdds1)
    plunderChestLateOdds2 = str(plunderChestLateOdds2)
    plunderChestLateOdds34 = str(plunderChestLateOdds34)

    # Gaddbrush: DX
    gaddbrushEarlyOdds1 = str(gaddbrushEarlyOdds1)
    gaddbrushEarlyOdds2 = str(gaddbrushEarlyOdds2)
    gaddbrushEarlyOdds34 = str(gaddbrushEarlyOdds34)
    gaddbrushMidOdds1 = str(gaddbrushMidOdds1)
    gaddbrushMidOdds2 = str(gaddbrushMidOdds2)
    gaddbrushMidOdds34 = str(gaddbrushMidOdds34)
    gaddbrushLateOdds1 = str(gaddbrushLateOdds1)
    gaddbrushLateOdds2 = str(gaddbrushLateOdds2)
    gaddbrushLateOdds34 = str(gaddbrushLateOdds34)

    # Warp Block: DX
    warpBlockEarlyOdds1 = str(warpBlockEarlyOdds1)
    warpBlockEarlyOdds2 = str(warpBlockEarlyOdds2)
    warpBlockEarlyOdds34 = str(warpBlockEarlyOdds34)
    warpBlockMidOdds1 = str(warpBlockMidOdds1)
    warpBlockMidOdds2 = str(warpBlockMidOdds2)
    warpBlockMidOdds34 = str(warpBlockMidOdds34)
    warpBlockLateOdds1 = str(warpBlockLateOdds1)
    warpBlockLateOdds2 = str(warpBlockLateOdds2)
    warpBlockLateOdds34 = str(warpBlockLateOdds34)

    # Fly Guy: DX
    flyGuyEarlyOdds1 = str(flyGuyEarlyOdds1)
    flyGuyEarlyOdds2 = str(flyGuyEarlyOdds2)
    flyGuyEarlyOdds34 = str(flyGuyEarlyOdds34)
    flyGuyMidOdds1 = str(flyGuyMidOdds1)
    flyGuyMidOdds2 = str(flyGuyMidOdds2)
    flyGuyMidOdds34 = str(flyGuyMidOdds34)
    flyGuyLateOdds1 = str(flyGuyLateOdds1)
    flyGuyLateOdds2 = str(flyGuyLateOdds2)
    flyGuyLateOdds34 = str(flyGuyLateOdds34)

    # Plus Block: DX
    plusBlockEarlyOdds1 = str(plusBlockEarlyOdds1)
    plusBlockEarlyOdds2 = str(plusBlockEarlyOdds2)
    plusBlockEarlyOdds34 = str(plusBlockEarlyOdds34)
    plusBlockMidOdds1 = str(plusBlockMidOdds1)
    plusBlockMidOdds2 = str(plusBlockMidOdds2)
    plusBlockMidOdds34 = str(plusBlockMidOdds34)
    plusBlockLateOdds1 = str(plusBlockLateOdds1)
    plusBlockLateOdds2 = str(plusBlockLateOdds2)
    plusBlockLateOdds34 = str(plusBlockLateOdds34)

    # Minus Block: DX
    minusBlockEarlyOdds1 = str(minusBlockEarlyOdds1)
    minusBlockEarlyOdds2 = str(minusBlockEarlyOdds2)
    minusBlockEarlyOdds34 = str(minusBlockEarlyOdds34)
    minusBlockMidOdds1 = str(minusBlockMidOdds1)
    minusBlockMidOdds2 = str(minusBlockMidOdds2)
    minusBlockMidOdds34 = str(minusBlockMidOdds34)
    minusBlockLateOdds1 = str(minusBlockLateOdds1)
    minusBlockLateOdds2 = str(minusBlockLateOdds2)
    minusBlockLateOdds34 = str(minusBlockLateOdds34)

    # Speed Block: DX
    speedBlockEarlyOdds1 = str(speedBlockEarlyOdds1)
    speedBlockEarlyOdds2 = str(speedBlockEarlyOdds2)
    speedBlockEarlyOdds34 = str(speedBlockEarlyOdds34)
    speedBlockMidOdds1 = str(speedBlockMidOdds1)
    speedBlockMidOdds2 = str(speedBlockMidOdds2)
    speedBlockMidOdds34 = str(speedBlockMidOdds34)
    speedBlockLateOdds1 = str(speedBlockLateOdds1)
    speedBlockLateOdds2 = str(speedBlockLateOdds2)
    speedBlockLateOdds34 = str(speedBlockLateOdds34)

    # Slow Block: DX
    slowBlockEarlyOdds1 = str(slowBlockEarlyOdds1)
    slowBlockEarlyOdds2 = str(slowBlockEarlyOdds2)
    slowBlockEarlyOdds34 = str(slowBlockEarlyOdds34)
    slowBlockMidOdds1 = str(slowBlockMidOdds1)
    slowBlockMidOdds2 = str(slowBlockMidOdds2)
    slowBlockMidOdds34 = str(slowBlockMidOdds34)
    slowBlockLateOdds1 = str(slowBlockLateOdds1)
    slowBlockLateOdds2 = str(slowBlockLateOdds2)
    slowBlockLateOdds34 = str(slowBlockLateOdds34)

    # Hidden Block Card: DX
    hiddenBlockCardEarlyOdds1 = str(hiddenBlockCardEarlyOdds1)
    hiddenBlockCardEarlyOdds2 = str(hiddenBlockCardEarlyOdds2)
    hiddenBlockCardEarlyOdds34 = str(hiddenBlockCardEarlyOdds34)
    hiddenBlockCardMidOdds1 = str(hiddenBlockCardMidOdds1)
    hiddenBlockCardMidOdds2 = str(hiddenBlockCardMidOdds2)
    hiddenBlockCardMidOdds34 = str(hiddenBlockCardMidOdds34)
    hiddenBlockCardLateOdds1 = str(hiddenBlockCardLateOdds1)
    hiddenBlockCardLateOdds2 = str(hiddenBlockCardLateOdds2)
    hiddenBlockCardLateOdds34 = str(hiddenBlockCardLateOdds34)

    # Barter Box: DX
    barterBoxEarlyOdds1 = str(barterBoxEarlyOdds1)
    barterBoxEarlyOdds2 = str(barterBoxEarlyOdds2)
    barterBoxEarlyOdds34 = str(barterBoxEarlyOdds34)
    barterBoxMidOdds1 = str(barterBoxMidOdds1)
    barterBoxMidOdds2 = str(barterBoxMidOdds2)
    barterBoxMidOdds34 = str(barterBoxMidOdds34)
    barterBoxLateOdds1 = str(barterBoxLateOdds1)
    barterBoxLateOdds2 = str(barterBoxLateOdds2)
    barterBoxLateOdds34 = str(barterBoxLateOdds34)

    # Super Warp Pipe: DX
    superWarpPipeEarlyOdds1 = str(superWarpPipeEarlyOdds1)
    superWarpPipeEarlyOdds2 = str(superWarpPipeEarlyOdds2)
    superWarpPipeEarlyOdds34 = str(superWarpPipeEarlyOdds34)
    superWarpPipeMidOdds1 = str(superWarpPipeMidOdds1)
    superWarpPipeMidOdds2 = str(superWarpPipeMidOdds2)
    superWarpPipeMidOdds34 = str(superWarpPipeMidOdds34)
    superWarpPipeLateOdds1 = str(superWarpPipeLateOdds1)
    superWarpPipeLateOdds2 = str(superWarpPipeLateOdds2)
    superWarpPipeLateOdds34 = str(superWarpPipeLateOdds34)

    # Chance Time Charm: DX
    chanceTimeCharmEarlyOdds1 = str(chanceTimeCharmEarlyOdds1)
    chanceTimeCharmEarlyOdds2 = str(chanceTimeCharmEarlyOdds2)
    chanceTimeCharmEarlyOdds34 = str(chanceTimeCharmEarlyOdds34)
    chanceTimeCharmMidOdds1 = str(chanceTimeCharmMidOdds1)
    chanceTimeCharmMidOdds2 = str(chanceTimeCharmMidOdds2)
    chanceTimeCharmMidOdds34 = str(chanceTimeCharmMidOdds34)
    chanceTimeCharmLateOdds1 = str(chanceTimeCharmLateOdds1)
    chanceTimeCharmLateOdds2 = str(chanceTimeCharmLateOdds2)
    chanceTimeCharmLateOdds34 = str(chanceTimeCharmLateOdds34)

    # Wacky Watch: DX
    wackyWatchEarlyOdds1 = str(wackyWatchEarlyOdds1)
    wackyWatchEarlyOdds2 = str(wackyWatchEarlyOdds2)
    wackyWatchEarlyOdds34 = str(wackyWatchEarlyOdds34)
    wackyWatchMidOdds1 = str(wackyWatchMidOdds1)
    wackyWatchMidOdds2 = str(wackyWatchMidOdds2)
    wackyWatchMidOdds34 = str(wackyWatchMidOdds34)
    wackyWatchLateOdds1 = str(wackyWatchLateOdds1)
    wackyWatchLateOdds2 = str(wackyWatchLateOdds2)
    wackyWatchLateOdds34 = str(wackyWatchLateOdds34)

    # Double Dip: DX
    doubleDipEarlyOdds1 = str(doubleDipEarlyOdds1)
    doubleDipEarlyOdds2 = str(doubleDipEarlyOdds2)
    doubleDipEarlyOdds34 = str(doubleDipEarlyOdds34)
    doubleDipMidOdds1 = str(doubleDipMidOdds1)
    doubleDipMidOdds2 = str(doubleDipMidOdds2)
    doubleDipMidOdds34 = str(doubleDipMidOdds34)
    doubleDipLateOdds1 = str(doubleDipLateOdds1)
    doubleDipLateOdds2 = str(doubleDipLateOdds2)
    doubleDipLateOdds34 = str(doubleDipLateOdds34)


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
    miniMushroomEarlyOdds1 = convert_to_hex_weight(miniMushroomEarlyOdds1)
    miniMushroomEarlyOdds2 = convert_to_hex_weight(miniMushroomEarlyOdds2)
    miniMushroomEarlyOdds34 = convert_to_hex_weight(miniMushroomEarlyOdds34)
    miniMushroomMidOdds1 = convert_to_hex_weight(miniMushroomMidOdds1)
    miniMushroomMidOdds2 = convert_to_hex_weight(miniMushroomMidOdds2)
    miniMushroomMidOdds34 = convert_to_hex_weight(miniMushroomMidOdds34)
    miniMushroomLateOdds1 = convert_to_hex_weight(miniMushroomLateOdds1)
    miniMushroomLateOdds2 = convert_to_hex_weight(miniMushroomLateOdds2)
    miniMushroomLateOdds34 = convert_to_hex_weight(miniMushroomLateOdds34)
    
    # Mega Mushroom
    megaMushroomEarlyOdds1 = convert_to_hex_weight(megaMushroomEarlyOdds1)
    megaMushroomEarlyOdds2 = convert_to_hex_weight(megaMushroomEarlyOdds2)
    megaMushroomEarlyOdds34 = convert_to_hex_weight(megaMushroomEarlyOdds34)
    megaMushroomMidOdds1 = convert_to_hex_weight(megaMushroomMidOdds1)
    megaMushroomMidOdds2 = convert_to_hex_weight(megaMushroomMidOdds2)
    megaMushroomMidOdds34 = convert_to_hex_weight(megaMushroomMidOdds34)
    megaMushroomLateOdds1 = convert_to_hex_weight(megaMushroomLateOdds1)
    megaMushroomLateOdds2 = convert_to_hex_weight(megaMushroomLateOdds2)
    megaMushroomLateOdds34 = convert_to_hex_weight(megaMushroomLateOdds34)

    # Super Mini Mushroom
    superMiniMushroomEarlyOdds1 = convert_to_hex_weight(superMiniMushroomEarlyOdds1)
    superMiniMushroomEarlyOdds2 = convert_to_hex_weight(superMiniMushroomEarlyOdds2)
    superMiniMushroomEarlyOdds34 = convert_to_hex_weight(superMiniMushroomEarlyOdds34)
    superMiniMushroomMidOdds1 = convert_to_hex_weight(superMiniMushroomMidOdds1)
    superMiniMushroomMidOdds2 = convert_to_hex_weight(superMiniMushroomMidOdds2)
    superMiniMushroomMidOdds34 = convert_to_hex_weight(superMiniMushroomMidOdds34)
    superMiniMushroomLateOdds1 = convert_to_hex_weight(superMiniMushroomLateOdds1)
    superMiniMushroomLateOdds2 = convert_to_hex_weight(superMiniMushroomLateOdds2)
    superMiniMushroomLateOdds34 = convert_to_hex_weight(superMiniMushroomLateOdds34)

    # Super Mega Mushroom
    superMegaMushroomEarlyOdds1 = convert_to_hex_weight(superMegaMushroomEarlyOdds1)
    superMegaMushroomEarlyOdds2 = convert_to_hex_weight(superMegaMushroomEarlyOdds2)
    superMegaMushroomEarlyOdds34 = convert_to_hex_weight(superMegaMushroomEarlyOdds34)
    superMegaMushroomMidOdds1 = convert_to_hex_weight(superMegaMushroomMidOdds1)
    superMegaMushroomMidOdds2 = convert_to_hex_weight(superMegaMushroomMidOdds2)
    superMegaMushroomMidOdds34 = convert_to_hex_weight(superMegaMushroomMidOdds34)
    superMegaMushroomLateOdds1 = convert_to_hex_weight(superMegaMushroomLateOdds1)
    superMegaMushroomLateOdds2 = convert_to_hex_weight(superMegaMushroomLateOdds2)
    superMegaMushroomLateOdds34 = convert_to_hex_weight(superMegaMushroomLateOdds34)

    # Mini Mega Hammer
    miniMegaHammerEarlyOdds1 = convert_to_hex_weight(miniMegaHammerEarlyOdds1)
    miniMegaHammerEarlyOdds2 = convert_to_hex_weight(miniMegaHammerEarlyOdds2)
    miniMegaHammerEarlyOdds34 = convert_to_hex_weight(miniMegaHammerEarlyOdds34)
    miniMegaHammerMidOdds1 = convert_to_hex_weight(miniMegaHammerMidOdds1)
    miniMegaHammerMidOdds2 = convert_to_hex_weight(miniMegaHammerMidOdds2)
    miniMegaHammerMidOdds34 = convert_to_hex_weight(miniMegaHammerMidOdds34)
    miniMegaHammerLateOdds1 = convert_to_hex_weight(miniMegaHammerLateOdds1)
    miniMegaHammerLateOdds2 = convert_to_hex_weight(miniMegaHammerLateOdds2)
    miniMegaHammerLateOdds34 = convert_to_hex_weight(miniMegaHammerLateOdds34)

    # Warp Pipe
    warpPipeEarlyOdds1 = convert_to_hex_weight(warpPipeEarlyOdds1)
    warpPipeEarlyOdds2 = convert_to_hex_weight(warpPipeEarlyOdds2)
    warpPipeEarlyOdds34 = convert_to_hex_weight(warpPipeEarlyOdds34)
    warpPipeMidOdds1 = convert_to_hex_weight(warpPipeMidOdds1)
    warpPipeMidOdds2 = convert_to_hex_weight(warpPipeMidOdds2)
    warpPipeMidOdds34 = convert_to_hex_weight(warpPipeMidOdds34)
    warpPipeLateOdds1 = convert_to_hex_weight(warpPipeLateOdds1)
    warpPipeLateOdds2 = convert_to_hex_weight(warpPipeLateOdds2)
    warpPipeLateOdds34 = convert_to_hex_weight(warpPipeLateOdds34)

    # Swap Card
    swapCardEarlyOdds1 = convert_to_hex_weight(swapCardEarlyOdds1)
    swapCardEarlyOdds2 = convert_to_hex_weight(swapCardEarlyOdds2)
    swapCardEarlyOdds34 = convert_to_hex_weight(swapCardEarlyOdds34)
    swapCardMidOdds1 = convert_to_hex_weight(swapCardMidOdds1)
    swapCardMidOdds2 = convert_to_hex_weight(swapCardMidOdds2)
    swapCardMidOdds34 = convert_to_hex_weight(swapCardMidOdds34)
    swapCardLateOdds1 = convert_to_hex_weight(swapCardLateOdds1)
    swapCardLateOdds2 = convert_to_hex_weight(swapCardLateOdds2)
    swapCardLateOdds34 = convert_to_hex_weight(swapCardLateOdds34)

    # Sparky Sticker
    sparkyStickerEarlyOdds1 = convert_to_hex_weight(sparkyStickerEarlyOdds1)
    sparkyStickerEarlyOdds2 = convert_to_hex_weight(sparkyStickerEarlyOdds2)
    sparkyStickerEarlyOdds34 = convert_to_hex_weight(sparkyStickerEarlyOdds34)
    sparkyStickerMidOdds1 = convert_to_hex_weight(sparkyStickerMidOdds1)
    sparkyStickerMidOdds2 = convert_to_hex_weight(sparkyStickerMidOdds2)
    sparkyStickerMidOdds34 = convert_to_hex_weight(sparkyStickerMidOdds34)
    sparkyStickerLateOdds1 = convert_to_hex_weight(sparkyStickerLateOdds1)
    sparkyStickerLateOdds2 = convert_to_hex_weight(sparkyStickerLateOdds2)
    sparkyStickerLateOdds34 = convert_to_hex_weight(sparkyStickerLateOdds34)

    # Gaddlight
    gaddlightEarlyOdds1 = convert_to_hex_weight(gaddlightEarlyOdds1)
    gaddlightEarlyOdds2 = convert_to_hex_weight(gaddlightEarlyOdds2)
    gaddlightEarlyOdds34 = convert_to_hex_weight(gaddlightEarlyOdds34)
    gaddlightMidOdds1 = convert_to_hex_weight(gaddlightMidOdds1)
    gaddlightMidOdds2 = convert_to_hex_weight(gaddlightMidOdds2)
    gaddlightMidOdds34 = convert_to_hex_weight(gaddlightMidOdds34)
    gaddlightLateOdds1 = convert_to_hex_weight(gaddlightLateOdds1)
    gaddlightLateOdds2 = convert_to_hex_weight(gaddlightLateOdds2)
    gaddlightLateOdds34 = convert_to_hex_weight(gaddlightLateOdds34)

    # Chomp Call
    chompCallEarlyOdds1 = convert_to_hex_weight(chompCallEarlyOdds1)
    chompCallEarlyOdds2 = convert_to_hex_weight(chompCallEarlyOdds2)
    chompCallEarlyOdds34 = convert_to_hex_weight(chompCallEarlyOdds34)
    chompCallMidOdds1 = convert_to_hex_weight(chompCallMidOdds1)
    chompCallMidOdds2 = convert_to_hex_weight(chompCallMidOdds2)
    chompCallMidOdds34 = convert_to_hex_weight(chompCallMidOdds34)
    chompCallLateOdds1 = convert_to_hex_weight(chompCallLateOdds1)
    chompCallLateOdds2 = convert_to_hex_weight(chompCallLateOdds2)
    chompCallLateOdds34 = convert_to_hex_weight(chompCallLateOdds34)

    # Bowser Suit
    bowserSuitEarlyOdds1 = convert_to_hex_weight(bowserSuitEarlyOdds1)
    bowserSuitEarlyOdds2 = convert_to_hex_weight(bowserSuitEarlyOdds2)
    bowserSuitEarlyOdds34 = convert_to_hex_weight(bowserSuitEarlyOdds34)
    bowserSuitMidOdds1 = convert_to_hex_weight(bowserSuitMidOdds1)
    bowserSuitMidOdds2 = convert_to_hex_weight(bowserSuitMidOdds2)
    bowserSuitMidOdds34 = convert_to_hex_weight(bowserSuitMidOdds34)
    bowserSuitLateOdds1 = convert_to_hex_weight(bowserSuitLateOdds1)
    bowserSuitLateOdds2 = convert_to_hex_weight(bowserSuitLateOdds2)
    bowserSuitLateOdds34 = convert_to_hex_weight(bowserSuitLateOdds34)

    # Crystal Ball
    crystalBallEarlyOdds1 = convert_to_hex_weight(crystalBallEarlyOdds1)
    crystalBallEarlyOdds2 = convert_to_hex_weight(crystalBallEarlyOdds2)
    crystalBallEarlyOdds34 = convert_to_hex_weight(crystalBallEarlyOdds34)
    crystalBallMidOdds1 = convert_to_hex_weight(crystalBallMidOdds1)
    crystalBallMidOdds2 = convert_to_hex_weight(crystalBallMidOdds2)
    crystalBallMidOdds34 = convert_to_hex_weight(crystalBallMidOdds34)
    crystalBallLateOdds1 = convert_to_hex_weight(crystalBallLateOdds1)
    crystalBallLateOdds2 = convert_to_hex_weight(crystalBallLateOdds2)
    crystalBallLateOdds34 = convert_to_hex_weight(crystalBallLateOdds34)

    # Magic Lamp
    magicLampEarlyOdds1 = convert_to_hex_weight(magicLampEarlyOdds1)
    magicLampEarlyOdds2 = convert_to_hex_weight(magicLampEarlyOdds2)
    magicLampEarlyOdds34 = convert_to_hex_weight(magicLampEarlyOdds34)
    magicLampMidOdds1 = convert_to_hex_weight(magicLampMidOdds1)
    magicLampMidOdds2 = convert_to_hex_weight(magicLampMidOdds2)
    magicLampMidOdds34 = convert_to_hex_weight(magicLampMidOdds34)
    magicLampLateOdds1 = convert_to_hex_weight(magicLampLateOdds1)
    magicLampLateOdds2 = convert_to_hex_weight(magicLampLateOdds2)
    magicLampLateOdds34 = convert_to_hex_weight(magicLampLateOdds34)

    # Item Bag
    itemBagEarlyOdds1 = convert_to_hex_weight(itemBagEarlyOdds1)
    itemBagEarlyOdds2 = convert_to_hex_weight(itemBagEarlyOdds2)
    itemBagEarlyOdds34 = convert_to_hex_weight(itemBagEarlyOdds34)
    itemBagMidOdds1 = convert_to_hex_weight(itemBagMidOdds1)
    itemBagMidOdds2 = convert_to_hex_weight(itemBagMidOdds2)
    itemBagMidOdds34 = convert_to_hex_weight(itemBagMidOdds34)
    itemBagLateOdds1 = convert_to_hex_weight(itemBagLateOdds1)
    itemBagLateOdds2 = convert_to_hex_weight(itemBagLateOdds2)
    itemBagLateOdds34 = convert_to_hex_weight(itemBagLateOdds34)

    # Mushroom: DX
    mushroomEarlyOdds1 = convert_to_hex_weight(mushroomEarlyOdds1)
    mushroomEarlyOdds2 = convert_to_hex_weight(mushroomEarlyOdds2)
    mushroomEarlyOdds34 = convert_to_hex_weight(mushroomEarlyOdds34)
    mushroomMidOdds1 = convert_to_hex_weight(mushroomMidOdds1)
    mushroomMidOdds2 = convert_to_hex_weight(mushroomMidOdds2)
    mushroomMidOdds34 = convert_to_hex_weight(mushroomMidOdds34)
    mushroomLateOdds1 = convert_to_hex_weight(mushroomLateOdds1)
    mushroomLateOdds2 = convert_to_hex_weight(mushroomLateOdds2)
    mushroomLateOdds34 = convert_to_hex_weight(mushroomLateOdds34)

    # Golden Mushroom: DX
    goldenMushroomEarlyOdds1 = convert_to_hex_weight(goldenMushroomEarlyOdds1)
    goldenMushroomEarlyOdds2 = convert_to_hex_weight(goldenMushroomEarlyOdds2)
    goldenMushroomEarlyOdds34 = convert_to_hex_weight(goldenMushroomEarlyOdds34)
    goldenMushroomMidOdds1 = convert_to_hex_weight(goldenMushroomMidOdds1)
    goldenMushroomMidOdds2 = convert_to_hex_weight(goldenMushroomMidOdds2)
    goldenMushroomMidOdds34 = convert_to_hex_weight(goldenMushroomMidOdds34)
    goldenMushroomLateOdds1 = convert_to_hex_weight(goldenMushroomLateOdds1)
    goldenMushroomLateOdds2 = convert_to_hex_weight(goldenMushroomLateOdds2)
    goldenMushroomLateOdds34 = convert_to_hex_weight(goldenMushroomLateOdds34)

    # Reverse Mushroom: DX
    reverseMushroomEarlyOdds1 = convert_to_hex_weight(reverseMushroomEarlyOdds1)
    reverseMushroomEarlyOdds2 = convert_to_hex_weight(reverseMushroomEarlyOdds2)
    reverseMushroomEarlyOdds34 = convert_to_hex_weight(reverseMushroomEarlyOdds34)
    reverseMushroomMidOdds1 = convert_to_hex_weight(reverseMushroomMidOdds1)
    reverseMushroomMidOdds2 = convert_to_hex_weight(reverseMushroomMidOdds2)
    reverseMushroomMidOdds34 = convert_to_hex_weight(reverseMushroomMidOdds34)
    reverseMushroomLateOdds1 = convert_to_hex_weight(reverseMushroomLateOdds1)
    reverseMushroomLateOdds2 = convert_to_hex_weight(reverseMushroomLateOdds2)
    reverseMushroomLateOdds34 = convert_to_hex_weight(reverseMushroomLateOdds34)

    # Poison Mushroom: DX
    poisonMushroomEarlyOdds1 = convert_to_hex_weight(poisonMushroomEarlyOdds1)
    poisonMushroomEarlyOdds2 = convert_to_hex_weight(poisonMushroomEarlyOdds2)
    poisonMushroomEarlyOdds34 = convert_to_hex_weight(poisonMushroomEarlyOdds34)
    poisonMushroomMidOdds1 = convert_to_hex_weight(poisonMushroomMidOdds1)
    poisonMushroomMidOdds2 = convert_to_hex_weight(poisonMushroomMidOdds2)
    poisonMushroomMidOdds34 = convert_to_hex_weight(poisonMushroomMidOdds34)
    poisonMushroomLateOdds1 = convert_to_hex_weight(poisonMushroomLateOdds1)
    poisonMushroomLateOdds2 = convert_to_hex_weight(poisonMushroomLateOdds2)
    poisonMushroomLateOdds34 = convert_to_hex_weight(poisonMushroomLateOdds34)

    # Triple Poison Mushroom: DX
    triplePoisonMushroomEarlyOdds1 = convert_to_hex_weight(triplePoisonMushroomEarlyOdds1)
    triplePoisonMushroomEarlyOdds2 = convert_to_hex_weight(triplePoisonMushroomEarlyOdds2)
    triplePoisonMushroomEarlyOdds34 = convert_to_hex_weight(triplePoisonMushroomEarlyOdds34)
    triplePoisonMushroomMidOdds1 = convert_to_hex_weight(triplePoisonMushroomMidOdds1)
    triplePoisonMushroomMidOdds2 = convert_to_hex_weight(triplePoisonMushroomMidOdds2)
    triplePoisonMushroomMidOdds34 = convert_to_hex_weight(triplePoisonMushroomMidOdds34)
    triplePoisonMushroomLateOdds1 = convert_to_hex_weight(triplePoisonMushroomLateOdds1)
    triplePoisonMushroomLateOdds2 = convert_to_hex_weight(triplePoisonMushroomLateOdds2)
    triplePoisonMushroomLateOdds34 = convert_to_hex_weight(triplePoisonMushroomLateOdds34)

    # Celluar Shopper: DX
    celluarShopperEarlyOdds1 = convert_to_hex_weight(celluarShopperEarlyOdds1)
    celluarShopperEarlyOdds2 = convert_to_hex_weight(celluarShopperEarlyOdds2)
    celluarShopperEarlyOdds34 = convert_to_hex_weight(celluarShopperEarlyOdds34)
    celluarShopperMidOdds1 = convert_to_hex_weight(celluarShopperMidOdds1)
    celluarShopperMidOdds2 = convert_to_hex_weight(celluarShopperMidOdds2)
    celluarShopperMidOdds34 = convert_to_hex_weight(celluarShopperMidOdds34)
    celluarShopperLateOdds1 = convert_to_hex_weight(celluarShopperLateOdds1)
    celluarShopperLateOdds2 = convert_to_hex_weight(celluarShopperLateOdds2)
    celluarShopperLateOdds34 = convert_to_hex_weight(celluarShopperLateOdds34)

    # Skeleton Key: DX
    skeletonKeyEarlyOdds1 = convert_to_hex_weight(skeletonKeyEarlyOdds1)
    skeletonKeyEarlyOdds2 = convert_to_hex_weight(skeletonKeyEarlyOdds2)
    skeletonKeyEarlyOdds34 = convert_to_hex_weight(skeletonKeyEarlyOdds34)
    skeletonKeyMidOdds1 = convert_to_hex_weight(skeletonKeyMidOdds1)
    skeletonKeyMidOdds2 = convert_to_hex_weight(skeletonKeyMidOdds2)
    skeletonKeyMidOdds34 = convert_to_hex_weight(skeletonKeyMidOdds34)
    skeletonKeyLateOdds1 = convert_to_hex_weight(skeletonKeyLateOdds1)
    skeletonKeyLateOdds2 = convert_to_hex_weight(skeletonKeyLateOdds2)
    skeletonKeyLateOdds34 = convert_to_hex_weight(skeletonKeyLateOdds34)

    # Plunder Chest: DX
    plunderChestEarlyOdds1 = convert_to_hex_weight(plunderChestEarlyOdds1)
    plunderChestEarlyOdds2 = convert_to_hex_weight(plunderChestEarlyOdds2)
    plunderChestEarlyOdds34 = convert_to_hex_weight(plunderChestEarlyOdds34)
    plunderChestMidOdds1 = convert_to_hex_weight(plunderChestMidOdds1)
    plunderChestMidOdds2 = convert_to_hex_weight(plunderChestMidOdds2)
    plunderChestMidOdds34 = convert_to_hex_weight(plunderChestMidOdds34)
    plunderChestLateOdds1 = convert_to_hex_weight(plunderChestLateOdds1)
    plunderChestLateOdds2 = convert_to_hex_weight(plunderChestLateOdds2)
    plunderChestLateOdds34 = convert_to_hex_weight(plunderChestLateOdds34)

    # Gaddbrush: DX
    gaddbrushEarlyOdds1 = convert_to_hex_weight(gaddbrushEarlyOdds1)
    gaddbrushEarlyOdds2 = convert_to_hex_weight(gaddbrushEarlyOdds2)
    gaddbrushEarlyOdds34 = convert_to_hex_weight(gaddbrushEarlyOdds34)
    gaddbrushMidOdds1 = convert_to_hex_weight(gaddbrushMidOdds1)
    gaddbrushMidOdds2 = convert_to_hex_weight(gaddbrushMidOdds2)
    gaddbrushMidOdds34 = convert_to_hex_weight(gaddbrushMidOdds34)
    gaddbrushLateOdds1 = convert_to_hex_weight(gaddbrushLateOdds1)
    gaddbrushLateOdds2 = convert_to_hex_weight(gaddbrushLateOdds2)
    gaddbrushLateOdds34 = convert_to_hex_weight(gaddbrushLateOdds34)

    # Warp Block: DX
    warpBlockEarlyOdds1 = convert_to_hex_weight(warpBlockEarlyOdds1)
    warpBlockEarlyOdds2 = convert_to_hex_weight(warpBlockEarlyOdds2)
    warpBlockEarlyOdds34 = convert_to_hex_weight(warpBlockEarlyOdds34)
    warpBlockMidOdds1 = convert_to_hex_weight(warpBlockMidOdds1)
    warpBlockMidOdds2 = convert_to_hex_weight(warpBlockMidOdds2)
    warpBlockMidOdds34 = convert_to_hex_weight(warpBlockMidOdds34)
    warpBlockLateOdds1 = convert_to_hex_weight(warpBlockLateOdds1)
    warpBlockLateOdds2 = convert_to_hex_weight(warpBlockLateOdds2)
    warpBlockLateOdds34 = convert_to_hex_weight(warpBlockLateOdds34)

    # Fly Guy: DX
    flyGuyEarlyOdds1 = convert_to_hex_weight(flyGuyEarlyOdds1)
    flyGuyEarlyOdds2 = convert_to_hex_weight(flyGuyEarlyOdds2)
    flyGuyEarlyOdds34 = convert_to_hex_weight(flyGuyEarlyOdds34)
    flyGuyMidOdds1 = convert_to_hex_weight(flyGuyMidOdds1)
    flyGuyMidOdds2 = convert_to_hex_weight(flyGuyMidOdds2)
    flyGuyMidOdds34 = convert_to_hex_weight(flyGuyMidOdds34)
    flyGuyLateOdds1 = convert_to_hex_weight(flyGuyLateOdds1)
    flyGuyLateOdds2 = convert_to_hex_weight(flyGuyLateOdds2)
    flyGuyLateOdds34 = convert_to_hex_weight(flyGuyLateOdds34)

    # Plus Block: DX
    plusBlockEarlyOdds1 = convert_to_hex_weight(plusBlockEarlyOdds1)
    plusBlockEarlyOdds2 = convert_to_hex_weight(plusBlockEarlyOdds2)
    plusBlockEarlyOdds34 = convert_to_hex_weight(plusBlockEarlyOdds34)
    plusBlockMidOdds1 = convert_to_hex_weight(plusBlockMidOdds1)
    plusBlockMidOdds2 = convert_to_hex_weight(plusBlockMidOdds2)
    plusBlockMidOdds34 = convert_to_hex_weight(plusBlockMidOdds34)
    plusBlockLateOdds1 = convert_to_hex_weight(plusBlockLateOdds1)
    plusBlockLateOdds2 = convert_to_hex_weight(plusBlockLateOdds2)
    plusBlockLateOdds34 = convert_to_hex_weight(plusBlockLateOdds34)

    # Minus Block: DX
    minusBlockEarlyOdds1 = convert_to_hex_weight(minusBlockEarlyOdds1)
    minusBlockEarlyOdds2 = convert_to_hex_weight(minusBlockEarlyOdds2)
    minusBlockEarlyOdds34 = convert_to_hex_weight(minusBlockEarlyOdds34)
    minusBlockMidOdds1 = convert_to_hex_weight(minusBlockMidOdds1)
    minusBlockMidOdds2 = convert_to_hex_weight(minusBlockMidOdds2)
    minusBlockMidOdds34 = convert_to_hex_weight(minusBlockMidOdds34)
    minusBlockLateOdds1 = convert_to_hex_weight(minusBlockLateOdds1)
    minusBlockLateOdds2 = convert_to_hex_weight(minusBlockLateOdds2)
    minusBlockLateOdds34 = convert_to_hex_weight(minusBlockLateOdds34)

    # Speed Block: DX
    speedBlockEarlyOdds1 = convert_to_hex_weight(speedBlockEarlyOdds1)
    speedBlockEarlyOdds2 = convert_to_hex_weight(speedBlockEarlyOdds2)
    speedBlockEarlyOdds34 = convert_to_hex_weight(speedBlockEarlyOdds34)
    speedBlockMidOdds1 = convert_to_hex_weight(speedBlockMidOdds1)
    speedBlockMidOdds2 = convert_to_hex_weight(speedBlockMidOdds2)
    speedBlockMidOdds34 = convert_to_hex_weight(speedBlockMidOdds34)
    speedBlockLateOdds1 = convert_to_hex_weight(speedBlockLateOdds1)
    speedBlockLateOdds2 = convert_to_hex_weight(speedBlockLateOdds2)
    speedBlockLateOdds34 = convert_to_hex_weight(speedBlockLateOdds34)

    # Slow Block: DX
    slowBlockEarlyOdds1 = convert_to_hex_weight(slowBlockEarlyOdds1)
    slowBlockEarlyOdds2 = convert_to_hex_weight(slowBlockEarlyOdds2)
    slowBlockEarlyOdds34 = convert_to_hex_weight(slowBlockEarlyOdds34)
    slowBlockMidOdds1 = convert_to_hex_weight(slowBlockMidOdds1)
    slowBlockMidOdds2 = convert_to_hex_weight(slowBlockMidOdds2)
    slowBlockMidOdds34 = convert_to_hex_weight(slowBlockMidOdds34)
    slowBlockLateOdds1 = convert_to_hex_weight(slowBlockLateOdds1)
    slowBlockLateOdds2 = convert_to_hex_weight(slowBlockLateOdds2)
    slowBlockLateOdds34 = convert_to_hex_weight(slowBlockLateOdds34)

    # Hidden Block Card: DX
    hiddenBlockCardEarlyOdds1 = convert_to_hex_weight(hiddenBlockCardEarlyOdds1)
    hiddenBlockCardEarlyOdds2 = convert_to_hex_weight(hiddenBlockCardEarlyOdds2)
    hiddenBlockCardEarlyOdds34 = convert_to_hex_weight(hiddenBlockCardEarlyOdds34)
    hiddenBlockCardMidOdds1 = convert_to_hex_weight(hiddenBlockCardMidOdds1)
    hiddenBlockCardMidOdds2 = convert_to_hex_weight(hiddenBlockCardMidOdds2)
    hiddenBlockCardMidOdds34 = convert_to_hex_weight(hiddenBlockCardMidOdds34)
    hiddenBlockCardLateOdds1 = convert_to_hex_weight(hiddenBlockCardLateOdds1)
    hiddenBlockCardLateOdds2 = convert_to_hex_weight(hiddenBlockCardLateOdds2)
    hiddenBlockCardLateOdds34 = convert_to_hex_weight(hiddenBlockCardLateOdds34)

    # Barter Box: DX
    barterBoxEarlyOdds1 = convert_to_hex_weight(barterBoxEarlyOdds1)
    barterBoxEarlyOdds2 = convert_to_hex_weight(barterBoxEarlyOdds2)
    barterBoxEarlyOdds34 = convert_to_hex_weight(barterBoxEarlyOdds34)
    barterBoxMidOdds1 = convert_to_hex_weight(barterBoxMidOdds1)
    barterBoxMidOdds2 = convert_to_hex_weight(barterBoxMidOdds2)
    barterBoxMidOdds34 = convert_to_hex_weight(barterBoxMidOdds34)
    barterBoxLateOdds1 = convert_to_hex_weight(barterBoxLateOdds1)
    barterBoxLateOdds2 = convert_to_hex_weight(barterBoxLateOdds2)
    barterBoxLateOdds34 = convert_to_hex_weight(barterBoxLateOdds34)

    # Super Warp Pipe: DX
    superWarpPipeEarlyOdds1 = convert_to_hex_weight(superWarpPipeEarlyOdds1)
    superWarpPipeEarlyOdds2 = convert_to_hex_weight(superWarpPipeEarlyOdds2)
    superWarpPipeEarlyOdds34 = convert_to_hex_weight(superWarpPipeEarlyOdds34)
    superWarpPipeMidOdds1 = convert_to_hex_weight(superWarpPipeMidOdds1)
    superWarpPipeMidOdds2 = convert_to_hex_weight(superWarpPipeMidOdds2)
    superWarpPipeMidOdds34 = convert_to_hex_weight(superWarpPipeMidOdds34)
    superWarpPipeLateOdds1 = convert_to_hex_weight(superWarpPipeLateOdds1)
    superWarpPipeLateOdds2 = convert_to_hex_weight(superWarpPipeLateOdds2)
    superWarpPipeLateOdds34 = convert_to_hex_weight(superWarpPipeLateOdds34)

    # Chance Time Charm: DX
    chanceTimeCharmEarlyOdds1 = convert_to_hex_weight(chanceTimeCharmEarlyOdds1)
    chanceTimeCharmEarlyOdds2 = convert_to_hex_weight(chanceTimeCharmEarlyOdds2)
    chanceTimeCharmEarlyOdds34 = convert_to_hex_weight(chanceTimeCharmEarlyOdds34)
    chanceTimeCharmMidOdds1 = convert_to_hex_weight(chanceTimeCharmMidOdds1)
    chanceTimeCharmMidOdds2 = convert_to_hex_weight(chanceTimeCharmMidOdds2)
    chanceTimeCharmMidOdds34 = convert_to_hex_weight(chanceTimeCharmMidOdds34)
    chanceTimeCharmLateOdds1 = convert_to_hex_weight(chanceTimeCharmLateOdds1)
    chanceTimeCharmLateOdds2 = convert_to_hex_weight(chanceTimeCharmLateOdds2)
    chanceTimeCharmLateOdds34 = convert_to_hex_weight(chanceTimeCharmLateOdds34)

    # Wacky Watch: DX
    wackyWatchEarlyOdds1 = convert_to_hex_weight(wackyWatchEarlyOdds1)
    wackyWatchEarlyOdds2 = convert_to_hex_weight(wackyWatchEarlyOdds2)
    wackyWatchEarlyOdds34 = convert_to_hex_weight(wackyWatchEarlyOdds34)
    wackyWatchMidOdds1 = convert_to_hex_weight(wackyWatchMidOdds1)
    wackyWatchMidOdds2 = convert_to_hex_weight(wackyWatchMidOdds2)
    wackyWatchMidOdds34 = convert_to_hex_weight(wackyWatchMidOdds34)
    wackyWatchLateOdds1 = convert_to_hex_weight(wackyWatchLateOdds1)
    wackyWatchLateOdds2 = convert_to_hex_weight(wackyWatchLateOdds2)
    wackyWatchLateOdds34 = convert_to_hex_weight(wackyWatchLateOdds34)

    # Bowser Phone: DX
    bowserPhoneEarlyOdds1 = convert_to_hex_weight(bowserPhoneEarlyOdds1)
    bowserPhoneEarlyOdds2 = convert_to_hex_weight(bowserPhoneEarlyOdds2)
    bowserPhoneEarlyOdds34 = convert_to_hex_weight(bowserPhoneEarlyOdds34)
    bowserPhoneMidOdds1 = convert_to_hex_weight(bowserPhoneMidOdds1)
    bowserPhoneMidOdds2 = convert_to_hex_weight(bowserPhoneMidOdds2)
    bowserPhoneMidOdds34 = convert_to_hex_weight(bowserPhoneMidOdds34)
    bowserPhoneLateOdds1 = convert_to_hex_weight(bowserPhoneLateOdds1)
    bowserPhoneLateOdds2 = convert_to_hex_weight(bowserPhoneLateOdds2)
    bowserPhoneLateOdds34 = convert_to_hex_weight(bowserPhoneLateOdds34)

    # Double Dip: DX
    doubleDipEarlyOdds1 = convert_to_hex_weight(doubleDipEarlyOdds1)
    doubleDipEarlyOdds2 = convert_to_hex_weight(doubleDipEarlyOdds2)
    doubleDipEarlyOdds34 = convert_to_hex_weight(doubleDipEarlyOdds34)
    doubleDipMidOdds1 = convert_to_hex_weight(doubleDipMidOdds1)
    doubleDipMidOdds2 = convert_to_hex_weight(doubleDipMidOdds2)
    doubleDipMidOdds34 = convert_to_hex_weight(doubleDipMidOdds34)
    doubleDipLateOdds1 = convert_to_hex_weight(doubleDipLateOdds1)
    doubleDipLateOdds2 = convert_to_hex_weight(doubleDipLateOdds2)
    doubleDipLateOdds34 = convert_to_hex_weight(doubleDipLateOdds34)
    
    generatedCode = getItemShopOddsFourDX(miniMushroomEarlyOdds1, miniMushroomEarlyOdds2, miniMushroomEarlyOdds34, miniMushroomMidOdds1, miniMushroomMidOdds2, miniMushroomMidOdds34, miniMushroomLateOdds1, miniMushroomLateOdds2, miniMushroomLateOdds34, megaMushroomEarlyOdds1, megaMushroomEarlyOdds2, megaMushroomEarlyOdds34, megaMushroomMidOdds1, megaMushroomMidOdds2, megaMushroomMidOdds34, megaMushroomLateOdds1, megaMushroomLateOdds2, megaMushroomLateOdds34, superMiniMushroomEarlyOdds1, superMiniMushroomEarlyOdds2, superMiniMushroomEarlyOdds34, superMiniMushroomMidOdds1, superMiniMushroomMidOdds2, superMiniMushroomMidOdds34, superMiniMushroomLateOdds1, superMiniMushroomLateOdds2, superMiniMushroomLateOdds34, superMegaMushroomEarlyOdds1, superMegaMushroomEarlyOdds2, superMegaMushroomEarlyOdds34, superMegaMushroomMidOdds1, superMegaMushroomMidOdds2, superMegaMushroomMidOdds34, superMegaMushroomLateOdds1, superMegaMushroomLateOdds2, superMegaMushroomLateOdds34, miniMegaHammerEarlyOdds1, miniMegaHammerEarlyOdds2, miniMegaHammerEarlyOdds34, miniMegaHammerMidOdds1, miniMegaHammerMidOdds2, miniMegaHammerMidOdds34, miniMegaHammerLateOdds1, miniMegaHammerLateOdds2, miniMegaHammerLateOdds34, warpPipeEarlyOdds1, warpPipeEarlyOdds2, warpPipeEarlyOdds34, warpPipeMidOdds1, warpPipeMidOdds2, warpPipeMidOdds34, warpPipeLateOdds1, warpPipeLateOdds2, warpPipeLateOdds34, swapCardEarlyOdds1, swapCardEarlyOdds2, swapCardEarlyOdds34, swapCardMidOdds1, swapCardMidOdds2, swapCardMidOdds34, swapCardLateOdds1, swapCardLateOdds2, swapCardLateOdds34, sparkyStickerEarlyOdds1, sparkyStickerEarlyOdds2, sparkyStickerEarlyOdds34, sparkyStickerMidOdds1, sparkyStickerMidOdds2, sparkyStickerMidOdds34, sparkyStickerLateOdds1, sparkyStickerLateOdds2, sparkyStickerLateOdds34, gaddlightEarlyOdds1, gaddlightEarlyOdds2, gaddlightEarlyOdds34, gaddlightMidOdds1, gaddlightMidOdds2, gaddlightMidOdds34, gaddlightLateOdds1, gaddlightLateOdds2, gaddlightLateOdds34, chompCallEarlyOdds1, chompCallEarlyOdds2, chompCallEarlyOdds34, chompCallMidOdds1, chompCallMidOdds2, chompCallMidOdds34, chompCallLateOdds1, chompCallLateOdds2, chompCallLateOdds34, bowserSuitEarlyOdds1, bowserSuitEarlyOdds2, bowserSuitEarlyOdds34, bowserSuitMidOdds1, bowserSuitMidOdds2, bowserSuitMidOdds34, bowserSuitLateOdds1, bowserSuitLateOdds2, bowserSuitLateOdds34, crystalBallEarlyOdds1, crystalBallEarlyOdds2, crystalBallEarlyOdds34, crystalBallMidOdds1, crystalBallMidOdds2, crystalBallMidOdds34, crystalBallLateOdds1, crystalBallLateOdds2, crystalBallLateOdds34, magicLampEarlyOdds1, magicLampEarlyOdds2, magicLampEarlyOdds34, magicLampMidOdds1, magicLampMidOdds2, magicLampMidOdds34, magicLampLateOdds1, magicLampLateOdds2, magicLampLateOdds34, itemBagEarlyOdds1, itemBagEarlyOdds2, itemBagEarlyOdds34, itemBagMidOdds1, itemBagMidOdds2, itemBagMidOdds34, itemBagLateOdds1, itemBagLateOdds2, itemBagLateOdds34, mushroomEarlyOdds1, mushroomEarlyOdds2, mushroomEarlyOdds34, mushroomMidOdds1, mushroomMidOdds2, mushroomMidOdds34, mushroomLateOdds1, mushroomLateOdds2, mushroomLateOdds34, goldenMushroomEarlyOdds1, goldenMushroomEarlyOdds2, goldenMushroomEarlyOdds34, goldenMushroomMidOdds1, goldenMushroomMidOdds2, goldenMushroomMidOdds34, goldenMushroomLateOdds1, goldenMushroomLateOdds2, goldenMushroomLateOdds34, reverseMushroomEarlyOdds1, reverseMushroomEarlyOdds2, reverseMushroomEarlyOdds34, reverseMushroomMidOdds1, reverseMushroomMidOdds2, reverseMushroomMidOdds34, reverseMushroomLateOdds1, reverseMushroomLateOdds2, reverseMushroomLateOdds34, poisonMushroomEarlyOdds1, poisonMushroomEarlyOdds2, poisonMushroomEarlyOdds34, poisonMushroomMidOdds1, poisonMushroomMidOdds2, poisonMushroomMidOdds34, poisonMushroomLateOdds1, poisonMushroomLateOdds2, poisonMushroomLateOdds34, triplePoisonMushroomEarlyOdds1, triplePoisonMushroomEarlyOdds2, triplePoisonMushroomEarlyOdds34, triplePoisonMushroomMidOdds1, triplePoisonMushroomMidOdds2, triplePoisonMushroomMidOdds34, triplePoisonMushroomLateOdds1, triplePoisonMushroomLateOdds2, triplePoisonMushroomLateOdds34, celluarShopperEarlyOdds1, celluarShopperEarlyOdds2, celluarShopperEarlyOdds34, celluarShopperMidOdds1, celluarShopperMidOdds2, celluarShopperMidOdds34, celluarShopperLateOdds1, celluarShopperLateOdds2, celluarShopperLateOdds34, skeletonKeyEarlyOdds1, skeletonKeyEarlyOdds2, skeletonKeyEarlyOdds34, skeletonKeyMidOdds1, skeletonKeyMidOdds2, skeletonKeyMidOdds34, skeletonKeyLateOdds1, skeletonKeyLateOdds2, skeletonKeyLateOdds34, plunderChestEarlyOdds1, plunderChestEarlyOdds2, plunderChestEarlyOdds34, plunderChestMidOdds1, plunderChestMidOdds2, plunderChestMidOdds34, plunderChestLateOdds1, plunderChestLateOdds2, plunderChestLateOdds34, gaddbrushEarlyOdds1, gaddbrushEarlyOdds2, gaddbrushEarlyOdds34, gaddbrushMidOdds1, gaddbrushMidOdds2, gaddbrushMidOdds34, gaddbrushLateOdds1, gaddbrushLateOdds2, gaddbrushLateOdds34, warpBlockEarlyOdds1, warpBlockEarlyOdds2, warpBlockEarlyOdds34, warpBlockMidOdds1, warpBlockMidOdds2, warpBlockMidOdds34, warpBlockLateOdds1, warpBlockLateOdds2, warpBlockLateOdds34, flyGuyEarlyOdds1, flyGuyEarlyOdds2, flyGuyEarlyOdds34, flyGuyMidOdds1, flyGuyMidOdds2, flyGuyMidOdds34, flyGuyLateOdds1, flyGuyLateOdds2, flyGuyLateOdds34, plusBlockEarlyOdds1, plusBlockEarlyOdds2, plusBlockEarlyOdds34, plusBlockMidOdds1, plusBlockMidOdds2, plusBlockMidOdds34, plusBlockLateOdds1, plusBlockLateOdds2, plusBlockLateOdds34, minusBlockEarlyOdds1, minusBlockEarlyOdds2, minusBlockEarlyOdds34, minusBlockMidOdds1, minusBlockMidOdds2, minusBlockMidOdds34, minusBlockLateOdds1, minusBlockLateOdds2, minusBlockLateOdds34, speedBlockEarlyOdds1, speedBlockEarlyOdds2, speedBlockEarlyOdds34, speedBlockMidOdds1, speedBlockMidOdds2, speedBlockMidOdds34, speedBlockLateOdds1, speedBlockLateOdds2, speedBlockLateOdds34, slowBlockEarlyOdds1, slowBlockEarlyOdds2, slowBlockEarlyOdds34, slowBlockMidOdds1, slowBlockMidOdds2, slowBlockMidOdds34, slowBlockLateOdds1, slowBlockLateOdds2, slowBlockLateOdds34, bowserPhoneEarlyOdds1, bowserPhoneEarlyOdds2, bowserPhoneEarlyOdds34, bowserPhoneMidOdds1, bowserPhoneMidOdds2, bowserPhoneMidOdds34, bowserPhoneLateOdds1, bowserPhoneLateOdds2, bowserPhoneLateOdds34, doubleDipEarlyOdds1, doubleDipEarlyOdds2, doubleDipEarlyOdds34, doubleDipMidOdds1, doubleDipMidOdds2, doubleDipMidOdds34, doubleDipLateOdds1, doubleDipLateOdds2, doubleDipLateOdds34, hiddenBlockCardEarlyOdds1, hiddenBlockCardEarlyOdds2, hiddenBlockCardEarlyOdds34, hiddenBlockCardMidOdds1, hiddenBlockCardMidOdds2, hiddenBlockCardMidOdds34, hiddenBlockCardLateOdds1, hiddenBlockCardLateOdds2, hiddenBlockCardLateOdds34, barterBoxEarlyOdds1, barterBoxEarlyOdds2, barterBoxEarlyOdds34, barterBoxMidOdds1, barterBoxMidOdds2, barterBoxMidOdds34, barterBoxLateOdds1, barterBoxLateOdds2, barterBoxLateOdds34, superWarpPipeEarlyOdds1, superWarpPipeEarlyOdds2, superWarpPipeEarlyOdds34, superWarpPipeMidOdds1, superWarpPipeMidOdds2, superWarpPipeMidOdds34, superWarpPipeLateOdds1, superWarpPipeLateOdds2, superWarpPipeLateOdds34, chanceTimeCharmEarlyOdds1, chanceTimeCharmEarlyOdds2, chanceTimeCharmEarlyOdds34, chanceTimeCharmMidOdds1, chanceTimeCharmMidOdds2, chanceTimeCharmMidOdds34, chanceTimeCharmLateOdds1, chanceTimeCharmLateOdds2, chanceTimeCharmLateOdds34, wackyWatchEarlyOdds1, wackyWatchEarlyOdds2, wackyWatchEarlyOdds34, wackyWatchMidOdds1, wackyWatchMidOdds2, wackyWatchMidOdds34, wackyWatchLateOdds1, wackyWatchLateOdds2, wackyWatchLateOdds34)
    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)

    print("Generated code copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)

def itemsEvent_mp4ShopOdds(miniMushroomEarlyOdds1 = "0", miniMushroomEarlyOdds2 = "0", miniMushroomEarlyOdds34 = "0", miniMushroomMidOdds1 = "0", miniMushroomMidOdds2 = "0", miniMushroomMidOdds34 = "0", miniMushroomLateOdds1 = "0", miniMushroomLateOdds2 = "0", miniMushroomLateOdds34 = "0", megaMushroomEarlyOdds1 = "0", megaMushroomEarlyOdds2 = "0", megaMushroomEarlyOdds34 = "0", megaMushroomMidOdds1 = "0", megaMushroomMidOdds2 = "0", megaMushroomMidOdds34 = "0", megaMushroomLateOdds1 = "0", megaMushroomLateOdds2 = "0", megaMushroomLateOdds34 = "0", superMiniMushroomEarlyOdds1 = "0", superMiniMushroomEarlyOdds2 = "0", superMiniMushroomEarlyOdds34 = "0", superMiniMushroomMidOdds1 = "0", superMiniMushroomMidOdds2 = "0", superMiniMushroomMidOdds34 = "0", superMiniMushroomLateOdds1 = "0", superMiniMushroomLateOdds2 = "0", superMiniMushroomLateOdds34 = "0", superMegaMushroomEarlyOdds1 = "0", superMegaMushroomEarlyOdds2 = "0", superMegaMushroomEarlyOdds34 = "0", superMegaMushroomMidOdds1 = "0", superMegaMushroomMidOdds2 = "0", superMegaMushroomMidOdds34 = "0", superMegaMushroomLateOdds1 = "0", superMegaMushroomLateOdds2 = "0", superMegaMushroomLateOdds34 = "0", miniMegaHammerEarlyOdds1 = "0", miniMegaHammerEarlyOdds2 = "0", miniMegaHammerEarlyOdds34 = "0", miniMegaHammerMidOdds1 = "0", miniMegaHammerMidOdds2 = "0", miniMegaHammerMidOdds34 = "0", miniMegaHammerLateOdds1 = "0", miniMegaHammerLateOdds2 = "0", miniMegaHammerLateOdds34 = "0", warpPipeEarlyOdds1 = "0", warpPipeEarlyOdds2 = "0", warpPipeEarlyOdds34 = "0", warpPipeMidOdds1 = "0", warpPipeMidOdds2 = "0", warpPipeMidOdds34 = "0", warpPipeLateOdds1 = "0", warpPipeLateOdds2 = "0", warpPipeLateOdds34 = "0", swapCardEarlyOdds1 = "0", swapCardEarlyOdds2 = "0", swapCardEarlyOdds34 = "0", swapCardMidOdds1 = "0", swapCardMidOdds2 = "0", swapCardMidOdds34 = "0", swapCardLateOdds1 = "0", swapCardLateOdds2 = "0", swapCardLateOdds34 = "0", sparkyStickerEarlyOdds1 = "0", sparkyStickerEarlyOdds2 = "0", sparkyStickerEarlyOdds34 = "0", sparkyStickerMidOdds1 = "0", sparkyStickerMidOdds2 = "0", sparkyStickerMidOdds34 = "0", sparkyStickerLateOdds1 = "0", sparkyStickerLateOdds2 = "0", sparkyStickerLateOdds34 = "0", gaddlightEarlyOdds1 = "0", gaddlightEarlyOdds2 = "0", gaddlightEarlyOdds34 = "0", gaddlightMidOdds1 = "0", gaddlightMidOdds2 = "0", gaddlightMidOdds34 = "0", gaddlightLateOdds1 = "0", gaddlightLateOdds2 = "0", gaddlightLateOdds34 = "0", chompCallEarlyOdds1 = "0", chompCallEarlyOdds2 = "0", chompCallEarlyOdds34 = "0", chompCallMidOdds1 = "0", chompCallMidOdds2 = "0", chompCallMidOdds34 = "0", chompCallLateOdds1 = "0", chompCallLateOdds2 = "0", chompCallLateOdds34 = "0", bowserSuitEarlyOdds1 = "0", bowserSuitEarlyOdds2 = "0", bowserSuitEarlyOdds34 = "0", bowserSuitMidOdds1 = "0", bowserSuitMidOdds2 = "0", bowserSuitMidOdds34 = "0", bowserSuitLateOdds1 = "0", bowserSuitLateOdds2 = "0", bowserSuitLateOdds34 = "0", crystalBallEarlyOdds1 = "0", crystalBallEarlyOdds2 = "0", crystalBallEarlyOdds34 = "0", crystalBallMidOdds1 = "0", crystalBallMidOdds2 = "0", crystalBallMidOdds34 = "0", crystalBallLateOdds1 = "0", crystalBallLateOdds2 = "0", crystalBallLateOdds34 = "0", magicLampEarlyOdds1 = "0", magicLampEarlyOdds2 = "0", magicLampEarlyOdds34 = "0", magicLampMidOdds1 = "0", magicLampMidOdds2 = "0", magicLampMidOdds34 = "0", magicLampLateOdds1 = "0", magicLampLateOdds2 = "0", magicLampLateOdds34 = "0", itemBagEarlyOdds1 = "0", itemBagEarlyOdds2 = "0", itemBagEarlyOdds34 = "0", itemBagMidOdds1 = "0", itemBagMidOdds2 = "0", itemBagMidOdds34 = "0", itemBagLateOdds1 = "0", itemBagLateOdds2 = "0", itemBagLateOdds34 = "0"):
    # Mini Mushroom
    miniMushroomEarlyOdds1 = get_capsule_value(miniMushroomEarlyOdds1)
    miniMushroomEarlyOdds2 = get_capsule_value(miniMushroomEarlyOdds2)
    miniMushroomEarlyOdds34 = get_capsule_value(miniMushroomEarlyOdds34)
    miniMushroomMidOdds1 = get_capsule_value(miniMushroomMidOdds1)
    miniMushroomMidOdds2 = get_capsule_value(miniMushroomMidOdds2)
    miniMushroomMidOdds34 = get_capsule_value(miniMushroomMidOdds34)
    miniMushroomLateOdds1 = get_capsule_value(miniMushroomLateOdds1)
    miniMushroomLateOdds2 = get_capsule_value(miniMushroomLateOdds2)
    miniMushroomLateOdds34 = get_capsule_value(miniMushroomLateOdds34)
    
    # Mega Mushroom
    megaMushroomEarlyOdds1 = get_capsule_value(megaMushroomEarlyOdds1)
    megaMushroomEarlyOdds2 = get_capsule_value(megaMushroomEarlyOdds2)
    megaMushroomEarlyOdds34 = get_capsule_value(megaMushroomEarlyOdds34)
    megaMushroomMidOdds1 = get_capsule_value(megaMushroomMidOdds1)
    megaMushroomMidOdds2 = get_capsule_value(megaMushroomMidOdds2)
    megaMushroomMidOdds34 = get_capsule_value(megaMushroomMidOdds34)
    megaMushroomLateOdds1 = get_capsule_value(megaMushroomLateOdds1)
    megaMushroomLateOdds2 = get_capsule_value(megaMushroomLateOdds2)
    megaMushroomLateOdds34 = get_capsule_value(megaMushroomLateOdds34)

    # Super Mini Mushroom
    superMiniMushroomEarlyOdds1 = get_capsule_value(superMiniMushroomEarlyOdds1)
    superMiniMushroomEarlyOdds2 = get_capsule_value(superMiniMushroomEarlyOdds2)
    superMiniMushroomEarlyOdds34 = get_capsule_value(superMiniMushroomEarlyOdds34)
    superMiniMushroomMidOdds1 = get_capsule_value(superMiniMushroomMidOdds1)
    superMiniMushroomMidOdds2 = get_capsule_value(superMiniMushroomMidOdds2)
    superMiniMushroomMidOdds34 = get_capsule_value(superMiniMushroomMidOdds34)
    superMiniMushroomLateOdds1 = get_capsule_value(superMiniMushroomLateOdds1)
    superMiniMushroomLateOdds2 = get_capsule_value(superMiniMushroomLateOdds2)
    superMiniMushroomLateOdds34 = get_capsule_value(superMiniMushroomLateOdds34)

    # Super Mega Mushroom
    superMegaMushroomEarlyOdds1 = get_capsule_value(superMegaMushroomEarlyOdds1)
    superMegaMushroomEarlyOdds2 = get_capsule_value(superMegaMushroomEarlyOdds2)
    superMegaMushroomEarlyOdds34 = get_capsule_value(superMegaMushroomEarlyOdds34)
    superMegaMushroomMidOdds1 = get_capsule_value(superMegaMushroomMidOdds1)
    superMegaMushroomMidOdds2 = get_capsule_value(superMegaMushroomMidOdds2)
    superMegaMushroomMidOdds34 = get_capsule_value(superMegaMushroomMidOdds34)
    superMegaMushroomLateOdds1 = get_capsule_value(superMegaMushroomLateOdds1)
    superMegaMushroomLateOdds2 = get_capsule_value(superMegaMushroomLateOdds2)
    superMegaMushroomLateOdds34 = get_capsule_value(superMegaMushroomLateOdds34)

    # Mini Mega Hammer
    miniMegaHammerEarlyOdds1 = get_capsule_value(miniMegaHammerEarlyOdds1)
    miniMegaHammerEarlyOdds2 = get_capsule_value(miniMegaHammerEarlyOdds2)
    miniMegaHammerEarlyOdds34 = get_capsule_value(miniMegaHammerEarlyOdds34)
    miniMegaHammerMidOdds1 = get_capsule_value(miniMegaHammerMidOdds1)
    miniMegaHammerMidOdds2 = get_capsule_value(miniMegaHammerMidOdds2)
    miniMegaHammerMidOdds34 = get_capsule_value(miniMegaHammerMidOdds34)
    miniMegaHammerLateOdds1 = get_capsule_value(miniMegaHammerLateOdds1)
    miniMegaHammerLateOdds2 = get_capsule_value(miniMegaHammerLateOdds2)
    miniMegaHammerLateOdds34 = get_capsule_value(miniMegaHammerLateOdds34)

    # Warp Pipe
    warpPipeEarlyOdds1 = get_capsule_value(warpPipeEarlyOdds1)
    warpPipeEarlyOdds2 = get_capsule_value(warpPipeEarlyOdds2)
    warpPipeEarlyOdds34 = get_capsule_value(warpPipeEarlyOdds34)
    warpPipeMidOdds1 = get_capsule_value(warpPipeMidOdds1)
    warpPipeMidOdds2 = get_capsule_value(warpPipeMidOdds2)
    warpPipeMidOdds34 = get_capsule_value(warpPipeMidOdds34)
    warpPipeLateOdds1 = get_capsule_value(warpPipeLateOdds1)
    warpPipeLateOdds2 = get_capsule_value(warpPipeLateOdds2)
    warpPipeLateOdds34 = get_capsule_value(warpPipeLateOdds34)

    # Swap Card
    swapCardEarlyOdds1 = get_capsule_value(swapCardEarlyOdds1)
    swapCardEarlyOdds2 = get_capsule_value(swapCardEarlyOdds2)
    swapCardEarlyOdds34 = get_capsule_value(swapCardEarlyOdds34)
    swapCardMidOdds1 = get_capsule_value(swapCardMidOdds1)
    swapCardMidOdds2 = get_capsule_value(swapCardMidOdds2)
    swapCardMidOdds34 = get_capsule_value(swapCardMidOdds34)
    swapCardLateOdds1 = get_capsule_value(swapCardLateOdds1)
    swapCardLateOdds2 = get_capsule_value(swapCardLateOdds2)
    swapCardLateOdds34 = get_capsule_value(swapCardLateOdds34)

    # Sparky Sticker
    sparkyStickerEarlyOdds1 = get_capsule_value(sparkyStickerEarlyOdds1)
    sparkyStickerEarlyOdds2 = get_capsule_value(sparkyStickerEarlyOdds2)
    sparkyStickerEarlyOdds34 = get_capsule_value(sparkyStickerEarlyOdds34)
    sparkyStickerMidOdds1 = get_capsule_value(sparkyStickerMidOdds1)
    sparkyStickerMidOdds2 = get_capsule_value(sparkyStickerMidOdds2)
    sparkyStickerMidOdds34 = get_capsule_value(sparkyStickerMidOdds34)
    sparkyStickerLateOdds1 = get_capsule_value(sparkyStickerLateOdds1)
    sparkyStickerLateOdds2 = get_capsule_value(sparkyStickerLateOdds2)
    sparkyStickerLateOdds34 = get_capsule_value(sparkyStickerLateOdds34)

    # Gaddlight
    gaddlightEarlyOdds1 = get_capsule_value(gaddlightEarlyOdds1)
    gaddlightEarlyOdds2 = get_capsule_value(gaddlightEarlyOdds2)
    gaddlightEarlyOdds34 = get_capsule_value(gaddlightEarlyOdds34)
    gaddlightMidOdds1 = get_capsule_value(gaddlightMidOdds1)
    gaddlightMidOdds2 = get_capsule_value(gaddlightMidOdds2)
    gaddlightMidOdds34 = get_capsule_value(gaddlightMidOdds34)
    gaddlightLateOdds1 = get_capsule_value(gaddlightLateOdds1)
    gaddlightLateOdds2 = get_capsule_value(gaddlightLateOdds2)
    gaddlightLateOdds34 = get_capsule_value(gaddlightLateOdds34)

    # Chomp Call
    chompCallEarlyOdds1 = get_capsule_value(chompCallEarlyOdds1)
    chompCallEarlyOdds2 = get_capsule_value(chompCallEarlyOdds2)
    chompCallEarlyOdds34 = get_capsule_value(chompCallEarlyOdds34)
    chompCallMidOdds1 = get_capsule_value(chompCallMidOdds1)
    chompCallMidOdds2 = get_capsule_value(chompCallMidOdds2)
    chompCallMidOdds34 = get_capsule_value(chompCallMidOdds34)
    chompCallLateOdds1 = get_capsule_value(chompCallLateOdds1)
    chompCallLateOdds2 = get_capsule_value(chompCallLateOdds2)
    chompCallLateOdds34 = get_capsule_value(chompCallLateOdds34)

    # Bowser Suit
    bowserSuitEarlyOdds1 = get_capsule_value(bowserSuitEarlyOdds1)
    bowserSuitEarlyOdds2 = get_capsule_value(bowserSuitEarlyOdds2)
    bowserSuitEarlyOdds34 = get_capsule_value(bowserSuitEarlyOdds34)
    bowserSuitMidOdds1 = get_capsule_value(bowserSuitMidOdds1)
    bowserSuitMidOdds2 = get_capsule_value(bowserSuitMidOdds2)
    bowserSuitMidOdds34 = get_capsule_value(bowserSuitMidOdds34)
    bowserSuitLateOdds1 = get_capsule_value(bowserSuitLateOdds1)
    bowserSuitLateOdds2 = get_capsule_value(bowserSuitLateOdds2)
    bowserSuitLateOdds34 = get_capsule_value(bowserSuitLateOdds34)

    # Crystal Ball
    crystalBallEarlyOdds1 = get_capsule_value(crystalBallEarlyOdds1)
    crystalBallEarlyOdds2 = get_capsule_value(crystalBallEarlyOdds2)
    crystalBallEarlyOdds34 = get_capsule_value(crystalBallEarlyOdds34)
    crystalBallMidOdds1 = get_capsule_value(crystalBallMidOdds1)
    crystalBallMidOdds2 = get_capsule_value(crystalBallMidOdds2)
    crystalBallMidOdds34 = get_capsule_value(crystalBallMidOdds34)
    crystalBallLateOdds1 = get_capsule_value(crystalBallLateOdds1)
    crystalBallLateOdds2 = get_capsule_value(crystalBallLateOdds2)
    crystalBallLateOdds34 = get_capsule_value(crystalBallLateOdds34)

    # Magic Lamp
    magicLampEarlyOdds1 = get_capsule_value(magicLampEarlyOdds1)
    magicLampEarlyOdds2 = get_capsule_value(magicLampEarlyOdds2)
    magicLampEarlyOdds34 = get_capsule_value(magicLampEarlyOdds34)
    magicLampMidOdds1 = get_capsule_value(magicLampMidOdds1)
    magicLampMidOdds2 = get_capsule_value(magicLampMidOdds2)
    magicLampMidOdds34 = get_capsule_value(magicLampMidOdds34)
    magicLampLateOdds1 = get_capsule_value(magicLampLateOdds1)
    magicLampLateOdds2 = get_capsule_value(magicLampLateOdds2)
    magicLampLateOdds34 = get_capsule_value(magicLampLateOdds34)

    # Item Bag
    itemBagEarlyOdds1 = get_capsule_value(itemBagEarlyOdds1)
    itemBagEarlyOdds2 = get_capsule_value(itemBagEarlyOdds2)
    itemBagEarlyOdds34 = get_capsule_value(itemBagEarlyOdds34)
    itemBagMidOdds1 = get_capsule_value(itemBagMidOdds1)
    itemBagMidOdds2 = get_capsule_value(itemBagMidOdds2)
    itemBagMidOdds34 = get_capsule_value(itemBagMidOdds34)
    itemBagLateOdds1 = get_capsule_value(itemBagLateOdds1)
    itemBagLateOdds2 = get_capsule_value(itemBagLateOdds2)
    itemBagLateOdds34 = get_capsule_value(itemBagLateOdds34)

    earlyOdds1 = [
        miniMushroomEarlyOdds1,
        megaMushroomEarlyOdds1,
        superMiniMushroomEarlyOdds1,
        superMegaMushroomEarlyOdds1,
        miniMegaHammerEarlyOdds1,
        warpPipeEarlyOdds1,
        swapCardEarlyOdds1,
        sparkyStickerEarlyOdds1,
        gaddlightEarlyOdds1,
        chompCallEarlyOdds1,
        bowserSuitEarlyOdds1,
        crystalBallEarlyOdds1,
        magicLampEarlyOdds1,
        itemBagEarlyOdds1,
    ]
    
    earlyOdds2 = [
        miniMushroomEarlyOdds2,
        megaMushroomEarlyOdds2,
        superMiniMushroomEarlyOdds2,
        superMegaMushroomEarlyOdds2,
        miniMegaHammerEarlyOdds2,
        warpPipeEarlyOdds2,
        swapCardEarlyOdds2,
        sparkyStickerEarlyOdds2,
        gaddlightEarlyOdds2,
        chompCallEarlyOdds2,
        bowserSuitEarlyOdds2,
        crystalBallEarlyOdds2,
        magicLampEarlyOdds2,
        itemBagEarlyOdds2,    
    ]

    earlyOdds34 = [
        miniMushroomEarlyOdds34,
        megaMushroomEarlyOdds34,
        superMiniMushroomEarlyOdds34,
        superMegaMushroomEarlyOdds34,
        miniMegaHammerEarlyOdds34,
        warpPipeEarlyOdds34,
        swapCardEarlyOdds34,
        sparkyStickerEarlyOdds34,
        gaddlightEarlyOdds34,
        chompCallEarlyOdds34,
        bowserSuitEarlyOdds34,
        crystalBallEarlyOdds34,
        magicLampEarlyOdds34,
        itemBagEarlyOdds34,
    ]
    
    midOdds1 = [
        miniMushroomMidOdds1,
        megaMushroomMidOdds1,
        superMiniMushroomMidOdds1,
        superMegaMushroomMidOdds1,
        miniMegaHammerMidOdds1,
        warpPipeMidOdds1,
        swapCardMidOdds1,
        sparkyStickerMidOdds1,
        gaddlightMidOdds1,
        chompCallMidOdds1,
        bowserSuitMidOdds1,
        crystalBallMidOdds1,
        magicLampMidOdds1,
        itemBagMidOdds1,
    ]

    midOdds2 = [
        miniMushroomMidOdds2,
        megaMushroomMidOdds2,
        superMiniMushroomMidOdds2,
        superMegaMushroomMidOdds2,
        miniMegaHammerMidOdds2,
        warpPipeMidOdds2,
        swapCardMidOdds2,
        sparkyStickerMidOdds2,
        gaddlightMidOdds2,
        chompCallMidOdds2,
        bowserSuitMidOdds2,
        crystalBallMidOdds2,
        magicLampMidOdds2,
        itemBagMidOdds2,
    ]

    midOdds34 = [
        miniMushroomMidOdds34,
        megaMushroomMidOdds34,
        superMiniMushroomMidOdds34,
        superMegaMushroomMidOdds34,
        miniMegaHammerMidOdds34,
        warpPipeMidOdds34,
        swapCardMidOdds34,
        sparkyStickerMidOdds34,
        gaddlightMidOdds34,
        chompCallMidOdds34,
        bowserSuitMidOdds34,
        crystalBallMidOdds34,
        magicLampMidOdds34,
        itemBagMidOdds34,
    ]

    lateOdds1 = [
        miniMushroomLateOdds1,
        megaMushroomLateOdds1,
        superMiniMushroomLateOdds1,
        superMegaMushroomLateOdds1,
        miniMegaHammerLateOdds1,
        warpPipeLateOdds1,
        swapCardLateOdds1,
        sparkyStickerLateOdds1,
        gaddlightLateOdds1,
        chompCallLateOdds1,
        bowserSuitLateOdds1,
        crystalBallLateOdds1,
        magicLampLateOdds1,
        itemBagLateOdds1,
    ]

    lateOdds2 = [
        miniMushroomLateOdds2,
        megaMushroomLateOdds2,
        superMiniMushroomLateOdds2,
        superMegaMushroomLateOdds2,
        miniMegaHammerLateOdds2,
        warpPipeLateOdds2,
        swapCardLateOdds2,
        sparkyStickerLateOdds2,
        gaddlightLateOdds2,
        chompCallLateOdds2,
        bowserSuitLateOdds2,
        crystalBallLateOdds2,
        magicLampLateOdds2,
        itemBagLateOdds2,
    ]

    lateOdds34 = [
        miniMushroomLateOdds34,
        megaMushroomLateOdds34,
        superMiniMushroomLateOdds34,
        superMegaMushroomLateOdds34,
        miniMegaHammerLateOdds34,
        warpPipeLateOdds34,
        swapCardLateOdds34,
        sparkyStickerLateOdds34,
        gaddlightLateOdds34,
        chompCallLateOdds34,
        bowserSuitLateOdds34,
        crystalBallLateOdds34,
        magicLampLateOdds34,
        itemBagLateOdds34,
    ]

    earlyOdds1Weights = sum(int(weight) if weight else 0 for weight in earlyOdds1)
    earlyOdds2Weights = sum(int(weight) if weight else 0 for weight in earlyOdds2)
    earlyOdds34Weights = sum(int(weight) if weight else 0 for weight in earlyOdds34)
    midOdds1Weights = sum(int(weight) if weight else 0 for weight in midOdds1)
    midOdds2Weights = sum(int(weight) if weight else 0 for weight in midOdds2)
    midOdds34Weights = sum(int(weight) if weight else 0 for weight in midOdds34)
    lateOdds1Weights = sum(int(weight) if weight else 0 for weight in lateOdds1)
    lateOdds2Weights = sum(int(weight) if weight else 0 for weight in lateOdds2)
    lateOdds34Weights = sum(int(weight) if weight else 0 for weight in lateOdds34)

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

    # Mini Mushroom
    miniMushroomEarlyOdds1 = calculateWeight(miniMushroomEarlyOdds1, earlyOdds1Weights)
    miniMushroomEarlyOdds2 = calculateWeight(miniMushroomEarlyOdds2, earlyOdds2Weights)
    miniMushroomEarlyOdds34 = calculateWeight(miniMushroomEarlyOdds34, earlyOdds34Weights)
    miniMushroomMidOdds1 = calculateWeight(miniMushroomMidOdds1, midOdds1Weights)
    miniMushroomMidOdds2 = calculateWeight(miniMushroomMidOdds2, midOdds2Weights)
    miniMushroomMidOdds34 = calculateWeight(miniMushroomMidOdds34, midOdds34Weights)
    miniMushroomLateOdds1 = calculateWeight(miniMushroomLateOdds1, lateOdds1Weights)
    miniMushroomLateOdds2 = calculateWeight(miniMushroomLateOdds2, lateOdds2Weights)
    miniMushroomLateOdds34 = calculateWeight(miniMushroomLateOdds34, lateOdds34Weights)

    # Mega Mushroom
    megaMushroomEarlyOdds1 = calculateWeight(megaMushroomEarlyOdds1, earlyOdds1Weights)
    megaMushroomEarlyOdds2 = calculateWeight(megaMushroomEarlyOdds2, earlyOdds2Weights)
    megaMushroomEarlyOdds34 = calculateWeight(megaMushroomEarlyOdds34, earlyOdds34Weights)
    megaMushroomMidOdds1 = calculateWeight(megaMushroomMidOdds1, midOdds1Weights)
    megaMushroomMidOdds2 = calculateWeight(megaMushroomMidOdds2, midOdds2Weights)
    megaMushroomMidOdds34 = calculateWeight(megaMushroomMidOdds34, midOdds34Weights)
    megaMushroomLateOdds1 = calculateWeight(megaMushroomLateOdds1, lateOdds1Weights)
    megaMushroomLateOdds2 = calculateWeight(megaMushroomLateOdds2, lateOdds2Weights)
    megaMushroomLateOdds34 = calculateWeight(megaMushroomLateOdds34, lateOdds34Weights)

    # Super Mini Mushroom
    superMiniMushroomEarlyOdds1 = calculateWeight(superMiniMushroomEarlyOdds1, earlyOdds1Weights)
    superMiniMushroomEarlyOdds2 = calculateWeight(superMiniMushroomEarlyOdds2, earlyOdds2Weights)
    superMiniMushroomEarlyOdds34 = calculateWeight(superMiniMushroomEarlyOdds34, earlyOdds34Weights)
    superMiniMushroomMidOdds1 = calculateWeight(superMiniMushroomMidOdds1, midOdds1Weights)
    superMiniMushroomMidOdds2 = calculateWeight(superMiniMushroomMidOdds2, midOdds2Weights)
    superMiniMushroomMidOdds34 = calculateWeight(superMiniMushroomMidOdds34, midOdds34Weights)
    superMiniMushroomLateOdds1 = calculateWeight(superMiniMushroomLateOdds1, lateOdds1Weights)
    superMiniMushroomLateOdds2 = calculateWeight(superMiniMushroomLateOdds2, lateOdds2Weights)
    superMiniMushroomLateOdds34 = calculateWeight(superMiniMushroomLateOdds34, lateOdds34Weights)

    # Super Mega Mushroom
    superMegaMushroomEarlyOdds1 = calculateWeight(superMegaMushroomEarlyOdds1, earlyOdds1Weights)
    superMegaMushroomEarlyOdds2 = calculateWeight(superMegaMushroomEarlyOdds2, earlyOdds2Weights)
    superMegaMushroomEarlyOdds34 = calculateWeight(superMegaMushroomEarlyOdds34, earlyOdds34Weights)
    superMegaMushroomMidOdds1 = calculateWeight(superMegaMushroomMidOdds1, midOdds1Weights)
    superMegaMushroomMidOdds2 = calculateWeight(superMegaMushroomMidOdds2, midOdds2Weights)
    superMegaMushroomMidOdds34 = calculateWeight(superMegaMushroomMidOdds34, midOdds34Weights)
    superMegaMushroomLateOdds1 = calculateWeight(superMegaMushroomLateOdds1, lateOdds1Weights)
    superMegaMushroomLateOdds2 = calculateWeight(superMegaMushroomLateOdds2, lateOdds2Weights)
    superMegaMushroomLateOdds34 = calculateWeight(superMegaMushroomLateOdds34, lateOdds34Weights)

    # Mini Mega Hammer
    miniMegaHammerEarlyOdds1 = calculateWeight(miniMegaHammerEarlyOdds1, earlyOdds1Weights)
    miniMegaHammerEarlyOdds2 = calculateWeight(miniMegaHammerEarlyOdds2, earlyOdds2Weights)
    miniMegaHammerEarlyOdds34 = calculateWeight(miniMegaHammerEarlyOdds34, earlyOdds34Weights)
    miniMegaHammerMidOdds1 = calculateWeight(miniMegaHammerMidOdds1, midOdds1Weights)
    miniMegaHammerMidOdds2 = calculateWeight(miniMegaHammerMidOdds2, midOdds2Weights)
    miniMegaHammerMidOdds34 = calculateWeight(miniMegaHammerMidOdds34, midOdds34Weights)
    miniMegaHammerLateOdds1 = calculateWeight(miniMegaHammerLateOdds1, lateOdds1Weights)
    miniMegaHammerLateOdds2 = calculateWeight(miniMegaHammerLateOdds2, lateOdds2Weights)
    miniMegaHammerLateOdds34 = calculateWeight(miniMegaHammerLateOdds34, lateOdds34Weights)

    # Warp Pipe
    warpPipeEarlyOdds1 = calculateWeight(warpPipeEarlyOdds1, earlyOdds1Weights)
    warpPipeEarlyOdds2 = calculateWeight(warpPipeEarlyOdds2, earlyOdds2Weights)
    warpPipeEarlyOdds34 = calculateWeight(warpPipeEarlyOdds34, earlyOdds34Weights)
    warpPipeMidOdds1 = calculateWeight(warpPipeMidOdds1, midOdds1Weights)
    warpPipeMidOdds2 = calculateWeight(warpPipeMidOdds2, midOdds2Weights)
    warpPipeMidOdds34 = calculateWeight(warpPipeMidOdds34, midOdds34Weights)
    warpPipeLateOdds1 = calculateWeight(warpPipeLateOdds1, lateOdds1Weights)
    warpPipeLateOdds2 = calculateWeight(warpPipeLateOdds2, lateOdds2Weights)
    warpPipeLateOdds34 = calculateWeight(warpPipeLateOdds34, lateOdds34Weights)

    # Swap Card
    swapCardEarlyOdds1 = calculateWeight(swapCardEarlyOdds1, earlyOdds1Weights)
    swapCardEarlyOdds2 = calculateWeight(swapCardEarlyOdds2, earlyOdds2Weights)
    swapCardEarlyOdds34 = calculateWeight(swapCardEarlyOdds34, earlyOdds34Weights)
    swapCardMidOdds1 = calculateWeight(swapCardMidOdds1, midOdds1Weights)
    swapCardMidOdds2 = calculateWeight(swapCardMidOdds2, midOdds2Weights)
    swapCardMidOdds34 = calculateWeight(swapCardMidOdds34, midOdds34Weights)
    swapCardLateOdds1 = calculateWeight(swapCardLateOdds1, lateOdds1Weights)
    swapCardLateOdds2 = calculateWeight(swapCardLateOdds2, lateOdds2Weights)
    swapCardLateOdds34 = calculateWeight(swapCardLateOdds34, lateOdds34Weights)

    # Sparky Sticker
    sparkyStickerEarlyOdds1 = calculateWeight(sparkyStickerEarlyOdds1, earlyOdds1Weights)
    sparkyStickerEarlyOdds2 = calculateWeight(sparkyStickerEarlyOdds2, earlyOdds2Weights)
    sparkyStickerEarlyOdds34 = calculateWeight(sparkyStickerEarlyOdds34, earlyOdds34Weights)
    sparkyStickerMidOdds1 = calculateWeight(sparkyStickerMidOdds1, midOdds1Weights)
    sparkyStickerMidOdds2 = calculateWeight(sparkyStickerMidOdds2, midOdds2Weights)
    sparkyStickerMidOdds34 = calculateWeight(sparkyStickerMidOdds34, midOdds34Weights)
    sparkyStickerLateOdds1 = calculateWeight(sparkyStickerLateOdds1, lateOdds1Weights)
    sparkyStickerLateOdds2 = calculateWeight(sparkyStickerLateOdds2, lateOdds2Weights)
    sparkyStickerLateOdds34 = calculateWeight(sparkyStickerLateOdds34, lateOdds34Weights)

    # Gaddlight
    gaddlightEarlyOdds1 = calculateWeight(gaddlightEarlyOdds1, earlyOdds1Weights)
    gaddlightEarlyOdds2 = calculateWeight(gaddlightEarlyOdds2, earlyOdds2Weights)
    gaddlightEarlyOdds34 = calculateWeight(gaddlightEarlyOdds34, earlyOdds34Weights)
    gaddlightMidOdds1 = calculateWeight(gaddlightMidOdds1, midOdds1Weights)
    gaddlightMidOdds2 = calculateWeight(gaddlightMidOdds2, midOdds2Weights)
    gaddlightMidOdds34 = calculateWeight(gaddlightMidOdds34, midOdds34Weights)
    gaddlightLateOdds1 = calculateWeight(gaddlightLateOdds1, lateOdds1Weights)
    gaddlightLateOdds2 = calculateWeight(gaddlightLateOdds2, lateOdds2Weights)
    gaddlightLateOdds34 = calculateWeight(gaddlightLateOdds34, lateOdds34Weights)

    # Chomp Call
    chompCallEarlyOdds1 = calculateWeight(chompCallEarlyOdds1, earlyOdds1Weights)
    chompCallEarlyOdds2 = calculateWeight(chompCallEarlyOdds2, earlyOdds2Weights)
    chompCallEarlyOdds34 = calculateWeight(chompCallEarlyOdds34, earlyOdds34Weights)
    chompCallMidOdds1 = calculateWeight(chompCallMidOdds1, midOdds1Weights)
    chompCallMidOdds2 = calculateWeight(chompCallMidOdds2, midOdds2Weights)
    chompCallMidOdds34 = calculateWeight(chompCallMidOdds34, midOdds34Weights)
    chompCallLateOdds1 = calculateWeight(chompCallLateOdds1, lateOdds1Weights)
    chompCallLateOdds2 = calculateWeight(chompCallLateOdds2, lateOdds2Weights)
    chompCallLateOdds34 = calculateWeight(chompCallLateOdds34, lateOdds34Weights)

    # Bowser Suit
    bowserSuitEarlyOdds1 = calculateWeight(bowserSuitEarlyOdds1, earlyOdds1Weights)
    bowserSuitEarlyOdds2 = calculateWeight(bowserSuitEarlyOdds2, earlyOdds2Weights)
    bowserSuitEarlyOdds34 = calculateWeight(bowserSuitEarlyOdds34, earlyOdds34Weights)
    bowserSuitMidOdds1 = calculateWeight(bowserSuitMidOdds1, midOdds1Weights)
    bowserSuitMidOdds2 = calculateWeight(bowserSuitMidOdds2, midOdds2Weights)
    bowserSuitMidOdds34 = calculateWeight(bowserSuitMidOdds34, midOdds34Weights)
    bowserSuitLateOdds1 = calculateWeight(bowserSuitLateOdds1, lateOdds1Weights)
    bowserSuitLateOdds2 = calculateWeight(bowserSuitLateOdds2, lateOdds2Weights)
    bowserSuitLateOdds34 = calculateWeight(bowserSuitLateOdds34, lateOdds34Weights)

    # Crystal Ball
    crystalBallEarlyOdds1 = calculateWeight(crystalBallEarlyOdds1, earlyOdds1Weights)
    crystalBallEarlyOdds2 = calculateWeight(crystalBallEarlyOdds2, earlyOdds2Weights)
    crystalBallEarlyOdds34 = calculateWeight(crystalBallEarlyOdds34, earlyOdds34Weights)
    crystalBallMidOdds1 = calculateWeight(crystalBallMidOdds1, midOdds1Weights)
    crystalBallMidOdds2 = calculateWeight(crystalBallMidOdds2, midOdds2Weights)
    crystalBallMidOdds34 = calculateWeight(crystalBallMidOdds34, midOdds34Weights)
    crystalBallLateOdds1 = calculateWeight(crystalBallLateOdds1, lateOdds1Weights)
    crystalBallLateOdds2 = calculateWeight(crystalBallLateOdds2, lateOdds2Weights)
    crystalBallLateOdds34 = calculateWeight(crystalBallLateOdds34, lateOdds34Weights)

    # Magic Lamp
    magicLampEarlyOdds1 = calculateWeight(magicLampEarlyOdds1, earlyOdds1Weights)
    magicLampEarlyOdds2 = calculateWeight(magicLampEarlyOdds2, earlyOdds2Weights)
    magicLampEarlyOdds34 = calculateWeight(magicLampEarlyOdds34, earlyOdds34Weights)
    magicLampMidOdds1 = calculateWeight(magicLampMidOdds1, midOdds1Weights)
    magicLampMidOdds2 = calculateWeight(magicLampMidOdds2, midOdds2Weights)
    magicLampMidOdds34 = calculateWeight(magicLampMidOdds34, midOdds34Weights)
    magicLampLateOdds1 = calculateWeight(magicLampLateOdds1, lateOdds1Weights)
    magicLampLateOdds2 = calculateWeight(magicLampLateOdds2, lateOdds2Weights)
    magicLampLateOdds34 = calculateWeight(magicLampLateOdds34, lateOdds34Weights)

    # Item Bag
    itemBagEarlyOdds1 = calculateWeight(itemBagEarlyOdds1, earlyOdds1Weights)
    itemBagEarlyOdds2 = calculateWeight(itemBagEarlyOdds2, earlyOdds2Weights)
    itemBagEarlyOdds34 = calculateWeight(itemBagEarlyOdds34, earlyOdds34Weights)
    itemBagMidOdds1 = calculateWeight(itemBagMidOdds1, midOdds1Weights)
    itemBagMidOdds2 = calculateWeight(itemBagMidOdds2, midOdds2Weights)
    itemBagMidOdds34 = calculateWeight(itemBagMidOdds34, midOdds34Weights)
    itemBagLateOdds1 = calculateWeight(itemBagLateOdds1, lateOdds1Weights)
    itemBagLateOdds2 = calculateWeight(itemBagLateOdds2, lateOdds2Weights)
    itemBagLateOdds34 = calculateWeight(itemBagLateOdds34, lateOdds34Weights)

    earlyOdds1 = [
        miniMushroomEarlyOdds1,
        megaMushroomEarlyOdds1,
        superMiniMushroomEarlyOdds1,
        superMegaMushroomEarlyOdds1,
        miniMegaHammerEarlyOdds1,
        warpPipeEarlyOdds1,
        swapCardEarlyOdds1,
        sparkyStickerEarlyOdds1,
        gaddlightEarlyOdds1,
        chompCallEarlyOdds1,
        bowserSuitEarlyOdds1,
        crystalBallEarlyOdds1,
        magicLampEarlyOdds1,
        itemBagEarlyOdds1,
    ]
    
    earlyOdds2 = [
        miniMushroomEarlyOdds2,
        megaMushroomEarlyOdds2,
        superMiniMushroomEarlyOdds2,
        superMegaMushroomEarlyOdds2,
        miniMegaHammerEarlyOdds2,
        warpPipeEarlyOdds2,
        swapCardEarlyOdds2,
        sparkyStickerEarlyOdds2,
        gaddlightEarlyOdds2,
        chompCallEarlyOdds2,
        bowserSuitEarlyOdds2,
        crystalBallEarlyOdds2,
        magicLampEarlyOdds2,
        itemBagEarlyOdds2,    
    ]

    earlyOdds34 = [
        miniMushroomEarlyOdds34,
        megaMushroomEarlyOdds34,
        superMiniMushroomEarlyOdds34,
        superMegaMushroomEarlyOdds34,
        miniMegaHammerEarlyOdds34,
        warpPipeEarlyOdds34,
        swapCardEarlyOdds34,
        sparkyStickerEarlyOdds34,
        gaddlightEarlyOdds34,
        chompCallEarlyOdds34,
        bowserSuitEarlyOdds34,
        crystalBallEarlyOdds34,
        magicLampEarlyOdds34,
        itemBagEarlyOdds34,
    ]
    
    midOdds1 = [
        miniMushroomMidOdds1,
        megaMushroomMidOdds1,
        superMiniMushroomMidOdds1,
        superMegaMushroomMidOdds1,
        miniMegaHammerMidOdds1,
        warpPipeMidOdds1,
        swapCardMidOdds1,
        sparkyStickerMidOdds1,
        gaddlightMidOdds1,
        chompCallMidOdds1,
        bowserSuitMidOdds1,
        crystalBallMidOdds1,
        magicLampMidOdds1,
        itemBagMidOdds1,
    ]

    midOdds2 = [
        miniMushroomMidOdds2,
        megaMushroomMidOdds2,
        superMiniMushroomMidOdds2,
        superMegaMushroomMidOdds2,
        miniMegaHammerMidOdds2,
        warpPipeMidOdds2,
        swapCardMidOdds2,
        sparkyStickerMidOdds2,
        gaddlightMidOdds2,
        chompCallMidOdds2,
        bowserSuitMidOdds2,
        crystalBallMidOdds2,
        magicLampMidOdds2,
        itemBagMidOdds2,
    ]

    midOdds34 = [
        miniMushroomMidOdds34,
        megaMushroomMidOdds34,
        superMiniMushroomMidOdds34,
        superMegaMushroomMidOdds34,
        miniMegaHammerMidOdds34,
        warpPipeMidOdds34,
        swapCardMidOdds34,
        sparkyStickerMidOdds34,
        gaddlightMidOdds34,
        chompCallMidOdds34,
        bowserSuitMidOdds34,
        crystalBallMidOdds34,
        magicLampMidOdds34,
        itemBagMidOdds34,
    ]

    lateOdds1 = [
        miniMushroomLateOdds1,
        megaMushroomLateOdds1,
        superMiniMushroomLateOdds1,
        superMegaMushroomLateOdds1,
        miniMegaHammerLateOdds1,
        warpPipeLateOdds1,
        swapCardLateOdds1,
        sparkyStickerLateOdds1,
        gaddlightLateOdds1,
        chompCallLateOdds1,
        bowserSuitLateOdds1,
        crystalBallLateOdds1,
        magicLampLateOdds1,
        itemBagLateOdds1,
    ]

    lateOdds2 = [
        miniMushroomLateOdds2,
        megaMushroomLateOdds2,
        superMiniMushroomLateOdds2,
        superMegaMushroomLateOdds2,
        miniMegaHammerLateOdds2,
        warpPipeLateOdds2,
        swapCardLateOdds2,
        sparkyStickerLateOdds2,
        gaddlightLateOdds2,
        chompCallLateOdds2,
        bowserSuitLateOdds2,
        crystalBallLateOdds2,
        magicLampLateOdds2,
        itemBagLateOdds2,
    ]

    lateOdds34 = [
        miniMushroomLateOdds34,
        megaMushroomLateOdds34,
        superMiniMushroomLateOdds34,
        superMegaMushroomLateOdds34,
        miniMegaHammerLateOdds34,
        warpPipeLateOdds34,
        swapCardLateOdds34,
        sparkyStickerLateOdds34,
        gaddlightLateOdds34,
        chompCallLateOdds34,
        bowserSuitLateOdds34,
        crystalBallLateOdds34,
        magicLampLateOdds34,
        itemBagLateOdds34,
    ]

    earlyOdds1Weights = sum(int(weight) for weight in earlyOdds1)
    earlyOdds2Weights = sum(int(weight) for weight in earlyOdds2)
    earlyOdds34Weights = sum(int(weight) for weight in earlyOdds34)
    midOdds1Weights = sum(int(weight) for weight in midOdds1)
    midOdds2Weights = sum(int(weight) for weight in midOdds2)
    midOdds34Weights = sum(int(weight) for weight in midOdds34)
    lateOdds1Weights = sum(int(weight) for weight in lateOdds1)
    lateOdds2Weights = sum(int(weight) for weight in lateOdds2)
    lateOdds34Weights = sum(int(weight) for weight in lateOdds34)

    earlyOdds1Max = max(zip(earlyOdds1, earlyOdds1), key=lambda tuple: int(tuple[1]))[0]
    earlyOdds2Max = max(zip(earlyOdds2, earlyOdds2), key=lambda tuple: int(tuple[1]))[0]
    earlyOdds34Max = max(zip(earlyOdds34, earlyOdds34), key=lambda tuple: int(tuple[1]))[0]
    midOdds1Max = max(zip(midOdds1, midOdds1), key=lambda tuple: int(tuple[1]))[0]
    midOdds2Max = max(zip(midOdds2, midOdds2), key=lambda tuple: int(tuple[1]))[0]
    midOdds34Max = max(zip(midOdds34, midOdds34), key=lambda tuple: int(tuple[1]))[0]
    lateOdds1Max = max(zip(lateOdds1, lateOdds1), key=lambda tuple: int(tuple[1]))[0]
    lateOdds2Max = max(zip(lateOdds2, lateOdds2), key=lambda tuple: int(tuple[1]))[0]
    lateOdds34Max = max(zip(lateOdds34, lateOdds34), key=lambda tuple: int(tuple[1]))[0]

    # Mini Mushroom
    if earlyOdds1Max == 'miniMushroomEarlyOdds1':
        miniMushroomEarlyOdds1 += (100 - miniMushroomEarlyOdds1)
    if earlyOdds2Max == 'miniMushroomEarlyOdds2':
        miniMushroomEarlyOdds2 += (100 - miniMushroomEarlyOdds2)
    if earlyOdds34Max == 'miniMushroomEarlyOdds34':
        miniMushroomEarlyOdds34 += (100 - miniMushroomEarlyOdds34)
    if midOdds1Max == 'miniMushroomMidOdds1':
        miniMushroomMidOdds1 += (100 - miniMushroomMidOdds1)
    if midOdds2Max == 'miniMushroomMidOdds2':
        miniMushroomMidOdds2 += (100 - miniMushroomMidOdds2)
    if midOdds34Max == 'miniMushroomMidOdds34':
        miniMushroomMidOdds34 += (100 - miniMushroomMidOdds34)
    if lateOdds1Max == 'miniMushroomLateOdds1':
        miniMushroomLateOdds1 += (100 - miniMushroomLateOdds1)
    if lateOdds2Max == 'miniMushroomLateOdds2':
        miniMushroomLateOdds2 += (100 - miniMushroomLateOdds2)
    if lateOdds34Max == 'miniMushroomLateOdds34':
        miniMushroomLateOdds34 += (100 - miniMushroomLateOdds34)

    # Mega Mushroom
    if earlyOdds1Max == 'megaMushroomEarlyOdds1':
        megaMushroomEarlyOdds1 += (100 - megaMushroomEarlyOdds1)
    if earlyOdds2Max == 'megaMushroomEarlyOdds2':
        megaMushroomEarlyOdds2 += (100 - megaMushroomEarlyOdds2)
    if earlyOdds34Max == 'megaMushroomEarlyOdds34':
        megaMushroomEarlyOdds34 += (100 - megaMushroomEarlyOdds34)
    if midOdds1Max == 'megaMushroomMidOdds1':
        megaMushroomMidOdds1 += (100 - megaMushroomMidOdds1)
    if midOdds2Max == 'megaMushroomMidOdds2':
        megaMushroomMidOdds2 += (100 - megaMushroomMidOdds2)
    if midOdds34Max == 'megaMushroomMidOdds34':
        megaMushroomMidOdds34 += (100 - megaMushroomMidOdds34)
    if lateOdds1Max == 'megaMushroomLateOdds1':
        megaMushroomLateOdds1 += (100 - megaMushroomLateOdds1)
    if lateOdds2Max == 'megaMushroomLateOdds2':
        megaMushroomLateOdds2 += (100 - megaMushroomLateOdds2)
    if lateOdds34Max == 'megaMushroomLateOdds34':
        megaMushroomLateOdds34 += (100 - megaMushroomLateOdds34)

    # Super Mini Mushroom
    if earlyOdds1Max == 'superMiniMushroomEarlyOdds1':
        superMiniMushroomEarlyOdds1 += (100 - superMiniMushroomEarlyOdds1)
    if earlyOdds2Max == 'superMiniMushroomEarlyOdds2':
        superMiniMushroomEarlyOdds2 += (100 - superMiniMushroomEarlyOdds2)
    if earlyOdds34Max == 'superMiniMushroomEarlyOdds34':
        superMiniMushroomEarlyOdds34 += (100 - superMiniMushroomEarlyOdds34)
    if midOdds1Max == 'superMiniMushroomMidOdds1':
        superMiniMushroomMidOdds1 += (100 - superMiniMushroomMidOdds1)
    if midOdds2Max == 'superMiniMushroomMidOdds2':
        superMiniMushroomMidOdds2 += (100 - superMiniMushroomMidOdds2)
    if midOdds34Max == 'superMiniMushroomMidOdds34':
        superMiniMushroomMidOdds34 += (100 - superMiniMushroomMidOdds34)
    if lateOdds1Max == 'superMiniMushroomLateOdds1':
        superMiniMushroomLateOdds1 += (100 - superMiniMushroomLateOdds1)
    if lateOdds2Max == 'superMiniMushroomLateOdds2':
        superMiniMushroomLateOdds2 += (100 - superMiniMushroomLateOdds2)
    if lateOdds34Max == 'superMiniMushroomLateOdds34':
        superMiniMushroomLateOdds34 += (100 - superMiniMushroomLateOdds34)

    # Super Mega Mushroom
    if earlyOdds1Max == 'superMegaMushroomEarlyOdds1':
        superMegaMushroomEarlyOdds1 += (100 - superMegaMushroomEarlyOdds1)
    if earlyOdds2Max == 'superMegaMushroomEarlyOdds2':
        superMegaMushroomEarlyOdds2 += (100 - superMegaMushroomEarlyOdds2)
    if earlyOdds34Max == 'superMegaMushroomEarlyOdds34':
        superMegaMushroomEarlyOdds34 += (100 - superMegaMushroomEarlyOdds34)
    if midOdds1Max == 'superMegaMushroomMidOdds1':
        superMegaMushroomMidOdds1 += (100 - superMegaMushroomMidOdds1)
    if midOdds2Max == 'superMegaMushroomMidOdds2':
        superMegaMushroomMidOdds2 += (100 - superMegaMushroomMidOdds2)
    if midOdds34Max == 'superMegaMushroomMidOdds34':
        superMegaMushroomMidOdds34 += (100 - superMegaMushroomMidOdds34)
    if lateOdds1Max == 'superMegaMushroomLateOdds1':
        superMegaMushroomLateOdds1 += (100 - superMegaMushroomLateOdds1)
    if lateOdds2Max == 'superMegaMushroomLateOdds2':
        superMegaMushroomLateOdds2 += (100 - superMegaMushroomLateOdds2)
    if lateOdds34Max == 'superMegaMushroomLateOdds34':
        superMegaMushroomLateOdds34 += (100 - superMegaMushroomLateOdds34)

    # Mini Mega Hammer
    if earlyOdds1Max == 'miniMegaHammerEarlyOdds1':
        miniMegaHammerEarlyOdds1 += (100 - miniMegaHammerEarlyOdds1)
    if earlyOdds2Max == 'miniMegaHammerEarlyOdds2':
        miniMegaHammerEarlyOdds2 += (100 - miniMegaHammerEarlyOdds2)
    if earlyOdds34Max == 'miniMegaHammerEarlyOdds34':
        miniMegaHammerEarlyOdds34 += (100 - miniMegaHammerEarlyOdds34)
    if midOdds1Max == 'miniMegaHammerMidOdds1':
        miniMegaHammerMidOdds1 += (100 - miniMegaHammerMidOdds1)
    if midOdds2Max == 'miniMegaHammerMidOdds2':
        miniMegaHammerMidOdds2 += (100 - miniMegaHammerMidOdds2)
    if midOdds34Max == 'miniMegaHammerMidOdds34':
        miniMegaHammerMidOdds34 += (100 - miniMegaHammerMidOdds34)
    if lateOdds1Max == 'miniMegaHammerLateOdds1':
        miniMegaHammerLateOdds1 += (100 - miniMegaHammerLateOdds1)
    if lateOdds2Max == 'miniMegaHammerLateOdds2':
        miniMegaHammerLateOdds2 += (100 - miniMegaHammerLateOdds2)
    if lateOdds34Max == 'miniMegaHammerLateOdds34':
        miniMegaHammerLateOdds34 += (100 - miniMegaHammerLateOdds34)

    # Warp Pipe
    if earlyOdds1Max == 'warpPipeEarlyOdds1':
        warpPipeEarlyOdds1 += (100 - warpPipeEarlyOdds1)
    if earlyOdds2Max == 'warpPipeEarlyOdds2':
        warpPipeEarlyOdds2 += (100 - warpPipeEarlyOdds2)
    if earlyOdds34Max == 'warpPipeEarlyOdds34':
        warpPipeEarlyOdds34 += (100 - warpPipeEarlyOdds34)
    if midOdds1Max == 'warpPipeMidOdds1':
        warpPipeMidOdds1 += (100 - warpPipeMidOdds1)
    if midOdds2Max == 'warpPipeMidOdds2':
        warpPipeMidOdds2 += (100 - warpPipeMidOdds2)
    if midOdds34Max == 'warpPipeMidOdds34':
        warpPipeMidOdds34 += (100 - warpPipeMidOdds34)
    if lateOdds1Max == 'warpPipeLateOdds1':
        warpPipeLateOdds1 += (100 - warpPipeLateOdds1)
    if lateOdds2Max == 'warpPipeLateOdds2':
        warpPipeLateOdds2 += (100 - warpPipeLateOdds2)
    if lateOdds34Max == 'warpPipeLateOdds34':
        warpPipeLateOdds34 += (100 - warpPipeLateOdds34)

    # Swap Card
    if earlyOdds1Max == 'swapCardEarlyOdds1':
        swapCardEarlyOdds1 += (100 - swapCardEarlyOdds1)
    if earlyOdds2Max == 'swapCardEarlyOdds2':
        swapCardEarlyOdds2 += (100 - swapCardEarlyOdds2)
    if earlyOdds34Max == 'swapCardEarlyOdds34':
        swapCardEarlyOdds34 += (100 - swapCardEarlyOdds34)
    if midOdds1Max == 'swapCardMidOdds1':
        swapCardMidOdds1 += (100 - swapCardMidOdds1)
    if midOdds2Max == 'swapCardMidOdds2':
        swapCardMidOdds2 += (100 - swapCardMidOdds2)
    if midOdds34Max == 'swapCardMidOdds34':
        swapCardMidOdds34 += (100 - swapCardMidOdds34)
    if lateOdds1Max == 'swapCardLateOdds1':
        swapCardLateOdds1 += (100 - swapCardLateOdds1)
    if lateOdds2Max == 'swapCardLateOdds2':
        swapCardLateOdds2 += (100 - swapCardLateOdds2)
    if lateOdds34Max == 'swapCardLateOdds34':
        swapCardLateOdds34 += (100 - swapCardLateOdds34)

    # Sparky Sticker
    if earlyOdds1Max == 'sparkyStickerEarlyOdds1':
        sparkyStickerEarlyOdds1 += (100 - sparkyStickerEarlyOdds1)
    if earlyOdds2Max == 'sparkyStickerEarlyOdds2':
        sparkyStickerEarlyOdds2 += (100 - sparkyStickerEarlyOdds2)
    if earlyOdds34Max == 'sparkyStickerEarlyOdds34':
        sparkyStickerEarlyOdds34 += (100 - sparkyStickerEarlyOdds34)
    if midOdds1Max == 'sparkyStickerMidOdds1':
        sparkyStickerMidOdds1 += (100 - sparkyStickerMidOdds1)
    if midOdds2Max == 'sparkyStickerMidOdds2':
        sparkyStickerMidOdds2 += (100 - sparkyStickerMidOdds2)
    if midOdds34Max == 'sparkyStickerMidOdds34':
        sparkyStickerMidOdds34 += (100 - sparkyStickerMidOdds34)
    if lateOdds1Max == 'sparkyStickerLateOdds1':
        sparkyStickerLateOdds1 += (100 - sparkyStickerLateOdds1)
    if lateOdds2Max == 'sparkyStickerLateOdds2':
        sparkyStickerLateOdds2 += (100 - sparkyStickerLateOdds2)
    if lateOdds34Max == 'sparkyStickerLateOdds34':
        sparkyStickerLateOdds34 += (100 - sparkyStickerLateOdds34)

    # Gaddlight
    if earlyOdds1Max == 'gaddlightEarlyOdds1':
        gaddlightEarlyOdds1 += (100 - gaddlightEarlyOdds1)
    if earlyOdds2Max == 'gaddlightEarlyOdds2':
        gaddlightEarlyOdds2 += (100 - gaddlightEarlyOdds2)
    if earlyOdds34Max == 'gaddlightEarlyOdds34':
        gaddlightEarlyOdds34 += (100 - gaddlightEarlyOdds34)
    if midOdds1Max == 'gaddlightMidOdds1':
        gaddlightMidOdds1 += (100 - gaddlightMidOdds1)
    if midOdds2Max == 'gaddlightMidOdds2':
        gaddlightMidOdds2 += (100 - gaddlightMidOdds2)
    if midOdds34Max == 'gaddlightMidOdds34':
        gaddlightMidOdds34 += (100 - gaddlightMidOdds34)
    if lateOdds1Max == 'gaddlightLateOdds1':
        gaddlightLateOdds1 += (100 - gaddlightLateOdds1)
    if lateOdds2Max == 'gaddlightLateOdds2':
        gaddlightLateOdds2 += (100 - gaddlightLateOdds2)
    if lateOdds34Max == 'gaddlightLateOdds34':
        gaddlightLateOdds34 += (100 - gaddlightLateOdds34)

    # Chomp Call
    if earlyOdds1Max == 'chompCallEarlyOdds1':
        chompCallEarlyOdds1 += (100 - chompCallEarlyOdds1)
    if earlyOdds2Max == 'chompCallEarlyOdds2':
        chompCallEarlyOdds2 += (100 - chompCallEarlyOdds2)
    if earlyOdds34Max == 'chompCallEarlyOdds34':
        chompCallEarlyOdds34 += (100 - chompCallEarlyOdds34)
    if midOdds1Max == 'chompCallMidOdds1':
        chompCallMidOdds1 += (100 - chompCallMidOdds1)
    if midOdds2Max == 'chompCallMidOdds2':
        chompCallMidOdds2 += (100 - chompCallMidOdds2)
    if midOdds34Max == 'chompCallMidOdds34':
        chompCallMidOdds34 += (100 - chompCallMidOdds34)
    if lateOdds1Max == 'chompCallLateOdds1':
        chompCallLateOdds1 += (100 - chompCallLateOdds1)
    if lateOdds2Max == 'chompCallLateOdds2':
        chompCallLateOdds2 += (100 - chompCallLateOdds2)
    if lateOdds34Max == 'chompCallLateOdds34':
        chompCallLateOdds34 += (100 - chompCallLateOdds34)

    # Bowser Suit
    if earlyOdds1Max == 'bowserSuitEarlyOdds1':
        bowserSuitEarlyOdds1 += (100 - bowserSuitEarlyOdds1)
    if earlyOdds2Max == 'bowserSuitEarlyOdds2':
        bowserSuitEarlyOdds2 += (100 - bowserSuitEarlyOdds2)
    if earlyOdds34Max == 'bowserSuitEarlyOdds34':
        bowserSuitEarlyOdds34 += (100 - bowserSuitEarlyOdds34)
    if midOdds1Max == 'bowserSuitMidOdds1':
        bowserSuitMidOdds1 += (100 - bowserSuitMidOdds1)
    if midOdds2Max == 'bowserSuitMidOdds2':
        bowserSuitMidOdds2 += (100 - bowserSuitMidOdds2)
    if midOdds34Max == 'bowserSuitMidOdds34':
        bowserSuitMidOdds34 += (100 - bowserSuitMidOdds34)
    if lateOdds1Max == 'bowserSuitLateOdds1':
        bowserSuitLateOdds1 += (100 - bowserSuitLateOdds1)
    if lateOdds2Max == 'bowserSuitLateOdds2':
        bowserSuitLateOdds2 += (100 - bowserSuitLateOdds2)
    if lateOdds34Max == 'bowserSuitLateOdds34':
        bowserSuitLateOdds34 += (100 - bowserSuitLateOdds34)

    # Crystal Ball
    if earlyOdds1Max == 'crystalBallEarlyOdds1':
        crystalBallEarlyOdds1 += (100 - crystalBallEarlyOdds1)
    if earlyOdds2Max == 'crystalBallEarlyOdds2':
        crystalBallEarlyOdds2 += (100 - crystalBallEarlyOdds2)
    if earlyOdds34Max == 'crystalBallEarlyOdds34':
        crystalBallEarlyOdds34 += (100 - crystalBallEarlyOdds34)
    if midOdds1Max == 'crystalBallMidOdds1':
        crystalBallMidOdds1 += (100 - crystalBallMidOdds1)
    if midOdds2Max == 'crystalBallMidOdds2':
        crystalBallMidOdds2 += (100 - crystalBallMidOdds2)
    if midOdds34Max == 'crystalBallMidOdds34':
        crystalBallMidOdds34 += (100 - crystalBallMidOdds34)
    if lateOdds1Max == 'crystalBallLateOdds1':
        crystalBallLateOdds1 += (100 - crystalBallLateOdds1)
    if lateOdds2Max == 'crystalBallLateOdds2':
        crystalBallLateOdds2 += (100 - crystalBallLateOdds2)
    if lateOdds34Max == 'crystalBallLateOdds34':
        crystalBallLateOdds34 += (100 - crystalBallLateOdds34)

    # Magic Lamp
    if earlyOdds1Max == 'magicLampEarlyOdds1':
        magicLampEarlyOdds1 += (100 - magicLampEarlyOdds1)
    if earlyOdds2Max == 'magicLampEarlyOdds2':
        magicLampEarlyOdds2 += (100 - magicLampEarlyOdds2)
    if earlyOdds34Max == 'magicLampEarlyOdds34':
        magicLampEarlyOdds34 += (100 - magicLampEarlyOdds34)
    if midOdds1Max == 'magicLampMidOdds1':
        magicLampMidOdds1 += (100 - magicLampMidOdds1)
    if midOdds2Max == 'magicLampMidOdds2':
        magicLampMidOdds2 += (100 - magicLampMidOdds2)
    if midOdds34Max == 'magicLampMidOdds34':
        magicLampMidOdds34 += (100 - magicLampMidOdds34)
    if lateOdds1Max == 'magicLampLateOdds1':
        magicLampLateOdds1 += (100 - magicLampLateOdds1)
    if lateOdds2Max == 'magicLampLateOdds2':
        magicLampLateOdds2 += (100 - magicLampLateOdds2)
    if lateOdds34Max == 'magicLampLateOdds34':
        magicLampLateOdds34 += (100 - magicLampLateOdds34)

    # Item Bag
    if earlyOdds1Max == 'itemBagEarlyOdds1':
        itemBagEarlyOdds1 += (100 - itemBagEarlyOdds1)
    if earlyOdds2Max == 'itemBagEarlyOdds2':
        itemBagEarlyOdds2 += (100 - itemBagEarlyOdds2)
    if earlyOdds34Max == 'itemBagEarlyOdds34':
        itemBagEarlyOdds34 += (100 - itemBagEarlyOdds34)
    if midOdds1Max == 'itemBagMidOdds1':
        itemBagMidOdds1 += (100 - itemBagMidOdds1)
    if midOdds2Max == 'itemBagMidOdds2':
        itemBagMidOdds2 += (100 - itemBagMidOdds2)
    if midOdds34Max == 'itemBagMidOdds34':
        itemBagMidOdds34 += (100 - itemBagMidOdds34)
    if lateOdds1Max == 'itemBagLateOdds1':
        itemBagLateOdds1 += (100 - itemBagLateOdds1)
    if lateOdds2Max == 'itemBagLateOdds2':
        itemBagLateOdds2 += (100 - itemBagLateOdds2)
    if lateOdds34Max == 'itemBagLateOdds34':
        itemBagLateOdds34 += (100 - itemBagLateOdds34)

    # Mini Mushroom
    miniMushroomEarlyOdds1 = str(miniMushroomEarlyOdds1)
    miniMushroomEarlyOdds2 = str(miniMushroomEarlyOdds2)
    miniMushroomEarlyOdds34 = str(miniMushroomEarlyOdds34)
    miniMushroomMidOdds1 = str(miniMushroomMidOdds1)
    miniMushroomMidOdds2 = str(miniMushroomMidOdds2)
    miniMushroomMidOdds34 = str(miniMushroomMidOdds34)
    miniMushroomLateOdds1 = str(miniMushroomLateOdds1)
    miniMushroomLateOdds2 = str(miniMushroomLateOdds2)
    miniMushroomLateOdds34 = str(miniMushroomLateOdds34)
    
    # Mega Mushroom
    megaMushroomEarlyOdds1 = str(megaMushroomEarlyOdds1)
    megaMushroomEarlyOdds2 = str(megaMushroomEarlyOdds2)
    megaMushroomEarlyOdds34 = str(megaMushroomEarlyOdds34)
    megaMushroomMidOdds1 = str(megaMushroomMidOdds1)
    megaMushroomMidOdds2 = str(megaMushroomMidOdds2)
    megaMushroomMidOdds34 = str(megaMushroomMidOdds34)
    megaMushroomLateOdds1 = str(megaMushroomLateOdds1)
    megaMushroomLateOdds2 = str(megaMushroomLateOdds2)
    megaMushroomLateOdds34 = str(megaMushroomLateOdds34)

    # Super Mini Mushroom
    superMiniMushroomEarlyOdds1 = str(superMiniMushroomEarlyOdds1)
    superMiniMushroomEarlyOdds2 = str(superMiniMushroomEarlyOdds2)
    superMiniMushroomEarlyOdds34 = str(superMiniMushroomEarlyOdds34)
    superMiniMushroomMidOdds1 = str(superMiniMushroomMidOdds1)
    superMiniMushroomMidOdds2 = str(superMiniMushroomMidOdds2)
    superMiniMushroomMidOdds34 = str(superMiniMushroomMidOdds34)
    superMiniMushroomLateOdds1 = str(superMiniMushroomLateOdds1)
    superMiniMushroomLateOdds2 = str(superMiniMushroomLateOdds2)
    superMiniMushroomLateOdds34 = str(superMiniMushroomLateOdds34)

    # Super Mega Mushroom
    superMegaMushroomEarlyOdds1 = str(superMegaMushroomEarlyOdds1)
    superMegaMushroomEarlyOdds2 = str(superMegaMushroomEarlyOdds2)
    superMegaMushroomEarlyOdds34 = str(superMegaMushroomEarlyOdds34)
    superMegaMushroomMidOdds1 = str(superMegaMushroomMidOdds1)
    superMegaMushroomMidOdds2 = str(superMegaMushroomMidOdds2)
    superMegaMushroomMidOdds34 = str(superMegaMushroomMidOdds34)
    superMegaMushroomLateOdds1 = str(superMegaMushroomLateOdds1)
    superMegaMushroomLateOdds2 = str(superMegaMushroomLateOdds2)
    superMegaMushroomLateOdds34 = str(superMegaMushroomLateOdds34)

    # Mini Mega Hammer
    miniMegaHammerEarlyOdds1 = str(miniMegaHammerEarlyOdds1)
    miniMegaHammerEarlyOdds2 = str(miniMegaHammerEarlyOdds2)
    miniMegaHammerEarlyOdds34 = str(miniMegaHammerEarlyOdds34)
    miniMegaHammerMidOdds1 = str(miniMegaHammerMidOdds1)
    miniMegaHammerMidOdds2 = str(miniMegaHammerMidOdds2)
    miniMegaHammerMidOdds34 = str(miniMegaHammerMidOdds34)
    miniMegaHammerLateOdds1 = str(miniMegaHammerLateOdds1)
    miniMegaHammerLateOdds2 = str(miniMegaHammerLateOdds2)
    miniMegaHammerLateOdds34 = str(miniMegaHammerLateOdds34)

    # Warp Pipe
    warpPipeEarlyOdds1 = str(warpPipeEarlyOdds1)
    warpPipeEarlyOdds2 = str(warpPipeEarlyOdds2)
    warpPipeEarlyOdds34 = str(warpPipeEarlyOdds34)
    warpPipeMidOdds1 = str(warpPipeMidOdds1)
    warpPipeMidOdds2 = str(warpPipeMidOdds2)
    warpPipeMidOdds34 = str(warpPipeMidOdds34)
    warpPipeLateOdds1 = str(warpPipeLateOdds1)
    warpPipeLateOdds2 = str(warpPipeLateOdds2)
    warpPipeLateOdds34 = str(warpPipeLateOdds34)

    # Swap Card
    swapCardEarlyOdds1 = str(swapCardEarlyOdds1)
    swapCardEarlyOdds2 = str(swapCardEarlyOdds2)
    swapCardEarlyOdds34 = str(swapCardEarlyOdds34)
    swapCardMidOdds1 = str(swapCardMidOdds1)
    swapCardMidOdds2 = str(swapCardMidOdds2)
    swapCardMidOdds34 = str(swapCardMidOdds34)
    swapCardLateOdds1 = str(swapCardLateOdds1)
    swapCardLateOdds2 = str(swapCardLateOdds2)
    swapCardLateOdds34 = str(swapCardLateOdds34)

    # Sparky Sticker
    sparkyStickerEarlyOdds1 = str(sparkyStickerEarlyOdds1)
    sparkyStickerEarlyOdds2 = str(sparkyStickerEarlyOdds2)
    sparkyStickerEarlyOdds34 = str(sparkyStickerEarlyOdds34)
    sparkyStickerMidOdds1 = str(sparkyStickerMidOdds1)
    sparkyStickerMidOdds2 = str(sparkyStickerMidOdds2)
    sparkyStickerMidOdds34 = str(sparkyStickerMidOdds34)
    sparkyStickerLateOdds1 = str(sparkyStickerLateOdds1)
    sparkyStickerLateOdds2 = str(sparkyStickerLateOdds2)
    sparkyStickerLateOdds34 = str(sparkyStickerLateOdds34)

    # Gaddlight
    gaddlightEarlyOdds1 = str(gaddlightEarlyOdds1)
    gaddlightEarlyOdds2 = str(gaddlightEarlyOdds2)
    gaddlightEarlyOdds34 = str(gaddlightEarlyOdds34)
    gaddlightMidOdds1 = str(gaddlightMidOdds1)
    gaddlightMidOdds2 = str(gaddlightMidOdds2)
    gaddlightMidOdds34 = str(gaddlightMidOdds34)
    gaddlightLateOdds1 = str(gaddlightLateOdds1)
    gaddlightLateOdds2 = str(gaddlightLateOdds2)
    gaddlightLateOdds34 = str(gaddlightLateOdds34)

    # Chomp Call
    chompCallEarlyOdds1 = str(chompCallEarlyOdds1)
    chompCallEarlyOdds2 = str(chompCallEarlyOdds2)
    chompCallEarlyOdds34 = str(chompCallEarlyOdds34)
    chompCallMidOdds1 = str(chompCallMidOdds1)
    chompCallMidOdds2 = str(chompCallMidOdds2)
    chompCallMidOdds34 = str(chompCallMidOdds34)
    chompCallLateOdds1 = str(chompCallLateOdds1)
    chompCallLateOdds2 = str(chompCallLateOdds2)
    chompCallLateOdds34 = str(chompCallLateOdds34)

    # Bowser Suit
    bowserSuitEarlyOdds1 = str(bowserSuitEarlyOdds1)
    bowserSuitEarlyOdds2 = str(bowserSuitEarlyOdds2)
    bowserSuitEarlyOdds34 = str(bowserSuitEarlyOdds34)
    bowserSuitMidOdds1 = str(bowserSuitMidOdds1)
    bowserSuitMidOdds2 = str(bowserSuitMidOdds2)
    bowserSuitMidOdds34 = str(bowserSuitMidOdds34)
    bowserSuitLateOdds1 = str(bowserSuitLateOdds1)
    bowserSuitLateOdds2 = str(bowserSuitLateOdds2)
    bowserSuitLateOdds34 = str(bowserSuitLateOdds34)

    # Crystal Ball
    crystalBallEarlyOdds1 = str(crystalBallEarlyOdds1)
    crystalBallEarlyOdds2 = str(crystalBallEarlyOdds2)
    crystalBallEarlyOdds34 = str(crystalBallEarlyOdds34)
    crystalBallMidOdds1 = str(crystalBallMidOdds1)
    crystalBallMidOdds2 = str(crystalBallMidOdds2)
    crystalBallMidOdds34 = str(crystalBallMidOdds34)
    crystalBallLateOdds1 = str(crystalBallLateOdds1)
    crystalBallLateOdds2 = str(crystalBallLateOdds2)
    crystalBallLateOdds34 = str(crystalBallLateOdds34)

    # Magic Lamp
    magicLampEarlyOdds1 = str(magicLampEarlyOdds1)
    magicLampEarlyOdds2 = str(magicLampEarlyOdds2)
    magicLampEarlyOdds34 = str(magicLampEarlyOdds34)
    magicLampMidOdds1 = str(magicLampMidOdds1)
    magicLampMidOdds2 = str(magicLampMidOdds2)
    magicLampMidOdds34 = str(magicLampMidOdds34)
    magicLampLateOdds1 = str(magicLampLateOdds1)
    magicLampLateOdds2 = str(magicLampLateOdds2)
    magicLampLateOdds34 = str(magicLampLateOdds34)

    # Item Bag
    itemBagEarlyOdds1 = str(itemBagEarlyOdds1)
    itemBagEarlyOdds2 = str(itemBagEarlyOdds2)
    itemBagEarlyOdds34 = str(itemBagEarlyOdds34)
    itemBagMidOdds1 = str(itemBagMidOdds1)
    itemBagMidOdds2 = str(itemBagMidOdds2)
    itemBagMidOdds34 = str(itemBagMidOdds34)
    itemBagLateOdds1 = str(itemBagLateOdds1)
    itemBagLateOdds2 = str(itemBagLateOdds2)
    itemBagLateOdds34 = str(itemBagLateOdds34)

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
    miniMushroomEarlyOdds1 = convert_to_hex_weight(miniMushroomEarlyOdds1)
    miniMushroomEarlyOdds2 = convert_to_hex_weight(miniMushroomEarlyOdds2)
    miniMushroomEarlyOdds34 = convert_to_hex_weight(miniMushroomEarlyOdds34)
    miniMushroomMidOdds1 = convert_to_hex_weight(miniMushroomMidOdds1)
    miniMushroomMidOdds2 = convert_to_hex_weight(miniMushroomMidOdds2)
    miniMushroomMidOdds34 = convert_to_hex_weight(miniMushroomMidOdds34)
    miniMushroomLateOdds1 = convert_to_hex_weight(miniMushroomLateOdds1)
    miniMushroomLateOdds2 = convert_to_hex_weight(miniMushroomLateOdds2)
    miniMushroomLateOdds34 = convert_to_hex_weight(miniMushroomLateOdds34)
    
    # Mega Mushroom
    megaMushroomEarlyOdds1 = convert_to_hex_weight(megaMushroomEarlyOdds1)
    megaMushroomEarlyOdds2 = convert_to_hex_weight(megaMushroomEarlyOdds2)
    megaMushroomEarlyOdds34 = convert_to_hex_weight(megaMushroomEarlyOdds34)
    megaMushroomMidOdds1 = convert_to_hex_weight(megaMushroomMidOdds1)
    megaMushroomMidOdds2 = convert_to_hex_weight(megaMushroomMidOdds2)
    megaMushroomMidOdds34 = convert_to_hex_weight(megaMushroomMidOdds34)
    megaMushroomLateOdds1 = convert_to_hex_weight(megaMushroomLateOdds1)
    megaMushroomLateOdds2 = convert_to_hex_weight(megaMushroomLateOdds2)
    megaMushroomLateOdds34 = convert_to_hex_weight(megaMushroomLateOdds34)

    # Super Mini Mushroom
    superMiniMushroomEarlyOdds1 = convert_to_hex_weight(superMiniMushroomEarlyOdds1)
    superMiniMushroomEarlyOdds2 = convert_to_hex_weight(superMiniMushroomEarlyOdds2)
    superMiniMushroomEarlyOdds34 = convert_to_hex_weight(superMiniMushroomEarlyOdds34)
    superMiniMushroomMidOdds1 = convert_to_hex_weight(superMiniMushroomMidOdds1)
    superMiniMushroomMidOdds2 = convert_to_hex_weight(superMiniMushroomMidOdds2)
    superMiniMushroomMidOdds34 = convert_to_hex_weight(superMiniMushroomMidOdds34)
    superMiniMushroomLateOdds1 = convert_to_hex_weight(superMiniMushroomLateOdds1)
    superMiniMushroomLateOdds2 = convert_to_hex_weight(superMiniMushroomLateOdds2)
    superMiniMushroomLateOdds34 = convert_to_hex_weight(superMiniMushroomLateOdds34)

    # Super Mega Mushroom
    superMegaMushroomEarlyOdds1 = convert_to_hex_weight(superMegaMushroomEarlyOdds1)
    superMegaMushroomEarlyOdds2 = convert_to_hex_weight(superMegaMushroomEarlyOdds2)
    superMegaMushroomEarlyOdds34 = convert_to_hex_weight(superMegaMushroomEarlyOdds34)
    superMegaMushroomMidOdds1 = convert_to_hex_weight(superMegaMushroomMidOdds1)
    superMegaMushroomMidOdds2 = convert_to_hex_weight(superMegaMushroomMidOdds2)
    superMegaMushroomMidOdds34 = convert_to_hex_weight(superMegaMushroomMidOdds34)
    superMegaMushroomLateOdds1 = convert_to_hex_weight(superMegaMushroomLateOdds1)
    superMegaMushroomLateOdds2 = convert_to_hex_weight(superMegaMushroomLateOdds2)
    superMegaMushroomLateOdds34 = convert_to_hex_weight(superMegaMushroomLateOdds34)

    # Mini Mega Hammer
    miniMegaHammerEarlyOdds1 = convert_to_hex_weight(miniMegaHammerEarlyOdds1)
    miniMegaHammerEarlyOdds2 = convert_to_hex_weight(miniMegaHammerEarlyOdds2)
    miniMegaHammerEarlyOdds34 = convert_to_hex_weight(miniMegaHammerEarlyOdds34)
    miniMegaHammerMidOdds1 = convert_to_hex_weight(miniMegaHammerMidOdds1)
    miniMegaHammerMidOdds2 = convert_to_hex_weight(miniMegaHammerMidOdds2)
    miniMegaHammerMidOdds34 = convert_to_hex_weight(miniMegaHammerMidOdds34)
    miniMegaHammerLateOdds1 = convert_to_hex_weight(miniMegaHammerLateOdds1)
    miniMegaHammerLateOdds2 = convert_to_hex_weight(miniMegaHammerLateOdds2)
    miniMegaHammerLateOdds34 = convert_to_hex_weight(miniMegaHammerLateOdds34)

    # Warp Pipe
    warpPipeEarlyOdds1 = convert_to_hex_weight(warpPipeEarlyOdds1)
    warpPipeEarlyOdds2 = convert_to_hex_weight(warpPipeEarlyOdds2)
    warpPipeEarlyOdds34 = convert_to_hex_weight(warpPipeEarlyOdds34)
    warpPipeMidOdds1 = convert_to_hex_weight(warpPipeMidOdds1)
    warpPipeMidOdds2 = convert_to_hex_weight(warpPipeMidOdds2)
    warpPipeMidOdds34 = convert_to_hex_weight(warpPipeMidOdds34)
    warpPipeLateOdds1 = convert_to_hex_weight(warpPipeLateOdds1)
    warpPipeLateOdds2 = convert_to_hex_weight(warpPipeLateOdds2)
    warpPipeLateOdds34 = convert_to_hex_weight(warpPipeLateOdds34)

    # Swap Card
    swapCardEarlyOdds1 = convert_to_hex_weight(swapCardEarlyOdds1)
    swapCardEarlyOdds2 = convert_to_hex_weight(swapCardEarlyOdds2)
    swapCardEarlyOdds34 = convert_to_hex_weight(swapCardEarlyOdds34)
    swapCardMidOdds1 = convert_to_hex_weight(swapCardMidOdds1)
    swapCardMidOdds2 = convert_to_hex_weight(swapCardMidOdds2)
    swapCardMidOdds34 = convert_to_hex_weight(swapCardMidOdds34)
    swapCardLateOdds1 = convert_to_hex_weight(swapCardLateOdds1)
    swapCardLateOdds2 = convert_to_hex_weight(swapCardLateOdds2)
    swapCardLateOdds34 = convert_to_hex_weight(swapCardLateOdds34)

    # Sparky Sticker
    sparkyStickerEarlyOdds1 = convert_to_hex_weight(sparkyStickerEarlyOdds1)
    sparkyStickerEarlyOdds2 = convert_to_hex_weight(sparkyStickerEarlyOdds2)
    sparkyStickerEarlyOdds34 = convert_to_hex_weight(sparkyStickerEarlyOdds34)
    sparkyStickerMidOdds1 = convert_to_hex_weight(sparkyStickerMidOdds1)
    sparkyStickerMidOdds2 = convert_to_hex_weight(sparkyStickerMidOdds2)
    sparkyStickerMidOdds34 = convert_to_hex_weight(sparkyStickerMidOdds34)
    sparkyStickerLateOdds1 = convert_to_hex_weight(sparkyStickerLateOdds1)
    sparkyStickerLateOdds2 = convert_to_hex_weight(sparkyStickerLateOdds2)
    sparkyStickerLateOdds34 = convert_to_hex_weight(sparkyStickerLateOdds34)

    # Gaddlight
    gaddlightEarlyOdds1 = convert_to_hex_weight(gaddlightEarlyOdds1)
    gaddlightEarlyOdds2 = convert_to_hex_weight(gaddlightEarlyOdds2)
    gaddlightEarlyOdds34 = convert_to_hex_weight(gaddlightEarlyOdds34)
    gaddlightMidOdds1 = convert_to_hex_weight(gaddlightMidOdds1)
    gaddlightMidOdds2 = convert_to_hex_weight(gaddlightMidOdds2)
    gaddlightMidOdds34 = convert_to_hex_weight(gaddlightMidOdds34)
    gaddlightLateOdds1 = convert_to_hex_weight(gaddlightLateOdds1)
    gaddlightLateOdds2 = convert_to_hex_weight(gaddlightLateOdds2)
    gaddlightLateOdds34 = convert_to_hex_weight(gaddlightLateOdds34)

    # Chomp Call
    chompCallEarlyOdds1 = convert_to_hex_weight(chompCallEarlyOdds1)
    chompCallEarlyOdds2 = convert_to_hex_weight(chompCallEarlyOdds2)
    chompCallEarlyOdds34 = convert_to_hex_weight(chompCallEarlyOdds34)
    chompCallMidOdds1 = convert_to_hex_weight(chompCallMidOdds1)
    chompCallMidOdds2 = convert_to_hex_weight(chompCallMidOdds2)
    chompCallMidOdds34 = convert_to_hex_weight(chompCallMidOdds34)
    chompCallLateOdds1 = convert_to_hex_weight(chompCallLateOdds1)
    chompCallLateOdds2 = convert_to_hex_weight(chompCallLateOdds2)
    chompCallLateOdds34 = convert_to_hex_weight(chompCallLateOdds34)

    # Bowser Suit
    bowserSuitEarlyOdds1 = convert_to_hex_weight(bowserSuitEarlyOdds1)
    bowserSuitEarlyOdds2 = convert_to_hex_weight(bowserSuitEarlyOdds2)
    bowserSuitEarlyOdds34 = convert_to_hex_weight(bowserSuitEarlyOdds34)
    bowserSuitMidOdds1 = convert_to_hex_weight(bowserSuitMidOdds1)
    bowserSuitMidOdds2 = convert_to_hex_weight(bowserSuitMidOdds2)
    bowserSuitMidOdds34 = convert_to_hex_weight(bowserSuitMidOdds34)
    bowserSuitLateOdds1 = convert_to_hex_weight(bowserSuitLateOdds1)
    bowserSuitLateOdds2 = convert_to_hex_weight(bowserSuitLateOdds2)
    bowserSuitLateOdds34 = convert_to_hex_weight(bowserSuitLateOdds34)

    # Crystal Ball
    crystalBallEarlyOdds1 = convert_to_hex_weight(crystalBallEarlyOdds1)
    crystalBallEarlyOdds2 = convert_to_hex_weight(crystalBallEarlyOdds2)
    crystalBallEarlyOdds34 = convert_to_hex_weight(crystalBallEarlyOdds34)
    crystalBallMidOdds1 = convert_to_hex_weight(crystalBallMidOdds1)
    crystalBallMidOdds2 = convert_to_hex_weight(crystalBallMidOdds2)
    crystalBallMidOdds34 = convert_to_hex_weight(crystalBallMidOdds34)
    crystalBallLateOdds1 = convert_to_hex_weight(crystalBallLateOdds1)
    crystalBallLateOdds2 = convert_to_hex_weight(crystalBallLateOdds2)
    crystalBallLateOdds34 = convert_to_hex_weight(crystalBallLateOdds34)

    # Magic Lamp
    magicLampEarlyOdds1 = convert_to_hex_weight(magicLampEarlyOdds1)
    magicLampEarlyOdds2 = convert_to_hex_weight(magicLampEarlyOdds2)
    magicLampEarlyOdds34 = convert_to_hex_weight(magicLampEarlyOdds34)
    magicLampMidOdds1 = convert_to_hex_weight(magicLampMidOdds1)
    magicLampMidOdds2 = convert_to_hex_weight(magicLampMidOdds2)
    magicLampMidOdds34 = convert_to_hex_weight(magicLampMidOdds34)
    magicLampLateOdds1 = convert_to_hex_weight(magicLampLateOdds1)
    magicLampLateOdds2 = convert_to_hex_weight(magicLampLateOdds2)
    magicLampLateOdds34 = convert_to_hex_weight(magicLampLateOdds34)

    # Item Bag
    itemBagEarlyOdds1 = convert_to_hex_weight(itemBagEarlyOdds1)
    itemBagEarlyOdds2 = convert_to_hex_weight(itemBagEarlyOdds2)
    itemBagEarlyOdds34 = convert_to_hex_weight(itemBagEarlyOdds34)
    itemBagMidOdds1 = convert_to_hex_weight(itemBagMidOdds1)
    itemBagMidOdds2 = convert_to_hex_weight(itemBagMidOdds2)
    itemBagMidOdds34 = convert_to_hex_weight(itemBagMidOdds34)
    itemBagLateOdds1 = convert_to_hex_weight(itemBagLateOdds1)
    itemBagLateOdds2 = convert_to_hex_weight(itemBagLateOdds2)
    itemBagLateOdds34 = convert_to_hex_weight(itemBagLateOdds34)
    
    generatedCode = getItemShopOddsFour(miniMushroomEarlyOdds1, miniMushroomEarlyOdds2, miniMushroomEarlyOdds34, miniMushroomMidOdds1, miniMushroomMidOdds2, miniMushroomMidOdds34, miniMushroomLateOdds1, miniMushroomLateOdds2, miniMushroomLateOdds34, megaMushroomEarlyOdds1, megaMushroomEarlyOdds2, megaMushroomEarlyOdds34, megaMushroomMidOdds1, megaMushroomMidOdds2, megaMushroomMidOdds34, megaMushroomLateOdds1, megaMushroomLateOdds2, megaMushroomLateOdds34, superMiniMushroomEarlyOdds1, superMiniMushroomEarlyOdds2, superMiniMushroomEarlyOdds34, superMiniMushroomMidOdds1, superMiniMushroomMidOdds2, superMiniMushroomMidOdds34, superMiniMushroomLateOdds1, superMiniMushroomLateOdds2, superMiniMushroomLateOdds34, superMegaMushroomEarlyOdds1, superMegaMushroomEarlyOdds2, superMegaMushroomEarlyOdds34, superMegaMushroomMidOdds1, superMegaMushroomMidOdds2, superMegaMushroomMidOdds34, superMegaMushroomLateOdds1, superMegaMushroomLateOdds2, superMegaMushroomLateOdds34, miniMegaHammerEarlyOdds1, miniMegaHammerEarlyOdds2, miniMegaHammerEarlyOdds34, miniMegaHammerMidOdds1, miniMegaHammerMidOdds2, miniMegaHammerMidOdds34, miniMegaHammerLateOdds1, miniMegaHammerLateOdds2, miniMegaHammerLateOdds34, warpPipeEarlyOdds1, warpPipeEarlyOdds2, warpPipeEarlyOdds34, warpPipeMidOdds1, warpPipeMidOdds2, warpPipeMidOdds34, warpPipeLateOdds1, warpPipeLateOdds2, warpPipeLateOdds34, swapCardEarlyOdds1, swapCardEarlyOdds2, swapCardEarlyOdds34, swapCardMidOdds1, swapCardMidOdds2, swapCardMidOdds34, swapCardLateOdds1, swapCardLateOdds2, swapCardLateOdds34, sparkyStickerEarlyOdds1, sparkyStickerEarlyOdds2, sparkyStickerEarlyOdds34, sparkyStickerMidOdds1, sparkyStickerMidOdds2, sparkyStickerMidOdds34, sparkyStickerLateOdds1, sparkyStickerLateOdds2, sparkyStickerLateOdds34, gaddlightEarlyOdds1, gaddlightEarlyOdds2, gaddlightEarlyOdds34, gaddlightMidOdds1, gaddlightMidOdds2, gaddlightMidOdds34, gaddlightLateOdds1, gaddlightLateOdds2, gaddlightLateOdds34, chompCallEarlyOdds1, chompCallEarlyOdds2, chompCallEarlyOdds34, chompCallMidOdds1, chompCallMidOdds2, chompCallMidOdds34, chompCallLateOdds1, chompCallLateOdds2, chompCallLateOdds34, bowserSuitEarlyOdds1, bowserSuitEarlyOdds2, bowserSuitEarlyOdds34, bowserSuitMidOdds1, bowserSuitMidOdds2, bowserSuitMidOdds34, bowserSuitLateOdds1, bowserSuitLateOdds2, bowserSuitLateOdds34, crystalBallEarlyOdds1, crystalBallEarlyOdds2, crystalBallEarlyOdds34, crystalBallMidOdds1, crystalBallMidOdds2, crystalBallMidOdds34, crystalBallLateOdds1, crystalBallLateOdds2, crystalBallLateOdds34, magicLampEarlyOdds1, magicLampEarlyOdds2, magicLampEarlyOdds34, magicLampMidOdds1, magicLampMidOdds2, magicLampMidOdds34, magicLampLateOdds1, magicLampLateOdds2, magicLampLateOdds34, itemBagEarlyOdds1, itemBagEarlyOdds2, itemBagEarlyOdds34, itemBagMidOdds1, itemBagMidOdds2, itemBagMidOdds34, itemBagLateOdds1, itemBagLateOdds2, itemBagLateOdds34)
    generatedCode = generatedCode.strip()
    pyperclip.copy(generatedCode)

    print("Generated code copied to the clipboard.")
    createDialog("Operation Sucessful", "success", "Generated codes copied to clipboard!.", None)