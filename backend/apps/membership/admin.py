from django.contrib import admin

# Register your models here.
from .models import CoopMember, Coop

@admin.register(CoopMember)
class CoopMemberadmin(admin.ModelAdmin):
    change_list_template = 'admin/change_list.html'

@admin.register(Coop)
class Coop(admin.ModelAdmin):
    pass
