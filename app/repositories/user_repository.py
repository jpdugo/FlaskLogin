from app.database import Database

class UserRepository:
    @staticmethod
    def get_user_status_by_dni(dni):
        connection = Database.get_connection()
        if connection:
            cursor = connection.cursor(dictionary=True)
            cursor.execute("""
                SELECT s.description AS status 
                FROM user u
                LEFT JOIN status s ON u.status_id = s.id
                WHERE u.dni = %s
            """, (dni,))
            result = cursor.fetchone()
            cursor.close()
            if result:
                return result['status']
        return None