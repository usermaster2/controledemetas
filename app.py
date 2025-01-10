from flask import Flask, render_template, request, jsonify, redirect, url_for
import pyodbc

app = Flask(__name__)

# Configuração do banco de dados
db_config = {
    'server'                : '10.10.0.200',
    'database'              : 'CigamDB',
    'username'              : 'sa',
    'password'              : 'PadA505.sa',
    'driver'                : '{ODBC Driver 17 for SQL Server}',
    'encrypt'               : False,                             # Se precisar de conexão segura
    'trustServerCertificate': True  # Aceita certificados autoassinados
}

# Função para conectar ao banco de dados
def get_db_connection(): 
    conn = pyodbc.connect(
        f"DRIVER={db_config['driver']};"
        f"SERVER={db_config['server']};"
        f"DATABASE={db_config['database']};"
        f"UID={db_config['username']};"
        f"PWD={db_config['password']}"
    )
    return conn
#rotas para as paginas  /////////////////////////////////

@app.route('/cadastrar_usuarios.html')
def cadastrar_usuario(): 
    return render_template('cadastrar_usuarios.html')

@app.route('/tela_inicial')
def tela_inicial(): 
    return render_template('tela_inicial.html')


@app.route('/cadastrar_usuarios')
def cadastrar_usuarios(): 
    return render_template('cadastrar_usuarios.html')


@app.route('/cadastrar', methods=['POST'])
def cadastrar(): 
    data     = request.get_json()  # Captura os dados JSON enviados pelo front-end
    nome     = data.get('nome')
    cargo    = data.get('cargo')
    cadastra = data.get('cadastra')
    altera   = data.get('altera')
    remove   = data.get('remove')
    lista    = data.get('lista')
    usuario  = data.get('usuario')
    senha    = data.get('senha')
    
    
    
#  //////////////////////////////////////////////////


    # Validação de dados
    if not nome or not cargo or not usuario or not senha: 
        return jsonify({'success': False, 'message': 'Dados incompletos'})

    try: 
        conn   = get_db_connection()
        cursor = conn.cursor()

        # Inserção no banco de dados
        query = """
        INSERT INTO SENHAMETASJCP (nome, cargo, cadastra, altera, remove, lista, usuario, senha)
        VALUES (?, ?, ?, ?, ?, ?, ?, ?)
        """
        cursor.execute(query, (nome, cargo, cadastra, altera, remove, lista, usuario, senha))
        conn.commit()

        return jsonify({'success': True, 'message': 'Usuário cadastrado com sucesso!'})

    except Exception as e: 
        print("Erro ao cadastrar no banco de dados:", e)
        return jsonify({'success': False, 'message': 'Erro ao cadastrar no banco de dados.'})

    finally: 
        conn.close()



# Rota para exibir a página de login
@app.route('/')
def login_page(): 
    return render_template('login.html')




# Rota para processar o login
@app.route('/login', methods=['POST'])
def login(): 
    data     = request.json  # Receber JSON do JavaScript
    username = data.get('login')
    password = data.get('senha')

    try: 
        conn   = get_db_connection()
        cursor = conn.cursor()
        query  = """
        SELECT * FROM SENHAMETASJCP WHERE usuario = ? AND senha = ?
        """
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        if user: 
            # Retorna um JSON com a URL para redirecionar
            return jsonify({'redirect_url': 'tela_inicial'}), 200
        else: 
            return jsonify({'message': 'Credenciais inválidas.'}), 401

    except Exception as e: 
        print("Erro no servidor:", e)
        return jsonify({'message': 'Erro no servidor.'}), 500

    finally: 
        conn.close()


# Iniciar o servidor
if __name__ == '__main__':
    app.run(debug=True)
