from sanic import Blueprint, response
from crud import Shorten_url_exe

bp = Blueprint('shortenUrlBlueprint')

@bp.route("/POST/shorten")
async def on_post(request):
    url = "http://127.0.0.1:61949/browser"
    Shorten_url_exe(url=url)
    
    return response.html('<h1>Success</h1>')
        
@bp.route('/')
def index(request):
    return response.html('<h1>shortened url:</h1>')

    