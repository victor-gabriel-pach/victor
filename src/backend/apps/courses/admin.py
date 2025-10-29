from django.contrib import admin
from .models import Course, Module, Unit, ModuleCompletion

admin.site.register(Course)
admin.site.register(Module)
admin.site.register(Unit)
admin.site.register(ModuleCompletion)
