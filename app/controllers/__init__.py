from app import app


@app.route("/api/version")
def version():
    return "1.0"
