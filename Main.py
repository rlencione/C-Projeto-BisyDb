
import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
import customtkinter as ctk
from PIL import Image, ImageTk
from tkcalendar import DateEntry
import mysql.connector


def enviar_dados():

    empth_dados = {
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
    }

    empth_dados = [nome for nome, valor in empth_dados.items() if not valor.strip()]

    if empth_dados:
        mensagem = "ENTRY MISSING:\n" + \
            ", ".join(empth_dados)
        messagebox.showwarning("WARNING", mensagem)
        return

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
        "":item_mel.get(),
        "":ata_mel.get(),
        "":cat_mel.get(),
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

def clear_all():
    for clear in entradas_3:
        clear.delete("0", tk.END)

    for clear_text in entradas_4:
        clear_text.delete("1.0", tk.END)
        
# Criando janela principal

img = Image.open(r'C:\Projetos\BisyDb\image_bisy\logo.png')
img.save("logo.ico", format="ICO")


janela = tk.Tk()
janela.title("BisyDb")
janela.iconbitmap("logo.ico")
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

frame_7 = tk.Frame(janela,
                   background="#435059",
                   width=1360,
                   height=30,
                   )
frame_7.grid(column=0, row=7, columnspan=15)

frame_10 = tk.Frame(janela,
                    background="#435059",
                    width=1360,
                    height=30,
                    )
frame_10.grid(column=0, row=10, columnspan=15)

frame_11 = tk.Frame(janela,
                    background="#435059",
                    width=1360,
                    height=100,
                    )
frame_11.grid(column=0, row=14, columnspan=15)

# Labels e Entradas
# Combo base
label_base = tk.Label(
    janela,
    bg="#435059",
    text="BASE",
    font=("Arial", 12, "bold"),
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
base.bind("<<ComboboxSelected>>", mostrar_base)
base.grid(column=0, row=5)

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
    width=13,
)
bis_log.grid(column=1, row=5)

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
client.bind("<<ComboboxSelected>>", mostrar_client)
client.grid(column=2, row=5)

# Combo Flight NUmber
label_flight = tk.Label(
    janela,
    bg="#435059",
    text="FLIGHT",
    font=("Arial", 12, "bold"),
    width=9,
    fg="white",
)
label_flight.grid(column=3, row=4)

def mostrar_flight():
    print("Selecionado:", flight.get())
flights_avianca = ["AV86", "AV184", "AV249", "AV161",]
flight = ttk.Combobox(
    janela,
    values=flights_avianca,
    font=("Arial", 12, "bold",),
    width=11,
)
# client.current(0)
flight.bind("<<ComboboxSelected>>", mostrar_flight)
flight.grid(column=3, row=5)

# Combo Aircraft
label_acft = tk.Label(
    janela,
    bg="#435059",
    text="ACFT",
    font=("Arial", 12, "bold"),
    width=9,
    fg="white",
)
label_acft.grid(column=4, row=4)

def mostrar_acft():
    print("Selecionado:", acft.get())
acfts_avianca = ["A320 NEO", "HC-CRU", "HC-CJV", "HC-CJW", "HC-CSF", "HC-CTX", "HK-5273", "HK-5318", "HK-5319", "HK-5320", "HK-5335", "HK-5352",
                 "HK-5353", "HK-5360", "HK-5361", "HK-5365", "HK-5366", "HK-5367", "HK-5368", "HK-5378", "HK-5388", "HK-5389", "HK-5390", "HK-5393", "HK-5395",
                 "HK-5406", "HK-5407", "HK-5408", "HK-5409", "HK-5410", "HK-5421", "HK-5422", "HK-5423", "HK-5424", "HK-5425", "N195AV", "N206FR", "N207FR",
                 "N230AC", "N253AC", 'N281AV', "N284AV", "N345AV", "N398AV", "N401AV", "N411AE", "N411AV", "N416AV", "N422AV", "N426AV", "N430AV", "N446AV",
                 "N451AV", "N454AV", "N477AV", "N481AV", "N519AV", "N536AV", "N538AV", "N557AV", "N562AV", "N567AV", "N599AV", "N632AV", "N647AV", "N664AV",
                 "N686TA", "N688TA", "N689TA", "N691AV", "N723AV", "N724AV", "N726AV", "N728AV", "N740AV", "N741AV", "N742AV", "N743AV", "N745AV", "N748AV",
                 "N750AV", "N755AV", "N762AV", "N763AV", "N764AV", "N765AV", "N766AV", "N769AV", "N775AV", "N776AV", "N779AV", "N788AV", "N818AV", "N821AV",
                 "N862AV", "N901AV", "N902AV", "N903AV", "N904AV", "N905AV", "N906AV", "N908AV", "N909AV", "N919AV", "N920AV", "N920CG", "N930AV", "N931AV",
                 "N932AV", "N934AG", "N937AV", "N938AV", "N939AV", "N940AV", "N942AV", "N943AV", "N944AV", "N945AV", "N946AV", "N948AV", "N950AV", "N951AV",
                 "N954AV", "N955AV", "N956AV", "N957AV", "N958AV", "N959AV", "N960AV", "N961AV", "N962AV", "N963AV", "N964AV", "N965AV", "N966AV", "N967AV",
                 "N980AV", "N992AV", "PR-AVC", "B787/800"
                 ]
