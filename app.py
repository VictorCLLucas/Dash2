from crypt import methods
from flask import Flask
from flask_restful import Api, Resource

import external_calls as ext


app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET'])
def home():
		xmen = { 
			"data" : """
   =ccccc,      ,cccc       ccccc      ,cccc,  ?$$$$$$$,  ,ccc,   -ccc           
  :::"$$$$bc    $$$$$     ::`$$$$$c,  : $$$$$c`:"$$$$???'`."$$$$c,:`?$$c         
  `::::"?$$$$c,z$$$$F     `:: ?$$$$$c,`:`$$$$$h`:`?$$$,` :::`$$$$$$c,"$$h,       
	`::::."$$$$$$$$$'    ..,,,:"$$$$$$h, ?$$$$$$c`:"$$$$$$$b':"$$$$$$$$$$$c      
		`::::"?$$$$$$    :"$$$$c:`$$$$$$$$d$$$P$$$b`:`?$$$c : ::`?$$c "?$$$$h,   
		  `:::.$$$$$$$c,`::`????":`?$$$E"?$$$$h ?$$$.`:?$$$h..,,,:"$$$,:."?$$$c  
			`: $$$$$$$$$c, ::``  :::"$$$b `"$$$ :"$$$b`:`?$$$$$$$c``?$F `:: "::  
			 .,$$$$$"?$$$$$c,    `:::"$$$$.::"$.:: ?$$$.:.???????" `:::  ` ```   
			' J$$$$P'::"?$$$$h,   `:::`?$$$c`::``:: .:: : :::::''   `            
			:,$$$$$':::::`?$$$$$c,  ::: "::  ::  ` ::'   ``                      
			.'J$$$$F  `::::: .::::    ` :::'  `                                  
		   .: ???):     `:: :::::                                                
		  : :::::'        `                                                      
		   ``
		"""
		}
		resp = app.make_response(xmen)
		resp.headers["Access-Control-Allow-Origin"] = "*"
		return resp


@app.route("/boredapi", methods=['GET'])
def get_bored_api():
	#Get data from http://www.boredapi.com/api/activity
	bored_api_data = ext.get_bored_data()
	#Return the data to the endpoint
	resp = app.make_response(bored_api_data)
	resp.headers["Access-Control-Allow-Origin"] = "*"
	return resp



if __name__ == "__main__":
		app.run(debug=True)
		