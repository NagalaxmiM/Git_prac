from sanic import Sanic
from sanic_cors import CORS
from git_blueprint import bp

app = Sanic(__name__)
CORS(app)
app.blueprint(bp)


app.run(debug=True)