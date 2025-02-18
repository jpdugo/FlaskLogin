from flask import request
from flask_restx import Namespace, Resource

from app.schemas.dto.validate_user_request import ValidateUserRequest
from app.services.user_services import UserService

ns = Namespace("users", description="User related operations")

@ns.route("/acceso")
class ValidateUserAccess(Resource):
    @ns.expect(ValidateUserRequest.api_model, validate=True)
    def post(self):
        data = request.json
        dni = data.get("dni")
        response = UserService.validate_user_by_dni(dni)
        return response.to_dict(), response.status_code
