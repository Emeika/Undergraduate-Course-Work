function calculate() {
    const num1 = parseFloat(document.getElementById('num1').value);
    const num2 = parseFloat(document.getElementById('num2').value);

    const sum = num1 + num2;
    const subtract = num1 - num2;
    const multiply = num1 * num2;

    let divide;
    if (num2 === 0) {
        divide = 'Cannot divide by zero';
    } else {
        divide = num1 / num2;
    }

    document.getElementById('sum').textContent = sum;
    document.getElementById('subtract').textContent = subtract;
    document.getElementById('multiply').textContent = multiply;
    document.getElementById('divide').textContent = divide;
}
