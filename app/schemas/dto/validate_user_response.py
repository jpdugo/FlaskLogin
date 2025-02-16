class ValidateUserResponse:
    def __init__(self, message, status_code, user=None):
        self.message = message
        self.status_code = status_code
        self.user = user

    def to_dict(self):
        response = {
            'message': self.message,
            'status_code': self.status_code
        }
        if self.user:
            response['user'] = self.user
        return response