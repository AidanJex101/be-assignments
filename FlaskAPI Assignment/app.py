# In app.py

from flask import Flask

from routes.products_read import product

app = Flask(__name__)

app.register_blueprint(product)

if __name__ == '__main__':
  app.run(port='8086', host='0.0.0.0')