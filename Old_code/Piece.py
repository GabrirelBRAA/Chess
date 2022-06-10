###Essa é a classe mãe para todas as peças
class Piece():
    letter_values={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8}
    number_values = {1:"A",2:"B",3:"C",4:"D",5:"E",6:"F",7:"G",8:"H"}
    def __init__(self, number,position,color,board):
        self.number=number
        self.position=(position[0],self.letter_values[position[1]])
        self.old=None
        self.color=0 if color=="White" else 1
        self.board=board
        self.label_preto = 0
        self.label_branco = 0
###Função de teste
    def test_number(self):
        print(self.number,self.position)
###Função que dá um dicionário com a posição atual
    def give_location(self):
        return {self.position:self.letter}
###Função que dá um dicionário com a posição antiga
    def give_old(self):
        return {self.old:self.letter}







