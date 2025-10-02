// Обработка формы предсказания
document.getElementById('predictionForm').addEventListener('submit', async function(e) {
    e.preventDefault();

    const formData = {
        matrix: document.getElementById('matrix').value,
        density: document.getElementById('density').value,
        density_mod: document.getElementById('density_mod').value,
        hardener_q: document.getElementById('hardener_q').value,
        epoxy_groups: document.getElementById('epoxy_groups').value,
        surface_density: document.getElementById('surface_density').value,
        temp: document.getElementById('temp').value,
        resin_cons: document.getElementById('resin_cons').value,
        angle: document.getElementById('angle').value,
        pitch: document.getElementById('pitch').value,
        patch_density: document.getElementById('patch_density').value
    };

    try {
        const response = await fetch('/predict', {
            method: 'POST',
            headers: {
                'Content-Type': 'application/json',
            },
            body: JSON.stringify(formData)
        });

        const result = await response.json();

        if (result.status === 'success') {
            document.getElementById('elasticResult').textContent = result.elastic_modulus;
            document.getElementById('strengthResult').textContent = result.tensile_strength;
            document.getElementById('result').style.display = 'block';
        } else {
            alert('Ошибка: ' + result.message);
        }
    } catch (error) {
        alert('Ошибка соединения: ' + error);
    }
});