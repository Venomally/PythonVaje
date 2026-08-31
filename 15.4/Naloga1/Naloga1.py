from flask import Flask, request
import json

# '''
# Define a route using the @app.route decorator.
# Use the request object to access data like the request
# method (GET, POST, etc.) or form data.
# Use the json library to decode incoming JSON data or encode 
# Python data into JSON format.
# Write logic to handle the request and generate a response, 
# potentially using the jsonify function 
# from Flask to return JSON data.
# '''

# #The __name__ (__main__ usually)  helps Flask identify where 
# #to locate resources like templates or static files. 
# app = Flask(__name__)

# '''
# common HTTP methods:
# GET
# POST
# PUT
# PATCH
# DELETE
# HEAD
# OPTIONS
# TRACE
# '''

# '''
# POST: This method is primarily used to create new resources on the server.
#                                                                                               cause side effects on the server, such as submitting a form or uploading a file.
# PUT: This method is specifically used for creating or replacing a 
# resource at a specified URL. The data sent in the
# request body represents the complete state of the resource.
# '''
# #requests.get('http://127.0.0.1:1234/welcome')
# @app.route('/1', methods=['GET', 'POST'])
# def welcome():
#     if request.method == 'GET':
#         #html!
#         return '<h1>Welcome! You used GET</h1>'
#     if request.method == 'POST':
#         return '<h1>Welcome!You used POST</h1>'

# '''
# request.data: This part accesses the data attribute of the
# request object in Flask. The request object holds information about 
# the current HTTP request being processed by your application.
# The data attribute specifically refers to the
# raw bytes that were sent in the request body.
# '''

# '''
# .decode(): This method attempts to convert the raw bytes (request.data) 
# into a human-readable string format. However, for this to work correctly,
# you need to specify the character encoding 
# used to represent the text data in those bytes.
# '''
# @app.route('/postjson', methods=['POST'])
# def putjson():
#     try:
#         data = json.loads(request.data)
#         print(data)
#         return 'Hvala za JSON. Ima %i vrednosti.' % len(data)
#     except:
#         print(request.data)
#         return 'To ni bil JSON'
# #notice the difference in route and function name!    
# @app.route('/puttext', methods=['POST'])
# def putstring():
#     try:
#         data = request.data.decode()
#         print(data)
#         return 'Hvala za text. Je dolžine %i.' % len(data)
#     except:
#         print(request.data)
#         return 'To ni bil text'    

# #use_reloader=False: This argument controls whether the
# #development server will automatically reload your application code
# #when you make changes to the Python files. 
# app.run(host='127.0.0.1',debug=True, port=1234, use_reloader=False)
app = Flask(__name__)


@app.route('/1', methods=['GET', 'POST'])
def info():
    return "Ovo je informativna stranica sistema"
@app.route('/2', methods =['GET','POST'])
def send_text():
    text = request.data.decode('utf-8')
    print('Primljeni text: {text}')
    return f"Uspjesno primljen tekst duzine {len(text)} znakova"
@app.route('/3', methods = ['POST'])
def send_json():
    podaci = request.get_json()
    print(f"Primljen JSON: {podaci}")
    return f"JSON uspjesno primljen. Sadrzaj {len(podaci)} kljuceva."

if __name__ == '__main__':
    app.run(host='127.0.0.1', port=5000, debug=True)

