from Piece import Piece

class Knight(Piece):
    def __init__(self,number,position,color,board):
        super().__init__(number,position,color,board)
        self.letter="K" if color=="White" else "k"

    def find_moves(self):
        movimentos=[]
        if self.color==0:
           try:
               movimentos.append((self.position[0]-2,self.position[1]-1))
           except:pass
           try:
               movimentos.append((self.position[0]-1,self.position[1]-2))
           except:pass
           try:
               movimentos.append((self.position[0]+1,self.position[1]-2))
           except:pass
           try:
               movimentos.append((self.position[0]+2,self.position[1]-1))
           except:pass
           try:
               movimentos.append((self.position[0]+2,self.position[1]+1))
           except:pass
           try:
               movimentos.append((self.position[0]+1,self.position[1]+2))
           except:pass
           try:
               movimentos.append((self.position[0]-1,self.position[1]+2))
           except:pass
           try:
               movimentos.append((self.position[0]-2,self.position[1]+1))
           except:pass
           valido_na_mesa=[]
           for x in movimentos:
               if x in self.board.initial_board.keys():
                   valido_na_mesa.append(x)
           valido=[]
           for x in valido_na_mesa:
               if self.board.actual_board[x].color!=0:
                   valido.append(x)
           return valido

        elif self.color==1:
           try:
               movimentos.append((self.position[0]-2,self.position[1]-1))
           except:pass
           try:
               movimentos.append((self.position[0]-1,self.position[1]-2))
           except:pass
           try:
               movimentos.append((self.position[0]+1,self.position[1]-2))
           except:pass
           try:
               movimentos.append((self.position[0]+2,self.position[1]-1))
           except:pass
           try:
               movimentos.append((self.position[0]+2,self.position[1]+1))
           except:pass
           try:
               movimentos.append((self.position[0]+1,self.position[1]+2))
           except:pass
           try:
               movimentos.append((self.position[0]-1,self.position[1]+2))
           except:pass
           try:
               movimentos.append((self.position[0]-2,self.position[1]+1))
           except:pass
           valido_na_mesa=[]
           for x in movimentos:
               if x in self.board.initial_board.keys():
                   valido_na_mesa.append(x)
           valido=[]
           for x in valido_na_mesa:
               if self.board.actual_board[x].color!=1:
                   valido.append(x)
           return valido

    def move(self,posicao):
        posicao_numerica=(posicao[0],self.letter_values[posicao[1]])

        if posicao_numerica in self.find_moves():
            self.old=self.position
            self.position=posicao_numerica

