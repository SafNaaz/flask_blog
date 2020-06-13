from flask import Flask, render_template
app = Flask(__name__)

posts = [
    {
        'author':'Safnas',
        'title':'Blog Post',
        'content':'First Blog Post',
        'date_posted':'June 13, 2020'
    },
    {
        'author':'Safnas',
        'title':'Blog Post 2',
        'content':'Second Blog Post',
        'date_posted':'June 15, 2020'
    }
]

@app.route('/')
@app.route('/home')
def home():
    return render_template('home.html', posts=posts)

@app.route('/about')
def about():
    return render_template('about.html')

if __name__ == '__main__':
    app.run(debug=True)