# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 5/9/2024
# License: MIT
# ============================================

def getRedSpaceCodeFour(amount, amountDec):
    return f'''
MP4 - Red Spaces Take Away {amountDec} Coins
C207FD5C 00000001
3BC0{amount} 00000000
'''

def getBlueSpaceCodeFour(amount, amountDec):
    return f'''
MP4 - Blue Spaces Give {amountDec} Coins
C207FBC4 00000001
3BC0{amount} 00000000
'''

def getMinigameCodeFour(amount, amountDec):
    return f'''
MP4 - Minigames Award {amountDec} Coins
2A18FD2C 00000003
2A18FD2C 00000007
2A18FD2C 00000015
2A18FD2C 0000001D
2A18FD2C 00000025
2A18FD2C 00000026
2A18FD2C 00000027
2A18FD2C 00000028
2A18FD2C 00000036
2818FC60 0000000A
0218FC60 0000{amount}
E0000000 80008000
2A18FD2C 00000003
2A18FD2C 00000007
2A18FD2C 00000015
2A18FD2C 0000001D
2A18FD2C 00000025
2A18FD2C 00000026
2A18FD2C 00000027
2A18FD2C 00000028
2A18FD2C 00000036
2818FC90 0000000A
0218FC90 0000{amount}
E0000000 80008000
2A18FD2C 00000003
2A18FD2C 00000007
2A18FD2C 00000015
2A18FD2C 0000001D
2A18FD2C 00000025
2A18FD2C 00000026
2A18FD2C 00000027
2A18FD2C 00000028
2A18FD2C 00000036
2818FCC0 0000000A
0218FCC0 0000{amount}
E0000000 80008000
2A18FD2C 00000003
2A18FD2C 00000007
2A18FD2C 00000015
2A18FD2C 0000001D
2A18FD2C 00000025
2A18FD2C 00000026
2A18FD2C 00000027
2A18FD2C 00000028
2A18FD2C 00000036
2818FCF0 0000000A
0218FCF0 0000{amount}
E0000000 80008000
'''

def getBooSpaceStarFour(amount, amountDec):
    return f'''
MP4 - Star Stealing Costs {amountDec} at the Boo House.
C20A5F30 00000001
2C1E{amount} 00000000
'''

def getBooSpaceCoinsFour(amount, amountDec):
    return f'''
MP4 - Coin Stealing Costs {amountDec} at the Boo House.
C20A61DC 00000001
2C1E{amount} 00000000
C20A517C 00000001
2C03{amount} 00000000
'''

def getStarSpaceCodeFour(amount, amountDec):
    return f'''
MP4 - Stars Cost {amountDec} Coins
C20843CC 00000001
2C03{amount} 00000000
C2084590 00000001
2C03{amount} 00000000
C20845CC 00000001
2C03{amount} 00000000
C208473C 00000001
2C1C{amount} 00000000
'''

def getSquishCodeFour(amount, amountDec):
    return f'''
MP4 - Mega Mushroom Steals {amountDec} Coins
C206BE88 00000001
2C00{amount} 00000000
C206BE90 00000001
3800{amount} 00000000
'''

def getBowserSuitCodeFour(amount, amountDec):
    return f'''
MP4 - Bowser Suit Steals {amountDec} Coins
C206C788 00000001
2C00{amount} 00000000
C206C790 00000001
3800{amount} 00000000
'''

def getLotterySpaceCodeFour(amount, amountDec):
    return f'''
MP4 - Lottery Costs {amountDec} Coins
C207BD20 00000001
2C1E{amount} 00000000
'''

def getMinigameReplacement4(hexUno, hexDos, gameUno, gameDos):
    return f'''
MP4 - Minigame Replacement: {gameUno} ➜ {gameDos}
2818FD2C 000000{hexUno}
0218FD2C 000000{hexDos}
E2000001 80008000
'''

def getBooHouseMinimum(min, minDec):
    return f'''
MP4 - Steal Minimum of {minDec} Coins from Boo
C20A19CC 00000003
7C1D0000 4181000C
7C1D0378 3BBD0001
7C00E850 00000000
040A19B0 3BA0{min}
'''

def getInitialItemsFour(one, two, three, oneItem, twoItem, threeItem):
    return f'''
MP4 - Start with {oneItem}, {twoItem}, and {threeItem}
C2063AE0 00000013
7C83032E 2C040007
40820080 3DC08018
61CEFCFC 89CE0000
2C0E0001 4082006C
3DC08018 61CEFC3D
39E000{one} 99EE0000
39E000{two} 99EE0001
39E000{three} 99EE0002
39E000{one} 99EE0030
39E000{two} 99EE0031
39E000{three} 99EE0032
39E000{one} 99EE0060
39E000{two} 99EE0061
39E000{three} 99EE0062
39E000{one} 99EE0090
39E000{two} 99EE0091
39E000{three} 99EE0092
39C00000 39E00000
60000000 00000000
'''

def getSpaceReplaceFour1(spaceHex1, spaceHex2, spaceName, spaceName2):
    return f'''
MP4 - Replace {spaceName} with {spaceName2} (Slot A)
C2076A08 00000003
A01F0028 280000{spaceHex1}
4082000C 380000{spaceHex2}
B01F0028 00000000
'''

def getSpaceReplaceFour2(spaceHex1, spaceHex2, spaceName, spaceName2):
    return f'''
MP4 - Replace {spaceName} with {spaceName2} (Slot B)
C2076A0C 00000003
280000{spaceHex1} 4082000C
380000{spaceHex2} B01F0028
28000000 00000000
'''

def getLotteryRewards4(lotteryPrizeA, lotteryPrizeB, lotteryPrizeC, lotteryPrizeD, lotteryPrizeALabel, lotteryPrizeBLabel, lotteryPrizeCLabel, lotteryPrizeDLabel):
    return f'''
MP4 - Lottery 1st is {lotteryPrizeALabel} - 2nd is {lotteryPrizeBLabel} - 3rd is {lotteryPrizeCLabel} or {lotteryPrizeDLabel}
C207EA58 00000001
3B80{lotteryPrizeA} 00000000
C207EA60 00000001
3B80{lotteryPrizeB} 00000000
021D5678 0000{lotteryPrizeC}{lotteryPrizeD}
'''

def getStarHandicap(p1, p2, p3, p4):
    return f'''
MP4 - Star Handicap
C2063AE4 0000000B
7C83032E 2C040007
40820040 3DC08018
61CEFCFC 89CE0000
2C0E0001 4082002C
3DC08018 61CEFC63
39E0{p1} 99EE0000
39E0{p2} 99EE0030
39E0{p3} 99EE0060
39E0{p4} 99EE0090
39C00000 39E00000
60000000 00000000
'''

def initialCoinsMod4(hex, hexDec):
    return f'''
MP4 - Gain {hexDec} Coins at the Start of the Game
C20A8F0C 00000001
3AC0{hex} 00000000
'''

def getBattleGame4(p1, p2, p3, p4, p5, s1, s2, s3, s4, s5):
    return f'''
MP4 - Battle Minigames Bounties are {s1}, {s2}, {s3}, {s4}, and {s5}
041D5DE0 {p1}{p2}{p3}{p4}
041D5DE4 {p5}000000
'''


