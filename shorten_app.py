from sanic import Sanic
from shorten import bp

app = Sanic(__name__)

app.blueprint(bp)
app.run(debug=True)