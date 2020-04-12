import sys
import Tkinter as tk
import ttk
import HOME_support
import Login
import Register

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root, output
    root = tk.Tk()
    top = HOME (root)
    HOME_support.__init__(root, top)
    root.mainloop()

w = None
def create_HOME(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_HOME(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = HOME (w)
    HOME_support.__init__(w, top, *args, **kwargs)
    return (w, top)

def destroy_HOME():
    global w
    w.destroy()
    w = None

class HOME:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'

        top.geometry("400x350+530+176")
        top.minsize(120, 1)
        top.maxsize(1604, 881)
        top.resizable(1, 1)
        top.title("GROCERYBOX")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#f0f0f0f0f0f0")
        top.configure(highlightcolor="black")

        self.LOGIN = tk.Button(top, command=Login.vp_start_gui)
        self.LOGIN.place(relx=0.25, rely=0.4, height=64, width=187)
        self.LOGIN.configure(activebackground="#ececec")
        self.LOGIN.configure(activeforeground="#000000")
        self.LOGIN.configure(background="#00a832")
        self.LOGIN.configure(disabledforeground="#a3a3a3")
        self.LOGIN.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.LOGIN.configure(foreground="#000000")
        self.LOGIN.configure(highlightbackground="#d9d9d9")
        self.LOGIN.configure(highlightcolor="black")
        self.LOGIN.configure(pady="0")
        self.LOGIN.configure(text='''LOGIN''')
        
        
    

        self.REGISTER = tk.Button(top, command=Register.vp_start_gui)
        self.REGISTER.place(relx=0.25, rely=0.657, height=64, width=187)
        self.REGISTER.configure(activebackground="#ececec")
        self.REGISTER.configure(activeforeground="#000000")
        self.REGISTER.configure(background="#00a832")
        self.REGISTER.configure(disabledforeground="#a3a3a3")
        self.REGISTER.configure(font="-family {Segoe UI} -size 13 -weight bold")
        self.REGISTER.configure(foreground="#000000")
        self.REGISTER.configure(highlightbackground="#d9d9d9")
        self.REGISTER.configure(highlightcolor="black")
        self.REGISTER.configure(pady="0")
        self.REGISTER.configure(text='''REGISTER''')
        
        

        self.menubar = tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu = self.menubar)

        self.Label1 = tk.Message(top)
        self.Label1.place(relx=-0.025, rely=0.0, relheight=0.294, relwidth=1.05)
        self.Label1.configure(background="#0b0b0b")
        self.Label1.configure(font="-family {Segoe UI} -size 11 -weight bold")
        self.Label1.configure(foreground="#ffffff")
        self.Label1.configure(highlightbackground="#d9d9d9")
        self.Label1.configure(highlightcolor="black")
        self.Label1.configure(text='''GROCERYBOX
PILIHAN TEPAT BELANJA KEBUTUHAN TOKO ANDA''')
        self.Label1.configure(width=420)



if __name__ == '__main__':
    vp_start_gui()





