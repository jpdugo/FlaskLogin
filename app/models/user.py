from dataclasses import dataclass

@dataclass
class User:
    dni: str
    username: str
    lastname: str
    status: str
    
    