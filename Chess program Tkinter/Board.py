from Empty_figure import Empty
from Pawn import Pawn
from Knight import Knight
from Bishop import Bishop
from Queen import Queen
from Rook import Rook
from King import King
from tkinter import *
from tkinter import ttk
###Essa é a classe da mesa, que armazena a localização das peças e atualiza seus movimentos
class Board():
    empty_space=Empty()
###Função construtura
    def __init__(self):

        self.initial_board = {(1, 1): 0, (1, 2): 0, (1, 3): 0, (1, 4): 0, (1, 5): 0, (1, 6): 0, (1, 7): 0, (1, 8): 0,
                 (2, 1): 0, (2, 2): 0, (2, 3): 0, (2, 4): 0, (2, 5): 0, (2, 6): 0, (2, 7): 0, (2, 8): 0,
                 (3, 1): 0, (3, 2): 0, (3, 3): 0, (3, 4): 0, (3, 5): 0, (3, 6): 0, (3, 7): 0, (3, 8): 0,
                 (4, 1): 0, (4, 2): 0, (4, 3): 0, (4, 4): 0, (4, 5): 0, (4, 6): 0, (4, 7): 0, (4, 8): 0,
                 (5, 1): 0, (5, 2): 0, (5, 3): 0, (5, 4): 0, (5, 5): 0, (5, 6): 0, (5, 7): 0, (5, 8): 0,
                 (6, 1): 0, (6, 2): 0, (6, 3): 0, (6, 4): 0, (6, 5): 0, (6, 6): 0, (6, 7): 0, (6, 8): 0,
                 (7, 1): 0, (7, 2): 0, (7, 3): 0, (7, 4): 0, (7, 5): 0, (7, 6): 0, (7, 7): 0, (7, 8): 0,
                 (8, 1): 0, (8, 2): 0, (8, 3): 0, (8, 4): 0, (8, 5): 0, (8, 6): 0, (8, 7): 0, (8, 8): 0}
        self.actual_board=self.initial_board
        self.pieces=set()
        self.board_image={}
        self.root=0
### Essa função coloca espaços vazios no lugar dos zeros
    def initialize_board(self):
        for key in self.initial_board:
            self.actual_board[key]=self.empty_space

### A função update_piece atualiza as localizações das peças pegando um dicionário com as novas posições e deletando as antigas posições
    def update_piece(self,piece):
        for key in piece.give_old():
            self.actual_board[key]=self.empty_space
        for key in piece.give_location():
            try: self.actual_board[key].label_preto.grid_forget()
            except:pass
            try: self.actual_board[key].label_branco.grid_forget()
            except:pass
            self.pieces.discard(self.actual_board[key])
            self.actual_board[key]=piece
            self.pieces.add(piece)