def getItemShopPricesFourDX(minCoins, miniMushroomEarlyPrice1, miniMushroomEarlyPrice2, miniMushroomEarlyPrice34, miniMushroomMidPrice1, miniMushroomMidPrice2, miniMushroomMidPrice34, miniMushroomLatePrice1, miniMushroomLatePrice2, miniMushroomLatePrice34, megaMushroomEarlyPrice1, megaMushroomEarlyPrice2, megaMushroomEarlyPrice34, megaMushroomMidPrice1, megaMushroomMidPrice2, megaMushroomMidPrice34, megaMushroomLatePrice1, megaMushroomLatePrice2, megaMushroomLatePrice34, superMiniMushroomEarlyPrice1, superMiniMushroomEarlyPrice2, superMiniMushroomEarlyPrice34, superMiniMushroomMidPrice1, superMiniMushroomMidPrice2, superMiniMushroomMidPrice34, superMiniMushroomLatePrice1, superMiniMushroomLatePrice2, superMiniMushroomLatePrice34, superMegaMushroomEarlyPrice1, superMegaMushroomEarlyPrice2, superMegaMushroomEarlyPrice34, superMegaMushroomMidPrice1, superMegaMushroomMidPrice2, superMegaMushroomMidPrice34, superMegaMushroomLatePrice1, superMegaMushroomLatePrice2, superMegaMushroomLatePrice34, miniMegaHammerEarlyPrice1, miniMegaHammerEarlyPrice2, miniMegaHammerEarlyPrice34, miniMegaHammerMidPrice1, miniMegaHammerMidPrice2, miniMegaHammerMidPrice34, miniMegaHammerLatePrice1, miniMegaHammerLatePrice2, miniMegaHammerLatePrice34, warpPipeEarlyPrice1, warpPipeEarlyPrice2, warpPipeEarlyPrice34, warpPipeMidPrice1, warpPipeMidPrice2, warpPipeMidPrice34, warpPipeLatePrice1, warpPipeLatePrice2, warpPipeLatePrice34, swapCardEarlyPrice1, swapCardEarlyPrice2, swapCardEarlyPrice34, swapCardMidPrice1, swapCardMidPrice2, swapCardMidPrice34, swapCardLatePrice1, swapCardLatePrice2, swapCardLatePrice34, sparkyStickerEarlyPrice1, sparkyStickerEarlyPrice2, sparkyStickerEarlyPrice34, sparkyStickerMidPrice1, sparkyStickerMidPrice2, sparkyStickerMidPrice34, sparkyStickerLatePrice1, sparkyStickerLatePrice2, sparkyStickerLatePrice34, gaddlightEarlyPrice1, gaddlightEarlyPrice2, gaddlightEarlyPrice34, gaddlightMidPrice1, gaddlightMidPrice2, gaddlightMidPrice34, gaddlightLatePrice1, gaddlightLatePrice2, gaddlightLatePrice34, chompCallEarlyPrice1, chompCallEarlyPrice2, chompCallEarlyPrice34, chompCallMidPrice1, chompCallMidPrice2, chompCallMidPrice34, chompCallLatePrice1, chompCallLatePrice2, chompCallLatePrice34, bowserSuitEarlyPrice1, bowserSuitEarlyPrice2, bowserSuitEarlyPrice34, bowserSuitMidPrice1, bowserSuitMidPrice2, bowserSuitMidPrice34, bowserSuitLatePrice1, bowserSuitLatePrice2, bowserSuitLatePrice34, crystalBallEarlyPrice1, crystalBallEarlyPrice2, crystalBallEarlyPrice34, crystalBallMidPrice1, crystalBallMidPrice2, crystalBallMidPrice34, crystalBallLatePrice1, crystalBallLatePrice2, crystalBallLatePrice34, magicLampEarlyPrice1, magicLampEarlyPrice2, magicLampEarlyPrice34, magicLampMidPrice1, magicLampMidPrice2, magicLampMidPrice34, magicLampLatePrice1, magicLampLatePrice2, magicLampLatePrice34, itemBagEarlyPrice1, itemBagEarlyPrice2, itemBagEarlyPrice34, itemBagMidPrice1, itemBagMidPrice2, itemBagMidPrice34, itemBagLatePrice1, itemBagLatePrice2, itemBagLatePrice34, mushroomEarlyPrice1, mushroomEarlyPrice2, mushroomEarlyPrice34, mushroomMidPrice1, mushroomMidPrice2, mushroomMidPrice34, mushroomLatePrice1, mushroomLatePrice2, mushroomLatePrice34, goldenMushroomEarlyPrice1, goldenMushroomEarlyPrice2, goldenMushroomEarlyPrice34, goldenMushroomMidPrice1, goldenMushroomMidPrice2, goldenMushroomMidPrice34, goldenMushroomLatePrice1, goldenMushroomLatePrice2, goldenMushroomLatePrice34, reverseMushroomEarlyPrice1, reverseMushroomEarlyPrice2, reverseMushroomEarlyPrice34, reverseMushroomMidPrice1, reverseMushroomMidPrice2, reverseMushroomMidPrice34, reverseMushroomLatePrice1, reverseMushroomLatePrice2, reverseMushroomLatePrice34, poisonMushroomEarlyPrice1, poisonMushroomEarlyPrice2, poisonMushroomEarlyPrice34, poisonMushroomMidPrice1, poisonMushroomMidPrice2, poisonMushroomMidPrice34, poisonMushroomLatePrice1, poisonMushroomLatePrice2, poisonMushroomLatePrice34, triplePoisonMushroomEarlyPrice1, triplePoisonMushroomEarlyPrice2, triplePoisonMushroomEarlyPrice34, triplePoisonMushroomMidPrice1, triplePoisonMushroomMidPrice2, triplePoisonMushroomMidPrice34, triplePoisonMushroomLatePrice1, triplePoisonMushroomLatePrice2, triplePoisonMushroomLatePrice34, celluarShopperEarlyPrice1, celluarShopperEarlyPrice2, celluarShopperEarlyPrice34, celluarShopperMidPrice1, celluarShopperMidPrice2, celluarShopperMidPrice34, celluarShopperLatePrice1, celluarShopperLatePrice2, celluarShopperLatePrice34, skeletonKeyEarlyPrice1, skeletonKeyEarlyPrice2, skeletonKeyEarlyPrice34, skeletonKeyMidPrice1, skeletonKeyMidPrice2, skeletonKeyMidPrice34, skeletonKeyLatePrice1, skeletonKeyLatePrice2, skeletonKeyLatePrice34, plunderChestEarlyPrice1, plunderChestEarlyPrice2, plunderChestEarlyPrice34, plunderChestMidPrice1, plunderChestMidPrice2, plunderChestMidPrice34, plunderChestLatePrice1, plunderChestLatePrice2, plunderChestLatePrice34, gaddbrushEarlyPrice1, gaddbrushEarlyPrice2, gaddbrushEarlyPrice34, gaddbrushMidPrice1, gaddbrushMidPrice2, gaddbrushMidPrice34, gaddbrushLatePrice1, gaddbrushLatePrice2, gaddbrushLatePrice34, warpBlockEarlyPrice1, warpBlockEarlyPrice2, warpBlockEarlyPrice34, warpBlockMidPrice1, warpBlockMidPrice2, warpBlockMidPrice34, warpBlockLatePrice1, warpBlockLatePrice2, warpBlockLatePrice34, flyGuyEarlyPrice1, flyGuyEarlyPrice2, flyGuyEarlyPrice34, flyGuyMidPrice1, flyGuyMidPrice2, flyGuyMidPrice34, flyGuyLatePrice1, flyGuyLatePrice2, flyGuyLatePrice34, plusBlockEarlyPrice1, plusBlockEarlyPrice2, plusBlockEarlyPrice34, plusBlockMidPrice1, plusBlockMidPrice2, plusBlockMidPrice34, plusBlockLatePrice1, plusBlockLatePrice2, plusBlockLatePrice34, minusBlockEarlyPrice1, minusBlockEarlyPrice2, minusBlockEarlyPrice34, minusBlockMidPrice1, minusBlockMidPrice2, minusBlockMidPrice34, minusBlockLatePrice1, minusBlockLatePrice2, minusBlockLatePrice34, speedBlockEarlyPrice1, speedBlockEarlyPrice2, speedBlockEarlyPrice34, speedBlockMidPrice1, speedBlockMidPrice2, speedBlockMidPrice34, speedBlockLatePrice1, speedBlockLatePrice2, speedBlockLatePrice34, slowBlockEarlyPrice1, slowBlockEarlyPrice2, slowBlockEarlyPrice34, slowBlockMidPrice1, slowBlockMidPrice2, slowBlockMidPrice34, slowBlockLatePrice1, slowBlockLatePrice2, slowBlockLatePrice34, bowserPhoneEarlyPrice1, bowserPhoneEarlyPrice2, bowserPhoneEarlyPrice34, bowserPhoneMidPrice1, bowserPhoneMidPrice2, bowserPhoneMidPrice34, bowserPhoneLatePrice1, bowserPhoneLatePrice2, bowserPhoneLatePrice34, doubleDipEarlyPrice1, doubleDipEarlyPrice2, doubleDipEarlyPrice34, doubleDipMidPrice1, doubleDipMidPrice2, doubleDipMidPrice34, doubleDipLatePrice1, doubleDipLatePrice2, doubleDipLatePrice34, hiddenBlockCardEarlyPrice1, hiddenBlockCardEarlyPrice2, hiddenBlockCardEarlyPrice34, hiddenBlockCardMidPrice1, hiddenBlockCardMidPrice2, hiddenBlockCardMidPrice34, hiddenBlockCardLatePrice1, hiddenBlockCardLatePrice2, hiddenBlockCardLatePrice34, barterBoxEarlyPrice1, barterBoxEarlyPrice2, barterBoxEarlyPrice34, barterBoxMidPrice1, barterBoxMidPrice2, barterBoxMidPrice34, barterBoxLatePrice1, barterBoxLatePrice2, barterBoxLatePrice34, superWarpPipeEarlyPrice1, superWarpPipeEarlyPrice2, superWarpPipeEarlyPrice34, superWarpPipeMidPrice1, superWarpPipeMidPrice2, superWarpPipeMidPrice34, superWarpPipeLatePrice1, superWarpPipeLatePrice2, superWarpPipeLatePrice34, chanceTimeCharmEarlyPrice1, chanceTimeCharmEarlyPrice2, chanceTimeCharmEarlyPrice34, chanceTimeCharmMidPrice1, chanceTimeCharmMidPrice2, chanceTimeCharmMidPrice34, chanceTimeCharmLatePrice1, chanceTimeCharmLatePrice2, chanceTimeCharmLatePrice34, wackyWatchEarlyPrice1, wackyWatchEarlyPrice2, wackyWatchEarlyPrice34, wackyWatchMidPrice1, wackyWatchMidPrice2, wackyWatchMidPrice34, wackyWatchLatePrice1, wackyWatchLatePrice2, wackyWatchLatePrice34):
    return f'''
MP4DX - Item Modifer
C2077D84 00000001
2C0300{minCoins} 00000000
20071C98 00000000
04071F08 {miniMushroomEarlyPrice1}{megaMushroomEarlyPrice1}{superMiniMushroomEarlyPrice1}{superMegaMushroomEarlyPrice1}
04071F0C {miniMegaHammerEarlyPrice1}{warpPipeEarlyPrice1}{swapCardEarlyPrice1}{sparkyStickerEarlyPrice1}
04071F10 {gaddlightEarlyPrice1}{chompCallEarlyPrice1}{bowserSuitEarlyPrice1}{crystalBallEarlyPrice1}
04071F14 {magicLampEarlyPrice1}{itemBagEarlyPrice1}{bowserPhoneEarlyPrice1}{mushroomEarlyPrice1}
04071F18 {goldenMushroomEarlyPrice1}{hiddenBlockCardEarlyPrice1}{celluarShopperEarlyPrice1}{barterBoxEarlyPrice1}
04071F1C {superWarpPipeEarlyPrice1}{chanceTimeCharmEarlyPrice1}{wackyWatchEarlyPrice1}{plunderChestEarlyPrice1}
04071F20 {gaddbrushEarlyPrice1}{skeletonKeyEarlyPrice1}{warpBlockEarlyPrice1}{flyGuyEarlyPrice1}
04071F24 {plusBlockEarlyPrice1}{minusBlockEarlyPrice1}{speedBlockEarlyPrice1}{slowBlockEarlyPrice1}
04071F28 {poisonMushroomEarlyPrice1}{triplePoisonMushroomEarlyPrice1}{doubleDipEarlyPrice1}{reverseMushroomEarlyPrice1}
E0000000 80008000
20071C98 00000001
04071F08 {miniMushroomEarlyPrice2}{megaMushroomEarlyPrice2}{superMiniMushroomEarlyPrice2}{superMegaMushroomEarlyPrice2}
04071F0C {miniMegaHammerEarlyPrice2}{warpPipeEarlyPrice2}{swapCardEarlyPrice2}{sparkyStickerEarlyPrice2}
04071F10 {gaddlightEarlyPrice2}{chompCallEarlyPrice2}{bowserSuitEarlyPrice2}{crystalBallEarlyPrice2}
04071F14 {magicLampEarlyPrice2}{itemBagEarlyPrice2}{bowserPhoneEarlyPrice2}{mushroomEarlyPrice2}
04071F18 {goldenMushroomEarlyPrice2}{hiddenBlockCardEarlyPrice2}{celluarShopperEarlyPrice2}{barterBoxEarlyPrice2}
04071F1C {superWarpPipeEarlyPrice2}{chanceTimeCharmEarlyPrice2}{wackyWatchEarlyPrice2}{plunderChestEarlyPrice2}
04071F20 {gaddbrushEarlyPrice2}{skeletonKeyEarlyPrice2}{warpBlockEarlyPrice2}{flyGuyEarlyPrice2}
04071F24 {plusBlockEarlyPrice2}{minusBlockEarlyPrice2}{speedBlockEarlyPrice2}{slowBlockEarlyPrice2}
04071F28 {poisonMushroomEarlyPrice2}{triplePoisonMushroomEarlyPrice2}{doubleDipEarlyPrice2}{reverseMushroomEarlyPrice2}
E0000000 80008000
20071C98 00000002
04071F08 {miniMushroomEarlyPrice34}{megaMushroomEarlyPrice34}{superMiniMushroomEarlyPrice34}{superMegaMushroomEarlyPrice34}
04071F0C {miniMegaHammerEarlyPrice34}{warpPipeEarlyPrice34}{swapCardEarlyPrice34}{sparkyStickerEarlyPrice34}
04071F10 {gaddlightEarlyPrice34}{chompCallEarlyPrice34}{bowserSuitEarlyPrice34}{crystalBallEarlyPrice34}
04071F14 {magicLampEarlyPrice34}{itemBagEarlyPrice34}{bowserPhoneEarlyPrice34}{mushroomEarlyPrice34}
04071F18 {goldenMushroomEarlyPrice34}{hiddenBlockCardEarlyPrice34}{celluarShopperEarlyPrice34}{barterBoxEarlyPrice34}
04071F1C {superWarpPipeEarlyPrice34}{chanceTimeCharmEarlyPrice34}{wackyWatchEarlyPrice34}{plunderChestEarlyPrice34}
04071F20 {gaddbrushEarlyPrice34}{skeletonKeyEarlyPrice34}{warpBlockEarlyPrice34}{flyGuyEarlyPrice34}
04071F24 {plusBlockEarlyPrice34}{minusBlockEarlyPrice34}{speedBlockEarlyPrice34}{slowBlockEarlyPrice34}
04071F28 {poisonMushroomEarlyPrice34}{triplePoisonMushroomEarlyPrice34}{doubleDipEarlyPrice34}{reverseMushroomEarlyPrice34}
E0000000 80008000
20071C98 00010000
04071F08 {miniMushroomMidPrice1}{megaMushroomMidPrice1}{superMiniMushroomMidPrice1}{superMegaMushroomMidPrice1}
04071F0C {miniMegaHammerMidPrice1}{warpPipeMidPrice1}{swapCardMidPrice1}{sparkyStickerMidPrice1}
04071F10 {gaddlightMidPrice1}{chompCallMidPrice1}{bowserSuitMidPrice1}{crystalBallMidPrice1}
04071F14 {magicLampMidPrice1}{itemBagMidPrice1}{bowserPhoneMidPrice1}{mushroomMidPrice1}
04071F18 {goldenMushroomMidPrice1}{hiddenBlockCardMidPrice1}{celluarShopperMidPrice1}{barterBoxMidPrice1}
04071F1C {superWarpPipeMidPrice1}{chanceTimeCharmMidPrice1}{wackyWatchMidPrice1}{plunderChestMidPrice1}
04071F20 {gaddbrushMidPrice1}{skeletonKeyMidPrice1}{warpBlockMidPrice1}{flyGuyMidPrice1}
04071F24 {plusBlockMidPrice1}{minusBlockMidPrice1}{speedBlockMidPrice1}{slowBlockMidPrice1}
04071F28 {poisonMushroomMidPrice1}{triplePoisonMushroomMidPrice1}{doubleDipMidPrice1}{reverseMushroomMidPrice1}
E0000000 80008000
20071C98 00010001
04071F08 {miniMushroomMidPrice2}{megaMushroomMidPrice2}{superMiniMushroomMidPrice2}{superMegaMushroomMidPrice2}
04071F0C {miniMegaHammerMidPrice2}{warpPipeMidPrice2}{swapCardMidPrice2}{sparkyStickerMidPrice2}
04071F10 {gaddlightMidPrice2}{chompCallMidPrice2}{bowserSuitMidPrice2}{crystalBallMidPrice2}
04071F14 {magicLampMidPrice2}{itemBagMidPrice2}{bowserPhoneMidPrice2}{mushroomMidPrice2}
04071F18 {goldenMushroomMidPrice2}{hiddenBlockCardMidPrice2}{celluarShopperMidPrice2}{barterBoxMidPrice2}
04071F1C {superWarpPipeMidPrice2}{chanceTimeCharmMidPrice2}{wackyWatchMidPrice2}{plunderChestMidPrice2}
04071F20 {gaddbrushMidPrice2}{skeletonKeyMidPrice2}{warpBlockMidPrice2}{flyGuyMidPrice2}
04071F24 {plusBlockMidPrice2}{minusBlockMidPrice2}{speedBlockMidPrice2}{slowBlockMidPrice2}
04071F28 {poisonMushroomMidPrice2}{triplePoisonMushroomMidPrice2}{doubleDipMidPrice2}{reverseMushroomMidPrice2}
E0000000 80008000
20071C98 00010002
04071F08 {miniMushroomMidPrice34}{megaMushroomMidPrice34}{superMiniMushroomMidPrice34}{superMegaMushroomMidPrice34}
04071F0C {miniMegaHammerMidPrice34}{warpPipeMidPrice34}{swapCardMidPrice34}{sparkyStickerMidPrice34}
04071F10 {gaddlightMidPrice34}{chompCallMidPrice34}{bowserSuitMidPrice34}{crystalBallMidPrice34}
04071F14 {magicLampMidPrice34}{itemBagMidPrice34}{bowserPhoneMidPrice34}{mushroomMidPrice34}
04071F18 {goldenMushroomMidPrice34}{hiddenBlockCardMidPrice34}{celluarShopperMidPrice34}{barterBoxMidPrice34}
04071F1C {superWarpPipeMidPrice34}{chanceTimeCharmMidPrice34}{wackyWatchMidPrice34}{plunderChestMidPrice34}
04071F20 {gaddbrushMidPrice34}{skeletonKeyMidPrice34}{warpBlockMidPrice34}{flyGuyMidPrice34}
04071F24 {plusBlockMidPrice34}{minusBlockMidPrice34}{speedBlockMidPrice34}{slowBlockMidPrice34}
04071F28 {poisonMushroomMidPrice34}{triplePoisonMushroomMidPrice34}{doubleDipMidPrice34}{reverseMushroomMidPrice34}
E0000000 80008000
2C071C98 00000001
28071C9A 00000000
04071F08 {miniMushroomLatePrice1}{megaMushroomLatePrice1}{superMiniMushroomLatePrice1}{superMegaMushroomLatePrice1}
04071F0C {miniMegaHammerLatePrice1}{warpPipeLatePrice1}{swapCardLatePrice1}{sparkyStickerLatePrice1}
04071F10 {gaddlightLatePrice1}{chompCallLatePrice1}{bowserSuitLatePrice1}{crystalBallLatePrice1}
04071F14 {magicLampLatePrice1}{itemBagLatePrice1}{bowserPhoneLatePrice1}{mushroomLatePrice1}
04071F18 {goldenMushroomLatePrice1}{hiddenBlockCardLatePrice1}{celluarShopperLatePrice1}{barterBoxLatePrice1}
04071F1C {superWarpPipeLatePrice1}{chanceTimeCharmLatePrice1}{wackyWatchLatePrice1}{plunderChestLatePrice1}
04071F20 {gaddbrushLatePrice1}{skeletonKeyLatePrice1}{warpBlockLatePrice1}{flyGuyLatePrice1}
04071F24 {plusBlockLatePrice1}{minusBlockLatePrice1}{speedBlockLatePrice1}{slowBlockLatePrice1}
04071F28 {poisonMushroomLatePrice1}{triplePoisonMushroomLatePrice1}{doubleDipLatePrice1}{reverseMushroomLatePrice1}
E2000001 80008000
28071C9A 00000001
04071F08 {miniMushroomLatePrice2}{megaMushroomLatePrice2}{superMiniMushroomLatePrice2}{superMegaMushroomLatePrice2}
04071F0C {miniMegaHammerLatePrice2}{warpPipeLatePrice2}{swapCardLatePrice2}{sparkyStickerLatePrice2}
04071F10 {gaddlightLatePrice2}{chompCallLatePrice2}{bowserSuitLatePrice2}{crystalBallLatePrice2}
04071F14 {magicLampLatePrice2}{itemBagLatePrice2}{bowserPhoneLatePrice2}{mushroomLatePrice2}
04071F18 {goldenMushroomLatePrice2}{hiddenBlockCardLatePrice2}{celluarShopperLatePrice2}{barterBoxLatePrice2}
04071F1C {superWarpPipeLatePrice2}{chanceTimeCharmLatePrice2}{wackyWatchLatePrice2}{plunderChestLatePrice2}
04071F20 {gaddbrushLatePrice2}{skeletonKeyLatePrice2}{warpBlockLatePrice2}{flyGuyLatePrice2}
04071F24 {plusBlockLatePrice2}{minusBlockLatePrice2}{speedBlockLatePrice2}{slowBlockLatePrice2}
04071F28 {poisonMushroomLatePrice2}{triplePoisonMushroomLatePrice2}{doubleDipLatePrice2}{reverseMushroomLatePrice2}
E2000001 80008000
28071C9A 00000002
04071F08 {miniMushroomLatePrice34}{megaMushroomLatePrice34}{superMiniMushroomLatePrice34}{superMegaMushroomLatePrice34}
04071F0C {miniMegaHammerLatePrice34}{warpPipeLatePrice34}{swapCardLatePrice34}{sparkyStickerLatePrice34}
04071F10 {gaddlightLatePrice34}{chompCallLatePrice34}{bowserSuitLatePrice34}{crystalBallLatePrice34}
04071F14 {magicLampLatePrice34}{itemBagLatePrice34}{bowserPhoneLatePrice34}{mushroomLatePrice34}
04071F18 {goldenMushroomLatePrice34}{hiddenBlockCardLatePrice34}{celluarShopperLatePrice34}{barterBoxLatePrice34}
04071F1C {superWarpPipeLatePrice34}{chanceTimeCharmLatePrice34}{wackyWatchLatePrice34}{plunderChestLatePrice34}
04071F20 {gaddbrushLatePrice34}{skeletonKeyLatePrice34}{warpBlockLatePrice34}{flyGuyLatePrice34}
04071F24 {plusBlockLatePrice34}{minusBlockLatePrice34}{speedBlockLatePrice34}{slowBlockLatePrice34}
04071F28 {poisonMushroomLatePrice34}{triplePoisonMushroomLatePrice34}{doubleDipLatePrice34}{reverseMushroomLatePrice34}
E0000000 80008000
'''

