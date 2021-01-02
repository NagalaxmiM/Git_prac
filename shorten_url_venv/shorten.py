from sanic import Blueprint, response
from models import Shorten_url
from crud import Session

bp = Blueprint('shortenUrlBlueprint')

@bp.route("/POST/shorten")
async def on_post(request):
    url = "http://127.0.0.1:61949/browser"
    Shorten_url(url=url)
    return response.html('<h1>Success</h1>')

@bp.route("DELETE/shorten/<id>")
async def on_delete(request,id):
    s = Session()
    to_be_deleted = s.query(Shorten_url).filter_by(id=id).first()
    s.delete(to_be_deleted)
    s.commit()
    return response.html("<h1>Deleted</h1>")

@bp.route("GET/<short_url>")
async def on_get(request,short_url):
    s = Session()
    actual_url = s.query(Shorten_url).filter_by(short_url=short_url).first().url
    return response.text(actual_url)
    