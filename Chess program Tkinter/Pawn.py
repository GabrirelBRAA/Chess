from Piece import Piece
###Classe peão, que move apenas uma casa
class Pawn(Piece):
    def __init__(self,number,position,color,board):
        super().__init__(number,position,color,board)
        self.letter="P" if color=="White" else "p"
###Essa função faz o peão mover uma casa
    def move_normal(self):
        if  self.color==0 and (self.position[0]-1,self.position[1]) not in self.board.actual_board or self.color==0 and self.board.actual_board[(self.position[0]-1,self.position[1])] != self.board.empty_space:
           print("Cannot move Pawn")
        elif  self.color==1 and (self.position[0]+1,self.position[1]) not in self.board.actual_board or self.color==1 and self.board.actual_board[(self.position[0]+1,self.position[1])] != self.board.empty_space:
           print("Cannot move Pawn")
        else:
            self.old = self.position
            self.position = (self.position[0] - 1, self.position[1]) if self.color!=1 else (self.position[0]+1,self.position[1])

    def move_two(self):
        if self.old!=None:
            print("Esse peão já se movimentou")

        elif self.color == 0 and (
        self.position[0] - 2, self.position[1]) not in self.board.actual_board or self.color == 0 and \
                self.board.actual_board[(self.position[0] - 2, self.position[1])] != self.board.empty_space:

            print("Cannot move Pawn")

        elif self.color == 1 and (
        self.position[0] + 2, self.position[1]) not in self.board.actual_board or self.color == 1 and \
                self.board.actual_board[(self.position[0] + 2, self.position[1])] != self.board.empty_space:

            print("Cannot move Pawn")

        else:

            self.old = self.position

            self.position = (self.position[0] - 2, self.position[1]) if self.color != 1 else (
            self.position[0] + 2, self.position[1])

    #Essa função faz o peão achar possíveis movimentos de captura
    def find_moves(self):
        posicao_possivel=[]
        movimentos=[]
        if self.color==0:
            posicao_possivel.append((self.position[0]+1,self.position[1]-1))
            posicao_possivel.append((self.position[0]+1, self.position[1]+1))

            for x in posicao_possivel:
                if x in self.board.initial_board and self.board.actual_board[x].color!=0:
                   movimentos.append(x)

        elif self.color == 1:
            posicao_possivel.append((self.position[0] + 1, self.position[1]-1))
            posicao_possivel.append((self.position[0] + 1, self.position[1]+1))

            for x in posicao_possivel:
                if x in self.board.initial_board and self.board.actual_board[x].color != 1:
                   movimentos.append(x)

        return movimentos



    def move(self, posicao):
        posicao_numerica = (posicao[0], self.letter_values[posicao[1]])

        if posicao_numerica in self.find_moves():
            self.old = self.position
            self.position = posicao_numerica






