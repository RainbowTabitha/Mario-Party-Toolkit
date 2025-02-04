# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (naylahanegan@gmail.com)
# Date: 7/12/2024
# License: MIT
# ============================================

def getBlueSpaceCodeFive(amount, amountDec):
    return f'''
MP5 - Blue Spaces Give {amountDec} Coins
C20A9F5C 00000001
3880{amount} 00000000
'''

def getRedSpaceCodeFive(amount, amountDec):
    return f'''
MP5 - Red Spaces Take Away {amountDec} Coins
C20AA160 00000001
3880{amount} 00000000
'''

def getMinigameCodeFive(amount, amountDec):
    return f'''
MP5 - Minigames Award {amountDec} Coins
C2035A90 00000017
3DC08022 61CEA4C5
89EE0000 2C0F000F
41820090 2C0F0017
41820088 2C0F0044
41820080 2C0F004A
41820078 2C0F0022
41820070 2C0F0023
41820068 2C0F0024
41820060 2C0F0025
41820058 2C0F0026
41820050 2C0F0027
41820048 2C0F0046
41820040 2C0F0047
41820038 2C0F0048
41820030 3DC08022
61CEA09C A1EE0000
2C0F0000 4182000C
39E0{amount} B1EE0000
39CE0108 3A100001
2C100003 4081FFE0
3800FFFF 39C00000
39E00000 3A000000
60000000 00000000
'''

def getStarSpaceCodeFive(amount, negAmount, amountDec):
    return f'''
MP5 - Stars Cost {amountDec} Coins
C20AFDB0 00000001
2C03{amount} 00000000
C20AFF9C 00000001
3880{negAmount} 00000000
'''

def getKoopaBankFive(amount, amountDec):
    return f'''
MP5 - Koopa Bank Deposits are {amountDec} Coins
C20E7090 00000001
3B20{amount} 00000000
'''

def getWigglerSpaceCodeFive(amount, negAmount, amountDec):
    return f'''
MP5 - Stars Cost {amountDec} Coins from Wiggler
C20DB528 00000001
2C03{amount} 00000000
C20DBB40 00000001
3880{negAmount} 00000000
'''

def getChompSpaceCodeFive(amount, negAmount, amountDec):
    return f'''
MP4 - Star Stealing Costs {amountDec} with Chain Chomp.
C20F5F34 00000001
2C03{amount} 00000000
C20F630C 00000001
3880{negAmount} 00000000
'''

def getMinigameReplacement5(hexUno, hexDos, gameUno, gameDos):
    return f'''
MP5 - Minigame Replacement: {gameUno} ➜ {gameDos}
2822A4C4 000000{hexUno}
0222A4C4 000000{hexDos}
E2000001 80008000
'''

