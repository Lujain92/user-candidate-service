from uuid import UUID
from pydantic import BaseModel

class UserBase(BaseModel):
    """
    Base model for User without ID.

    Attributes:
        first_name (str): The user's first name.
        last_name (str): The user's last name.
        email (str): The user's email address.
    """

    first_name: str
    last_name: str
    email: str

class User(UserBase):
    """
    Model for User including ID.

    Inherits:
        UserBase: Base model for User without ID.

    Attributes:
        id (UUID): Unique identifier for the user.
    """

    id: UUID
