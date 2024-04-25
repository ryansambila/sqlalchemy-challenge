# Import the dependencies.
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine
import numpy as np
import pandas as pd
import sqlalchemy
from sqlalchemy import create_engine, func
import os
from flask import Flask, jsonify

#################################################
# Database Setup
os.chdir(os.path.dirname(os.path.realpath(__file__)))
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

Base = automap_base()

Base.prepare(engine, reflect=True)

# Save references to each table
Measurement = Base.classes.measurement
Station = Base.classes.station
#################################################



# Create our session (link) from Python to the DB
session = Session(engine)

#################################################
# Flask Setup
app = Flask(__name__)
#################################################

#################################################
# HTML Routes
#################################################
@app.route("/")
def home():   
    """List all available api routes."""
    html = "/api/v1.0/precipitation<br>"
    html += "/api/v1.0/stations<br>"
    html += "/api/v1.0/tobs<br>"
    html += "/api/v1.0/tstats/&lt;start&gt;<br>"
    html += "/api/v1.0/tstats/&lt;start&gt;&lt;end&gt;<br>"
    return html 


#################################################
# API Routes
#################################################


#################################################
# Run Flask
#################################################
if __name__ == "__main__":
    app.run(debug=True)


