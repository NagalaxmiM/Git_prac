from sanic import Blueprint, response
from crud import Session
import requests
from models import Shorten_url
bp = Blueprint('shortenUrlBlueprint')

@bp.route("/POST/shorten")
async def on_post(request):
    url = request.form['url']
    link = Shorten_url(url=url)
    s.add(link)
    s.commit()
    
    return response.html('''<!DOCTYPE html>
<html>
<
  <head>
    <title>Shortened url info</title>
  </head>
  <body>
  
    <p>{url:{{ Shorten_url.url }}, short_url:{{ Shorten_url.short_url}}, id:{{ Shorten_url.id}},success: True}</p>
                        
                        
  </body>
</html>''')
        
@bp.route('/')
def index(request):
    return response.html('''<!DOCTYPE html>
<html>

<head>
   <title>URL Shortener Service</title>
</head>

<body>
    <form method="POST" action="{{url_for(bp.on_post)}}">
	    <div class = "field">
		    <label class = "label">Original URL</label>
			<div class = "control">
			    <input class = "input" type="text" name = "url">
				<input type='submit' value="Submit">
		    </div>
	</form>
</body>
</html>''')

    