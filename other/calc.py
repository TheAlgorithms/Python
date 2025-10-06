from flask import Flask, request, render_template_string

app = Flask(__name__)

def calculate(num1: float, num2: float, operation: str) -> float:
    """
    Perform basic arithmetic operations: add, subtract, multiply, divide.

    >>> calculate(2, 3, 'add')
    5
    >>> calculate(5, 3, 'subtract')
    2
    >>> calculate(4, 2, 'multiply')
    8
    >>> calculate(10, 2, 'divide')
    5.0
    >>> calculate(5, 0, 'divide')
    Traceback (most recent call last):
        ...
    ValueError: Division by zero is not allowed.
    """
    if operation == "add":
        return num1 + num2
    elif operation == "subtract":
        return num1 - num2
    elif operation == "multiply":
        return num1 * num2
    elif operation == "divide":
        if num2 == 0:
            raise ValueError("Division by zero is not allowed.")
        return num1 / num2
    else:
        raise ValueError(f"Unknown operation: {operation}")

# HTML template for the web interface
template = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Calculator</title>
    <style>
        body { font-family: Arial, sans-serif; text-align: center; padding: 50px; background: #f7f7f7; }
        input, select { padding: 10px; margin: 5px; width: 150px; }
        input[type=submit] { width: auto; cursor: pointer; }
        .result { margin-top: 20px; font-size: 1.5em; color: #27ae60; }
        h1 { color: #2c3e50; }
    </style>
</head>
<body>
    <h1>Flask Calculator</h1>
    <form method="POST">
        <input type="number" name="num1" step="any" placeholder="First Number" required>
        <input type="number" name="num2" step="any" placeholder="Second Number" required>
        <br>
        <select name="operation">
            <option value="add">Add (+)</option>
            <option value="subtract">Subtract (-)</option>
            <option value="multiply">Multiply (×)</option>
            <option value="divide">Divide (÷)</option>
        </select>
        <br>
        <input type="submit" value="Calculate">
    </form>
    {% if result is not none %}
        <div class="result">Result: {{ result }}</div>
    {% endif %}
</body>
</html>
"""

@app.route("/", methods=["GET", "POST"])
def home():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            op = request.form["operation"]
            result = calculate(num1, num2, op)
        except Exception as e:
            result = str(e)
    return render_template_string(template, result=result)

if __name__ == "__main__":
    app.run(debug=True)
