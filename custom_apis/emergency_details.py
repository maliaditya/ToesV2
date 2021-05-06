from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authapp.models import (
    EmergencyDetails
)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def emergency(request, user_id):
    try:
        info = EmergencyDetails.objects.get(user=user_id)
        data = {
            "id": info.id,
            "emergency_contact": info.contact_no
        }
        return Response(data=data, status=200)

    except:

        EmergencyDetails(contact_no='0000000000', user=user_id).save()
        info = EmergencyDetails.objects.get(user=user_id)
        data = {
            "id": info.id,
            "emergency_contact": info.contact_no
        }
        return Response(data=data, status=200)
