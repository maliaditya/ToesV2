import random

import requests
from django.core.exceptions import ObjectDoesNotExist
from rest_framework.decorators import api_view, permission_classes
from rest_framework.response import Response

from authapp.models import User
from .models import VerifyOtp


def generateOTP():
    OTP = random.randint(1000, 9999)
    return OTP


@api_view(['GET'])
@permission_classes([])
def send_otp(request, phone):
    try:
        Mobile = User.objects.get(phone=phone)
        otp = generateOTP()
        val = VerifyOtp.objects.filter(phone=phone).exists()
        if val:
            VerifyOtp.objects.filter(phone=phone).update(otp=otp)
        else:
            a = VerifyOtp(phone=phone, otp=otp)
            a.save()

        querystring = {"authorization": "8SxMu8XjX6rpRasOGDY83AoGQzedmJA7wbgGOEgp92XYsWanQBiUx96IIVeU",
                       "sender_id": "FSTSMS", "language": "english", "route": "qt", "numbers": f"{Mobile}",
                       "message": "42422", "variables": "{BB}|{FF}",
                       "variables_values": f"{otp}|http://tcp-api.herokuapp.com/api/otp/"}
        headers = {
            'cache-control': "no-cache"
        }

        url = "https://www.fast2sms.com/dev/bulk"

        response = requests.request("GET", url, headers=headers, params=querystring)
        return Response({"otp": otp}, status=200)  # Just for demonstration

    except ObjectDoesNotExist:
        message = {
            'message': 'Phone Number does exist please enter registered phone number'
        }
        return Response(data=message, status=400)


@api_view(['GET'])
@permission_classes([])
def verify_otp(request, phone, otp):
    mobile = VerifyOtp.objects.get(phone=phone)
    if mobile.otp == otp:
        VerifyOtp.objects.filter(phone=phone).delete()
        return Response("correct", status=200)
    return Response("OTP is wrong", status=400)