def getCapsuleModsFive(oneP, oneW, twoP, twoW, threeP, threeW, fourP, fourW, fiveP, fiveW, sixP, sixW, sevenP, sevenW, eightP, eightW, nineP, nineW, tenP, tenW, elevenP, elevenW, twelveP, twelveW, thirteenP, thirteenW, fourteenP, fourteenW, fifteenP, fifteenW, sixteenP, sixteenW, seventeenP, seventeenW, eighteenP, eighteenW, ninteenP, ninteenW, twentyP, twentyW, twentyOneP, twentyOneW, twentyTwoP, twentyTwoW, twentyThreeP, twentyThreeW, twentyFourP, twentyFourW, twentyFiveP, twentyFiveW, twentySixP, twentySixW, twentySevenP, twentySevenW, twentyEightP, twentyEightW, twentyNineP, twentyNineW):
    return f'''
MP5 - Capsule Modifer
C20C8FA0 00000024
9421FFF0 7C0802A6
90010014 93E10000
48000081 60000000
00{oneW}0005 00{twoW}0100
00{threeW}0200 00{fourW}0300
00{fiveW}0400 00{sixW}0500
00{sevenW}0605 00{eightW}0A00
00{nineW}0B00 00{tenW}0C00
00{elevenW}0D00 00{twelveW}0E00
00{thirteenW}0F00 00{fourteenW}1000
00{fifteenW}1100 00{sixteenW}1400
00{seventeenW}1500 00{eighteenW}1600
00{ninteenW}1700 00{twentyW}1800
00{twentyOneW}1900 00{twentyTwoW}1E00
00{twentyThreeW}1F00 00{twentyFourW}2000
00{twentyFiveW}2100 00{twentySixW}2200
00{twentySevenW}2300 00{twentyEightW}2400
00{twentyNineW}2500 00000000
7CE802A6 38E70004
38600000 38800000
2C030074 41820014
7CA71A2E 7C842A14
38630004 4BFFFFEC
3CA08003 60A5B0F4
7CA903A6 7C832378
4E800421 38800000
38A00000 2C050074
41820024 7CC72A2E
7C661850 2C030000
40A00008 48000010
38840001 38A50004
4BFFFFDC 1C840004
38840002 7C6720AE
83E10000 80010014
7C0803A6 38210010
4E800020 00000000
001CA233 000000{oneP}
001CA24F 000000{twoP}
001CA26B 000000{threeP}
001CA287 000000{fourP}
001CA2A3 000000{fiveP}
001CA2CF 000000{sixP}
001CA2DB 000000{sevenP}
001CA34B 000000{eightP}
001CA367 000000{nineP}
001CA383 000000{tenP}
001CA39F 000000{elevenP}
001CA3BB 000000{twelveP}
001CA3D7 000000{thirteenP}
001CA3F3 000000{fourteenP}
001CA40F 000000{fifteenP}
001CA463 000000{sixteenP}
001CA47F 000000{seventeenP}
001CA49B 000000{eighteenP}
001CA4B7 000000{ninteenP}
001CA4D3 000000{twentyP}
001CA4EF 000000{twentyOneP}
001CA57B 000000{twentyTwoP}
001CA597 000000{twentyThreeP}
001CA5B3 000000{twentyFourP}
001CA5CF 000000{twentyFiveP}
001CA5EB 000000{twentySixP}
001CA607 000000{twentySevenP}
001CA623 000000{twentyEightP}
001CA63F 000000{twentyNineP}
'''

def getCoinStealBaseFive(value, amountDec):
    return f'''
MP5 - Steal Minimum Of {amountDec} Coins from Chain Chomp
C20F75A8 00000002
3B7B{value} 7C9B00D0
60000000 00000000
'''

def getStarReplaceFive1(amount, amountDec):
    return f'''
MP5 - Replace Minigame Star with {amountDec}
2046871C A81D0022
C246871C 00000001
{amount} 00000000
E2000001 80008000
'''

def getStarReplaceFive2(amount, amountDec):
    return f'''
MP5 - Replace Orb Star with {amountDec}
20468724 A81D0026
C2468724 00000001
{amount} 00000000
E2000001 80008000
'''

def getStarReplaceFive3(amount, amountDec):
    return f'''
MP5 - Replace Happening Star with {amountDec}
2046872C 881D0017
C246872C 00000001
{amount} 7C000378
60000000 00000000
E2000001 80008000
'''

def getStarHandicap(p1, p2, p3, p4):
    return f'''
MP5 - Star Handicap
28288862 00000060
0045583F 0000{p1}
00455840 0000{p2}
00455841 0000{p3}
00455842 0000{p4}
E2000001 80008000
'''

def getUnderseaShell(value, text):
    return f'''
MP5 - Undersea Dream: Seashells Only Give {text}
004886EF 000000{value}
'''

def initialCoinsMod5(hex, hexDec):
    return f'''
MP5 - Gain {hexDec} Coins at the Start of the Game
C208C8E6 00000001
3880{hex} 00000000
'''

def getBattleGame5(p1, p2, p3, p4, p5, s1, s2, s3, s4, s5):
    return f'''
MP5 - Battle Minigames Bounties are {s1}, {s2}, {s3}, {s4}, and {s5}
041CBFFC 0000{p1}
041CC000 0000{p2}
041CC004 0000{p3}
041C0008 0000{p4}
041C000C 0000{p5}
'''