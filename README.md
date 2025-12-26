## Overview

<p>This project is a Django-based microservice responsible for enforcing task overdue and status transition rules for a Task & Project Management System.
The service is stateless and does not manage any database records.
Its only responsibility is to validate whether a task status change is allowed.
All business rules are enforced here to ensure they cannot be bypassed, even if frontend or backend APIs are manipulated.</p>

## Business Rules Enforced

- Tasks past their due date and not marked as DONE become OVERDUE.
- OVERDUE tasks cannot move back to IN_PROGRESS.
- Only Admin can move an OVERDUE task to DONE.
- Rules apply regardless of frontend or backend logic.

## Tech Stack

- Python 3.x
- Django
- Django REST Framework
- Stateless REST API
- No database dependency

## Installation & Setup
``` bash
  python -m venv venv
source venv/bin/activate      # Mac/Linux
venv\Scripts\activate         # Windows
pip install -r requirements.txt  (Django
djangorestframework)

```


Register Apps:
settings.py


## API Endpoint
- POST /api/validate/

- Validates whether a task status change is allowed.

- payload{
  "current_status": "TODO",
  "new_status": "IN_PROGRESS",
  "due_date": "2024-01-01",
  "role": "user"

}

Response (Blocked)
{
  "valid": false,
  "message": "Overdue task cannot move back to In Progress"
}


Response (Allowed)
{
  "valid": true,
  "message": "Allowed"
}



## Rule Logic (High Level)

- Determines if task is overdue using current date
- Applies rule validation based on:
- Current status
- New requested status
- Due date
- User role
- Returns decision to calling backend (Laravel)

## Security Notes

- This service is not publicly exposed to frontend
- Called only by trusted backend (Laravel)
- No authentication required (internal service)

## Deployment

- Hosted as a Web Service on Render
- Stateless → easily scalable
- No database migrations required

## Why This Design?

- Clean separation of concerns
 - Centralized business rules
- Backend-level enforcement
- Microservice-ready
- Easily extensible
