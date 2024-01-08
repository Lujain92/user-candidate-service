import os
import csv
from uuid import uuid4
from fastapi import HTTPException
from controllers.models.candidate import Candidate
from utils.database import candidate_collection
from utils.database import user_collection

async def get(user, search_query):
    """
    Retrieve candidates from the database.

    Args:
        user: User object for authentication.
        search_query (str): Optional search query.

    Returns:
        list: A list of Candidate objects.

    Raises:
        HTTPException: If user is unauthorized (HTTP 401).
    """
    found_user = user_collection.find_one(user.dict())
    if not found_user:
        raise HTTPException(status_code=401, detail='Unauthorized user')

    query = {}

    if search_query:
        query['$or'] = [
            {field: {'$regex': search_query, '$options': 'i'}}
            for field in Candidate.model_fields.keys()
        ]

    candidates = []
    for candidate in candidate_collection.find(query):
        candidates.append(Candidate(**candidate))
    return candidates

async def generate(user):
    """
    Generate a CSV report for candidates.

    Args:
        user: User object for authentication.

    Returns:
        dict: Message confirming successful report generation.

    Raises:
        HTTPException: If user is unauthorized (HTTP 401).
    """
    found_user = user_collection.find_one(user.dict())
    if not found_user:
        raise HTTPException(status_code=401, detail='Unauthorized user')

    candidates = list(candidate_collection.find())

    fieldnames = list(Candidate.model_fields.keys())

    base_dir = os.path.dirname(os.path.realpath(__file__))
    report_path = os.path.join(base_dir, 'candidates_report.csv')

    with open(report_path, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.DictWriter(file, fieldnames=fieldnames)
        writer.writeheader()
        for candidate in candidates:
            candidate_dict = candidate.copy()
            del candidate_dict['_id']
            candidate_dict['id'] = str(candidate_dict['id'])
            writer.writerow(candidate_dict)

    return {'message': 'Report generated successfully'}

async def post(candidate):
    """
    Add a new candidate to the database.

    Args:
        candidate: Candidate object to be added.

    Returns:
        Candidate: The created Candidate object.
    """
    new_candidate = candidate.dict()
    new_candidate['id'] = uuid4()
    candidate_collection.insert_one(new_candidate)
    response = Candidate(**new_candidate)

    return response

async def get_by_id(id):
    """
    Retrieve a candidate by ID from the database.

    Args:
        id: ID of the candidate to retrieve.

    Returns:
        dict: Candidate information if found.

    Raises:
        HTTPException: If candidate is not found (HTTP 404).
    """
    candidate = candidate_collection.find_one({'id': id})
    if candidate:
        return candidate

    raise HTTPException(status_code=404, detail='Candidate not found')

async def delete(id):
    """
    Delete a candidate by ID from the database.

    Args:
        id: ID of the candidate to delete.

    Returns:
        dict: Message confirming successful deletion.

    Raises:
        HTTPException: If candidate is not found (HTTP 404).
    """
    existing_candidate = candidate_collection.find_one({'id': id})
    if existing_candidate:
        candidate_collection.delete_one({'id': id})
        return {'message': 'Candidate Deleted successfully'}

    raise HTTPException(status_code=404, detail='Candidate not found')

async def update(id, updated_candidate):
    """
    Update a candidate's information in the database.

    Args:
        id: ID of the candidate to update.
        updated_candidate: Updated Candidate object.

    Returns:
        dict: Message confirming successful update.

    Raises:
        HTTPException: If candidate is not found (HTTP 404).
    """
    existing_candidate = candidate_collection.find_one({'id': id})
    if existing_candidate:
        candidate_collection.update_one({'id': id}, {'$set': updated_candidate.dict()})
        return {'message': 'Candidate updated successfully'}

    raise HTTPException(status_code=404, detail='Candidate not found')
