from flask import Flask, request, make_response, render_template
from score import scoring
from leaderboard import leaderboard,leaderboard_2
import os

UPLOAD_FOLDER = '/home/slm/web/files'
ALLOWED_EXTENSIONS = {'csv'}

app = Flask(__name__)
app.config["DEBUG"] = False
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER


def allowed_file(filename):
    return '.' in filename and \
           filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS


@app.route("/", methods=["GET", "POST"])
def main_page():
    return render_template("jszn.html")


@app.route('/result',methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        input_file = request.files["input_file"]
        if input_file and allowed_file(input_file.filename):
            input_file.save(os.path.join(app.config['UPLOAD_FOLDER'], input_file.filename))
            file_path = os.path.join(app.config['UPLOAD_FOLDER'], input_file.filename)
            score = scoring(file_path,label_file='/home/slm/web/label_result.csv')
            if not score:
                return render_template("wrong_submittion.html")
            elif(score=="Warning"):
                return render_template("warning.html")
            else:
                return render_template("result.html",score = score)


@app.route('/board',methods=['POST',"GET"])
def board():
    results = leaderboard()
    return render_template("leaderboard.html",results = results)

@app.route('/privateboard',methods=['POST',"GET"])
def privateboard():
    results = leaderboard_2()
    return render_template("leaderboard.html",results = results)

@app.route('/wrong_sub',methods=['POST',"GET"])
def wrong_sub():
    results = leaderboard()
    return render_template("wrong_submittion.html")

if __name__ == '__main__':
    app.run(host='0.0.0.0',threaded=True)