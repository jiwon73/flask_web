
from flask import Flask, render_template

app = Flask(__name__)
app.debug=True

@app.route ('/data') #경로지정, 'local host:5000/data'로 요청이 오면 반응
def index():
    print("success")
    # return "test"
    return render_template('home.html') #text값을 html문서로 반환


if __name__=='__main__':
    app.run()
#    app.run(host='0.0.0.0',port='8080')


