# Specification

## Objective
Implement a GET route `/health` in the `app.py` file that returns a status code of 200 and a response body containing `{"status": "ok"}`. Ensure that all existing routes continue to function as before and unknown paths still return a 404 status code.

## Parameters / Requirements
- **File**: `app.py`
- **Route**: `/health`
- **HTTP Method**: GET
- **Response Status Code**: 200
- **Response Body**: JSON object with key-value pair `{"status": "ok"}`
- **Existing Routes**: Must remain functional without any changes.
- **Unknown Routes**: Should continue returning a 404 status code.

## Acceptance Criteria
1. When accessing `/health` via GET method, the server should respond with a status code of 200.
2. The response body must be a JSON object containing `{"status": "ok"}`.
3. All other existing routes in `app.py` should continue to work as intended.
4. Accessing an unknown route should result in a 404 status code being returned.