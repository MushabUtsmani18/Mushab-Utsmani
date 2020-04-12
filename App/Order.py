import sys
import Tkinter as tk
import ttk
import Order_support
import PembayaranO
import HOME

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = formCustomDemo (root)
    Order_support.__init__(root, top)
    root.mainloop()

w = None
def create_formCustomDemo(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_formCustomDemo(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = formCustomDemo (w)
    Order_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_formCustomDemo():
    global w
    w.destroy()
    w = None

class formCustomDemo:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font9 = "TkDefaultFont"
        self.style = ttk.Style()
        if sys.platform == "win32":
            self.style.theme_use('winnative')
        self.style.configure('.',background=_bgcolor)
        self.style.configure('.',foreground=_fgcolor)
        self.style.map('.',background=
            [('selected', _compcolor), ('active',_ana2color)])

        top.geometry("529x522+296+123")
        top.minsize(120, 1)
        top.maxsize(1265, 770)
        top.resizable(1, 1)
        top.title("Custom Widget Demo")
        top.configure(background="#d9d9d9")
        top.configure(highlightbackground="#d9d9d9")
        top.configure(highlightcolor="black")

        self.style.configure('TSizegrip', background=_bgcolor)
        self.TSizegrip1 = ttk.Sizegrip(top)
        self.TSizegrip1.place(anchor='se', relx=1.0, rely=1.0)

        self.Message1 = tk.Message(top)
        self.Message1.place(relx=0.038, rely=0.029, relheight=0.121
                , relwidth=0.928)
        self.Message1.configure(background="#d9d9d9")
        self.Message1.configure(font=font9)
        self.Message1.configure(foreground="#000000")
        self.Message1.configure(highlightbackground="#d9d9d9")
        self.Message1.configure(highlightcolor="black")
        self.Message1.configure(relief="sunken")
        self.Message1.configure(text='''Message''')
        self.Message1.configure(width=491)

        self.Frame1 = tk.Frame(top)
        self.Frame1.place(relx=0.057, rely=0.211, relheight=0.718
                , relwidth=0.501)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")
        self.Frame1.configure(highlightbackground="#d9d9d9")
        self.Frame1.configure(highlightcolor="black")

        self.Custom1 = Order_support.Custom(self.Frame1)
        self.Custom1.place(relx=0.0, rely=0.0, relheight=1.0, relwidth=1.0)

        self.btnGetOrder = tk.Button(top,command=PembayaranO.vp_start_gui)
        self.btnGetOrder.place(relx=0.681, rely=0.335, height=30, width=110)
        self.btnGetOrder.configure(activebackground="#d9d9d9")
        self.btnGetOrder.configure(activeforeground="black")
        self.btnGetOrder.configure(background="#d9d9d9")
        self.btnGetOrder.configure(command=Order_support.on_btnGetOrder)
        self.btnGetOrder.configure(cursor="fleur")
        self.btnGetOrder.configure(disabledforeground="#a3a3a3")
        self.btnGetOrder.configure(font=font9)
        self.btnGetOrder.configure(foreground="#000000")
        self.btnGetOrder.configure(highlightbackground="#d9d9d9")
        self.btnGetOrder.configure(highlightcolor="black")
        self.btnGetOrder.configure(pady="0")
        self.btnGetOrder.configure(text='''Get Order''')

        self.btnClearChecks = tk.Button(top)
        self.btnClearChecks.place(relx=0.681, rely=0.527, height=30, width=110)
        self.btnClearChecks.configure(activebackground="#d9d9d9")
        self.btnClearChecks.configure(activeforeground="black")
        self.btnClearChecks.configure(background="#d9d9d9")
        self.btnClearChecks.configure(command=Order_support.on_btnClearChecks)
        self.btnClearChecks.configure(disabledforeground="#a3a3a3")
        self.btnClearChecks.configure(font=font9)
        self.btnClearChecks.configure(foreground="#000000")
        self.btnClearChecks.configure(highlightbackground="#d9d9d9")
        self.btnClearChecks.configure(highlightcolor="black")
        self.btnClearChecks.configure(pady="0")
        self.btnClearChecks.configure(text='''Clear Checks''')

        self.btnExit = tk.Button(top)
        self.btnExit.place(relx=0.681, rely=0.718, height=30, width=110)
        self.btnExit.configure(activebackground="#d9d9d9")
        self.btnExit.configure(activeforeground="black")
        self.btnExit.configure(background="#d9d9d9")
        self.btnExit.configure(command=Order_support.on_btnExit)
        self.btnExit.configure(disabledforeground="#a3a3a3")
        self.btnExit.configure(font=font9)
        self.btnExit.configure(foreground="#000000")
        self.btnExit.configure(highlightbackground="#d9d9d9")
        self.btnExit.configure(highlightcolor="black")
        self.btnExit.configure(pady="0")
        self.btnExit.configure(text='''Exit''')

if __name__ == '__main__':
    vp_start_gui()





