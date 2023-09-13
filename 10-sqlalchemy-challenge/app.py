import numpy as np
import datetime as dt
import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
from flask import Flask, jsonify


# Database Setup
database_path = "Resources/hawaii.sqlite"
engine = create_engine("sqlite:///{database_path}")

# reflect an existing database into a new model
Base = automap_base()

# reflect the tables
Base.prepare(engine, reflect=True)

# Save reference to the table
Measurement = Base.classes.measurement
Station = Base.classes.station



# Design Climate App

#################################################

# Flask Setup
app = Flask(__name__)

# Flask Routes
@app.route("/")
def welcome():
    
    return (
        f'<br/>'
        f'<br/>'
        f'<br/>'
        f'<br/>'
        f'<br/>'
        f'<br/>'
        f'<br/>'
        f'<br/>'
        f'<h1 style="text-align:center">Welcome to the Surfs_Up API!<br/></h1>'
        f'<h2 style="text-align:center">Available Routes (Clickable):<br/></h2>'
        f'<h3 style="text-align:center"><a href="/api/v1.0/precipitation">api/v1.0/precipitation</a><br/></h3>'
        f'<h3 style="text-align:center"><a href="/api/v1.0/stations">api/v1.0/stations</a><br/></h3>'
        f'<h3 style="text-align:center"><a href="/api/v1.0/tobs">api/v1.0/tobs</a><br/></h3>'
        f'<h3 style="text-align:center"><a href="/api/v1.0/2015-03-14">(Start Date)</a><br/></h3>'
        f'<h3 style="text-align:center"><a href="/api/v1.0/2011-03-14/2015-03-28">(End Date)</a><br/></h3>'
        
    )


# Precipitation
    # 1. Convert the query results to a dictionary using date as the key and prcp as the value.
    # 2. Return the JSON representation of your dictionary.

@app.route("/api/v1.0/precipitation")
def prcp_date():
    session = Session(engine)
    res=session.query(Measurement.date, Measurement.prcp)
    session.close()

    result=[]
    for date,prcp in res:
        prcp_dict={}
        prcp_dict["date"]=date
        prcp_dict["prcp"]=prcp
        result.append(prcp_dict)
    return jsonify(result)


# Stations
    # 1. Return a JSON list of stations from the dataset.

@app.route("/api/v1.0/stations")
def station_list():
    session = Session(engine)
    res=session.query(Station.name).all()
    session.close()
    all_names = list(np.ravel(res))
    
    return jsonify(all_names)

#tobs
    # 1. Query the dates and temperature observations of the most active station for the last year of data.
    # 2. Return a JSON list of temperature observations (TOBS) for the previous year.

@app.route("/api/v1.0/tobs")
def tob():
    session = Session(engine)
    most_recent_date=dt.datetime.strptime(session.query(Measurement.date).order_by(Measurement.date.desc()).first()[0], '%Y-%m-%d')
    last_12_months=most_recent_date - dt.timedelta(days=365)
    last_12_months=last_12_months.date()

    most_active_station = session.query(Measurement.station).filter(Measurement.date >= last_12_months)\
        .group_by(Measurement.station).order_by(func.count(Measurement.station).desc()).first()[0] 

    TOBS_ =session.query(Measurement.tobs).filter(Measurement.station == most_active_station).all()
    session.close()
    TOBS = list(np.ravel(TOBS_))
    return jsonify(TOBS)



# /api/v1.0/<start> and /api/v1.0/<start>/<end>
    # 1. Return a JSON list of the minimum temperature, the average temperature, and the maximum temperature for a given start or start-end range.
    # 2. When given the start only, calculate TMIN, TAVG, and TMAX for all dates greater than or equal to the start date.
    # 3. When given the start and the end date, calculate the TMIN, TAVG, and TMAX for dates from the start date through the end date


@app.route("/api/v1.0/<start>")
def start_day(start):
    session = Session(engine)
    query_ = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start).all()
    start_list=list(np.ravel(query_))
    session.close()
    return jsonify(start_list)

@app.route("/api/v1.0/<start>/<end>")
def start_end_day(start,end):
    session = Session(engine)
    query_ = session.query(func.min(Measurement.tobs), func.avg(Measurement.tobs), func.max(Measurement.tobs)).filter(Measurement.date >= start,Measurement.date<= end).all()
    start_list=list(np.ravel(query_))
    session.close()
    return jsonify(start_list)        



if __name__ == '__main__':
    app.run(debug=True)