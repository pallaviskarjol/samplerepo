from django.contrib import admin
#from home.models import Student
from .models import * 

#from .models import Student
#from account.models import AccInfo

# Register your models here.

'''admin.site.register(Student)
admin.site.register(details)
admin.site.register(link)
admin.site.register(Department)
admin.site.register(Section)
admin.site.register(Employee)
'''

@admin.register(Student)
class StudentAdmin(admin.ModelAdmin):
	search_fields = ('name','id')
	list_filter = ('name','id')
	fields = ('name','Branch')

@admin.register(details)
class detailsAdmin(admin.ModelAdmin):
	search_fields = ('id','USN')
	list_filter = ('id','USN')
	fields = ('USN','name','sem','dob','cgpa')

@admin.register(link)
class linkAdmin(admin.ModelAdmin):
	pass


@admin.register(Department)
class DepartmentAdmin(admin.ModelAdmin):
	pass


@admin.register(Section)
class SectionAdmin(admin.ModelAdmin):
	pass



@admin.register(Employee)
class EmployeeAdmin(admin.ModelAdmin):
	pass


