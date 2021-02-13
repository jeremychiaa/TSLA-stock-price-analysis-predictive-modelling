import sqlalchemy
from sqlalchemy.ext.automap import automap_base
from sqlalchemy.orm import Session
from sqlalchemy import create_engine, func
import os
from flask import Flask, jsonify
from flask import Flask, render_template

# Database setup

database_path = "./sqlite_db/stock_market_sqlite.db"
engine = create_engine(f"sqlite:///{database_path}")

# reflect an existing database into a new model
Base = automap_base()
# reflect the tables
Base.prepare(engine, reflect=True)

# Save references to each table
Tesla = Base.classes.tesla

# Flask set up and routes

app = Flask(__name__)

@app.route("/")
def home():
    return render_template("index.html")

@app.route("/")
def welcome():
    """List all available api routes."""
    return (
        f"Available Routes:<br/>"
        f"/api/v1.0/tsla<br/>"
        f"/api/v1.0/msft<br/>"
        f"/api/v1.0/gme<br/>"
    )

@app.route("/api/v1.0/tsla-actual")
def tsla():
    # Create session from Python to database
    session = Session(engine)
    
    """Return all TSLA stock market info"""
    results = engine.execute("SELECT * FROM TSLA").fetchall()
    session.close()
    
    # Create a dictionary from the row data and append to a list of Tesla stock
    tsla_stock = []
    for date, open, high, low, close, adj_close, volume in results:
        tsla_dict = {}
        tsla_dict["date"] = date
        tsla_dict["open"] = open
        tsla_dict["high"] = high
        tsla_dict["low"] = low
        tsla_dict["close"] = close
        tsla_dict["adj_close"] = adj_close
        tsla_dict["volume"] = volume
        tsla_stock.append(tsla_dict)

    
    return jsonify(tsla_stock)

@app.route("/api/v1.0/msft")
def msft():
    # Create session from Python to database
    session = Session(engine)
    
    
    """Return all MSFT stock market info"""
    results = engine.execute("SELECT * FROM MSFT").fetchall()
    session.close()
    
    # Create a dictionary from the row data and append to a list of Microsoft stock
    msft_stock = []
    for date, open, high, low, close, adj_close, volume in results:
        msft_dict = {}
        msft_dict["date"] = date
        msft_dict["open"] = open
        msft_dict["high"] = high
        msft_dict["low"] = low
        msft_dict["close"] = close
        msft_dict["adj_close"] = adj_close
        msft_dict["volume"] = volume
        msft_stock.append(msft_dict)
        
    return jsonify(msft_stock)

@app.route("/api/v1.0/gme")
def gme():
    # Create session from Python to database
    session = Session(engine)
    
     
    """Return all GME stock market info"""
    results = engine.execute("SELECT * FROM GME").fetchall()
    session.close()
    
    # Create a dictionary from the row data and append to a list of GameStop stock
    gme_stock = []
    for date, open, high, low, close, adj_close, volume in results:
        gme_dict = {}
        gme_dict["date"] = date
        gme_dict["open"] = open
        gme_dict["high"] = high
        gme_dict["low"] = low
        gme_dict["close"] = close
        gme_dict["adj_close"] = adj_close
        gme_dict["volume"] = volume
        gme_stock.append(gme_dict)
        
    return jsonify(gme_stock)

if __name__ == '__main__':
    app.run(debug=True)