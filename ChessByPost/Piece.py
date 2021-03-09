# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 20:12:30 2021

@author: bfisc
"""

from enum import Enum
import numpy

WHITE = 1
BLACK = -1

class Side(Enum):
    WHITE = 1
    BLACK = -1

class Diagonal():
    FORWARD_RIGHT = numpy.array([-1, 1])
    FORWARD_LEFT = numpy.array([1, 1])
    BACKWARD_RIGHT = numpy.array([-1, -1])
    BACKWARD_LEFT = numpy.array([1, -1])

class Piece:
        
    def __init__(self, code, side, x, y):
        self.code = code
        self.side = side
        self.hasMoved = False
        self.x = x
        self.y = y
        
    def Move(self, board, x, y):
        board[y][x] = self
        board[self.y][self.x] = 0
        self.x = x
        self.y = y
        self.hasMoved = True
        
    def Is_Valid_Coordinate(self, x, y):
        xValid = 0 <= x <= 7
        yValid = 0 <= y <= 7
        return xValid and yValid
        
    def Is_Valid_Move(self, board, deltaX, deltaY, canTakePiece):
        newX = self.x + deltaX
        newY = self.y + deltaY
        
        if not self.Is_Valid_Coordinate(newX, newY):
            return False
        
        tile = board[newY][newX]

        if isinstance(tile, Piece):
            if canTakePiece and tile.side != self.side:
                    return True
            return False
        return True
    
    def Can_Move_Forward(self, board, n, canTakePiece = True):
        return self.Is_Valid_Move(board, 0, n * self.side, canTakePiece)
    
    def Can_Move_Backward(self, board, n, canTakePiece = True):
        return self.Is_Valid_Move(board, 0, n * -self.side, canTakePiece)
    
    def Can_Move_Right(self, board, n, canTakePiece = True):
        return self.Is_Valid_Move(board, n * -self.side, 0, canTakePiece)
    
    def Can_Move_Left(self, board, n, canTakePiece = True):
        return self.Is_Valid_Move(board, n * self.side, 0, canTakePiece)
    
    def Can_Move_Diagonal(self, board, direction, n, canTakePiece = True):
        deltaX = n * direction[0] * self.side
        deltaY = n * direction[1] * self.side
        return self.Is_Valid_Move(board, deltaX, deltaY, canTakePiece)
    
    def Get_Forward_Coordinate(self, n):
        x = self.x
        y = self.y + n * self.side
        return (x, y)

    def Get_Backward_Coordinate(self, n):
        x = self.x
        y = self.y - n * self.side
        return (x, y)
    
    def Get_Right_Coordinate(self, n):
        x = self.x + n * -self.side
        y = self.y
        return (x, y)
    
    def Get_Left_Coordinate(self, n):
        x = self.x + n * self.side
        y = self.y
        return (x, y)
    
    def Get_Diagonal_Coordinate(self, direction, n):
        x = self.x + direction[0] * n * self.side
        y = self.y + direction[1] * n * self.side
        return (x, y)
    
    def Get_Valid_Forward_Moves(self, board, moves = [], n = 7, canTakePiece = True):
        for i in range(1, n + 1):
            if self.Can_Move_Forward(board, i, canTakePiece):
                coord = self.Get_Forward_Coordinate(i)
                moves.append(coord)
                if isinstance(board[coord[1]][coord[0]], Piece):
                    break
            else:
                break
        return moves
    
    def Get_Valid_Backward_Moves(self, board, moves = [], n = 7, canTakePiece = True):
        for i in range(1, n + 1):
            if self.Can_Move_Backward(board, i, canTakePiece):
                coord = self.Get_Backward_Coordinate(i)
                moves.append(coord)
                if isinstance(board[coord[1]][coord[0]], Piece):
                    break
            else:
                break
        return moves
    
    
    def Get_Valid_Right_Moves(self, board, moves = [], n = 7, canTakePiece = True):
        # Check right
        for i in range(1, n + 1):
            if self.Can_Move_Right(board, i, canTakePiece):
                coord = self.Get_Right_Coordinate(i)
                moves.append(coord)
                if isinstance(board[coord[1]][coord[0]], Piece):
                    break
            else:
                break
        return moves

    def Get_Valid_Left_Moves(self, board, moves = [], n = 7, canTakePiece = True):
        for i in range(1, n + 1):
            if self.Can_Move_Left(board, i, canTakePiece):
                coord = self.Get_Left_Coordinate(i)
                moves.append(coord)
                if isinstance(board[coord[1]][coord[0]], Piece):
                    break
            else:
                break
        return moves
    
    def Get_Valid_Forward_Diagonal_Moves(self, board, moves = [], n = 7, canTakePiece = True):
        # Check forward right diagonal
        for i in range(1, n + 1):
            if self.Can_Move_Diagonal(board, Diagonal.FORWARD_RIGHT, i, canTakePiece):
                coord = self.Get_Diagonal_Coordinate(Diagonal.FORWARD_RIGHT, i)
                moves.append(coord)
                if isinstance(board[coord[1]][coord[0]], Piece):
                    break
            else:
                break
            
        # Check forward left diagonal
        for i in range(1, n + 1):
            if self.Can_Move_Diagonal(board, Diagonal.FORWARD_LEFT, i, canTakePiece):
                coord = self.Get_Diagonal_Coordinate(Diagonal.FORWARD_LEFT, i)
                moves.append(coord)
                if isinstance(board[coord[1]][coord[0]], Piece):
                    break
            else:
                break
        return moves
    
    def Get_Valid_Backward_Diagonal_Moves(self, board, moves = [], n = 7, canTakePiece = True):
        # Check backward right diagonal
        for i in range(1, n + 1):
            if self.Can_Move_Diagonal(board, Diagonal.BACKWARD_RIGHT, i, canTakePiece):
                coord = self.Get_Diagonal_Coordinate(Diagonal.BACKWARD_RIGHT, i)
                moves.append(coord)
                if isinstance(board[coord[1]][coord[0]], Piece):
                    break
            else:
                break
            
        # Check backward left diagonal
        for i in range(1, n + 1):
            if self.Can_Move_Diagonal(board, Diagonal.BACKWARD_LEFT, i, canTakePiece):
                coord = self.Get_Diagonal_Coordinate(Diagonal.BACKWARD_LEFT, i)
                moves.append(coord)
                if isinstance(board[coord[1]][coord[0]], Piece):
                    break
            else:
                break
        return moves
    
    def Get_Valid_Forward_And_Backward_Moves(self, board, moves = [], n = 7):
        self.Get_Valid_Forward_Moves(board, moves, n)
        self.Get_Valid_Backward_Moves(board, moves, n)
        return moves
    
    def Get_Valid_Side_Moves(self, board, moves = [], n = 7):
        self.Get_Valid_Right_Moves(board, moves, n)
        self.Get_Valid_Left_Moves(board, moves, n)
        return moves
    
    def Get_Valid_Diagonal_Moves(self, board, moves = [], n = 7):
        self.Get_Valid_Forward_Diagonal_Moves(board, moves, n)
        self.Get_Valid_Backward_Diagonal_Moves(board, moves, n)
        return moves

    def Get_Copy(self):
        print("base")

class Pawn(Piece):
    code = 1
    name = "Pawn"
    
    def __init__(self, side, x, y):
        Piece.__init__(self, Pawn.code, side, x, y)
        
    def Get_Valid_Moves(self, board):
        validMoves = []
        if not self.hasMoved:
            self.Get_Valid_Forward_Moves(board, validMoves, n=2, canTakePiece=False)
        else:
            self.Get_Valid_Forward_Moves(board, validMoves, n=1, canTakePiece=False)
            
        deltaX = Diagonal.FORWARD_RIGHT[0] * self.side
        deltaY = Diagonal.FORWARD_RIGHT[1] * self.side
        if self.Is_Valid_Move(board, deltaX, deltaY, True) and board[self.y + deltaY][self.x + deltaX] != 0:
            validMoves.append(self.Get_Diagonal_Coordinate(Diagonal.FORWARD_RIGHT, 1))

        deltaX = Diagonal.FORWARD_LEFT[0] * self.side
        deltaY = Diagonal.FORWARD_LEFT[1] * self.side
        if self.Is_Valid_Move(board, deltaX, deltaY, True) and board[self.y + deltaY][self.x + deltaX] != 0:
            validMoves.append(self.Get_Diagonal_Coordinate(Diagonal.FORWARD_LEFT, 1))
        
        # todo en passant
        # todo promotion
        return validMoves
    
    def Get_Copy(self):
        piece = Pawn(self.side, self.x, self.y)
        piece.hasMoved = self.hasMoved
        return piece
    

class Rook(Piece):
    code = 2
    name = "Rook"
    
    def __init__(self, side, x, y):
        Piece.__init__(self, Rook.code, side, x, y)
        
    def Get_Valid_Moves(self, board):
        validMoves = []
        self.Get_Valid_Forward_And_Backward_Moves(board, validMoves)
        self.Get_Valid_Side_Moves(board, validMoves)
        return validMoves
    
    def Get_Copy(self):
        piece = Rook(self.side, self.x, self.y)
        piece.hasMoved = self.hasMoved
        return piece
    

class Knight(Piece):
    code = 3
    name = "Knight"
    
    def __init__(self, side, x, y):
        Piece.__init__(self, Knight.code, side, x, y)
        
    def Get_Valid_Moves(self, board):
        validMoves = []
        deltaXYList = [[-2, -1], [-2, 1], [-1, -2], [-1, 2], [1, -2], [1, 2], [2, -1], [2, 1]]
        
        for delta in deltaXYList:
            if self.Is_Valid_Move(board, delta[0], delta[1], True):
                validMoves.append((self.x + delta[0], self.y + delta[1]))

        return validMoves
    
    def Get_Copy(self):
        piece = Knight(self.side, self.x, self.y)
        piece.hasMoved = self.hasMoved
        return piece
    

class Bishop(Piece):
    code = 4
    name = "Bishop"
    
    def __init__(self, side, x, y):
        Piece.__init__(self, Bishop.code, side, x, y)
        
    def Get_Valid_Moves(self, board):
        validMoves = []
        self.Get_Valid_Diagonal_Moves(board, validMoves)
        return validMoves
    
    def Get_Copy(self):
        piece = Bishop(self.side, self.x, self.y)
        piece.hasMoved = self.hasMoved
        return piece
    

class Queen(Piece):
    code = 5
    name = "Queen"
    
    def __init__(self, side, x, y):
        Piece.__init__(self, Queen.code, side, x, y)
        
    def Get_Valid_Moves(self, board):
        validMoves = []
        self.Get_Valid_Forward_And_Backward_Moves(board, validMoves)
        self.Get_Valid_Side_Moves(board, validMoves)
        self.Get_Valid_Diagonal_Moves(board, validMoves)
        return validMoves
    
    def Get_Copy(self):
        piece = Queen(self.side, self.x, self.y)
        piece.hasMoved = self.hasMoved
        return piece
    

class King(Piece):
    code = 6
    name = "King"
    
    def __init__(self, side, x, y):
        Piece.__init__(self, King.code, side, x, y)
        
    def Get_Castle_Left(self, board, validMoves):
        shift = (self.side + 1) >> 1
        x = 7 - 7 * shift
        rook = board[self.y][x]
        if not isinstance(rook, Rook) or rook.hasMoved:
            return False
        n = x + self.side * self.x - 1
        rookCanMove = rook.Can_Move_Left(board, n, False)
        if rookCanMove:
            validMoves.append((self.x - 2 * self.side, self.y))
        return rookCanMove
    
    def Get_Castle_Right(self, board, validMoves):
        shift = (self.side + 1) >> 1
        x = 7 * shift
        rook = board[self.y][x]
        if not isinstance(rook, Rook) or rook.hasMoved:
            return False
        n = x - self.side * self.x - 1
        rookCanMove = rook.Can_Move_Right(board, n, False)
        if rookCanMove:
            validMoves.append((self.x + 2 * self.side, self.y))
        return rookCanMove
        
    def Get_Valid_Moves(self, board):
        validMoves = []
        self.Get_Valid_Forward_And_Backward_Moves(board, validMoves, n=1)
        self.Get_Valid_Side_Moves(board, validMoves, n=1)
        self.Get_Valid_Diagonal_Moves(board, validMoves, n=1)
        # Check for castling
        if not self.hasMoved:
            self.Get_Castle_Left(board, validMoves)
            self.Get_Castle_Right(board, validMoves)
        return validMoves
    
    def Get_Copy(self):
        piece = King(self.side, self.x, self.y)
        piece.hasMoved = self.hasMoved
        return piece
    
    