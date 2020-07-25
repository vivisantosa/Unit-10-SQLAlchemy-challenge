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
engine = create_engine("sqlite:///hawaii.sqlite")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)
tables = Base.classes.keys()
# Create our session (link) from Python to the DB
session = Session(engine)

# Save reference to the table
Station = Base.classes.station
Measurement = Base.classes.measurement


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
        f"  /api/v1.0/precipitation <br/>"
        f"- To list weather stations in Hawaii, <br/>"
        f"  /api/v1.0/stations <br/>"
        f"- To query dates and temperature observations of the most active station for the last year of data, <br/>"
        f"  /api/v1.0/tobs <br/>"
        f"- To query tmax, tavg, and tmin for all dates from a given start_date (YYYY-MM-DD), <br/>"
        f"  /api/v1.0/start/<start> <br/>"
        f"- To query tmax, tavg, and tmin for a start_date (YYYY-MM-DD) to end_date (YYYY-MM-DD) range of days, <br/>"
        f"  /api/v1.0/range/<begin>/<end> <br/>"
    )

#################################################
# Static Flask Apps
#################################################

### Precipitation ###
"""Return a list of the last 12 months of precipitation data"""

@app.route("/api/v1.0/precipitation")
def precipitation():
    # Create our session (link) from Python to the DB
    session = Session(engine)
    
    # indentify the date that will give a year of precipitation data
    LastDate = (session.query(func.max(Measurement.date)).first())
    PrevYrDate = dt.datetime.strptime(LastDate[0], '%Y-%m-%d') - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    prcp_results = session.query(Measurement.date, Measurement.station, Measurement.prcp).\
            filter(Measurement.date >= PrevYrDate).all()
    session.close()

    return jsonify(prcp_results)


### Stations ###
"""Return a list of stations from the dataset."""

@app.route("/api/v1.0/stations")
def stations():
    # Query all stations
    session = Session(engine)
    st_results = session.query(Station.station, Station.name).all()
    session.close()

    return jsonify(st_results)


### TOBS ###
"""Return a list of temperature observations (TOBS) for the last 12 months of data."""

@app.route("/api/v1.0/tobs")
def tobs():
    # Create our session (link) from Python to the DB
    session = Session(engine)

    # indentify the date that will give a year of precipitation data
    LastDate = (session.query(func.max(Measurement.date)).first())
    PrevYrDate = dt.datetime.strptime(LastDate[0], '%Y-%m-%d') - dt.timedelta(days=365)

    # Perform a query to retrieve the data and precipitation scores
    tobs_results = session.query(Measurement.date, Measurement.tobs).\
            filter(Measurement.station == "USC00519281").filter(Measurement.date >= PrevYrDate).all()
    session.close()

    return jsonify(tobs_results)


#################################################
# Dynamic Flask Apps
#################################################
    
### START ###
"""Return a list of TMIN, TAVG, and TMAX for all dates greater than and equal to the start date."""

@app.route("/api/v1.0/start/<start>")
def start(start):
    
    # Perform a query to retrieve temperature data
    session = Session(engine)
    tobs_ls1 = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
            filter(Measurement.date >= start).all()
    session.close()

    print("vivi here")
    print(tobs_ls1)

    return jsonify(tobs_ls1)

    
### RANGE ###
"""Return a list of TMIN, TAVG, and TMAX for all dates within the range of to the start and end date."""

@app.route("/api/v1.0/range/<begin>/<end>")
def range(begin, end):

    # Perform a query to retrieve temperature data
    session = Session(engine)
    tobs_ls1 = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).\
        filter(Measurement.date >= begin).filter(Measurement.date <= end).all()
    session.close()

    print("vivi here")
    print(tobs_ls1)

    return jsonify(tobs_ls1)


if __name__ == '__main__':
    app.run(debug=True)
