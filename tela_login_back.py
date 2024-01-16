import psycopg2

from tkinter import *


class FuncsTelaLogin():

    def conecta_bd_login(self):
        self.conectar = psycopg2.connect(database="login", user="postgres", password="123", host="localhost")
        self.cur = self.conectar.cursor()

    def check_cadastro_existe(self):
        self.root_login_front.destroy()
        from front__2_cadastro_aluno import Aplication

        # self.conecta_bd_login()
        #
        # login_entry = str(self.login_entry_root_login.get()).strip()
        # senha_entry = str(self.senha_entry_root_login.get()).strip()
        #
        # self.cur.execute(f"SELECT cpf_login FROM login")
        # resultado = self.cur.fetchall()
        #
        # lista_cpf = []
        # for cpf in resultado:
        #     lista_cpf.append(cpf[0])
        #
        # if login_entry in lista_cpf:
        #
        #     self.cur.execute(f"SELECT senha FROM login WHERE cpf_login = '{login_entry}'")
        #     senha = self.cur.fetchall()
        #
        #     if (senha[0][0] == senha_entry):
        #         self.conectar.close()
        #         self.root_login_front.destroy()
        #         from front__2_cadastro_aluno import Aplication
        #     else:
        #         self.lb_login_senha_incorreto_root_login.configure(text="Login ou Senha incorreto.", fg="red")
        #         self.conectar.close()
        #
        # else:
        #     self.lb_login_senha_incorreto_root_login.configure(text="Login ou Senha incorreto.", fg="red")
        #     self.conectar.close()

    def open_root_cadastro(self, event):
        self.root_login_front.destroy()
        from tela_cadastro_front import RootCadastro



