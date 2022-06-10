from .Piece import Piece
from .Rook import Rook
from .Empty_figure import Empty

class King(Piece):
    def __init__(self,number,position,color,board):
        super().__init__(number,position,color,board)
        self.letter="Z" if color=="White" else "z"
        self.castle=False

    def find_moves(self, action=True):
        movimentos=[]
        posicao_possivel=[]
        castle=list()
        if self.color==1:
            print("meme")
            posicao_possivel.append((self.position[0] + 1,self.position[1]))
            posicao_possivel.append((self.position[0] + 1, self.position[1] - 1))
            posicao_possivel.append((self.position[0], self.position[1] - 1))
            posicao_possivel.append((self.position[0] - 1, self.position[1] - 1))
            posicao_possivel.append((self.position[0] - 1, self.position[1]))
            posicao_possivel.append((self.position[0] - 1, self.position[1] + 1))
            posicao_possivel.append((self.position[0], self.position[1] + 1))
            posicao_possivel.append((self.position[0] + 1, self.position[1] + 1))

            for x in posicao_possivel:
                if x in self.board.initial_board and self.board.actual_board[x].color!=1:
                    movimentos.append(x)

            #Castle
            if self.old==None and action:
                print("mastermeme")
                castle_left=list()
                castle_right=list()

                can_castle_right=False
                can_castle_left=False

                castle_right.append((self.position[0] ,self.position[1] + 1))
                castle_right.append((self.position[0], self.position[1] + 2))
                castle_right.append((self.position[0], self.position[1] + 3))

                castle_left.append((self.position[0], self.position[1] - 1))
                castle_left.append((self.position[0], self.position[1] - 2))
                castle_left.append((self.position[0], self.position[1] - 3))
                castle_left.append((self.position[0], self.position[1] - 4))


                if not self.board.check_tile(castle_right[0], 1) and not self.board.check_tile(castle_right[1], 1) and  isinstance(self.board.actual_board[castle_right[2]], Rook)\
                        and self.board.actual_board[(1,6)]==self.board.empty_space and self.board.actual_board[(1,7)]==self.board.empty_space\
                        and self.board.actual_board[(1,8)].old==None:
                    can_castle_right=True
                    castle.append(castle_right[1])

                if not self.board.check_tile(castle_left[0], 1) and not self.board.check_tile(castle_left[1], 1) and not self.board.check_tile(castle_right[2], 1)  and isinstance(self.board.actual_board[castle_left[3]], Rook)\
                        and self.board.actual_board[(1,4)]==self.board.empty_space and self.board.actual_board[(1,3)]==self.board.empty_space\
                        and self.board.actual_board[(1,2)]==self.board.empty_space and self.board.actual_board[(1,1)].old==None:
                    can_castle_left=True
                    castle.append(castle_left[1])


        elif self.color == 0:
            posicao_possivel.append((self.position[0] + 1, self.position[1]))
            posicao_possivel.append((self.position[0] + 1, self.position[1] - 1))
            posicao_possivel.append((self.position[0], self.position[1] - 1))
            posicao_possivel.append((self.position[0] - 1, self.position[1] - 1))
            posicao_possivel.append((self.position[0] - 1, self.position[1]))
            posicao_possivel.append((self.position[0] - 1, self.position[1] + 1))
            posicao_possivel.append((self.position[0], self.position[1] + 1))
            posicao_possivel.append((self.position[0] + 1, self.position[1] + 1))

            for x in posicao_possivel:
                if x in self.board.initial_board and self.board.actual_board[x].color != 0:
                    movimentos.append(x)

            #Castle
            if self.old==None and action:
                castle_left=list()
                castle_right=list()

                can_castle_right=False
                can_castle_left=False

                castle_right.append(tuple([self.position[0] ,self.position[1] + 1]))
                castle_right.append(tuple([self.position[0], self.position[1] + 2]))
                castle_right.append(tuple([self.position[0], self.position[1] + 3]))

                castle_left.append(tuple([self.position[0], self.position[1] - 1]))
                castle_left.append(tuple([self.position[0], self.position[1] - 2]))
                castle_left.append(tuple([self.position[0], self.position[1] - 3]))
                castle_left.append(tuple([self.position[0], self.position[1] - 4]))
                print("this is castle right")
                print(castle_right)

                if not self.board.check_tile(castle_right[0], 0) and not self.board.check_tile(castle_right[1], 0) and isinstance(self.board.actual_board[castle_right[2]], Rook)\
                        and self.board.actual_board[(8,6)]==self.board.empty_space and self.board.actual_board[(8,7)]==self.board.empty_space\
                        and self.board.actual_board[(8,8)].old==None:
                    can_castle_right=True
                    castle.append(castle_right[1])

                if not self.board.check_tile(castle_left[0], 0) and not self.board.check_tile(castle_left[1], 0) and not self.board.check_tile(castle_right[2], 0)  and isinstance(self.board.actual_board[castle_left[3]], Rook)\
                        and self.board.actual_board[(8,4)]==self.board.empty_space and self.board.actual_board[(8,3)]==self.board.empty_space\
                        and self.board.actual_board[(8,2)]==self.board.empty_space and self.board.actual_board[(8,1)].old==None:
                    can_castle_left=True
                    castle.append(castle_left[1])
        if castle:
            return movimentos,castle
        else: return movimentos

    def move(self, posicao):
        posicao_numerica = (posicao[0], self.letter_values[posicao[1]])

        if posicao_numerica in self.find_moves():
            self.old = self.position
            self.position = posicao_numerica