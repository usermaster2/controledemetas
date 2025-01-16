const janeiro = document.getElementById('janeiro');
const fevereiro = document.getElementById('fevereiro');
const março = document.getElementById('marco');
const abril = document.getElementById('abril');
const maio = document.getElementById('maio');
const junho = document.getElementById('junho');
const julho = document.getElementById('julho');
const agosto = document.getElementById('agosto');
const setembro = document.getElementById('setembro');
const outubro = document.getElementById('outubro');
const novembro = document.getElementById('novembro');
const dezembro = document.getElementById('dezembro');

const inputs = [janeiro, fevereiro, março, abril, maio, junho, julho, agosto, setembro, outubro, novembro, dezembro];

inputs.forEach(input => {
    input.addEventListener('input', (e) => {
        let value = e.target.value;

        value = value.replace(/[^\d,]/g, '');

        // Substitui vírgulas extras
        value = value.replace(/,+/g, ',');

        // Adiciona separadores de milhar
        const parts = value.split(',');
        parts[0] = parts[0].replace(/\B(?=(\d{3})+(?!\d))/g, '.');

        e.target.value = parts.join(',');
    });

    input.addEventListener('blur', () => {
        let value = input.value;

        // Adiciona ",00" caso o campo esteja vazio ou sem decimais
        if (!value.includes(',')) {
            value += ',00';
        } else if (value.endsWith(',')) {
            value += '00';
        } else if (value.split(',')[1].length === 1) {
            value += '0';
        }

        input.value = value;
    });
});


