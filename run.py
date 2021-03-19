"""Routes for the course resource.
"""

"""
-------------------------------------------------------------------------
Challenge general notes:
-------------------------------------------------------------------------

1. Bonus points for returning sensible HTTP codes from the API routes
2. Bonus points for efficient code (e.g. title search)
"""

from flask import Flask
import data
from flask import Flask, render_template, request
app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template("index.html")

# Import the API routes
from routes.course import *



if __name__ == '__main__':
    print("Loading data", end=" ")
    data.load_data()
    print("... done")
    app.run(debug=True)
