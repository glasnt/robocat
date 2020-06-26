from flask import Flask, send_file
import io
from robohash import Robohash

app = Flask(__name__)

@app.route("/<uuid>")
def cat(uuid):
    rh = Robohash(uuid)
    rh.assemble(roboset='set4') #🐱
    fakefile = io.BytesIO()
    rh.img.save(fakefile,format='PNG')
    fakefile.seek(0)
    return send_file(fakefile, mimetype="image/png")


@app.route("/")
def hello():
    return "Give me a string. E.g. <a href='/cat'>/cat</a>.<br> Powered by <a href='https://github.com/e1ven/Robohash'>robohash</a>"


if __name__ == "__main__":
    app.run(host="localhost", port=8080, debug=True)
