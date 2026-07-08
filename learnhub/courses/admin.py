from django.contrib import admin

# Register your models here.


from .models import Enrollment, DemoClassRequest, StudentQuestion


admin.site.register(Enrollment)
admin.site.register(DemoClassRequest)
admin.site.register(StudentQuestion)