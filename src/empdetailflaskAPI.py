import pandas as pd
import json
from flask import Flask, request, jsonify
import logging

# Create and configure logger
logging.basicConfig(filename="logfile.log",
                    format='%(asctime)s %(message)s',
                    filemode='w')

# Creating an object
logger = logging.getLogger()

# Setting the threshold of logger to DEBUG
logger.setLevel(logging.DEBUG)

app = Flask(__name__)

@app.route('/empdetails', methods=['GET'])
def empdetails():
    logger.info("Reading data from csv file")
    df = pd.read_csv("data.csv")  
    json_data = df.to_json(orient='records', lines=True)
    logger.info("Data from csv file")
    return json_data

app.run(debug=True)
