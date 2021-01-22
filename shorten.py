from sanic import Blueprint, response
from models import ShortenUrl, Session
from sqlalchemy.orm import sessionmaker
import json 
from urllib.parse import urlencode
bp = Blueprint('shorten url blueprint')

@bp.route("/shorten", methods=['POST'])  
async def onPost(request): 
    s = Session()
    urlDict = request.json
    
    if s.query(ShortenUrl).filter_by(url=urlDict['url']).first() == None:
        link = ShortenUrl(url=urlDict['url'])
        s.add(link)
        s.commit()
        shortUrl = s.query(ShortenUrl).filter_by(url=urlDict['url']).first().shortUrl
        id = s.query(ShortenUrl).filter_by(url = urlDict['url']).first().id
        s.close()
        return response.json({"url": urlDict['url'], "short url": shortUrl, "id": id, "success": "true"})

    else:
        shortUrl = s.query(ShortenUrl).filter_by(url=urlDict['url']).first().shortUrl
        id = s.query(ShortenUrl).filter_by(url=urlDict['url']).first().id
        s.close()
        return response.json({"url": urlDict['url'], "short url": shortUrl, "id": id, "success": "true"})

@bp.route("/shorten/<id>", methods = ['DELETE'])
async def on_delete(request,id):
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
async def on_get(request,shortUrl):
    s = Session()
    try:
        actual_url = s.query(ShortenUrl).filter_by(shortUrl=shortUrl).first().url
        s.commit()
        return response.json({"success": "true", "url":actual_url })
    except:
        return response.text("Invalid SHORT URL !!")
    finally:
        s.close()
    