# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (tabitha@tabs.gay)
# Date: 2/21/2024
# License: MIT
# ============================================

def getBlueSpaceCodeSix(amount, amountDec):
    return f'''
MP6 - Blue Spaces Give {amountDec} Coins
C215F1E8 00000001
3880{amount} 00000000
'''

def getRedSpaceCodeSix(amount, amountDec):
    return f'''
MP6 - Red Spaces Take Away {amountDec} Coins
C215F278 00000001
3880{amount} 00000000
'''

def getMinigameCodeSix(amount, amountDec):
    return f'''
MP6 - Minigames Award {amountDec} Coins
2A265BA8 00000015
2A265BA8 00000016
2A265BA8 00000029
2A265BA8 0000002D
2A265BA8 0000002E
2A265BA8 00000030
2A265BA8 0000003F
2A265BA8 0000004F
2A265BA8 00000050
28265778 0000000A
02265778 0000{amount}
E2000001 80008000
2A265BA8 00000015
2A265BA8 00000016
2A265BA8 00000029
2A265BA8 0000002D
2A265BA8 0000002E
2A265BA8 00000030
2A265BA8 0000003F
2A265BA8 0000004F
2A265BA8 00000050
28265988 0000000A
02265988 0000{amount}
E2000001 80008000
2A265BA8 00000015
2A265BA8 00000016
2A265BA8 00000029
2A265BA8 0000002D
2A265BA8 0000002E
2A265BA8 00000030
2A265BA8 0000003F
2A265BA8 0000004F
2A265BA8 00000050
28265A90 0000000A
02265A90 0000{amount}
E2000001 80008000
2A265BA8 00000015
2A265BA8 00000016
2A265BA8 00000029
2A265BA8 0000002D
2A265BA8 0000002E
2A265BA8 00000030
2A265BA8 0000003F
2A265BA8 0000004F
2A265BA8 00000050
28265880 0000000A
02265880 0000{amount}
E2000001 80008000
'''

def getCharacterSpaceCodeSix(amount, amountDec):
    return f'''
MP6 - Character Spaces Give {amountDec} Coins
C215F230 00000001
3880{amount} 00000000
'''

def getStarSpaceCodeSix(amount, negAmount, amountDec, y4, y2, x2, x4):
    return f'''
MP6 - Stars Cost {amountDec} Coins
C218333C 00000001
2C03{amount} 00000000
C218342C 00000001
2C03{amount} 00000000
C21834C4 00000001
2C03{amount} 00000000
C215F668 00000001
2C03{amount} 00000000
C215FA18 00000001
3880{negAmount} 00000000
C216068C 00000001
2C00{amount} 00000000
C2160D0C 00000001
3880{negAmount} 00000000  
C2183590 00000002
3880{amount} 7C8400D0
60000000 00000000
28265B8A 00000014
00265B8B 0000{amount}
E2000001 80008000
204F0E28 2C030014
044F0E28 2C03{amount}
E2000001 80008000
204F0F38 3880FFEC
044F0F38 3880{negAmount}
E2000001 80008000
C2184538 00000001
2C14{amount} 00000000
C2184544 00000001
3880{negAmount} 00000000
28265B8A 00000014
00265B8B 000000{amount}
E2000001 80008000
04248064 000000{y4}
04248068 000000{y2}
04248070 000000{x2}
04248074 000000{x4}
04248D3C 000000{y4}
04248D40 000000{y2}
04248D48 000000{x2}
04248D4C 000000{x4}
204DDF60 465F6C00
044DDF74 000000{y4}
044DDF78 000000{y2}
044DDF80 000000{x2}
044DDF84 000000{x4}
E2000001 80008000


'''

def getPinkBooSpaceCodeSix(amount, negAmount, amountDec):
    return f'''
MP6 - Star Stealing Costs {amountDec} with Pink Boo.
C21B1FB4 00000001
2C04{amount} 00000000
C21B2634 00000001
3880{negAmount} 00000000
'''

def getPinkBooCoinsSpaceCodeSix(amount, negAmount, amountDec):
    return f'''
MP6 - Coin Stealing Costs {amountDec} with Pink Boo.
C21B1F28 00000001
2C03{amount} 00000000
C21B2626 00000001
3880{negAmount} 00000000
'''

def getMinigameReplacement6(hexUno, hexDos, gameUno, gameDos):
    return f'''
MP6 - Minigame Replacement: {gameUno} ➜ {gameDos}
28265BA8 000000{hexUno}
02265BA8 000000{hexDos}
E2000001 80008000
'''

