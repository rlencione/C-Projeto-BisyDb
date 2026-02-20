
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import mysql.connector


def enviar_dados():
    dados = {
        "BASE": base.get(),
        "BISLOG": bis_log.get(),
        "CLIENT": client.get(),
        "FLIGHT": flight.get(),
        "ACFT": acft.get(),
        "LOGDATE": log_date.get(),
        "LOGBOOK": logbook.get(),
        "ENG OIL LH": oil_lh.get(),
        "ENG OIL RH": oil_rh.get(),
        "APU OIL": oil_apu.get(),
        "TECHNICIAN": log_AMT.get(),
        "REPORT": report.get("1.0", "end-1c"),
        "ACTION": action.get("1.0", "end-1c"),
    }

    try:

        conexao = mysql.connector.connect(
            host="localhost",       # endereço do servidor MySQL
            user="root",     # usuário do MySQL
            password="Bis092",   # senha do MySQL
            database="bisydb"    # nome do banco de dados
        )

        cursor = conexao.cursor(buffered=True)

        # Criando um cursor para executar comandos SQL

        comando = '''INSERT INTO bis_log_table (base, log_bis, client, flight, acft, log_date, logbook, oil_lh, oil_rh, oil_apu, log_AMT, entry_report, entry_action) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)'''

        # Exemplo de consulta
        cursor.execute(comando, tuple(dados.values()))
        # Edita o banco de dados
        conexao.commit()
        # Lê o banco de dadosentry_logbook
        # resultado = cursor.fetchone()
        print("Banco de dados conectado:")

        # Fechando cursor e conexão
        cursor.close()
        conexao.close()

    except mysql.connector.Error as erro:
        print("Erro ao conectar no MySQL:", {erro})

# Exibe os dados coletados

# Limpa os campos
    for entry in entradas:
        entry.delete("0", tk.END)

    for text in entradas_2:
        text.delete("1.0", tk.END)

# Criando janela principal

img = Image.open("C:\Projetos\BisyDb\image_bisy\logo.png")
img.save("logo.ico", format="ICO")


janela = tk.Tk()
janela.title("BisyDb")
janela.iconbitmap("logo.ico") #sizes=[(32,32), (64,64), (128,128)]))
janela.geometry("1360x720+0+0")
janela.resizable(False, False)
janela.config(bg="#435059")

frame_1 = tk.Frame(janela,
                   background="#1271b7",
                   width=1360,
                   height=70,
                   )
frame_1.grid(column=0, row=0, columnspan=15)

frame_2 = tk.Frame(janela,
                   background="#be0218",

                   width=1360,
                   height=3,
                   )
frame_2.grid(column=0, row=1, columnspan=15)


frame_3 = tk.Frame(janela,
                   background="#909298",
                   width=1360,
                   height=10,
                   )
frame_3.grid(column=0, row=2, columnspan=15)

frame_4 = tk.Frame(janela,
                   background="#435059",
                   width=1360,
                   height=30,
                   )
frame_4.grid(column=0, row=3, columnspan=15)
# Labels e Entradas

# Combo base
label_base = tk.Label(
    janela,
    bg="#435059",
    text="BASE",
    font=("Arial", 11, "bold"),
    width=9,
    fg="white",
)
label_base.grid(column=0, row=4)


def mostrar_base():
    print("Selecionado:", base.get())


bases = ["GRU", "GIG", "SJC"]
base = ttk.Combobox(
    janela,
    values=bases,
    font=("Arial", 12, "bold",),
    width=11,
)
base.grid(column=0, row=5, padx=10)
# base.current(0)
base.bind("<<ComboboxSelected>>", mostrar_base)

# bislog
label_bis_log = tk.Label(
    janela,
    bg="#435059",
    text="BISLOG",
    font=("Arial", 12, "bold"),
    width=9,
    fg="white",
)
label_bis_log.grid(column=1, row=4)
bis_log = tk.Entry(
    janela,
    bg="white",                  # cor de fundo
    fg="black",                         # cor do texto
    font=("Arial", 12, "bold"),                # fonte e tamanho
    width=11,
)

bis_log.grid(column=1, row=5, padx=10)

# Combo Client

label_client = tk.Label(
    janela,
    bg="#435059",
    text="CLIENT",
    font=("Arial", 12, "bold"),
    width=9,
    fg="white",
)
label_client.grid(column=2, row=4)


def mostrar_client():
    print("Selecionado:", client.get())


clients = ["AVIANCA", "AIR MAROC", "ARAJET", "SKY",]
client = ttk.Combobox(
    janela,
    values=clients,
    font=("Arial", 12, "bold",),
    width=11,
)
client.grid(column=2, row=5, padx=10)
# client.current(0)
client.bind("<<ComboboxSelected>>", mostrar_client)


# Flight NUmber
label_flight = tk.Label(
    janela,
    bg="#435059",
    text="FLIGHT",
    font=("Arial", 12, "bold"),
    width=9,
    fg="white",
)
label_flight.grid(column=3, row=4)
flight = tk.Entry(
    janela,
    bg="white",
    fg="black",
    font=("Arial", 12, "bold"),
    width=11
)
flight.grid(column=3, row=5, padx=10)

# Aircraft
label_acft = tk.Label(
    janela,
    bg="#435059",
    text="ACFT",
    font=("Arial", 12, "bold"),
    width=9,
    fg="white",
)
label_acft.grid(column=4, row=4)
acft = tk.Entry(
    janela,
    bg="white",
    fg="black",
    font=("Arial", 12, "bold"),
    width=11
)
acft.grid(column=4, row=5, padx=10)

