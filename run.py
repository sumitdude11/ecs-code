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

@app.route('/check',methods=['POST'])
def check1():
    print("hello ")
    d1 = str(request.form["n1"])

    #print(d1)

    #for database

    #for csv
    import csv
    filename = "ecs_data2.csv"
    fields = []
    rows = []


    with open(filename,'r',encoding="utf8") as csvfile:
        csvreader = csv.reader(csvfile)
        fields.append(next(csvreader))
        for row2 in csvreader:
            if(d1 in row2[8]):
                rows.append(row2)



    return render_template("page2.html",data=rows)

if __name__ == '__main__':
    print("Loading data", end=" ")
    data.load_data()
    print("... done")
    app.run(debug=True)
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

@app.route('/check',methods=['POST'])
def check1():
    print("hello ")
    d1 = str(request.form["n1"])

    #print(d1)

    #for database

    #for csv
    import csv
    filename = "ecs_data2.csv"
    fields = []
    rows = []


    with open(filename,'r',encoding="utf8") as csvfile:
        csvreader = csv.reader(csvfile)
        fields.append(next(csvreader))
        for row2 in csvreader:
            if(d1 in row2[8]):
                rows.append(row2)



    return render_template("page2.html",data=rows)

if __name__ == '__main__':
    print("Loading data", end=" ")
    data.load_data()
    print("... done")
    app.run(debug=True)
