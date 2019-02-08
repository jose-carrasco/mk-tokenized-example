from flask_restful import Resource, Api
from flask_httpauth import HTTPBasicAuth
from flask import Blueprint, session
from flask import request, abort
from .models import db, User, Customer
import json


auth = HTTPBasicAuth()
services = Blueprint('services', __name__)

class ErrorFriendlyApi(Api):
    def error_router(self, original_handler, e):
        return super(ErrorFriendlyApi, self).error_router(original_handler, e)

api = ErrorFriendlyApi(services)

@auth.verify_password
def verify(username, password):
    if not (username and password):
        return False
    user = current_user(username)
    if user is not None:
        return user.check_password(password)
    return False

def current_user(username):
    user = User.query.filter_by(username=username).first()
    if not user:
        return None
    return user


class TokenApiRest(Resource):
    @auth.login_required
    def post(self):
        if 'tokenValues' not in request.json:
            abort(400)
        tokens = request.json['tokenValues']
        response_tokens = []
        for token in tokens:
            customer = Customer.query.filter_by(token=token["tokenValue"]).first()
            if customer is not None:
                response_tokens.append({
                    "tokenRequestId" : token["tokenRequestId"],
                    "token" : customer.mobile_number if token["tokenType"] == "MobileNumber" else customer.email
                    })   
        return { "tokens" : response_tokens}, 200


api.add_resource(TokenApiRest, '/api/v1/customer/token')