acft = ttk.Combobox(
    janela,
    values=acfts_avianca,
    font=("Arial", 12, "bold",),
    width=11,
)
acft.bind("<<ComboboxSelected>>", mostrar_acft)
acft.grid(column=4, row=5)
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
    width=13
)
logbook.grid(column=5, row=5)

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
log_date.grid(column=6, row=5)

# Combo oil_lh
label_oil_lh = tk.Label(
    janela,
    text="LH",
    bg="#435059",
    font=("Arial", 12, "bold"),
    width=3,
    fg="white",
)
label_oil_lh.grid(column=7, row=4)

def mostrar_oil_lh():
    print("Selecionado:", oil_lh.get())
oil_lhs = (0, 1, 2, 3, 4, 5, 6)
oil_lh = ttk.Combobox(
    janela,
    values=oil_lhs,
    font=("Arial", 12, "bold",),
    width=3,
)
client.bind("<<ComboboxSelected>>", mostrar_oil_lh)
oil_lh.grid(column=7, row=5)

# Combo oil_rh
label_oil_rh = tk.Label(
    janela,
    text="RH",
    bg="#435059",
    font=("Arial", 12, "bold"),
    width=3,
    fg="white",
)
label_oil_rh.grid(column=8, row=4)

def mostrar_oil_rh():
    print("Selecionado:", oil_rh.get())
oil_rhs = (0, 1, 2, 3, 4, 5, 6)
oil_rh = ttk.Combobox(
    janela,
    values=oil_rhs,
    font=("Arial", 12, "bold",),
    width=3,
)
oil_rh.bind("<<ComboboxSelected>>", mostrar_oil_rh)
oil_rh.grid(column=8, row=5)

# Comob oil_apu
label_oil_apu = tk.Label(
    janela,
    text="APU",
    bg="#435059",
    font=("Arial", 12, "bold"),
    width=3,
    fg="white",
)
label_oil_apu.grid(column=9, row=4)

def mostrar_oil_apu():
    print("Selecionado:", oil_apu.get())


oil_apus = (0, 1, 2, 3, 4, 5, 6)
oil_apu = ttk.Combobox(
    janela,
    values=oil_apus,
    font=("Arial", 12, "bold",),
    width=3
)
oil_apu.bind("<<ComboboxSelected>>", mostrar_oil_apu)
oil_apu.grid(column=9, row=5)

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
            "MELO_076", "MAURICIO_006", "RICARDO_085", "SAMUEL"]
log_AMT = ttk.Combobox(
    janela,
    values=log_AMTs,
    font=("Arial", 12, "bold"),
    width=15,
)
log_AMT.bind("<<ComboboxSelected>>", mostrar_log_AMT)
log_AMT.grid(column=10, row=5,)

# item mel
label_item_mel = tk.Label(
    janela,
    text="DEFERRAL",
    bg="#435059",
    font=("Arial", 12, "bold"),
    width=9,
    fg="white",
)
label_item_mel.grid(column=1, row=11)

def mostrar_item_mel():
    print("Selecionado:", item_mel.get())
item_mels = ["MEL", "NEF", "CDL", "EO"]
item_mel = ttk.Combobox(
    janela,
    values=item_mels,
    font=("Arial", 11, "bold"),
    width=11,
)
item_mel.bind("<<ComboboxSelected>>", mostrar_item_mel)
item_mel.grid(column=1, row=12)

# ata mel
label_ata_mel = tk.Label(
    janela,
    text="ATA CHPT",
    bg="#435059",
    font=("Arial", 12, "bold"),
    width=9,
    fg="white",
)
label_ata_mel.grid(column=2, row=11)

def mostrar_ata_mel():
    print("Selecionado:", ata_mel.get())
ata_mels = ["21-00-00", "22-00-00", "23-00-00", "24-00-00", "25-00-00"]
ata_mel = ttk.Combobox(
    janela,
    values=ata_mels,
    font=("Arial", 11, "bold"),
    width=11,
)
ata_mel.bind("<<ComboboxSelected>>", mostrar_ata_mel)
ata_mel.grid(column=2, row=12)

