from pydantic import BaseModel, constr, ValidationError

class User(BaseModel):
    id: int
    name: str
    password: str
    def valid_password(password):
        if not any(char.isupper() for char in password):
            raise ValidationError("You must use one upper letter!")
        if len(password)<4 or len(password)>15:
            raise ValidationError("Incorrect password lenght!")
        return password