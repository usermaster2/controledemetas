window.onload = async () => {
    const sessionResponse = await window.electron.checkSession();
  
    if (!sessionResponse.success) {
      // Redireciona para a tela de login se a sessão não existir
      window.location.href = 'login.html';
    } else {
      const userSession = sessionResponse.userSession;
      console.log('Usuário logado:', userSession);
      // Exibe informações do usuário na tela (por exemplo, nome e cargo)
      document.getElementById('username').innerText = `Bem-vindo, ${userSession.login}`;
      document.getElementById('userRole').innerText = `Cargo: ${userSession.cargo}`;
    }
  };
  
  // Logout: Apaga a sessão e redireciona para a página de login
  document.getElementById('logoutButton').addEventListener('click', async () => {
    const logoutResponse = await window.electron.logout();
    if (logoutResponse.success) {
      window.location.href = 'login.html';  // Redireciona para o login
    }
  });

  
  