# import flask
from flask import Flask
import utils.response as response
import utils.database as db

# create server
server = Flask(__name__)

@server.route("/welcome")
def welcome():
    return response.create_response("iothackathon");

@server.route("/LM35", methods = {'GET'})
def temperature_methods():
    # to get data from database form a query
    query = f"select * from LM35;"

    # execute query to get all temps from database
    temps = db.execute_select_query(temps)

    # return temps into response
    return response.create_response(value)

    query = f"select * from LDR;"
    
    value = db.execute_select_query(query)

    return response.create_response(value)

# run server
server.run(debug=True)
