from sanic import Sanic, response

app = Sanic(__name__)

@app.route("/", methods = ['POST'])
def index(request):
    url=request.json['url']
    return response.text(url)
    