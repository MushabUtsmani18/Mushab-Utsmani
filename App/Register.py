import sys
import Tkinter as tk
import ttk
import Register_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = RegisterSession (root)
    Register_support.init(root, top)
    root.mainloop()

w = None
def create_RegisterSession(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_RegisterSession(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = RegisterSession (w)
    Register_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_RegisterSession():
    global w
    w.destroy()
    w = None

class RegisterSession:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font10 = "-family {Segoe UI} -size 10 -weight bold"
        font9 = "-family {Segoe UI} -size 13"

        top.geometry("402x418+768+8")
        top.minsize(120, 1)
        top.maxsize(1604, 881)
        top.resizable(1, 1)
        top.title("RegisterSession")
        top.configure(background="#d9d9d9")

        self.RegisterLabel = tk.Message(top)
        self.RegisterLabel.place(relx=-0.025, rely=0.0, relheight=0.184
                , relwidth=1.032)
        self.RegisterLabel.configure(background="#080808")
        self.RegisterLabel.configure(cursor="arrow")
        self.RegisterLabel.configure(font=font9)
        self.RegisterLabel.configure(foreground="#fdfdfd")
        self.RegisterLabel.configure(highlightbackground="#d9d9d9")
        self.RegisterLabel.configure(highlightcolor="black")
        self.RegisterLabel.configure(text='''REGISTER
MASUKAN DATA UNTUK REGISTER''')
        self.RegisterLabel.configure(width=490)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.022, rely=0.22, height=21, width=69)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''USERNAME''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.025, rely=0.335, height=19, width=45)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''EMAIL''')

        self.Label3 = tk.Label(top)
        self.Label3.place(relx=0.025, rely=0.431, height=19, width=69)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#000000")
        self.Label3.configure(text='''PASSWORD''')

        self.Label4 = tk.Label(top)
        self.Label4.place(relx=0.025, rely=0.526, height=19, width=56)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#000000")
        self.Label4.configure(text='''ALAMAT''')

        self.Label5 = tk.Label(top)
        self.Label5.place(relx=0.025, rely=0.622, height=19, width=55)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#000000")
        self.Label5.configure(text='''NO TELP''')

        self.Entry2 = tk.Entry(top)
        self.Entry2.place(relx=0.224, rely=0.208,height=30, relwidth=0.731)
        self.Entry2.configure(background="white")
        self.Entry2.configure(disabledforeground="#a3a3a3")
        self.Entry2.configure(font="TkFixedFont")
        self.Entry2.configure(foreground="#000000")
        self.Entry2.configure(insertbackground="black")

        self.Entry3 = tk.Entry(top)
        self.Entry3.place(relx=0.224, rely=0.311,height=30, relwidth=0.731)
        self.Entry3.configure(background="white")
        self.Entry3.configure(disabledforeground="#a3a3a3")
        self.Entry3.configure(font="TkFixedFont")
        self.Entry3.configure(foreground="#000000")
        self.Entry3.configure(insertbackground="black")

        self.Entry4 = tk.Entry(top)
        self.Entry4.place(relx=0.224, rely=0.407,height=30, relwidth=0.731)
        self.Entry4.configure(background="white")
        self.Entry4.configure(disabledforeground="#a3a3a3")
        self.Entry4.configure(font="TkFixedFont")
        self.Entry4.configure(foreground="#000000")
        self.Entry4.configure(insertbackground="black")

        self.Entry5 = tk.Entry(top)
        self.Entry5.place(relx=0.224, rely=0.502,height=30, relwidth=0.731)
        self.Entry5.configure(background="white")
        self.Entry5.configure(disabledforeground="#a3a3a3")
        self.Entry5.configure(font="TkFixedFont")
        self.Entry5.configure(foreground="#000000")
        self.Entry5.configure(insertbackground="black")

        self.Entry6 = tk.Entry(top)
        self.Entry6.place(relx=0.224, rely=0.598,height=30, relwidth=0.731)
        self.Entry6.configure(background="white")
        self.Entry6.configure(disabledforeground="#a3a3a3")
        self.Entry6.configure(font="TkFixedFont")
        self.Entry6.configure(foreground="#000000")
        self.Entry6.configure(insertbackground="black")

        self.RegisterButton = tk.Button(top)
        self.RegisterButton.place(relx=0.05, rely=0.844, height=34, width=367)
        self.RegisterButton.configure(activebackground="#ececec")
        self.RegisterButton.configure(activeforeground="#000000")
        self.RegisterButton.configure(background="#00a832")
        self.RegisterButton.configure(cursor="fleur")
        self.RegisterButton.configure(disabledforeground="#a3a3a3")
        self.RegisterButton.configure(font=font10)
        self.RegisterButton.configure(foreground="#000000")
        self.RegisterButton.configure(highlightbackground="#d9d9d9")
        self.RegisterButton.configure(highlightcolor="black")
        self.RegisterButton.configure(pady="0")
        self.RegisterButton.configure(text='''REGISTER''')
        self.RegisterButton.bind('<Button-1>',lambda e:Register_support.RegisterButton(e))

if __name__ == '__main__':
    vp_start_gui()





