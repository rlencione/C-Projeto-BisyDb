import mysql.connector


try:
    # Criando a conexão
    conexao = mysql.connector.connect(
        host="localhost",       # endereço do servidor MySQL
        user="root",     # usuário do MySQL
        password="Bis092",   # senha do MySQL
        database="bisydb"    # nome do banco de dados
    )

    if conexao.is_connected():
        print("Conexão realizada com sucesso!")

        # Criando um cursor para executar comandos SQL
        cursor = conexao.cursor(buffered=True)

        comando = f'INSERT INTO bis_log_table (base, log_bis, client, ' \
            'log_date, logbook, log_AMT, oil_lh, oil_rh, oil_apu, entry_report, ' \
            'entry_action) VALUES ({base}, {bis_log}, {client},{log_date}, {logbook}, {oil_lh}, {oil_rh}, {oil_apu}, ' \
            '{log_AMT}, {report}, {action})'

        # Exemplo de consulta
        cursor.execute(" SELECT DATABASE();")

        # Edita o banco de dados
        conexao.commit()

        # Lê o banco de dadosentry_logbook
        resultado = cursor.fetchone()
        print("Banco de dados conectado:", resultado)

        # Fechando cursor e conexão
        cursor.close()
        conexao.close()

except mysql.connector.Error as erro:
    print("Erro ao conectar no MySQL:", {erro})
