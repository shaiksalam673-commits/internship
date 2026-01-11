from flask import Flask, request, render_template_string
import random

app = Flask(__name__)

# HTML template for display
template = """
<!DOCTYPE html>
<html>
<head>
    <title>Flask Fun App</title>
    <style>
        body {
            background-color: #f4f4f9;
            font-family: Arial, sans-serif;
            text-align: center;
            margin-top: 100px;
        }
        h1 {
            color: {{color}};
            font-size: 50px;
            text-shadow: 2px 2px 10px gray;
        }
        a {
            text-decoration: none;
            color: #007bff;
            font-size: 18px;
        }
    </style>
</head>
<body>
    <h1>{{message}}</h1>
    <p><a href="/">Go Home</a></p>
</body>
</html>
"""

@app.route('/')
def home():
    return """
    <h2>Welcome to Flask Fun App 🎨</h2>
    <p>Try the following routes:</p>
    <ul>
        <li>/shout?name=yourname → Converts to uppercase</li>
        <li>/reverse?name=yourname → Reverses your name</li>
        <li>/stylish?name=yourname → Displays your name in a random color</li>
    </ul>
    """

@app.route('/shout')
def shout():
    name = request.args.get('name', 'Guest')
    message = f"HELLO, {name.upper()}!"
    return render_template_string(template, message=message, color="#FF5733")

@app.route('/reverse')
def reverse():
    name = request.args.get('name', 'Guest')
    message = f"Reversed: {name[::-1]}"
    return render_template_string(template, message=message, color="#33B5E5")

@app.route('/stylish')
def stylish():
    name = request.args.get('name', 'Guest')
    colors = ['#FF33A8', '#33FF57', '#FFD133', '#33D1FF', '#B833FF']
    message = f"Stylish Name: {name.upper()}"
    return render_template_string(template, message=message, color=random.choice(colors))

if __name__ == '__main__':
    app.run(debug=True)
