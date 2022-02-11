from flask import Flask, render_template

# Create a flask instance
app = Flask(__name__)

# Create a route decorator
@app.route('/')
#def index():
#    return "<h1>Hello World!</h1>"

def index():
    context = {
        'title': 'Hello World!',
        'heading': 'This is the first mywebsite',
    }
    return render_template('index.html', context=context)
    
# localhost:5000/user/john
@app.route('/user/<name>')
#def user(name):
#    return "<h1>Hello {}.</h1>".format(name)
    
def user(name):
    context = {
        'name': name, 'strg': 'halo bosque..!!!',
    }
    return render_template('user.html', context=context)
    
# Create custom error page

# Invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404
    
# Internal server error
@app.errorhandler(500)
def page_not_found(e):
    return render_template('500.html'), 500










