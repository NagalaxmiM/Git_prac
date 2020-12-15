from sanic import Sanic
from blue_print import bp

app = Sanic(__name__)
app.blueprint(bp)


app.run(debug=True)
