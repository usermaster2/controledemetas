document.getElementById('formCadastro').addEventListener('submit', async (event) => {
  event.preventDefault(); // Previne o envio padrão do formulário

  // Captura os valores dos campos
  const nome = document.getElementById('nome').value;
  const cargo = document.getElementById('cargo').value;
  const cadastra = document.getElementById('cadastra').checked ? 'S' : 'N';
  const altera = document.getElementById('altera').checked ? 'S' : 'N';
  const remove = document.getElementById('remove').checked ? 'S' : 'N';
  const lista = document.getElementById('lista').checked ? 'S' : 'N';
  const usuario = document.getElementById('usuario').value;
  const senha = document.getElementById('senha').value;
  const confirmSenha = document.getElementById('confirmSenha').value;

  // Validação de senha
  if (senha !== confirmSenha) {
    alert('As senhas não coincidem!');
    return;
  }

  // Dados para envio ao backend
  const userData = {
    nome,
    cargo,
    cadastra,
    altera,
    remove,
    lista,
    usuario,
    senha,
  };

  // Pop-up de revisão
  const confirm = window.confirm(`
      Confirmar os dados:
      Nome: ${nome}
      Cargo: ${cargo}
      Permissões: 
      Cadastrar: ${cadastra}, 
      Alterar: ${altera}, 
      Remover: ${remove}, 
      Listar: ${lista}
      Usuário: ${usuario}
      Senha: ${senha}
      INSERT INTO SENHAMETASJCP (nome, cargo, cadastra, altera, remove, lista, usuario, senha)
        VALUES (@nome, @cargo, @cadastra, @altera, @remove, @lista, @usuario, @senha)
    `);

  if (!confirm) return;

  try {
    // Envio para o backend via Flask
    const response = await fetch('/cadastrar', {
      method: 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(userData),
    });

    const result = await response.json();

    if (result.success) {
      alert('Usuário cadastrado com sucesso!');
      document.getElementById('formCadastro').reset(); // Limpa o formulário
    } else {
      alert(`Erro ao cadastrar: ${result.message}`);
    }
  } catch (error) {
    console.error('Erro ao cadastrar usuário:', error);
    alert('Erro ao processar o cadastro.');
  }
});

function abrirpopup() {
  var popupsair = document.getElementById("popupsair");
  popupsair.style.display = "block"; 
}
 
function fecharpopup() {
  var popupsair = document.getElementById("popupsair");
  popupsair.style.display = "none";
}

function volt() {
  window.location.href = "/tela_inicial";
}
