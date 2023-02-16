from django.http.response import HttpResponse, HttpResponseRedirect
from django.shortcuts import render
from django.urls import reverse
from attendance.models import MemberRecord
from rest_framework.views import APIView
from rest_framework.response import Response


from .models import *
from .serializers import AttendanceSerializer

# Create your views here.


class AttendanceApi(APIView):
    def get(self, request, *args, **kwargs):
        data = {
            'username': 'admin',
            'active_years': 1
        }
        return Response(data)

    def post(self, request, *args, **kwargs):
        serializer = AttendanceSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save(serializer.data)
        else:
            return Response(serializer.errors)


def index(request):
    return render(request, 'attendance/index.html')


def memberForm(request):
    MemberForm = MemberRecord(
        firstname=request.POST['firstName'],
        lastname=request.POST['lastName'],
        address=request.POST['address'],
        gender=request.POST['sex'],
        email=request.POST['email'],
        phonenumber=request.POST['phonenumber'],
        department=request.POST['department'],
        birthday=request.POST['birthday']

    )
    return MemberForm


def submitRecord(request):
    if request.method == "POST":
        member = memberForm(request)
        member.save()

        return HttpResponseRedirect(reverse('index'))
    else:
        return render(request, 'attendance/index.html')
