from flask_restx import fields

from app.extensions import api


class ValidateUserRequest:
    api_model = api.model("ValidateUserRequest", {
        "dni": fields.String(required=True, description="The user DNI")
    })
