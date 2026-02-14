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
        cursor = conexao.cursor()

        # Exemplo de consulta
        cursor.execute("SELECT DATABASE();")
        resultado = cursor.fetchone()
        print("Banco de dados conectado:", resultado)

        # Fechando cursor e conexão
        cursor.close()
        conexao.close()

except mysql.connector.Error as erro:
    print("Erro ao conectar no MySQL:", {erro})
