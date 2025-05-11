function updateUI(data) {
    document.getElementById('direction').innerText = data.direction ?? 'Loading...';
    document.getElementById('vrx').innerText = data.vrx ?? 'Loading...';
    document.getElementById('vry').innerText = data.vry ?? 'Loading...';

    if (data.button_status === 1) {
        document.getElementById('button_status').innerText = 'Released';
    } else if (data.button_status === 0) {
        document.getElementById('button_status').innerText = 'Pressed';
    } else {
        document.getElementById('button_status').innerText = 'Loading...';
    }

    if (data.sensor_status == -1) {
        document.getElementById('sensor_status').innerText = 'Invalid Value';
    } else {
        document.getElementById('sensor_status').innerText = data.sensor_status ?? 'Loading...';
    }
}

async function fetchData() {
    try {
        const response = await fetch('/data');
        const data = await response.json();

        updateUI(data);
    } catch (err) {
        console.error('Erro ao buscar dados:', err);
    }
}

setInterval(fetchData, 500);