# cat mel
label_cat_mel = tk.Label(
    janela,
    text="MEL CAT",
    bg="#435059",
    font=("Arial", 12, "bold"),
    width=9,
    fg="white",
)
label_cat_mel.grid(column=3, row=11)

def mostrar_cat_mel():
    print("Selecionado:", cat_mel.get())
cat_mels = ["CAT_A", "CAT_B", "CAT_C", "CAT_D"]
cat_mel = ttk.Combobox(
    janela,
    values=cat_mels,
    font=("Arial", 11, "bold"),
    width=11,
)
cat_mel.bind("<<ComboboxSelected>>", mostrar_cat_mel)
cat_mel.grid(column=3, row=12)

# Checkbuttons report

def change_color_report():
    if check_var_report.get() == 1:
        check_report.config(bg="#1271b7")
    else:
        check_report.config(bg="#435059")
check_var_report = tk.IntVar()
check_report = tk.Checkbutton(
    janela,
    text="NOREP",
    variable=check_var_report,
    command=change_color_report,
    font=("Arial", 10, "bold"),
    fg="white",
    bg="#435059",
    selectcolor="#435059",
    width=8
)
check_report.grid(column=1, row=8)

# Checkbuttons pilot rep
def change_color_pirep():
    if check_var_pirep.get() == 1:
        pilot_repot.config(bg="#1271b7")
    else:
        pilot_repot.config(bg="#435059")
check_var_pirep = tk.IntVar()
pilot_repot = tk.Checkbutton(
    janela,
    text="PIREP",
    variable=check_var_pirep,
    command=change_color_pirep,
    font=("Arial", 10, "bold"),
    fg="white",
    bg="#435059",
    selectcolor="#435059",
    width=8
)
pilot_repot.grid(column=2, row=8)

# Checkbuttons techn rep
def change_color_techrep():
    if check_var_techrep.get() == 1:
        tech_report.config(bg="#1271b7")
    else:
        tech_report.config(bg="#435059")
check_var_techrep = tk.IntVar()
tech_report = tk.Checkbutton(
    janela,
    text="TECHREP",
    variable=check_var_techrep,
    command=change_color_techrep,
    font=("Arial", 10, "bold"),
    fg="white",
    bg="#435059",
    selectcolor="#435059",
    width=8
)
tech_report.grid(column=3, row=8)

# Ceckbuttons Report
label_report = tk.Label(
    janela,
    text="REPORT",
    bg="#435059",
    font=("Arial", 12, "bold"),
    width=11,
    fg="white",
)
label_report.grid(column=0, row=8)
report = tk.Text(
    janela,
    bg="white",
    fg="black",
    font=("Arial", 12, "bold"),
    height=5, width=62,
)
report.grid(column=0, row=9, columnspan=4)

# Action
label_action = tk.Label(
    janela,
    text="ACTION",
    bg="#435059",
    font=("Arial", 12, "bold"),
    width=11,
    fg="white",
)
label_action.grid(column=0, row=12,)
action = tk.Text(
    janela,
    bg="white",                  # cor de fundo
    fg="black",                         # cor do texto
    font=("Arial", 12, "bold"),                # fonte e tamanho
    height=5, width=62,
)
action.grid(column=0, row=13, columnspan=4)

entradas = [base, bis_log, flight, acft, client, logbook, log_date,
            oil_lh, oil_rh, oil_apu, log_AMT, cat_mel, ata_mel, item_mel]
entradas_2 = [report, action] 
entradas_3 = [base, flight, acft, client, logbook, log_date,
            oil_lh, oil_rh, oil_apu, log_AMT, cat_mel, ata_mel, item_mel]
entradas_4 = [report, action,]

# Botão de ações

btn_new_entry = tk.Button(
    janela,
    bg= "#be0218",
    fg="white",
    font=("Arial", 12, "bold"),
    text="NEW LOG ENTRY",
    width=39,
    #command=""
)
btn_new_entry.grid(column=0, row=15, pady=10, columnspan=3)

btn_enviar = tk.Button(
    janela,
    font=("Arial", 11, "bold"),
    text="SAVE",
    width=12,
    command=enviar_dados)
btn_enviar.grid(column=0, row=16,)

btn_exit = tk.Button(
    janela,
    font=("Arial", 11, "bold"),
    text="EXIT",
    width=12,
    command=exit
)
btn_exit.grid(column=1, row=16,)

btn_clear = tk.Button(
    janela,
    font=("Arial", 11, "bold"),
    text="CLEAR",
    width=12,
    command=clear_all
    )
btn_clear.grid(column=2, row=16,)


# Executar janela
janela.mainloop()