def getOrbModsSix(oneW, twoP, twoW, threeP, threeW, fourP, fourW, fiveP, fiveW, sixP, sixW, sevenP, sevenW, eightP, eightW, nineP, nineW, tenP, tenW, elevenP, elevenW, twelveP, twelveW, thirteenP, thirteenW, fourteenP, fourteenW, fifteenP, fifteenW, sixteenP, sixteenW, seventeenP, seventeenW, eighteenP, eighteenW, ninteenP, ninteenW, twentyP, twentyW, twentyOneP, twentyOneW, twentyTwoP, twentyTwoW, twentyThreeP, twentyThreeW, twentyFourP, twentyFourW, twentyFiveP, twentyFiveW, twentySixP, twentySixW, twentySevenP, twentySevenW, twentyEightP, twentyEightW):
    return f'''
MP6 - Orb Modifier
042BD220 00050505
042BD224 {oneW}{oneW}{oneW}{oneW}
042BD228 {oneW}{oneW}{oneW}{oneW}
042BD22C {oneW}{oneW}{oneW}{oneW}
042BD230 01{twoP}{twoP}{twoP}
042BD234 {twoW}{twoW}{twoW}{twoW}
042BD238 {twoW}{twoW}{twoW}{twoW}
042BD23C {twoW}{twoW}{twoW}{twoW}
042BD240 02{threeP}{threeP}{threeP}
042BD244 {threeW}{threeW}{threeW}{threeW}
042BD248 {threeW}{threeW}{threeW}{threeW}
042BD24C {threeW}{threeW}{threeW}{threeW}
042BD250 03{fourP}{fourP}{fourP}
042BD254 {fourW}{fourW}{fourW}{fourW}
042BD258 {fourW}{fourW}{fourW}{fourW}
042BD25C {fourW}{fourW}{fourW}{fourW}
042BD260 04{fiveP}{fiveP}{fiveP}
042BD264 {fiveW}{fiveW}{fiveW}{fiveW}
042BD268 {fiveW}{fiveW}{fiveW}{fiveW}
042BD26C {fiveW}{fiveW}{fiveW}{fiveW}
042BD270 05{sixP}{sixP}{sixP}
042BD274 {sixW}{sixW}{sixW}{sixW}
042BD278 {sixW}{sixW}{sixW}{sixW}
042BD27C {sixW}{sixW}{sixW}{sixW}
042BD280 06{sevenP}{sevenP}{sevenP}
042BD284 {sevenW}{sevenW}{sevenW}{sevenW}
042BD288 {sevenW}{sevenW}{sevenW}{sevenW}
042BD28C {sevenW}{sevenW}{sevenW}{sevenW}
042BD290 07{eightP}{eightP}{eightP}
042BD294 {eightW}{eightW}{eightW}{eightW}
042BD298 {eightW}{eightW}{eightW}{eightW}
042BD29C {eightW}{eightW}{eightW}{eightW}
042BD2A0 0A{nineP}{nineP}{nineP}
042BD2A4 {nineW}{nineW}{nineW}{nineW}
042BD2A8 {nineW}{nineW}{nineW}{nineW}
042BD2AC {nineW}{nineW}{nineW}{nineW}
042BD2B0 0B{tenP}{tenP}{tenP}
042BD2B4 {tenW}{tenW}{tenW}{tenW}
042BD2B8 {tenW}{tenW}{tenW}{tenW}
042BD2BC {tenW}{tenW}{tenW}{tenW}
042BD2C0 0C{elevenP}{elevenP}{elevenP}
042BD2C4 {elevenW}{elevenW}{elevenW}{elevenW}
042BD2C8 {elevenW}{elevenW}{elevenW}{elevenW}
042BD2CC {elevenW}{elevenW}{elevenW}{elevenW}
042BD2D0 0D{twelveP}{twelveP}{twelveP}
042BD2D4 {twelveW}{twelveW}{twelveW}{twelveW}
042BD2D8 {twelveW}{twelveW}{twelveW}{twelveW}
042BD2DC {twelveW}{twelveW}{twelveW}{twelveW}
042BD2E0 0F{thirteenP}{thirteenP}{thirteenP}
042BD2E4 {thirteenW}{thirteenW}{thirteenW}{thirteenW}
042BD2E8 {thirteenW}{thirteenW}{thirteenW}{thirteenW}
042BD2EC {thirteenW}{thirteenW}{thirteenW}{thirteenW}
042BD2F0 10{fourteenP}{fourteenP}{fourteenP}
042BD2F4 {fourteenW}{fourteenW}{fourteenW}{fourteenW}
042BD2F8 {fourteenW}{fourteenW}{fourteenW}{fourteenW}
042BD2FC {fourteenW}{fourteenW}{fourteenW}{fourteenW}
042BD300 11{fifteenP}{fifteenP}{fifteenP}
042BD304 {fifteenW}{fifteenW}{fifteenW}{fifteenW}
042BD308 {fifteenW}{fifteenW}{fifteenW}{fifteenW}
042BD30C {fifteenW}{fifteenW}{fifteenW}{fifteenW}
042BD310 14{sixteenP}{sixteenP}{sixteenP}
042BD314 {sixteenW}{sixteenW}{sixteenW}{sixteenW}
042BD318 {sixteenW}{sixteenW}{sixteenW}{sixteenW}
042BD31C {sixteenW}{sixteenW}{sixteenW}{sixteenW}
042BD320 15{seventeenP}{seventeenP}{seventeenP}
042BD324 {seventeenW}{seventeenW}{seventeenW}{seventeenW}
042BD328 {seventeenW}{seventeenW}{seventeenW}{seventeenW}
042BD32C {seventeenW}{seventeenW}{seventeenW}{seventeenW}
042BD330 16{eighteenP}{eighteenP}{eighteenP}
042BD334 {eighteenW}{eighteenW}{eighteenW}{eighteenW}
042BD338 {eighteenW}{eighteenW}{eighteenW}{eighteenW}
042BD33C {eighteenW}{eighteenW}{eighteenW}{eighteenW}
042BD340 17{ninteenP}{ninteenP}{ninteenP}
042BD344 {ninteenW}{ninteenW}{ninteenW}{ninteenW}
042BD348 {ninteenW}{ninteenW}{ninteenW}{ninteenW}
042BD34C {ninteenW}{ninteenW}{ninteenW}{ninteenW}
042BD350 18{twentyP}{twentyP}{twentyP}
042BD354 {twentyW}{twentyW}{twentyW}{twentyW}
042BD358 {twentyW}{twentyW}{twentyW}{twentyW}
042BD35C {twentyW}{twentyW}{twentyW}{twentyW}
042BD360 19{twentyOneP}{twentyOneP}{twentyOneP}
042BD364 {twentyOneW}{twentyOneW}{twentyOneW}{twentyOneW}
042BD368 {twentyOneW}{twentyOneW}{twentyOneW}{twentyOneW}
042BD36C {twentyOneW}{twentyOneW}{twentyOneW}{twentyOneW}
042BD370 1E{twentyTwoP}{twentyTwoP}{twentyTwoP}
042BD374 {twentyTwoW}{twentyTwoW}{twentyTwoW}{twentyTwoW}
042BD378 {twentyTwoW}{twentyTwoW}{twentyTwoW}{twentyTwoW}
042BD37C {twentyTwoW}{twentyTwoW}{twentyTwoW}{twentyTwoW}
042BD380 1F{twentyThreeP}{twentyThreeP}{twentyThreeP}
042BD384 {twentyThreeW}{twentyThreeW}{twentyThreeW}{twentyThreeW}
042BD388 {twentyThreeW}{twentyThreeW}{twentyThreeW}{twentyThreeW}
042BD38C {twentyThreeW}{twentyThreeW}{twentyThreeW}{twentyThreeW}
042BD390 2E{twentyFourP}{twentyFourP}{twentyFourP}
042BD394 {twentyFourW}{twentyFourW}{twentyFourW}{twentyFourW}
042BD398 {twentyFourW}{twentyFourW}{twentyFourW}{twentyFourW}
042BD39C {twentyFourW}{twentyFourW}{twentyFourW}{twentyFourW}
042BD3A0 2A{twentyFiveP}{twentyFiveP}{twentyFiveP}
042BD3A4 {twentyFiveW}{twentyFiveW}{twentyFiveW}{twentyFiveW}
042BD3A8 {twentyFiveW}{twentyFiveW}{twentyFiveW}{twentyFiveW}
042BD3AC {twentyFiveW}{twentyFiveW}{twentyFiveW}{twentyFiveW}
042BD3B0 2B{twentySixP}{twentySixP}{twentySixP}
042BD3B4 {twentySixW}{twentySixW}{twentySixW}{twentySixW}
042BD3B8 {twentySixW}{twentySixW}{twentySixW}{twentySixW}
042BD3BC {twentySixW}{twentySixW}{twentySixW}{twentySixW}
042BD3C0 2C{twentySevenP}{twentySevenP}{twentySevenP}
042BD3C4 {twentySevenW}{twentySevenW}{twentySevenW}{twentySevenW}
042BD3C8 {twentySevenW}{twentySevenW}{twentySevenW}{twentySevenW}
042BD3CC {twentySevenW}{twentySevenW}{twentySevenW}{twentySevenW}
042BD3D0 29{twentyEightP}{twentyEightP}{twentyEightP}
042BD3D4 {twentyEightW}{twentyEightW}{twentyEightW}{twentyEightW}
042BD3D8 {twentyEightW}{twentyEightW}{twentyEightW}{twentyEightW}
042BD3DC {twentyEightW}{twentyEightW}{twentyEightW}{twentyEightW}
042BD3E0 FF000000
042BD3E4 00000000
042BD3E8 00000000
042BD3EC 00000000
'''

