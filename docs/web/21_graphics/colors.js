const SIZE = 100;

function changeColor() {
    const color = Math.floor(Math.random() * Math.pow(2, 24)).toString(16);
    document.getElementById('box').setAttribute('fill', `#${color}`);
    document.getElementById('control').textContent = color;
}

function drawInitial() {
    const drawing = SVG().addTo('#drawing').size(SIZE, SIZE);
    drawing.rect(SIZE, SIZE).attr({ id: 'box' }).move(0, 0);
    changeColor();
}

window.addEventListener('load', drawInitial)
