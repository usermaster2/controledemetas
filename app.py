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
@app.route('/verMetas.html')
def verMetas():
    return render_template('verMetas.html')

@app.route('/cadastrar_usuarios.html')
def cadastrar_usuario(): 
    return render_template('cadastrar_usuarios.html')

@app.route('/tela_inicial')
def tela_inicial(): 
    return render_template('tela_inicial.html')

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
    
    

    
  # Adicionar dados
  
   # Convertendo os valores de texto para número (int)

        
@app.route('/addmetas.html', methods=['GET', 'POST'])
def addmetas():
    if request.method == 'POST':
        ano = request.form['ano']
        
        # Função para limpar o formato e converter para número
        def converter_para_numero(valor):
            # Remover pontos (separadores de milhar) e substituir a vírgula por ponto
            valor_limpo = valor.replace('.', '').replace(',', '.')
            try:
                return float(valor_limpo)
            except ValueError:
                return 0  # Retorna 0 caso o valor não seja válido
        
        # Convertendo os valores de texto para número (float)
        janeiro = converter_para_numero(request.form['janeiro']) if request.form['janeiro'] else 0
        fevereiro = converter_para_numero(request.form['fevereiro']) if request.form['fevereiro'] else 0
        marco = converter_para_numero(request.form['marco']) if request.form['marco'] else 0
        abril = converter_para_numero(request.form['abril']) if request.form['abril'] else 0
        maio = converter_para_numero(request.form['maio']) if request.form['maio'] else 0
        junho = converter_para_numero(request.form['junho']) if request.form['junho'] else 0
        julho = converter_para_numero(request.form['julho']) if request.form['julho'] else 0
        agosto = converter_para_numero(request.form['agosto']) if request.form['agosto'] else 0
        setembro = converter_para_numero(request.form['setembro']) if request.form['setembro'] else 0
        outubro = converter_para_numero(request.form['outubro']) if request.form['outubro'] else 0
        novembro = converter_para_numero(request.form['novembro']) if request.form['novembro'] else 0
        dezembro = converter_para_numero(request.form['dezembro']) if request.form['dezembro'] else 0

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO metas (ano, janeiro, fevereiro, marco, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (ano, janeiro, fevereiro, marco, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro))
        conn.commit()
        conn.close()
        return redirect(url_for('addmetas'))

    return render_template('addmetas.html')

 
    
# Editar dados
@app.route('/editarmetas/<int:id>', methods=['GET', 'POST'])
def editarmetas(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    if request.method == 'POST':
        ano = request.form['ano']
        janeiro = request.form['janeiro']
        fevereiro = request.form['fevereiro']
        marco = request.form['marco']
        abril = request.form['abril']
        maio = request.form['maio']
        junho = request.form['junho']
        julho = request.form['julho']
        agosto = request.form['agosto']
        setembro = request.form['setembro']
        outubro = request.form['outubro']
        novembro = request.form['novembro']
        dezembro = request.form['dezembro']

        cursor.execute('''
            UPDATE metas
            SET ano = ?, janeiro = ?, fevereiro = ?, marco = ?, abril = ?, maio = ?, junho = ?, julho = ?, agosto = ?, setembro = ?, outubro = ?, novembro = ?, dezembro = ?
            WHERE id = ?
        ''', (ano, janeiro, fevereiro, marco, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro, id))
        conn.commit()
        conn.close()
        return redirect(url_for('index'))

    cursor.execute('SELECT * FROM metas WHERE id = ?', (id,))
    meta = cursor.fetchone()
    conn.close()
    return render_template('editarmetas.html', meta=meta)


    # Excluir dados
@app.route('/delete/<int:id>', methods=['GET', 'POST'])
def delete(id):
    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute('DELETE FROM metas WHERE id = ?', (id,))
    conn.commit()
    conn.close()
    return redirect(url_for('index'))
    
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
