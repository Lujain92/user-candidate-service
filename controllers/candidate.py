from uuid import UUID
from fastapi import APIRouter, Depends
from typing import List, Optional
from .models.candidate import Candidate, CandidateBase
from repositories import candidate
from .models.user import UserBase

candidate_router = APIRouter()

@candidate_router.post('/', response_model=Candidate)
async def create_candidate(new_candidate: CandidateBase):
    """
    Create a new candidate.

    Args:
        new_candidate (CandidateBase): CandidateBase object containing candidate information.

    Returns:
        Candidate: The created Candidate object.
    """
    result = await candidate.post(new_candidate)
    return result

@candidate_router.get('/all', response_model=List[Candidate])
async def get_all_candidates(
    user: UserBase = Depends(), search_query: Optional[str] = None
):
    """
    Retrieve all candidates.

    Args:
        user (User): User object for authentication.
        search_query (Optional[str]): Optional search query.

    Returns:
        List[Candidate]: A list of Candidate objects.
    """
    result = await candidate.get(user, search_query)
    return result

@candidate_router.get('/generate-report')
async def generate_report(user: UserBase = Depends()):
    """
    Generate a report for candidates.

    Args:
        user (User): User object for authentication.

    Returns:
        [type]: The generated report.
    """
    result = await candidate.generate(user)
    return result

@candidate_router.get('/{id}', response_model=Candidate)
async def get_candidate(id: UUID):
    """
    Retrieve a candidate by ID.

    Args:
        id (UUID): The UUID of the candidate.

    Returns:
        Candidate: The Candidate object corresponding to the given ID.
    """
    result = await candidate.get_by_id(id)
    return result

@candidate_router.put('/{id}')
async def update_candidate(id: UUID, updated_candidate: CandidateBase):
    """
    Update a candidate's information.

    Args:
        id (UUID): The UUID of the candidate to update.
        updated_candidate (CandidateBase): Updated CandidateBase object with new information.

    Returns:
        [type]: The result of the update operation.
    """
    result = await candidate.update(id, updated_candidate)
    return result

@candidate_router.delete('/{id}')
async def delete_candidate(id: UUID):
    """
    Delete a candidate by ID.

    Args:
        id (UUID): The UUID of the candidate to delete.

    Returns:
        [type]: The result of the delete operation.
    """
    result = await candidate.delete(id)
    return result
