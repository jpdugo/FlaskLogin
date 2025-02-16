import jwt
import datetime
from app.repositories.user_repository import UserRepository
from app.schemas.dto.validate_user_response import ValidateUserResponse
from app.enums.status_enum import Status
import logging

logger = logging.getLogger(__name__)

class UserService:
    @staticmethod
    def validate_user_by_dni(dni):
        logger.info(f"Intento de acceso de usuario: dni {dni}")
        status = UserRepository.get_user_status_by_dni(dni)
        if status:
            match status:
                case Status.AUTORIZADO.value:
                    token = UserService._generate_jwt_token(dni, status)
                    return ValidateUserResponse('Acceso permitido', 200, {'dni': dni, 'status': status, 'token': token})
                case Status.DENEGADO.value:
                    return ValidateUserResponse('Acceso rechazado', 403)
        return ValidateUserResponse('Error: DNI no encontrado', 404)

    @staticmethod
    def _generate_jwt_token(dni, status):
        payload = {
            'dni': dni,
            'status': status,
            'exp': datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(hours=1)  # Token expires in 1 hour
        }
        token = jwt.encode(payload, 'your_secret_key', algorithm='HS256')
        return token