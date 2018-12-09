from flask import Flask, render_template

#create an instance of the flask app.
app = Flask(__name__)

@app.route('/')
def index():
    """Homepage."""
    return render_template('index.html')

if __name__ == "__main__":
    #set to True for debugging
    #set to False for production
    app.debug = True

    app.run(host="0.0.0.0")
