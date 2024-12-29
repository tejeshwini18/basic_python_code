from flask import Flask
app = Flask(__name__)

@app.route("/home",methods=['GET'])
def home():
    data = {'message':"Hello,Welcome to my flask web application"}
    return data

if __name__ == '__main__':
    app.run(debug=True)