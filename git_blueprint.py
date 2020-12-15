from sanic import Blueprint, response
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
        print(details_json)
        return response.json(details_json) 
    except:
        return response.text("Server down . Try again after sometime...")

