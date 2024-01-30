from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

from pymongo import MongoClient
client = MongoClient('mongodb+srv://spart:test@cluster0.taz7xeo.mongodb.net/Cluster0?retryWrites=true&w=majority')
db = client.dbsparta

@app.route('/')
def home():
   return render_template('index.html')

@app.route("/website", methods=["POST"])
def website_post():
    cord_receive = request.form['code_give']
    lang_receive = request.form['lang_give']
    overview_receive = request.form['overview_give']
    img_receive = request.form['img_give']

    doc = {
        'cord':cord_receive,
        'lang':lang_receive,
        'overview': overview_receive,
        'img': img_receive
    }
    db.cord.insert_one(doc)
    return jsonify({'msg': '保存完了!'})

@app.route("/website", methods=["GET"])
def website_get():
    all_cords = list(db.cord.find({}, {'_id': False}))
    return jsonify({'result': all_cords})

if __name__ == '__main__':
   app.run('0.0.0.0', port=5000, debug=True)