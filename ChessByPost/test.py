# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 20:11:04 2021

@author: bfisc
"""

from ChessByPost import Controller

p1 = "Player 1"
p2 = "Player 2"

b = Controller.Controller(p1, p2)

if True:
    # Return code test
    b.Do_Move_Algebraic_Notation(p1, "j2", "h4", False) # Invalid Coord
    b.Do_Move_Algebraic_Notation(p1, "h2", "h4", False) # Successful

    b.Do_Move_Algebraic_Notation(p2, "e7", "e4", False) # Invalid Move
    b.Do_Move_Algebraic_Notation(p1, "g2", "g4", False) # Not player's turn
    b.Do_Move_Algebraic_Notation(p2, "e6", "e5", False) # No piece at coord
    b.Do_Move_Algebraic_Notation(p2, "e7", "e6", False)
    b.Do_Move_Algebraic_Notation("Player 3", "g1", "h3", False) # No such player

    b.Do_Move_Algebraic_Notation(p1, "f2", "f4", False)
    b.Do_Move_Algebraic_Notation(p2, "d8", "h4", False) # Successful move king in check
    b.Do_Move_Algebraic_Notation(p1, "g2", "b3", False) # Invalid move king in check
    b.Do_Move_Algebraic_Notation(p1, "g2", "g3", True) # Get king out of check
    b.Do_Move_Algebraic_Notation(p2, "h4", "g3", True) # Successful move checkmate
    b.Do_Move_Algebraic_Notation(p1, "c2", "c3", False) # Gameover

if False:
    # p1 Left castling test
    b.Do_Move_Algebraic_Notation(p1, "d2", "d4", False) # Move pawn out of the way
    b.Do_Move_Algebraic_Notation(p2, "a7", "a6", False)
    b.Do_Move_Algebraic_Notation(p1, "c1", "e3", False) # Move bishop
    b.Do_Move_Algebraic_Notation(p2, "b7", "b6", False)
    b.Do_Move_Algebraic_Notation(p1, "b1", "a3", False) # Move knight
    b.Do_Move_Algebraic_Notation(p2, "c7", "c6", False)
    b.Do_Move_Algebraic_Notation(p1, "d1", "d3", False) # Move the queen
    b.Do_Move_Algebraic_Notation(p2, "d7", "d6", False)
    b.Do_Move_Algebraic_Notation(p1, "e1", "c1") # castle King

if False:
    # p1 right castling test
    b.Do_Move_Algebraic_Notation(p1, "e2", "e4", False) # Move pawn out of the way
    b.Do_Move_Algebraic_Notation(p2, "a7", "a6", False)
    b.Do_Move_Algebraic_Notation(p1, "f1", "d3", False) # Move bishop
    b.Do_Move_Algebraic_Notation(p2, "b7", "b6", False)
    b.Do_Move_Algebraic_Notation(p1, "g1", "h3", False) # Move knight
    b.Do_Move_Algebraic_Notation(p2, "c7", "c6", False)
    b.Do_Move_Algebraic_Notation(p1, "e1", "g1") # castle King
    
if False:
    # p2 right castling test
    b.Do_Move_Algebraic_Notation(p1, "a2", "a3", False)
    b.Do_Move_Algebraic_Notation(p2, "d7", "d5", False) # Move pawn out of the way
    b.Do_Move_Algebraic_Notation(p1, "b2", "b3", False)
    b.Do_Move_Algebraic_Notation(p2, "c8", "e6", False) # Move bishop
    b.Do_Move_Algebraic_Notation(p1, "c2", "c3", False)
    b.Do_Move_Algebraic_Notation(p2, "b8", "a6", False) # Move knight
    b.Do_Move_Algebraic_Notation(p1, "d2", "d3", False)
    b.Do_Move_Algebraic_Notation(p2, "d8", "d7", False) # Move the queen
    b.Do_Move_Algebraic_Notation(p1, "e2", "e3", False)
    b.Do_Move_Algebraic_Notation(p2, "e8", "c8") # castle King
    
if False:
    # p2 right castling test
    b.Do_Move_Algebraic_Notation(p1, "a2", "a3", False)
    b.Do_Move_Algebraic_Notation(p2, "e7", "e5", False) # Move pawn out of the way
    b.Do_Move_Algebraic_Notation(p1, "b2", "b3", False)
    b.Do_Move_Algebraic_Notation(p2, "f8", "d6", False) # Move bishop
    b.Do_Move_Algebraic_Notation(p1, "c2", "c3", False)
    b.Do_Move_Algebraic_Notation(p2, "g8", "h6", False) # Move knight
    b.Do_Move_Algebraic_Notation(p1, "d2", "d3", False)
    b.Do_Move_Algebraic_Notation(p2, "e8", "g8") # castle King


if False:
    # Fools mate for testing checkmate
    b.Do_Move_Algebraic_Notation(p1, "f2", "f3")
    b.Do_Move_Algebraic_Notation(p2, "e7", "e6")
    b.Do_Move_Algebraic_Notation(p1, "g2", "g4")
    b.Do_Move_Algebraic_Notation(p2, "d8", "h4")

if False:
    # Just check for testing checkmate
    b.Do_Move_Algebraic_Notation(p1, "f2", "f3")
    b.Do_Move_Algebraic_Notation(p2, "e7", "e6")
    b.Do_Move_Algebraic_Notation(p1, "a2", "a4")
    b.Do_Move_Algebraic_Notation(p2, "d8", "h4")
    
if False:
    # pawn logic
    b.Do_Move_Algebraic_Notation(p1, "a2", "a3")
    b.Do_Move_Algebraic_Notation(p2, "c7", "c6")
    b.Do_Move_Algebraic_Notation(p1, "d2", "d3")
    b.Do_Move_Algebraic_Notation(p2, "g7", "g6")
    
'''
Todo:
    Add letters and number to board image
    Finish pawn movement:
        en passant
        promotion
'''