###Essa função mostra o estado da mesa
    def print_board(self):
        print("\n1  "
      +
      str(self.actual_board[(1, 1)].letter) +
      "  "+str(self.actual_board[(1, 2)].letter)+
      "  "+str(self.actual_board[(1, 3)].letter)+
      "  "+str(self.actual_board[(1, 4)].letter)+
      "  "+str(self.actual_board[(1, 5)].letter)+
      "  "+str(self.actual_board[(1, 6)].letter)+
      "  "+str(self.actual_board[(1, 7)].letter)+
      "  "+str(self.actual_board[(1, 8)].letter)+

      "   \n2  "
      +
      str(self.actual_board[(2, 1)].letter) +
      "  " + str(self.actual_board[(2, 2)].letter) +
      "  " + str(self.actual_board[(2, 3)].letter) +
      "  " + str(self.actual_board[(2, 4)].letter) +
      "  " + str(self.actual_board[(2, 5)].letter) +
      "  " + str(self.actual_board[(2, 6)].letter) +
      "  " + str(self.actual_board[(2, 7)].letter) +
      "  " + str(self.actual_board[(2, 8)].letter) +

      "\n3  "
      +
      str(self.actual_board[(3, 1)].letter) +
      "  " + str(self.actual_board[(3, 2)].letter) +
      "  " + str(self.actual_board[(3, 3)].letter) +
      "  " + str(self.actual_board[(3, 4)].letter) +
      "  " + str(self.actual_board[(3, 5)].letter) +
      "  " + str(self.actual_board[(3, 6)].letter) +
      "  " + str(self.actual_board[(3, 7)].letter) +
      "  " + str(self.actual_board[(3, 8)].letter) +

      "\n4  "
      +
      str(self.actual_board[(4, 1)].letter) +
      "  " + str(self.actual_board[(4, 2)].letter) +
      "  " + str(self.actual_board[(4, 3)].letter) +
      "  " + str(self.actual_board[(4, 4)].letter) +
      "  " + str(self.actual_board[(4, 5)].letter) +
      "  " + str(self.actual_board[(4, 6)].letter) +
      "  " + str(self.actual_board[(4, 7)].letter) +
      "  " + str(self.actual_board[(4, 8)].letter) +

      "\n5  "
      +
      str(self.actual_board[(5, 1)].letter) +
      "  " + str(self.actual_board[(5, 2)].letter) +
      "  " + str(self.actual_board[(5, 3)].letter) +
      "  " + str(self.actual_board[(5, 4)].letter) +
      "  " + str(self.actual_board[(5, 5)].letter) +
      "  " + str(self.actual_board[(5, 6)].letter) +
      "  " + str(self.actual_board[(5, 7)].letter) +
      "  " + str(self.actual_board[(5, 8)].letter) +

      "\n6  "
      +
      str(self.actual_board[(6, 1)].letter) +
      "  " + str(self.actual_board[(6, 2)].letter) +
      "  " + str(self.actual_board[(6, 3)].letter) +
      "  " + str(self.actual_board[(6, 4)].letter) +
      "  " + str(self.actual_board[(6, 5)].letter) +
      "  " + str(self.actual_board[(6, 6)].letter) +
      "  " + str(self.actual_board[(6, 7)].letter) +
      "  " + str(self.actual_board[(6, 8)].letter) +

      "\n7  "
      +
      str(self.actual_board[(7, 1)].letter) +
      "  " + str(self.actual_board[(7, 2)].letter) +
      "  " + str(self.actual_board[(7, 3)].letter) +
      "  " + str(self.actual_board[(7, 4)].letter) +
      "  " + str(self.actual_board[(7, 5)].letter) +
      "  " + str(self.actual_board[(7, 6)].letter) +
      "  " + str(self.actual_board[(7, 7)].letter) +
      "  " + str(self.actual_board[(7, 8)].letter) +

      "\n8  "
      +
      str(self.actual_board[(8, 1)].letter) +
      "  " + str(self.actual_board[(8, 2)].letter) +
      "  " + str(self.actual_board[(8, 3)].letter) +
      "  " + str(self.actual_board[(8, 4)].letter) +
      "  " + str(self.actual_board[(8, 5)].letter) +
      "  " + str(self.actual_board[(8, 6)].letter) +
      "  " + str(self.actual_board[(8, 7)].letter) +
      "  " + str(self.actual_board[(8, 8)].letter) +

      "\n   A  B  C  D  E  F  G  H")


    def check_king(self,king):
        king_position=king.position
        king_color=king.color
        opposing_pieces=[]
        mensagem="O rei não está em check"
        if king_color==0:
            for x in self.pieces:
                if x.color==1:
                    opposing_pieces.append(x)

            for x in opposing_pieces:
                if king_position in x.find_moves():
                    mensagem="Rei  está em check"
                    break

            print(mensagem)

        elif king_color==1:
            for x in self.pieces:
                if x.color==0:
                    opposing_pieces.append(x)


            for x in opposing_pieces:
                if king_position in x.find_moves():
                    mensagem="Rei está em check"
                    break

            print(mensagem)

    def put_pieces(self):
        self.update_piece(Pawn(1,(7,"A"),"White",self))
        self.update_piece(Pawn(2, (7, "B"), "White", self))
        self.update_piece(Pawn(3, (7, "C"), "White", self))
        self.update_piece(Pawn(4, (7, "D"), "White", self))
        self.update_piece(Pawn(5, (7, "E"), "White", self))
        self.update_piece(Pawn(6, (7, "F"), "White", self))
        self.update_piece(Pawn(7, (7, "G"), "White", self))
        self.update_piece(Pawn(8, (7, "H"), "White", self))
        self.update_piece(Rook(1, (8, "A"), "White", self))
        self.update_piece(Rook(2, (8, "H"), "White", self))
        self.update_piece(Bishop(1, (8, "C"), "White", self))
        self.update_piece(Bishop(2, (8, "F"), "White", self))
        self.update_piece(Knight(1, (8, "B"), "White", self))
        self.update_piece(Knight(2, (8, "G"), "White", self))
        self.update_piece(Queen(1, (8, "D"), "White", self))
        self.update_piece(King(1, (8, "E"), "White", self))

        self.update_piece(Pawn(1, (2, "A"), "Black", self))
        self.update_piece(Pawn(2, (2, "B"), "Black", self))
        self.update_piece(Pawn(3, (2, "C"), "Black", self))
        self.update_piece(Pawn(4, (2, "D"), "Black", self))
        self.update_piece(Pawn(5, (2, "E"), "Black", self))
        self.update_piece(Pawn(6, (2, "F"), "Black", self))
        self.update_piece(Pawn(7, (2, "G"), "Black", self))
        self.update_piece(Pawn(8, (2, "H"), "Black", self))
        self.update_piece(Rook(1, (1, "A"), "Black", self))
        self.update_piece(Rook(2, (1, "H"), "Black", self))
        self.update_piece(Bishop(1, (1, "C"), "Black", self))
        self.update_piece(Bishop(2, (1, "F"), "Black", self))
        self.update_piece(Knight(1, (1, "B"), "Black", self))
        self.update_piece(Knight(2, (1, "G"), "Black", self))
        self.update_piece(Queen(1, (1, "D"), "Black", self))
        self.update_piece(King(1, (1, "E"), "Black", self))




