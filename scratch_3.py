from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
@app.route('/about')
def about():
    name='flask'
    return render_template('about.html',name2=name)

if (__name__ == "__main__"):
    app.run(debug=True)
