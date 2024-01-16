import psycopg2
from tkinter import *
from check_cpf import check_cpf_func
import tkinter as tk


class FuncsRootCadastro():
    def __init__(self):
        check_cpf_func()

    def get_date_entry(self):
        self.nome_cadastro = str(self.entry_nome_completo_root_cadastro.get().strip().title())
        self.cpf_cadastro = str(self.entry_cpf_root_cadastro.get()).strip()
        self.rg_cadastro = str(self.entry_rg_root_cadastro.get()).strip()
        self.email_cadastro = str(self.entry_email_root_cadastro.get()).strip()
        self.dt_nascimento_cadastro = str(self.entry_dt_nascimento_root_cadastro.get()).strip().title()
        self.senha1_cadastro = str(self.entry_senha_1_root_cadastro.get()).strip()
        self.senha2_cadastro = str(self.entry_senha_2_root_cadastro.get()).strip()

    def messages(self, msg_tipo, msg):
        root_msg_cadastro = Tk()
        root_msg_cadastro.title(msg_tipo)
        root_msg_cadastro.geometry("500x90")

        label = Label(root_msg_cadastro, text=msg)
        button = Button(root_msg_cadastro, text="OK", border=2, command=lambda: root_msg_cadastro.destroy())

        label.grid(column=0, row=0, pady=10, sticky="ew")
        button.grid(column=0, row=1)

        root_msg_cadastro.grid_columnconfigure(0, weight=1)

        root_msg_cadastro.mainloop()

    # def conecta_bd_cadastro(self):
    #     self.conectar = psycopg2.connect(database="login", user="postgres", password="123", host="localhost")
    #     self.cur = self.conectar.cursor()

    # def check_cpf_exists(self):
    #     self.conecta_bd_cadastro()
    #     self.cur.execute(f"SELECT cpf_login FROM login")
    #     resultado = self.cur.fetchall()
    #
    #     lista_cpf = []
    #     for cpf in resultado:
    #         lista_cpf.append(cpf[0])
    #     if self.cpf_cadastro in lista_cpf:
    #         return False
    #     else:
    #         return True
    #     self.conectar.close()

    def verificar_senhas_key_release(self, event):
        self.get_date_entry()
        if self.senha1_cadastro != self.senha2_cadastro:
            self.lb_result_senha_root_cadastro.configure(text="As senhas precisam ser iguais.", fg="red", font=("Verdana", 7, "bold"))
        else:
            self.lb_result_senha_root_cadastro.configure(text="")

    def check_cpf_cadastro(self, event):
        self.get_date_entry()

        if self.cpf_cadastro != "":
            texto, cor = check_cpf_func(self.cpf_cadastro)

            if cor == "confirmed":
                self.lb_cpf_check_root_cadastro.configure(text=texto, fg="green")
            else:
                self.lb_cpf_check_root_cadastro.configure(text=texto, fg="red")

    def add_dot_and_underline_root_cadastro_and_limit_entry_cpf(self, event,):
        self.cpf_cadastro = str(self.entry_cpf_root_cadastro.get()).strip()


        if len(self.cpf_cadastro) == 3:
            self.entry_cpf_root_cadastro.insert(3, ".")

        elif len(self.cpf_cadastro) == 7:
            self.entry_cpf_root_cadastro.insert(7, ".")

        elif len(self.cpf_cadastro) == 11:
            self.entry_cpf_root_cadastro.insert(11, "-")

        elif len(self.cpf_cadastro) > 14:
            self.entry_cpf_root_cadastro.delete(14, tk.END)

    def add_bar_and_limit_entry_date(self, event,):
        self.dt_nascimento_cadastro = str(self.entry_dt_nascimento_root_cadastro.get()).strip().title()

        if len(self.dt_nascimento_cadastro) == 2:
            self.entry_dt_nascimento_root_cadastro.insert(3, "/")

        elif len(self.dt_nascimento_cadastro) == 5:
            self.entry_dt_nascimento_root_cadastro.insert(7, "/")

        elif len(self.dt_nascimento_cadastro) > 10:
            self.entry_dt_nascimento_root_cadastro.delete(10, tk.END)


    def criar_cadastro(self):
        self.root_cadastro_front.destroy()
        from tela_login_front import Rootlogin

        # self.get_date_entry()
        #
        # check = self.check_cpf_exists()
        #
        # if check:
        #     #CHECK IF SENHA1 == SENHA2
        #     if self.nome_cadastro == "" or self.cpf_cadastro == "" or self.rg_cadastro == "" or self.email_cadastro == "" or self.dt_nascimento_cadastro == "" or self.senha1_cadastro == "" or self.senha2_cadastro == "":
        #         self.messages("Error", "Todos os campos precisam estar preenchidos.")
        #
        #     elif self.senha1_cadastro != self.senha2_cadastro:
        #         self.messages("Error", "As senhas precisam ser iguais.")
        #
        #     #IF SENHA1 == SENHA2
        #     else:
        #         print("senhas iguais")
        #         self.conecta_bd_cadastro()
        #
        #         self.cur.execute(f"INSERT INTO login (nome_completo, cpf_login, rg, email, data_nascimento, senha) VALUES ('{self.nome_cadastro}', '{self.cpf_cadastro}', '{self.rg_cadastro}', '{self.email_cadastro}', '{self.dt_nascimento_cadastro}', '{self.senha1_cadastro}')")
        #         self.conectar.commit()
        #         self.cur.close()
        #         self.conectar.close()
        #
        #         self.root_cadastro_front.destroy()
        #         from tela_login_front import Rootlogin
        # else:
        #     self.messages("Error", "O CPF informado já está cadastrado.")
