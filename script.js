document.addEventListener('DOMContentLoaded', () => {
    // 1. Lead Capture Form
    const form = document.getElementById('leadForm');
    const submitBtn = document.getElementById('submitBtn');

    if (form && submitBtn) {
        form.addEventListener('submit', () => {
            submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Enviando...';
        });
    }

    // 2. Máscara para WhatsApp
    const whatsappInput = document.querySelector('input[name="whatsapp"]');
    if (whatsappInput) {
        whatsappInput.addEventListener('input', (e) => {
            let val = e.target.value.replace(/\D/g, '');
            if (val.length > 2 && val.length <= 6) {
                val = () ;
            } else if (val.length > 6 && val.length <= 10) {
                val = () -;
            } else if (val.length > 10) {
                val = () -;
            }
            e.target.value = val;
        });
    }

    // 3. Simulador Interativo de Lucro e Economia
    const chips = document.querySelectorAll('.publico-chips .chip');
    const simVendas = document.getElementById('simVendas');
    const simTempo = document.getElementById('simTempo');
    const simEconomia = document.getElementById('simEconomia');

    const dadosSimulacao = {
        '500': {
            vendas: '+25% a +35%',
            tempo: '15 segundos',
            economia: 'R$ 1.500 a R$ 3.000'
        },
        '1000': {
            vendas: '+25% a +40%',
            tempo: '15 segundos',
            economia: 'R$ 3.000 a R$ 6.000'
        },
        '2500': {
            vendas: '+30% a +45%',
            tempo: '15 segundos',
            economia: 'R$ 7.500 a R$ 15.000'
        },
        '5000': {
            vendas: '+35% a +50%',
            tempo: '15 segundos',
            economia: 'R$ 15.000 a R$ 30.000+'
        }
    };

    chips.forEach(chip => {
        chip.addEventListener('click', () => {
            chips.forEach(c => c.classList.remove('active'));
            chip.classList.add('active');

            const publico = chip.getAttribute('data-publico');
            const data = dadosSimulacao[publico] || dadosSimulacao['500'];

            if (simVendas) simVendas.textContent = data.vendas;
            if (simTempo) simTempo.textContent = data.tempo;
            if (simEconomia) simEconomia.textContent = data.economia;
        });
    });
});
