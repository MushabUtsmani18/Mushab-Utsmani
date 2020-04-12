import sys
from ScrolledCheckedListBox import ScrolledCheckedListBox
from Tkinter import *
import ttk



def on_click(s=None):
    update_label()
    print(w.Custom1.get())


def on_btnDeleteBarang():
    w.Custom1.clear()
    w.Message1.configure(text='')


def on_btnExit():
    destroy_window()


def on_btnTambahBarang():
    lst = w.Custom1.get()
    print(lst)


def __init__(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top
    global ListInfo, ListInfo2
   
    ListInfo = [['Beng-Beng'], 'Chocolatos', 'Oreo', 'Ultramilk', 'Nabati', 'Kacang Garuda',
                'Indomilk']
    ListInfo2 = [['Beng-Beng', 'Rp 180.000'], ['Chocolatos', 'Rp 160.000'],
                 ['Oreo', 'Rp 170.000'], ['Ultramilk', 'Rp 100.000'],['Nabati', 'Rp 120.000'],
                 ['Kacang Garuda', 'Rp 80.000'], ['Indomilk', 'Rp 110.000']]

    initialize_order()


def initialize_order():
    w.Custom1.cback = on_click
    # To use a single list of item names comment out the next line and
    # uncomment the second line down.
    w.Custom1.load(ListInfo2)
    # w.Custom1.load(ListInfo)
    clear_label()
    set_labels()



def set_labels():
    w.Custom1.set([''])
    update_label()



def update_label():
    dat = w.Custom1.get()
    lst = []
    for x in dat:
        # print(len(x),x)
        if len(x) == 2:
            t = x[0]
            k = x[1]
            lst.append(t)
        else:
            lst.append(x)
    s = ", ".join(lst)
    w.Message1.configure(text=s)


def clear_label():
    w.Message1.configure(text="")


def destroy_window():
    
    global top_level
    top_level.destroy()
    top_level = None



Custom = Frame
Custom = ScrolledCheckedListBox


if __name__ == '__main__':
    import Order
    Order.vp_start_gui()