def getItemShopPricesFour(minCoins, miniMushroomEarlyPrice1, miniMushroomEarlyPrice2, miniMushroomEarlyPrice34, miniMushroomMidPrice1, miniMushroomMidPrice2, miniMushroomMidPrice34, miniMushroomLatePrice1, miniMushroomLatePrice2, miniMushroomLatePrice34, megaMushroomEarlyPrice1, megaMushroomEarlyPrice2, megaMushroomEarlyPrice34, megaMushroomMidPrice1, megaMushroomMidPrice2, megaMushroomMidPrice34, megaMushroomLatePrice1, megaMushroomLatePrice2, megaMushroomLatePrice34, superMiniMushroomEarlyPrice1, superMiniMushroomEarlyPrice2, superMiniMushroomEarlyPrice34, superMiniMushroomMidPrice1, superMiniMushroomMidPrice2, superMiniMushroomMidPrice34, superMiniMushroomLatePrice1, superMiniMushroomLatePrice2, superMiniMushroomLatePrice34, superMegaMushroomEarlyPrice1, superMegaMushroomEarlyPrice2, superMegaMushroomEarlyPrice34, superMegaMushroomMidPrice1, superMegaMushroomMidPrice2, superMegaMushroomMidPrice34, superMegaMushroomLatePrice1, superMegaMushroomLatePrice2, superMegaMushroomLatePrice34, miniMegaHammerEarlyPrice1, miniMegaHammerEarlyPrice2, miniMegaHammerEarlyPrice34, miniMegaHammerMidPrice1, miniMegaHammerMidPrice2, miniMegaHammerMidPrice34, miniMegaHammerLatePrice1, miniMegaHammerLatePrice2, miniMegaHammerLatePrice34, warpPipeEarlyPrice1, warpPipeEarlyPrice2, warpPipeEarlyPrice34, warpPipeMidPrice1, warpPipeMidPrice2, warpPipeMidPrice34, warpPipeLatePrice1, warpPipeLatePrice2, warpPipeLatePrice34, swapCardEarlyPrice1, swapCardEarlyPrice2, swapCardEarlyPrice34, swapCardMidPrice1, swapCardMidPrice2, swapCardMidPrice34, swapCardLatePrice1, swapCardLatePrice2, swapCardLatePrice34, sparkyStickerEarlyPrice1, sparkyStickerEarlyPrice2, sparkyStickerEarlyPrice34, sparkyStickerMidPrice1, sparkyStickerMidPrice2, sparkyStickerMidPrice34, sparkyStickerLatePrice1, sparkyStickerLatePrice2, sparkyStickerLatePrice34, gaddlightEarlyPrice1, gaddlightEarlyPrice2, gaddlightEarlyPrice34, gaddlightMidPrice1, gaddlightMidPrice2, gaddlightMidPrice34, gaddlightLatePrice1, gaddlightLatePrice2, gaddlightLatePrice34, chompCallEarlyPrice1, chompCallEarlyPrice2, chompCallEarlyPrice34, chompCallMidPrice1, chompCallMidPrice2, chompCallMidPrice34, chompCallLatePrice1, chompCallLatePrice2, chompCallLatePrice34, bowserSuitEarlyPrice1, bowserSuitEarlyPrice2, bowserSuitEarlyPrice34, bowserSuitMidPrice1, bowserSuitMidPrice2, bowserSuitMidPrice34, bowserSuitLatePrice1, bowserSuitLatePrice2, bowserSuitLatePrice34, crystalBallEarlyPrice1, crystalBallEarlyPrice2, crystalBallEarlyPrice34, crystalBallMidPrice1, crystalBallMidPrice2, crystalBallMidPrice34, crystalBallLatePrice1, crystalBallLatePrice2, crystalBallLatePrice34, magicLampEarlyPrice1, magicLampEarlyPrice2, magicLampEarlyPrice34, magicLampMidPrice1, magicLampMidPrice2, magicLampMidPrice34, magicLampLatePrice1, magicLampLatePrice2, magicLampLatePrice34, itemBagEarlyPrice1, itemBagEarlyPrice2, itemBagEarlyPrice34, itemBagMidPrice1, itemBagMidPrice2, itemBagMidPrice34, itemBagLatePrice1, itemBagLatePrice2, itemBagLatePrice34):
    return f'''
MP4 - Item Modifier
C2086480 00000013
80640000 3DE08018
61EFFD02 89EF0000
1DEF0030 3C808018
6084FC38 7C847A14
88840009 70840060
5484D97E 3DE08018
61EFFD62 B08F0000
3DC08018 61CEFCFC
888E0001 89CE0000
39C00003 7C8473D6
3DC08018 61CEFCFC
89CE0000 39E00000
7C0E2000 40810018
39E00001 1C840002
7C0E2000 40810008
39E00002 3C808018
6084FD72 B1E40000
39C00000 39E00000
60000000 00000000
C2077D84 00000001
2C0300{minCoins} 00000000
2818FD62 00000000
2818FD72 00000000
04139D2C {miniMushroomEarlyPrice1}{megaMushroomEarlyPrice1}{superMiniMushroomEarlyPrice1}{superMegaMushroomEarlyPrice1}
04139D30 {miniMegaHammerEarlyPrice1}{warpPipeEarlyPrice1}{swapCardEarlyPrice1}{sparkyStickerEarlyPrice1}
04139D34 {gaddlightEarlyPrice1}{chompCallEarlyPrice1}{bowserSuitEarlyPrice1}{crystalBallEarlyPrice1}
02139D38 0000{magicLampEarlyPrice1}{itemBagEarlyPrice1}
E2000001 80008000
2818FD72 00000001
04139D2C {miniMushroomEarlyPrice2}{megaMushroomEarlyPrice2}{superMiniMushroomEarlyPrice2}{superMegaMushroomEarlyPrice2}
04139D30 {miniMegaHammerEarlyPrice2}{warpPipeEarlyPrice2}{swapCardEarlyPrice2}{sparkyStickerEarlyPrice2}
04139D34 {gaddlightEarlyPrice2}{chompCallEarlyPrice2}{bowserSuitEarlyPrice2}{crystalBallEarlyPrice2}
02139D38 0000{magicLampEarlyPrice2}{itemBagEarlyPrice2}
E2000001 80008000
2818FD72 00000002
04139D2C {miniMushroomEarlyPrice34}{megaMushroomEarlyPrice34}{superMiniMushroomEarlyPrice34}{superMegaMushroomEarlyPrice34}
04139D30 {miniMegaHammerEarlyPrice34}{warpPipeEarlyPrice34}{swapCardEarlyPrice34}{sparkyStickerEarlyPrice34}
04139D34 {gaddlightEarlyPrice34}{chompCallEarlyPrice34}{bowserSuitEarlyPrice34}{crystalBallEarlyPrice34}
02139D38 0000{magicLampEarlyPrice34}{itemBagEarlyPrice34}
E0000000 80008000
2818FD62 00000001
2818FD72 00000000
04139D2C {miniMushroomMidPrice1}{megaMushroomMidPrice1}{superMiniMushroomMidPrice1}{superMegaMushroomMidPrice1}
04139D30 {miniMegaHammerMidPrice1}{warpPipeMidPrice1}{swapCardMidPrice1}{sparkyStickerMidPrice1}
04139D34 {gaddlightMidPrice1}{chompCallMidPrice1}{bowserSuitMidPrice1}{crystalBallMidPrice1}
02139D38 0000{magicLampMidPrice1}{itemBagMidPrice1}
E2000001 80008000
2818FD72 00000001
04139D2C {miniMushroomMidPrice2}{megaMushroomMidPrice2}{superMiniMushroomMidPrice2}{superMegaMushroomMidPrice2}
04139D30 {miniMegaHammerMidPrice2}{warpPipeMidPrice2}{swapCardMidPrice2}{sparkyStickerMidPrice2}
04139D34 {gaddlightMidPrice2}{chompCallMidPrice2}{bowserSuitMidPrice2}{crystalBallMidPrice2}
02139D38 0000{magicLampMidPrice2}{itemBagMidPrice2}
E2000001 80008000
2818FD72 00000001
04139D2C {miniMushroomMidPrice34}{megaMushroomMidPrice34}{superMiniMushroomMidPrice34}{superMegaMushroomMidPrice34}
04139D30 {miniMegaHammerMidPrice34}{warpPipeMidPrice34}{swapCardMidPrice34}{sparkyStickerMidPrice34}
04139D34 {gaddlightMidPrice34}{chompCallMidPrice34}{bowserSuitMidPrice34}{crystalBallMidPrice34}
02139D38 0000{magicLampMidPrice34}{itemBagMidPrice34}
E2000001 80008000
2C18FD62 00000002
2818FD72 00000000
04139D2C {miniMushroomLatePrice1}{megaMushroomLatePrice1}{superMiniMushroomLatePrice1}{superMegaMushroomLatePrice1}
04139D30 {miniMegaHammerLatePrice1}{warpPipeLatePrice1}{swapCardLatePrice1}{sparkyStickerLatePrice1}
04139D34 {gaddlightLatePrice1}{chompCallLatePrice1}{bowserSuitLatePrice1}{crystalBallLatePrice1}
02139D38 0000{magicLampLatePrice1}{itemBagLatePrice1}
2818FD72 00000001
04139D2C {miniMushroomLatePrice2}{megaMushroomLatePrice2}{superMiniMushroomLatePrice2}{superMegaMushroomLatePrice2}
04139D30 {miniMegaHammerLatePrice2}{warpPipeLatePrice2}{swapCardLatePrice2}{sparkyStickerLatePrice2}
04139D34 {gaddlightLatePrice2}{chompCallLatePrice2}{bowserSuitLatePrice2}{crystalBallLatePrice2}
02139D38 0000{magicLampLatePrice2}{itemBagLatePrice2}
E2000001 80008000
2818FD72 00000002
04139D2C {miniMushroomLatePrice34}{megaMushroomLatePrice34}{superMiniMushroomLatePrice34}{superMegaMushroomLatePrice34}
04139D30 {miniMegaHammerLatePrice34}{warpPipeLatePrice34}{swapCardLatePrice34}{sparkyStickerLatePrice34}
04139D34 {gaddlightLatePrice34}{chompCallLatePrice34}{bowserSuitLatePrice34}{crystalBallLatePrice34}
02139D38 0000{magicLampLatePrice34}{itemBagLatePrice34}
E0000000 80008000
'''

