
from tkinter import *
import tkinter as tk
import psycopg2
from check_cpf import check_cpf_func

class Funcs():

    def __init__(self):
        check_cpf_func()

    # def conecta_bd(self):
    #     self.conectar = psycopg2.connect(database="postgres", user="postgres", password="123", host="localhost")
    #     self.cur = self.conectar.cursor()
    #
    # def desconecta_bd(self):
    #     self.conectar.close()

    # def pegar_dados_entry(self):
    #     self.nome = str(self.nome_entry.get().strip().title())
    #     self.matricula = str(self.matricula_entry.get()).strip()
    #     self.email = str(self.email_entry.get()).strip()
    #     self.dt_nascimento = str(self.dt_nascimento_entry.get()).strip().title()
    #     self.rg = str(self.rg_entry.get()).strip()
    #     self.cpf = str(self.cpf_entry.get()).strip()
    #     self.estado_aluno = str(self.estado_aluno_entry.get())
    #     self.curso = str(self.curso_entry.get())
    #     self.dt_matricula = str(self.dt_matricula_entry.get()).strip().title()
    #     self.contrato = str(self.contrato_entry.get()).strip()

    # def limpa_tela(self):
    #     self.nome_entry.delete(0, END)
    #     self.matricula_entry.delete(0, END)
    #     self.email_entry.delete(0, END)
    #     self.dt_nascimento_entry.delete(0, END)
    #     self.rg_entry.delete(0, END)
    #     self.cpf_entry.delete(0, END)
    #     self.estado_aluno_entry.delete(0, END)
    #     self.curso_entry.delete(0, END)
    #     self.dt_matricula_entry.delete(0, END)
    #     self.contrato_entry.delete(0, END)
    #
    #     self.lb_resultado_cpf.configure(text="")
    #
    #     self.select_lista()
    #
    # def adiciona_aluno(self):
    #
    #     self.pegar_dados_entry()
    #
    #     if self.nome == "" or self.cpf == "":
    #         self.messages(f'Error"', f'Preencha o campo "Nome" e "CPF" para adicionar um aluno(a)!')
    #     else:
    #         self.conecta_bd()
    #
    #         self.cur.execute(f"INSERT INTO aluno (nome, matricula, email, data_nascimento, rg, cpf, estado_aluno, curso, data_matricula, contrato) VALUES ('{self.nome}', '{self.matricula}', '{self.email}', '{self.dt_nascimento}', '{self.rg}', '{self.cpf}', '{self.estado_aluno}', '{self.curso}', '{self.dt_matricula}', '{self.contrato}')")
    #
    #         self.conectar.commit()
    #         self.cur.close()
    #         self.conectar.close()
    #         self.limpa_tela()
    #         self.select_lista()
    #         self.messages(f'Confirmação', f'Cadastro realizado com sucesso!')
    #
    # def edita_aluno(self):
    #     self.pegar_dados_entry()
    #
    #     if self.cpf == "":
    #         self.messages(f'Error"', f'Preencha o campo "CPF" para alterar um aluno(a)!')
    #
    #     self.conecta_bd()
    #
    #     self.cur.execute(f"UPDATE aluno SET nome = '{self.nome}', matricula = '{self.matricula}', email = '{self.email}', data_nascimento = '{self.dt_nascimento}', rg = '{self.rg}', cpf = '{self.cpf}', estado_aluno = '{self.estado_aluno}', curso = '{self.curso}', data_matricula = '{self.dt_matricula}', contrato = '{self.contrato}' WHERE cpf = '{self.cpf}'")
    #     self.conectar.commit()
    #     self.cur.close()
    #     self.conectar.close()
    #     self.limpa_tela()
    #     self.select_lista()
    #     self.messages(f'Confirmação', f'Alteração realizada com sucesso!')
    #
    # def select_lista(self):
    #
    #
    #     self.listaCli.delete(*self.listaCli.get_children())
    #     self.conecta_bd()
    #     self.cur.execute("""SELECT nome, matricula, cpf, data_nascimento, email FROM aluno""")
    #     lista = self.cur.fetchall()
    #
    #     for i in lista:
    #         self.listaCli.insert("", END, values=i)
    #     self.desconecta_bd()
    #
    # def remove_aluno(self):
    #     self.conecta_bd()
    #
    #     self.pegar_dados_entry()
    #
    #     if self.cpf == "":
    #         self.messages(f'Error"', f'Preencha o campo "CPF" para remover o aluno(a)!')
    #         self.cur.close()
    #         self.conectar.close()
    #         return
    #
    #     self.cur.execute(f"SELECT cpf FROM aluno")
    #     lista = self.cur.fetchall()
    #     lista_cpf = []
    #     for i in lista:
    #         lista_cpf.append((i[0]))
    #     if self.cpf not in lista_cpf:
    #         self.messages(f'Error"', f'CPF não encontrado!')
    #         return
    #
    #
    #     self.cur.execute(f"DELETE FROM aluno WHERE cpf = '{self.cpf}'")
    #
    #     self.conectar.commit()
    #     self.cur.close()
    #     self.conectar.close()
    #     self.select_lista()
    #     self.limpa_tela()
    #     self.messages(f'Confirmação', "Aluno(a) apagado(a) com sucesso!")
    #
    # def buscar_aluno(self):
    #     self.pegar_dados_entry()
    #     if self.nome =="" and self.matricula == "" and self.curso=="":
    #         self.messages(f'Error"', f'O campo "Nome", "Matricula" ou "Curso" precisam estar preenchidos!')
    #     else:
    #         if self.nome != "":
    #             self.listaCli.delete(*self.listaCli.get_children())
    #             self.conecta_bd()
    #             self.cur.execute(f"SELECT nome, matricula, cpf, data_nascimento, email FROM aluno WHERE nome LIKE '%{self.nome}%'")
    #             resultado = self.cur.fetchall()
    #
    #             for i in resultado:
    #                 self.listaCli.insert("", END, values=i)
    #             self.desconecta_bd()
    #
    #         elif self.nome =="" and self.curso=="":
    #             self.listaCli.delete(*self.listaCli.get_children())
    #             self.conecta_bd()
    #             self.cur.execute(f"SELECT nome, matricula, cpf, data_nascimento, email FROM aluno WHERE matricula = '{self.matricula}'")
    #             resultado = self.cur.fetchall()
    #
    #             for i in resultado:
    #                 self.listaCli.insert("", END, values=i)
    #             self.desconecta_bd()
    #
    #         elif self.nome == "" and self.matricula=="":
    #             self.listaCli.delete(*self.listaCli.get_children())
    #             print(self.curso)
    #             self.conecta_bd()
    #             self.cur.execute(f"SELECT nome, matricula, cpf, data_nascimento, email FROM aluno WHERE curso = '{self.curso}'")
    #             resultado = self.cur.fetchall()
    #
    #             for i in resultado:
    #                 self.listaCli.insert("", END, values=i)
    #             self.desconecta_bd()
    #
    # def OnDoubleClick(self, event):
    #     self.nome_entry.delete(0, END)
    #     self.matricula_entry.delete(0, END)
    #     self.email_entry.delete(0, END)
    #     self.dt_nascimento_entry.delete(0, END)
    #     self.rg_entry.delete(0, END)
    #     self.cpf_entry.delete(0, END)
    #     self.estado_aluno_entry.delete(0, END)
    #     self.curso_entry.delete(0, END)
    #     self.dt_matricula_entry.delete(0, END)
    #     self.contrato_entry.delete(0, END)
    #
    #     item_selecionado = self.listaCli.selection()[0]
    #     col_mat = self.listaCli.item(item_selecionado, "values")
    #
    #     #CASO PRECISASSE PEGAR TODOS OS ITEMS DO TREEVIEW, PODERIA FAZER UM LOOP:
    #     # for n in self.listaCli.selection():
    #     #     col1, col2, col3, col4, col5 = self.listaCli.item(n, 'values')
    #
    #     self.conecta_bd()
    #     self.cur.execute(f"SELECT * FROM aluno WHERE cpf = '{col_mat[2]}'")
    #     resultado = self.cur.fetchall()
    #
    #     self.nome_entry.insert(END, resultado[0][0])
    #     self.matricula_entry.insert(END, resultado[0][1])
    #     self.email_entry.insert(END, resultado[0][2])
    #     self.dt_nascimento_entry.insert(END, resultado[0][3])
    #     self.rg_entry.insert(END, resultado[0][4])
    #     self.cpf_entry.insert(END, resultado[0][5])
    #     self.estado_aluno_entry.insert(END, resultado[0][6])
    #     self.curso_entry.insert(END, resultado[0][7])
    #     self.dt_matricula_entry.insert(END, resultado[0][8])
    #     self.contrato_entry.insert(END, resultado[0][9])
    #
    #     self.lb_resultado_cpf.configure(text="")
    #
    #     #self.nome_entry_editar = resultado[0][0]
    #
    #     self.desconecta_bd()
    #
    # def messages(self, msg_tipo, msg):
    #     root_msg = Tk()
    #     root_msg.title(msg_tipo)
    #     root_msg.geometry("500x90")
    #
    #     label = Label(root_msg, text=msg)
    #     button = Button(root_msg, text="OK", border=2, command=lambda: root_msg.destroy())
    #
    #     label.grid(column=0, row=0, pady=10, sticky="ew")
    #     button.grid(column=0, row=1)
    #
    #     root_msg.grid_columnconfigure(0, weight=1)
    #
    #     root_msg.mainloop()
    #
    # def check_cpf(self, event):
    #     self.pegar_dados_entry()
    #
    #     if self.cpf != "":
    #         texto, cor = check_cpf_func(self.cpf)
    #
    #         if cor == "confirmed":
    #             self.lb_resultado_cpf.configure(text=texto, fg="green")
    #         else:
    #             self.lb_resultado_cpf.configure(text=texto, fg="red")
    #
    # def key_release_search_nome(self, event):
    #     nome = str(self.nome_entry.get().strip().title())
    #     if len(nome) > 2:
    #         self.buscar_aluno()
    #     elif len(nome) ==0:
    #         self.limpa_tela()
    #
    # def add_dot_and_underline_and_limit_entry_cpf(self, event):
    #     self.cpf = str(self.cpf_entry.get()).strip()
    #
    #     if len(self.cpf) == 3:
    #         self.cpf_entry.insert(3, ".")
    #
    #     elif len(self.cpf) == 7:
    #         self.cpf_entry.insert(7, ".")
    #
    #     elif len(self.cpf) == 11:
    #         self.cpf_entry.insert(11, "-")
    #
    #     elif len(self.cpf) > 14:
    #         self.cpf_entry.delete(14, tk.END)
    #
    # def add_bar_and_limit_entry_dt_nascimento(self, event):
    #     self.dt_nascimento = str(self.dt_nascimento_entry.get()).strip().title()
    #
    #     if len(self.dt_nascimento) == 2:
    #         self.dt_nascimento_entry.insert(3, "/")
    #
    #     elif len(self.dt_nascimento) == 5:
    #         self.dt_nascimento_entry.insert(7, "/")
    #
    #     elif len(self.dt_nascimento) > 10:
    #         self.dt_nascimento_entry.delete(10, tk.END)
    #
    # def add_bar_and_limit_entry_dt_matricula(self, event):
    #     self.dt_matricula = str(self.dt_matricula_entry.get()).strip().title()
    #
    #     if len(self.dt_matricula) == 2:
    #         self.dt_matricula_entry.insert(3, "/")
    #
    #     elif len(self.dt_matricula) == 5:
    #         self.dt_matricula_entry.insert(7, "/")
    #
    #     elif len(self.dt_matricula) > 10:
    #         self.dt_matricula_entry.delete(10, tk.END)


