from sanic import Blueprint, response
from models import ShortenUrl, Session
from sqlalchemy.orm import sessionmaker
import json 
bp = Blueprint('shorten url blueprint')

@bp.route("/shorten", methods=['POST'])  
async def onPost(request): 
    s = Session()
    actualUrl = request.json
    
    if s.query(ShortenUrl).filter_by(url=actualUrl['url']).first() == None:
        link = ShortenUrl(url=actualUrl['url'])
        s.add(link)
        s.commit()
        shortUrl = s.query(ShortenUrl).filter_by(url=actualUrl['url']).first().shortUrl
        id = s.query(ShortenUrl).filter_by(url = actualUrl['url']).first().id
        s.close()
        return response.json({"url": actualUrl['url'], "short url": shortUrl, "id": id, "success": "true"})

    else:
        shortUrl = s.query(ShortenUrl).filter_by(url=actualUrl['url']).first().shortUrl
        id = s.query(ShortenUrl).filter_by(url=actualUrl['url']).first().id
        s.close()
        return response.json({"url": actualUrl['url'], "short url": shortUrl, "id": id, "success": "true"})

@bp.route("/shorten/<id>", methods = ['POST'])
async def onDelete(request,id):
    s = Session()
    try:
        toBeDeleted = s.query(ShortenUrl).filter_by(id=id).first()
        s.delete(toBeDeleted)
        s.commit()
    except:
        return response.text("Invalid ID!")
    finally:
        s.close()
    return response.json({"success": "true"})

@bp.route("/<shortUrl>", methods = ['GET'])
async def onGet(request,shortUrl):
    s = Session()
    try:
        shortUrl = shortUrl[8:]
        actual_url = s.query(ShortenUrl).filter_by(shortUrl=shortUrl).first().url
        return response.json({"success": "true", "url":actual_url })
    except:
        return response.text("Invalid SHORT URL !!")
    finally:
        s.close()
    