def getInitialItemsSix(one, two, three, oneItem, twoItem, threeItem):
    return f'''
MP6 - Start with {oneItem}, {twoItem}, and {threeItem}
06003620 00000028
3D808000 618C363C
1C1F0003 7C00E214
7CAC00AE 98A30005
48150114 {one}{two}{three}{one}
{two}{three}{one}{two} {three}{one}{two}{three}
C2153748 00000001
4BEAFED8 00000000
'''

def getCoinStealBaseSix(value, amountDec):
    return f'''
MP6 - Steal Minimum Of {amountDec} Coins from Pink Boo
C21B3498 00000002
3884{value} 9081002C
60000000 00000000
'''

def getSpaceReplaceSix1(spaceHex1, spaceHex2, spaceName, spaceName2):
    return f'''
MP6 - Replace {spaceName} with {spaceName2} (Slot A)
C217590C 00000005
A01F0030 280000{spaceHex1}
40820018 A09F0032
2804FFFF 4082000C
380000{spaceHex2} B01F0030
88030000 00000000
'''

def getSpaceReplaceSix2(spaceHex1, spaceHex2, spaceName, spaceName2):
    return f'''
MP6 - Replace {spaceName} with {spaceName2} (Slot B)
C2175910 00000005
5418CFFE A01F0030
280000{spaceHex1} 40820018
A09F0032 2804FFFF
4082000C 380000{spaceHex2}
B01F0030 00000000
'''

