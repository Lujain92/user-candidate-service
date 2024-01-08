from fastapi import FastAPI
from controllers.user import user_router
from controllers.candidate import candidate_router

app = FastAPI()

app.include_router(user_router, tags=['user'], prefix='/user')
app.include_router(candidate_router, tags=['candidate'], prefix='/candidate')

@app.get('/health',tags=['health'])
def check_health():
    """
    Check server health status.

    Returns:
        dict: A dictionary containing the server status message.
    """
    return {'Status': 'The server is running'}


@app.get('/')
def get_root():
    """
    Root endpoint to check if the app is running.
    """
    return 'The app is running'
