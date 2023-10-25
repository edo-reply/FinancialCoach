from app import app

@app.route("/version")
def version():
    return "1.0"
