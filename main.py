from flask import Flask, request, render_template
import pickle

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('plantindex.html')

@ app.route('/Detail')
def Detail():
    return render_template('Detail.html')
    
if __name__ == "__main__":
    app.run(debug=True)
