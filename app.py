from flask import Flask, jsonify, render_template_string

app = Flask(__name__)

def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

HTML_TEMPLATE = """
<!DOCTYPE html>
<html>
<head>
    <title>Fibonacci Counter</title>
    <style>
        body {
            font-family: Arial, sans-serif;
            max-width: 800px;
            margin: 0 auto;
            padding: 20px;
            text-align: center;
        }
        .container {
            margin-top: 50px;
        }
        .fibonacci {
            font-size: 24px;
            margin: 20px 0;
            padding: 10px;
            border: 1px solid #ddd;
            border-radius: 5px;
            min-height: 36px;
        }
        button {
            padding: 10px 20px;
            font-size: 16px;
            background-color: #4CAF50;
            color: white;
            border: none;
            border-radius: 4px;
            cursor: pointer;
            margin: 5px;
        }
        button:hover {
            background-color: #45a049;
        }
    </style>
</head>
<body>
    <div class="container">
        <h1>Fibonacci Counter</h1>
        <div class="fibonacci" id="fibonacci">0</div>
        <div>
            <button onclick="getNextFibonacci()">Next Fibonacci Number</button>
            <button onclick="resetCounter()">Reset</button>
        </div>
    </div>

    <script>
        let count = 0;
        let fibNumbers = [0, 1];

        function updateDisplay() {
            document.getElementById('fibonacci').textContent = fibNumbers[count];
        }

        function getNextFibonacci() {
            count++;
            if (count >= fibNumbers.length) {
                fibNumbers.push(fibNumbers[count-1] + fibNumbers[count-2]);
            }
            updateDisplay();
        }

        function resetCounter() {
            count = 0;
            fibNumbers = [0, 1];
            updateDisplay();
        }

        // Initialize display
        updateDisplay();
    </script>
</body>
</html>
"""

@app.route('/')
def index():
    return render_template_string(HTML_TEMPLATE)

@app.route('/api/fibonacci/<int:n>', methods=['GET'])
def get_fibonacci(n):
    if n < 0:
        return jsonify({"error": "Please provide a non-negative number"}), 400
    return jsonify({"fibonacci_sequence": fibonacci(n)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
