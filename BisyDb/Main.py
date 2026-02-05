import tkinter as tk
from tkinter import messagebox
import customtkinter as ctk


def enviar_dados():
    dados = {
        "BASE": entry_base.get(),
        "BISLOG": entry_log_bis.get(),
        "CLIENT": entry_client.get(),
        "LOGDATE": entry_log_date.get(),
        "LOGBOOK": entry_logbook.get(),
        "ENG OIL LH": entry_oil_lh.get(),
        "ENG OIL RH": entry_oil_rh.get(),
        "APU OIL": entry_oil_apu.get(),
        "TECHNICIAN": entry_log_AMT.get(),
        "REPORT": entry_report.get(),
        "ACTION": entry_action.get(),
        "IMAGE": entry_image.get(),
    }

    # Exibe os dados coletados
    mensagem = "\n".join(
        [f"{chave}: {valor}" for chave, valor in dados.items()])
    messagebox.showinfo("Dados enviados", mensagem)

    # Limpa os campos
    for entry in entradas:
        entry.delete(0, tk.END)


# Criando janela principal
janela = tk.Tk()
janela.title("BisyDb")
janela.geometry("1300x650")
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
label_base.place(x=10, y=175)
entry_base = tk.Entry(
    janela,
    bg="#B8B8B9",
    fg="black",
    font=("Arial", 12, "bold"),
    width=11,
)
entry_base.place(x=10, y=200,)

# bislog
label_log_bis = tk.Label(
    janela,
    bg="#000000",
    text="BISLOG",
    font=("Arial", 12, "bold"),
    width=10,
    fg="#D2CFCF",
)
label_log_bis.place(x=130, y=175)
entry_log_bis = tk.Entry(
    janela,
    bg="#B8B8B9",                  # cor de fundo
    fg="black",                         # cor do texto
    font=("Arial", 12, "bold"),                # fonte e tamanho
    width=11
)
entry_log_bis.place(x=130, y=200)

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
entry_client = tk.Entry(
    janela,
    bg="#B8B8B9",
    fg="black",
    font=("Arial", 12, "bold"),
    width=11
)
entry_client.place(x=250, y=200)

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
entry_logbook = tk.Entry(
    janela,
    bg="#B8B8B9",
    fg="black",
    font=("Arial", 12, "bold"),
    width=11
)
entry_logbook.place(x=370, y=200)

# date
label_log_date = tk.Label(
    janela,
    bg="#000000",
    text="DATE",
    font=("Arial", 12, "bold"),
    width=8,
    fg="#D2CFCF",
)
label_log_date.place(x=485, y=175)
entry_log_date = tk.Entry(
    janela,
    bg="#B8B8B9",
    fg="black",
    font=("Arial", 12, "bold"),
    width=8,
)
entry_log_date.place(x=490, y=200)

# oil_lh
label_oil_lh = tk.Label(
    janela,
    text="LH",
    bg="#000000",
    font=("Arial", 12, "bold"),
    width=5,
    fg="#D2CFCF",
)
label_oil_lh.place(x=580, y=175)
entry_oil_lh = tk.Entry(
    janela,
    bg="#B8B8B9",                  # cor de fundo
    fg="black",                         # cor do texto
    font=("Arial", 12, "bold"),                # fonte e tamanho
    width=5
)
entry_oil_lh.place(x=582, y=200)

# oil_rh
label_oil_rh = tk.Label(
    janela,
    text="RH",
    bg="#000000",
    font=("Arial", 12, "bold"),
    width=5,
    fg="#D2CFCF",
)
label_oil_rh.place(x=640, y=175)
entry_oil_rh = tk.Entry(
    janela,
    bg="#B8B8B9",                  # cor de fundo
    fg="black",                         # cor do texto
    font=("Arial", 12, "bold"),                # fonte e tamanho
    width=5
)
entry_oil_rh.place(x=645, y=200)

# oil_apu
label_oil_apu = tk.Label(
    janela,
    text="APU",
    bg="#000000",
    font=("Arial", 12, "bold"),
    width=5,
    fg="#D2CFCF",
)
label_oil_apu.place(x=705, y=175)
entry_oil_apu = tk.Entry(
    janela,
    bg="#B8B8B9",                  # cor de fundo
    fg="black",                         # cor do texto
    font=("Arial", 12, "bold"),                # fonte e tamanho
    width=5
)
entry_oil_apu.place(x=708, y=200)

# technician
label_log_AMT = tk.Label(
    janela,
    text="TECHNICIAN",
    bg="#000000",
    font=("Arial", 12, "bold"),
    width=10,
    fg="#D2CFCF",
)
label_log_AMT.place(x=768, y=175)
entry_log_AMT = tk.Entry(
    janela,
    bg="#B8B8B9",                  # cor de fundo
    fg="black",                         # cor do texto
    font=("Arial", 12, "bold"),                # fonte e tamanho
    width=11
)
entry_log_AMT.place(x=770, y=200)

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
entry_report = tk.Text(
    janela,
    bg="#B8B8B9",                  
    fg="black",                         
    font=("Arial", 12, "bold"),                
    width=82, height=5, borderwidth=4, 
)
entry_report.place(x=10, y=275)

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
entry_action = tk.Text(
    janela,
    bg="#B8B8B9",                  # cor de fundo
    fg="black",                         # cor do texto
    font=("Arial", 12, "bold"),                # fonte e tamanho
    width=82, height=5, borderwidth=4, 
)
entry_action.place(x=10, y=435)

# Image
label_image = tk.Label(
    janela,
    text="IMAGE",
    bg="#000000",
    font=("Arial", 12, "bold"),
    width=10,
    fg="#D2CFCF",
)
label_image.place(x=758, y=250)
entry_image = tk.Entry(
    janela,
    bg="#B8B8B9",                  # cor de fundo
    fg="black",                         # cor do texto
    font=("Arial", 12, "bold"),                # fonte e tamanho
    width=11
)
entry_image.place(x=770, y=275)

# Lista de entradas para facilitar limpeza
entradas = [entry_base, entry_log_bis, entry_client, entry_logbook, entry_log_date,
            entry_oil_lh, entry_oil_rh, entry_oil_apu, entry_report, entry_action, entry_image]


# Botão de envio
btn_enviar = tk.Button(
    janela,
    text="Enviar",
    width=20,
    command=enviar_dados
)
btn_enviar.place(x=10, y=615)


btn_enviar = tk.Button(
    janela,
    text="Exit",
    width=20,
    command=enviar_dados
)
btn_enviar.place(x=200, y=615)

# Executar janela
janela.mainloop()
