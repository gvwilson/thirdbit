function hex(num) {
    const hex = num.toString(16);
    return hex.length == 1 ? '0' + hex : hex;
}

async function changeColor () {
    const response = await fetch('http://127.0.0.1:5000/');
    const data = await response.json();
    const color = `#${hex(data['red'])}${hex(data['green'])}${hex(data['blue'])}`;
    document.querySelector('h1#title').style.color = color;
}
