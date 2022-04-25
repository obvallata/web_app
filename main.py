from flask import Flask, url_for, request, render_template

app = Flask(__name__)


@app.route('/')
def main_page():
    return render_template('main.html', text='May be it will make you happy')


@app.route("/carousel")
def carousel():
    return render_template('carousel.html')


@app.route('/loadim', methods=['POST', 'GET'])
def sample_file_upload():
    if request.method == 'GET':
        return render_template('load.html')
    elif request.method == 'POST':
        f = request.files['file']
        if os.getcwd()[-11:] != "/static/img":
            os.chdir("./static/img")
        out = open("img.jpg", "wb")
        out.write(f.read())
        out.close()
        return render_template('load.html')


if __name__ == "__main__":
    app.run(host='127.0.0.1', port=8089)
