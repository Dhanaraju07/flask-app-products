from flask import Flask, render_template
import requests

app = Flask(__name__)

@app.route('/')
def index():
    api_url = 'https://dummyjson.com/products'
    response = requests.get(api_url)
    data = response.json().get('products', [])
    return render_template('home.html', products=data)

if __name__ == '__main__':
    app.run(debug=True)
