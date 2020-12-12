from sanic import Sanic, response

app = Sanic(__name__)

#app.blue_print(my_bp)

@app.route("/external/GitHub/users", methods = ['GET','POST'])
def on_post(request):
    return response.redirect("https://api.github.com/users?per_page=10")

if __name__ == "__main__":
    app.run(debug=True)
    