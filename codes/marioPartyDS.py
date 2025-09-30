# ============================================
# Mario Party Toolkit
# Author: Nayla Hanegan (tabitha@tabs.gay)
# Date: 7/3/2024
# License: MIT
# ============================================

def getMinigameReplacementDS(hexUno, hexDos, gameUno, gameDos):
    return f'''
MPDS - Minigame Replacement: {gameUno} -> {gameDos}
520AAA20 000000{hexUno}
020AAA20 000000{hexDos}
D2000000 00000000		
'''