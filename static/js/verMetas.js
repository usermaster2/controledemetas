
// Selecionando todas as linhas da tabela
const rows = document.querySelectorAll('.meta-row');
const editLink = document.getElementById('edit-link');

rows.forEach(row => {
    row.addEventListener('click', function() {
        // Pegando o ano da linha clicada
        const ano = this.getAttribute('data-ano');
        // Atualizando o link de edição com o ano da linha
        editLink.href = `/editarmetas/${ano}`; // Gerando a URL diretamente
        // Adicionando uma classe de seleção para destacar a linha
        rows.forEach(r => r.classList.remove('selected'));
        this.classList.add('selected');
    });
});