def getStarHandicap(p1, p2, p3, p4):
    return f'''
MP6 - Star Handicap
28265772 00000000
02265780 0000{p1}
02265888 0000{p2}
02265990 0000{p3}
02265A98 0000{p4}
E2000001 80008000
'''

def getStarReplaceSix1(amount, amountDec):
    return f'''
MP6 - Replace Minigame Star with {amountDec}
204ECF10 A883001E
C24ECF10 00000001
{amount} 00000000
E2000001 80008000
'''

def getStarReplaceSix2(amount, amountDec):
    return f'''
MP6 - Replace Orb Star with {amountDec}
204ECF4C A8C70034
C24ECF4C 00000001
{amount} 00000000
E2000001 80008000
'''

def getStarReplaceSix3(amount, amountDec):
    return f'''
MP6 - Replace Happening Star with {amountDec}
204ECF88 88040017
C24ECF88 00000002
{amount} 7C060378
60000000 00000000
E2000001 80008000
'''

def initialCoinsMod6(hex, hexDec):
    return f'''
MP6 - Gain {hexDec} Coins at the Start of the Game
C214B3AC 00000001
3880{hex} 00000000
'''

def getBattleGame6(p1, p2, p3, p4, p5, s1, s2, s3, s4, s5):
    return f'''
MP6 - Battle Minigames Bounties are {s1}, {s2}, {s3}, {s4}, and {s5}
0424BAB0 0000{p1}
0424BAB4 0000{p2}
0424BAB8 0000{p3}
0424BABC 0000{p4}
0424BAC0 0000{p5}
'''

def getZapOrb6(hex, amountDec):
    return f'''
MP6 - Zap Takes {amountDec} Coins
C21AE1B8 00000001
3B60{hex} 00000000
'''

def getFaireFlowerEventStars(value):
    return f'''
MP6 - Always Wager Stars at Faire Square Flower Event
282C0256 0000007D
C24D3C68 00000001
38E00001 00000000
C24D4E34 00000001
38000001 00000000
C24D3C68 00000001
38E00001 00000000
E2000001 80008000
'''

def getFaireFlowerEventCoins(value):
    return f'''
MP6 - Always Wager Coins at Faire Square Flower Event
282C0256 0000007D
C24D3C70 00000001
60000000 00000000
C24D4E3C 00000001
60000000 00000000
C24D3C70 00000001
60000000 00000000
E2000001 80008000
'''