from flask import Flask, render_template, request, jsonify, redirect, url_for
import pyodbc

app = Flask(__name__)

# Configuração do banco de dados
db_config = {
    'server': '10.10.0.200',
    'database': 'CigamDB',
    'username': 'sa',
    'password': 'PadA505.sa',
    'driver': '{ODBC Driver 17 for SQL Server}',
    'encrypt': False,  
    'trustServerCertificate': True  
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

# Rotas para as páginas
@app.route('/verMetas.html')
def verMetas():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(''' 
            SELECT 
                ano,
                janeiro,
                fevereiro,
                marco,
                abril,
                maio,
                junho,
                julho,
                agosto,
                setembro,
                outubro,
                novembro,
                dezembro,
                meta_total
            FROM Metas
        ''')
        rows = cursor.fetchall()

        # Formatar os dados em uma lista de dicionários
        metas = [
            {
                'ano': row[0],
                'janeiro': row[1],
                'fevereiro': row[2],
                'marco': row[3],
                'abril': row[4],
                'maio': row[5],
                'junho': row[6],
                'julho': row[7],
                'agosto': row[8],
                'setembro': row[9],
                'outubro': row[10],
                'novembro': row[11],
                'dezembro': row[12],
                'meta_total':row[13]
            }
            for row in rows
        ]

        return render_template('verMetas.html', metas=metas)
    except Exception as e:
        return f"Erro: {e}"
    
#LANCAR METAS#
@app.route('/lancarmetas.html')
def lancarmetas():
    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(''' 
        select CD_EMPRESA, Nome_completo, Divisao from geempres where DIVISAO IN ('C2', 'C3', 'C1', 'C4')
        ''')
        rows = cursor.fetchall()

        # Formatar os dados em uma lista de dicionários
        lancarmetas = [
            {
                'CD_EMPRESA': row[0],
                'Nome_completo': row[1],
                'Divisao': row[2]
            }
            for row in rows
        ]

        return render_template('lancarmetas.html', lancarmetas=lancarmetas)  # Passando os dados para o template
    except Exception as e:
        return f"Erro: {e}"


  

@app.route('/cadastrar_usuarios.html')
def cadastrar_usuario():
    return render_template('cadastrar_usuarios.html')

@app.route('/tela_inicial')
def tela_inicial():
    return render_template('tela_inicial.html')

@app.route('/cadastrar', methods=['POST'])
def cadastrar():
    data = request.get_json() 
    nome = data.get('nome')
    cargo = data.get('cargo')
    cadastra = data.get('cadastra')
    altera = data.get('altera')
    remove = data.get('remove')
    lista = data.get('lista')
    usuario = data.get('usuario')
    senha = data.get('senha')

    # Validação de dados
    if not nome or not cargo or not usuario or not senha:
        return jsonify({'success': False, 'message': 'Dados incompletos'})

    try:
        conn = get_db_connection()
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
        
    


@app.route('/addmetas.html', methods=['GET', 'POST'])
def addmetas():
    if request.method == 'POST':
        ano = request.form['ano']

        # Função para limpar o formato e converter para número
        def converter_para_numero(valor):
            valor_limpo = valor.replace('.', '').replace(',', '.')
            try:
                return float(valor_limpo)
            except ValueError:
                return 0

        # Convertendo os valores de texto para número (float)
        meses = ['janeiro', 'fevereiro', 'marco', 'abril', 'maio', 'junho',
                 'julho', 'agosto', 'setembro', 'outubro', 'novembro', 'dezembro']
        valores = [converter_para_numero(request.form[m]) if request.form[m] else 0 for m in meses]

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute('''
            INSERT INTO metas (ano, janeiro, fevereiro, marco, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro)
            VALUES (?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?, ?)
        ''', (ano, *valores))
        conn.commit()
        cursor.execute('''
            UPDATE Metas SET meta_total =  ( janeiro + fevereiro + marco + abril + maio + junho + julho + agosto + setembro + outubro + novembro + dezembro)
            WHERE ANO = ?
        ''', (ano))
        conn.commit()
        
        
        conn.close()
        return redirect(url_for('addmetas'))

    return render_template('addmetas.html')


@app.route('/editarmetas/<int:ano>', methods=['GET', 'POST'])
def editarmetas(ano):
    try:
        conn = get_db_connection()
        cursor = conn.cursor()

        if request.method == 'POST':
            # Captura os dados do formulário
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
       

           

            # Atualiza os dados no banco de dados
            cursor.execute('''
                UPDATE Metas
                SET janeiro = ?, fevereiro = ?, marco = ?, abril = ?, maio = ?, junho = ?, 
                    julho = ?, agosto = ?, setembro = ?, outubro = ?, novembro = ?, dezembro = ?
                WHERE ano = ?
            ''', (janeiro, fevereiro, marco, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro, ano))

            conn.commit()  # Confirma as alterações no banco
            
            cursor.execute('''
            UPDATE Metas SET meta_total =  ( janeiro + fevereiro + marco + abril + maio + junho + julho + agosto + setembro + outubro + novembro + dezembro)
            WHERE ANO = ?
        ''', (ano))
            conn.commit()
            

            return redirect(url_for('verMetas'))  # Redireciona para a página de visualização das metas

        # Caso o método seja GET, busca os dados para exibição
        cursor.execute(''' 
            SELECT 
                ano,
                janeiro,
                fevereiro,
                marco,
                abril,
                maio,
                junho,
                julho,
                agosto,
                setembro,
                outubro,
                novembro,
                dezembro
            
              
            FROM Metas
            WHERE ano = ?
        ''', (ano,))
        row = cursor.fetchone()

        if row:
            meta = {
                'ano': row[0],
                'janeiro': row[1],
                'fevereiro': row[2],
                'marco': row[3],
                'abril': row[4],
                'maio': row[5],
                'junho': row[6],
                'julho': row[7],
                'agosto': row[8],
                'setembro': row[9],
                'outubro': row[10],
                'novembro': row[11],
                'dezembro': row[12]
                
            }
            return render_template('editarmetas.html', meta=meta)
        else:
            return "Meta não encontrada para o ano especificado.", 404

    except Exception as e:
        return f"Erro: {e}"
    finally:
        conn.close()




# Rota para exibir a página de login
@app.route('/')
def login_page():
    return render_template('login.html')

# Rota para processar o login
@app.route('/login', methods=['POST'])
def login():
    data = request.json  # Receber JSON do JavaScript
    username = data.get('login')
    password = data.get('senha')

    try:
        conn = get_db_connection()
        cursor = conn.cursor()
        query = """
        SELECT * FROM SENHAMETASJCP WHERE usuario = ? AND senha = ?
        """
        cursor.execute(query, (username, password))
        user = cursor.fetchone()

        if user:
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
