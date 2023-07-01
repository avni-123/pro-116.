# importing modules from flask library
from flask import Flask , render_template

# creating instance of class Flask, by providing __name__ keyword as argument
app = Flask(__name__)

# write the routes using decorator functions
# default route or 'URL'
@app.route("/")
def home():

    name = "Avni Vig" # write your name
    age = "15 yrs" # write your age

    return render_template('index.html' , name = name , age = age)

# define the route to father webpage

@app.route('/father')
def dad():

    name = 'Gaurav Vig'
    age = '44 yrs'

    return render_template('father.html', name=name, age=age)

# define the route to mother webpage

@app.route('/mother')
def mom():

    name = 'Sumedha Vig'
    age = '40 yrs'

    return render_template('mother.html', name=name, age=age)

# define the route to friends webpage

@app.route('/sister')
def sis():

    name = 'Aarika Vig'
    age = '12 yrs'

    return render_template('sister.html', name=name, age=age)

# add other routes, if you want

# run the file
if __name__  ==  '__main__':
    app.run(debug=True)
