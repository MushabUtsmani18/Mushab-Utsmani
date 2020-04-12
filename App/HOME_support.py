import sys
import Tkinter as tk
import ttk



def __init__(top, gui, *args, **kwargs):
    global w, top_level, root
    w = gui
    top_level = top
    root = top

def LoginButton(p1):
    print  ("Login Session")
    sys.stdout.flush()
    

def RegisterLogin(p1):
    print  ("Register Session")
    sys.stdout.flush()
    

def destroy_window():
    # Function which closes the window.
    global top_level
    top_level.destroy()
    top_level = None

if __name__ == '__main__':
    import HOME
    HOME.vp_start_gui()





