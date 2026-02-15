import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image, ImageTk


def enviar_dados():
    dados = {
        "BASE": base.get(),
        "BISLOG": bis_log.get(),
        "CLIENT": client.get(),
        "LOGDATE": log_date.get(),
        "LOGBOOK": logbook.get(),
        "ENG OIL LH": oil_lh.get(),
        "ENG OIL RH": oil_rh.get(),
        "APU OIL": oil_apu.get(),
        "TECHNICIAN": log_AMT.get(),
        "REPORT": report.get(),
        "ACTION": action.get(),
        # "IMAGE": entry_image.get(),
    }

    # Exibe os dados coletados
    mensagem = "\n".join(
        [f"{chave}: {valor}" for chave, valor in dados.items()])
    messagebox.showinfo("Dados enviados", mensagem)

    # Limpa os campos
    for entry in entradas:
        entry.delete("0", tk.END)


# Criando janela principal
janela = tk.Tk()
janela.title("BisyDb")
janela.geometry("1370x720+0+0")
janela.resizable(False, False)
janela.config(bg="#000000")

frame = tk.Frame(janela,
                 background="#C02026",
                 width=1400,
                 height=90,
                 )
frame.pack(pady=0, padx=0,)

frame = tk.Frame(janela,
                 background="#909298",
                 width=1400,
                 height=10,
                 )
frame.pack(pady=0, padx=0,)


# Labels e Entradas

# base
label_base = tk.Label(
    janela,
    bg="#000000",
    text="BASE",
    font=("Arial", 11, "bold"),
    width=10,
    fg="#D2CFCF",
)
label_base.place(x=8, y=175)
base = tk.Entry(
    janela,
    bg="#B8B8B9",
    fg="black",
    font=("Arial", 12, "bold"),
    width=11,
)
base.place(x=10, y=200,)

# bislog
label_bis_log = tk.Label(
    janela,
    bg="#000000",
    text="BISLOG",
    font=("Arial", 12, "bold"),
    width=10,
    fg="#D2CFCF",
)
label_bis_log.place(x=125, y=175)
bis_log = tk.Entry(
    janela,
    bg="#B8B8B9",                  # cor de fundo
    fg="black",                         # cor do texto
    font=("Arial", 12, "bold"),                # fonte e tamanho
    width=11
)
bis_log.place(x=130, y=200)

# Client
label_client = tk.Label(
    janela,
    bg="#000000",
    text="CLIENT",
    font=("Arial", 12, "bold"),
    width=10,
    fg="#D2CFCF",
)
label_client.place(x=243, y=175)
client = tk.Entry(
    janela,
    bg="#B8B8B9",
    fg="black",
    font=("Arial", 12, "bold"),
    width=11
)
client.place(x=250, y=200)

# Logbook
label_logbook = tk.Label(
    janela,
    bg="#000000",
    text="LOGBOOK",
    font=("Arial", 12, "bold"),
    width=8,
    fg="#D2CFCF",
)
label_logbook.place(x=378, y=175)
logbook = tk.Entry(
    janela,
    bg="#B8B8B9",
    fg="black",
    font=("Arial", 12, "bold"),
    width=11
)
logbook.place(x=370, y=200)

# date
label_log_date = tk.Label(
    janela,
    bg="#000000",
    text="DATE",
    font=("Arial", 12, "bold"),
    width=8,
    fg="#D2CFCF",
)
label_log_date.place(x=488, y=175)
log_date = tk.Entry(
    janela,
    bg="#B8B8B9",
    fg="black",
    font=("Arial", 12, "bold"),
    width=11,
)
log_date.place(x=485, y=200)

# oil_lh
label_oil_lh = tk.Label(
    janela,
    text="LH",
    bg="#000000",
    font=("Arial", 12, "bold"),
    width=5,
    fg="#D2CFCF",
)
label_oil_lh.place(x=598, y=175)
oil_lh = tk.Entry(
    janela,
    bg="#B8B8B9",                  # cor de fundo
    fg="black",                         # cor do texto
    font=("Arial", 12, "bold"),                # fonte e tamanho
    width=5
)
oil_lh.place(x=602, y=200)

# oil_rh
label_oil_rh = tk.Label(
    janela,
    text="RH",
    bg="#000000",
    font=("Arial", 12, "bold"),
    width=5,
    fg="#D2CFCF",
)
label_oil_rh.place(x=660, y=175)
oil_rh = tk.Entry(
    janela,
    bg="#B8B8B9",                  # cor de fundo
    fg="black",                         # cor do texto
    font=("Arial", 12, "bold"),                # fonte e tamanho
    width=5
)
oil_rh.place(x=665, y=200)

# oil_apu
label_oil_apu = tk.Label(
    janela,
    text="APU",
    bg="#000000",
    font=("Arial", 12, "bold"),
    width=5,
    fg="#D2CFCF",
)
label_oil_apu.place(x=725, y=175)
oil_apu = tk.Entry(
    janela,
    bg="#B8B8B9",                  # cor de fundo
    fg="black",                         # cor do texto
    font=("Arial", 12, "bold"),                # fonte e tamanho
    width=5
)
oil_apu.place(x=728, y=200)

# technician
label_log_AMT = tk.Label(
    janela,
    text="TECHNICIAN",
    bg="#000000",
    font=("Arial", 12, "bold"),
    width=10,
    fg="#D2CFCF",
)
label_log_AMT.place(x=788, y=175)
log_AMT = tk.Entry(
    janela,
    bg="#B8B8B9",                  # cor de fundo
    fg="black",                         # cor do texto
    font=("Arial", 12, "bold"),                # fonte e tamanho
    width=11
)
log_AMT.place(x=790, y=200)

# Report
label_report = tk.Label(
    janela,
    text="REPORT",
    bg="#000000",
    font=("Arial", 12, "bold"),
    width=10,
    fg="#D2CFCF",
)
label_report.place(x=10, y=250)
report = tk.Entry(
    janela,
    bg="#B8B8B9",
    fg="black",
    font=("Arial", 12, "bold"),
    width=82, borderwidth=4,
)
report.place(x=10, y=275)

# Action
label_action = tk.Label(
    janela,
    text="ACTION",
    bg="#000000",
    font=("Arial", 12, "bold"),
    width=10,
    fg="#D2CFCF",
)
label_action.place(x=10, y=410)
action = tk.Entry(
    janela,
    bg="#B8B8B9",                  # cor de fundo
    fg="black",                         # cor do texto
    font=("Arial", 12, "bold"),                # fonte e tamanho
    width=82, borderwidth=4,
)
action.place(x=10, y=435)

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
entradas = [base, bis_log, client, logbook, log_date,
            oil_lh, oil_rh, oil_apu, report, action,]  # image]

# Botão de envio
btn_enviar = tk.Button(
    janela,
    text="Save",
    width=20,
    command=enviar_dados
)
btn_enviar.place(x=10, y=615)


btn_enviar = tk.Button(
    janela,
    text="Exit",
    width=20,
    command=exit
)
btn_enviar.place(x=200, y=615)

# Executar janela
janela.mainloop()
