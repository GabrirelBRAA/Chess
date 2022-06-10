from .Piece import Piece
###Classe peão, que move apenas uma casa
class Pawn(Piece):
    def __init__(self,number,position,color,board):
        super().__init__(number,position,color,board)
        self.letter="P" if color=="White" else "p"
###Essa função faz o peão mover uma casa
    def move_normal(self):
        """Função inutilizada"""

        if  self.color==0 and (self.position[0]-1,self.position[1]) not in self.board.actual_board or self.color==0 and self.board.actual_board[(self.position[0]-1,self.position[1])] != self.board.empty_space:
           print("Cannot move Pawn")
        elif  self.color==1 and (self.position[0]+1,self.position[1]) not in self.board.actual_board or self.color==1 and self.board.actual_board[(self.position[0]+1,self.position[1])] != self.board.empty_space:
           print("Cannot move Pawn")
        else:
            self.old = self.position
            self.position = (self.position[0] - 1, self.position[1]) if self.color!=1 else (self.position[0]+1,self.position[1])

    def move_two(self):
        """Função initilizada"""

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

    def en_passant(self):
        left=(self.position[0],self.position[1]-1) if self.position[1]-1!=0 else False
        right=(self.position[0],self.position[1]+1) if self.position[1]+1 < 9 else False
        lista=[0,0] #esquerdo para esquerda e direito para direita
        if self.color == 0:
            if left in self.board.actual_board.keys():
                print(left)
                print(self.board.actual_board[left])
            if left and left in self.board.actual_board and isinstance(self.board.actual_board[left], Pawn) and self.board.actual_board[left].color==1 and self.board.actual_board[left].old and self.board.actual_board[left].old[0]==2:
                lista[0]=(left[0]-1,left[1])

            if right and right in self.board.actual_board and isinstance(self.board.actual_board[right], Pawn) and self.board.actual_board[right].color==1 and self.board.actual_board[right].old and self.board.actual_board[right].old[0]==2:
                lista[1]=(right[0]-1,right[1])
        elif self.color == 1:
            if left and left in self.board.actual_board and isinstance(self.board.actual_board[left], Pawn) and self.board.actual_board[left].color==0 and self.board.actual_board[left].old and self.board.actual_board[left].old[0] == 7:
                lista[0] = (left[0] + 1, left[1])

            if right and right in self.board.actual_board and isinstance(self.board.actual_board[right], Pawn) and self.board.actual_board[right].color==0 and self.board.actual_board[right].old and self.board.actual_board[right].old[0] == 7:
                lista[1] = (right[0] + 1, right[1])

        return lista


    def find_moves(self):
        posicao_possivel=[]
        movimentos=[]
        trash=[]
        if self.color==0:
            posicao_possivel.append((self.position[0] - 1,self.position[1]-1))
            posicao_possivel.append((self.position[0] - 1, self.position[1]+1))
            for x in posicao_possivel:
                if x in self.board.actual_board and self.board.actual_board[x].color==1:
                    movimentos.append(x)
            posicao_possivel=[]

            posicao_possivel.append((self.position[0] - 1, self.position[1]))

            if self.old == None:
                double_jump_initial = (self.position[0] - 2, self.position[1])
                if self.board.actual_board[(self.position[0] - 1, self.position[1])].color == None and self.board.actual_board[double_jump_initial].color==None:
                    movimentos.append(double_jump_initial)

            for x in posicao_possivel:
                if x in self.board.initial_board and self.board.actual_board[x].color == None:
                   movimentos.append(x)

        elif self.color == 1:
            posicao_possivel.append((self.position[0] + 1, self.position[1]-1))
            posicao_possivel.append((self.position[0] + 1, self.position[1]+1))

            for x in posicao_possivel:
                if x in self.board.actual_board and self.board.actual_board[x].color==0:
                    movimentos.append(x)

            posicao_possivel=[]


            posicao_possivel.append((self.position[0] + 1, self.position[1]))

            if self.old == None:
                double_jump_initial=(self.position[0] + 2, self.position[1])
                if self.board.actual_board[(self.position[0] + 1, self.position[1])].color == None and self.board.actual_board[double_jump_initial].color==None:
                    movimentos.append(double_jump_initial)

            for x in posicao_possivel:
                if x in self.board.initial_board and self.board.actual_board[x].color == None:
                   movimentos.append(x)

        enpassant=self.en_passant()
        print("essa é a lista")
        print(enpassant)
        flag=False
        if enpassant!=[0,0]:
            flag=True
        if flag:
            return movimentos, enpassant
        else: return movimentos



    def move(self, posicao):
        posicao_numerica = (posicao[0], self.letter_values[posicao[1]])

        if posicao_numerica in self.find_moves():
            self.old = self.position
            self.position = posicao_numerica






