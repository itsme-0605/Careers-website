from flask import Flask
#flask->module, Flask->class,app created below is->object
# name valriablemeans how the application is invoked
app = Flask(__name__)

#route is everything after domain name
@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"

#0.0.0.0->localserver, debug=True changes are saved
#if we are running this file as a script
if __name__=="__main__":
  app.run(host="0.0.0.0",debug=True)