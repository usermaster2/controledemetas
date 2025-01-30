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

