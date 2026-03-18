document.addEventListener('DOMContentLoaded', () => {
    const form = document.getElementById('leadForm');
    const submitBtn = document.getElementById('submitBtn');
    const successMessage = document.getElementById('successMessage');

    // O envio silencioso (AJAX) foi desativado temporariamente 
    // para forçar a página de ativação do FormSubmit.
    form.addEventListener('submit', () => {
        // Estado de "Carregando" no botão
        const originalBtnText = submitBtn.innerHTML;
        submitBtn.innerHTML = '<i class="fa-solid fa-spinner fa-spin"></i> Redirecionando...';
        // Não usamos e.preventDefault() para que o FormSubmit abra sua própria página
    });

    // Máscara simples para WhatsApp (apenas remove não números antes de enviar e permite formatação básica)
    const whatsappInput = document.querySelector('input[name="whatsapp"]');
    whatsappInput.addEventListener('input', (e) => {
        let val = e.target.value.replace(/\D/g, '');
        if (val.length > 2 && val.length <= 6) {
            val = `(${val.slice(0, 2)}) ${val.slice(2)}`;
        } else if (val.length > 6 && val.length <= 10) {
            val = `(${val.slice(0, 2)}) ${val.slice(2, 6)}-${val.slice(6)}`;
        } else if (val.length > 10) {
            val = `(${val.slice(0, 2)}) ${val.slice(2, 7)}-${val.slice(7, 11)}`;
        }
        e.target.value = val;
    });
});
