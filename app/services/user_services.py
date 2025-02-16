import jwt
import datetime
from app.repositories.user_repository import UserRepository
from app.schemas.dto.validate_user_response import ValidateUserResponse

class UserService:
    @staticmethod
    def validate_user_by_dni(dni):
        status = UserRepository.get_user_status_by_dni(dni)
        if status:
            if status == 'autorizado':
                payload = {
                    'dni': dni,
                    'status': status,
                    'exp': datetime.datetime.now(tz=datetime.timezone.utc) + datetime.timedelta(hours=1)  # Token expires in 1 hour
                }
                token = jwt.encode(payload, 'your_secret_key', algorithm='HS256')
                return ValidateUserResponse('Access granted', 200, {'dni': dni, 'status': status, 'token': token})
            elif status == 'denegado':
                return ValidateUserResponse('Access denied', 403)
        return ValidateUserResponse('User not found', 404)