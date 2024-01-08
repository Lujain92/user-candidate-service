from uuid import UUID
from enum import Enum
from typing import List
from pydantic import BaseModel

class Gender(str, Enum):
    """
    Enumeration representing different genders.

    Attributes:
        male (str): Male gender.
        female (str): Female gender.
        not_specified (str): Gender not specified.
    """
    male = 'male'
    female = 'female'
    not_specified = 'Not Specified'

class CandidateBase(BaseModel):
    """
    Base model for Candidate without ID.

    Attributes:
        first_name (str): The candidate's first name.
        last_name (str): The candidate's last name.
        email (str): The candidate's email address.
        career_level (str): The career level of the candidate.
        job_major (str): The major area of the candidate's job.
        years_of_experience (int): Number of years of experience.
        degree_type (str): The type of degree the candidate holds.
        skills (List[str]): List of skills possessed by the candidate.
        nationality (str): The candidate's nationality.
        city (str): The city where the candidate is located.
        salary (float): The candidate's salary expectation.
        gender (List[str]): List of genders associated with the candidate.
    """

    first_name: str
    last_name: str
    email: str
    career_level: str
    job_major: str
    years_of_experience: int
    degree_type: str
    skills: List[str]
    nationality: str
    city: str
    salary: float
    gender: Gender

class Candidate(CandidateBase):
    """
    Model for Candidate including ID.

    Inherits:
        CandidateBase: Base model for Candidate without ID.

    Attributes:
        id (UUID): Unique identifier for the candidate.
    """

    id: UUID
