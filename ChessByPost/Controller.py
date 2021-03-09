# -*- coding: utf-8 -*-
"""
Created on Tue Mar  2 20:15:19 2021

@author: bfisc
"""

from . import Piece
from . import Player
import cv2
import os

this_dir, this_filename = os.path.split(__file__)
IMAGE_PATH = os.path.join(this_dir, "images")

class Controller():
    def __init__(self, name1, name2):
        self.isGameOver = False
        self.player1 = Player.Player(name1, Piece.WHITE)
        self.player2 = Player.Player(name2, Piece.BLACK)
        self.playersDict = {}
        self.playersDict[name1] = self.player1
        self.playersDict[name2] = self.player2
        self.turn = self.playersDict[name1].side
        self.board = self.Create_Board()
        self.player1.Place_Pieces(self.board)
        self.player2.Place_Pieces(self.board)
        self.Print_Board(self.board)
        
    def Create_Board(self):
        board = []
        for i in range(8):
            row = []
            for j in range(8):
                row.append(0)
            board.append(row)
        return board
    
    def Get_Board_Copy(self, board):
        newBoard = self.Create_Board()
        for y in range(len(board)):
            for x in range(len(board[y])):
                tile = board[y][x]
                if isinstance(tile, Piece.Piece):
                    piece = tile.Get_Copy()
                    newBoard[y][x] = piece
        return newBoard

    def Print_Board(self, board):
        for row in board:
            output = []
            for col in row:
                if isinstance(col, Piece.Piece):
                    side = "W"
                    if col.side == Piece.BLACK:
                        side = "B"
                    output.append(side + str(col.code))
                else:
                    output.append("00")
            print(output)
        print()
      
    def Get_Board_Image(self, board):
        boardImg = cv2.imread(os.path.join(IMAGE_PATH, "empty_board.png"))
        print(os.path.join(IMAGE_PATH, "empty_board.png"))
        for y in range(len(board)):
            for x in range(len(board[0])):
                tile = board[y][x]
                if isinstance(tile, Piece.Piece):
                    pieceImg = cv2.imread(os.path.join(IMAGE_PATH, "{}.png".format(tile.name)))
                    print(os.path.join(IMAGE_PATH, "{}.png".format(tile.name)))
                    xOffset = 2 * (x + 1) + pieceImg.shape[1] * x
                    yOffset = boardImg.shape[0] - (y + 1) * (2 + pieceImg.shape[0])
                    for j in range(pieceImg.shape[0]):
                        for i in range(pieceImg.shape[1]):
                            if pieceImg[j][i].any():
                                color = pieceImg[j][i]
                                if tile.side == Piece.BLACK:
                                    color = 255 - pieceImg[j][i]
                                boardImg[yOffset + j][xOffset + i] = color
        return boardImg

    def Display_Board(self, board):
        cv2.imshow('Board', self.Get_Board_Image(board))
        cv2.waitKey(0)
        cv2.destroyAllWindows()
        
    def Check_Valid_Move(self, player, x1, y1, x2, y2):
        isValid = False
        piece = self.board[y1][x1]
        if isinstance(piece, Piece.Piece) and piece.side == player.side:
            if (x2, y2) in piece.Get_Valid_Moves(self.board):
                isValid = True
            else:
                print("Invalid move: {} to ({}, {})".format(piece.name, x2, y2))
        else:
            print("There is no valid piece at coordinate ({}, {})".format(x1, y1))
        return isValid
    
    def Check_Player_In_Check(self, player, board):
        inCheck = False
        for y in range(len(board)):
            for x in range(len(board[y])):
                piece = board[y][x]
                if isinstance(piece, Piece.Piece) and piece.side != player.side:
                    validMoves = piece.Get_Valid_Moves(board)
                    for coord in validMoves:
                        if isinstance(board[coord[1]][coord[0]], Piece.King):
                            if board[coord[1]][coord[0]].side == player.side:
                                inCheck = True
                                break
        return inCheck
    
    def Will_Result_In_Check(self, player, x1, y1, x2, y2):
        nextBoard = self.Get_Board_Copy(self.board)
        nextBoard[y2][x2] = nextBoard[y1][x1]
        nextBoard[y1][x1] = 0   
        nextBoard[y2][x2].hasMoved = True
        return self.Check_Player_In_Check(player, nextBoard)
    
    def Player_Is_In_Checkmate(self, player):
        for y in range(len(self.board)):
            for x in range(len(self.board[y])):
                piece = self.board[y][x]
                if isinstance(piece, Piece.Piece) and piece.side == player.side:
                    validMoves = piece.Get_Valid_Moves(self.board)
                    for coord in validMoves:
                        x1 = piece.x
                        y1 = piece.y
                        x2 = coord[0]
                        y2 = coord[1]
                        if not self.Will_Result_In_Check(player, x1, y1, x2, y2):
                            print("Moving ({}, {}) to ({}, {}) will not result in check.".format(x1, y1, x2, y2))
                            return False
        return True
            
    
    def Do_Move(self, name, x1, y1, x2, y2):
        msg = "An error has occurred."
        if not name in self.playersDict.keys():
            msg = "{} is not a valid player.".format(name)
            print(msg)
            return msg
            
        player = self.playersDict[name]
        if player.side != self.turn:
            msg = "It is not {}'s turn.".format(player.name)
            print(msg)
            return msg
        
        if self.isGameOver:
            msg = "The game is over."
            print(msg)
            return msg
      
        if self.Check_Valid_Move(player, x1, y1, x2, y2):
            if self.Check_Player_In_Check(player, self.board):
                if self.Will_Result_In_Check(x1, y1, x2, y2):
                    msg = "Cannot do move, King still in check."
                    print(msg)
                    return msg
            player.Do_Move(self.board, x1, y1, x2, y2)
            self.turn = player.side * -1
            otherPlayer = self.player2
            if player == self.player2:
                otherPlayer = self.player1
            if self.Check_Player_In_Check(otherPlayer, self.board):
                msg = "{} is now in check!".format(otherPlayer.name)
                print(msg)
                if self.Player_Is_In_Checkmate(otherPlayer):
                    msg = "Checkmate! {} wins.".format(player.name)
                    print(msg)
                    self.isGameOver = True
                return msg
        else:
            print("Inavlid movement")
            
        return msg

    def Do_Move_Algebraic_Notation(self, playerName, pos1, pos2, display = True):
        x1 = (ord(pos1[0].lower()) - 96) - 1
        y1 = int(pos1[1]) - 1
        x2 = (ord(pos2[0].lower()) - 96) - 1
        y2 = int(pos2[1]) - 1
        return self.Do_Move(playerName, x1, y1, x2, y2)
 
