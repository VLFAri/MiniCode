# Specification

## Objective
Implement a GET route `/health` in the `app.py` file that returns a status code of 200 and a response body containing `{"status": "ok"}`. Ensure that all existing routes continue to function as before and unknown paths still return a 404 status code.

## Parameters / Requirements
- **File**: `app.py`
- **Route**: `/health`
- **Method**: GET
- **Response**:
  - Status Code: 200
  - Response Body: `{"status": "ok"}`
- **Existing Routes**: Must remain functional without any changes.
- **Unknown Paths**: Should continue returning a 404 status code.

## Acceptance Criteria
- The application should respond with a status code of 200 when the `/health` endpoint is accessed via a GET request.
- The response body for the `/health` endpoint must be `{"status": "ok"}`.
- All other existing routes should continue to work as intended.
- Accessing an unknown path should result in a 404 status code being returned.