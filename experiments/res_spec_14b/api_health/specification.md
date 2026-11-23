# Specification

## Objective
Implement a GET route `/health` in the `app.py` file that returns a status code of 200 and a response body containing `{"status": "ok"}`. Ensure that existing routes continue to function as before and unknown paths still return a 404 status code.

## Parameters / Requirements
- **File**: `app.py`
- **Route**: `/health`
- **HTTP Method**: GET
- **Response Status Code**: 200
- **Response Body**: JSON object with key-value pair `{"status": "ok"}`
- **Existing Routes**: Must remain functional without any changes to their behavior.
- **Unknown Routes**: Should continue returning a 404 status code.

## Acceptance Criteria
1. When accessing `/health` via GET method, the server should respond with HTTP status code 200.
2. The response body must be a JSON object containing exactly one key-value pair: `{"status": "ok"}`.
3. All existing routes in `app.py` should continue to work as intended.
4. Any request to an undefined or unknown route should result in a 404 status code being returned.