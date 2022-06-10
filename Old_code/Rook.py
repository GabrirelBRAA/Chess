from .Piece import Piece

class Rook(Piece):
    def __init__(self,number,position,color,board):
        super().__init__(number,position,color,board)
        self.letter="R" if color=="White" else "r"

    def find_moves(self):
        movimentos=[]
        if self.color==0:
            movimento_possivel=self.position
            for x in range(0,8):
                movimento_possivel=(movimento_possivel[0],movimento_possivel[1]+1)
                if movimento_possivel in self.board.initial_board.keys() and self.board.actual_board[movimento_possivel].color==None:
                    movimentos.append(movimento_possivel)
                elif movimento_possivel in self.board.initial_board.keys() and self.board.actual_board[movimento_possivel].color==1:
                    movimentos.append(movimento_possivel)
                    break
                elif movimento_possivel in self.board.initial_board.keys() and self.board.actual_board[movimento_possivel].color==0:
                    break

            movimento_possivel = self.position
            for x in range(0, 8):
                movimento_possivel = (movimento_possivel[0], movimento_possivel[1] - 1)
                if movimento_possivel in self.board.initial_board.keys() and self.board.actual_board[movimento_possivel].color==None:
                    movimentos.append(movimento_possivel)
                elif movimento_possivel in self.board.initial_board.keys() and self.board.actual_board[movimento_possivel].color==1:
                    movimentos.append(movimento_possivel)
                    break
                elif movimento_possivel in self.board.initial_board.keys() and self.board.actual_board[movimento_possivel].color==0:
                    break

            movimento_possivel = self.position
            for x in range(0, 8):
                movimento_possivel = (movimento_possivel[0]+1, movimento_possivel[1])
                if movimento_possivel in self.board.initial_board.keys() and self.board.actual_board[movimento_possivel].color==None:
                    movimentos.append(movimento_possivel)
                elif movimento_possivel in self.board.initial_board.keys() and self.board.actual_board[movimento_possivel].color==1:
                    movimentos.append(movimento_possivel)
                    break
                elif movimento_possivel in self.board.initial_board.keys() and self.board.actual_board[movimento_possivel].color==0:
                    break

            movimento_possivel = self.position
            for x in range(0, 8):
                movimento_possivel = (movimento_possivel[0]-1, movimento_possivel[1])
                if movimento_possivel in self.board.initial_board.keys() and self.board.actual_board[movimento_possivel].color==None:
                    movimentos.append(movimento_possivel)
                elif movimento_possivel in self.board.initial_board.keys() and self.board.actual_board[movimento_possivel].color==1:
                    movimentos.append(movimento_possivel)
                    break
                elif movimento_possivel in self.board.initial_board.keys() and self.board.actual_board[movimento_possivel].color==0:
                    break

        elif self.color==1:
            movimento_possivel=self.position
            for x in range(0,8):
                movimento_possivel=(movimento_possivel[0],movimento_possivel[1]+1)
                if movimento_possivel in self.board.initial_board.keys() and self.board.actual_board[movimento_possivel].color==None:
                    movimentos.append(movimento_possivel)
                elif movimento_possivel in self.board.initial_board.keys() and self.board.actual_board[movimento_possivel].color==0:
                    movimentos.append(movimento_possivel)
                    break
                elif movimento_possivel in self.board.initial_board.keys() and self.board.actual_board[movimento_possivel].color==1:
                    break

            movimento_possivel = self.position
            for x in range(0, 8):
                movimento_possivel = (movimento_possivel[0], movimento_possivel[1] - 1)
                if movimento_possivel in self.board.initial_board.keys() and self.board.actual_board[movimento_possivel].color==None:
                    movimentos.append(movimento_possivel)
                elif movimento_possivel in self.board.initial_board.keys() and self.board.actual_board[movimento_possivel].color==0:
                    movimentos.append(movimento_possivel)
                    break
                elif movimento_possivel in self.board.initial_board.keys() and self.board.actual_board[movimento_possivel].color==1:
                    break

            movimento_possivel = self.position
            for x in range(0, 8):
                movimento_possivel = (movimento_possivel[0]+1, movimento_possivel[1])
                if movimento_possivel in self.board.initial_board.keys() and self.board.actual_board[movimento_possivel].color==None:
                    movimentos.append(movimento_possivel)
                elif movimento_possivel in self.board.initial_board.keys() and self.board.actual_board[movimento_possivel].color==0:
                    movimentos.append(movimento_possivel)
                    break
                elif movimento_possivel in self.board.initial_board.keys() and self.board.actual_board[movimento_possivel].color==1:
                    break

            movimento_possivel = self.position
            for x in range(0, 8):
                movimento_possivel = (movimento_possivel[0]-1, movimento_possivel[1])
                if movimento_possivel in self.board.initial_board.keys() and self.board.actual_board[movimento_possivel].color==None:
                    movimentos.append(movimento_possivel)
                elif movimento_possivel in self.board.initial_board.keys() and self.board.actual_board[movimento_possivel].color==0:
                    movimentos.append(movimento_possivel)
                    break
                elif movimento_possivel in self.board.initial_board.keys() and self.board.actual_board[movimento_possivel].color==1:
                    break

        return movimentos

    def move(self, posicao):
        posicao_numerica = (posicao[0], self.letter_values[posicao[1]])

        if posicao_numerica in self.find_moves():
            self.old = self.position
            self.position = posicao_numerica
