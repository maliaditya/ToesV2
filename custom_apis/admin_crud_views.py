from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from authapp.models import User


# RESPONSES
@api_view(['GET'])
@permission_classes([IsAuthenticated])
def block(request, st, user_id):
    User.objects.filter(id=user_id).update(isblocked=st)
    return Response(data={"message": "user blocked success"}, status=status.HTTP_200_OK)


@api_view(['GET'])
@permission_classes([IsAuthenticated])
def delete1(request, user_id):
    User.objects.filter(id=user_id).delete()
    return Response(status=status.HTTP_200_OK)
