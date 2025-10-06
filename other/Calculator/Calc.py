# calc.py
from flask import Flask, render_template_string, request

app = Flask(__name__)

# HTML template
template = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Calculator</title>
    <style>
        body { font-family: Arial; background-color: #f5f5f5; text-align: center; padding: 50px; }
        input[type=number], select { padding: 10px; margin: 10px; width: 150px; }
        input[type=submit] { padding: 10px 20px; margin: 10px; }
        h1 { color: #2c3e50; }
        .result { margin-top: 20px; font-size: 1.5em; color: #27ae60; }
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
def calculator():
    result = None
    if request.method == "POST":
        try:
            num1 = float(request.form["num1"])
            num2 = float(request.form["num2"])
            op = request.form["operation"]

            if op == "add":
                result = num1 + num2
            elif op == "subtract":
                result = num1 - num2
            elif op == "multiply":
                result = num1 * num2
            elif op == "divide":
                result = num1 / num2 if num2 != 0 else "Error: Division by zero"
        except ValueError:
            result = "Invalid input"
    return render_template_string(template, result=result)

if __name__ == "__main__":
    app.run(debug=True)
