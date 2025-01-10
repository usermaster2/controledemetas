document.querySelector('.container').addEventListener('submit', async (event) => {
    event.preventDefault();

    const login = document.getElementById('login').value;
    const senha = document.getElementById('senha').value;

    try {
        const response = await fetch('/login', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({ login, senha }),
        });

        if (response.ok) {
                    const data = await response.json();

            // Redirecionar para a URL recebida no JSON
            window.location.href = data.redirect_url;
        } else {
            alert(data.message);
        }
    } catch (err) {
        console.error('Erro:', err);
        alert('Erro ao conectar ao servidor.');
    }
});
