from bootstrap import bootstrap3, container
from htmler.fun import h1

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return bootstrap3(container(h1('Hello, world!')))



if __name__ == "__main__":
    app.run()

