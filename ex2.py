from bootstrap import bootstrap3, container
from htmler.fun import h1

from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    try:
        return bootstrap3(container(h1('Hello, world!')))
    except:
        import ipdb; ipdb.set_trace() # BREAKPOINT



if __name__ == "__main__":
    app.run()

