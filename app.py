from sanic import Sanic
from git_blueprint import bp

app = Sanic(__name__)
app.blueprint(bp)


app.run(debug=True)