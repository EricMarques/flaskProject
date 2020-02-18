from flask import Flask, render_template

app = Flask(__name__)

all_posts = [
    {
        'title': 'Post 1',
        'content': 'This is the content of post 1',
        'author': 'Eric Marques'
    },
    {
        'title': 'Post 2',
        'content': 'This is the content of post 2',
        'author': 'Talía Brasil'
    },
    {
        'title': 'Post 3',
        'content': 'This is the content of post 3'
    },
]

@app.route('/index')
def index():
    return render_template('index.html')

@app.route('/posts')
def posts():
    return render_template('posts.html', posts=all_posts)

@app.route('/home/users/<string:name>/posts/<int:id>')
def hello(name, id):
    return  "Rélou Uordi, " + name + " => " + str(id)

@app.route('/onlyGet', methods=['GET'])
def onlyGet():
    return 'You can only "get" this webpage. 4'

if __name__ == "__main__":
    app.run(debug=True)