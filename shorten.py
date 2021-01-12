from sanic import Blueprint, response
from models import Shorten_url
from crud import Session
import json 
bp = Blueprint('shortenUrlBlueprint')

@bp.route("/generate_url/<url_dict>", methods=['POST','GET'])  
async def gen_url(request, url_dict): 
    s = Session()
    
    if s.query(Shorten_url).filter_by(url=url_dict).first().url:
        short_url = s.query(Shorten_url).filter_by(url=url_dict).first().short_url
        id = s.query(Shorten_url).filter_by(url=url_dict).first().id
        s.close()
        return response.json({"url": url_dict, "shortUrl": short_url, "id": id, "success": "true"})
    
    link = Shorten_url(url=url_dict)
    s.add(link)
    s.commit()
    short_url = s.query(Shorten_url).filter_by(url=url_dict).first().short_url
    id = s.query(Shorten_url).filter_by(url = url_dict).first().id
    s.close()
    return response.json({"url": url_dict, "shortUrl": short_url, "id": id, "success": "true"})


@bp.route("/POST/shorten", methods=['POST','GET'])
async def on_post(request):
    data = request.body
    url_string = data.decode('utf-8').replace("'", '"')
    url_dict = json.loads(url_string)
    return response.redirect('/generate_url/<url_dict>',url_dict['url'] )

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
    