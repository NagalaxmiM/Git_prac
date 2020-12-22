from sanic import Blueprint, response
from pandas import DataFrame
import requests
bp = Blueprint("git_blueprint")

@bp.route("/external/GitHub/users")
async def on_post(request):
    try:
        details_json = []
        data = requests.get('https://api.github.com/users?per_page=10').json()
        for evey_user in data:
            user_details = dict()
            for key,value in evey_user.items():
                if key in ['id','login','url']:
                    user_details.update({key:value})
            details_json.append(user_details)
            del user_details
        
        df =  DataFrame(details_json)
        df = df.set_index("id")
        return response.html(df.to_html())
    except:
        return response.html("<h1>500-Internal server Error</h1>")