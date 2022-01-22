# pythonbank - Programa criado que simula um funcionamento de um Banco.
#
# Site:       http://luizguilherme.tech
# Autor:      Luiz Guilherme
# Manutenção: Luiz Guilherme
#
# ------------------------------------------------------------------------ #
#
# Histórico:
#
#   v1.0 04/01/2022, Luiz :
#       - Início do programa
# ------------------------------------------------------------------------ #
# Testado em:
# python 3.9  
# # ------------------------------- VARIÁVEIS E BIBLIOTECAS IMPORTADAS ----------------------------------------- #
import pandas as pd
from tkinter import *

df = pd.read_excel("/home/luiz/Documentos/Python/base.xlsx")


# ------------------------------------------------------------------------ #

# ------------------------------- TESTES ----------------------------------------- #

# ------------------------------------------------------------------------ #

# ------------------------------- FUNÇÕES ----------------------------------------- #

def abreconta():
    janela_abreconta = Tk()
    janela_abreconta.title("Abertura de conta")
    janela_abreconta.geometry("380x300")
    label_topo = Label(janela_abreconta, text="Preencha os campos abaixo para abrirmos sua conta.")
    label_topo.grid(column=0, row=1, padx=10, pady=5)

    label_cpf = Label(janela_abreconta,text="Digite seu CPF: ")
    label_cpf.grid(column=0, row=2)
    cpf = Entry(janela_abreconta, width=20)
    cpf.grid(row=3,column=0)

    label_nome = Label(janela_abreconta,text="Digite seu Nome Completo: ")
    label_nome.grid(column=0, row=4)
    nome = Entry(janela_abreconta, width=20)
    nome.grid(row=5,column=0)

    label_saldo = Label(janela_abreconta,text="Qual valor você quer depositar em sua conta ? ")
    label_saldo.grid(column=0, row=6)
    saldo = Entry(janela_abreconta, width=20)
    saldo.grid(row=7,column=0)


    def teste():
        c = cpf.get()
        n = nome.get()
        s = saldo.get()

        novo = [c, n, s]
        df.loc[len(df)] = novo
        df.to_excel("base.xlsx", index=False)

        label_confirma = Label(janela_abreconta, text= n + " sua conta foi criada, seu saldo é: " + s)
        label_confirma.grid(row=10, column=0)

    b = Button(janela_abreconta, text= "Criar Conta", bg="red", command=teste)
    b.grid(row=9, column=0)


def consulta ():
    janela_consulta = Tk()
    janela_consulta.title("Consulta de Saldo")
    janela_consulta.geometry("380x300")
    label_topo = Label(janela_consulta, text="Digite seu CPF para consultarmos seu saldo.")
    label_topo.grid(column=0, row=1, padx=40, pady=10)

    cpf_consulta = Entry(janela_consulta, width=20)
    cpf_consulta.grid(row=2,column=0)

    def cons ():
        c = int(cpf_consulta.get())

        s = str(df.loc[df["CPF"] == c]) 
        label_consulta = Label(janela_consulta, text= s)
        label_consulta.grid(row=4, column=0)

    b = Button(janela_consulta, text= "Ver meu Saldo.", bg="red", command=cons)
    b.grid(row=3, column=0)

    

def transfer ():
    janela_transfer = Tk()
    janela_transfer.title("Transferência entre Contas")
    janela_transfer.geometry("450x300")
    label_topo = Label(janela_transfer, text="Digite o CPF da sua conta.")
    label_topo.grid(column=0, row=1, padx=40, pady=10)

    cpf_envio = Entry(janela_transfer, width=20)
    cpf_envio.grid(row=2,column=0)

    label_cpf = Label(janela_transfer, text="Digite o CPF da conta que irá receber o valor transferido.")
    label_cpf.grid(column=0, row=3, padx=40, pady=10)

    cpf_recebe = Entry(janela_transfer, width=20)
    cpf_recebe.grid(row=4,column=0)

    label_saldo = Label(janela_transfer, text="Digite o valor a ser transferido.")
    label_saldo.grid(column=0, row=5, padx=40, pady=10)

    saldo = Entry(janela_transfer, width=20)
    saldo.grid(row=6,column=0)

    def tran ():
        e = int(cpf_envio.get())
        r = int(cpf_recebe.get())
        s = int(saldo.get())

        a = int(df.loc[df["CPF"] == e, "Saldo"]) 
        b = a - s
        df.loc[df["CPF"] == e, "Saldo"] = b

        c = int(df.loc[df["CPF"] == r, "Saldo"]) 
        d = c + s
        df.loc[df["CPF"] == r, "Saldo"] = d
     

        df.to_excel("base.xlsx", index=False)

        label_transferencia = Label(janela_transfer, text="Transferência realizada com Sucesso.")
        label_transferencia.grid(row=11, column=0)

    b = Button(janela_transfer, text= "Concluir Transferência.", bg="red", command=tran)
    b.grid(row=9, column=0)

def banco ():
    janela = Tk()
    janela.title("PythonBank")

    img = PhotoImage(file="/home/luiz/Documentos/Python/pythonbank.png")
    label_imagem = Label(image=img)
    label_imagem.grid(column=0, row=0, padx=10, pady=10 )

    botao = Button(janela, text="Abra sua conta!", bg="red", command=abreconta)
    botao.grid(column=0, row=1, padx=10, pady=10)

    botao = Button(janela, text="Consultar saldo.", bg="red", command=consulta)
    botao.grid(column=0, row=3, padx=10, pady=10)

    botao = Button(janela, text="Transferência.", bg="red", command=transfer)
    botao.grid(column=0, row=5, padx=10, pady=10)



    janela.mainloop()


banco()