from flask import Flask, render_template
# import requests, json

app = Flask(__name__, template_folder='templates')

@app.route("/")
def index():
    data = {'username': 'rammanoj', 'auth': True}
    return render_template('index.html', data=data)


@app.route("/home")
def home():
    return render_template('home.html')



if __name__ == "__main__":
    app.run(host='0.0.0.0', port='8080', debug=True)
