# -*- coding: utf-8 -*-
"""
Created on Fri Mar  5 00:37:34 2021

@author: bfisc
"""

from . import Piece

class Player():
    def __init__(self, name, side):
        self.name = name
        self.side = side
        self.pieces = []
        self.capturedPieces = []
        self.Create_Pieces()
        return
    
    def Create_Pieces(self):
        shift = (-self.side + 1) >> 1
        for k in range(8):
            self.pieces.append(Piece.Pawn(self.side, k, 1 + 5 * shift))
            
        self.pieces.append(Piece.Rook(self.side, 0, 7 * shift))
        self.pieces.append(Piece.Rook(self.side, 7, 7 * shift))
        
        self.pieces.append(Piece.Knight(self.side, 1, 7 * shift))
        self.pieces.append(Piece.Knight(self.side, 6, 7 * shift))
        
        self.pieces.append(Piece.Bishop(self.side, 2, 7 * shift))
        self.pieces.append(Piece.Bishop(self.side, 5, 7 * shift))
        
        self.pieces.append(Piece.Queen(self.side, 3, 7 * shift))
        
        self.king = Piece.King(self.side, 4, 7 * shift)
        self.pieces.append(self.king)
             
    def Place_Pieces(self, board):
        for piece in self.pieces:
            board[piece.y][piece.x] = piece
        
    def Capture_Piece(self, piece):
        print("{} captured!".format(piece.name))
        self.capturedPieces.append(piece)
        print("Captured pieces: {}".format(", ".join(self.Get_Captured_Piece_Names())))
        
    def Get_Captured_Piece_Names(self):
        return [x.name for x in self.capturedPieces]
    
    def Do_Move(self, board, x1, y1, x2, y2):
        piece = board[y1][x1]
        goalTile = board[y2][x2]
        if isinstance(goalTile, Piece.Piece):
            self.Capture_Piece(goalTile)
        piece.Move(board, x2, y2)
        print("{} to ({}, {})".format(piece.name, x2, y2))
        if isinstance(piece, Piece.King) and abs(x2 - x1) == 2:
            if (x2 - x1) > 0:
                newX1 = 7
                newX2 = x1 + 1
            else:
                newX1 = 0
                newX2 = x1 - 1
            print("{} at ({}, {})".format(board[y1][newX1].name, newX1, y2))
            self.Do_Move(board, newX1, y2, newX2, y2)
        return
