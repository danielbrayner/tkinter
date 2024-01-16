from tkinter import *
from tkinter import ttk
from tela_login_back import FuncsTelaLogin


root_login_front = Tk()

class Rootlogin(FuncsTelaLogin):
    def __init__(self):
        self.root_login_front = root_login_front
        self.root_login()
        self.frame_da_root_login()
        self.widget_frame_root_login()
        root_login_front.mainloop()

    def root_login(self):
        self.root_login_front.title("Unichristus - Login")

        #iniciar tela ao centro:
        screen_width = self.root_login_front.winfo_screenwidth()
        screen_height = self.root_login_front.winfo_screenheight()
        x = (screen_width // 2) - (700 // 2)
        y = (screen_height // 2) - (400 // 2)
        self.root_login_front.geometry(f"{700}x{350}+{x}+{y}")

        self.root_login_front.resizable(False, False)
        self.root_login_front.configure(bg="white")

    def frame_da_root_login(self):
        self.frame_1_root_login = Frame(self.root_login_front, bg="#cfcfcf")
        self.frame_1_root_login.place(relx=0, rely=0, relwidth=0.59, relheight=1)

        self.frame_2_root_login = Frame(self.root_login_front, bg="#0a448e")
        self.frame_2_root_login.place(relx=0.594, rely=0, relwidth=0.406, relheight=1)

    def widget_frame_root_login(self):
        #FRAME 1
        self.img_root_login_logo = PhotoImage(file="icons/logo_unichristus.png")
        self.logo_frame1_root_login = Label(self.frame_1_root_login, image=self.img_root_login_logo, bg="#cfcfcf")
        self.logo_frame1_root_login.place(relx=0.165, rely=0.40)


        #FRAME 2
        self.img_root_login = PhotoImage(file="icons/img_login.png")
        self.logo_frame2_root_login = Label(self.frame_2_root_login, image=self.img_root_login, bg="#0a448e")
        self.logo_frame2_root_login.place(relx=0.36, rely=0.07)


        #LABEL E ENTRY DO LOGIN
        self.lb_login_root_login = Label(self.frame_2_root_login, text="Login:", bg="#0a448e", font=("Verdana", 10, "bold"), fg="white")
        self.lb_login_root_login.place(relx=0.08, rely=0.43)

        self.login_entry_root_login = ttk.Entry(self.frame_2_root_login, font=("Verdana", 9))
        self.login_entry_root_login.place(relx=0.285, rely=0.43, relwidth=0.61, relheight=0.057)

        #LABEL E ENTRY DO PASSWORD
        self.lb_senha_root_login = Label(self.frame_2_root_login, text="Senha:", bg="#0a448e", font=("Verdana", 10, "bold"), fg="white")
        self.lb_senha_root_login.place(relx=0.08, rely=0.53)

        self.senha_entry_root_login = ttk.Entry(self.frame_2_root_login, font=("Verdana", 9), show="*")
        self.senha_entry_root_login.place(relx=0.285, rely=0.53, relwidth=0.61, relheight=0.057)

        # LABEL LOGIN/SENHA ERRADO
        self.lb_login_senha_incorreto_root_login = Label(self.frame_2_root_login, text="", bg="#0a448e",font=("Verdana", 8, "bold"), fg="red")
        self.lb_login_senha_incorreto_root_login.place(relx=0.23, rely=0.6)

        #BUTTON ENTRAR
        self.bt_entrar_root_login = Button(self.frame_2_root_login, text="Entrar", font=("arial", 9), bg="#cfcfcf", border=2, command=self.check_cadastro_existe)
        self.bt_entrar_root_login.place(relx=0.398, rely=0.68, relwidth=0.21, relheight=0.07)
        self.bt_entrar_root_login.bind("<Enter>", self.bt_entrar_root_login.config(cursor="hand2"))

        # LABEL NAO TEM CADASTRO?
        self.lb_cadstro_root_login = Label(self.frame_2_root_login, text="Cadastrar", bg="#0a448e", font=("Verdana", 9, "bold"), fg="white")
        self.lb_cadstro_root_login.place(relx=0.385, rely=0.84)
        self.lb_cadstro_root_login.bind("<Button-1>", self.open_root_cadastro)
        self.lb_cadstro_root_login.bind("<Enter>", self.lb_cadstro_root_login.config(cursor="hand2"))



Rootlogin()









