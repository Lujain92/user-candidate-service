from uuid import uuid4
from fastapi import HTTPException
from controllers.models.user import User
from utils.database import user_collection

async def get():
    """
    Retrieve all users from the database.

    Returns:
        list: A list of User objects.
    """
    users = []
    for user in user_collection.find({}):
        users.append(User(**user))
    return users

async def post(user):
    """
    Add a new user to the database.

    Args:
        user: User object to be added.

    Returns:
        User: The created User object.
    """
    new_user = user.dict()
    new_user['id'] = uuid4()
    user_collection.insert_one(new_user)
    response = User(**new_user)

    return response

async def get_by_id(id):
    """
    Retrieve a user from the database by ID.

    Args:
        id: ID of the user to retrieve.

    Returns:
        dict: User information if found.

    Raises:
        HTTPException: If user is not found (HTTP 404).
    """
    user = user_collection.find_one({'id': id})
    if user:
        return user

    raise HTTPException(status_code=404, detail='User not found')

async def delete(id):
    """
    Delete a user from the database by ID.

    Args:
        id: ID of the user to delete.

    Returns:
        dict: Message confirming successful deletion.

    Raises:
        HTTPException: If user is not found (HTTP 404).
    """
    existing_user = user_collection.find_one({'id': id})
    if existing_user:
        user_collection.delete_one({'id': id})
        return {'message': 'User Deleted successfully'}

    raise HTTPException(status_code=404, detail='User not found')

async def update(id, updated_user):
    """
    Update a user's information in the database.

    Args:
        id: ID of the user to update.
        updated_user: Updated User object.

    Returns:
        dict: Message confirming successful update.

    Raises:
        HTTPException: If user is not found (HTTP 404).
    """
    existing_user = user_collection.find_one({'id': id})
    if existing_user:
        user_collection.update_one({'id': id}, {'$set': updated_user.dict()})
        return {'message': 'User updated successfully'}

    raise HTTPException(status_code=404, detail='User not found')
