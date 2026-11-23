# Specification

## Objective
Implement a GET route `/health` in the `app.py` file that returns a status code of 200 and a response body containing `{"status": "ok"}`. Ensure that all existing routes continue to function as before and unknown paths still return a 404 status code.

## Parameters / Requirements
- **File**: `app.py`
- **Route**: `/health`
- **HTTP Method**: GET
- **Response Body**: JSON object `{"status": "ok"}`
- **Status Code**: 200 OK
- **Existing Routes**: Must remain functional without any changes.
- **Unknown Routes**: Should continue returning a 404 status code.

## Acceptance Criteria
1. When accessing `/health` via GET method, the response should be:
   - Status code: 200
   - Response body: `{"status": "ok"}`

2. All other existing routes in `app.py` should continue to work as expected.

3. Accessing an unknown route should result in a 404 status code being returned.

These criteria can be verified through automated tests that check the HTTP responses for the specified conditions.