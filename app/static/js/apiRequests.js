function updateUI(data) {
    document.getElementById('direction').innerText = data.direction ?? 'Loading...';
    document.getElementById('vrx').innerText = data.vrx ?? 'Loading...';
    document.getElementById('vry').innerText = data.vry ?? 'Loading...';

    if (data.button_status === 1) {
        document.getElementById('button_status').innerText = 'RELEASED';
    } else if (data.button_status === 0) {
        document.getElementById('button_status').innerText = 'PRESSED';
    } else {
        document.getElementById('button_status').innerText = 'Loading...';
    }
}

function setLoadingUI() {
    document.getElementById('direction').innerText = 'Loading...';
    document.getElementById('vrx').innerText = 'Loading...';
    document.getElementById('vry').innerText = 'Loading...';
    document.getElementById('button_status').innerText = 'Loading...';
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