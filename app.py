from flask import Flask
import data

app = Flask(__name__)


@app.route('/')
def hello_world():
    return 'Hello World!'

# Import the API routes
from routes.course import *







if __name__ == '__main__':
    print("Loading data", end=" ")
    data.load_data()
    print("... done")
    app.run(debug=True)

    