def getItemShopOddsFour(miniMushroomEarlyOdds1, miniMushroomEarlyOdds2, miniMushroomEarlyOdds34, miniMushroomMidOdds1, miniMushroomMidOdds2, miniMushroomMidOdds34, miniMushroomLateOdds1, miniMushroomLateOdds2, miniMushroomLateOdds34, megaMushroomEarlyOdds1, megaMushroomEarlyOdds2, megaMushroomEarlyOdds34, megaMushroomMidOdds1, megaMushroomMidOdds2, megaMushroomMidOdds34, megaMushroomLateOdds1, megaMushroomLateOdds2, megaMushroomLateOdds34, superMiniMushroomEarlyOdds1, superMiniMushroomEarlyOdds2, superMiniMushroomEarlyOdds34, superMiniMushroomMidOdds1, superMiniMushroomMidOdds2, superMiniMushroomMidOdds34, superMiniMushroomLateOdds1, superMiniMushroomLateOdds2, superMiniMushroomLateOdds34, superMegaMushroomEarlyOdds1, superMegaMushroomEarlyOdds2, superMegaMushroomEarlyOdds34, superMegaMushroomMidOdds1, superMegaMushroomMidOdds2, superMegaMushroomMidOdds34, superMegaMushroomLateOdds1, superMegaMushroomLateOdds2, superMegaMushroomLateOdds34, miniMegaHammerEarlyOdds1, miniMegaHammerEarlyOdds2, miniMegaHammerEarlyOdds34, miniMegaHammerMidOdds1, miniMegaHammerMidOdds2, miniMegaHammerMidOdds34, miniMegaHammerLateOdds1, miniMegaHammerLateOdds2, miniMegaHammerLateOdds34, warpPipeEarlyOdds1, warpPipeEarlyOdds2, warpPipeEarlyOdds34, warpPipeMidOdds1, warpPipeMidOdds2, warpPipeMidOdds34, warpPipeLateOdds1, warpPipeLateOdds2, warpPipeLateOdds34, swapCardEarlyOdds1, swapCardEarlyOdds2, swapCardEarlyOdds34, swapCardMidOdds1, swapCardMidOdds2, swapCardMidOdds34, swapCardLateOdds1, swapCardLateOdds2, swapCardLateOdds34, sparkyStickerEarlyOdds1, sparkyStickerEarlyOdds2, sparkyStickerEarlyOdds34, sparkyStickerMidOdds1, sparkyStickerMidOdds2, sparkyStickerMidOdds34, sparkyStickerLateOdds1, sparkyStickerLateOdds2, sparkyStickerLateOdds34, gaddlightEarlyOdds1, gaddlightEarlyOdds2, gaddlightEarlyOdds34, gaddlightMidOdds1, gaddlightMidOdds2, gaddlightMidOdds34, gaddlightLateOdds1, gaddlightLateOdds2, gaddlightLateOdds34, chompCallEarlyOdds1, chompCallEarlyOdds2, chompCallEarlyOdds34, chompCallMidOdds1, chompCallMidOdds2, chompCallMidOdds34, chompCallLateOdds1, chompCallLateOdds2, chompCallLateOdds34, bowserSuitEarlyOdds1, bowserSuitEarlyOdds2, bowserSuitEarlyOdds34, bowserSuitMidOdds1, bowserSuitMidOdds2, bowserSuitMidOdds34, bowserSuitLateOdds1, bowserSuitLateOdds2, bowserSuitLateOdds34, crystalBallEarlyOdds1, crystalBallEarlyOdds2, crystalBallEarlyOdds34, crystalBallMidOdds1, crystalBallMidOdds2, crystalBallMidOdds34, crystalBallLateOdds1, crystalBallLateOdds2, crystalBallLateOdds34, magicLampEarlyOdds1, magicLampEarlyOdds2, magicLampEarlyOdds34, magicLampMidOdds1, magicLampMidOdds2, magicLampMidOdds34, magicLampLateOdds1, magicLampLateOdds2, magicLampLateOdds34, itemBagEarlyOdds1, itemBagEarlyOdds2, itemBagEarlyOdds34, itemBagMidOdds1, itemBagMidOdds2, itemBagMidOdds34, itemBagLateOdds1, itemBagLateOdds2, itemBagLateOdds34):
    return f'''
C2077FF4 00000039
3C80801A 60844A60
386000FF 90640000
90640004 90640008
9064000C 90640010
3C608018 6063FCFC
88830001 88630000
38A00003 7C842BD6
38A00000 7C032000
40810048 38A0000E
1C840002 7C032000
40810008 38A00046
3C808019 6084FD02
88840000 1C840030
3C608018 6063FC38
7C832214 8C640009
70630060 5463D97E
1C63000E 7CA51A14
3CC08013 60C69DB2
7CC62A14 38600000
3A200000 7C8618AE
7E312214 38630001
2C03000E 40800008
4BFFFFEC 3C608005
6063FB40 7C6903A6
2C030000 418200DC
7E238B78 4E800421
7C651B78 38600000
39600000 7C8618AE
7D6B2214 7C0B2800
41810018 7C0B8800
41820010 38630001
4BFFFFE4 4BFFFFCC
3C80801A 60844A60
81640000 3AA00000
3A400000 7CA6A8AE
2C050000 41820008
3A520001 3AB50001
2C15000E 40800008
4BFFFFE4 3AA00000
3CA0801A 60A54A60
7CA5AA14 80A50000
2C0500FF 4182002C
3AB50001 2C150005
40800008 4BFFFFDC
7C0B1800 4182FF64
2C0B00FF 41820018
38840004 4BFFFF94
7C159000 4080FFEC
4BFFFFE0 90640000
3C80801A 60844A60
80840010 2C0400FF
4082002C 4BFFFF2C
3860000E 4E800421
3C80801A 60844A60
98640000 98640004
98640008 9864000C
98640010 00000000
C2086480 00000013
80640000 3DE08018
61EFFD02 89EF0000
1DEF0030 3C808018
6084FC38 7C847A14
88840009 70840060
5484D97E 3DE08018
61EFFD62 B08F0000
3DC08018 61CEFCFC
888E0001 89CE0000
39C00003 7C8473D6
3DC08018 61CEFCFC
89CE0000 39E00000
7C0E2000 40810018
39E00001 1C840002
7C0E2000 40810008
39E00002 3C808018
6084FD72 B1E40000
39C00000 39E00000
60000000 00000000
2818FD72 00000000
02139DB2 0000{miniMushroomEarlyOdds1}{megaMushroomEarlyOdds1}
04139DB4 {superMiniMushroomEarlyOdds1}{superMegaMushroomEarlyOdds1}{miniMegaHammerEarlyOdds1}{warpPipeEarlyOdds1}
04139DB8 {swapCardEarlyOdds1}{sparkyStickerEarlyOdds1}{gaddlightEarlyOdds1}{chompCallEarlyOdds1}
04139DBC {bowserSuitEarlyOdds1}{crystalBallEarlyOdds1}{magicLampEarlyOdds1}{itemBagEarlyOdds1}
E2000001 80008000
2818FD72 00000000
02139DB2 0000{miniMushroomMidOdds1}{megaMushroomMidOdds1}
04139DB4 {superMiniMushroomMidOdds1}{superMegaMushroomMidOdds1}{miniMegaHammerMidOdds1}{warpPipeMidOdds1}
04139DB8 {swapCardMidOdds1}{sparkyStickerMidOdds1}{gaddlightMidOdds1}{chompCallMidOdds1}
04139DBC {bowserSuitMidOdds1}{crystalBallMidOdds1}{magicLampMidOdds1}{itemBagMidOdds1}
E2000001 80008000
2818FD72 00000000
02139DB2 0000{miniMushroomLateOdds1}{megaMushroomLateOdds1}
04139DB4 {superMiniMushroomLateOdds1}{superMegaMushroomLateOdds1}{miniMegaHammerLateOdds1}{warpPipeLateOdds1}
04139DB8 {swapCardLateOdds1}{sparkyStickerLateOdds1}{gaddlightLateOdds1}{chompCallLateOdds1}
04139DBC {bowserSuitLateOdds1}{crystalBallLateOdds1}{magicLampLateOdds1}{itemBagLateOdds1}
E2000001 80008000
04139DC0 {miniMushroomMidOdds1}{megaMushroomMidOdds1}{superMiniMushroomMidOdds1}{superMegaMushroomMidOdds1}
04139DC4 {miniMegaHammerMidOdds1}{warpPipeMidOdds1}{swapCardMidOdds1}{sparkyStickerMidOdds1}
04139DC8 {gaddlightMidOdds1}{chompCallMidOdds1}{bowserSuitMidOdds1}{crystalBallMidOdds1}
04139DCC {magicLampMidOdds1}{itemBagMidOdds1}{miniMushroomMidOdds2}{megaMushroomMidOdds2}
04139DD0 {superMiniMushroomMidOdds2}{superMegaMushroomMidOdds2}{miniMegaHammerMidOdds2}{warpPipeMidOdds2}
04139DD4 {swapCardMidOdds2}{sparkyStickerMidOdds2}{gaddlightMidOdds2}{chompCallMidOdds2}
02139DD8 {bowserSuitMidOdds2}{crystalBallMidOdds2}{magicLampMidOdds2}{itemBagMidOdds2}
04139DDC {miniMushroomMidOdds34}{megaMushroomMidOdds34}{superMiniMushroomMidOdds34}{superMegaMushroomMidOdds34}
04139DE0 {miniMegaHammerMidOdds34}{warpPipeMidOdds34}{swapCardMidOdds34}{sparkyStickerMidOdds34}
04139DE4 {gaddlightMidOdds34}{chompCallMidOdds34}{bowserSuitMidOdds34}{crystalBallMidOdds34}
04139DE8 {magicLampMidOdds34}{itemBagMidOdds34}{miniMushroomMidOdds34}{megaMushroomMidOdds34}
04139DEC {superMiniMushroomMidOdds34}{superMegaMushroomMidOdds34}{miniMegaHammerMidOdds34}{warpPipeMidOdds34}
04139DF0 {swapCardMidOdds34}{sparkyStickerMidOdds34}{gaddlightMidOdds34}{chompCallMidOdds34}
02139DF4 {bowserSuitMidOdds34}{crystalBallMidOdds34}{magicLampMidOdds34}{itemBagMidOdds34}
04139DF8 {miniMushroomLateOdds1}{megaMushroomLateOdds1}{superMiniMushroomLateOdds1}{superMegaMushroomLateOdds1}
04139DFC {miniMegaHammerLateOdds1}{warpPipeLateOdds1}{swapCardLateOdds1}{sparkyStickerLateOdds1}
04139E00 {gaddlightLateOdds1}{chompCallLateOdds1}{bowserSuitLateOdds1}{crystalBallLateOdds1}
04139E04 {magicLampLateOdds1}{itemBagLateOdds1}{miniMushroomLateOdds2}{megaMushroomLateOdds2}
04139E08 {superMiniMushroomLateOdds2}{superMegaMushroomLateOdds2}{miniMegaHammerLateOdds2}{warpPipeLateOdds2}
04139E0C {swapCardLateOdds2}{sparkyStickerLateOdds2}{gaddlightLateOdds2}{chompCallLateOdds2}
04139E10 {bowserSuitLateOdds2}{crystalBallLateOdds2}{magicLampLateOdds2}{itemBagLateOdds2}
04139E14 {miniMushroomLateOdds34}{megaMushroomLateOdds34}{superMiniMushroomLateOdds34}{superMegaMushroomLateOdds34}
04139E18 {miniMegaHammerLateOdds34}{warpPipeLateOdds34}{swapCardLateOdds34}{sparkyStickerLateOdds34}
04139E1C {gaddlightLateOdds34}{chompCallLateOdds34}{bowserSuitLateOdds34}{crystalBallLateOdds34}
04139E20 {magicLampLateOdds34}{itemBagLateOdds34}{miniMushroomLateOdds34}{megaMushroomLateOdds34}
04139E24 {superMiniMushroomLateOdds34}{superMegaMushroomLateOdds34}{miniMegaHammerLateOdds34}{warpPipeLateOdds34}
04139E28 {swapCardLateOdds34}{sparkyStickerLateOdds34}{gaddlightLateOdds34}{chompCallLateOdds34}
04139E2C {bowserSuitLateOdds34}{crystalBallLateOdds34}{magicLampLateOdds34}{itemBagLateOdds34}
'''

