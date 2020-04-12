
import sys
import Tkinter as tk
import ttk
import Login_support
import Order
import Order_support

def vp_start_gui():
    '''Starting point when module is the main routine.'''
    global val, w, root
    root = tk.Tk()
    top = LoginSession (root)
    Login_support.init(root, top)
    root.mainloop()

w = None
def create_LoginSession(rt, *args, **kwargs):
    '''Starting point when module is imported by another module.
       Correct form of call: 'create_LoginSession(root, *args, **kwargs)' .'''
    global w, w_win, root
    #rt = root
    root = rt
    w = tk.Toplevel (root)
    top = LoginSession (w)
    Login_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_LoginSession():
    global w
    w.destroy()
    w = None

class LoginSession:
    def __init__(self, top=None):
        '''This class configures and populates the toplevel window.
           top is the toplevel containing window.'''
        _bgcolor = '#d9d9d9'  # X11 color: 'gray85'
        _fgcolor = '#000000'  # X11 color: 'black'
        _compcolor = '#d9d9d9' # X11 color: 'gray85'
        _ana1color = '#d9d9d9' # X11 color: 'gray85'
        _ana2color = '#ececec' # Closest X11 color: 'gray92'
        font11 = "-family {Segoe UI} -size 12"
        font12 = "-family {Segoe UI} -size 10 -weight bold"

        top.geometry("473x361+585+159")
        top.minsize(120, 1)
        top.maxsize(1604, 881)
        top.resizable(1, 1)
        top.title("New Toplevel")
        top.configure(background="#d9d9d9")

        self.LoginLable = tk.Message(top)
        self.LoginLable.place(relx=0.0, rely=0.0, relheight=0.313
                , relwidth=1.015)
        self.LoginLable.configure(background="#060606")
        self.LoginLable.configure(font=font11)
        self.LoginLable.configure(foreground="#fdfdfd")
        self.LoginLable.configure(highlightbackground="#d9d9d9")
        self.LoginLable.configure(highlightcolor="black")
        self.LoginLable.configure(text='''LOGIN
MASUKAN USERNAME DAN PASSWORD UNTUK LOGIN''')
        self.LoginLable.configure(width=480)

        self.Label1 = tk.Label(top)
        self.Label1.place(relx=0.021, rely=0.36, height=21, width=73)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#000000")
        self.Label1.configure(text='''USERNAME :''')

        self.Label2 = tk.Label(top)
        self.Label2.place(relx=0.021, rely=0.554, height=21, width=74)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#000000")
        self.Label2.configure(text='''PASSWORD :''')

        self.UsernameEntry = tk.Entry(top)
        self.UsernameEntry.place(relx=0.042, rely=0.443, height=30
                , relwidth=0.896)
        self.UsernameEntry.configure(background="white")
        self.UsernameEntry.configure(disabledforeground="#a3a3a3")
        self.UsernameEntry.configure(font="TkFixedFont")
        self.UsernameEntry.configure(foreground="#000000")
        self.UsernameEntry.configure(insertbackground="black")

        self.PasswordEntry = tk.Entry(top)
        self.PasswordEntry.place(relx=0.042, rely=0.609, height=30
                , relwidth=0.896)
        self.PasswordEntry.configure(background="white")
        self.PasswordEntry.configure(disabledforeground="#a3a3a3")
        self.PasswordEntry.configure(font="TkFixedFont")
        self.PasswordEntry.configure(foreground="#000000")
        self.PasswordEntry.configure(insertbackground="black")
        self.PasswordEntry.configure(show="*")

        self.LoginButton = tk.Button(top, command=Order.vp_start_gui)
        self.LoginButton.place(relx=0.042, rely=0.776, height=34, width=427)
        self.LoginButton.configure(activebackground="#ececec")
        self.LoginButton.configure(activeforeground="#000000")
        self.LoginButton.configure(background="#00a832")
        self.LoginButton.configure(disabledforeground="#a3a3a3")
        self.LoginButton.configure(font=font12)
        self.LoginButton.configure(foreground="#000000")
        self.LoginButton.configure(highlightbackground="#d9d9d9")
        self.LoginButton.configure(highlightcolor="black")
        self.LoginButton.configure(pady="0")
        self.LoginButton.configure(text='''LOGIN''')
        self.LoginButton.bind('<Button-1>',lambda e:Login_support.LogButton(e))

if __name__ == '__main__':
    vp_start_gui()





