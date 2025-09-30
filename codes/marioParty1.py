# ============================================
# Mario Party Toolkit
# Author: Tabitha Hanegan (tabitha@tabs.gay)
# Date: 09/30/2025
# License: MIT
# ============================================

def getBlueSpaceCodeOne(amount, switch, amountDec, switchDec):
    return f'''
MP1 - Blue Spaces Give {amountDec} Coins: {switchDec}
81057D80 3408
81057D82 000{switch}
81057D84 1100
81057D86 0003
81057D88 3410
81057D8A {amount}
81057D8C 5440
81057D8E 0001
81057D90 0010
81057D92 8040
0407FBE0 3BC0
'''

def getRedSpaceCodeOne(amount, switch, amountDec, switchDec):
    return f'''
MP1 - Red Spaces Take Away {amountDec} Coins: {switchDec}
81057DD8 3408
81057DDA 000{switch}
81057DDC 1100
81057DDE 0003
81057DE0 3410
81057DE2 {amount}
81057DE4 5440
81057DE6 0001
81057DE8 0010
81057DEA 8040
'''

def getMinigameReplacement1(hexUno, hexDos, gameUno, gameDos):
    return f'''
MP1 - Minigame Replacement: {gameUno} -> {gameDos}
D10ED5DE 00{hexUno}
810ED5DE 00{hexDos}		
'''

def getStarHandicapP1(p1, p2, p3, p4):
    return f'''
MP1 - Star Handicap
D10FCDA8 0000
D10F09F6 0062
D10FCDB2 0000
D10F32B8 0000
810F32BC {p1}
D10FCDA8 0000
D10F09F6 0062
D10FCDB2 0000
D10F32B8 0000
810F32EC {p2}
D10FCDA8 0000
D10F09F6 0062
D10FCDB2 0000
D10F32B8 0000
810F331C {p3}
D10FCDA8 0000
D10F09F6 0062
D10FCDB2 0000
D10F32B8 0000
810F334C {p4}
'''

def getBlockWeights(one, two, three, four, five, six):
    return f'''
MP1 - Custom Item Block Weights
81040828 3050
8104082A 00FF
8104082C 2A02
8104082E 00{one}
81040830 1040
81040832 000D
81040834 2402
81040836 00{two}
81040838 0000
8104083A 0000
8104083C 0000
8104083E 0000
81040864 2A02
81040866 00{two}
81040868 1040
8104086A 000D
8104086C 2402
8104086E 00{three}
810408A0 2A02
810408A2 00{three}
810408A4 1040
810408A6 000D
810408A8 2402
810408AA 00{four}
810408DC 2A02
810408DE 00{four}
810408E0 1040
810408E2 000D
810408E4 2402
810408E6 00{five}
81040918 2A02
8104091A 00{five}
8104091C 1040
8104091E 0012
81040920 2402
81040922 00{six}
'''

def getStarSpaceCodeOne(amount, negAmount, starPrice):
    return f'''
MP1 - Stars Cost {starPrice} Coins
D10F778E 0014
810F778E {amount}
D10F6D5A 0014
810F6D5A {amount}
D10F6CD2 0014
810F6CD2 {amount}
D10F6C58 0014
810F6C58 {amount}
D10F6E9A FFEC
810F6E9A {negAmount}
D10F6E12 FFEC
810F6E12 {negAmount}
'''
