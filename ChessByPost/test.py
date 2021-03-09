# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 20:11:04 2021

@author: bfisc
"""

import Chess

def Move_Coord(player, pos1, pos2, display = True):
    x1 = (ord(pos1[0].lower()) - 96) - 1
    y1 = int(pos1[1]) - 1
    x2 = (ord(pos2[0].lower()) - 96) - 1
    y2 = int(pos2[1]) - 1
    b.Do_Move(player, x1, y1, x2, y2)
    if display:
        b.Display_Board(b.board)
        
p1 = "Player 1"
p2 = "Player 2"

b = Chess.Controller(p1, p2)

if False:
    # p1 Left castling test
    Move_Coord(p1, "d2", "d4", False) # Move pawn out of the way
    Move_Coord(p2, "a7", "a6", False)
    Move_Coord(p1, "c1", "e3", False) # Move bishop
    Move_Coord(p2, "b7", "b6", False)
    Move_Coord(p1, "b1", "a3", False) # Move knight
    Move_Coord(p2, "c7", "c6", False)
    Move_Coord(p1, "d1", "d3", False) # Move the queen
    Move_Coord(p2, "d7", "d6", False)
    Move_Coord(p1, "e1", "c1") # castle King

if False:
    # p1 right castling test
    Move_Coord(p1, "e2", "e4", False) # Move pawn out of the way
    Move_Coord(p2, "a7", "a6", False)
    Move_Coord(p1, "f1", "d3", False) # Move bishop
    Move_Coord(p2, "b7", "b6", False)
    Move_Coord(p1, "g1", "h3", False) # Move knight
    Move_Coord(p2, "c7", "c6", False)
    Move_Coord(p1, "e1", "g1") # castle King
    
if False:
    # p2 right castling test
    Move_Coord(p1, "a2", "a3", False)
    Move_Coord(p2, "d7", "d5", False) # Move pawn out of the way
    Move_Coord(p1, "b2", "b3", False)
    Move_Coord(p2, "c8", "e6", False) # Move bishop
    Move_Coord(p1, "c2", "c3", False)
    Move_Coord(p2, "b8", "a6", False) # Move knight
    Move_Coord(p1, "d2", "d3", False)
    Move_Coord(p2, "d8", "d7", False) # Move the queen
    Move_Coord(p1, "e2", "e3", False)
    Move_Coord(p2, "e8", "c8") # castle King
    
if False:
    # p2 right castling test
    Move_Coord(p1, "a2", "a3", False)
    Move_Coord(p2, "e7", "e5", False) # Move pawn out of the way
    Move_Coord(p1, "b2", "b3", False)
    Move_Coord(p2, "f8", "d6", False) # Move bishop
    Move_Coord(p1, "c2", "c3", False)
    Move_Coord(p2, "g8", "h6", False) # Move knight
    Move_Coord(p1, "d2", "d3", False)
    Move_Coord(p2, "e8", "g8") # castle King


if False:
    # Fools mate for testing checkmate
    Move_Coord(p1, "f2", "f3")
    Move_Coord(p2, "e7", "e6")
    Move_Coord(p1, "g2", "g4")
    Move_Coord(p2, "d8", "h4")

if False:
    # Just check for testing checkmate
    Move_Coord(p1, "f2", "f3")
    Move_Coord(p2, "e7", "e6")
    Move_Coord(p1, "a2", "a4")
    Move_Coord(p2, "d8", "h4")
    
if False:
    # Fucking pawn logic
    Move_Coord(p1, "a2", "a3")
    Move_Coord(p2, "c7", "c6")
    Move_Coord(p1, "d2", "d3")
    Move_Coord(p2, "g7", "g6")
    
'''
Todo:
    Create controller:
        Detect when king is in check
        Detect checkmate (i.e. gameover)
        Keep the eventual discord integration in mind:
            Try to keep things tied to posted events (ex. Player_Move(white, ...))
    Add letters and number to board image
'''
