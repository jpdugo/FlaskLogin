from app.repositories.user_repository import UserRepository
from app.schemas.dto.validate_user_response import ValidateUserResponse

class UserService:
    @staticmethod
    def validate_user_by_dni(dni):
        status = UserRepository.get_user_status_by_dni(dni)
        if status:
            if status == 'autorizado':
                return ValidateUserResponse('Access granted', 200, {'dni': dni, 'status': status})
            elif status == 'denegado':
                return ValidateUserResponse('Access denied', 403)
        return ValidateUserResponse('User not found', 404)