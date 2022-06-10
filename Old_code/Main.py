from Pawn import Pawn
from Knight import Knight
from Bishop import Bishop
from Queen import Queen
from Rook import Rook
from King import King
from Board import Board
letter_values={"A":1,"B":2,"C":3,"D":4,"E":5,"F":6,"G":7,"H":8}

print("Bem vindo ao xadrez do Galdino")
x=Board()
x.initialize_board()
x.put_pieces()
x.print_board()
x.setup_tkinter_board()
x.import_piece_images()
x.create_labels()
x.show_initial_labels()
x.root.update()
while True:
    numero_de_escolha=int(input("\nEscolha a peça pela posição Ex: 6,H\nDigite um caractere de cada vez\nSelecione o número : "))
    letra_de_escolha=input("\nSelecione uma letra : ")
    escolha=(numero_de_escolha,letter_values[letra_de_escolha])
    print(x.actual_board[escolha])
    escolha=x.actual_board[escolha]
    if isinstance(escolha,Pawn):
        logica=int(input("1 para mover adiante , 2 para capturar peça e 3 para mover duas casas:"))
        if logica==1:
            escolha.move_normal()

        elif logica==2:
            numero_de_movimento = int(input("\nEscolha a posição para mover Ex: 6,H\nDigite um caractere de cada vez\nSelecione o número : "))
            letra_de_movimento = input("\nSelecione uma letra : ")
            escolha.move((numero_de_movimento, letra_de_movimento))

        elif logica==3:
            escolha.move_two()
    else:
        numero_de_movimento = int(input("\nEscolha a posição para mover Ex: 6,H\nDigite um caractere de cada vez\nSelecione o número : "))
        letra_de_movimento = input("\nSelecione uma letra : ")
        escolha.move((numero_de_movimento,letra_de_movimento))
    x.update_piece(escolha)
    x.update_label(escolha)
    x.print_board()
    x.root.update()