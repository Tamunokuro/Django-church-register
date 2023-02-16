from django.db.models import fields
from rest_framework import serializers
from .models import *


class AttendanceSerializer(serializers.ModelSerializer):
    class Meta:
        model = MemberRecord
        fields = "__all__"
