
from tkinter import *
from tkinter import ttk
from back_2_cadastro_aluno import Funcs
from tkcalendar import DateEntry

root = Tk()

class Aplication (Funcs):
    def __init__(self):
        self.root = root
        self.tela()
        self.frame_da_tela()
        self.widget_frame()
        self.select_lista()
        root.mainloop()

    def tela(self):
        self.root.title("Unichristus - Alunos")
        self.root.attributes('-zoomed', True)
        self.root.resizable(False, False)
        self.root.configure(bg="white")

    def frame_da_tela(self):
        self.frame_1 = Frame(self.root, bg="#cfcfcf")
        self.frame_1.place(relx = 0, rely = 0, relwidth=0.25, relheight=1)

        self.frame_2 = Frame(self.root, width=400, height=250, bg = "#cfcfcf")
        self.frame_2.place(relx = 0.253, rely = 0, relwidth=0.748, relheight=0.15)

        self.frame_3 = Frame(self.root, bg="#cfcfcf")
        self.frame_3.place(relx=0.253, rely=0.154, relwidth=0.748, relheight=0.35)

        self.frame_4 = Frame(self.root, bg="#cfcfcf")
        self.frame_4.place(relx=0.253, rely=0.51, relwidth=0.748, relheight=0.49)

    def widget_frame(self):
        #FRAME 1
        #LOGO
        self.logo_unichristus = PhotoImage(file="icons/logo_unichristus.png")
        self.logo_frame1 = Label(self.frame_1, image = self.logo_unichristus, bg ="#cfcfcf")
        self.logo_frame1.place(relx = 0.1, rely= 0.44)


        #FRAME 2
        #LABEL TITLE
        self.lb_title = Label(self.frame_2, text="Unichristus", font=("verdana", 13, "bold"), bg="#cfcfcf", fg="#0a448e")
        self.lb_title.place(relx = 0.4, rely= 0.09)

        #LABEL E ENTRY DO NOME
        self.lb_nome = Label(self.frame_2, text="Nome:", bg="#cfcfcf", font=("Verdana", 11, "bold"))
        self.lb_nome.place(relx=0.02, rely=0.4)

        self.nome_entry = ttk.Entry(self.frame_2, font=("Verdana", 9))
        self.nome_entry.place(relx=0.09, rely=0.4, relwidth=0.687, relheight=0.2)
        #self.nome_entry.bind("<KeyRelease>", self.key_release_search_nome)


        # LABEL E ENTRY DA MATRICULA
        self.lb_matricula = Label(self.frame_2, text="Matricula:", bg="#cfcfcf", font=("Verdana", 9))
        self.lb_matricula.place(relx=0.02, rely=0.7)

        self.matricula_entry = ttk.Entry(self.frame_2, font=("Verdana", 9))
        self.matricula_entry.place(relx=0.09, rely=0.7, relwidth=0.15, relheight=0.2)

        # BOTAO BUSCAR
        self.bt_buscar = Button(self.frame_2, text="Buscar", font=("verdana", 10, "bold"), bg="#cfcfcf", border=2)
        self.bt_buscar.place(relx=0.82, rely=0.3, relwidth=0.08, relheight=0.40)



        #FRAME 3 - COLUNA 1
        #LABEL E ENTRY DA E-MAIL
        self.lb_email = Label(self.frame_3, text="E-mail:", bg="#cfcfcf", font=("Verdana", 11))
        self.lb_email.place(relx=0.02, rely=0.1)

        self.email_entry = ttk.Entry(self.frame_3, font=("Verdana", 9))
        self.email_entry.place(relx=0.125, rely=0.1, relwidth=0.24, relheight=0.08)

        #LABEL E ENTRY DA DATA DE NASCIMENTO
        self.lb_dt_nascimento = Label(self.frame_3, text="Nascimento:", bg="#cfcfcf", font=("Verdana", 11))
        self.lb_dt_nascimento.place(relx=0.02, rely=0.23)

        #self.dt_nascimento_entry = ttk.Entry(self.frame_3, font=("Verdana", 9))
        self.dt_nascimento_entry = DateEntry(self.frame_3, width=12, background='#0a448e', foreground='white', borderwidth=3, font=("", 9))
        self.dt_nascimento_entry.set_date(None)
        self.dt_nascimento_entry.place(relx=0.125, rely=0.23, relwidth=0.24, relheight=0.08)
        #self.dt_nascimento_entry.bind("<KeyRelease>", self.add_bar_and_limit_entry_dt_nascimento)


        # LABEL E ENTRY DO RG
        self.lb_rg = Label(self.frame_3, text="RG:", bg="#cfcfcf", font=("Verdana", 11))
        self.lb_rg.place(relx=0.02, rely=0.36)

        self.rg_entry = ttk.Entry(self.frame_3, font=("Verdana", 9))
        self.rg_entry.place(relx=0.125, rely=0.36, relwidth=0.24, relheight=0.08)

        # LABEL, ENTRY E RESULTADO CHECK DO CPF
        self.lb_cpf = Label(self.frame_3, text="CPF:", bg="#cfcfcf", font=("Verdana", 11))
        self.lb_cpf.place(relx=0.02, rely=0.49)

        self.cpf_entry = ttk.Entry(self.frame_3, font=("Verdana", 9))
        self.cpf_entry.place(relx=0.125, rely=0.49, relwidth=0.24, relheight=0.08)
        # self.cpf_entry.bind("<FocusOut>", self.check_cpf)
        # self.cpf_entry.bind("<KeyRelease>", self.add_dot_and_underline_and_limit_entry_cpf)

        self.lb_resultado_cpf = Label(self.frame_3, text="", bg="#cfcfcf", font=("Verdana", 8, "italic"))
        self.lb_resultado_cpf.place(relx=0.125, rely=0.57)



        #FRAME3 - COLUNA 2
        # LABEL E ENTRY DO ESTADO DO ALUNO
        self.lb_estado_aluno = Label(self.frame_3, text="Estado do Aluno:", bg="#cfcfcf", font=("Verdana", 11))
        self.lb_estado_aluno.place(relx=0.4, rely=0.1)

        self.estado_aluno_entry = ttk.Combobox(self.frame_3, values=["Ativo", "Concludente", "Trancado"], font=("Verdana", 9))
        self.estado_aluno_entry.place(relx=0.535, rely=0.1, relwidth=0.24, relheight=0.08)

        # LABEL E ENTRY DO CURSO
        self.lb_curso = Label(self.frame_3, text="Curso:", bg="#cfcfcf", font=("Verdana", 11))
        self.lb_curso.place(relx=0.4, rely=0.23)

        self.curso_entry = ttk.Combobox(self.frame_3, values=["Administração", "Administração - EAD", "Análise e Desenvolvimento de Sistemas", "Arquitetura e Urbanismo", "Biomedicina", "Ciências Contábeis", "Ciências Contábeis - EAD", "Direito", "Enfermagem", "Engenharia Civil", "Engenharia de Produção", "Gastronomia", "Medicina", "Medicina Veterinária", "Nutrição", "Pedagogia", "Psicologia", "Odontologia"], font=("Verdana", 9))
        self.curso_entry.place(relx=0.535, rely=0.23, relwidth=0.24, relheight=0.08)

        # LABEL E ENTRY DA DATA DA MATRICULA
        self.lb_dt_matricula = Label(self.frame_3, text="Data Matricula:", bg="#cfcfcf", font=("Verdana", 11))
        self.lb_dt_matricula.place(relx=0.4, rely=0.36)

        self.dt_matricula_entry = DateEntry(self.frame_3, width=12, background='#0a448e', foreground='white', borderwidth=3, font=("", 9))
        self.dt_matricula_entry.place(relx=0.535, rely=0.36, relwidth=0.24, relheight=0.08)
        #self.dt_matricula_entry.bind("<KeyRelease>", self.add_bar_and_limit_entry_dt_matricula)


        # LABEL E ENTRY DO CONTRATO
        self.lb_contrato = Label(self.frame_3, text="Contrato:", bg="#cfcfcf", font=("Verdana", 11))
        self.lb_contrato.place(relx=0.4, rely=0.49)

        self.contrato_entry = ttk.Entry(self.frame_3, font=("Verdana", 9))
        self.contrato_entry.place(relx=0.535, rely=0.49, relwidth=0.24, relheight=0.08)


        #FRAME 3 - COLUNA 3
        self.imagem_aluno = PhotoImage(file="icons/perfil-sem-cara-da-mulher.png")
        self.imagem_aluno_frame3 = Label(self.frame_3, image=self.imagem_aluno, bg="white")
        self.imagem_aluno_frame3.place(relx=0.83, rely=0.104)

        self.captura_imagem = Button(self.frame_3, text="Tirar Foto", font=("arial", 9), bg="#cfcfcf", border=2)
        self.captura_imagem.place(relx=0.814, rely=0.54, relwidth=0.12, relheight=0.09)

        #FRAME 3 - ROW 2
        #BOTAO ADICIONAR
        self.bt_adicionar = Button(self.frame_3, text="Adicionar", font=("arial", 10,"bold"), border=2, bg="#0a448e", fg="white")
        self.bt_adicionar.place(relx=0.10, rely=0.77, relwidth=0.14, relheight=0.12)

        #BOTAO LIMPAR
        self.bt_limpar = Button(self.frame_3, text="Limpar", font=("arial", 10), bg = "#cfcfcf", border=2)
        self.bt_limpar.place(relx=0.32, rely=0.77, relwidth=0.14, relheight=0.12)

        # BOTAO EDITAR
        self.bt_editar = Button(self.frame_3, text="Editar", font=("arial", 10), bg="#cfcfcf", border=2)
        self.bt_editar.place(relx=0.54, rely=0.77, relwidth=0.14, relheight=0.12)

        #BOTAO APAGAR
        self.bt_limpar = Button(self.frame_3, text="Apagar", font=("arial", 10), bg = "#cfcfcf", border=2)
        self.bt_limpar.place(relx=0.76, rely=0.77, relwidth=0.14, relheight=0.12)


        #FRAME 4
        self.listaCli = ttk.Treeview(self.frame_4, height=3, columns=("col1", "col2", "col3", "col4", "col5"))

        self.listaCli.heading("#0", text="")
        self.listaCli.heading("#1", text="Nome")
        self.listaCli.heading("#2", text="Matricula")
        self.listaCli.heading("#3", text="CPF")
        self.listaCli.heading("#4", text="Data Nascimento")
        self.listaCli.heading("#5", text="E-mail")


        self.listaCli.column("#0", width=1)
        self.listaCli.column("#1", width=200)
        self.listaCli.column("#2", width=50)
        self.listaCli.column("#3", width=50)
        self.listaCli.column("#4", width=80)
        self.listaCli.column("#5", width=150)

        self.listaCli.place(relx=0.01, rely=0.05, relwidth=0.95, relheight=0.9)

        self.scroolLista = Scrollbar(self.frame_4, orient="vertical")
        #self.listaCli.configure(yscroll=self.scroolLista.set)
        self.scroolLista.place(relx=0.96, rely=0.05, relwidth=0.025, relheight=0.9)
        #self.listaCli.bind("<Double-1>", self.OnDoubleClick)

Aplication()