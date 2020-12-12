from sanic import Sanic, response
import requests
app = Sanic(__name__)

@app.route("/external/GitHub/users")
async def on_post(request):
    my_list = []
    d = dict()
    data = requests.get('https://api.github.com/users?per_page=10').json()
    for i in data:
        d = dict()
        for key,value in i.items():
            if key in ['id','login','url']:
                d.update({key:value})
        my_list.append(d)
        del d
    print(my_list)
    return response.json(my_list)    
if __name__ == "__main__":
    app.run(host = '192.168.43.9',debug=True)
