from sanic import Blueprint, response
from models import Shorten_url
from crud import Session
import json 
bp = Blueprint('shortenUrlBlueprint')

@bp.route("/shorten", methods=['POST'])  
async def on_post(request): 
    s = Session()
    url_dict = request.json
    
    #checking if the entered url is already in the database, if yes return already created short_url
    if s.query(Shorten_url).filter_by(url=url_dict['url'] is not None):
        short_url = s.query(Shorten_url).filter_by(url=url_dict['url']).short_url
        id = s.query(Shorten_url).filter_by(url=url_dict['url']).id
        s.close()
        return response.json({"url": url_dict['url'], "shortUrl": short_url, "id": id, "success": "true"})
    else:
        link = Shorten_url(url=url_dict['url'])
        s.add(link)
        s.commit()
        short_url = s.query(Shorten_url).filter_by(url=url_dict['url']).short_url
        id = s.query(Shorten_url).filter_by(url = url_dict['url']).id
        s.close()
        return response.json({"url": url_dict['url'], "shortUrl": short_url, "id": id, "success": "true"})
    

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
    