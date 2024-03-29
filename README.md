# User-Candidate Service

This project contains several modules and functionalities for managing users and candidates using FastAPI and MongoDB.

### Author : Lujain Al-Jarrah
### Version : 1.0.0

## Table of Contents

- [Introduction](#introduction)
- [Prerequisites](#prerequisites)
- [Usage](#usage)
- [Services](#services)
- [Accessing Services](#accessing-services)
- [Code Structure](#code-structure)
- [API Endpoints](#api-endpoints)
- [Models](#models)
- [Clean Up](#clean-up)
- [Additional Notes](#additional-notes)

## Introduction

This project implements functionalities for managing users and candidates utilizing FastAPI, MongoDB, and Pydantic models. It comprises different modules such as controllers, models, repositories, and utilities, each handling specific aspects of the application.

## Prerequisites

- Docker
- Docker-compose


## Usage
1. Clone this repository.
2. To start the services, use the following command:

```bash
docker-compose up
```
This will build the FastAPI service, set up a MongoDB instance, and launch Mongo Express for database management.

3. Access the API endpoints described below.



## Services

### FastAPI Service

The FastAPI service is configured to run on port `8000`.

#### Environment Variables

The FastAPI service requires environment variables specified in a `.env` file.

### MongoDB Service

The MongoDB service uses the official Mongo image.

#### Configuration

- Username: `user`
- Password: `password`
- Database Storage: A volume named `mongo-data` is used to persist MongoDB data.

### Mongo Express

Mongo Express provides a web-based user interface for managing the MongoDB instance.

#### Configuration

- Username: `user`
- Password: `password`
- URL: [http://localhost:8081](http://localhost:8081)
- MongoDB Connection URL: `mongodb://user:password@mongo:27017/`

## Accessing Services

- FastAPI: [http://localhost:8000](http://localhost:8000)
- Mongo Express: [http://localhost:8081](http://localhost:8081)


## Code Structure

- `controllers`: Contains functions handling API routes and business logic.
- `models`: Pydantic models defining schemas for users and candidates.
- `repositories`: Functions interacting with the MongoDB collections.
- `utils`: Utility modules such as database connection.

## API Endpoints

### Users

- `GET /user`: Retrieve all users.
- `POST /user`: Create a new user.
- `GET /user/{id}`: Retrieve a user by ID.
- `PUT /user/{id}`: Update a user by ID.
- `DELETE /user/{id}`: Delete a user by ID.

### Candidates

- `POST /candidate`: Add a new candidate.
- `GET /candidate`: Retrieve candidates with optional search queries.
- `GET /candidate/{id}`: Retrieve a candidate by ID.
- `PUT /candidate/{id}`: Update a candidate by ID.
- `DELETE /candidate/{id}`: Delete a candidate by ID.
- `GET /candidate/generate-report`: Generate a CSV report for candidates.


### Health

- `GET /health`: Check server health status.
  - **Description:** Endpoint to verify the server's operational status.
  - **Response:** Returns a JSON object containing the server status message.
    ```json
    {
      "Status": "The server is running"
    }
    ```
## Models

### User

- `id`: UUID
- `first_name`: string
- `last_name`: string
- `email`: string

### Candidate

- `id`: UUID
- `first_name`: string
- `last_name`: string
- `email`: string
- ... (other fields as defined in the `controllers.models.candidate` module)

## Clean Up

To stop the services, use the following command:

```bash
docker-compose down
```

This will stop and remove the containers while preserving the data stored in the MongoDB volume.

## Additional Notes

- Ensure no other services are running on the specified ports (FastAPI on `8000`, Mongo Express on `8081`).
- The `Gender` enum provides options for gender representation.

