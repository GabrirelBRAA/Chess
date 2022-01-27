from Piece import Piece

class King(Piece):
    def __init__(self,number,position,color,board):
        super().__init__(number,position,color,board)
        self.letter="Z" if color=="White" else "z"

    def find_moves(self):
        movimentos=[]
        posicao_possivel=[]
        if self.color==1:
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

        return movimentos

    def move(self, posicao):
        posicao_numerica = (posicao[0], self.letter_values[posicao[1]])

        if posicao_numerica in self.find_moves():
            self.old = self.position
            self.position = posicao_numerica