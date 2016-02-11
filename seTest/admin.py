from django.contrib import admin
from seTest.models import State


class StateAdmin(admin.ModelAdmin):
    pass

admin.site.register(State, StateAdmin)
