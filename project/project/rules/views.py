from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import date

@api_view(["POST"])
def validate_task(request):
    data = request.data

    current_status = data.get("current_status")
    new_status = data.get("new_status")
    due_date = data.get("due_date")
    role = data.get("role")

    if not all([current_status, new_status, due_date, role]):
        return Response({
            "valid": False,
            "message": "Missing fields"
        }, status=400)

    due = date.fromisoformat(due_date)
    is_overdue = date.today() > due and current_status != "DONE"

    if is_overdue and new_status == "IN_PROGRESS":
        return Response({
            "valid": False,
            "message": "Overdue task cannot move back to In Progress"
        })

    if is_overdue and new_status == "DONE" and role != "admin":
        return Response({
            "valid": False,
            "message": "Only admin can close overdue tasks"
        })

    return Response({
        "valid": True,
        "message": "Allowed"
    })  