def getItemShopOddsFourDX(miniMushroomEarlyOdds1, miniMushroomEarlyOdds2, miniMushroomEarlyOdds34, miniMushroomMidOdds1, miniMushroomMidOdds2, miniMushroomMidOdds34, miniMushroomLateOdds1, miniMushroomLateOdds2, miniMushroomLateOdds34, megaMushroomEarlyOdds1, megaMushroomEarlyOdds2, megaMushroomEarlyOdds34, megaMushroomMidOdds1, megaMushroomMidOdds2, megaMushroomMidOdds34, megaMushroomLateOdds1, megaMushroomLateOdds2, megaMushroomLateOdds34, superMiniMushroomEarlyOdds1, superMiniMushroomEarlyOdds2, superMiniMushroomEarlyOdds34, superMiniMushroomMidOdds1, superMiniMushroomMidOdds2, superMiniMushroomMidOdds34, superMiniMushroomLateOdds1, superMiniMushroomLateOdds2, superMiniMushroomLateOdds34, superMegaMushroomEarlyOdds1, superMegaMushroomEarlyOdds2, superMegaMushroomEarlyOdds34, superMegaMushroomMidOdds1, superMegaMushroomMidOdds2, superMegaMushroomMidOdds34, superMegaMushroomLateOdds1, superMegaMushroomLateOdds2, superMegaMushroomLateOdds34, miniMegaHammerEarlyOdds1, miniMegaHammerEarlyOdds2, miniMegaHammerEarlyOdds34, miniMegaHammerMidOdds1, miniMegaHammerMidOdds2, miniMegaHammerMidOdds34, miniMegaHammerLateOdds1, miniMegaHammerLateOdds2, miniMegaHammerLateOdds34, warpPipeEarlyOdds1, warpPipeEarlyOdds2, warpPipeEarlyOdds34, warpPipeMidOdds1, warpPipeMidOdds2, warpPipeMidOdds34, warpPipeLateOdds1, warpPipeLateOdds2, warpPipeLateOdds34, swapCardEarlyOdds1, swapCardEarlyOdds2, swapCardEarlyOdds34, swapCardMidOdds1, swapCardMidOdds2, swapCardMidOdds34, swapCardLateOdds1, swapCardLateOdds2, swapCardLateOdds34, sparkyStickerEarlyOdds1, sparkyStickerEarlyOdds2, sparkyStickerEarlyOdds34, sparkyStickerMidOdds1, sparkyStickerMidOdds2, sparkyStickerMidOdds34, sparkyStickerLateOdds1, sparkyStickerLateOdds2, sparkyStickerLateOdds34, gaddlightEarlyOdds1, gaddlightEarlyOdds2, gaddlightEarlyOdds34, gaddlightMidOdds1, gaddlightMidOdds2, gaddlightMidOdds34, gaddlightLateOdds1, gaddlightLateOdds2, gaddlightLateOdds34, chompCallEarlyOdds1, chompCallEarlyOdds2, chompCallEarlyOdds34, chompCallMidOdds1, chompCallMidOdds2, chompCallMidOdds34, chompCallLateOdds1, chompCallLateOdds2, chompCallLateOdds34, bowserSuitEarlyOdds1, bowserSuitEarlyOdds2, bowserSuitEarlyOdds34, bowserSuitMidOdds1, bowserSuitMidOdds2, bowserSuitMidOdds34, bowserSuitLateOdds1, bowserSuitLateOdds2, bowserSuitLateOdds34, crystalBallEarlyOdds1, crystalBallEarlyOdds2, crystalBallEarlyOdds34, crystalBallMidOdds1, crystalBallMidOdds2, crystalBallMidOdds34, crystalBallLateOdds1, crystalBallLateOdds2, crystalBallLateOdds34, magicLampEarlyOdds1, magicLampEarlyOdds2, magicLampEarlyOdds34, magicLampMidOdds1, magicLampMidOdds2, magicLampMidOdds34, magicLampLateOdds1, magicLampLateOdds2, magicLampLateOdds34, itemBagEarlyOdds1, itemBagEarlyOdds2, itemBagEarlyOdds34, itemBagMidOdds1, itemBagMidOdds2, itemBagMidOdds34, itemBagLateOdds1, itemBagLateOdds2, itemBagLateOdds34, mushroomEarlyOdds1, mushroomEarlyOdds2, mushroomEarlyOdds34, mushroomMidOdds1, mushroomMidOdds2, mushroomMidOdds34, mushroomLateOdds1, mushroomLateOdds2, mushroomLateOdds34, goldenMushroomEarlyOdds1, goldenMushroomEarlyOdds2, goldenMushroomEarlyOdds34, goldenMushroomMidOdds1, goldenMushroomMidOdds2, goldenMushroomMidOdds34, goldenMushroomLateOdds1, goldenMushroomLateOdds2, goldenMushroomLateOdds34, reverseMushroomEarlyOdds1, reverseMushroomEarlyOdds2, reverseMushroomEarlyOdds34, reverseMushroomMidOdds1, reverseMushroomMidOdds2, reverseMushroomMidOdds34, reverseMushroomLateOdds1, reverseMushroomLateOdds2, reverseMushroomLateOdds34, poisonMushroomEarlyOdds1, poisonMushroomEarlyOdds2, poisonMushroomEarlyOdds34, poisonMushroomMidOdds1, poisonMushroomMidOdds2, poisonMushroomMidOdds34, poisonMushroomLateOdds1, poisonMushroomLateOdds2, poisonMushroomLateOdds34, triplePoisonMushroomEarlyOdds1, triplePoisonMushroomEarlyOdds2, triplePoisonMushroomEarlyOdds34, triplePoisonMushroomMidOdds1, triplePoisonMushroomMidOdds2, triplePoisonMushroomMidOdds34, triplePoisonMushroomLateOdds1, triplePoisonMushroomLateOdds2, triplePoisonMushroomLateOdds34, celluarShopperEarlyOdds1, celluarShopperEarlyOdds2, celluarShopperEarlyOdds34, celluarShopperMidOdds1, celluarShopperMidOdds2, celluarShopperMidOdds34, celluarShopperLateOdds1, celluarShopperLateOdds2, celluarShopperLateOdds34, skeletonKeyEarlyOdds1, skeletonKeyEarlyOdds2, skeletonKeyEarlyOdds34, skeletonKeyMidOdds1, skeletonKeyMidOdds2, skeletonKeyMidOdds34, skeletonKeyLateOdds1, skeletonKeyLateOdds2, skeletonKeyLateOdds34, plunderChestEarlyOdds1, plunderChestEarlyOdds2, plunderChestEarlyOdds34, plunderChestMidOdds1, plunderChestMidOdds2, plunderChestMidOdds34, plunderChestLateOdds1, plunderChestLateOdds2, plunderChestLateOdds34, gaddbrushEarlyOdds1, gaddbrushEarlyOdds2, gaddbrushEarlyOdds34, gaddbrushMidOdds1, gaddbrushMidOdds2, gaddbrushMidOdds34, gaddbrushLateOdds1, gaddbrushLateOdds2, gaddbrushLateOdds34, warpBlockEarlyOdds1, warpBlockEarlyOdds2, warpBlockEarlyOdds34, warpBlockMidOdds1, warpBlockMidOdds2, warpBlockMidOdds34, warpBlockLateOdds1, warpBlockLateOdds2, warpBlockLateOdds34, flyGuyEarlyOdds1, flyGuyEarlyOdds2, flyGuyEarlyOdds34, flyGuyMidOdds1, flyGuyMidOdds2, flyGuyMidOdds34, flyGuyLateOdds1, flyGuyLateOdds2, flyGuyLateOdds34, plusBlockEarlyOdds1, plusBlockEarlyOdds2, plusBlockEarlyOdds34, plusBlockMidOdds1, plusBlockMidOdds2, plusBlockMidOdds34, plusBlockLateOdds1, plusBlockLateOdds2, plusBlockLateOdds34, minusBlockEarlyOdds1, minusBlockEarlyOdds2, minusBlockEarlyOdds34, minusBlockMidOdds1, minusBlockMidOdds2, minusBlockMidOdds34, minusBlockLateOdds1, minusBlockLateOdds2, minusBlockLateOdds34, speedBlockEarlyOdds1, speedBlockEarlyOdds2, speedBlockEarlyOdds34, speedBlockMidOdds1, speedBlockMidOdds2, speedBlockMidOdds34, speedBlockLateOdds1, speedBlockLateOdds2, speedBlockLateOdds34, slowBlockEarlyOdds1, slowBlockEarlyOdds2, slowBlockEarlyOdds34, slowBlockMidOdds1, slowBlockMidOdds2, slowBlockMidOdds34, slowBlockLateOdds1, slowBlockLateOdds2, slowBlockLateOdds34, bowserPhoneEarlyOdds1, bowserPhoneEarlyOdds2, bowserPhoneEarlyOdds34, bowserPhoneMidOdds1, bowserPhoneMidOdds2, bowserPhoneMidOdds34, bowserPhoneLateOdds1, bowserPhoneLateOdds2, bowserPhoneLateOdds34, doubleDipEarlyOdds1, doubleDipEarlyOdds2, doubleDipEarlyOdds34, doubleDipMidOdds1, doubleDipMidOdds2, doubleDipMidOdds34, doubleDipLateOdds1, doubleDipLateOdds2, doubleDipLateOdds34, hiddenBlockCardEarlyOdds1, hiddenBlockCardEarlyOdds2, hiddenBlockCardEarlyOdds34, hiddenBlockCardMidOdds1, hiddenBlockCardMidOdds2, hiddenBlockCardMidOdds34, hiddenBlockCardLateOdds1, hiddenBlockCardLateOdds2, hiddenBlockCardLateOdds34, barterBoxEarlyOdds1, barterBoxEarlyOdds2, barterBoxEarlyOdds34, barterBoxMidOdds1, barterBoxMidOdds2, barterBoxMidOdds34, barterBoxLateOdds1, barterBoxLateOdds2, barterBoxLateOdds34, superWarpPipeEarlyOdds1, superWarpPipeEarlyOdds2, superWarpPipeEarlyOdds34, superWarpPipeMidOdds1, superWarpPipeMidOdds2, superWarpPipeMidOdds34, superWarpPipeLateOdds1, superWarpPipeLateOdds2, superWarpPipeLateOdds34, chanceTimeCharmEarlyOdds1, chanceTimeCharmEarlyOdds2, chanceTimeCharmEarlyOdds34, chanceTimeCharmMidOdds1, chanceTimeCharmMidOdds2, chanceTimeCharmMidOdds34, chanceTimeCharmLateOdds1, chanceTimeCharmLateOdds2, chanceTimeCharmLateOdds34, wackyWatchEarlyOdds1, wackyWatchEarlyOdds2, wackyWatchEarlyOdds34, wackyWatchMidOdds1, wackyWatchMidOdds2, wackyWatchMidOdds34, wackyWatchLateOdds1, wackyWatchLateOdds2, wackyWatchLateOdds34):
    return f'''
28071C98 00000000
04071f30 {miniMushroomEarlyOdds1}{megaMushroomEarlyOdds1}{superMiniMushroomEarlyOdds1}{superMegaMushroomEarlyOdds1}
04071f34 {miniMegaHammerEarlyOdds1}{warpPipeEarlyOdds1}{swapCardEarlyOdds1}{sparkyStickerEarlyOdds1}
04071f38 {gaddlightEarlyOdds1}{chompCallEarlyOdds1}{bowserSuitEarlyOdds1}{crystalBallEarlyOdds1}
04071f3C {magicLampEarlyOdds1}{itemBagEarlyOdds1}{bowserPhoneEarlyOdds1}{mushroomEarlyOdds1}
04071f40 {goldenMushroomEarlyOdds1}{hiddenBlockCardEarlyOdds1}{celluarShopperEarlyOdds1}{barterBoxEarlyOdds1}
04071f44 {superWarpPipeEarlyOdds1}{chanceTimeCharmEarlyOdds1}{wackyWatchEarlyOdds1}{plunderChestEarlyOdds1}
04071f48 {gaddbrushEarlyOdds1}{skeletonKeyEarlyOdds1}{warpBlockEarlyOdds1}{flyGuyEarlyOdds1}
04071f4C {plusBlockEarlyOdds1}{minusBlockEarlyOdds1}{speedBlockEarlyOdds1}{slowBlockEarlyOdds1}
04071f50 {poisonMushroomEarlyOdds1}{triplePoisonMushroomEarlyOdds1}{doubleDipEarlyOdds1}{reverseMushroomEarlyOdds1}
E2000001 80008000
28071C98 00000000
04071f30 {miniMushroomEarlyOdds2}{megaMushroomEarlyOdds2}{superMiniMushroomEarlyOdds2}{superMegaMushroomEarlyOdds2}
04071f34 {miniMegaHammerEarlyOdds2}{warpPipeEarlyOdds2}{swapCardEarlyOdds2}{sparkyStickerEarlyOdds2}
04071f38 {gaddlightEarlyOdds2}{chompCallEarlyOdds2}{bowserSuitEarlyOdds2}{crystalBallEarlyOdds2}
04071f3C {magicLampEarlyOdds2}{itemBagEarlyOdds2}{bowserPhoneEarlyOdds2}{mushroomEarlyOdds2}
04071f40 {goldenMushroomEarlyOdds2}{hiddenBlockCardEarlyOdds2}{celluarShopperEarlyOdds2}{barterBoxEarlyOdds2}
04071f44 {superWarpPipeEarlyOdds2}{chanceTimeCharmEarlyOdds2}{wackyWatchEarlyOdds2}{plunderChestEarlyOdds2}
04071f48 {gaddbrushEarlyOdds2}{skeletonKeyEarlyOdds2}{warpBlockEarlyOdds2}{flyGuyEarlyOdds2}
04071f4C {plusBlockEarlyOdds2}{minusBlockEarlyOdds2}{speedBlockEarlyOdds2}{slowBlockEarlyOdds2}
04071f50 {poisonMushroomEarlyOdds2}{triplePoisonMushroomEarlyOdds2}{doubleDipEarlyOdds2}{reverseMushroomEarlyOdds2}
E2000001 80008000
2C071C98 00000001
04071f30 {miniMushroomEarlyOdds34}{megaMushroomEarlyOdds34}{superMiniMushroomEarlyOdds34}{superMegaMushroomEarlyOdds34}
04071f34 {miniMegaHammerEarlyOdds34}{warpPipeEarlyOdds34}{swapCardEarlyOdds34}{sparkyStickerEarlyOdds34}
04071f38 {gaddlightEarlyOdds34}{chompCallEarlyOdds34}{bowserSuitEarlyOdds34}{crystalBallEarlyOdds34}
04071f3C {magicLampEarlyOdds34}{itemBagEarlyOdds34}{bowserPhoneEarlyOdds34}{mushroomEarlyOdds34}
04071f40 {goldenMushroomEarlyOdds34}{hiddenBlockCardEarlyOdds34}{celluarShopperEarlyOdds34}{barterBoxEarlyOdds34}
04071f44 {superWarpPipeEarlyOdds34}{chanceTimeCharmEarlyOdds34}{wackyWatchEarlyOdds34}{plunderChestEarlyOdds34}
04071f48 {gaddbrushEarlyOdds34}{skeletonKeyEarlyOdds34}{warpBlockEarlyOdds34}{flyGuyEarlyOdds34}
04071f4C {plusBlockEarlyOdds34}{minusBlockEarlyOdds34}{speedBlockEarlyOdds34}{slowBlockEarlyOdds34}
04071f50 {poisonMushroomEarlyOdds34}{triplePoisonMushroomEarlyOdds34}{doubleDipEarlyOdds34}{reverseMushroomEarlyOdds34}
E2000001 80008000
02071f62 0000{miniMushroomMidOdds1}{megaMushroomMidOdds1}
04071f64 {superMegaMushroomMidOdds1}{superMegaMushroomMidOdds1}{miniMegaHammerMidOdds1}{superWarpPipeMidOdds1}
04071f68 {swapCardMidOdds1}{sparkyStickerMidOdds1}{gaddlightMidOdds1}{chompCallMidOdds1}
04071f6C {bowserSuitMidOdds1}{crystalBallMidOdds1}{magicLampMidOdds1}{itemBagMidOdds1}
04071f70 {bowserPhoneMidOdds1}{mushroomMidOdds1}{goldenMushroomMidOdds1}{hiddenBlockCardMidOdds1}
04071f74 {celluarShopperMidOdds1}{barterBoxMidOdds1}{superWarpPipeMidOdds1}{chanceTimeCharmMidOdds1}
04071f78 {wackyWatchMidOdds1}{plunderChestMidOdds1}{gaddbrushMidOdds1}{skeletonKeyMidOdds1}
04071f7C {warpBlockMidOdds1}{flyGuyMidOdds1}{plusBlockMidOdds1}{minusBlockMidOdds1}
04071f80 {speedBlockMidOdds1}{slowBlockMidOdds1}{poisonMushroomMidOdds1}{triplePoisonMushroomMidOdds1}
04071f84 {doubleDipMidOdds1}{reverseMushroomMidOdds1}0000
04071F94 {miniMushroomMidOdds2}{megaMushroomMidOdds2}{superMiniMushroomMidOdds2}{superMegaMushroomMidOdds2}
04071f98 {miniMegaHammerMidOdds2}{warpPipeMidOdds2}{swapCardMidOdds2}{sparkyStickerMidOdds2}
04071f9C {gaddlightMidOdds2}{chompCallMidOdds2}{bowserSuitMidOdds2}{crystalBallMidOdds2}
04071fA0 {magicLampMidOdds2}{itemBagMidOdds2}{bowserPhoneMidOdds2}{mushroomMidOdds2}
04071fA4 {goldenMushroomMidOdds2}{hiddenBlockCardMidOdds2}{celluarShopperMidOdds2}{barterBoxMidOdds2}
04071fA8 {superWarpPipeMidOdds2}{chanceTimeCharmMidOdds2}{wackyWatchMidOdds2}{plunderChestMidOdds2}
04071fAC {gaddbrushMidOdds2}{skeletonKeyMidOdds2}{warpBlockMidOdds2}{flyGuyMidOdds2}
04071fB0 {plusBlockMidOdds2}{minusBlockMidOdds2}{speedBlockMidOdds2}{slowBlockMidOdds2}
04071fB4 {poisonMushroomMidOdds2}{triplePoisonMushroomMidOdds2}{doubleDipMidOdds2}{reverseMushroomMidOdds2}
02071FC6 0000{miniMushroomMidOdds34}{megaMushroomMidOdds34}
04071fC8 {superMegaMushroomMidOdds34}{superMegaMushroomMidOdds34}{miniMegaHammerMidOdds34}{superWarpPipeMidOdds34}
04071fCC {swapCardMidOdds34}{sparkyStickerMidOdds34}{gaddlightMidOdds34}{chompCallMidOdds34}
04071fD0 {bowserSuitMidOdds34}{crystalBallMidOdds34}{magicLampMidOdds34}{itemBagMidOdds34}
04071fD4 {bowserPhoneMidOdds34}{mushroomMidOdds34}{goldenMushroomMidOdds34}{hiddenBlockCardMidOdds34}
04071fD8 {celluarShopperMidOdds34}{barterBoxMidOdds34}{superWarpPipeMidOdds34}{chanceTimeCharmMidOdds34}
04071fDC {wackyWatchMidOdds34}{plunderChestMidOdds34}{gaddbrushMidOdds34}{skeletonKeyMidOdds34}
04071fE0 {warpBlockMidOdds34}{flyGuyMidOdds34}{plusBlockMidOdds34}{minusBlockMidOdds34}
04071fE4 {speedBlockMidOdds34}{slowBlockMidOdds34}{poisonMushroomMidOdds34}{triplePoisonMushroomMidOdds34}
04071fE8 {doubleDipMidOdds34}{reverseMushroomMidOdds34}0000
04071Ff8 {miniMushroomMidOdds34}{megaMushroomMidOdds34}{superMiniMushroomMidOdds34}{superMegaMushroomMidOdds34}
04071ffc {miniMegaHammerMidOdds34}{warpPipeMidOdds34}{swapCardMidOdds34}{sparkyStickerMidOdds34}
04072000 {gaddlightMidOdds34}{chompCallMidOdds34}{bowserSuitMidOdds34}{crystalBallMidOdds34}
04072004 {magicLampMidOdds34}{itemBagMidOdds34}{bowserPhoneMidOdds34}{mushroomMidOdds34}
04072008 {goldenMushroomMidOdds34}{hiddenBlockCardMidOdds34}{celluarShopperMidOdds34}{barterBoxMidOdds34}
0407200c {superWarpPipeMidOdds34}{chanceTimeCharmMidOdds34}{wackyWatchMidOdds34}{plunderChestMidOdds34}
04072010 {gaddbrushMidOdds34}{skeletonKeyMidOdds34}{warpBlockMidOdds34}{flyGuyMidOdds34}
04072014 {plusBlockMidOdds34}{minusBlockMidOdds34}{speedBlockMidOdds34}{slowBlockMidOdds34}
04072018 {poisonMushroomMidOdds34}{triplePoisonMushroomMidOdds34}{doubleDipMidOdds34}{reverseMushroomMidOdds34}
0207202A 0000{miniMushroomLateOdds1}{megaMushroomLateOdds1}
0407202C {superMegaMushroomLateOdds1}{superMegaMushroomLateOdds1}{miniMegaHammerLateOdds1}{superWarpPipeLateOdds1}
04072030 {swapCardLateOdds1}{sparkyStickerLateOdds1}{gaddlightLateOdds1}{chompCallLateOdds1}
04072034 {bowserSuitLateOdds1}{crystalBallLateOdds1}{magicLampLateOdds1}{itemBagLateOdds1}
04072038 {bowserPhoneLateOdds1}{mushroomLateOdds1}{goldenMushroomLateOdds1}{hiddenBlockCardLateOdds1}
0407203C {celluarShopperLateOdds1}{barterBoxLateOdds1}{superWarpPipeLateOdds1}{chanceTimeCharmLateOdds1}
04072040 {wackyWatchLateOdds1}{plunderChestLateOdds1}{gaddbrushLateOdds1}{skeletonKeyLateOdds1}
04072044 {warpBlockLateOdds1}{flyGuyLateOdds1}{plusBlockLateOdds1}{minusBlockLateOdds1}
04072048 {speedBlockLateOdds1}{slowBlockLateOdds1}{poisonMushroomLateOdds1}{triplePoisonMushroomLateOdds1}
0407204C {doubleDipLateOdds1}{reverseMushroomLateOdds1}0000
0407205C {miniMushroomLateOdds2}{megaMushroomLateOdds2}{superMiniMushroomLateOdds2}{superMegaMushroomLateOdds2}
04072060 {miniMegaHammerLateOdds2}{warpPipeLateOdds2}{swapCardLateOdds2}{sparkyStickerLateOdds2}
04072064 {gaddlightLateOdds2}{chompCallLateOdds2}{bowserSuitLateOdds2}{crystalBallLateOdds2}
04072068 {magicLampLateOdds2}{itemBagLateOdds2}{bowserPhoneLateOdds2}{mushroomLateOdds2}
0407206C {goldenMushroomLateOdds2}{hiddenBlockCardLateOdds2}{celluarShopperLateOdds2}{barterBoxLateOdds2}
04072070 {superWarpPipeLateOdds2}{chanceTimeCharmLateOdds2}{wackyWatchLateOdds2}{plunderChestLateOdds2}
04072074 {gaddbrushLateOdds2}{skeletonKeyLateOdds2}{warpBlockLateOdds2}{flyGuyLateOdds2}
04072078 {plusBlockLateOdds2}{minusBlockLateOdds2}{speedBlockLateOdds2}{slowBlockLateOdds2}
0407207C {poisonMushroomLateOdds2}{triplePoisonMushroomLateOdds2}{doubleDipLateOdds2}{reverseMushroomLateOdds2}
0207208E 0000{miniMushroomLateOdds34}{megaMushroomLateOdds34}
04072090 {superMegaMushroomLateOdds34}{superMegaMushroomLateOdds34}{miniMegaHammerLateOdds34}{superWarpPipeLateOdds34}
04072094 {swapCardLateOdds34}{sparkyStickerLateOdds34}{gaddlightLateOdds34}{chompCallLateOdds34}
04072098 {bowserSuitLateOdds34}{crystalBallLateOdds34}{magicLampLateOdds34}{itemBagLateOdds34}
0407209C {bowserPhoneLateOdds34}{mushroomLateOdds34}{goldenMushroomLateOdds34}{hiddenBlockCardLateOdds34}
040720A0 {celluarShopperLateOdds34}{barterBoxLateOdds34}{superWarpPipeLateOdds34}{chanceTimeCharmLateOdds34}
040720A4 {wackyWatchLateOdds34}{plunderChestLateOdds34}{gaddbrushLateOdds34}{skeletonKeyLateOdds34}
040720A8 {warpBlockLateOdds34}{flyGuyLateOdds34}{plusBlockLateOdds34}{minusBlockLateOdds34}
040720AC {speedBlockLateOdds34}{slowBlockLateOdds34}{poisonMushroomLateOdds34}{triplePoisonMushroomLateOdds34}
040720B0 {doubleDipLateOdds34}{reverseMushroomLateOdds34}0000
040720C0 {miniMushroomLateOdds34}{megaMushroomLateOdds34}{superMiniMushroomLateOdds34}{superMegaMushroomLateOdds34}
040720C4 {miniMegaHammerLateOdds34}{warpPipeLateOdds34}{swapCardLateOdds34}{sparkyStickerLateOdds34}
040720C8 {gaddlightLateOdds34}{chompCallLateOdds34}{bowserSuitLateOdds34}{crystalBallLateOdds34}
040720CC {magicLampLateOdds34}{itemBagLateOdds34}{bowserPhoneLateOdds34}{mushroomLateOdds34}
040720D0 {goldenMushroomLateOdds34}{hiddenBlockCardLateOdds34}{celluarShopperLateOdds34}{barterBoxLateOdds34}
040720D4 {superWarpPipeLateOdds34}{chanceTimeCharmLateOdds34}{wackyWatchLateOdds34}{plunderChestLateOdds34}
040720D8 {gaddbrushLateOdds34}{skeletonKeyLateOdds34}{warpBlockLateOdds34}{flyGuyLateOdds34}
040720DC {plusBlockLateOdds34}{minusBlockLateOdds34}{speedBlockLateOdds34}{slowBlockLateOdds34}
040720E0 {poisonMushroomLateOdds34}{triplePoisonMushroomLateOdds34}{doubleDipLateOdds34}{reverseMushroomLateOdds34}
'''