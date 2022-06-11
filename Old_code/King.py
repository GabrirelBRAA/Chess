from .Piece import Piece
from .Rook import Rook

class King(Piece):
    def __init__(self,number,position,color,board):
        super().__init__(number,position,color,board)
        self.letter="Z" if color=="White" else "z"
        self.castle=False

    def find_moves(self, action=True):
        """Acha os movimentos do Rei
           O parâmetro action diz que uma ação de um jogador está ocorrendo,
           caso contrário é uma tentativa da lógica interna de achar movimentos para validar check ou o castle e a própria função castle é ignorada"""

        movimentos=list()         #Movimentos que foram validados
        posicao_possivel=list()   #Movimentos que não foram validados
        castle=list()             #Movimentos de castelo

        def movimentos_normais(color):
            """Essa função acha e valida os movimentos normais do rei (Ela não checa se o rei está em check, isso é papel da Board)"""
            ###Possivelmente precisará de alteração para invalidar movimentos para casas em check

            posicao_possivel.append((self.position[0] + 1, self.position[1]    ))
            posicao_possivel.append((self.position[0] + 1, self.position[1] - 1))
            posicao_possivel.append((self.position[0] + 1, self.position[1] + 1))
            posicao_possivel.append((self.position[0],     self.position[1] - 1))
            posicao_possivel.append((self.position[0],     self.position[1] + 1))
            posicao_possivel.append((self.position[0] - 1, self.position[1] - 1))
            posicao_possivel.append((self.position[0] - 1, self.position[1]    ))
            posicao_possivel.append((self.position[0] - 1, self.position[1] + 1))

            for x in posicao_possivel:
                if x in self.board.initial_board and self.board.actual_board[x].color!=color:
                    movimentos.append(x)

        def check_castle(color):
            """Checa se é posssível fazer o castle."""

            castle_right = [(self.position[0], self.position[1]+n) for n in range(1,4)] ### Castle para esquerda, sendo o último item a posição da torre
            castle_left = [(self.position[0], self.position[1]-n) for n in range(1,5)] ### Mesma coisa para direita

            rook_right = self.board.actual_board[castle_right.pop()]
            rook_left = self.board.actual_board[castle_left.pop()]

            if (self.board.actual_board[castle_right[0]] and self.board.actual_board[castle_right[1]]) == self.board.empty_space \
                and not (self.board.check_tile(castle_right[0], color) or self.board.check_tile(castle_right[1], color) or self.board.check_tile(self.position, color)) \
                and rook_right.old==None:

                    castle.append(castle_right[1])

            if (self.board.actual_board[castle_left[0]] and self.board.actual_board[castle_left[1]] and \
                self.board.actual_board[castle_left[2]]) == self.board.empty_space \
                    and not (self.board.check_tile(castle_left[0], color) or \
                             self.board.check_tile(castle_left[1], color) or self.board.check_tile(self.position, color)) \
                        and rook_left.old == None:

                    castle.append(castle_left[1])


        if self.color==1:

            movimentos_normais(1)
            if self.old == None and action:
                check_castle(1)

        elif self.color == 0:

            movimentos_normais(0)
            if self.old == None and action:
                check_castle(0)

        if castle:
            return movimentos,castle
        else: return movimentos

    def move(self, posicao):
        posicao_numerica = (posicao[0], self.letter_values[posicao[1]])

        if posicao_numerica in self.find_moves():
            self.old = self.position
            self.position = posicao_numerica