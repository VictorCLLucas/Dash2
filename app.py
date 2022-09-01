from crypt import methods
from urllib import response
from flask import Flask
from flask_restful import Api, Resource

app = Flask(__name__)
api = Api(app)

@app.route('/', methods=['GET'])

def home():
    xmen = r"""
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
    response = app.response_class(headers="Access-Control-Allow-Origin")
    return response


if __name__ == "__main__":
    app.run(debug=True)
    