#Essa função inicia o GUI do tkinter
    def setup_tkinter_board(self):
        global mainframe
        global root
        flag = 0
        linha = 0
        coluna = 0
        self.root= root = Tk()
        root.title("Xadrez")
        ttk.Style().configure("black.TFrame", background="black")
        ttk.Style().configure("white.TFrame", background="white")
        mainframe = ttk.Frame(root)
        mainframe.grid(row=0, column=0)
        ###Esse código cria uma matriz 8x8 (uma mesa de xadrez) e um dicionário com todos os Frames
        for n in range(0, 64):
            if flag == 1:
                self.board_image[(linha, coluna)] = ttk.Frame(mainframe, height="3c", width="3c", style="black.TFrame")
                self.board_image[(linha, coluna)].grid(row=linha, column=coluna)
            elif flag == 0:
                self.board_image[(linha, coluna)] = ttk.Frame(mainframe, height="3c", width="3c", style="white.TFrame")
                self.board_image[(linha, coluna)].grid(row=linha, column=coluna)
            flag = not flag
            coluna += 1
            if coluna == 8:
                coluna = 0
                linha += 1
                flag = not flag

        for n in range(0, 8):
            root.columnconfigure(n, weight=1)
            root.rowconfigure(n, weight=1)

#Essa função cria as imagens das peças como Labels no Tkinter.
    def import_piece_images(self):

        global peao_preto_branco
        global peao_preto_preto
        global cavalo_preto_branco
        global cavalo_preto_preto
        global torre_preto_branco
        global torre_preto_preto
        global bispo_preto_branco
        global bispo_preto_preto
        global rainha_preto_branco
        global rainha_preto_preto
        global rei_preto_branco
        global rei_preto_preto
        global peao_branco_branco
        global peao_branco_preto
        global cavalo_branco_branco
        global cavalo_branco_preto
        global torre_branco_branco
        global torre_branco_preto
        global bispo_branco_branco
        global bispo_branco_preto
        global rainha_branco_branco
        global rainha_branco_preto
        global rei_branco_branco
        global rei_branco_preto

        peao_preto_branco = PhotoImage(file="peao_preto_branco.png")
        peao_preto_preto = PhotoImage(file="peao_preto_preto.png")
        cavalo_preto_branco= PhotoImage(file="cavalo_preto_branco.png")
        cavalo_preto_preto=  PhotoImage(file="cavalo_preto_preto.png")
        torre_preto_branco = PhotoImage(file="torre_preto_branco.png")
        torre_preto_preto  =PhotoImage(file="torre_preto_preto.png")
        bispo_preto_branco = PhotoImage(file="bispo_preto_branco.png")
        bispo_preto_preto=  PhotoImage(file="bispo_preto_preto.png")
        rainha_preto_branco =  PhotoImage(file="rainha_preto_branco.png")
        rainha_preto_preto =  PhotoImage(file="rainha_preto_preto.png")
        rei_preto_branco =  PhotoImage(file="rei_preto_branco.png")
        rei_preto_preto =  PhotoImage(file="rei_preto_preto.png")

        peao_branco_branco = PhotoImage(file="peao_branco_branco.png")
        peao_branco_preto = PhotoImage(file="peao_branco_preto.png")
        cavalo_branco_branco = PhotoImage(file="cavalo_branco_branco.png")
        cavalo_branco_preto = PhotoImage(file="cavalo_branco_preto.png")
        torre_branco_branco = PhotoImage(file="torre_branco_branco.png")
        torre_branco_preto = PhotoImage(file="torre_branco_preto.png")
        bispo_branco_branco = PhotoImage(file="bispo_branco_branco.png")
        bispo_branco_preto = PhotoImage(file="bispo_branco_preto.png")
        rainha_branco_branco = PhotoImage(file="rainha_branco_branco.png")
        rainha_branco_preto = PhotoImage(file="rainha_branco_preto.png")
        rei_branco_branco = PhotoImage(file="rei_branco_branco.png")
        rei_branco_preto = PhotoImage(file="rei_branco_preto.png")




