###Essa classe existe dentro de board como um preenchimento para o espaço vazio (Veja a função initialize_board da classe Board()
###Seus atributos servem como lógica para funções de mover peças ou achar possíveis movimentos
class Empty():
    def __init__(self):
        self.letter=0
        self.color=None
