from sanic import Blueprint, response
from models import Shorten_url
from crud import Session

bp = Blueprint('shortenUrlBlueprint')

@bp.route("/POST/shorten", methods=['POST', 'GET'])
async def on_post(request):
    s = Session()
    if s.query(Shorten_url).filter_by(url=request.json['url']).first().url:
        short_url = s.query(Shorten_url).filter_by(url=request.json['url']).first().short_url
        id = s.query(Shorten_url).filter_by(url=request.json['url']).first().id
        s.close()
        return response.json({"url": request.json['url'], "shortUrl": short_url, "id": id, "success": "true"})
    link = Shorten_url(url=request.json['url'])
    s.add(link)
    s.commit()
    short_url = s.query(Shorten_url).filter_by(url=request.json['url']).first().short_url
    id = s.query(Shorten_url).filter_by(url=request.json['url']).first().id
    s.close()
    return response.json({"url": request.json['url'], "shortUrl": short_url, "id": id, "success": "true"})

@bp.route("/DELETE/shorten/<id>")
async def on_delete(request,id):
    s = Session()
    try:
        to_be_deleted = s.query(Shorten_url).filter_by(id=id).first()
        s.delete(to_be_deleted)
        s.commit()
    except:
        return response.text("Invalid ID!")
    finally:
        s.close()
    return response.json({"success": "true"})

@bp.route("/GET/<short_url>")
async def on_get(request,short_url):
    s = Session()
    try:
        actual_url = s.query(Shorten_url).filter_by(short_url=short_url).first().url
        return response.json({"success": "true", "url":actual_url })
    except:
        return response.text("Invalid SHORT URL !!")
    finally:
        s.close()
    