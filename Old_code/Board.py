from .Empty_figure import Empty
from .Pawn import Pawn
from .Knight import Knight
from .Bishop import Bishop
from .Queen import Queen
from .Rook import Rook
from .King import King
from .Piece import Piece
###Essa é a classe da mesa, que armazena a localização das peças e atualiza seus movimentos
class Board():
    empty_space=Empty()
###Função construtura
    def __init__(self):

        self.initial_board = {(1, 1): 0, (1, 2): 0, (1, 3): 0, (1, 4): 0, (1, 5): 0, (1, 6): 0, (1, 7): 0, (1, 8): 0,
                 (2, 1): 0, (2, 2): 0, (2, 3): 0, (2, 4): 0, (2, 5): 0, (2, 6): 0, (2, 7): 0, (2, 8): 0,
                 (3, 1): 0, (3, 2): 0, (3, 3): 0, (3, 4): 0, (3, 5): 0, (3, 6): 0, (3, 7): 0, (3, 8): 0,
                 (4, 1): 0, (4, 2): 0, (4, 3): 0, (4, 4): 0, (4, 5): 0, (4, 6): 0, (4, 7): 0, (4, 8): 0,
                 (5, 1): 0, (5, 2): 0, (5, 3): 0, (5, 4): 0, (5, 5): 0, (5, 6): 0, (5, 7): 0, (5, 8): 0,
                 (6, 1): 0, (6, 2): 0, (6, 3): 0, (6, 4): 0, (6, 5): 0, (6, 6): 0, (6, 7): 0, (6, 8): 0,
                 (7, 1): 0, (7, 2): 0, (7, 3): 0, (7, 4): 0, (7, 5): 0, (7, 6): 0, (7, 7): 0, (7, 8): 0,
                 (8, 1): 0, (8, 2): 0, (8, 3): 0, (8, 4): 0, (8, 5): 0, (8, 6): 0, (8, 7): 0, (8, 8): 0}
        self.actual_board=self.initial_board
        self.pieces=set()
        self.board_image={}
        self.root=0
### Essa função coloca espaços vazios no lugar dos zeros
    def initialize_board(self):
        for key in self.initial_board.keys():
            self.actual_board[key]=self.empty_space

### A função update_piece atualiza as localizações das peças pegando um dicionário com as novas posições e deletando as antigas posições
    def update_piece(self,piece):

        self.actual_board[piece.old]=self.empty_space
        self.pieces.discard(self.actual_board[piece.position])
        self.actual_board[piece.position]=piece
        self.pieces.add(piece)

    def update_initial_piece(self,piece):
        self.pieces.discard(self.actual_board[piece.position])
        self.actual_board[piece.position]=piece
        self.pieces.add(piece)

