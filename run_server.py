# USAGE
# Start the server:
# 	python run_server.py
# Submit a request via cURL:
# 	curl -X POST -F image=@dog.jpg 'http://localhost:5000/predict'
# Submit a request via Python:
#	python simple_request.py

# import the necessary packages
import numpy as np
import dill
import pandas as pd
import flask

# initialize our Flask application and the model
app = flask.Flask(__name__)


@app.route("/", methods=["GET"])
def general():
    return "Welcome to a prediction process"


@app.route("/predict", methods=["POST"])
def predict():
    # initialize the data dictionary that will be returned from the
    # view
    data = {"success": False}

    # ensure an image was properly uploaded to our endpoint
    if flask.request.method == "POST":
        duration, contact, poutcome = "", "", ""
        request_json = flask.request.get_json()
        if request_json["duration"]:
            duration = request_json['duration']
        if request_json["contact"]:
            contact = request_json['contact']
        if request_json["poutcome"]:
            poutcome = request_json['poutcome']

        preds = model.predict_proba(pd.DataFrame({"duration": [duration],
                                                  "contact": [contact],
                                                  "poutcome": [poutcome]}))
        data["predictions"] = preds[:, 1][0]
        data["duration"] = duration
        # indicate that the request was a success
        data["success"] = True

    # return the data dictionary as a JSON response
    return flask.jsonify(data)


# if this is the main thread of execution first load the model and
# then start the server
if __name__ == "__main__":
    print(("* Loading the model and Flask starting server..."
           "please wait until server has fully started"))
    model_path = 'app/models/catboost_pipeline.dill'
    with open(model_path, 'rb') as f:
        model = dill.load(f)
    app.run()
