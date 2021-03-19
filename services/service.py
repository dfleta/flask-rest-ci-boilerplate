# from flask import jsonify, make_response
from flask_restful import fields, marshal_with, abort

from repository.db import DB


class Service():

    resource_fields = {
        'name': fields.String,
        'sell_in': fields.Integer,
        'quality': fields.Integer
    }

    @staticmethod
    # @marshal_with(resource_fields)
    def get_item(name):

        if not name:
            abort(404, message="Es necesario el nombre del item")
        
        item = DB.get_item(name)
        
        if not item:
            abort(404, message="El item {} no existe".format(name))

        return { 'name': item[0], 'sell_in': item[1], 'quality': item[2] }
        # return make_response(jsonify(name=item[0], sell_in=item[1], quality=item[2]))
    
    @staticmethod    
    @marshal_with(resource_fields)
    def get_objeto(name):

        if not name:
            abort(404, message="Es necesario el nombre del item")
        
        item = DB.get_objeto(name)
        
        if not item:
            abort(404, message="El item {} no existe".format(name))

        return item