# Logbook
label_logbook = tk.Label(
    janela,
    bg="#435059",
    text="LOGBOOK",
    font=("Arial", 12, "bold"),
    width=9,
    fg="white",
)
label_logbook.grid(column=5, row=4)
logbook = tk.Entry(
    janela,
    bg="white",
    fg="black",
    font=("Arial", 12, "bold"),
    width=11
)
logbook.grid(column=5, row=5, padx=10)

# date

# DateEntry(locale='pt_PT', date_pattern='MM/dd/yyyy')

label_log_date = tk.Label(
    janela,
    bg="#435059",
    text="DATE",
    font=("Arial", 12, "bold"),
    width=9,
    fg="white",
)
label_log_date.grid(column=6, row=4)
log_date = DateEntry(
    janela,
    date_pattern='dd/MM/yyyy',
    bg="white",
    fg="black",
    font=("Arial", 12, "bold"),
    width=11,
)
log_date.grid(column=6, row=5, padx=10)

# oil_lh
label_oil_lh = tk.Label(
    janela,
    text="LH",
    bg="#435059",
    font=("Arial", 12, "bold"),
    width=4,
    fg="white",
)
label_oil_lh.grid(column=7, row=4)
oil_lh = tk.Entry(
    janela,
    bg="white",                  # cor de fundo
    fg="black",                         # cor do texto
    font=("Arial", 12, "bold"),                # fonte e tamanho
    width=5
)
oil_lh.grid(column=7, row=5, padx=10)

# oil_rh
label_oil_rh = tk.Label(
    janela,
    text="RH",
    bg="#435059",
    font=("Arial", 12, "bold"),
    width=4,
    fg="white",
)
label_oil_rh.grid(column=8, row=4)
oil_rh = tk.Entry(
    janela,
    bg="white",                  # cor de fundo
    fg="black",                         # cor do texto
    font=("Arial", 12, "bold"),                # fonte e tamanho
    width=5
)
oil_rh.grid(column=8, row=5, padx=10)

# oil_apu
label_oil_apu = tk.Label(
    janela,
    text="APU",
    bg="#435059",
    font=("Arial", 12, "bold"),
    width=4,
    fg="white",
)
label_oil_apu.grid(column=9, row=4)
oil_apu = tk.Entry(
    janela,
    bg="white",                  # cor de fundo
    fg="black",                         # cor do texto
    font=("Arial", 12, "bold"),                # fonte e tamanho
    width=5
)
oil_apu.grid(column=9, row=5, padx=10)

# technician
label_log_AMT = tk.Label(
    janela,
    text="TECHNICIAN",
    bg="#435059",
    font=("Arial", 12, "bold"),
    width=9,
    fg="white",
)
label_log_AMT.grid(column=10, row=4)


def mostrar_log_AMT():
    print("Selecionado:", log_AMT.get())


log_AMTs = ["COELHO_014", "LENCIONE_092", "MARCELO_033",
            "MELO_076", "MAURICIO", "RICARDO_085", "SAMUEL"]
log_AMT = ttk.Combobox(
    janela,
    values=log_AMTs,
    font=("Arial", 10, "bold"),
    width=15,
)
log_AMT.grid(column=10, row=5, padx=10)
# base.current(0)
log_AMT.bind("<<ComboboxSelected>>", mostrar_log_AMT())

# Report
label_report = tk.Label(
    janela,
    text="REPORT",
    bg="#435059",
    font=("Arial", 12, "bold"),
    width=10,
    fg="white",
)
label_report.place(x=15, y=195)
report = tk.Text(
    janela,
    bg="white",
    fg="black",
    font=("Arial", 12, "bold"),
    height=5, width=70,
)
report.place(x=10, y=220)
# Action
label_action = tk.Label(
    janela,
    text="ACTION",
    bg="#435059",
    font=("Arial", 12, "bold"),
    width=10,
    fg="white",
)
label_action.place(x=15, y=355)
action = tk.Text(
    janela,
    bg="white",                  # cor de fundo
    fg="black",                         # cor do texto
    font=("Arial", 12, "bold"),                # fonte e tamanho
    height=5, width=70,
)
action.place(x=10, y=380,)

# Image
# label_image = tk.Label(
# janela,
# text = "IMAGE",
# bg = "#000000",
# font = ("Arial", 12, "bold"),
# width = 10,
# fg = "#D2CFCF",
# )
# label_image.place(x=758, y=250)
# entry_image = tk.Entry(
# janela,
# bg = "#B8B8B9",                  # cor de fundo
# fg = "black",                         # cor do texto
# font = ("Arial", 12, "bold"),                # fonte e tamanho

# )
# entry_image.place(x=770, y=275)

# Lista de entradas para facilitar limpeza
entradas = [base, bis_log, flight, acft, client, logbook, log_date,
            oil_lh, oil_rh, oil_apu, log_AMT]
entradas_2 = [report, action, log_AMT]  # image]

# Botão de envio
btn_enviar = tk.Button(
    janela,
    font=("Arial", 12, "bold"),
    text="Save",
    width=12,
    command=enviar_dados
)
btn_enviar.place(x=10, y=625)


btn_enviar = tk.Button(
    janela,
    font=("Arial", 12, "bold"),
    text="Exit",
    width=12,
    command=exit
)
btn_enviar.place(x=150, y=625)

# Executar janela
janela.mainloop()
