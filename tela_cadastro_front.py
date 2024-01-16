from tkinter import *
from tkinter import ttk
from tela_cadastro_back import FuncsRootCadastro


root_cadastro_front = Tk()


class RootCadastro(FuncsRootCadastro):
    def __init__(self):
        self.root_cadastro_front = root_cadastro_front
        self.root_cadastro()
        self.frame_da_root_cadastro()
        self.widget_frame_root_cadastro()
        root_cadastro_front.mainloop()

    def root_cadastro(self):
        self.root_cadastro_front.title("Unichristus - Cadastro")

        # iniciar tela ao centro:
        screen_width = self.root_cadastro_front.winfo_screenwidth()
        screen_height = self.root_cadastro_front.winfo_screenheight()
        x = (screen_width // 2) - (450 // 2)
        y = (screen_height // 2) - (500 // 2)
        self.root_cadastro_front.geometry(f"{450}x{500}+{x}+{y}")

        self.root_cadastro_front.resizable(False, False)
        self.root_cadastro_front.configure(bg="white")

    def frame_da_root_cadastro(self):
        self.frame_1_root_cadastro = Frame(self.root_cadastro_front, bg="#cfcfcf")
        self.frame_1_root_cadastro.place(relx=0, rely=0, relwidth=1, relheight=0.13)

        self.frame_2_root_cadastro = Frame(self.root_cadastro_front, bg="#0a448e")
        self.frame_2_root_cadastro.place(relx=0.0, rely=0.133, relwidth=1, relheight=.867)

    def widget_frame_root_cadastro(self):
        #FRAME1
        self.img_root_cadastro_logo = PhotoImage(file="icons/logo_unichristus_pequena.png")
        self.logo_frame1_cadastro_login = Label(self.frame_1_root_cadastro, image=self.img_root_cadastro_logo, bg="#cfcfcf")
        self.logo_frame1_cadastro_login.place(relx=0.3, rely=0.10)

        #FRAME 2
        #LABEL TITLE
        self.lb_title_root_cadastro = Label(self.frame_2_root_cadastro, text="CADASTRO", bg="#0a448e", font=("Verdana", 10, "bold"), fg="white")
        self.lb_title_root_cadastro.place(relx=0.4, rely=0.02)

        #LABEL E ENTRY NOME COMPLETO
        self.lb_nome_completo_root_cadastro = Label(self.frame_2_root_cadastro, text="Nome Completo", bg="#0a448e", font=("Verdana", 9, "bold"), fg="white")
        self.lb_nome_completo_root_cadastro.place(relx=0.0955, rely=0.1)

        self.entry_nome_completo_root_cadastro = ttk.Entry(self.frame_2_root_cadastro, font=("Verdana", 9))
        self.entry_nome_completo_root_cadastro.place(relx=0.1, rely=0.15, relwidth=0.8, relheight=0.05)

        #LABEL E ENTRY CPF
        self.lb_cpf_root_cadastro = Label(self.frame_2_root_cadastro, text="CPF", bg="#0a448e", font=("Verdana", 9, "bold"), fg="white")
        self.lb_cpf_root_cadastro.place(relx=0.0955, rely=0.25)

        self.entry_cpf_root_cadastro = ttk.Entry(self.frame_2_root_cadastro, font=("Verdana", 9))
        self.entry_cpf_root_cadastro.place(relx=0.1, rely=0.3, relwidth=0.33, relheight=0.05)
        self.entry_cpf_root_cadastro.bind("<FocusOut>", self.check_cpf_cadastro)
        self.entry_cpf_root_cadastro.bind("<KeyRelease>", self.add_dot_and_underline_root_cadastro_and_limit_entry_cpf)


        # LABEL IF CPF CHECK
        self.lb_cpf_check_root_cadastro = Label(self.frame_2_root_cadastro, text="", bg="#0a448e", font=("Verdana", 7, "bold"))
        self.lb_cpf_check_root_cadastro.place(relx=0.0955, rely=0.35)


        #LABEL E ENTRY RG
        self.lb_rg_root_cadastro = Label(self.frame_2_root_cadastro, text="RG", bg="#0a448e", font=("Verdana", 9, "bold"), fg="white")
        self.lb_rg_root_cadastro.place(relx=0.5655, rely=0.25)

        self.entry_rg_root_cadastro = ttk.Entry(self.frame_2_root_cadastro, font=("Verdana", 9))
        self.entry_rg_root_cadastro.place(relx=0.57, rely=0.3, relwidth=0.33, relheight=0.05)

        #LABEL E ENTRY DO E-MAIL
        self.lb_email_root_cadastro = Label(self.frame_2_root_cadastro, text="E-mail", bg="#0a448e", font=("Verdana", 9, "bold"), fg="white")
        self.lb_email_root_cadastro.place(relx=0.0955, rely=0.4)

        self.entry_email_root_cadastro = ttk.Entry(self.frame_2_root_cadastro, font=("Verdana", 9))
        self.entry_email_root_cadastro.place(relx=0.1, rely=0.45, relwidth=0.43, relheight=0.05)

        #LABEL E ENTRY DA DATA NASCIMENTO
        self.lb_dt_nacimento_root_cadastro = Label(self.frame_2_root_cadastro, text="Data Nascimento", bg="#0a448e", font=("Verdana", 9, "bold"), fg="white")
        self.lb_dt_nacimento_root_cadastro.place(relx=0.635, rely=0.4)

        self.entry_dt_nascimento_root_cadastro = ttk.Entry(self.frame_2_root_cadastro, font=("Verdana", 9))
        self.entry_dt_nascimento_root_cadastro.place(relx=0.6395, rely=0.45, relwidth=0.26, relheight=0.05)
        self.entry_dt_nascimento_root_cadastro.bind("<KeyRelease>", self.add_bar_and_limit_entry_date)


        #LABEL E ENTRY DA SENHA 1
        self.lb_senha_1_root_cadastro = Label(self.frame_2_root_cadastro, text="Senha", bg="#0a448e", font=("Verdana", 9, "bold"), fg="white")
        self.lb_senha_1_root_cadastro.place(relx=0.1, rely=0.55)

        self.entry_senha_1_root_cadastro = ttk.Entry(self.frame_2_root_cadastro, font=("Verdana", 9), show="*")
        self.entry_senha_1_root_cadastro.place(relx=0.1, rely=0.6, relwidth=0.8, relheight=0.05)

        # LABEL E ENTRY DA SENHA 2
        self.lb_senha_2_root_cadastro = Label(self.frame_2_root_cadastro, text="Confirme a Senha", bg="#0a448e",font=("Verdana", 9, "bold"), fg="white")
        self.lb_senha_2_root_cadastro.place(relx=0.1, rely=0.7)

        self.entry_senha_2_root_cadastro = ttk.Entry(self.frame_2_root_cadastro, font=("Verdana", 9), show="*")
        self.entry_senha_2_root_cadastro.place(relx=0.1, rely=0.75, relwidth=0.8, relheight=0.05)
        self.entry_senha_2_root_cadastro.bind("<KeyRelease>", self.verificar_senhas_key_release)

        # LABEL IF SENHA1 == SENHA2
        self.lb_result_senha_root_cadastro = Label(self.frame_2_root_cadastro, text="", bg="#0a448e")
        self.lb_result_senha_root_cadastro.place(relx=0.1, rely=0.8)

        #BUTTON CADASTRAR
        self.bt_cadastrar_root_cadastro = Button(self.frame_2_root_cadastro, text="CADASTRAR", font=("arial", 10, "bold"), bg="#cfcfcf", border=1, fg="#0a448e", command = self.criar_cadastro)
        self.bt_cadastrar_root_cadastro.place(relx=0.35, rely=0.86, relwidth=0.3, relheight=0.05)
        self.bt_cadastrar_root_cadastro.bind("<Enter>", self.bt_cadastrar_root_cadastro.config(cursor="hand2"))



RootCadastro()