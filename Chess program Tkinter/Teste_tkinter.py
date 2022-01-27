from Board import *
from time import sleep
x=Board()
x.initialize_board()
x.put_pieces()
x.print_board()
x.setup_tkinter_board()
x.root.update()
x.import_piece_images()
x.create_labels()
x.show_initial_labels()

sleep(1)
x.root.update()
sleep(1)
p=x.actual_board[(7,8)]
p.move_normal()
x.update_piece(p)
x.update_label(p)
x.root.update()
sleep(1)
p.move_normal()
x.update_piece(p)
x.update_label(p)
x.root.update()
sleep(1)
s=x.actual_board[(2,7)]
s.move_normal()
x.update_piece(s)
x.update_label(s)
x.root.update()
sleep(1)
s.move_normal()
x.update_piece(s)
x.update_label(s)
x.root.update()
sleep(1)
s.move((5,"H"))
x.update_piece(s)
x.update_label(s)
x.root.update()
sleep(1)
s.move_normal()
x.update_piece(s)
x.update_label(s)
x.root.update()
sleep(1)
k=x.actual_board[(8,7)]
k.move((6,"H"))
print(k.old)
x.update_piece(k)
x.update_label(k)
x.root.update()
sleep(1)
k.move((5,"F"))
x.update_piece(k)
x.update_label(k)
x.root.update()
sleep(1)
