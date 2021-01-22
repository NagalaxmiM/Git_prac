from sanic import Blueprint, response
from models import Shorten_url, Session
from sqlalchemy.orm import sessionmaker
import json 
from urllib.parse import urlencode
bp = Blueprint('shorten url blueprint')

@bp.route("/shorten", methods=['POST'])  
async def on_post(request): 
    s = Session()
    url_dict = request.json
    
    if s.query(Shorten_url).filter_by(url=url_dict['url']).first() == None:
        link = Shorten_url(url=url_dict['url'])
        s.add(link)
        s.commit()
        short_url = s.query(Shorten_url).filter_by(url=url_dict['url']).first().short_url
        id = s.query(Shorten_url).filter_by(url = url_dict['url']).first().id
        s.close()
        return response.json({"url": url_dict['url'], "short url": short_url, "id": id, "success": "true"})

    else:
        short_url = s.query(Shorten_url).filter_by(url=url_dict['url']).first().short_url
        id = s.query(Shorten_url).filter_by(url=url_dict['url']).first().id
        s.close()
        return response.json({"url": url_dict['url'], "short url": short_url, "id": id, "success": "true"})

@bp.route("/shorten/<id>", methods = ['DELETE'])
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

@bp.route("/<short_url>", methods = ['GET'])
async def on_get(request,short_url):
    s = Session()
    try:
        actual_url = s.query(Shorten_url).filter_by(short_url=short_url).first().url
        s.commit()
        return response.json({"success": "true", "url":actual_url })
    except:
        return response.text("Invalid SHORT URL !!")
    finally:
        s.close()
    