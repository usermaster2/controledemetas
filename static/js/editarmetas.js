document.addEventListener("DOMContentLoaded", function () {
    const inputs = document.querySelectorAll(".meta-input");
    const totalMeta = document.getElementById("total_meta");

    function atualizarTotal() {
        let total = 0;
        inputs.forEach(input => {
            let valor = parseFloat(input.value.replace(",", ".")) || 0;
            total += valor;
        });
        totalMeta.value = total.toFixed(2);
    }

    // Atualizar o total quando qualquer campo for modificado
    inputs.forEach(input => {
        input.addEventListener("input", atualizarTotal);
    });

    // Atualizar ao carregar a página
    atualizarTotal();
});

document.addEventListener("DOMContentLoaded", function () {
    const inputs = document.querySelectorAll(".meta-input");
    const totalMeta = document.getElementById("total_meta1");

    function atualizarTotal() {
        let total = 0;
        inputs.forEach(input => {
            let valor = parseFloat(input.value.replace(",", ".")) || 0;
            total += valor;
        });
        totalMeta.value = total.toFixed(2);
    }


    // Atualizar ao carregar a página
    atualizarTotal();
});

// document.addEventListener("DOMContentLoaded", function () {
//     metapercent(); // Chama a função assim que a página carregar
// });

function metapercent() {
    const novaMeta = document.getElementById("total_meta");
    const metaAtual = document.getElementById("total_meta1");
    const porcentagemInput = document.getElementById("Porcentagem");
    

    if (!novaMeta || !metaAtual || !porcentagemInput) return;

    // Converte valores para float, substituindo vírgula por ponto (caso necessário)
    const valorNovaMeta = parseFloat(novaMeta.value.replace(',', '.')) || 0;
    const valorMetaAtual = parseFloat(metaAtual.value.replace(',', '.')) || 0;

    let percentualDiferenca = 0;
    let cor = "black"; // Cor padrão

    // Calcula a variação percentual de forma que, se houver queda, o valor será negativo
    percentualDiferenca = ((valorNovaMeta - valorMetaAtual) / valorMetaAtual) * 100;
    
    // Se a variação for positiva, a cor será verde; se for negativa, será vermelha
    if (percentualDiferenca > 0) {
        cor = "green"; // Crescimento
    } else if (percentualDiferenca < 0) {
        cor = "red"; // Queda
    }

    porcentagemInput.value = percentualDiferenca.toFixed(2) + "%";
    porcentagemInput.style.color = cor;
}



