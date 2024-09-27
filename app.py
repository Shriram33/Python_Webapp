from flask import Flask, render_template

app = Flask(__name__)

# Home page route
@app.route('/')
def home():
    return '<h1>Welcome to My Python Webpage!</h1><p>This is a simple webpage built using Flask.</p>'

# About page route
@app.route('/about')
def about():
    return '<h2>About</h2><p>This page gives more information about this project.</p>'

if __name__ == '__main__':
    app.run(debug=True)