###Essa função mostra o estado da mesa
    def print_board(self):
        print("\n1  "
      +
      str(self.actual_board[(1, 1)].letter) +
      "  "+str(self.actual_board[(1, 2)].letter)+
      "  "+str(self.actual_board[(1, 3)].letter)+
      "  "+str(self.actual_board[(1, 4)].letter)+
      "  "+str(self.actual_board[(1, 5)].letter)+
      "  "+str(self.actual_board[(1, 6)].letter)+
      "  "+str(self.actual_board[(1, 7)].letter)+
      "  "+str(self.actual_board[(1, 8)].letter)+

      "   \n2  "
      +
      str(self.actual_board[(2, 1)].letter) +
      "  " + str(self.actual_board[(2, 2)].letter) +
      "  " + str(self.actual_board[(2, 3)].letter) +
      "  " + str(self.actual_board[(2, 4)].letter) +
      "  " + str(self.actual_board[(2, 5)].letter) +
      "  " + str(self.actual_board[(2, 6)].letter) +
      "  " + str(self.actual_board[(2, 7)].letter) +
      "  " + str(self.actual_board[(2, 8)].letter) +

      "\n3  "
      +
      str(self.actual_board[(3, 1)].letter) +
      "  " + str(self.actual_board[(3, 2)].letter) +
      "  " + str(self.actual_board[(3, 3)].letter) +
      "  " + str(self.actual_board[(3, 4)].letter) +
      "  " + str(self.actual_board[(3, 5)].letter) +
      "  " + str(self.actual_board[(3, 6)].letter) +
      "  " + str(self.actual_board[(3, 7)].letter) +
      "  " + str(self.actual_board[(3, 8)].letter) +

      "\n4  "
      +
      str(self.actual_board[(4, 1)].letter) +
      "  " + str(self.actual_board[(4, 2)].letter) +
      "  " + str(self.actual_board[(4, 3)].letter) +
      "  " + str(self.actual_board[(4, 4)].letter) +
      "  " + str(self.actual_board[(4, 5)].letter) +
      "  " + str(self.actual_board[(4, 6)].letter) +
      "  " + str(self.actual_board[(4, 7)].letter) +
      "  " + str(self.actual_board[(4, 8)].letter) +

      "\n5  "
      +
      str(self.actual_board[(5, 1)].letter) +
      "  " + str(self.actual_board[(5, 2)].letter) +
      "  " + str(self.actual_board[(5, 3)].letter) +
      "  " + str(self.actual_board[(5, 4)].letter) +
      "  " + str(self.actual_board[(5, 5)].letter) +
      "  " + str(self.actual_board[(5, 6)].letter) +
      "  " + str(self.actual_board[(5, 7)].letter) +
      "  " + str(self.actual_board[(5, 8)].letter) +

      "\n6  "
      +
      str(self.actual_board[(6, 1)].letter) +
      "  " + str(self.actual_board[(6, 2)].letter) +
      "  " + str(self.actual_board[(6, 3)].letter) +
      "  " + str(self.actual_board[(6, 4)].letter) +
      "  " + str(self.actual_board[(6, 5)].letter) +
      "  " + str(self.actual_board[(6, 6)].letter) +
      "  " + str(self.actual_board[(6, 7)].letter) +
      "  " + str(self.actual_board[(6, 8)].letter) +

      "\n7  "
      +
      str(self.actual_board[(7, 1)].letter) +
      "  " + str(self.actual_board[(7, 2)].letter) +
      "  " + str(self.actual_board[(7, 3)].letter) +
      "  " + str(self.actual_board[(7, 4)].letter) +
      "  " + str(self.actual_board[(7, 5)].letter) +
      "  " + str(self.actual_board[(7, 6)].letter) +
      "  " + str(self.actual_board[(7, 7)].letter) +
      "  " + str(self.actual_board[(7, 8)].letter) +

      "\n8  "
      +
      str(self.actual_board[(8, 1)].letter) +
      "  " + str(self.actual_board[(8, 2)].letter) +
      "  " + str(self.actual_board[(8, 3)].letter) +
      "  " + str(self.actual_board[(8, 4)].letter) +
      "  " + str(self.actual_board[(8, 5)].letter) +
      "  " + str(self.actual_board[(8, 6)].letter) +
      "  " + str(self.actual_board[(8, 7)].letter) +
      "  " + str(self.actual_board[(8, 8)].letter) +

      "\n   A  B  C  D  E  F  G  H")

    def check_tile(self, tile, color):
        opposing_pieces=[]
        can_reach=False
        possible=list()
        if color==0:
            for x in self.pieces:
                if x.color==1:
                    opposing_pieces.append(x)

            for x in opposing_pieces:
                    if isinstance(x,King):
                     possible+=x.find_moves(action=False)

                    else: possible += x.find_moves()

            if tile in possible:
                can_reach=True

        elif color==1:
            for x in self.pieces:
                if x.color==0:
                    opposing_pieces.append(x)

            for x in opposing_pieces:

                if isinstance(x, King):
                    possible += x.find_moves(action=False)

                else:
                    possible += x.find_moves()

            if tile in possible:
                can_reach = True
        return can_reach

    def put_pieces(self):
        self.update_initial_piece(Pawn(1,(7,"A"),"White",self))
        self.update_initial_piece(Pawn(2, (7, "B"), "White", self))
        self.update_initial_piece(Pawn(3, (7, "C"), "White", self))
        self.update_initial_piece(Pawn(4, (7, "D"), "White", self))
        self.update_initial_piece(Pawn(5, (7, "E"), "White", self))
        self.update_initial_piece(Pawn(6, (7, "F"), "White", self))
        self.update_initial_piece(Pawn(7, (7, "G"), "White", self))
        self.update_initial_piece(Pawn(8, (7, "H"), "White", self))
        self.update_initial_piece(Rook(1, (8, "A"), "White", self))
        self.update_initial_piece(Rook(2, (8, "H"), "White", self))
        self.update_initial_piece(Bishop(1, (8, "C"), "White", self))
        self.update_initial_piece(Bishop(2, (8, "F"), "White", self))
        self.update_initial_piece(Knight(1, (8, "B"), "White", self))
        self.update_initial_piece(Knight(2, (8, "G"), "White", self))
        self.update_initial_piece(Queen(1, (8, "D"), "White", self))
        self.update_initial_piece(King(1, (8, "E"), "White", self))

        self.update_initial_piece(Pawn(1, (2, "A"), "Black", self))
        self.update_initial_piece(Pawn(2, (2, "B"), "Black", self))
        self.update_initial_piece(Pawn(3, (2, "C"), "Black", self))
        self.update_initial_piece(Pawn(4, (2, "D"), "Black", self))
        self.update_initial_piece(Pawn(5, (2, "E"), "Black", self))
        self.update_initial_piece(Pawn(6, (2, "F"), "Black", self))
        self.update_initial_piece(Pawn(7, (2, "G"), "Black", self))
        self.update_initial_piece(Pawn(8, (2, "H"), "Black", self))
        self.update_initial_piece(Rook(1, (1, "A"), "Black", self))
        self.update_initial_piece(Rook(2, (1, "H"), "Black", self))
        self.update_initial_piece(Bishop(1, (1, "C"), "Black", self))
        self.update_initial_piece(Bishop(2, (1, "F"), "Black", self))
        self.update_initial_piece(Knight(1, (1, "B"), "Black", self))
        self.update_initial_piece(Knight(2, (1, "G"), "Black", self))
        self.update_initial_piece(Queen(1, (1, "D"), "Black", self))
        self.update_initial_piece(King(1, (1, "E"), "Black", self))




#