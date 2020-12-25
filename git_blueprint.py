from sanic import Blueprint, response

import requests
bp = Blueprint("git_blueprint")

@bp.route("/external/GitHub/users/homepage")
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
        #print(details_json)
        details_html = response.json(details_json)
        return response.empty()
    except:
        return response.json([{"error":["Internal Server Error!"]},{"status": 500}])