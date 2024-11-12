from flask import Flask, jsonify
from flask_restful import Api, Resource, reqparse

import db_actions 
from db import create_db
app = Flask(__name__)
api = Api(app)


def row_to_json(restourants: list):
    data = []
    for restourant in restourants:
        data.append({
            "id": restourant.id,
            "owner": restourant.owner,
            "comp_dish": restourant.comp_dish
        })
        
        
        data_responce = jsonify(data)
        data_responce.status_code = 200
        return data_responce
    

class RestorauntAPI(Resource):
    def get(self, id=0):
        if id:
            restourant = db_actions.get_restourant(id)
            if restourant:
                return row_to_json([restourant])
            
            answer = jsonify("")
            answer.status_code = 404
            return answer 
        
        restourants = db_actions.get_restourants()
        return row_to_json(restourants)
    
    
    def restourant(self):
        parser = reqparse.RequestParser()
        parser.add_argument("owner")
        parser.add_argument("comp_dish")
        params = parser.parse_args()
        id = db_actions.add_dish(params.get("owner"), params.get("comp_dish"))
        answer = jsonify(f"Нову інформацію про ресторан додано під id{id}")
        answer.status_code = 200
        return answer
    
    
    def put(self, id):
        parser = reqparse.RequestParser()
        parser.add_argument("owner")
        parser.add_argument("comp_dish")
        params = parser.parse_args()
        answer = db_actions.update_restourant(id, params.get("owner"), params.get("comp_dish"))
        answer = jsonify(answer)
        answer.status_code = 200
        return answer
    
    def delete(self, id):
        answer = db_actions(id)
        answer = jsonify(answer)
        answer.status_code = 200
        return answer

api.add_resource(RestorauntAPI, "/api/restourants/", "/api/restourants/<int:id>")


if __name__ == "__main__":
    create_db()
    app.run(debug=True, port=3001)