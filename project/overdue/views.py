from rest_framework.decorators import api_view
from rest_framework.response import Response
from datetime import datetime, date

@api_view(['POST'])
def validate_task(request):
    """
    Input:
    {
        status: "TODO",
        new_status: "IN_PROGRESS",
        due_date: "2024-01-01",
        role: "user"
    }
    """

    status = request.data.get('status')
    new_status = request.data.get('new_status')
    due_date = request.data.get('due_date')
    role = request.data.get('role')

    due_date = datetime.strptime(due_date, "%Y-%m-%d").date()

    # RULE 1: Past due → OVERDUE
    if due_date < date.today() and status != "DONE":
        status = "OVERDUE"

    # RULE 2: OVERDUE cannot go back
    if status == "OVERDUE" and new_status == "IN_PROGRESS":
        return Response({
            "valid": False,
            "message": "Overdue task cannot move back to IN_PROGRESS"
        })

    # RULE 3: Only admin can close overdue
    if status == "OVERDUE" and new_status == "DONE" and role != "admin":
        return Response({
            "valid": False,
            "message": "Only admin can close overdue tasks"
        })

    return Response({
        "valid": True,
        "final_status": new_status
    })
