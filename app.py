
from flask import Flask, render_template
from data import Articles

app = Flask(__name__)
app.debug=True


@app.route ('/')
# @app.route ('/data', methods=['GET','POST']) #경로지정, 'local host:5000/data'로 요청이 오면 반응
def index():
    print("success")
    # return "test"
    return render_template('home.html',hello='Garykim') #text값을 html문서로 반환

@app.route ('/about')
def about():
    print("success")
    return render_template('about.html',hello='Garykim')

@app.route ('/articles')
def articles():
    print("success")
    articles=Articles()
    print(len(articles))
    return render_template('articles.html',articles=articles)


if __name__=='__main__':
    app.run()
#    app.run(host='0.0.0.0',port='8080')


