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
- **Existing Routes**: Must not be affected; they should continue to work as intended.
- **Unknown Paths**: Should continue to return a 404 status code.

## Acceptance Criteria
- The application must include a new route `/health`.
- When the `/health` route is accessed via a GET request, it must return a JSON object with the content `{"status": "ok"}` and a status code of 200.
- All other existing routes must remain functional and unchanged.
- Any request to an undefined or unknown route must result in a 404 status code being returned.
- Automated tests must pass without any failures, confirming that the implementation meets the specified requirements.