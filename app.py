#################################################
# STEP 2 : CLIMATE APP
#################################################

#################################################
# Import Dependencies
#################################################
import numpy as np
import pandas as pd
import datetime as dt

import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func

from flask import Flask, jsonify

#################################################
# Database Setup
#################################################
engine = create_engine("sqlite:///Resources/hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Create our session (link) from Python to the DB
session = Session(engine)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station

#################################################
# Flask Setup
#################################################
app = Flask(__name__)


#################################################
# Flask Routes
#################################################

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"- To query precipitation of a certain previous year date, <br/>"
        f"  /api/v1.0/precipitation"
        f"- To list weather stations in Hawaii, <br/>"
        f"  /api/v1.0/stations"
        f"- To query dates and temperature observations of the most active station for the last year of data, <br/>"
        f"  /api/v1.0/tobs"
        f"- To query tmax, tavg, and tmin for all dates from a given start_date (YYYY-MM-DD), <br/>"
        f"  /api/v1.0/<start>"
        f"- To query tmax, tavg, and tmin for a start_date (YYYY-MM-DD) to end_date (YYYY-MM-DD) range of days, <br/>"
        f"  /api/v1.0/<start>/<end>"
    )

#################################################
# Flask Apps
#################################################

### Precipitation ###
"""Return a list of the last 12 months of precipitation data"""

@app.route("/api/v1.0/precipitation")
def precipitation():
    # indentify the date that will give a year of precipitation data
    LastDate = (session.query(func.max(Measurement.date)).first())
    PrevYrDate = dt.datetime.strptime(LastDate[0], '%Y-%m-%d') - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    prcp_results = session.query(Measurement.date, Measurement.station, Measurement.prcp).\
            filter(Measurement.date >= PrevYrDate).all()
    session.close()

    # Convert list of tuples into normal list
    prcp_list = list(np.ravel(prcp_results))

    return jsonify(prcp_list)


### Stations ###
"""Return a list of stations from the dataset."""

@app.route("/api/v1.0/stations")
def stations():
    # Query all stations
    st_results = session.query(Station.station, Station.name).all()
    session.close()
    # Convert list of tuples into normal list
    st_list = list(np.ravel(st_results))

    return jsonify(st_list)


### TOBS ###
"""Return a list of temperature observations (TOBS) for the last 12 months of data."""

@app.route("/api/v1.0/tobs")
def tobs():
    # indentify the date that will give a year of precipitation data
    LastDate = (session.query(func.max(Measurement.date)).first())
    PrevYrDate = dt.datetime.strptime(LastDate[0], '%Y-%m-%d') - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    tobs_results = session.query(Measurement.date, Measurement.tobs).\
            filter(Measurement.station == "USC00519281").filter(Measurement.date >= PrevYrDate).all()
    session.close()

    # Convert list of tuples into normal list
    tobs_list = list(np.ravel(tobs_results))

    return jsonify(tobs_list)

    
### START ###
"""Return a list of TMIN, TAVG, and TMAX for all dates greater than and equal to the start date."""

@app.route("/api/v1.0/start")
def start(start=None):
    # Get input start data
    Start_date = "2016-11-11"
    
    # Query all passengers
    # Perform a query to retrieve temperature data
    tobs_ls1 = session.query(Measurement.date, Measurement.tobs).\
            filter(Measurement.date >= Start_date).all()
    session.close()

    # calculate temperature normals (Tmax,Tavg,Tmin)
    tobs_df = pd.DataFrame(tobs_ls1)

    Tavg = tobs_df["tobs"].mean()
    Tmax = tobs_df["tobs"].max()
    Tmin = tobs_df["tobs"].min()

    return jsonify(Tmax,Tavg,Tmin)


if __name__ == '__main__':
    app.run(debug=True)
