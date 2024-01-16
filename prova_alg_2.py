from tkinter import *
import psycopg2


def cadastrar():
    conectar = psycopg2.connect(database="login", user="postgres", password="123", host="localhost")
    cur = conectar.cursor()
    cur.execute(f"INSERT INTO login (nome, email, senha) VALUES ('{entry_nome}', '{entry_email}', '{entry_senha}')")
    conectar.commit()
    cur.close()
    conectar.close()


root = Tk()

root.title("Cadastro")
root.geometry("400x400")
root.configure(bg="white")

frame = Frame(root, bg="blue")
frame.place(relx=0, rely=0, relwidth=1, relheight=1)

label_nome = Label(frame, text="Nome")
label_nome.place(relx=0.2, rely=0.2)
entry_nome = Entry(frame)
entry_nome.place(relx=0.4, rely=0.2)

label_email = Label(frame, text="E-mail")
label_email.place(relx=0.2, rely=0.3)
entry_email = Entry(frame)
entry_email.place(relx=0.4, rely=0.3)

label_senha = Label(frame, text="Senha")
label_senha.place(relx=0.2, rely=0.4)
entry_senha = Entry(frame)
entry_senha.place(relx=0.4, rely=0.4)

button_cadastro = Button(frame, text="Cadastrar")
button_cadastro.place(relx=0.4, rely=0.6, relwidth=0.2, relheight=0.08, command=cadastrar)

root.mainloop()




