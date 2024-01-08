from uuid import UUID
from fastapi import APIRouter
from typing import List
from .models.user import User, UserBase
from repositories import user

user_router = APIRouter()

@user_router.get('/', response_model=List[User])
async def get_all_users():
    """
    Retrieve all users.

    Returns:
        List[User]: A list of User objects.
    """
    result = await user.get()
    return result

@user_router.post('/', response_model=User)
async def create_user(new_user: UserBase):
    """
    Create a new user.

    Args:
        new_user (UserBase): UserBase object containing user information.

    Returns:
        User: The created User object.
    """
    result = await user.post(new_user)
    return result

@user_router.get('/{id}', response_model=User)
async def get_user(id: UUID):
    """
    Retrieve a user by ID.

    Args:
        id (UUID): The UUID of the user.

    Returns:
        User: The User object corresponding to the given ID.
    """
    result = await user.get_by_id(id)
    return result

@user_router.put('/{id}')
async def update_user(id: UUID, updated_user: UserBase):
    """
    Update a user's information.

    Args:
        id (UUID): The UUID of the user to update.
        updated_user (UserBase): Updated UserBase object with new information.

    Returns:
        [type]: The result of the update operation.
    """
    result = await user.update(id, updated_user)
    return result

@user_router.delete('/{id}')
async def delete_user(id: UUID):
    """
    Delete a user by ID.

    Args:
        id (UUID): The UUID of the user to delete.

    Returns:
        [type]: The result of the delete operation.
    """
    result = await user.delete(id)
    return result
