from django.contrib import admin
from .models import *

class BookAdmin(admin.ModelAdmin):
    pass
admin.site.register(Book)
class StudentAdmin(admin.ModelAdmin):
    pass
admin.site.register(Student)
class IssuedBook(admin.ModelAdmin):
    pass
admin.site.register(IssuedBook)