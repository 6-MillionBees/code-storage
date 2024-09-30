from flask import Flask

app = Flask(__name__) # What does any of this mean? My brain is not ready

if __name__ == '__main__':
    app.run(debug=True, port=8000)