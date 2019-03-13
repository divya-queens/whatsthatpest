import os
from flask import Flask
app = Flask(__name__)

@app.route('/')
def Welcome():
    return "Hello World!"

#This sets that we want to use local host 'your #port' for this call
port = os.getenv('PORT', '5021')

#This starts the web server if we are on the correct webpage
#If true, this starts the app with debugging at the correct port
if __name__ == "__main__":
        app.run(host='127.0.0.1', port=int(port), debug=True)