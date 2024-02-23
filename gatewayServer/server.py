# import flask
from flask import Flask, request
import utils.response as response
import utils.database as db

# create server
server = Flask(__name__)

@server.route("/welcome")
def welcome():
    return response.create_response("Welcome to Sunbeam Premise Monitoring  Application");

@server.route("/temperature", methods = {'GET', 'POST', 'PUT', 'DELETE'})
def temperature_methods():
    if (request.method == 'GET'):
        # to get data from database form a query
        query = f"select * from sensorsLog;"

        # execute query to get all temps from database
        temps = db.execute_select_query(query)

        # return temps into response
        return response.create_response(temps)
    elif(request.method == 'POST'):
        # retrieve data from request body
        value = request.get_json().get('value')
        loc = "kaveri"
        sen = "LM35"

        # insert data into database
        query = f"insert into sensorsLog(location, sensor, value) values(\"{loc}\", \"{sen}\", {value});"
        db.execute_query(query)
        print(query)

        # return some response to the client
        return response.create_response("Temperature value is added successfully")
    elif(request.method == 'PUT'):
        pass
    elif(request.method == 'DELETE'):
        pass

@server.route("/ldr", methods = {'GET', 'POST', 'PUT', 'DELETE'})
def ldr_methods():
    if (request.method == 'GET'):
        # to get data from database form a query
        query = f"select * from sensorsLog;"

        # execute query to get all temps from database
        temps = db.execute_select_query(query)

        # return temps into response
        return response.create_response(temps)
    elif(request.method == 'POST'):
        # retrieve data from request body
        value = request.get_json().get('value')
        loc = "kaveri"
        sen = "LDR"

        # insert data into database
        query = f"insert into sensorsLog(location, sensor, value) values(\"{loc}\", \"{sen}\", {value});"
        db.execute_query(query)

        # return some response to the client
        return response.create_response("LDR value is added successfully")
    elif(request.method == 'PUT'):
        pass
    elif(request.method == 'DELETE'):
        pass


# run server
server.run(host="0.0.0.0", port=4000, debug=True)