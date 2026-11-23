# Specification

## Objective
Implement a GET route `/health` in the `app.py` file that returns a status code of 200 and a response body containing `{"status": "ok"}`. Ensure that all existing routes continue to function as before and unknown paths still return a 404 status code.

## Parameters / Requirements
- **File**: `app.py`
- **Route**: `/health`
- **HTTP Method**: GET
- **Response Status Code**: 200
- **Response Body**: JSON object with key-value pair `{"status": "ok"}`
- **Existing Routes**: Must remain functional without any changes to their behavior.
- **Unknown Paths**: Should continue returning a 404 status code.

## Acceptance Criteria
1. When accessing the `/health` route via a GET request, the server should respond with a status code of 200.
2. The response body must be a JSON object containing exactly one key-value pair: `{"status": "ok"}`.
3. All other existing routes in the application should continue to work as intended.
4. Any requests made to non-existent routes should result in a 404 status code being returned.