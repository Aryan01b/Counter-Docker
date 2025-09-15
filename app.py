from flask import Flask, jsonify, send_from_directory
import os

app = Flask(__name__)

def fibonacci(n):
    a, b = 0, 1
    result = []
    for _ in range(n):
        result.append(a)
        a, b = b, a + b
    return result

# HTML template has been moved to res/fib-counter.html

@app.route('/')
def index():
    return send_from_directory('res', 'fib-counter.html')

@app.route('/api/fibonacci/<int:n>', methods=['GET'])
def get_fibonacci(n):
    if n < 0:
        return jsonify({"error": "Please provide a non-negative number"}), 400
    return jsonify({"fibonacci_sequence": fibonacci(n)})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
