from django.urls import path
from . import views
from attendance.views import AttendanceApi
from django.conf.urls import include

urlpatterns = [
    path('', views.index, name='index'),
    path('attendance-data/', AttendanceApi.as_view(), name='attendance-data'),
    path('submitRecord/', views.submitRecord, name='sumbitRecord')

]
