from tkinter import *
from tkinter import ttk
from Old_code.Board import *


class Tela:
    def __init__(self, board):
        self.dict = dict()
        self.color_dict = dict()
        self.board = board
        self.root = None
        self.last_color = None
        self.image = None
        self.action=False
        self.action_piece=None
        self.possible_positions=None
        self.movepiece=False
        self.right_castle=None
        self.left_castle=None

    def initiate(self):
        '''Inicializa o display do jogo de xadrez'''

        self.root = Tk()
        self.root.title("Xadrez")
        self.root.config(bg="green")
        self.root.minsize(1000, 840)
        self.root.rowconfigure(0, weight=1)
        self.root.columnconfigure(0, weight=1)


        frm = ttk.Frame(self.root)
        frm.grid()

        ###Coloca os 64 Labels em seus lugares com cores alternadas e uma imagem vazia dentro de cada um
        ###Também adiciona esses 64 Labels a self.dict com índices em forma de tuples EX: self.dic[(1,1)] = label1, self.dic[(8,8)] = label64
        flag = True
        a = 1
        b = 1
        self.image = PhotoImage(master=self.root)
        for n in range(0, 64):

            flag = not flag
            if flag:
                x = Label(frm, bg="black", image=self.image, height=100, width=100)
                x.grid(row=a, column=b, sticky="news")

            else:
                x = Label(frm, bg="white", image=self.image, height=100, width=100)
                x.grid(row=a, column=b, sticky="news")

            self.dict[(a, b)] = x
            self.color_dict[(a, b)] = "black" if flag else "white"
            if b > 7:
                b = 0
                a += 1
                flag = not flag
            b += 1

        # Letras de identificação de posição na mesa
        Label(frm, text="8", bg="green", foreground="black").grid(row=1, column=0, sticky="news")
        Label(frm, text="7", bg="green", foreground="black").grid(row=2, column=0, sticky="news")
        Label(frm, text="6", bg="green", foreground="black").grid(row=3, column=0, sticky="news")
        Label(frm, text="5", bg="green", foreground="black").grid(row=4, column=0, sticky="news")
        Label(frm, text="4", bg="green", foreground="black").grid(row=5, column=0, sticky="news")
        Label(frm, text="3", bg="green", foreground="black").grid(row=6, column=0, sticky="news")
        Label(frm, text="2", bg="green", foreground="black").grid(row=7, column=0, sticky="news")
        Label(frm, text="1", bg="green", foreground="black").grid(row=8, column=0, sticky="news")

        Label(frm, text="A", bg="green", foreground="black").grid(row=0, column=1, sticky="news")
        Label(frm, text="B", bg="green", foreground="black").grid(row=0, column=2, sticky="news")
        Label(frm, text="C", bg="green", foreground="black").grid(row=0, column=3, sticky="news")
        Label(frm, text="D", bg="green", foreground="black").grid(row=0, column=4, sticky="news")
        Label(frm, text="E", bg="green", foreground="black").grid(row=0, column=5, sticky="news")
        Label(frm, text="F", bg="green", foreground="black").grid(row=0, column=6, sticky="news")
        Label(frm, text="G", bg="green", foreground="black").grid(row=0, column=7, sticky="news")
        Label(frm, text="H", bg="green", foreground="black").grid(row=0, column=8, sticky="news")

        Label(frm, bg="green").grid(row=0, column=0, sticky="news")

        #Ajusta os parametros de weight do grid para os Labels
        a = 0
        b = 0
        for n in range(0, 8):
            frm.rowconfigure(a, weight=1)
            a += 1

        for n in range(0, 8):
            frm.columnconfigure(b, weight=1)
            b += 1

        #Essas funções e o for-loop mudam a cor de cada quadrado ao passar o mouse
        def change_color(event):
            a = event.widget
            self.last_color = a.cget('bg')
            a.config(bg="red")

        def change_color_normal(event=False):
            if not self.action:
                for n, value in self.dict.items():
                   value.config(bg=self.color_dict[n] ,relief="flat")

            elif event.widget.cget("bg")!="blue":
                event.widget.config(bg=self.last_color)


        for value in self.dict.values():
            value.bind("<Enter>", change_color)
            value.bind("<Leave>", change_color_normal)

        #Define a tecla q como "retornar ao normal" o que reseta a escolha de peças na GUI
        def return_to_normal(event):
            self.action=False

        self.root.bind_all("q", return_to_normal)

    def board_activate(self):
        """Essa função irá ativar a board que fica em self.board"""
        self.board.initialize_board()
        self.board.put_pieces()

    def load_images(self):
        from PIL import Image, ImageTk
        black_pawn = Image.open("./images/pawn_black.png")
        black_tower = Image.open("./images/tower_black.png")
        black_rook = Image.open("./images/rook_black.png")
        black_knight = Image.open("./images/horse_black.png")
        black_king = Image.open("./images/king_black.png")
        black_queen = Image.open("./images/queen_black.png")
        white_pawn = Image.open("./images/pawn_white.png")
        white_tower = Image.open("./images/tower_white.png")
        white_rook = Image.open("./images/rook_white.png")
        white_knight = Image.open("./images/horse_white.png")
        white_king = Image.open("./images/king_white.png")
        white_queen = Image.open("./images/queen_white.png")

        display_black_pawn   = ImageTk.PhotoImage(master=self.root, image=black_pawn)
        display_black_tower  = ImageTk.PhotoImage(master=self.root, image=black_tower)
        display_black_rook   = ImageTk.PhotoImage(master=self.root, image=black_rook)
        display_black_knight = ImageTk.PhotoImage(master=self.root, image=black_knight)
        display_black_king   = ImageTk.PhotoImage(master=self.root, image=black_king)
        display_black_queen  = ImageTk.PhotoImage(master=self.root, image=black_queen)
        display_white_pawn   = ImageTk.PhotoImage(master=self.root, image=white_pawn)
        display_white_tower  = ImageTk.PhotoImage(master=self.root, image=white_tower)
        display_white_rook   = ImageTk.PhotoImage(master=self.root, image=white_rook)
        display_white_knight = ImageTk.PhotoImage(master=self.root, image=white_knight)
        display_white_king   = ImageTk.PhotoImage(master=self.root, image=white_king)
        display_white_queen  = ImageTk.PhotoImage(master=self.root, image=white_queen)

        pawn_images = {0:display_white_pawn, 1:display_black_pawn}
        knight_images = {0:display_white_knight,1:display_black_knight}
        bishop_images = {0:display_white_rook, 1:display_black_rook}
        rook_images = {0: display_white_tower, 1:display_black_tower}
        queen_images = {0: display_white_queen, 1:display_black_queen}
        king_images = {0: display_white_king, 1: display_black_king}

        self.images_dict={Pawn:pawn_images,Knight:knight_images, Bishop: bishop_images, Rook:rook_images, Queen:queen_images, King: king_images}



    def update_screen(self):
        """Função que atualiza o display da mesa com o objeto de board em self.board"""
        for key, value in self.board.actual_board.items():
            if isinstance(value, Empty):
                self.dict[key].config(image=self.image)

            elif isinstance(value, Pawn):
                if value.color==0:
                    self.dict[key].config(image=self.images_dict[Pawn][0])
                else:
                    self.dict[key].config(image=self.images_dict[Pawn][1])
            elif isinstance(value, Rook):
                if value.color==0:
                    self.dict[key].config(image=self.images_dict[Rook][0])
                else:
                    self.dict[key].config(image=self.images_dict[Rook][1])

            elif isinstance(value, Bishop):
                if value.color==0:
                    self.dict[key].config(image=self.images_dict[Bishop][0])
                else:
                    self.dict[key].config(image=self.images_dict[Bishop][1])

            elif isinstance(value, Queen):
                if value.color==0:
                    self.dict[key].config(image=self.images_dict[Queen][0])
                else:
                    self.dict[key].config(image=self.images_dict[Queen][1])

            elif isinstance(value, Knight):
                if value.color==0:
                    self.dict[key].config(image=self.images_dict[Knight][0])
                else:
                    self.dict[key].config(image=self.images_dict[Knight][1])

            elif isinstance(value, King):
                if value.color==0:
                    self.dict[key].config(image=self.images_dict[King][0])
                else:
                    self.dict[key].config(image=self.images_dict[King][1])

    def update_piece_place(self ,tile, castle=False):
        if castle:
            self.action_piece.old = self.action_piece.position
            self.dict[self.action_piece.old].config(image=self.image)
            self.action_piece.position = self.new_dict[tile]
            self.dict[self.action_piece.position].config(
                image=self.images_dict[type(self.action_piece)][self.action_piece.color])

            self.board.update_piece(self.action_piece)

            self.action = False
            if not self.action:
                for n, value in self.dict.items():
                    value.config(bg=self.color_dict[n], relief="flat")

        elif self.new_dict[tile] in self.possible_positions:

            self.action_piece.old=self.action_piece.position
            self.dict[self.action_piece.old].config(image=self.image)
            self.action_piece.position=self.new_dict[tile]
            self.dict[self.action_piece.position].config(image=self.images_dict[type(self.action_piece)][self.action_piece.color])

            self.board.update_piece(self.action_piece)

            self.action=False
            if not self.action:
                for n, value in self.dict.items():
                   value.config(bg=self.color_dict[n], relief="flat")



    def action_function(self):
        self.new_dict=dict()
        for key , value in self.dict.items():
            self.new_dict[value]=key

        def action(event):
            a=event.widget
            if self.board.actual_board[self.new_dict[a]]!=self.board.empty_space:
                print("essa é a posição")
                print(self.board.actual_board[self.new_dict[a]].position)
            piece=self.board.actual_board[self.new_dict[a]]
            if str(a.cget("image"))=="pyimage1":
                if self.action==True:
                    if isinstance(self.action_piece, King):
                        print("Is King")
                        print(self.new_dict[a],self.left_castle)
                        if self.new_dict[a] == self.left_castle:
                            print("left_castle_white")
                            self.update_piece_place(a, castle=True)
                            if self.action_piece.color==0:
                                self.action_piece=self.board.actual_board[8,1]
                                direction=(8,4)
                            else:
                                self.action_piece = self.board.actual_board[1, 1]
                                direction=(1,4)
                            self.update_piece_place(self.dict[direction], castle=True)

                        elif self.new_dict[a] == self.right_castle:
                                self.update_piece_place(a ,castle=True)
                                if self.action_piece.color == 0:
                                    self.action_piece = self.board.actual_board[8, 8]
                                    direction = (8, 6)
                                else:
                                    self.action_piece = self.board.actual_board[1, 8]
                                    direction = (1, 6)
                                self.update_piece_place(self.dict[direction],castle=True)

                    self.update_piece_place(a)
                    self.action=False

            if self.action==True:



                if piece.color == self.action_piece.color:
                    for n, value in self.dict.items():
                        value.config(bg=self.color_dict[n])
                else:
                    self.update_piece_place(a)
                    return

            if isinstance(piece, King):
                possible=piece.find_moves()
                if isinstance(possible, tuple):
                    normal=possible[0]
                    castle=possible[1]
                    for n in castle:
                        if piece.position[1] > n[1]:
                            self.left_castle = n
                        elif piece.position[1] < n[1]:
                            self.right_castle = n
                        self.dict[n].config(bg="purple", relief="solid")
                else: normal=possible
                for n in normal:
                    self.dict[n].config(bg="orange", relief="solid")
                a.config(bg="blue")
                self.action=True
                self.action_piece=piece
                self.possible_positions=normal

            elif isinstance(piece, Pawn):
                possible=piece.find_moves()
                print("this is possible")
                print(possible)
                if isinstance(possible, tuple):
                    print("lol")
                    normal=possible[0]
                    enpassant=[x for x in possible[1] if x!=0]
                    self.enpassant=enpassant

                    for n in enpassant:
                        self.dict[n].config(bg="purple")


                    for n in normal:
                        self.dict[n].config(bg="orange", relief="solid")
                    a.config(bg="blue")
                    self.action = True
                    self.action_piece = piece
                    self.possible_positions = normal


                else:
                    for n in possible:
                        self.dict[n].config(bg="orange", relief="solid")
                    a.config(bg="blue")
                    self.action = True
                    self.action_piece = piece
                    self.possible_positions = possible



            elif isinstance(piece, Piece):
                possible=(piece.find_moves())
                for n in possible:
                    self.dict[n].config(bg="orange", relief="solid")
                a.config(bg="blue")
                self.action=True
                self.action_piece=piece
                self.possible_positions=possible



        for label in self.dict.values():
            label.bind('<ButtonPress-1>', action)

    #Essa parte seria para criar movimentos de arraste para movimentar as peças, porém isso foi descartado pois precisaria de um canvas, já que o tkinter
    # normal não possui labels transparentes (até onde achei)
    #
    #def test_func_mouse_tracing(self):
    #    self.label=Label(self.root, image=self.image, bg="pink",height=40, width=40)
    #
    #
    #    def HelloWorld(event):
    #        x=event.x
    #        y=event.y
    #        a=event.widget
    #        ax=a.winfo_rootx()
    #        ay=a.winfo_rooty()
    #        self.label.place(x=self.root.winfo_pointerx()-self.root.winfo_rootx()-20, y=self.root.winfo_pointery()-self.root.winfo_rooty()-20)
    #
    #
    #    self.root.bind_all('<Button-1>',HelloWorld)

    #def move_piece_action(self):
    #    self.new_dict = dict()
    #    for key, value in self.dict.items():
    #        self.new_dict[value] = key
    #
    #    def movepiece(event):
    #        x = event.x
    #        y = event.y
    #        a = event.widget
    #        ax = a.winfo_rootx()
    #        ay = a.winfo_rooty()
    #
    #    def function1(event):
    #        label = event.widget
    #        piece = self.board.actual_board[self.new_dict[label]]
    #        print(self.new_dict[label])
    #        #Checa se o quadro clicado é de uma peça e, se for, começa uma ação
    #        if isinstance(piece, Piece) and self.action==False:
    #            self.action=True
    #            self.action_piece=piece
    #            self.possible_positions = piece.find_moves()
    #
    #            #Colore as ações possíveis e a peça escolhida
    #            self.dict[piece.position].config(bg="purple")
    #            for position in self.possible_positions:
    #                self.dict[position].config(bg="orange")
    #
    #        #Se o quadro clicado não for uma peça, tenta concluir uma ação e encerra a atual
    #        #elif self.action == True:
    #        #    self.action=False
    #        #    self.update_piece_place(label)
    #
    #    def function2(event):
    #        if self.action:
    #            label=event.widget.winfo_containing(event.x_root, event.y_root)
    #            self.action = False
    #            self.update_piece_place(label)
    #
    #    #def function3(event):
    #
    #
    #
    #
    #
    #    for label in self.dict.values():
    #        label.bind('<Button-1>', function1)
    #        label.bind('<ButtonRelease-1>', function2)
    #        #label.bind('<B1-Motion', function)











y=Board()


x=Tela(y)
x.initiate()
x.board_activate()
x.load_images()

x.update_screen()

x.action_function()

x.root.mainloop()





















