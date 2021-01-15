from sanic import Sanic
from shorten import bp

app = Sanic(__name__)

app.blueprint(bp)

if __name__=="__main__":
    app.run(debug=True)