#Essa função só deve ser usada uma vez para criar os Labels de imagem de peças no início do jogo, para mudanças após isso atualize os Labels.
    def create_labels(self):
        for piece in self.pieces:
            if piece.letter=="p":
               piece.label_preto = ttk.Label(mainframe,image=peao_preto_preto)
               piece.label_branco = ttk.Label(mainframe, image=peao_preto_branco)

            elif piece.letter=="P":
               piece.label_preto = ttk.Label(mainframe,image=peao_branco_preto)
               piece.label_branco = ttk.Label(mainframe, image=peao_branco_branco)

            elif piece.letter == "k":
                piece.label_preto = ttk.Label(mainframe, image=cavalo_preto_preto)
                piece.label_branco = ttk.Label(mainframe, image=cavalo_preto_branco)

            elif piece.letter == "K":
                piece.label_preto = ttk.Label(mainframe, image=cavalo_branco_preto)
                piece.label_branco = ttk.Label(mainframe, image=cavalo_branco_branco)

            elif piece.letter == "b":
                piece.label_preto = ttk.Label(mainframe, image=bispo_preto_preto)
                piece.label_branco = ttk.Label(mainframe, image=bispo_preto_branco)

            elif piece.letter == "B":
                piece.label_preto = ttk.Label(mainframe, image=bispo_branco_preto)
                piece.label_branco = ttk.Label(mainframe, image=bispo_branco_branco)

            elif piece.letter == "r":
                piece.label_preto = ttk.Label(mainframe, image=torre_preto_preto)
                piece.label_branco = ttk.Label(mainframe, image=torre_preto_branco)

            elif piece.letter == "R":
                piece.label_preto = ttk.Label(mainframe, image=torre_branco_preto)
                piece.label_branco = ttk.Label(mainframe, image=torre_branco_branco)

            elif piece.letter == "q":
                piece.label_preto = ttk.Label(mainframe, image=rainha_preto_preto)
                piece.label_branco = ttk.Label(mainframe, image=rainha_preto_branco)

            elif piece.letter == "Q":
                piece.label_preto = ttk.Label(mainframe, image=rainha_branco_preto)
                piece.label_branco = ttk.Label(mainframe, image=rainha_branco_branco)

            elif piece.letter == "z":
                piece.label_preto = ttk.Label(mainframe, image=rei_preto_preto)
                piece.label_branco = ttk.Label(mainframe, image=rei_preto_branco)

            elif piece.letter == "Z":
                piece.label_preto = ttk.Label(mainframe, image=rei_branco_preto)
                piece.label_branco = ttk.Label(mainframe, image=rei_branco_branco)

            else:pass

    def show_initial_labels(self):
        for piece in self.pieces:
            if piece.color == 1:

              if self.board_image[(piece.position[0]-1,piece.position[1]-1)]["style"]=="black.TFrame":
                piece.label_preto.grid(row=piece.position[0] - 1, column=piece.position[1] - 1)

              elif self.board_image[(piece.position[0] - 1, piece.position[1]-1)]["style"] == "white.TFrame":
                piece.label_branco.grid(row=piece.position[0] - 1, column=piece.position[1] - 1)

            if piece.color == 0:

                if self.board_image[(piece.position[0] - 1, piece.position[1] - 1)]["style"] == "black.TFrame":
                    piece.label_preto.grid(row=piece.position[0] - 1, column=piece.position[1] - 1)

                elif self.board_image[(piece.position[0] - 1, piece.position[1] - 1)]["style"] == "white.TFrame":
                    piece.label_branco.grid(row=piece.position[0] - 1, column=piece.position[1] - 1)



    def update_label(self,piece):
        if piece.color == 1:
            piece.label_branco.grid_forget()
            piece.label_preto.grid_forget()
            if self.board_image[(piece.position[0] - 1, piece.position[1] - 1)]["style"] == "black.TFrame":
                piece.label_preto.grid(row=piece.position[0] - 1, column=piece.position[1] - 1)

            elif self.board_image[(piece.position[0] - 1, piece.position[1] - 1)]["style"] == "white.TFrame":
                piece.label_branco.grid(row=piece.position[0] - 1, column=piece.position[1] - 1)





        elif piece.color == 0:
            piece.label_branco.grid_forget()
            piece.label_preto.grid_forget()
            if self.board_image[(piece.position[0] - 1, piece.position[1] - 1)]["style"] == "black.TFrame":
                piece.label_preto.grid(row=piece.position[0] - 1, column=piece.position[1] - 1)

            elif self.board_image[(piece.position[0] - 1, piece.position[1] - 1)]["style"] == "white.TFrame":
                piece.label_branco.grid(row=piece.position[0] - 1, column=piece.position[1] - 1)