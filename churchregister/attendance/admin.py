from django.contrib import admin
from import_export.admin import ImportExportModelAdmin
from attendance.models import MemberRecord

# Register your models here.
admin.site.site_header = 'HOC Attendance'
admin.site.index_title = 'HOC Attendance'
admin.site.site_title = 'HOC Attendance'


class MemberRecordAdmin(admin.ModelAdmin):
    list_display = ['firstname', 'lastname', 'address',
                    'gender', 'email', 'phonenumber', 'department', 'birthday', 'added']

    search_fields = ['firstname', 'lastname', 'phonenumber']


admin.site.register(MemberRecord, MemberRecordAdmin)
