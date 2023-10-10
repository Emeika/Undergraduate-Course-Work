function calculate() {
    const a = parseFloat(document.getElementById('a').value);
    const b = parseFloat(document.getElementById('b').value);
    const c = parseFloat(document.getElementById('c').value);
    const d = parseFloat(document.getElementById('d').value);

    const min = Math.min(a, b, c, d);
    const max = Math.max(a, b, c, d);

    document.getElementById('min').textContent = min;
    document.getElementById('max').textContent = max;

    const numbersArray = [a, b, c, d];
    const randomIndex = Math.floor(Math.random() * numbersArray.length);
    const random = numbersArray[randomIndex];

    document.getElementById('random').textContent = random;


}