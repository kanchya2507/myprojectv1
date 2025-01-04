from flask import Flask, render_template

app = Flask(__name__)

@app.route('')
def home()
    return h1Welcome to My Python Website!h1pThis is a simple Flask app.p

@app.route('about')
def about()
    return h1About Ush1pThis is the about page.p

if __name__ == '__main__'
    app.run(debug=True)
